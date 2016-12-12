#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#    Copyright © Manoel Vilela 2016
#
#    @project: Decorating
#     @author: Manoel Vilela
#      @email: manoel_vilela@engineer.com
#
# pylint: disable=redefined-builtin
# pylint: disable=invalid-name

"""
    An collection of usefull decorators for debug
    and time evaluation of functions flow
"""

# stdlib
from functools import wraps
import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3


if PY2:  # pragma: no cover
    from itertools import izip
    zip = izip
else:  # pragma: no cover
    zip = zip


def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    # This requires a bit of explanation: the basic idea is to make a dummy
    # metaclass for one level of class instantiation that replaces itself with
    # the actual metaclass.

    # Copied from `six' library.
    # Copyright (c) 2010-2015 Benjamin Peterson
    # License: MIT

    class metaclass(meta):
        """Dummy metaclass"""
        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)
    return type.__new__(metaclass, 'temporary_class', (), {})


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
