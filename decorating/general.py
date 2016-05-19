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


def debug(fn):
    """
    Function: debug
    Summary: decorator to debug a function
    Examples: at the execution of the function wrapped,
              the decorator will allows to print the
              input and output of each execution
    Attributes:
        @param (fn): function
    Returns: wrapped function
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        for key, value in kwargs.items():
            args += ('='.join(map(str, [key, value])),)
        if len(args) == 1:
            args = '({})'.format(args[0])
        stdout.write('@{0}{1} -> {2}\n'.format(fn.__name__, args, result))
        wrapper.last_output = [fn.__name__, args, result]
        return result
    wrapper.last_output = []
    return wrapper


def counter(func):
    """
    Function: counter
    Summary: Decorator to count the number of a function is executed each time
    Examples: You can use that to had a progress of heally heavy
              computation without progress feedback
    Attributes:
        @param (func): function
    Returns: wrapped function
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        stdout.write("\r{0} has been used: {1}x".format(
            func.__name__, wrapper.count
        )
        )
        stdout.flush()
        return res
    wrapper.count = 0
    return wrapper


def cache(fn):
    """
    Function: cache
    Summary: Decorator used to cache the input->output
    Examples: An fib memoized executes at O(1) time
              instead O(e^n)
    Attributes:
        @param (fn): function
    Returns: wrapped function
    """

    cache = {}
    miss = object()

    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = cache.get(args, miss)
        if result is miss:
            wrapper.call += 1
            result = fn(*args)
            cache[args] = result
        return result
    wrapper.call = 0
    return wrapper


def count_time(fn):
    """
    Function: count_time
    Summary: get the time to finish a function
             print at the end that time to stdout
    Examples: <NONE>
    Attributes:
        @param (fn): function
    Returns: wrapped function
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        before = time()
        result = fn(*args, **kwargs)
        diff = time() - before
        print("{!r} func leave it {:f} ms to finish".format(fn.__name__, diff))
        wrapper.time = diff
        return result

    wrapper.time = 0
    return wrapper
