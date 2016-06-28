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
tests = unittest.defaultTestLoader.discover(__file__)
suite = unittest.defaultTestLoader.suiteClass(tests)
unittest.TextTestRunner(verbosity=2).run(suite)
