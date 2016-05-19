#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyright © Manoel Vilela
#
#


import unittest

from decorating.general import debug, cache, count_time, counter


class TestCashDecorator(unittest.TestCase):

    def test_cache(self):
        @cache
        def fib(x):
            if x < 2:
                return x
            else:
                return fib(x - 1) + fib(x - 2)

        # First call gives a call count of 1
        self.assertEqual(fib(1), 1, "output invalid")
        self.assertEqual(fib.call, 1, "initial count wrong")

        # Second call keeps the call count at 1 - the cached value is used
        self.assertEqual(fib(1), 1, "output invalid")
        self.assertEqual(fib.call, 1, 'the second equal count must be 1')

        # Subsequent call with a new value increased the call count
        self.assertEqual(fib(5), 5, "output invalid")
        self.assertEqual(fib.call, 6, 'the other count must be 6')


class TestDebugDecorator(unittest.TestCase):

    def test_debug_output(self):
        @debug
        def add(x, y):
            return x + y

        table_tests = {
            (add, (1, 2)): ["add", (1, 2), 3],
            (add, (1, 3)): ["add", (1, 3), 4],
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
