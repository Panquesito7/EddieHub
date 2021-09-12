# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/EddieHub/blob/main/LICENSE

import pathlib
from setuptools import setup, find_packages


def read(file: str) -> list:
    with open(file, encoding="utf-8") as r:
        return [i.strip() for i in r]


file = pathlib.Path(__file__).parent

README = (file / "README.md").read_text()

setup(
    name="EddieHub",
    version="1.1.0",
    author="FayasNoushad",
    long_description=README,
    long_description_content_type="text/markdown",
    description="A EddieHub API python package.",
    license="MIT",
    url="https://github.com/FayasNoushad/EddieHub",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=read("requirements.txt"),
    python_requires=">=3.6"
)
