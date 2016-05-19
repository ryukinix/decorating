#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyright © Manoel Vilela
#
#

import sys
import time
import threading
import signal
import logging
from math import sin
from itertools import cycle
from functools import wraps
from decorating import color
from decorating.general import debug

DEBUGGING = False
if DEBUGGING:
    format = ('%(levelname)s: function %(funcName)s: line %(lineno)s\n'
              '---->: %(message)s')
    logging.basicConfig(format=format, level=logging.DEBUG)


class AnimationStream(object):

    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush()

    def erase(self, data):
        self.stream.write('\r' + len(data) * ' ')
        self.stream.write(2 * len(data) * "\010")
        self.stream.flush()

    def __getattr__(self, attr):
        return getattr(self.stream, attr)


class SpinnerController(object):
    position = 0
    done = False
    message = 'loading'
    running = False
    last_thread = None


# THIS IS A LOL ZONE

#    /\O    |    _O    |      O
#     /\/   |   //|_   |     /_
#    /\     |    |     |     |\
#   /  \    |   /|     |    / |
# LOL  LOL  |   LLOL   |  LOLLOL

braily = "⣾⣽⣻⢿⡿⣟⣯"
pulse = '▁▂▃▄▅▆▇▆▅▄▃▁'


def space_wave(x, b, char='█'):
    return char * int(20 * abs(sin(0.05 * (x + b))))


def _spinner(control):
    slow_braily = ''.join(x * 5 for x in braily)
    if not sys.stdout.isatty():  # not send to pipe/redirection
        return
    stream_animation = AnimationStream(sys.stdout)
    template = '{padding} {start} {control.message} {end}'
    for n, (start, end) in enumerate(zip(cycle(slow_braily), cycle(pulse))):
        padding = space_wave(n, control.position)
        message = '\r' + color.colorize(template.format_map(locals()), 'cyan')
        stream_animation.write(message)
        time.sleep(0.05)
        stream_animation.erase(message)
        if control.done:
            control.position = n
            break
    stream_animation.erase(message)

# D
#   E
#     C
#       O
#         R
#           A
#             T
#               O
#                 R
#                   S


# deal with it
class AnimatedDecorator(object):

    last_thread = None
    # to handle various decorated functions
    controller = SpinnerController()

    def __init__(self, arg):
        self.decorating = False
        logging.debug('arg passed: {!r}'.format(arg))
        if callable(arg):
            self.func = arg
            self.message = self.func.__name__
        else:
            self.func = None
            self.message = arg

    def calling(self):
        return self.func(*self.args, **self.kwargs)(context_manager=self)()

    def start_animation(self):
        logging.debug('starting animation!')
        if not self.controller.running:
            self.controller.message = self.message
            self.spinner_thread = threading.Thread(target=_spinner,
                                                   args=(self.controller,))
            self.controller.last_thread = self.spinner_thread
            self.controller.done = False
            self.spinner_thread.start()
            self.controller.running = True

    @staticmethod
    def stop_animation():
        if AnimatedDecorator.controller.running:
            AnimatedDecorator.controller.done = True
            AnimatedDecorator.controller.last_thread.join()
            AnimatedDecorator.controller.done = False
            AnimatedDecorator.controller.running = False
            logging.debug('animation finished!')

    def __enter__(self):
        logging.debug('entering in context')
        self.start_animation()

    def __exit__(self, *args):
        self.stop_animation()
        logging.debug('exiting from context')

    def __call__(self, *args, **kwargs):
        func = self.func or args[0]

        @wraps(func)
        def wrapper(*args, **kargs):
            self.start_animation()
            result = func(*args, **kargs)
            self.stop_animation()
            return result

        # called when decorated with args, so in __call__
        # the first argument is a function
        if callable(args[0]):
            logging.debug('decorator called before decorating!')
            return wrapper

        return wrapper(*args, **kwargs)

    @property
    def __name__(self):
        # well, for some reason, a underlying bug
        # occurs when a decorator is called without args
        # example:
        #          @debug
        #          @animated
        #          def slow():
        #             sleep(1)
        #
        # if we call this without this method, will throw an exception
        # about doesn't exists method __name__
        return self.func.__name__


animated = AnimatedDecorator


def killed():
    AnimatedDecorator.stop_animation()
    raise KeyboardInterrupt

signal.signal(signal.SIGINT, lambda x, y: killed())


def test():
    with animated('contextmanager'):
        time.sleep(2)

    @debug
    @animated('with args')
    def with_args(*args):
        time.sleep(2)
        return args

    @debug
    @animated()
    def decorated_with_called_decorator(*args):
        time.sleep(2)
        return args

    @debug
    @animated
    def without_args(*args):
        time.sleep(2)
        return args

    with_args('arg1', 'arg2')
    # decorated_with_called_decorator('arg1', 'arg2')
    # without_args('arg')


__all__ = ['animated']

if __name__ == '__main__':
    test()
