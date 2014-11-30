Change log
==========

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
