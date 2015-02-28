#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Default Variables"""


def defaults(my_required, my_optional=True):
    """This module returns boolean for food available.

        Args:
        my_required(bool): Arg to be compared with the default.
        my_optional(bool): Arg with edfault value of True

    Returns:
        bool: Truthiness is checked for variables and retuned

    Examples:

        >>> defaults(True)
        True

        >>> defaults(False, True)
        False

        >>> defaults(True, False)
        False
    """

    myanswer = my_optional is my_required
    return myanswer
