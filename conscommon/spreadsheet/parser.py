#!/usr/bin/env python3

from enum import Enum
from typing import Tuple, Iterable, Dict

import pandas
import numpy

from conscommon import get_logger
from conscommon.spreadsheet import SheetName

logger = get_logger("Parser")


def normalizeAgilent(sheet) -> dict:
    return normalize(sheet, ["C1", "C2", "C3", "C4"])


def normalizeMKS(sheet) -> dict:
    return normalize(sheet, ["A1", "A2", "B1", "B2", "C1", "C2"])


def normalize(sheet, ch_names: list) -> dict:
    """ Create a dictionary with the beaglebone IP as keys.  Aka: {ip:[devices ...] ... ipn:[devicesn ... ]} """
    ips = {}
    try:
        for n, row in sheet.iterrows():
            ip = row["IP"]
            if ip not in ips:
                ips[ip] = []
            ip_devices = ips[ip]
            data = {}

            ip_devices.append(data)
            data["enable"] = row["ENABLE"] if type(row["ENABLE"]) is bool else False
            data["prefix"] = row["Dispositivo"]

            info = {}
            info["sector"] = row["Setor"]
            info["serial_id"] = row["RS485 ID"]
            info["rack"] = row["Rack"]
            data["info"] = info

            channels = {}
            num = 0
            for ch_name in ch_names:
                channel = {}
                channel["num"] = num
                channel["prefix"] = row[ch_name]
                channel["enable"] = row[ch_name] != "" or row[ch_name] is None

                info = {}
                info["pressure_hi"] = row["HI " + ch_name]
                info["pressure_hihi"] = row["HIHI " + ch_name]
                if "Sensor " + ch_name in row:
                    info["sensor"] = row["Sensor " + ch_name]
                channel["info"] = info

                channels[ch_name] = channel
                num += 1

            data["channels"] = channels
    except Exception:
        logger.exception("Failed to update data from spreadsheet.")

    logger.info("Loaded data from sheet with {} different IPs.".format(len(ips)))
    return ips

def loadSheet(spreadsheet_xlsx_path: str, sheetName:SheetName) -> dict):
    logger.info('Loading spreadsheet "{}" from url "{}"'.format( spreadsheet_xlsx_path, sheetName.value))
    sheet = pandas.read_excel(spreadsheet_xlsx_path, sheet_name=sheetName.value)
    sheet = sheets[sheetName].replace(numpy.nan, "", regex=True)

    if sheetName == SheetName.AGILENT:
        return normalizeAgilent(sheet)
    elif sheetName == SheetName.MKS:
        return normalizeMKS(sheet)
    else:
        return {}


def loadSheets(spreadsheet_xlsx_path: str) -> Dict[SheetName, dict]:
    data:Dict[SheetName, dict] = {}
    for sheetName in SheetName:
        data[SheetName] = loadSheet(spreadsheet_xlsx_path, sheetName)
    return data
