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
    DECORATING: A MODULE OF DECORATORS FROM HELL

    You have a collection of decorators, like thesexg:

    * animated: create animations on terminal until the result's returns
    * cache: returns without reprocess if the give input was already processed
    * counter: count the number of times whose the decorated function is called
    * debug: when returns, print this pattern: @function(args) -> result
    * count_time: count the time of the function decorated did need to return
"""

from decorating.animation import animated, writing
from decorating.debugging import count_time, counter, debug
from decorating.general import cache
from decorating.monitor import monitor_stdout

__version__ = '0.6.1'
__author__ = 'Manoel Vilela'
__email__ = 'manoel_vilela@engineer.com'
__url__ = 'https://github.com/ryukinix/decorating'


__all__ = [
    'animated',
    'cache',
    'counter',
    'debug',
    'count_time',
    'writing',
    'monitor_stdout'
]
