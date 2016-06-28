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
    An collection of usefull decorators for debug
    and time evaluation of functions flow
"""

# stdlib
from functools import wraps


def cache(function):
    """
    Function: cache
    Summary: Decorator used to cache the input->output
    Examples: An fib memoized executes at O(1) time
              instead O(e^n)
    Attributes:
        @param (function): function
    Returns: wrapped function

    TODO: Give support to functions with kwargs
    """

    memory = {}
    miss = object()

    @wraps(function)
    def _wrapper(*args):
        result = memory.get(args, miss)
        if result is miss:
            _wrapper.call += 1
            result = function(*args)
            memory[args] = result
        return result
    _wrapper.call = 0
    return _wrapper
