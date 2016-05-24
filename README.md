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

This project was encouraging a explore the limits of decorators powers in Python, whose, however is not so knew for everyone (mainly the beginners), is a extremely useful feature of the language similar, whose can be similar of Lisp Macros, but without change the AST. The famous examples is the `@animated` and `@writing` decorator. BTW, because is fun too. All the repository is made from scratch, just using the Python `stdlib`, no [dependency](requirements.txt)!

## Installation

**INFO**: we need some people to do support for Python2, only Python3 for now. Check #3

**stable: last release**:
`sudo pip install decorating`


**bleeding-edge**:
`sudo pip install git+https://www.github.com/ryukinix/decorating`

# Usage

Public decorators on the API of decorators `decorating`:

* **debug**
* **cache**
* **counter**
* **count_time**
* **animated**
* **writing**


# Examples

## Animated

*Using as decorator and mixed with context-managers*
![animation](https://i.imgur.com/hjkNvEE.gif)

Well

*Using with nested context-managers*
![context-manager](https://i.imgur.com/EeVnDyy.gif)


## Writing

Another project mine called [MAL](http://www.github.com/ryukinix/mal) whose is a basic command line interface for MyAnimeList, I recently test the features of @writing only adding 3 lines on my code! Check the awesome effect:

[![asciicast](https://asciinema.org/a/ctt1rozymvsqmeipc1zrqhsxb.png)](https://asciinema.org/a/ctt1rozymvsqmeipc1zrqhsxb)


#### Developers

```Bash
sudo git clone https://www.github.com/ryukinix/decorating
cd decorating
sudo make develop
```

The develop mode creates a .egg-info (egg-link) as symlink with your standard `site-packages`/`dist-packages` directory. Don't be worry with the `decorating.egg-info`, is only information for the package egg to link with your `PYTHONPATH`. For that, the usage is dynamic, you can modify the code in test on the command line always using absolute imports in anywhere (like the first example)

### Contributing

Avoid I blame you. You maybe don't will like that. I'm not Linus, but I can really do heavy critiques sometimes.[/lain ]. Although I'm joking, keep your life more easy, so setup the `pre-commit` after clone!

In the root of git repository, do that commands:
```
sudo pip install pre-commit pylint nose2
pre-commit install
```

If you don't know about pre-commit, check [pre-commit](http://pre-commit.com) website.

Now you can create a new branch `git checkout -b feature` based on the `master` (or other you wants improves, like `dev`) and send a pull-request for me!

If you just wants know something, I give a suggestion, create a new issue! I'll happy with it.

## License
[![PyPi License](https://img.shields.io/pypi/l/decorating.svg)](https://pypi.python.org/pypi/decorating/)

MIT

Because good things need be free.
