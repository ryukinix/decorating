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
from __future__ import unicode_literals

from functools import wraps
from time import time


def debug(function):
    """
    Function: debug
    Summary: decorator to debug a function
    Examples: at the execution of the function wrapped,
              the decorator will allows to print the
              input and output of each execution
    Attributes:
        @param (function): function
    Returns: wrapped function
    """

    @wraps(function)
    def _wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        for key, value in kwargs.items():
            args += tuple(['{}={!r}'.format(key, value)])
        if len(args) == 1:
            args = '({})'.format(args[0])
        print('@{0}{1} -> {2}'.format(function.__name__, args, result))
        _wrapper.last_output = [function.__name__, str(args), result]
        return result
    _wrapper.last_output = []
    return _wrapper


def counter(function):
    """
    Function: counter
    Summary: Decorator to count the number of a function is executed each time
    Examples: You can use that to had a progress of heally heavy
              computation without progress feedback
    Attributes:
        @param (function): function
    Returns: wrapped function
    """

    @wraps(function)
    def _wrapper(*args, **kwargs):
        _wrapper.count += 1
        res = function(*args, **kwargs)
        funcname = function.__name__
        count = _wrapper.count
        print("{} has been used: {}x".format(funcname, count))
        return res
    _wrapper.count = 0
    return _wrapper


def count_time(function):
    """
    Function: count_time
    Summary: get the time to finish a function
             print at the end that time to stdout
    Examples: <NONE>
    Attributes:
        @param (function): function
    Returns: wrapped function
    """
    @wraps(function)
    def _wrapper(*args, **kwargs):
        before = time()
        result = function(*args, **kwargs)
        diff = time() - before
        funcname = function.__name__
        print("{!r} func leave it {:.2f} ms to finish".format(funcname, diff))
        _wrapper.time = diff
        return result

    _wrapper.time = 0
    return _wrapper
