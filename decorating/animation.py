#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyright © Manoel Vilela
#

"""

    This module was be done to handle the beautiful animation using
    the sin function (whose cause a pulse in the stdout).

    Some examples of using is here:

        @animated
        def slow():
            heavy_stuff()

        As well with custom messages
        @animated('WOOOOW')
        def download_the_universe():
            while True:
                pass

        with animated('loool'):
            stuff_from_hell()

"""

import sys
import time
import threading
import signal
import logging
from math import sin
from itertools import cycle
from functools import wraps
from inspect import isfunction
from decorating import color

DEBUGGING = False
if DEBUGGING:
    logging.basicConfig(format=('%(levelname)s: function '
                                '%(funcName)s: line %(lineno)s\n'
                                '    | %(message)s'),
                        level=logging.DEBUG if DEBUGGING else logging.NOTSET)

LOGGER = logging.getLogger(__name__)
LOGGER.propagate = False


class AnimationStream(object):

    """A stream unbuffered whose write & erase at interval

    After you write something, you can easily clean the buffer
    and restart the points of the older message.
    stream = AnimationStream(stream, delay=0.5)
    self.write('message')

    """

    def __init__(self, stream, interval=0.05):
        self.stream = stream
        self.interval = interval

    def write(self, message):
        """Send something for stdout and erased after delay"""
        self.stream.write(message)
        self.stream.flush()
        time.sleep(self.interval)
        self.erase(message)

    def erase(self, message):
        """Erase something whose you write before: message"""
        self.stream.write('\r' + len(message) * ' ')
        self.stream.write(2 * len(message) * "\010")
        self.stream.flush()

    def __getattr__(self, attr):
        return getattr(self.stream, attr)


# THIS IS A LOL ZONE
#    /\O    |    _O    |      O
#     /\/   |   //|_   |     /_
#    /\     |    |     |     |\
#   /  \    |   /|     |    / |
# LOL  LOL  |   LLOL   |  LOLLOL

BRAILY = "⣾⣽⣻⢿⡿⣟⣯"
PULSE = '▁▂▃▄▅▆▇▆▅▄▃▁'
STREAM = AnimationStream(sys.stdout, interval=0.05)


def _space_wave(variable, bias, char='█'):
    return char * int(20 * abs(sin(0.05 * (variable + bias))))


def _spinner(control):
    if not sys.stdout.isatty():  # not send to pipe/redirection
        return

    template = '{padding} {start} {message} {end}'
    slow_braily = ''.join(x * 5 for x in BRAILY)
    for i, (start, end) in enumerate(zip(cycle(slow_braily), cycle(PULSE))):
        padding = _space_wave(i, control['last_position'])
        info = dict(padding=padding, start=start,
                    end=end, message=control['message'])
        message = '\r' + color.colorize(template.format_map(info), 'cyan')
        STREAM.write(message)
        STREAM.erase(message)
        if control['done']:
            control['last_position'] = i
            break
    STREAM.erase(message)

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

    """The animated decorator from hell

    You can use this these way:

        @animated
        def slow():
            heavy_stuff()

        As well with custom messages
        @animated('WOOOOW')
        def download_the_universe():
            while True:
                pass

        with animated('loool'):
            stuff_from_hell()
    """

    last_thread = None
    # to handle various decorated functions
    controller = dict(last_position=0,
                      last_thread=None,
                      done=False,
                      message='',
                      running=False)

    def __init__(self, arg=''):
        self.decorating = False
        self.last_message = ''
        if isfunction(arg):
            self.func = arg
            self.message = self.func.__name__  # pylint: disable=e1101
        else:
            self.func = None
            self.message = arg

        LOGGER.debug(str(arg))

    def start_animation(self, message=''):
        """Start a new animation instance"""
        LOGGER.debug('starting animation!')
        entities = [x for x in [self.controller['message'], self.message] if x]
        self.last_message = self.controller['message']
        self.controller['message'] = message or ' - '.join(entities)
        LOGGER.debug('[starting] last_message: ' + self.last_message)
        if not self.controller['running']:
            thread = threading.Thread(target=_spinner,
                                      args=(self.controller,))
            self.controller['last_thread'] = thread
            self.controller['done'] = False
            self.controller['last_thread'].start()
            self.controller['running'] = True

    @staticmethod
    def stop_animation(last_message=''):
        """Stop the thread animation gracefully and reset_message"""
        controller = AnimatedDecorator.controller
        if controller['running']:
            controller['done'] = True
            controller['last_thread'].join()
            controller['done'] = False
            controller['running'] = False
            LOGGER.debug('[stopping] last_message: ' + last_message)
            LOGGER.debug('animation finished!')

        # some context managers don't running because others are running
        # so, anyway, we need update the controller['message'] = last_message
        # to works fine with nested context_managers
        AnimatedDecorator.reset_message(last_message)

    @staticmethod
    def reset_message(last_message=''):
        """reset the message of the public controller spinner"""
        AnimatedDecorator.controller['message'] = last_message

    def __enter__(self):
        LOGGER.debug('entering in context: ' + self.message)
        self.start_animation()

    def __exit__(self, *args):
        LOGGER.debug('exiting from context: ' + self.message)
        LOGGER.debug('message active: ' + self.last_message)
        # if the context manager doesn't running yet
        if not self.last_message or self.controller['running']:
            LOGGER.debug('stopping')
            self.stop_animation(self.last_message)
        else:
            LOGGER.debug('reseting and start again')
            LOGGER.debug('last_message: ' + self.last_message)
            LOGGER.debug('thread: ' + self.message)
            self.reset_message(self.last_message)
            self.start_animation(self.last_message)

    def __call__(self, *args, **kwargs):
        func = self.func or args[0]

        @wraps(func)
        def _wrapper(*args, **kargs):
            self.start_animation()
            result = func(*args, **kargs)
            self.stop_animation(self.last_message)
            return result

        # called when decorated with args, so in __call__
        # the first argument is a function
        if any(args) and callable(args[0]):
            LOGGER.debug('decorator called before decorating!')
            return _wrapper

        return _wrapper(*args, **kwargs)

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
        return self.func.__name__ if self.func else ''  # pylint: disable=e1101


animated = AnimatedDecorator  # pylint: disable=C0103


def _killed():
    AnimatedDecorator.stop_animation()
    raise KeyboardInterrupt

signal.signal(signal.SIGINT, lambda x, y: _killed())


__all__ = ['animated']
