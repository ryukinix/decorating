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
    These tests cover the basic usage to create new decorators

    using the base class decorator.Decorator easily, only
    setuping the self.start() & self.stop() trigers, as well
    the optionals __exit__ and __enter__.


"""

import unittest
from decorating import writing
from decorating import decorator


class Wired(decorator.Decorator):

    """Wired pre-pos hook connection printer"""

    def __init__(self, user='Lain'):
        self.user = user

    def start(self):
        """Trigger the start hook"""
        self.login()

    def stop(self):
        """Trigger the stop hook"""
        self.logoff()

    def login(self):
        """Login in the wired with the default user"""
        print('Welcome to the Wired, {user}!'.format(user=self.user))

    def logoff(self):
        """Exits of this world, open the next"""
        print('Close this world, open the next!')
        print('Goodbye, {user}...'.format(user=self.user))
        del self.user


class TestWiredDecorator(unittest.TestCase):
    """Basic tests of DecoratorManager class

    The usage is filled into:
        as deco:
            * @Wired
            * @Wired()
            * @Wired(user='Chisa')
        as context-manager:
            * with Wired:
            * with Wired():
            * with Wired(user='Lain')

        Consistency is all!!!
    """

    wired = Wired()

    def test_deco_layer1(self):
        """Test decorator with basic usage"""
        with writing(0.01):
            @self.wired('Chisa')
            def _knights():
                with writing(0.03):
                    print('suiciding...')

            _knights()

    def test_deco_layer2(self):
        """Testing using with context-manager"""
        with writing(0.05):
            with self.wired('Manoel'):
                with writing(0.01):
                    print("I'm losing of my self.")
                    print("I'm exists, really?")

    def test_deco_layer3(self):
        """Mixed tests, nested func-decorated and context-manager"""
        @self.wired(user='Rafael From Hell')
        def _lain():
            print("FUCK YOURSELF")
            print("[#] lambda-shell")
            print(("λ- (def open-world (next)\n"
                   "     (eval next))"))
            print("λ- (open-world 'next-life)")

        with self.wired("Lerax"):
            with writing(0.01):
                print("I don't ever exists")
                print("But I'm exists.")
                print("hacking... hacking...")

        with writing(0.03):
            _lain()


if __name__ == '__main__':
    unittest.main()
