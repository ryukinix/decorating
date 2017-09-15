Decorating: A Meta Repo To Decorators
=====================================

|Build Status| |codecov| |Requirements Status| |PyPi version| |PyPI
pyversions| |PyPI status| |HitCount|

Abstract
========

This project encourages an exploration into the limits of decorators in
``Python``. While decorators might by new to beginners, they are an
extremely useful feature of the language. They can be similar to Lisp
Macros, but without changes to the AST. Great decorators from this
packages are ``@animated`` and ``@writing``. This repository is made
from scratch, just using Python's Standard Library, no dependency!

Examples
========

Animated
--------

*Using as decorator and mixed with context-managers* |animation|

*Using with nested context-managers* |context-manager|

Writing
-------

Another project mine called
`MAL <https://www.github.com/ryukinix/mal>`__ uses the decorating
package —- basically a command line interface for
`MyAnimeList <https://myanimelist.net/>`__. The decorator @writing can
be used by just adding 3 lines of code! The behavior is a retro
typing-like computer. Check out the awesome effect:

|asciicast|

More examples are covered on my personal blog post about
`decorating <http://manoel.tk/decorating>`__.

Decorators & Usage
==================

Currently public decorators on the API of decorators ``decorating``:

-  **decorating.debug**
-  **decorating.cache**
-  **decorating.counter**
-  **decorating.count\_time**
-  **decorating.animated**
-  **decorating.writing**

Mostly decorators has a pretty consistent usage, but for now only
``animated`` and ``writing`` has support to use as ``contextmanagers``
using the ``with`` syntax.

Installation
============

Supported Python versions:

-  Python3.4+
-  Python2.7

You can install the last release on
`PyPI <https://pypi.python.org/pypi/decorating/>`__ by calling:

.. code:: shell

    pip install --user decorating

If you want get the last development version install directly by the git
repository:

.. code:: shell

    pip install --user git+https://www.github.com/ryukinix/decorating

We have a published package on `Arch
Linux <https://aur.archlinux.org/packages/python-decorating/>`__,which
you can install using your favorite AUR Helper, like ``pacaur`` or
``yaourt``:

.. code:: shell

    yaourt -S python-decorating

Though since the version ``0.6`` we have support for Python2.7, an AUR
package for Python2 was not made yet. Fill a issue if you have interest
on that :). Thanks to `Maxim Kuznetsov <https://github.com/mkuznets>`
which implemented the necessary changes to make compatible with Python2!

License
-------

|PyPi License|

`MIT <LICENSE>`__

Because good things need to be free.

.. |Build Status| image:: https://travis-ci.org/ryukinix/decorating.svg?branch=master
   :target: https://travis-ci.org/ryukinix/decorating
.. |codecov| image:: https://codecov.io/gh/ryukinix/decorating/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/ryukinix/decorating
.. |Requirements Status| image:: https://requires.io/github/ryukinix/decorating/requirements.svg?branch=master
   :target: https://requires.io/github/ryukinix/decorating/requirements/?branch=master
.. |PyPi version| image:: https://img.shields.io/pypi/v/decorating.svg
   :target: https://pypi.python.org/pypi/decorating/
.. |PyPI pyversions| image:: https://img.shields.io/pypi/pyversions/decorating.svg
   :target: https://pypi.python.org/pypi/decorating/
.. |PyPI status| image:: https://img.shields.io/pypi/status/decorating.svg
   :target: https://pypi.python.org/pypi/decorating/
.. |HitCount| image:: https://hitt.herokuapp.com/ryukinix/decorating.svg
   :target: https://github.com/ryukinix/decorating
.. |animation| image:: https://i.imgur.com/hjkNvEE.gif
.. |context-manager| image:: https://i.imgur.com/EeVnDyy.gif
.. |asciicast| image:: https://asciinema.org/a/ctt1rozymvsqmeipc1zrqhsxb.png
   :target: https://asciinema.org/a/ctt1rozymvsqmeipc1zrqhsxb
.. |PyPi License| image:: https://img.shields.io/pypi/l/decorating.svg
   :target: https://pypi.python.org/pypi/decorating/
