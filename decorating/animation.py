#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyright © Manoel Vilela
#
# pylint: disable=no-member
# pylint: disable=C0103
# pylint: disable=too-few-public-methods

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

        @writing
        def printer():
            lot_of_messages()

        with writing(delay=0.5):
            print("L  O  L => IS NOT THE STUPID GAME LOL, LOL.")


"""

import signal
import sys
import threading
from itertools import cycle
from math import sin
from decorating import base
from decorating import color
from decorating import stream
from decorating import asciiart


# THIS IS A LOL ZONE
#    /\O    |    _O    |      O
#     /\/   |   //|_   |     /_
#    /\     |    |     |     |\
#   /  \    |   /|     |    / |
# LOL  LOL  |   LLOL   |  LOLLOL


class SpinnerController(object):
    """Variables to controlling the spinner in parallel

    Bias: the initial value of the padding function
          is used here because after a animation stop
          and other is started in sequence, the padding
          for a semantic view need be in the same place.

    done: variable signal-like to stop the thread
          on the main loop doing the animation

    message: the actual messaging on the spinner

    stream: the stream to do the animation, needs
            implement the AbstractClass stream.Stream

    """

    bias = 0
    done = False
    message = ''
    stream = stream.Animation(sys.stderr)


class AnimationController(object):
    """Used to controlling thread & running"""
    running = False
    thread = None
    context = 0


def _space_wave(variable, bias, char='█'):
    return char * int(20 * abs(sin(0.05 * (variable + bias))))


def _spinner(control, fpadding=_space_wave):
    if not sys.stdout.isatty():  # not send to pipe/redirection
        return

    template = '{padding} {start} {message} {end}'
    NBRAILY = ''.join(x * 5 for x in asciiart.BRAILY)
    iterator = zip(cycle(NBRAILY), cycle(asciiart.PULSE))
    for i, (start, end) in enumerate(iterator):
        padding = fpadding(i, control.bias)
        info = dict(message=control.message,
                    padding=padding,
                    start=start,
                    end=end)
        message = '\r' + color.colorize(template.format_map(info), 'cyan')
        if not control.stream.lock.locked():
            control.stream.write(message)
        if control.done:
            control.bias = i
            break
    control.stream.erase(message)

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
class AnimatedDecorator(base.Decorator):

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

    # to handle various decorated functions
    spinner = SpinnerController()
    # to know if some instance of this class is running
    # and proper handle that, like ctrl + c and exits
    animation = AnimationController()

    def __init__(self, arg=None, fpadding=_space_wave):
        super(AnimatedDecorator, self).__init__(arg)
        self.fpadding = fpadding
        self.message = self.argument or 'loading'
        self.last_message = self.message

    def start(self, message=None):
        """Start a new animation instance"""
        self.last_message = self.spinner.message
        entities = [x for x in [self.spinner.message, self.message] if bool(x)]
        self.spinner.message = message or ' - '.join(entities)
        if not self.animation.running:
            self.animation.thread = threading.Thread(target=_spinner,
                                                     args=(self.spinner,
                                                           self.fpadding))
            self.spinner.done = False
            self.animation.thread.start()
            self.animation.running = True
            sys.stdout = stream.Clean(sys.stdout, self.spinner.stream)

    @classmethod
    def stop(cls, last_message=''):
        """Stop the thread animation gracefully and reset_message"""
        if cls.animation.running:
            cls.spinner.done = True
            cls.animation.thread.join()
            cls.spinner.done = False
            cls.animation.running = False

        sys.stdout = sys.__stdout__

        # some context managers don't running because others are running
        # so, anyway, we need update the cls.spinner.message = last_message
        # to works fine with nested context_managers
        cls.reset_message(last_message)

    @classmethod
    def reset_message(cls, last_message=''):
        """reset the message of the public spinner spinner"""
        cls.spinner.message = last_message

    def __enter__(self):
        self.animation.context += 1
        self.start()

    def __exit__(self, *args):
        # if the context manager doesn't running yet
        print(self.animation.context)
        self.animation.context -= 1
        if self.animation.context == 0:
            self.stop(self.last_message)
        else:
            self.reset_message(self.last_message)
            self.start(self.last_message)


class WritingDecorator(base.Decorator):

    """A writing class context to simulate a delayed stream

    You can do something like that:

    with writing(delay=0.3):
        print('LOL!!! This is so awesome!')

    Or, as expected for this lib, using as decorator!

    @writing
    def somebody_talking():
        print("Oh man... I'm so sad. Why I even exists?")
        print("I'm no meeting anybody")
        print("I don't want answer my phone")
        print("I don't even to live")
        print("But dying is so hassle.")
        print("I'd wants just disappears.")

    delay: the down speed of writing, more bigger, more slow.


    """

    def __init__(self, arg=None, delay=0.08):
        super(WritingDecorator, self).__init__(arg)
        self.stream = stream.Writting(sys.stdout, delay=delay)

    def start(self):
        """Activate the TypingStream on stdout"""
        sys.stdout = self.stream

    @staticmethod
    def stop():
        """Change back the normal stdout after the end"""
        sys.stdout = sys.__stdout__

    def __enter__(self):
        self.start()

    def __exit__(self, *args):
        self.stop()


def _killed():
    AnimatedDecorator.stop()
    WritingDecorator.stop()
    raise KeyboardInterrupt

signal.signal(signal.SIGINT, lambda x, y: _killed())

animated = AnimatedDecorator
writing = WritingDecorator


__all__ = ['animated']

if __name__ == '__main__':
    with writing(delay=0.03):
        print('loooooollllllllllllllloool')
