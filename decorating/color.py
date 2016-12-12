#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#    Copyright © Manoel Vilela 2016
#
#    @project: Decorating
#     @author: Manoel Vilela
#      @email: manoel_vilela@engineer.com
#

"""
    Module focused in termcolor operations

    If the exection is not attatched in any tty,
    so colored is disabled
"""
from __future__ import unicode_literals

import sys

COLORED = True
if not sys.stdout.isatty() or sys.platform == 'win32':
    COLORED = False  # pragma: no cover

COLOR_MAP = {
    'brown': '\033[{style};30m',
    'red': '\033[{style};31m',
    'green': '\033[{style};32m',
    'yellow': '\033[{style};33m',
    'blue': '\033[{style};34m',
    'pink': '\033[{style};35m',
    'cyan': '\033[{style};36m',
    'gray': '\033[{style};37m',
    'white': '\033[{style};40m',
    'reset': '\033[00;00m'
}

STYLE_MAP = {
    'normal': '00',
    'bold': '01',
    'underline': '04',
}


def colorize(printable, color, style='normal', autoreset=True):
    """Colorize some message with ANSI colors specification

    :param printable: interface whose has __str__ or __repr__ method
    :param color: the colors defined in COLOR_MAP to colorize the text
    :style: can be 'normal', 'bold' or 'underline'

    :returns: the 'printable' colorized with style
    """
    if not COLORED:  # disable color
        return printable
    if color not in COLOR_MAP:
        raise RuntimeError('invalid color set, no {}'.format(color))

    return '{color}{printable}{reset}'.format(
        printable=printable,
        color=COLOR_MAP[color].format(style=STYLE_MAP[style]),
        reset=COLOR_MAP['reset'] if autoreset else ''
    )
