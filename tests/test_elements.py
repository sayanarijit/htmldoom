from htmldoom import render
from htmldoom.base import composite_tag, leaf_tag, txt
from htmldoom.elements import input_, p


def test_leaf_tag():
    assert render(leaf_tag("input")()) == "<input />"
    assert render(input_()) == "<input />"
    assert render(input_("a")) == "<input a />"
    assert render(input_("a", b="c")) == '<input a b="c" />'
    assert render(input_(b="c")) == '<input b="c" />'


def test_composite_tag():
    assert render(composite_tag("p")()()) == "<p></p>"
    assert render(p()(txt("x"))) == "<p>x</p>"
    assert render(p()(txt("x"))) == "<p>x</p>"
    assert render(p("a")(txt("x"))) == "<p a>x</p>"
    assert render(p("a", b="c")(txt("x"))) == '<p a b="c">x</p>'
    assert render(p(b="c")(txt("x"))) == '<p b="c">x</p>'
    assert render(p(b="c")(p()(txt("x")))) == '<p b="c"><p>x</p></p>'
