# +
from __future__ import annotations

from setuptools import find_packages, setup

__version__ = "0.1.0"


setup(
    name="cp2kx",
    version=__version__,
    author="Amir Hajibabaei",
    author_email="a.hajibabaei.86@gmail.com",
    description="CP2K input file generator",
    packages=find_packages(),
    python_requires=">=3.9",
    url="https://github.com/amirhajibabaei/cp2kx",
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
    ],
)
