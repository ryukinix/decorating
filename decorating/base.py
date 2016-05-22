#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyright © Manoel Vilela
#
# pylint: disable=no-member
# pylint: disable=too-few-public-methods


"""
    Abstract Classes to do composition by inheterince
    and some other utitities from base clases

    * Stream: Abstract Class for implementation of a Stream

    * Decorator: A base class for creating new decorators

"""

from functools import wraps
from abc import abstractmethod, ABCMeta


class Stream(metaclass=ABCMeta):

    """A base class whose is specify a Stream is

    We need at least a stream on init and a
    message param on write method

    """

    @abstractmethod
    def __init__(self, stream, **kargs):
        pass

    @abstractmethod
    def write(self, message, optional=None):
        """a write method interfacing sys.stdout or sys.stderr"""
        pass


class Decorator(object):

    """Decorator base class to keep easy creating more decorators

    argument: can be empty or a callable object (function or class)
    """

    def __init__(self, argument=None):
        if callable(argument):
            self.decorated = argument
            self.argument = self.decorated.__name__
        else:
            self.decorated = None
            self.argument = argument

    def __call__(self, *args, **kwargs):
        decorated = self.decorated or args[0]

        @wraps(decorated)
        def _wrapper(*args, **kargs):
            if hasattr(self, 'start') and callable(self.start):
                getattr(self, 'start')()
            result = decorated(*args, **kargs)
            if hasattr(self, 'stop') and callable(self.stop):
                getattr(self, 'stop')()
            return result

        # called when decorated with args, so in __call__
        # the first argument is a function
        if any(args) and callable(args[0]):
            return _wrapper

        return _wrapper(*args, **kwargs)

    @property
    def __name__(self):
        # well, for some reason, a underlying bug
        # occurs when a decorator is called without args
        # example:
        #          @debug
        #          @animated
        #          def slow():
        #             sleep(1)
        #
        # if we call this without this method, will throw an exception
        # about doesn't exists method __name__
        return self.decorated.__name__ if self.decorated else ''
