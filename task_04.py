#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module ensures 1 litterbox /kitten and some food available."""


def too_many_kittens(kittens, litterboxes, catfood):
    """This module returns boolean for food available.

        Args:
        kittens(int): Number of kittens.
        litterbox(int): Number of litterboxes for kittens.
        catfood(bool): Boolean, enough food available for kittens.

    Returns:
        bool: Enough catfood available.

    Examples:

        >>> too_many_kittens(100,0,False)
        True

        >>> too_many_kittens(100,0,0)
        True

        >>> too_many_kittens(12,12,False)
        True
    """
    enoughfood = not(litterboxes >= kittens and catfood)
    return enoughfood
