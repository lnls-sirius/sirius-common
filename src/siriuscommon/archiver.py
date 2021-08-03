import requests as _requests


def getCurrentlyDisconnectedPVs():
    for pv in _requests.get(
        "https://10.0.38.42/mgmt/bpl/getCurrentlyDisconnectedPVs", verify=False
    ).json():
        print(pv["pvName"])


def getPausedPVsReport():
    for pv in _requests.get(
        "https://10.0.38.42/mgmt/bpl/getPausedPVsReport", verify=False
    ).json():
        print(pv["pvName"])


def getMatchingPVs(search: str):
    for pv in _requests.get(
        f"https://10.0.38.42/retrieval/bpl/getMatchingPVs?pv={search}&limit=500",
        verify=False,
    ).json():
        print(pv)


def getPVStatus(search: str):
    for pv in _requests.get(
        f"https://10.0.38.42/mgmt/bpl/getPVStatus?pv={search}&reporttype=short",
        verify=False,
    ).json():
        print(pv)
