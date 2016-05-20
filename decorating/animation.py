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

DEBUGGING = False
level = logging.DEBUG if DEBUGGING else logging.NOTSET
if DEBUGGING:
    format = ('%(levelname)s: function %(funcName)s: line %(lineno)s\n'
              '    | %(message)s')

    logging.basicConfig(format=format, level=logging.DEBUG)

logger = logging.getLogger(__name__)
logger.propagate = False


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
    message = ''
    done = False
    running = False
    last_thread = None


# THIS IS A LOL ZONE

#    /\O    |    _O    |      O
#     /\/   |   //|_   |     /_
#    /\     |    |     |     |\
#   /  \    |   /|     |    / |
# LOL  LOL  |   LLOL   |  LOLLOL

BRAILY = "⣾⣽⣻⢿⡿⣟⣯"
PULSE = '▁▂▃▄▅▆▇▆▅▄▃▁'


def space_wave(x, b, char='█'):
    return char * int(20 * abs(sin(0.05 * (x + b))))


def _spinner(control):
    slow_braily = ''.join(x * 5 for x in BRAILY)
    if not sys.stdout.isatty():  # not send to pipe/redirection
        return
    stream_animation = AnimationStream(sys.stdout)
    template = '{padding} {start} {control.message} {end}'
    for n, (start, end) in enumerate(zip(cycle(slow_braily), cycle(PULSE))):
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

    def __init__(self, arg=''):
        self.decorating = False
        logger.debug('arg passed: {!r}'.format(arg))
        if callable(arg):
            self.func = arg
            self.message = self.func.__name__
        else:
            self.func = None
            self.message = arg
        self.last_message = ''

    def start_animation(self, message=''):
        logger.debug('starting animation!')
        entities = filter(bool, [self.controller.message, self.message])
        self.last_message = self.controller.message
        self.controller.message = message or ' - '.join(entities)
        logger.debug('[starting] last_message: ' + self.last_message)
        if not self.controller.running:
            self.spinner_thread = threading.Thread(target=_spinner,
                                                   args=(self.controller,))
            self.controller.last_thread = self.spinner_thread
            self.controller.done = False
            self.spinner_thread.start()
            self.controller.running = True

    @staticmethod
    def stop_animation(last_message=''):
        controller = AnimatedDecorator.controller
        if controller.running:
            controller.done = True
            controller.last_thread.join()
            controller.done = False
            controller.running = False
            logger.debug('[stopping] last_message: ' + last_message)
            logger.debug('animation finished!')

        # some context managers don't running because others are running
        # so, anyway, we need update the controller.message = last_message
        # to works fine with nested context_managers
        AnimatedDecorator.reset_message(last_message)

    @staticmethod
    def reset_message(last_message=''):
        AnimatedDecorator.controller.message = last_message

    def __enter__(self):
        logger.debug('entering in context: ' + self.message)
        self.start_animation()

    def __exit__(self, *args):
        logger.debug('exiting from context: ' + self.message)
        logger.debug('message active: ' + self.last_message)
        # if the context manager doesn't running yet
        if not self.last_message or self.controller.running:
            logger.debug('stopping')
            self.stop_animation(self.last_message)
        else:
            logger.debug('reseting and start again')
            logger.debug('last_message: ' + self.last_message)
            logger.debug('thread: ' + self.message)
            self.reset_message(self.last_message)
            self.start_animation(self.last_message)

    def __call__(self, *args, **kwargs):
        func = self.func or args[0]

        @wraps(func)
        def wrapper(*args, **kargs):
            self.start_animation()
            result = func(*args, **kargs)
            self.stop_animation(self.last_message)
            return result

        # called when decorated with args, so in __call__
        # the first argument is a function
        if any(args) and callable(args[0]):
            logger.debug('decorator called before decorating!')
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


__all__ = ['animated']
