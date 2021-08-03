Common module for Sirius applications
=====================================
[![Build Status](https://api.travis-ci.org/lnls-sirius/sirius-common.svg)](https://travis-ci.org/lnls-sirius/sirius-common)
![Latest tag](https://img.shields.io/github/tag/lnls-sirius/sirius-common.svg?style=flat)
[![Latest release](https://img.shields.io/github/release/lnls-sirius/sirius-common.svg?style=flat)](https://github.com/lnls-sirius/sirius-common/releases)
[![PyPI version fury.io](https://badge.fury.io/py/siriuscommon.svg)](https://pypi.python.org/pypi/siriuscommon/)

Common features for Sirius scripts.
Available at **PyPi** https://pypi.org/project/siriuscommon/


Data
----
Web API interface.

Data Model
----------
Data model.

Spreadsheet
-----------
XLSX parser, this module should be avoided in favor of the WEB API, usefull in applications that will deal directly with the spreadsheet. Requires `pandas` and `xlrd`.
