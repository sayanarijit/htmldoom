import pytest

from htmldoom import elements as e
from htmldoom.base import raw, txt
from htmldoom.util import render, renders


def test_render():
    assert render("&nbsp;") == "&amp;nbsp;"
    assert render(txt("&nbsp;")) == "&amp;nbsp;"
    assert render(b"&nbsp;") == "&nbsp;"
    assert render(raw("&nbsp;")) == "&nbsp;"
    assert render(e.p(), e.p()) == "<p></p><p></p>"
    with pytest.raises(ValueError):
        render(1)


def test_renders():
    @renders(e.p()("{x}"), e.p()("{x} again"))
    def render_paras(data: dict) -> dict:
        return {"x": data["x"]}

    assert render_paras({"x": "y"}) == "<p>y</p><p>y again</p>"

    render_paras = renders(e.p()("{x}"), e.p()("{x} again"))(
        lambda data: {"x": data["x"]}
    )
    assert render_paras({"x": "y"}) == "<p>y</p><p>y again</p>"
