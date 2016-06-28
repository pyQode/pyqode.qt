Change log
==========

2.10.0
------

- update version to follow the pyqode master version (no other changes)


2.9.0
-----

- update version to follow the pyqode master version (no other changes)


2.8.0
-----

- add support for importing Qt Web widgets (either from QtWebKit or from QtWebEngine)

2.7.0
-----

- update version to follow the pyqode master version (no other changes)

2.6.0
-----

- update version to follow the pyqode master version (no other changes except
  the support for stdeb and bdist_wheel)

2.5.0
-----

- update version to follow the pyqode master version (no other changes)

2.4.1
-----

- add support for multiple qt api names: e.g. pyqt can now be used as well as pyqt4 to force the use of PyQt4
  this improves compatiblity with IPython
- fix a bug with pyside imports
- improve auto-detection of available qt backend

2.4.0
-----

- fix missing call to setup_apiv2 when using pyqt4 + python2 and QT_API has
  already been set
- fix a similar issue with pyqt5

1.1.0
-----

New features:
    - Add support for python 2

1.0.1
-----

Fixed bugs:
    - Add missing QComboBox class in the sphinx section, needed to build doc on
      readthedocs.

1.0.0
-----

Initial release, API extracted from `pyqode.core.qt` which is now deprecated.
