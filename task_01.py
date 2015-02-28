#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Monty Python Wink string Function takes string and multiplies it.

    Args:
        wink(str): Arg to be multiplied.
        numwink(int): Multiply string, stored in wink.

    Returns:
        string: All arguments concatenated with commas combined to a string.

    Examples:

         >>>know_what_i_mean(wink, 2)
        'Know what I mean? wink wink, nudge nudge'

        >>> know_what_i_mean('wink ', 4)
        'Know what I mean? wink wink wink wink, nudge nudge nudge nudge'

    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
