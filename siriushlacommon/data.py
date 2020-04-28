#!/usr/bin/env python3
import requests
import logging
from typing import List, Iterable, Tuple

logger = logging.getLogger()
TIMEFMT = "%d/%m/%Y %H:%M:%S"

_DEVICES_URL = "http://10.0.38.42:26001/devices"


def getMKS() -> List[dict]:
    """ MKS json from upstream @return dict following the data_model pattern """
    return requests.get(_DEVICES_URL, verify=False, params={"type": "mks"}).json()


def getAgilent() -> List[dict]:
    """ Agilent json from upstream @return dict following the data_model pattern """
    return requests.get(_DEVICES_URL, verify=False, params={"type": "agilent"}).json()


def getDevicesDict(data: dict) -> Iterable[dict]:
    """ Device generator from json """
    for ip, beagle in data.items():
        for device in beagle:
            yield device


def getChannelsDict(data: dict) -> Iterable[Tuple[str, str, dict]]:
    """ Tuple of (device prefix, channel_name, channel_data) generator from json """
    for ip, beagle in data.items():
        for device in beagle:
            for channel_name, channel_data in device["channels"].items():
                yield device["prefix"], channel_name, channel_data


if __name__ == "__main__":
    # for ip, dev in getAgilent().items():
    data = getAgilent()
    for device, channel_name, channel_data in getChannelsDict(data):
        print(device, channel_name, channel_data["prefix"])
