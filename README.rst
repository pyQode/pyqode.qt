.. image:: https://raw.githubusercontent.com/pyQode/pyqode.core/master/doc/source/_static/pyqode-banner.png

pyqode.qt
---------

Provides an abstraction layer on top of the various Qt bindings (PyQt5, PyQt4 and PySide).

This package has been extracted from pyqode.core 2.0. 

Basically, it lets you write frameworks or applications that can run on various different Qt backends.

The default layout is the PyQt5 layout (QtGui and QtWidgets have been split into two different modules). 
This means that you write your application as if it was a PyQt5 application, pyqode.qt will then do the matching automatically if another API is used at runtime. 

If you have multiple bindings installed on your system, PyQt5 (or PyQt4) will be used as the default unless told not to do so. You can tell *pyqode.qt* about your preferred bindings by setting up the *QT_API* environment variable. E.g, if you have PyQt5 and PyQt4 installed on your system and want to use PyQt4, just set *QT_API* to *pyqt4*.

**Keep in mind that only the modules/classes needed for pyqode has beeen wrapped**. *You mind find that a specific module or class is missing. In this case, just open an issue or better, submit a pull request.*

License
-------

This project is licensed under the MIT license.


Requirements
------------

You need *PyQt5* or *PyQt4* or *PySide* installed on your system to make use of pyqode.qt, obviously.


Installation
------------
::

  pip install pyqode.qt
