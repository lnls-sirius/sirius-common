#!/usr/bin/env python3

import unittest
import requests
import siriushlacommon.data
import siriushlacommon.data_model
import siriushlacommon.data_model.mks as mks
import siriushlacommon.data_model.agilent as agilent
import siriushlacommon.spreadsheet.parser as spreadsheet_parser


class TestDataModel(unittest.TestCase):
    def setUp(self):
        self.data_mks = siriushlacommon.data.getMKS()
        self.data_agilent = siriushlacommon.data.getAgilent()

    def test_mksDevice(self):
        for device in siriushlacommon.data_model.getDevicesFromBeagles(
            siriushlacommon.data_model.getBeaglesFromList(self.data_mks)
        ):
            self.assertIn(device.enable, [True, False])
            self.assertEqual(device.channels.__len__(), 6)
            self.assertNotEqual(device.info, None)

    def test_mksChannel(self):
        for device in siriushlacommon.data_model.getDevicesFromBeagles(
            siriushlacommon.data_model.getBeaglesFromList(self.data_mks)
        ):
            for channel in device.channels:
                self.assertNotEqual(channel.info, None)
                self.assertIn(channel.name, mks.MKS_CHANNEL_NAMES)
                self.assertIn(
                    channel.info.sensor,
                    [
                        mks.MKS_SENSOR_COLD_CATHODE,
                        mks.MKS_SENSOR_PIRANI,
                        mks.MKS_SENSOR_NOT_USED,
                    ],
                )

    def test_spreadsheetParser(self):
        spreadsheet_parser.loadSheets("Redes e Beaglebones.xlsx")

    def test_agilentDevice(self):
        for device in siriushlacommon.data_model.getDevicesFromBeagles(
            siriushlacommon.data_model.getBeaglesFromList(self.data_agilent)
        ):
            self.assertIn(device.enable, [True, False])
            self.assertEqual(device.channels.__len__(), 4)


if __name__ == "__main__":
    unittest.main()
