#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#    Copyright © Manoel Vilela 2016
#
#    @project: Decorating
#     @author: Manoel Vilela
#      @email: manoel_vilela@engineer.com
#
# pylint: disable=no-member
# pylint: disable=too-few-public-methods


"""
    Abstract Classes to do composition by inheterince
    and some other utitities from base clases

    * Stream: Abstract Class for implementation of a Stream

    * Decorator: Abstract Class for creating new decorators

"""
from __future__ import unicode_literals
from abc import abstractmethod, ABCMeta
from .general import with_metaclass


class Stream(with_metaclass(ABCMeta)):
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


class DecoratorManager(with_metaclass(ABCMeta)):
    """Decorator-Context-Manager base class to keep easy creating more decorators

    argument: can be empty or a callable object (function or class)
    """

    @abstractmethod
    def __call__(self, function):
        """Base class to handle all the implementation of decorators"""
        pass

    @abstractmethod
    def start(self):
        """You active here your pre-fucking crazy feature"""
        pass

    @abstractmethod
    def stop(self):
        """You can deactivate any behavior re-writing your method here"""
        pass

    def __enter__(self):
        """Activated when enter in a context-manager (with keyword)"""
        self.start()

    def __exit__(self, *args):
        """Triggered when exit from a block of context-manager"""
        self.stop()
