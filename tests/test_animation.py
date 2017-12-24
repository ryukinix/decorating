#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#    Copyright © Manoel Vilela 2016
#
#    @project: Decorating
#     @author: Manoel Vilela
#      @email: manoel_vilela@engineer.com
#

"""
    Tests for the animation module!

    For now covers:

    [x] - AnimatedDecorator @ animated
    [x] - WritingDecorator @ writing
    [x] - _spacewave (running based on the class above)
    [x] - _spinner (running based on the class above)

"""

import unittest
import time
from decorating import debug, animated, writing


class TestAnimatedDecorator(unittest.TestCase):

    """General test for the class AnimatedDecorator — @animated"""

    args = ('banana', 'choque')

    def test1(self):
        """Test Decorator Function With Args"""
        @debug
        @animated('with args')
        def _with_args(*args):
            for i in range(10):
                print(i)
                time.sleep(0.5)
            return args

        self.assertEqual(_with_args(*self.args), self.args,
                         'need returns the same I/O')

    def test2(self):
        """Test Decorator Function Without Args"""
        @debug
        @animated()
        def _without_args(*args):
            time.sleep(0.5)
            return args

        self.assertEqual(_without_args(*self.args), self.args,
                         'need returns the same I/O')

    def test3(self):
        """Test Decorator Function Decorated"""
        @debug
        @animated
        def _decorated(*args):
            time.sleep(0.5)
            return args

        self.assertEqual(_decorated(*self.args), self.args,
                         'need returns the same I/O')

    def test4(self):
        """Test Decorator With Context Manager"""
        @debug
        @animated
        def _animation(*args):  # pylint: disable=unused-argument
            time.sleep(1)

        with animated('testing something'):
            self.assertIsNone(_animation(*self.args),
                              'need returns the same I/O')

    def test5(self):
        """Test Decorator With Nested Context Managers"""
        @debug
        @animated('with args')
        def _with_args(*args):
            time.sleep(1)
            return args

        with animated('layer-01'):
            with animated('layer-02'):
                with animated('level-03'):
                    level1 = _with_args(*self.args)
                level2 = _with_args(*self.args)

        for level in (level1, level2):
            self.assertEqual(level, self.args, 'need returns the same I/O')

    def test6(self):
        """Try disable the animation decorated"""
        print("Testing the enabled/disabled o animated")
        animated.enabled = False
        print("animated.enabled = False")
        self.test4()
        print("animated.enabled = True")
        animated.enabled = True
        self.test5()

class TestWritingDecorator(unittest.TestCase):

    """Tests covering the @writing decorator"""

    def test1(self):
        """Test writing as simple decorator"""
        @writing
        def _printer():
            print("Quantidade infinita de dor no rabo")
            return True

        self.assertTrue(_printer(), 'need be True')

    def test2(self):
        """Test writing as decorator with args"""
        @writing(delay=0.05)
        def _printer():
            print("Banana doce com pé de feijão")
            return True

        self.assertTrue(_printer(), 'need be True')

    @staticmethod
    def test3():
        """Test writing as context manager"""
        with writing():
            print("LOOOOOL")

    @staticmethod
    def test4():
        """Test writing as context manager with args"""
        with writing(delay=0.05):
            print("WOOOOOW")


if __name__ == '__main__':
    unittest.main()
