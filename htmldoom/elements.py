"""The core elements used to render HTML.

Example:
    >>> from htmldoom import elements as e
    >>> e.P(style=e.style(color="red"))("This is a paragraph")
    <p style="color: 'red';">This is a paragraph</p>
"""

import re
import typing as t
from collections import namedtuple
from functools import lru_cache
from html import escape
from types import MappingProxyType

MAX_CACHE_SIZE = 12800


@lru_cache(maxsize=MAX_CACHE_SIZE)
def double_quote(txt: str) -> str:
    """Double quote strings safely for attributes.
    
    Usage:
        >>> double_quote('abc"xyz')
        '"abc\\"xyz"'
    """
    return '"{}"'.format(txt.replace('"', '\\"'))


@lru_cache(maxsize=MAX_CACHE_SIZE)
def render_element(element: "_ElementType") -> str:
    """Render any element.
    
    Usage:
        >>> render_element(A(href="#"))
        '<a href="#"></a>'
        >>> 
        >>> render_element(A(href="#")("foo"))
        '<a href="#">foo</a>'
    """
    if not isinstance(element, _CompositeTag):
        return str(element)

    return "<{0}{1}{2}>{3}</{0}>".format(
        element.tagname,
        " "
        + (
            " ".join(
                double_quote(x) if re.sub(r"[a-zA-Z0-9]", "", x) else x
                for x in element.attrs
            )
        )
        if element.attrs
        else "",
        " " + (" ".join(f"{k}={double_quote(element.props[k])}" for k in element.props))
        if element.props
        else "",
        "".join(map(render_element, element.children)),
    )


def css(**code: t.Dict[str, t.Dict[str, t.Union[str, t.Iterable]]]) -> str:
    """Helps rendering CSS code.
    
    Usage:
        >>> css(**{
        ...     "p": {"color": "red"},
        ...     ".center": {"text-align": "center"},
        ... })
	"p{color:'red';}.center{text-align:'center';}"
    """
    return "".join(f"{k}{{{style(**(code[k]))}}}" for k in code)


def style(**code: t.Union[str, t.Iterable[str]]) -> str:
    """Use it to render styles.
    
    Usage:
        >>> style(**{
        ...     "color": "red",
        ...     "text-align": "center",
        ...     "font-family": ("Segoe UI", "Arial")
        ... })
        "color:'red';text-align:'center';font-family:'Segoe UI','Arial';"
    """
    return (
        ";".join(
            f"{k}:{repr(v)}" if isinstance(v, str) else f"{k}:{','.join(map(repr, v))}"
            for k, v in code.items()
        )
        + ";"
    )


@lru_cache(maxsize=MAX_CACHE_SIZE)
class _RawText:
    """Use it for unescaped text.
    
    Usage:
        >>> _RawText("<div>&nbsp;</div>")
        <div>&nbsp;</div>
    """

    __slots__ = ["value"]

    def __init__(self, value: str) -> None:
        super().__setattr__("value", value)

    def __setattr__(self, name, value):
        raise AttributeError("can't set attribute")

    def __eq__(self, value):
        return type(self) == type(value) and self.value == value.value

    def __hash__(self):
        return hash(f"type(self):self.value")

    def __repr__(self) -> str:
        return self.value


@lru_cache(maxsize=MAX_CACHE_SIZE)
class _Text:
    """Use it for escaped texts.
    
    Usage:
        >>> _Text("foo &nbsp;<p>")
        foo &amp;nbsp;&lt;p&gt;
    """

    __slots__ = ["value"]

    def __init__(self, value: str) -> None:
        super().__setattr__("value", value)

    def __setattr__(self, name, value):
        raise AttributeError("can't set attribute")

    def __eq__(self, value):
        return type(self) == type(value) and self.value == value.value

    def __hash__(self):
        return hash(f"type(self):self.value")

    def __repr__(self) -> str:
        return escape(self.value)


class _Declaration:
    """All declarations such as comments, doctypes etc. Do not use it directly."""

    pass


@lru_cache(maxsize=MAX_CACHE_SIZE)
class _Comment(_Declaration):
    """Use it to declare HTML comments: <!-- -->.
    
    Usage:
        >>> _Comment("Commenting -->")
        <!-- Commenting --&gt; -->
    """

    __slots__ = ["value"]

    def __init__(self, value: str) -> None:
        super().__setattr__("value", value)

    def __setattr__(self, name, value):
        raise AttributeError("can't set attribute")

    def __eq__(self, value):
        return type(self) == type(value) and self.value == value.value

    def __hash__(self):
        return hash(f"type(self):self.value")

    def __repr__(self) -> str:
        return f"<!-- {escape(self.value)} -->"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class DocType(_Declaration):
    """The DOCTYPE declaration: <!DOCTYPE>.
    
    Usage:
        >>> DocType("html")
        <!DOCTYPE html>
        >>> 
        >>> DocType("HTML", "PUBLIC", "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd")
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
    """

    __slots__ = ["attrs"]

    def __init__(self, *attrs: str) -> None:
        super().__setattr__("attrs", tuple(attrs))

    def __setattr__(self, name, value):
        raise AttributeError("can't set attribute")

    def __eq__(self, value):
        return type(self) == type(value) and self.attrs == value.attrs

    def __hash__(self):
        return hash(f"type(self):self.attrs")

    def __repr__(self) -> str:
        return "<!DOCTYPE {}>".format(
            " ".join(
                double_quote(x) if re.sub(r"[a-zA-Z0-9]", "", x) else x
                for x in self.attrs
            )
        )


class _Tag:
    """Base class for all tags."""

    __slots__ = ["attrs", "props"]

    tagname: str = ""

    def __init__(self, *attrs: str, **props: str) -> None:
        super().__setattr__("attrs", tuple(attrs))
        super().__setattr__("props", MappingProxyType(props))

    def __setattr__(self, name, value):
        raise AttributeError("can't set attribute")

    def __eq__(self, value):
        return (
            type(self) == type(value)
            and self.attrs == value.attrs
            and self.props == value.props
        )

    def __hash__(self):
        return hash(f"type(self):self.attrs:self.props")

    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def __repr__(self) -> str:
        return "<{}{}{} />".format(
            self.tagname,
            " "
            + (
                " ".join(
                    double_quote(x) if re.sub(r"[a-zA-Z0-9]", "", x) else x
                    for x in self.attrs
                )
            )
            if self.attrs
            else "",
            " " + (" ".join(f"{k}={double_quote(self.props[k])}" for k in self.props))
            if self.props
            else "",
        )


class _LeafTag(_Tag):
    """A leaf tag cannot have children."""

    pass


_ElementType = t.Union[_RawText, _Text, _Declaration, _Tag]


class _SingleChildTag(_Tag):
    """A single child tag can have only one child."""

    __slots__ = ["attrs", "props", "child"]

    def __init__(self, *attrs: str, **props: str) -> None:
        super().__init__(*attrs, **props)
        super().__class__.__setattr__(self, "child", _Text(""))

    def __eq__(self, value):
        return (
            type(self) == type(value)
            and self.attrs == value.attrs
            and self.props == value.props
            and self.child == value.child
        )

    def __hash__(self):
        return hash(f"type(self):self.attrs:self.props:self.child")

    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def __call__(self, child: t.Union["_ELementType", str, bytes]) -> "_SingleChildTag":
        _child = child
        if isinstance(child, str):
            _child = _Text(child)
        elif isinstance(child, bytes):
            _child = _RawText(child.decode("utf-8"))
        tag = type(self)(*self.attrs, **self.props)
        super(type(tag), tag).__class__.__setattr__(tag, "child", _child)
        return tag

    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def __repr__(self) -> str:
        return "<{0}{1}{2}>{3}</{0}>".format(
            self.tagname,
            " "
            + (
                " ".join(
                    double_quote(x) if re.sub(r"[a-zA-Z0-9]", "", x) else x
                    for x in self.attrs
                )
            )
            if self.attrs
            else "",
            " " + (" ".join(f"{k}={double_quote(self.props[k])}" for k in self.props))
            if self.props
            else "",
            render_element(self.child),
        )


class _CompositeTag(_Tag):
    """A composite tag can have children."""

    __slots__ = ["attrs", "props", "children"]

    def __init__(self, *attrs: str, **props: str) -> None:
        super().__init__(*attrs, **props)
        super().__class__.__setattr__(self, "children", tuple())

    def __eq__(self, value):
        return (
            type(self) == type(value)
            and self.attrs == value.attrs
            and self.props == value.props
            and self.children == value.children
        )

    def __hash__(self):
        return hash(f"type(self):self.attrs:self.children")

    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def __call__(self, *children: t.Union[_ElementType, str, bytes]) -> "_CompositeTag":
        _children = []
        for c in children:
            if isinstance(c, str):
                _children.append(_Text(c))
                continue
            if isinstance(c, bytes):
                _children.append(_RawText(c.decode("utf-8")))
                continue
            _children.append(c)
        tag = type(self)(*self.attrs, **self.props)
        super(type(tag), tag).__class__.__setattr__(tag, "children", tuple(_children))
        return tag

    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def __repr__(self) -> str:
        return render_element(self)


@lru_cache(maxsize=MAX_CACHE_SIZE)
class A(_CompositeTag):
    """Anchor tag: <a>.
    
    Usage:
        >>> A(href="#")
        <a href="#"></a>
        >>> 
        >>> A(href="#")("foo")
        <a href="#">foo</a>
    """

    tagname = "a"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Abbr(_CompositeTag):
    """Abbreviation tag: <abbr>.

    Usage:
        >>> Abbr(title="World Health Organization")("WHO")
        <abbr title="World Health Organization">WHO</abbr>
    """

    tagname = "abbr"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Address(_CompositeTag):
    """Address tag: <address>.
    
    Usage:
        >>> Address()(_RawText(f"
        ... John Doe{Br()}
        ... Visit us at:{Br()}
        ... Example.com{Br()}
        ... Box 564, Disneyland{Br()}
        ... USA")
        <address>John Doe<br />
        Visit us at:<br />
        Example.com<br />
        Box 564, Disneyland<br />
        USA</address>
    """

    tagname = "address"


# TODO: Create doc strings and unit tests from here...


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Area(_LeafTag):
    tagname = "area"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Article(_CompositeTag):
    tagname = "article"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Aside(_CompositeTag):
    tagname = "aside"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Audio(_CompositeTag):
    tagname = "audio"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class B(_CompositeTag):
    tagname = "b"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Base(_LeafTag):
    tagname = "base"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class BDI(_CompositeTag):
    tagname = "bdi"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class BDO(_CompositeTag):
    tagname = "bdo"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class BlockQuote(_CompositeTag):
    tagname = "blockquote"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Body(_CompositeTag):
    tagname = "body"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Br(_LeafTag):
    """Line break: <br>.
    
    Usage:
        >>> repr(Br())
        <br />
    """

    tagname = "br"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Button(_CompositeTag):
    tagname = "button"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Canvas(_CompositeTag):
    tagname = "canvas"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Caption(_CompositeTag):
    tagname = "caption"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Cite(_CompositeTag):
    tagname = "cite"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Code(_CompositeTag):
    tagname = "code"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Col(_LeafTag):
    tagname = "col"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class ColGroup(_CompositeTag):
    tagname = "colgroup"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Data(_CompositeTag):
    tagname = "data"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class DataList(_CompositeTag):
    tagname = "datalist"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class DD(_CompositeTag):
    tagname = "dd"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Del(_CompositeTag):
    tagname = "del"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Details(_CompositeTag):
    tagname = "details"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class DFN(_CompositeTag):
    tagname = "dfn"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Dialog(_CompositeTag):
    tagname = "dialog"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Div(_CompositeTag):
    tagname = "div"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class DL(_CompositeTag):
    tagname = "dl"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class DT(_CompositeTag):
    tagname = "dt"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Em(_CompositeTag):
    tagname = "em"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Embed(_CompositeTag):
    tagname = "embed"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FieldSet(_CompositeTag):
    tagname = "fieldset"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FigCaption(_CompositeTag):
    tagname = "fieldcaption"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Figure(_CompositeTag):
    tagname = "figure"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Footer(_CompositeTag):
    tagname = "footer"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Form(_CompositeTag):
    tagname = "form"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class H1(_CompositeTag):
    tagname = "h1"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class H2(_CompositeTag):
    tagname = "h2"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class H3(_CompositeTag):
    tagname = "h3"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class H4(_CompositeTag):
    tagname = "h4"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class H5(_CompositeTag):
    tagname = "h5"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class H6(_CompositeTag):
    tagname = "h6"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Head(_CompositeTag):
    tagname = "head"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Header(_CompositeTag):
    tagname = "header"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class HR(_LeafTag):
    tagname = "hr"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class HTML(_CompositeTag):
    tagname = "html"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class I(_CompositeTag):
    tagname = "i"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class IFrame(_CompositeTag):
    tagname = "iframe"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Img(_LeafTag):
    tagname = "img"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Input(_LeafTag):
    tagname = "input"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Ins(_CompositeTag):
    tagname = "ins"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Kbd(_CompositeTag):
    tagname = "kbd"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Label(_CompositeTag):
    tagname = "label"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Legend(_CompositeTag):
    tagname = "legend"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class LI(_CompositeTag):
    tagname = "li"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Link(_LeafTag):
    tagname = "link"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Main(_CompositeTag):
    tagname = "main"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Map(_CompositeTag):
    tagname = "map"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Mark(_CompositeTag):
    tagname = "mark"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Meta(_LeafTag):
    tagname = "meta"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Meter(_CompositeTag):
    tagname = "meter"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Nav(_CompositeTag):
    tagname = "nav"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class NoScript(_CompositeTag):
    tagname = "noscript"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Object(_CompositeTag):
    tagname = "object"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class OL(_CompositeTag):
    tagname = "ol"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class OptGroup(_CompositeTag):
    tagname = "optgroup"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Option(_CompositeTag):
    tagname = "option"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Output(_CompositeTag):
    tagname = "output"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class P(_CompositeTag):
    tagname = "p"


class Param(_LeafTag):
    tagname = "param"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Picture(_CompositeTag):
    tagname = "picture"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Pre(_CompositeTag):
    tagname = "pre"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Progress(_CompositeTag):
    tagname = "progress"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Q(_CompositeTag):
    tagname = "q"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class RP(_CompositeTag):
    tagname = "rp"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class RT(_CompositeTag):
    tagname = "rt"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Ruby(_CompositeTag):
    tagname = "ruby"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class S(_CompositeTag):
    tagname = "s"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Samp(_CompositeTag):
    tagname = "samp"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Script(_SingleChildTag):
    tagname = "script"

    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def __call__(self, child: str) -> "Script":
        s = Script(*self.attrs, **self.props)
        super(type(s), s).__class__.__setattr__(s, "child", _RawText(child))
        return s


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Section(_CompositeTag):
    tagname = "section"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Select(_CompositeTag):
    tagname = "select"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Small(_CompositeTag):
    tagname = "small"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Source(_LeafTag):
    tagname = "source"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Span(_CompositeTag):
    tagname = "span"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Strong(_CompositeTag):
    tagname = "strong"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Style(_SingleChildTag):
    tagname = "style"

    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def __call__(self, child: str) -> "Style":
        s = Style(*self.attrs, **self.props)
        super(type(s), s).__class__.__setattr__(s, "child", _RawText(child))
        return s


class Sub(_CompositeTag):
    tagname = "sub"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Summary(_CompositeTag):
    tagname = "summary"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Sup(_CompositeTag):
    tagname = "sup"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class SVG(_CompositeTag):
    tagname = "svg"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Table(_CompositeTag):
    tagname = "table"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class TBody(_CompositeTag):
    tagname = "tbody"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class TD(_CompositeTag):
    tagname = "td"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Template(_CompositeTag):
    tagname = "template"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class TextArea(_SingleChildTag):
    tagname = "textarea"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class TFoot(_CompositeTag):
    tagname = "tfoot"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class TH(_CompositeTag):
    tagname = "th"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class THead(_CompositeTag):
    tagname = "thead"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Time(_CompositeTag):
    tagname = "time"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Title(_SingleChildTag):
    tagname = "title"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class TR(_CompositeTag):
    tagname = "tr"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Track(_LeafTag):
    tagname = "track"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class U(_CompositeTag):
    tagname = "u"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class UL(_CompositeTag):
    tagname = "ul"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Var(_CompositeTag):
    tagname = "var"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Video(_CompositeTag):
    tagname = "video"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class WBr(_LeafTag):
    tagname = "wbr"
