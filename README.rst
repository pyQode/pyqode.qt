.. image:: https://raw.githubusercontent.com/pyQode/pyqode.core/master/doc/source/_static/pyqode-banner.png

About
-----


.. image:: http://img.shields.io/pypi/v/pyqode.qt.png
   :target: https://pypi.python.org/pypi/pyqode.qt/
   :alt: Latest PyPI version

.. image:: http://img.shields.io/pypi/dm/pyqode.qt.png
   :target: https://pypi.python.org/pypi/pyqode.qt/
   :alt: Number of PyPI downloads


**pyqode.qt** is a `shim`_ that let you write libraries/applications that
supports both PyQt and PySide.


We provide support for PyQt5, PyQt4 and PySide using the PyQt5 layout (where
the QtGui module has been split into QtGui and QtWidgets).


Basically, you write your code as if you were using PyQt5 but import qt from
``pyqode.qt`` instead of ``PyQt5``.

- `Issue tracker`_
- `Wiki`_
- `API reference`_
- `Contributing`_
- `Changelog`_


License
-------

This project is licensed under the MIT license.


Requirements
------------

You need *PyQt5* or *PyQt4* or *PySide* installed on your system to make use
of pyqode.qt, obviously.


Installation
------------
::

  pip install pyqode.qt

Testing
-------

pyqode.qt is implicitely tested by pyqode.core


.. _shim: http://en.wikipedia.org/wiki/Shim_%28computing%29
.. _Changelog: https://github.com/pyQode/pyqode.qt/blob/master/CHANGELOG.rst
.. _Contributing: https://github.com/pyQode/pyqode.qt/blob/master/CONTRIBUTING.rst
.. _pyQode: https://github.com/pyQode/pyQode
.. _Issue tracker: https://github.com/pyQode/pyQode/issues
.. _Wiki: https://github.com/pyQode/pyQode/wiki
.. _API reference: http://pyqodeqt.readthedocs.org/en/latest/
