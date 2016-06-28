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
from decorating import color


class TestColorize(unittest.TestCase):

    def test_colorize(self):
        string = 'lain'
        color.COLORED = True
        colored_string = color.colorize(string, 'cyan')

        self.assertNotEqual(string, colored_string, "Must be different")

    def test_colorize_disabled(self):
        string = 'test'
        color.COLORED = False
        colored_string = color.colorize(string, 'cyan')
        self.assertEqual(string, colored_string, "Disabled; must be the same")

    def test_failing(self):
        string = 'test'
        color.COLORED = True
        fails = False
        try:
            color.colorize(string, 'sua mae', 'eu e vc')
        except RuntimeError:
            fails = True

        self.assertTrue(fails, "Must fails with RunTime if fails")

if __name__ == '__main__':
    unittest.main()
