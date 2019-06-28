from htmldoom import render
from htmldoom.elements import _composite_tag, _raw, _txt, p


def test_p():
    assert render(p()(_txt("x"))) == "<p>x</p>"
    assert render(p()(_txt("x"))) == "<p>x</p>"
    assert render(p("a")(_txt("x"))) == "<p a>x</p>"
    assert render(p("a", b="c")(_txt("x"))) == '<p a b="c">x</p>'
    assert render(p(b="c")(_txt("x"))) == '<p b="c">x</p>'
    assert render(p(b="c")(p()(_txt("x")))) == '<p b="c"><p>x</p></p>'
