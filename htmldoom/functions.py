"""Functional APIs to render dynamic elements.

Most of the functions here helps make the code look a little nicer but there might be
some performance cost. For example, in case of the switch case, the cost of creating a
new dictionary instance for each case, or in case of the foreach loop, the cost of an extra
functiion call.

Hence, always prefer to stick with the builtin functions in Python such as map, lambda,
or even good old function definitions. use these functions where the other benefits 
outweights performance concerns.

Example:
    >>> from htmldoom import elements as e
    >>> from htmldoom import functions as fn
    >>> 
    >>> tuple(fn.foreach(["good", "bad", "evil"])(
    ...     lambda x: fn.switch({
    ...         x == "good": lambda: e.span(style="color: green")(f"this is {x}"),
    ...         x == "bad": lambda: e.span(style="color: yellow")(f"this is {x}"),
    ...         x == "evil": lambda: e.span(style="color: red")(f"this is {x}"),
    ...         fn.Case.DEFAULT: lambda: fn.Error.throw(ValueError(x)),
    ...     })
    ... ))
    (b'<span style="color: green">this is good</span>',
     b'<span style="color: yellow">this is bad</span>',
     b'<span style="color: red">this is evil</span>')
"""


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
        [2, 4, 8]
    """

    def wrapped(func):
        return map(func, data)

    return wrapped
