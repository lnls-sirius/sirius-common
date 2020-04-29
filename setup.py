#!/usr/bin/env python
from setuptools import setup, find_namespace_packages
from conscommon import __version__, __author__

requirements = None
with open("requirements.txt", "r") as _f:
    requirements = _f.readlines()

setup(
    name="siriushlacommon",
    version=__version__,
    author=__author__,
    description="CON Sirius commons",
    packages=find_namespace_packages(include=["conscommon", "conscommon.*"]),
    license="GNU GPLv3",
    include_package_data=True,
    install_requires=requirements,
)
