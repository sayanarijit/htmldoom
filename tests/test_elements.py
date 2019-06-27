import pytest

from htmldoom import elements as e


def test_double_quote():
    assert e.double_quote('abc"xyz') == '"abc\\"xyz"'


def test_style():
    txt = e.style(
        **{"color": "red", "text-align": "center", "font-family": ("Segoe UI", "Arial")}
    )
    assert txt == "color:'red';text-align:'center';font-family:'Segoe UI','Arial';"


def test_css():
    txt = e.css(**{"p": {"color": "red"}, ".center": {"text-align": "center"}})
    assert txt == "p{color:'red';}.center{text-align:'center';}"


def test__RawText():
    assert str(e._RawText("<div>&nbsp;</div>")) == "<div>&nbsp;</div>"
    assert e._RawText("<div>&nbsp;</div>").html == "<div>&nbsp;</div>"
    assert repr(e._RawText("<div>&nbsp;</div>")) == "b'<div>&nbsp;</div>'"


def test__Text():
    assert str(e._Text("foo &nbsp;<p>")) == "foo &amp;nbsp;&lt;p&gt;"


def test__Comment():
    assert str(e._Comment("Commenting -->")) == "<!-- Commenting --&gt; -->"
    assert repr(e._Comment("Commenting -->")) == "_Comment('Commenting -->')"
    assert isinstance(e._Comment("foo"), e._Declaration)


def test_DocType():
    assert str(e.DocType("html")) == "<!DOCTYPE html>"
    assert repr(e.DocType("html")) == "DocType('html')"
    assert (
        str(
            e.DocType(
                "HTML",
                "PUBLIC",
                "-//W3C//DTD HTML 4.01//EN",
                "http://www.w3.org/TR/html4/strict.dtd",
            )
        )
        == '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">'
    )
    assert isinstance(e.DocType("html"), e._Declaration)


def test_Br():
    assert str(e.Br()) == "<br />"


def test_A():
    assert str(e.A(href="#")) == '<a href="#"></a>'
    assert str(e.A(href="#")("foo")) == '<a href="#">foo</a>'
    assert str(e.A(href="#")(e._RawText("foo&"))) == '<a href="#">foo&</a>'


def test_Abbr():
    assert str(e.Abbr(title="foo")("bar")) == '<abbr title="foo">bar</abbr>'


def test_Address():
    assert str(e.Address()(f"foo{e.Br()}".encode())) == "<address>foo<br /></address>"


def test_Audio():
    assert str(e.Audio("controls")("foo")) == "<audio controls>foo</audio>"


def test_Script():
    assert (
        str(e.Script()('var x = "<p>&nbsp;</p>";'))
        == '<script>var x = "<p>&nbsp;</p>";</script>'
    )


def test_Style():
    assert str(e.Style()(e.css(p={"color": "red"}))) == "<style>p{color:'red';}</style>"


def test_TextArea():
    assert str(e.TextArea()("<div>")) == "<textarea>&lt;div&gt;</textarea>"
    assert str(e.TextArea()(b"<div>")) == "<textarea><div></textarea>"
    assert str(e.TextArea()(e._RawText("<div>"))) == "<textarea><div></textarea>"


def test_immutability():
    with pytest.raises(AttributeError) as exc:
        e._RawText("").value = "text"
    assert str(exc.value) == "can't set attribute"

    with pytest.raises(AttributeError) as exc:
        e._Text("").value = "text"
    assert str(exc.value) == "can't set attribute"

    with pytest.raises(AttributeError) as exc:
        e._Comment("").value = "text"
    assert str(exc.value) == "can't set attribute"

    with pytest.raises(AttributeError) as exc:
        e.DocType("").value = "text"
    assert str(exc.value) == "can't set attribute"

    with pytest.raises(AttributeError) as exc:
        e.P("").props = "text"
    assert str(exc.value) == "can't set attribute"


def test_equality():
    assert e._RawText("x") == e._RawText("x")
    assert e._RawText("x") != e._RawText("xy")
    assert hash(e._RawText("x")) == hash(e._RawText("x"))

    assert e._Text("x") == e._Text("x")
    assert e._Text("x") != e._Text("xy")
    assert hash(e._Text("x")) == hash(e._Text("x"))

    assert e._Comment("x") == e._Comment("x")
    assert e._Comment("x") != e._Comment("xy")
    assert hash(e._Comment("x")) == hash(e._Comment("x"))

    assert e.DocType("x") == e.DocType("x")
    assert e.DocType("x") != e.DocType("xy")
    assert hash(e.DocType("x")) == hash(e.DocType("x"))

    assert e.P("x") == e.P("x")
    assert e.P("x") != e.P("xy")
    assert hash(e.P("x")) == hash(e.P("x"))


def test_adhoc_composite_tag():
    Tag = e._new_adhoc_composite_tag("tag")
    assert Tag.tagname == "tag"
    assert str(Tag("x", y="z")("foo", "bar")) == '<tag x y="z">foobar</tag>'


def test_repr():
    assert repr(e.Br()) == "Br()"
    assert repr(e.Script("a", b="c")) == "Script('a', b='c')"
    assert repr(e.Script("a", b="c")("x")) == "Script('a', b='c')('x')"
    assert repr(e.Style("a", b="c")) == "Style('a', b='c')"
    assert repr(e.Style("a", b="c")("x")) == "Style('a', b='c')('x')"
    assert repr(e.Title("a", b="c")) == "Title('a', b='c')"
    assert repr(e.Title("a", b="c")("x")) == "Title('a', b='c')('x')"
    assert repr(e.P()) == "P()"
    assert repr(e.P()()) == "P()"
    assert repr(e.P("a")) == "P('a')"
    assert repr(e.P(b="c")) == "P(b='c')"
    assert repr(e.P("a", b="c")) == "P('a', b='c')"
    assert repr(e.P("a", b="c")("d")) == "P('a', b='c')('d')"
    assert (
        repr(e.P("a", b="c", repr="x")("d")) == "P('a', **{'b': 'c', 'repr': 'x'})('d')"
    )


def prefixed_str():
    assert e.P(e.Span("a")).prefixed_repr(preix="e.") == "e.P(e.Span('a'))"
