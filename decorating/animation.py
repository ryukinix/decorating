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
if DEBUGGING:
    logging.basicConfig(format=('%(levelname)s: function '
                                '%(funcName)s: line %(lineno)s\n'
                                '    | %(message)s'),
                        level=logging.DEBUG if DEBUGGING else logging.NOTSET)

LOGGER = logging.getLogger(__name__)
LOGGER.propagate = False


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


# THIS IS A LOL ZONE
#    /\O    |    _O    |      O
#     /\/   |   //|_   |     /_
#    /\     |    |     |     |\
#   /  \    |   /|     |    / |
# LOL  LOL  |   LLOL   |  LOLLOL

BRAILY = "⣾⣽⣻⢿⡿⣟⣯"
PULSE = '▁▂▃▄▅▆▇▆▅▄▃▁'


def space_wave(variable, bias, char='█'):
    return char * int(20 * abs(sin(0.05 * (variable + bias))))


def _spinner(control):
    slow_braily = ''.join(x * 5 for x in BRAILY)
    if not sys.stdout.isatty():  # not send to pipe/redirection
        return
    stream_animation = AnimationStream(sys.stdout)
    template = '{padding} {start} {message} {end}'
    for n, (start, end) in enumerate(zip(cycle(slow_braily), cycle(PULSE))):
        padding = space_wave(n, control['position'])
        info = dict(padding=padding, start=start,
                    end=end, message=control['message'])
        message = '\r' + color.colorize(template.format_map(info), 'cyan')
        stream_animation.write(message)
        time.sleep(0.05)
        stream_animation.erase(message)
        if control['done']:
            control['position'] = n
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
    controller = dict(last_position=0,
                      message='',
                      done=False,
                      running=False,
                      last_thread=None)

    def __init__(self, arg=''):
        self.decorating = False
        LOGGER.debug('arg passed: {!r}'.format(arg))
        if callable(arg):
            self.func = arg
            self.message = self.func.__name__
        else:
            self.func = None
            self.message = arg
        self.last_message = ''

    def start_animation(self, message=''):
        LOGGER.debug('starting animation!')
        entities = filter(bool, [self.controller['message'], self.message])
        self.last_message = self.controller['message']
        self.controller['message'] = message or ' - '.join(entities)
        LOGGER.debug('[starting] last_message: ' + self.last_message)
        if not self.controller['running']:
            self.spinner_thread = threading.Thread(target=_spinner,
                                                   args=(self.controller,))
            self.controller['last_thread'] = self.spinner_thread
            self.controller['done'] = False
            self.spinner_thread.start()
            self.controller['running'] = True

    @staticmethod
    def stop_animation(last_message=''):
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
        def wrapper(*args, **kargs):
            self.start_animation()
            result = func(*args, **kargs)
            self.stop_animation(self.last_message)
            return result

        # called when decorated with args, so in __call__
        # the first argument is a function
        if any(args) and callable(args[0]):
            LOGGER.debug('decorator called before decorating!')
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
        return self.func.__name__ if self.func else ''


animated = AnimatedDecorator


def killed():
    AnimatedDecorator.stop_animation()
    raise KeyboardInterrupt

signal.signal(signal.SIGINT, lambda x, y: killed())


__all__ = ['animated']
