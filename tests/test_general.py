#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyright © Manoel Vilela
#
#


import unittest

from decorating import cache


class TestCacheDecorator(unittest.TestCase):

    """Test for the cache decorator"""

    def test_cache(self):
        """Basic test for cache using fibonacci"""
        @cache
        def _fib(x):
            if x < 2:
                return x
            else:
                return _fib(x - 1) + _fib(x - 2)

        # First call gives a call count of 1
        self.assertEqual(_fib(1), 1, "output invalid")
        self.assertEqual(_fib.call, 1, "initial count wrong")

        # Second call keeps the call count at 1 - the cached value is used
        self.assertEqual(_fib(1), 1, "output invalid")
        self.assertEqual(_fib.call, 1, 'the second equal count must be 1')

        # Subsequent call with a new value increased the call count
        self.assertEqual(_fib(5), 5, "output invalid")
        self.assertEqual(_fib.call, 6, 'the other count must be 6')


if __name__ == '__main__':
    unittest.main()
