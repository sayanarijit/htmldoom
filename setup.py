# -*- coding: utf-8 -*-
from os import path

from setuptools import find_packages, setup
from htmldoom import (
    __author__,
    __description__,
    __email__,
    __homepage__,
    __license__,
    __version__,
)

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="htmldoom",
    version=__version__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__homepage__,
    author=__author__,
    author_email=__email__,
    license=__license__,
    py_modules=["htmldoom"],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
        "Topic :: Software Development",
        "Operating System :: MacOS",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft",
    ],
    platforms=["Any"],
    keywords="html dom builder",
    packages=find_packages(exclude=["contrib", "docs", "tests", "examples", "benchmark"]),
    install_requires=[],
    extras_require={"testing": ["pytest>=4.4.1", "pytest-cov>=2.7.1", "black>=19.3b0"]},
)
