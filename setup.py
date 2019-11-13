# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="PyGrouper",
    version="0.1",
    description=(
        "Function that parses ISO-formated datetime strings, naive datetimes and "
        "aware datetimes into an aware datetime"
    ),
    author="P. Scott DeVos",
    author_email="scott@bintouch.org",
    license="BSD 4-Clause",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=["pytz", "python_dateutil", "iso8601"],
    keywords="UUID uuid human readable",
    url="https://github.com/pscottdevos/pyparse_datetime",
)
