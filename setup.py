#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for pyqode.core
"""
import sys
from setuptools import setup, find_packages


def read_version():
    with open("pyqode/qt/__init__.py") as f:
        lines = f.read().splitlines()
        for l in lines:
            if "__version__" in l:
                return l.split("=")[1].strip().replace(
                    "'", '').replace('"', '')


DESCRIPTION = 'Shim library that wraps PyQt5, PyQt4 and PySide'


def readme():
    if 'bdist_deb' in sys.argv or 'sdist_dsc' in sys.argv:
        return DESCRIPTION
    return str(open('README.rst').read())


setup(
    name='pyqode.qt',
    namespace_packages=['pyqode'],
    version=read_version(),
    packages=[p for p in find_packages() if 'test' not in p],
    keywords=["qt PyQt4 PyQt5 PySide"],
    url='https://github.com/pyQode/pyqode.qt',
    license='MIT',
    author='Colin Duquesnoy',
    author_email='colin.duquesnoy@gmail.com',
    description=DESCRIPTION,
    long_description=readme(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: X11 Applications :: Qt',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Widget Sets'])
