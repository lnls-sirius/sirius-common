import requests as _requests
import typing as _typing

from .types import (
    ArchiverDisconnectedPV,
    ArchiverPausedPV,
    _make_archiver_disconnected_pv,
    _make_archiver_paused_pv,
    _make_archiver_status_pv,
)

_default_base_url = "https://10.0.38.42"


def getCurrentlyDisconnectedPVs(
    base_url: str = _default_base_url,
) -> _typing.List[ArchiverDisconnectedPV]:
    return [
        _make_archiver_disconnected_pv(**pv)
        for pv in _requests.get(
            f"{base_url}/mgmt/bpl/getCurrentlyDisconnectedPVs", verify=False
        ).json()
    ]


def getPausedPVsReport(
    base_url: str = _default_base_url,
) -> _typing.List[ArchiverPausedPV]:
    return [
        _make_archiver_paused_pv(**pv)
        for pv in _requests.get(
            f"{base_url}/mgmt/bpl/getPausedPVsReport", verify=False
        ).json()
    ]


def getMatchingPVs(search: str, base_url: str = _default_base_url) -> _typing.List[str]:
    return [
        pv
        for pv in _requests.get(
            f"{base_url}/retrieval/bpl/getMatchingPVs?pv={search}&limit=500",
            verify=False,
        ).json()
    ]


def getPVStatus(search: str, base_url: str = _default_base_url):
    return [
        _make_archiver_status_pv(**pv)
        for pv in _requests.get(
            f"{base_url}/mgmt/bpl/getPVStatus?pv={search}&reporttype=short",
            verify=False,
        ).json()
    ]
