#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#    Copyright © Manoel Vilela 2016
#
#    @project: Decorating
#     @author: Manoel Vilela
#      @email: manoel_vilela@engineer.com
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
from __future__ import unicode_literals
import signal
import sys
import threading
from math import sin
from functools import partial
from itertools import cycle
from . import decorator, color, stream, asciiart
from .general import zip


# THIS IS A LOL ZONE
#    /\O    |    _O    |      O
#     /\/   |   //|_   |     /_
#    /\     |    |     |     |\
#   /  \    |   /|     |    / |
# LOL  LOL  |   LLOL   |  LOLLOL



# HACK: Global variables to customize behavior of spinner

horizontal = asciiart.WAVE
vertical1 = ''.join(x * 5 for x in asciiart.BRAILY)
vertical2 = asciiart.VPULSE
animation_color = {
    'message': 'red',
    'padding': 'blue',
    'start': 'cyan',
    'end': 'cyan'
}



class SpinnerController(object):
    """Variables to controlling the spinner in parallel

    Bias: the initial value of the padding function
          is used here because after a animation stop
          and other is started in sequence, the padding
          for a semantic view need be in the same place.

    running: variable signal-like to stop the thread
          on the main loop doing the animation

    message: the actual messaging on the spinner

    stream: the stream to do the animation, needs
            implement the AbstractClass stream.Stream

    """

    bias = 0
    running = False
    message = ''
    stream = stream.Animation(sys.stderr)
    fpadding = None


class AnimationController(object):
    """Used to controlling thread & running

    context: the context level added +1 at each nested 'with'
    running: the object running in the actual moment

    """
    context = 0
    thread = None
    messages = []


def space_wave(phase, amplitude=12, frequency=0.1):
    """
    Function: space_wave
    Summary: This function is used to generate a wave-like padding
             spacement based on the variable lambda
    Examples: >>> print('\n'.join(space_wave(x) for x in range(100))
              █
              ███
              ████
              ██████
              ███████
              ████████
              █████████
              ██████████
              ██████████
              ██████████
              ██████████
              ██████████
              ██████████
              █████████
              ████████
              ███████
              █████
              ████
              ██
              █

    Attributes:
        @param (phase): your positive variable, can be a int or float
        @param (char) default='█': the char to construct the space_wave
        @param (amplitude) default=10: a float/int number to describe
                                       how long is the space_wave max
        @param (frequency) default=0.1: the speed of change
    Returns: a unique string of a sequence of 'char'
    """
    wave = cycle(horizontal)
    return ''.join((next(wave) for x in range
                    (int((amplitude + 1) * abs(sin(frequency * (phase)))))))


def _spinner(control):
    if not sys.stdout.isatty():  # not send to pipe/redirection
        return  # pragma: no cover

    colorize_no_reset = partial(color.colorize, autoreset=False)

    template = '{padding} {start} {message} {end}'
    iterator = zip(cycle(vertical1), cycle(vertical2))
    for i, (start, end) in enumerate(iterator):
        padding = control.fpadding(i + control.bias)
        message = '\r' + template.format(
            message=colorize_no_reset(control.message, animation_color['message']),
            padding=colorize_no_reset(padding, animation_color['padding']),
            start=colorize_no_reset(start, animation_color['start']),
            end=color.colorize(end, animation_color['end'])
        )
        with control.stream.lock:
            control.stream.write(message)
        if not control.running:
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
class AnimatedDecorator(decorator.Decorator):

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

    # if nothing is passed, so this is the message
    default_message = 'loading'
    # to handle various decorated functions
    spinner = SpinnerController()
    # to know if some instance of this class is running
    # and proper handle that, like ctrl + c and exits
    animation = AnimationController()

    _enabled = True

    def __init__(self, message=None, fpadding=space_wave):
        super(AnimatedDecorator, self).__init__()
        self.message = message
        self.spinner.fpadding = fpadding

    @property
    def enabled(self):
        """True if animation is enabled, false otherwise"""
        return AnimatedDecorator._enabled

    @enabled.setter
    def enabled(self, state):
        """Set a state on AnimatedDecorator._enabled"""
        AnimatedDecorator._enabled = state

    def start(self, autopush=True):
        """Start a new animation instance"""
        if self.enabled:
            if autopush:
                self.push_message(self.message)
                self.spinner.message = ' - '.join(self.animation.messages)
            if not self.spinner.running:
                self.animation.thread = threading.Thread(target=_spinner,
                                                         args=(self.spinner,))
                self.spinner.running = True
                self.animation.thread.start()
                sys.stdout = stream.Clean(sys.stdout, self.spinner.stream)

    @classmethod
    def stop(cls):
        """Stop the thread animation gracefully and reset_message"""
        if AnimatedDecorator._enabled:
            if cls.spinner.running:
                cls.spinner.running = False
                cls.animation.thread.join()

            if any(cls.animation.messages):
                cls.pop_message()

            sys.stdout = sys.__stdout__

    def __enter__(self):
        if self.enabled:
            self.animation.context += 1
            self.start()

    def __exit__(self, *args):
        # if the context manager doesn't running yet
        if self.enabled:
            self.animation.context -= 1
            self.pop_message()
            if self.animation.context == 0:
                self.stop()
            else:
                self.start(autopush=False)

    @classmethod
    def push_message(cls, message):
        """Push a new message for the public messages stack"""
        return cls.animation.messages.append(message)

    @classmethod
    def pop_message(cls):
        """Pop a new message (last) from the public message stack"""
        return cls.animation.messages.pop(-1)

    @classmethod
    def __call__(cls, *args, **kwargs):
        obj = super(AnimatedDecorator, cls).__call__(*args, **kwargs)
        if any(cls.instances):
            last_instance = cls.instances[-1]
            last_instance.message = last_instance.auto_message(args)
        elif isinstance(obj, cls):
            obj.message = obj.auto_message(args)
        return obj

    def auto_message(self, args):
        """Try guess the message by the args passed

        args: a set of args passed on the wrapper __call__ in
              the definition above.

        if the object already have some message (defined in __init__),
        we don't change that. If the first arg is a function, so is decorated
        without argument, use the func name as the message.

        If not self.message anyway, use the default_message global,
        another else  use the default self.message already

        """
        if any(args) and callable(args[0]) and not self.message:
            return args[0].__name__
        elif not self.message:
            return self.default_message
        else:
            return self.message


class WritingDecorator(decorator.Decorator):

    """A writing class context to simulate a delayed stream

    You can do something like that:

    with writing(delay=0.3):
        print('LOL!!! This is so awesome!')

    Or, as expected for this lib, using as decorator!

    @writing
    def somebody_talking():
        print("Oh man... I'm so sad. Why I even exists?")
        print("I don't meeting anybody")
        print("I don't want answer my phone")
        print("I don't even to live")
        print("But dying is so hassle.")
        print("I'd wish just disappears.")

    delay: the down speed of writing, more bigger, more slow.


    """

    # to handle nested streams
    streams = []
    enabled = True

    def __init__(self, delay=0.05):
        super(WritingDecorator, self).__init__()
        self.stream = stream.Writting(sys.stdout, delay=delay)
        if not self.enabled:
            self.stream = sys.__stdout__

    def start(self):
        """Activate the TypingStream on stdout"""
        self.streams.append(sys.stdout)
        sys.stdout = self.stream

    @classmethod
    def stop(cls):
        """Change back the normal stdout after the end"""
        if any(cls.streams):
            sys.stdout = cls.streams.pop(-1)
        else:
            sys.stdout = sys.__stdout__


def _killed():  # pragma: no cover
    AnimatedDecorator.stop()
    WritingDecorator.stop()
    AnimatedDecorator.spinner.stream.dump.close()
    raise KeyboardInterrupt

signal.signal(signal.SIGINT, lambda x, y: _killed())

animated = AnimatedDecorator('loading')
writing = WritingDecorator()


__all__ = [
    'animated',
    'writing'
]
