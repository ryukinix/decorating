#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyright © Manoel Vilela
#

import unittest
tests = unittest.defaultTestLoader.discover(__file__)
suite = unittest.defaultTestLoader.suiteClass(tests)
unittest.TextTestRunner(verbosity=2).run(suite)
