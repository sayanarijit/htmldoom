import pytest

from htmldoom import elements as e
from htmldoom.base import raw, txt
from htmldoom.util import render


def test_render():
    assert render("&nbsp;") == "&amp;nbsp;"
    assert render(txt("&nbsp;")) == "&amp;nbsp;"
    assert render(b"&nbsp;") == "&nbsp;"
    assert render(raw("&nbsp;")) == "&nbsp;"
    assert render(e.p(), e.p()) == "<p></p><p></p>"
    with pytest.raises(ValueError):
        render(1)
