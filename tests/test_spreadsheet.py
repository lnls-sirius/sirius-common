#!/usr/bin/env python3

import os
import unittest

import siriuscommon.devices.spreadsheet.parser as spreadsheet_parser
from siriuscommon.devices.spreadsheet import SheetName


class TestDataModel(unittest.TestCase):
    def test_sheet_name_enum(self):
        COUNTING_PRU = "PVs Counting PRU"
        AGILENT = "PVs Agilent 4UHV"
        MBTEMP = "PVs MBTemp"
        MKS = "PVs MKS937b"
        SPIXCONV = "PVs SPIxCONV"

        self.assertTrue(AGILENT == SheetName.AGILENT)
        self.assertTrue(COUNTING_PRU == SheetName.COUNTING_PRU)
        self.assertTrue(MBTEMP == SheetName.MBTEMP)
        self.assertTrue(MKS == SheetName.MKS)
        self.assertTrue(SPIXCONV == SheetName.SPIXCONV)

        self.assertTrue(SheetName.has_sheet("AgiLenT"))
        self.assertFalse(SheetName.has_sheet(" Agi Le nT "))
        self.assertFalse(SheetName.has_sheet({}))
        self.assertFalse(SheetName.has_sheet(None))

        self.assertTrue(SheetName.AGILENT in SheetName)

    def test_spreadsheetParser(self):
        spreadsheet_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "Redes e Beaglebones.xlsx"
        )
        self.assertIs(os.path.exists(spreadsheet_path), True)
        data = spreadsheet_parser.loadSheets(spreadsheet_path)

        self.assertIsNot(data[SheetName.AGILENT].__len__(), 0)
        self.assertIsNot(data[SheetName.MKS].__len__(), 0)
        self.assertIsNot(data[SheetName.MBTEMP].__len__(), 0)


if __name__ == "__main__":
    unittest.main()
