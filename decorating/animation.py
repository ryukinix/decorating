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
from math import sin
from itertools import cycle
from functools import wraps
from decorating import color


class Unbuffered(object):

    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush()

    def __getattr__(self, attr):
        return getattr(self.stream, attr)


class StopSpinner(object):
    done = False
    position = 0
    message = 'loading'


# global variables from hell
sys.stdout = Unbuffered(sys.stdout)
sig = StopSpinner()


# THIS IS A LOL ZONE

#    /\O    |    _O    |      O
#     /\/   |   //|_   |     /_
#    /\     |    |     |     |\
#   /  \    |   /|     |    / |
# LOL  LOL  |   LLOL   |  LOLLOL

animation_diagram = "⣾⣽⣻⢿⡿⣟⣯"
animation_spinner = '▁▂▃▄▅▆▇▆▅▄▃▁'


def _spinner(control):
    animation = ''.join(x * 5 for x in animation_diagram)
    if not sys.stdout.isatty():  # not send to pipe/redirection
        return
    anim = zip(cycle(animation), cycle(animation_spinner))
    for n, start_end_anim in enumerate(anim):
        start, end = start_end_anim
        padding = '█' * int(20 * abs(sin(0.05 * (n + control.position))))
        padding_colored = color.colorize(padding, 'cyan')
        banner = '{} {} {}'.format(start, control.message, end)
        banner_colored = color.colorize(banner, 'cyan')
        message = '\r' + padding_colored + banner_colored
        sys.stdout.write(message)
        time.sleep(0.05)
        sys.stdout.write('\r' + len(message) * ' ')
        sys.stdout.write(2 * len(message) * "\010")
        if control.done:
            control.position = n
            break
    sys.stdout.write(len(message) * ' ')
    sys.stdout.write('\r' + 2 * len(message) * "\010")

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
def animated(func_or_message):
    def _animated(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            global last_thread
            if not wrapper.running:
                sig.message = name
                spinner_thread = threading.Thread(target=_spinner, args=(sig,))
                spinner_thread.start()
                last_thread = spinner_thread
                wrapper.running = True
            result = func(*args, **kwargs)
            if wrapper.running:
                sig.done = True
                spinner_thread.join()
                wrapper.running = False
                sig.done = False

            return result

        wrapper.running = False

        return wrapper

    if callable(func_or_message):  # function, no args
        name = func_or_message.__name__
        return _animated(func_or_message)
    else:
        name = func_or_message  # string, with args
        return _animated

# END OF THE LOL ZONE
