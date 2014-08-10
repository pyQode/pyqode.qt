#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for pyqode.core
"""
from setuptools import setup, find_packages


def read_version():
    with open("pyqode/qt/__init__.py") as f:
        lines = f.read().splitlines()
        for l in lines:
            if "__version__" in l:
                return l.split("=")[1].strip().replace(
                    "'", '').replace('"', '')


def readme():
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
    description='Provides an abstraction layer on top of the various Qt '
                'bindings (PyQt5, PyQt4 and PySide)',
    long_description=readme(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: X11 Applications :: Qt',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Widget Sets'])
