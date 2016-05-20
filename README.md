Decorating: A Meta Repo To Decorators
=================

[![Build Status](https://travis-ci.org/ryukinix/decorating.svg?branch=master)](https://travis-ci.org/ryukinix/decorating)
[![codecov](https://codecov.io/gh/ryukinix/decorating/branch/master/graph/badge.svg)](https://codecov.io/gh/ryukinix/decorating)
[![Requirements Status](https://requires.io/github/ryukinix/decorating/requirements.svg?branch=master)](https://requires.io/github/ryukinix/decorating/requirements/?branch=master)
[![PyPi version](https://img.shields.io/pypi/v/decorating.svg)](https://pypi.python.org/pypi/decorating/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/decorating.svg)](https://pypi.python.org/pypi/decorating/)
[![PyPI status](https://img.shields.io/pypi/status/decorating.svg)](https://pypi.python.org/pypi/decorating/)
[![HitCount](https://hitt.herokuapp.com/ryukinix/decorating.svg)](https://github.com/ryukinix/decorating)

# Usage

Collection of decorators, a properly README will be write in soon. For now only we have few functionalities, the main usage is the `@animated` decorator.

## Animated

Using as decorator and mixed with contextmanagers
![animation](https://i.imgur.com/hjkNvEE.gif)

Using with nested contextmanagers
![contextmanager](https://i.imgur.com/EeVnDyy.gif)

## Installation

**WARNING**: This project is still in current development at alpha! Don't use in serious/production application yet.


#### Users

stable:
`sudo pip install decorating`


bleeding-edge:
`sudo pip install git+https://www.github.com/ryukinix/decorating`


#### Developers

```Bash
sudo git clone https://www.github.com/ryukinix/decorating
cd decorating
sudo make develop
```

The develop mode creates a .egg-info (egg-link) as symlink with your standard `site-packages`/`dist-packages` directory. Don't be worry with the `decorating.egg-info`, is only information for the package egg to link with your `PYTHONPATH`. For that, the usage is dynamic, you can modify the code in test on the command line always using absolute imports in anywhere (like the first example)

## License
[![PyPi License](https://img.shields.io/pypi/l/decorating.svg)](https://pypi.python.org/pypi/decorating/)

MIT