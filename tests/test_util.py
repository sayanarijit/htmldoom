from html import escape

import pytest

from htmldoom import elements as e
from htmldoom import functions as fn
from htmldoom.base import raw, txt
from htmldoom.util import loadraw, loadtxt, render, renders


def test_render():
    assert render("&nbsp;") == "&amp;nbsp;"
    assert render(txt("&nbsp;")) == "&amp;nbsp;"
    assert render(b"&nbsp;") == "&nbsp;"
    assert render(raw("&nbsp;")) == "&nbsp;"
    assert render(e.p(), e.p) == "<p></p><p></p>"
    with pytest.raises(ValueError):
        render(1)


def test_renders():
    @renders(e.p()("{x}"), e.p()("{x} again"))
    def render_paras(data: dict) -> dict:
        return {"x": data["x"]}

    assert render_paras({"x": "y"}) == b"<p>y</p><p>y again</p>"

    dangerous_script = "<script>I'm dangerous</script>"
    assert render_paras({"x": dangerous_script}) == raw(
        f"<p>{escape(dangerous_script)}</p><p>{escape(dangerous_script)} again</p>"
    )
    assert render_paras({"x": raw(dangerous_script)}) == raw(
        f"<p>{dangerous_script}</p><p>{dangerous_script} again</p>"
    )

    @renders(e.li()("{item}"))
    def render_list_item(item):
        return {"item": item}

    @renders(e.p()("{foo}"), e.ul()("{list_items}"))
    def render_component():
        return {
            "foo": e.hr,
            "list_items": fn.foreach(["a", "b", "c"])(lambda x: render_list_item(x)),
        }

    assert (
        render(render_component())
        == "<p><hr /></p><ul><li>a</li><li>b</li><li>c</li></ul>"
    )


def test_loadtxt_dynamic():
    @renders(loadtxt("tests/assets/html_components/component.html"))
    def render_component():
        return {"foo": "bar"}

    assert render_component() == txt("<p>bar</p>")


def test_loadtxt_static():
    @renders(loadtxt("tests/assets/html_components/component.html", static=True))
    def render_component():
        return {"foo": "bar"}

    assert render_component() == txt("<p>{foo}</p>")


def test_loadraw_dynamic():
    @renders(loadraw("tests/assets/html_components/component.html"))
    def render_component():
        return {"foo": "bar"}

    assert render_component() == raw("<p>bar</p>")


def test_loadraw_static():
    @renders(loadraw("tests/assets/html_components/component.html", static=True))
    def render_component():
        return {"foo": "bar"}

    assert render_component() == raw("<p>{foo}</p>")
