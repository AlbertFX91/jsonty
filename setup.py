# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='jsonty',
    version='0.0.1',
    description='Automatic custom class JSON serialization and deserialization',
    project_urls={
        "Code": "https://github.com/AlbertFX91/jsonty",
    },
    long_description=readme,
    author='Alberto Rojas',
    author_email='alberto.rojas.fndez@gmail.com',
    url='https://github.com/AlbertFX91/jsonty',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)

