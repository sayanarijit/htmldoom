import pytest

from htmldoom.value_loader import loadvalues


def test_loadvalues():
    values = loadvalues("tests/assets/values/valid")
    assert values.a == "<p>a</p>"
    assert values.b == "1&lt;3&gt;2"
    assert values.c.d == '<p class="x">x</p>'


def test_loadvalues_unsupported():
    with pytest.raises(TypeError):
        loadvalues("tests/assets/values/invalid/unsupported_type")


def test_loadvalues_no_ext():
    with pytest.raises(NameError):
        loadvalues("tests/assets/values/invalid/no_ext")


def test_loadvalues_duplicate():
    with pytest.raises(NameError):
        loadvalues("tests/assets/values/invalid/duplicate")
