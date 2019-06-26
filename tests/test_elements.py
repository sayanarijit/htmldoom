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
    assert repr(e._RawText("<div>&nbsp;</div>")) == "<div>&nbsp;</div>"


def test__Text():
    assert repr(e._Text("foo &nbsp;<p>")) == "foo &amp;nbsp;&lt;p&gt;"


def test__Comment():
    assert repr(e._Comment("Commenting -->")) == "<!-- Commenting --&gt; -->"
    assert isinstance(e._Comment("foo"), e._Declaration)


def test_DocType():
    assert repr(e.DocType("html")) == "<!DOCTYPE html>"
    assert (
        repr(
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
    assert repr(e.A(href="#")) == '<a href="#"></a>'
    assert repr(e.A(href="#")("foo")) == '<a href="#">foo</a>'
    assert repr(e.A(href="#")(e._RawText("foo&"))) == '<a href="#">foo&</a>'


def test_Abbr():
    assert repr(e.Abbr(title="foo")("bar")) == '<abbr title="foo">bar</abbr>'


def test_Address():
    assert repr(e.Address()(f"foo{e.Br()}".encode())) == "<address>foo<br /></address>"


def test_Audio():
    assert repr(e.Audio("controls")("foo")) == "<audio controls>foo</audio>"


def test_Script():
    assert (
        repr(e.Script()('var x = "<p>&nbsp;</p>";'))
        == '<script>var x = "<p>&nbsp;</p>";</script>'
    )


def test_Style():
    assert (
        repr(e.Style()(e.css(p={"color": "red"}))) == "<style>p{color:'red';}</style>"
    )


def test_TextArea():
    assert repr(e.TextArea()("<div>")) == "<textarea>&lt;div&gt;</textarea>"
    assert repr(e.TextArea()(b"<div>")) == "<textarea><div></textarea>"
    assert repr(e.TextArea()(e._RawText("<div>"))) == "<textarea><div></textarea>"


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
        e._Tag("").attrs = "text"
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

    assert e._Tag("x") == e._Tag("x")
    assert e._Tag("x") != e._Tag("xy")
    assert hash(e._Tag("x")) == hash(e._Tag("x"))


def test_adhoc_composite_tag():
    Tag = e._new_adhoc_composite_tag("tag")
    assert Tag.tagname == "tag"
    assert str(Tag("x", y="z")("foo", "bar")) == '<tag x y="z">foobar</tag>'
