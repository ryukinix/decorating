#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyright © Manoel Vilela
#
#

"""
    DECORATING: A MODULE OF DECORATORS FROM HELL

    You have that collection of decorators:

    * animated: create animations on terminal until the result's returns
    * cache: returns without reprocess if the give input was already processed
    * counter: count the number of times whose the decorated function is called
    * debug: when returns, print this pattern: @function(args) -> result
    * count_time: count the time of the function decorated did need to return
"""

from decorating.animation import animated
from decorating.general import cache, count_time, counter, debug

__version__ = '0.3'
__author__ = 'Manoel Vilela'
__email__ = 'manoel_vilela@engineer.com'
__url__ = 'https://github.com/ryukinix/decorating'


__all__ = [
    'animated',
    'cache',
    'counter',
    'debug',
    'count_time'
]
