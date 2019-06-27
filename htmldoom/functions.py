"""Functional APIs to render dynamic elements.

Example:
    >>> from htmldoom import elements as e
    >>> from htmldoom import functions as fn
    >>> 
    >>> tuple(fn.foreach(["good", "bad", "evil"])(
    ...     lambda x: fn.switch({
    ...         x == "good": lambda: e.Span(style="color: green")(f"this is {x}"),
    ...         x == "bad": lambda: e.Span(style="color: yellow")(f"this is {x}"),
    ...         x == "evil": lambda: e.Span(style="color: red")(f"this is {x}"),
    ...         fn.Case.DEFAULT: lambda: fn.Error.throw(ValueError(x)),
    ...     })
    ... ))
    (<span style="color: green">this is good</span>,
     <span style="color: yellow">this is bad</span>,
     <span style="color: red">this is evil</span>)
"""

import re
import typing as t
from collections import Mapping
from functools import lru_cache

MAX_CACHE_SIZE = 12800


class Case:
    """Builtin switch cases to help with the switch function."""

    class DEFAULT:
        """The default switch case."""

        pass


class Error:
    """Helps raising errors from lambdas."""

    @staticmethod
    def throw(error: Exception):
        raise error


def switch(cases):
    """A dirty implementation of the missing switch case.

    Example:
        >>> (lambda x: switch({
        ...     x == 0: lambda: "zero",
        ...     x == 1: lambda: "one",
        ...     Case.DEFAULT: lambda: Error.throw(ValueError(x)),
        ... }))(0)
        'zero'
    """
    return cases.get(True, cases[Case.DEFAULT])()


def foreach(data):
    """A foreach function to make map() look a little nicer.
    
    Example:
        >>> list(foreach([1, 2, 4])(lambda n: n * 2))
        [2, 4, 3]
    """

    def wrapped(func):
        return map(func, data)

    return wrapped
