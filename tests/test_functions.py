import pytest

from htmldoom import functions as fn

# Switch case


def test_switch_case():
    assert fn.switch({True: lambda: 1, fn.Case.DEFAULT: lambda: 0}) == 1
    assert fn.switch({False: lambda: 1, fn.Case.DEFAULT: lambda: 0}) == 0


# Loop


def test_foreach():
    numbers = [1, 2, 3]
    list(fn.foreach(numbers)(lambda n: n * 2)) == [2, 4, 3]
    tuple(fn.foreach(numbers)(lambda n: n * 2)) == (2, 4, 3)
