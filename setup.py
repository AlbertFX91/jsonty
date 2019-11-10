# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='jsonty',
    version='0.0.0',
    description='Automatic custom class JSON serialization/deserialization',
    long_description=readme,
    author='Alberto Rojas',
    author_email='alberto.rojas.fndez@gmail.com',
    url='https://github.com/AlbertFX91/jsonty',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

