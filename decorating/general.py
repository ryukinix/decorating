#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyright © Manoel Vilela
#

"""
    An collection of usefull decorators for debug
    and time evaluation of functions flow
"""

# stdlib
from functools import wraps
from time import time
from sys import stdout


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
            args += ('='.join([str(x) for x in (key, value)]))
        if len(args) == 1:
            args = '({})'.format(args[0])
        print('@{0}{1} -> {2}\n'.format(function.__name__, args, result))
        _wrapper.last_output = [function.__name__, args, result]
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
        msg = "\r{} has been used: {}x".format(function.__name__,
                                               _wrapper.count)
        stdout.write(msg)
        return res
    _wrapper.count = 0
    return _wrapper


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
        print("{!r} func leave it {:.2f} ms to finish".format(
            function.__name__, diff))
        _wrapper.time = diff
        return result

    _wrapper.time = 0
    return _wrapper
