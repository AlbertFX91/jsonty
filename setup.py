# -*- coding: utf-8 -*-

import io
import re

from setuptools import setup, find_packages


with io.open('README.rst', "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("jsonty/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name='jsonty',
    version=version,
    description='Automatic custom class JSON serialization and deserialization',
    project_urls={
        "Code": "https://github.com/AlbertFX91/jsonty",
    },
    long_description=readme,
    author='Alberto Rojas',
    author_email='alberto.rojas.fndez@gmail.com',
    url='https://github.com/AlbertFX91/jsonty',
    license='BSD-2-Clause',
    packages=find_packages(exclude=('tests', 'docs')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ]
)

