from enum import Enum, unique


@unique
class SheetName(Enum):
    AGILENT = "PVs Agilent 4UHV"
    COUNTING_PRU = "PVs Counting PRU"
    MBTEMP = "PVs MBTemp"
    MKS = "PVs MKS937b"
    SPIXCONV = "PVs SPIxCONV"
