Decorating: A Meta Repo To Decorators
=================

[![Build Status](https://travis-ci.org/ryukinix/decorating.svg?branch=master)](https://travis-ci.org/ryukinix/decorating)
[![codecov](https://codecov.io/gh/ryukinix/decorating/branch/master/graph/badge.svg)](https://codecov.io/gh/ryukinix/decorating)
[![Requirements Status](https://requires.io/github/ryukinix/decorating/requirements.svg?branch=master)](https://requires.io/github/ryukinix/decorating/requirements/?branch=master)
[![PyPi version](https://img.shields.io/pypi/v/decorating.svg)](https://pypi.python.org/pypi/decorating/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/decorating.svg)](https://pypi.python.org/pypi/decorating/)
[![PyPI status](https://img.shields.io/pypi/status/decorating.svg)](https://pypi.python.org/pypi/decorating/)
[![HitCount](https://hitt.herokuapp.com/ryukinix/decorating.svg)](https://github.com/ryukinix/decorating)

# Abstract

This project encourages an exploration into the limits of decorators
in `Python`. While decorators might by new to beginners, they are an
extremely useful feature of the language. They can be similar to Lisp
Macros, but without changes to the AST. Great decorators from this
packages are `@animated` and `@writing`. This repository is made from
scratch, just using Python's Standard Library, no dependency!


# Examples

## Animated

*Using as decorator and mixed with context-managers*
![animation](https://i.imgur.com/hjkNvEE.gif)

*Using with nested context-managers*
![context-manager](https://i.imgur.com/EeVnDyy.gif)


## Writing

Another project mine called [MAL] uses the decorating package —-
basically a command line interface for [MyAnimeList]. The decorator
@writing can be used by just adding 3 lines of code! The behavior is a
retro typing-like computer. Check out the awesome effect:

[![asciicast](https://asciinema.org/a/ctt1rozymvsqmeipc1zrqhsxb.png)](https://asciinema.org/a/ctt1rozymvsqmeipc1zrqhsxb)

[MAL]: https://www.github.com/ryukinix/mal
[MyAnimeList]: https://myanimelist.net/

More examples are covered on my personal blog post about [decorating](http://manoel.tk/decorating).

# Decorators & Usage

Currently public decorators on the API of decorators `decorating`:

* **decorating.debug**
* **decorating.cache**
* **decorating.counter**
* **decorating.count_time**
* **decorating.animated**
* **decorating.writing**

Mostly decorators has a pretty consistent usage, but for now only `animated`
and `writing` has support to use as `contextmanagers` using the `with` syntax.

# Installation

Supported Python versions:

* Python3.4+
* Python2.7

You can install the last release on [PyPI] by calling:

```shell
pip install --user decorating
```

If you want get the last development version install directly by the git
repository:

```shell
pip install --user git+https://www.github.com/ryukinix/decorating
```

We have a published package on [Arch Linux],which you can install
using your favorite AUR Helper, like `pacaur` or `yaourt`:

```shell
yaourt -S python-decorating
```

[Arch Linux]: https://aur.archlinux.org/packages/python-decorating/
[PyPI]: https://pypi.python.org/pypi/decorating/

Though since the version `0.6` we have support for Python2.7, an AUR
package for Python2 was not made yet. Fill a issue if you have
interest on that :). Thanks to [Maxim Kuznetsov]
which implemented the necessary changes to make compatible with Python2!

[Maxim Kuznetsov]: https://github.com/mkuznets


## License
[![PyPi License](https://img.shields.io/pypi/l/decorating.svg)](https://pypi.python.org/pypi/decorating/)

[MIT](LICENSE)

Because good things need to be free.
