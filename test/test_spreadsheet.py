#!/usr/bin/env python3

import unittest
import os
import conscommon.spreadsheet.parser as spreadsheet_parser


class TestDataModel(unittest.TestCase):
    def test_spreadsheetParser(self):
        spreadsheet_path = "./Redes e Beaglebones.xlsx"
        self.assertIs(os.path.exists(spreadsheet_path), True)
        spreadsheet_parser.loadSheets(spreadsheet_path)


if __name__ == "__main__":
    unittest.main()
