##!/usr/bin/env python
from setuptools import setup

setup(
    name='rngtool',
    version='1.0',
    author='Ayub Farah',
    author_email='razortyphon@gmail.com',
    description='Quick random number generating tool for Linux',
    packages='packages.txt',
    url='https://github.com/ayubf/rngtool',
    license='MIT',
    scripts=['bin/rngtool.py'],
    entry_points = {
        'console_scripts' : ['rngtool=rngtool:main']
    }
)
