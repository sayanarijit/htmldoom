from htmldoom import render
from htmldoom.base import composite_tag, leaf_tag, txt
from htmldoom.elements import input, p


def test_leaf_tag():
    assert render(leaf_tag(lambda: "input")()) == "<input />"
    assert render(input()) == "<input />"
    assert render(input("a")) == "<input a />"
    assert render(input("a", b="c")) == '<input a b="c" />'
    assert render(input(b="c")) == '<input b="c" />'


def test_composite_tag():
    assert render(composite_tag(lambda: "p")()()) == "<p></p>"
    assert render(p()(txt("x"))) == "<p>x</p>"
    assert render(p()(txt("x"))) == "<p>x</p>"
    assert render(p("a")(txt("x"))) == "<p a>x</p>"
    assert render(p("a", b="c")(txt("x"))) == '<p a b="c">x</p>'
    assert render(p(b="c")(txt("x"))) == '<p b="c">x</p>'
    assert render(p(b="c")(p()(txt("x")))) == '<p b="c"><p>x</p></p>'
