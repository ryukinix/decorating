#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#    Copyright © Manoel Vilela 2016
#
#    @project: Decorating
#     @author: Manoel Vilela
#      @email: manoel_vilela@engineer.com
#

import unittest
from decorating import debug, counter, count_time


class TestDebugDecorator(unittest.TestCase):

    def test_debug_output(self):
        @debug
        def add(x, y):
            return x + y

        @debug
        def lol(x):
            return '?'

        table_tests = {
            (add, (1, 2)): ["add", "(1, 2)", 3],
            (add, (1, 3)): ["add", "(1, 3)", 4],
            (lol, (1,)): ["lol", "(1)", '?']
        }

        for test, expected in table_tests.items():
            func, args = test
            result = func(*args)
            self.assertEqual(result, expected[-1], "Result of call wrong")
            self.assertEqual(func.last_output, expected,
                             "debug doesn't returns correct values")


class TestCountTimeDecorator(unittest.TestCase):

    def test_count_time_decorator(self):
        from time import sleep

        @count_time
        def test(x):
            sleep(0.01)
            return "output"

        for x in range(10):
            call = test(x)
            self.assertEqual(call, "output", "output incorrect for decorator")
            self.assertNotEqual(0, test.time, "execution times must > 0")


class TestCounterDecorator(unittest.TestCase):

    def test_counter_decorator(self):
        @counter
        def lol():
            return 'lol'

        output = lol()
        self.assertEqual(output, 'lol', "the output are incorrect")
        self.assertEqual(lol.count, 1, )


if __name__ == '__main__':
    unittest.main()
