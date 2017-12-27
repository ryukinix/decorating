#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#    Copyright © Manoel Vilela 2017
#
#    @project: Decorating
#     @author: Manoel Vilela
#      @email: manoel_vilela@engineer.com
#

"""
    These tests cover the basic usage of the decorator monitor_stdout

"""

import unittest
from decorating import monitor_stdout


class TestMonitorStdout(unittest.TestCase):

    def test1(self):
        """Test using a context manager"""
        test = "Cancer"
        expected = ["Cancer", "\n"]
        with monitor_stdout:
            print(test)
        self.assertListEqual(monitor_stdout.data, expected)

    # TODO: fix this test!
    # Description: this crash the decorating.decorator.Decorator.__call__
    # procedure! Why???
    # def test2(self):
    #     """Test using a function decorated"""
    #     monitor_stdout.clear()
    #     test = "This!"
    #     expected = ["This", "\n"]

    #     @monitor_stdout()
    #     def test():
    #         print(test)

    #     test()
    #     self.assertListEqual(monitor_stdout.data, expected)


if __name__ == '__main__':
    unittest.main()
