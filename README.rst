========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |github-actions| |codecov|
    * - package
      - |version| |wheel| |supported-versions| |supported-implementations| |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-copyq-lib/badge/?style=flat
    :target: https://readthedocs.org/projects/python-copyq-lib/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/weijia/python-copyq-lib/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/weijia/python-copyq-lib/actions

.. |codecov| image:: https://codecov.io/gh/weijia/python-copyq-lib/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://app.codecov.io/github/weijia/python-copyq-lib

.. |version| image:: https://img.shields.io/pypi/v/copyq-lib.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/copyq-lib

.. |wheel| image:: https://img.shields.io/pypi/wheel/copyq-lib.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/copyq-lib

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/copyq-lib.svg
    :alt: Supported versions
    :target: https://pypi.org/project/copyq-lib

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/copyq-lib.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/copyq-lib

.. |commits-since| image:: https://img.shields.io/github/commits-since/weijia/python-copyq-lib/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/weijia/python-copyq-lib/compare/v0.0.0...main



.. end-badges

Collection of copyq functions

* Free software: BSD 2-Clause License

Installation
============

::

    pip install copyq-lib

You can also install the in-development version with::

    pip install https://github.com/weijia/python-copyq-lib/archive/main.zip


Documentation
=============


https://python-copyq-lib.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
