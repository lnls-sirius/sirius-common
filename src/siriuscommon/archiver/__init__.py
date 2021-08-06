import typing as _typing

import requests as _requests

from .types import (
    ArchiverDisconnectedPV,
    ArchiverPausedPV,
    ArchiverStatusPV,
    _make_archiver_disconnected_pv,
    _make_archiver_paused_pv,
    _make_archiver_status_pv,
)

_default_base_url = "https://10.0.38.42"


class ArchiverLoginException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class ArchiverClient:
    def __init__(
        self,
        base_url: str = _default_base_url,
        username: _typing.Optional[str] = None,
        password: _typing.Optional[str] = None,
    ) -> None:

        self._mgmt_url = f"{base_url}/mgmt/bpl"
        self._retrieval_url = f"{base_url}/retrieval/bpl"
        self._authenticated = False

        self._session: _requests.Session = _requests.Session()

        if username and password:
            self.login(username, password)

    @property
    def authenticated(self):
        return self._authenticated

    def login(self, username: str, password: str):
        data = {"username": username, "password": password}

        response = self._session.post(
            f"{self._mgmt_url}/login", data=data, verify=False
        )
        self._authenticated = (
            response.status_code == 200 and "authenticated" in response.text
        )
        if not self.authenticated:
            raise ArchiverLoginException(f"failed to authenticat user {username}")

    def logout(self):
        raise NotImplementedError()

    def resume_pv(self, pv_name: str) -> bool:
        raise NotImplementedError()

    def delete_pv(self, pv_name: str) -> bool:
        raise NotImplementedError()

    def pause_pv(self, pv_name: str):
        if not self.authenticated:
            raise ArchiverLoginException("operation requires authentication")

        if not pv_name:
            raise ValueError()

        response = self._session.get(f"{self._mgmt_url}/pauseArchivingPV?pv={pv_name}")
        if (
            response.status_code == 200
            and (f"Successfully paused the archiving of PV {pv_name}")
            or (f"PV {pv_name} is already paused") in response.text
        ):
            return True
        return False

    def get_currently_disconnected_pvs(self) -> _typing.List[ArchiverDisconnectedPV]:
        return [
            _make_archiver_disconnected_pv(**pv)
            for pv in _requests.get(
                f"{self._mgmt_url}/getCurrentlyDisconnectedPVs", verify=False
            ).json()
        ]

    def get_paused_pvs_report(self) -> _typing.List[ArchiverPausedPV]:
        return [
            _make_archiver_paused_pv(**pv)
            for pv in _requests.get(
                f"{self._mgmt_url}/getPausedPVsReport", verify=False
            ).json()
        ]

    def get_matching_pvs(self, search: str, limit: int = 500) -> _typing.List[str]:
        return [
            pv
            for pv in _requests.get(
                f"{self._retrieval_url}/getMatchingPVs",
                params={"pv": search, "limit": limit},
                verify=False,
            ).json()
        ]

    def get_pv_status(self, search: str, reporttype: str = "short") -> ArchiverStatusPV:
        return [
            _make_archiver_status_pv(**pv)
            for pv in _requests.get(
                f"{self._mgmt_url}/getPVStatus",
                params={"pv": search, "reporttype": reporttype},
                verify=False,
            ).json()
        ]


def getCurrentlyDisconnectedPVs(
    base_url: str = _default_base_url,
) -> _typing.List[ArchiverDisconnectedPV]:
    return ArchiverClient(base_url=base_url).get_currently_disconnected_pvs()


def getPausedPVsReport(
    base_url: str = _default_base_url,
) -> _typing.List[ArchiverPausedPV]:
    return ArchiverClient(base_url=base_url).get_paused_pvs_report()


def getMatchingPVs(search: str, base_url: str = _default_base_url) -> _typing.List[str]:
    return ArchiverClient(base_url=base_url).get_matching_pvs(search=search)


def getPVStatus(search: str, base_url: str = _default_base_url):
    return ArchiverClient(base_url=base_url).get_pv_status(search=search)
