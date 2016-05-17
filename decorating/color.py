#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

COLORED = True

color_map = {
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

style_map = {
    'normal': '00',
    'bold': '01',
    'underline': '04',
}


def colorize(printable, color_selected, style_selected='normal'):
    if not COLORED:  # disable color
        return printable
    style = style_map[style_selected]
    color = color_map[color_selected].format(style=style)
    reset = color_map['reset']
    return '{color}{printable}{reset}'.format_map(locals())
