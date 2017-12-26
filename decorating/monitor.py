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
# pylint: disable=C0103
# pylint: disable=too-few-public-methods


from __future__ import unicode_literals
from decorating.stream import Unbuffered
from decorating.decorator import Decorator
import sys


class MonitorStream(Unbuffered):

    def __init__(self, stream):
        self.stream = stream
        self.data = []

    def write(self, message):
        self.stream.write(message)
        self.data.append(message)


class MonitorStdout(Decorator):

    def start(self):
        self.stream = MonitorStream(sys.stdout)
        sys.stdout = self.stream

    def stop(self):
        sys.stdout = sys.__stdout__


monitor_stdout = MonitorStdout()


def test():
    with monitor_stdout:
        print('test')

    print(monitor_stdout.stream.data)
