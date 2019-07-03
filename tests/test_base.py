import pytest

from htmldoom import render
from htmldoom.base import comment, composite_tag, doctype, leaf_tag


def test_comment():
    assert render(comment("abc")) == "<!-- abc -->"


def test_doctype():
    assert render(doctype("html", "a b c")) == '<!DOCTYPE html "a b c">'


def test_leaf_tag():
    with pytest.raises(ValueError):
        render(leaf_tag("a")(leaf_tag("b")))
    with pytest.raises(ValueError):
        render(composite_tag("a")(composite_tag("b")))

    with pytest.raises(ValueError):
        render(leaf_tag("a")(leaf_tag("b")()))
    with pytest.raises(ValueError):
        render(composite_tag("a")(composite_tag("b")()))
