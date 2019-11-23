# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='jsonty',
    version='0.0.1',
    description='Automatic custom class JSON serialization and deserialization',
    long_description=readme,
    long_description_content_type="text/markdown",
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

