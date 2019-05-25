from html import escape

import re
import typing as t


__author__ = "Arijit Basu"
__email__ = "sayanarijit@gmail.com"
__homepage__ = "https://github.com/sayanarijit/htmldoom"
__description__ = "Write safer and cleaner HTML using Python"
__version__ = "v0.1"
__license__ = "MIT"


def double_quote(txt: str) -> str:
    """Double quote strings safely for attributes.
    
    Usage:
        >>> double_quote('abc"xyz')
        '"abc\\"xyz"'
    """
    return '"{}"'.format(txt.replace('"', '\\"'))


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


def style(**code: t.Union[str, t.Iterable]) -> str:
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


class _RawText:
    """Use it for unescaped HTML.
    
    Usage:
        >>> _RawText("<div>&nbsp;</div>")
        <div>&nbsp;</div>
    """

    def __init__(self, value: str) -> None:
        self.value = value

    def __repr__(self) -> str:
        return self.value


class _Text:
    """Use it for escaped texts.
    
    Usage:
        >>> _Text("foo &nbsp;<p>")
        foo &amp;nbsp;&lt;p&gt;
    """

    def __init__(self, value: str) -> None:
        self.value = value

    def __repr__(self) -> str:
        return escape(self.value)


class _Declaration:
    """All declarations such as comments, doctypes etc. Do not use it directly."""

    pass


class _Comment(_Declaration):
    """Use it to declare HTML comments: <!-- -->.
    
    Usage:
        >>> _Comment("Commenting -->")
        <!-- Commenting --&gt; -->
    """

    def __init__(self, value: str) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"<!-- {escape(self.value)} -->"


class DocType(_Declaration):
    """The DOCTYPE declaration: <!DOCTYPE>.
    
    Usage:
        >>> DocType("html")
        <!DOCTYPE html>
        >>> 
        >>> DocType("HTML", "PUBLIC", "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd")
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
    """

    def __init__(self, *attrs: str) -> None:
        self.attrs = attrs

    def __repr__(self) -> str:
        return "<!DOCTYPE {}>".format(
            " ".join(
                double_quote(x) if re.sub(r"[a-zA-Z0-9]", "", x) else x
                for x in self.attrs
            )
        )


class _Tag:
    """Base class for all tags."""

    tagname: str = ""

    def __init__(self, *attrs: str, **props: str) -> None:
        self.attrs = attrs
        self.props = props

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

    def __init__(self, *attrs: str, **props: str) -> None:
        super().__init__(*attrs, **props)
        self.child = ""

    def __call__(self, child: t.Union["_ELementType", str, bytes]) -> "_SingleChildTag":
        tag = type(self)(*self.attrs, **self.props)
        if isinstance(child, str):
            tag.child = _Text(child)
            return tag
        if isinstance(child, bytes):
            tag.child = _RawText(child.decode("utf-8"))
            return tag
        tag.child = child
        return tag

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

    def __init__(self, *attrs: str, **props: str) -> None:
        super().__init__(*attrs, **props)
        self.children: _ElementType = []

    def __call__(self, *children: t.Union[_ElementType, str, bytes]) -> "_CompositeTag":
        tag = type(self)(*self.attrs, **self.props)
        for c in children:
            if isinstance(c, str):
                tag.children.append(_Text(c))
                continue
            if isinstance(c, bytes):
                tag.children.append(_RawText(c.decode("utf-8")))
                continue
            tag.children.append(c)
        return tag

    def __repr__(self) -> str:
        return render_element(self)


class A(_CompositeTag):
    """Anchor tag: <a>.
    
    Usage:
        >>> repr(A(href="#"))
        <a href="#"></a>
        >>> 
        >>> render_element(A(href="#")("foo"))
        <a href="#">foo</a>
    """

    tagname = "a"


class Abbr(_CompositeTag):
    """Abbreviation tag: <abbr>.

    Usage:
        >>> repr(Abbr(title="World Health Organization")("WHO"))
        <abbr title="World Health Organization">WHO</abbr>
    """

    tagname = "abbr"


class Address(_CompositeTag):
    """Address tag: <address>.
    
    Usage:
        >>> repr(Address()(_RawText(f"
        ... John Doe{Br()}
        ... Visit us at:{Br()}
        ... Example.com{Br()}
        ... Box 564, Disneyland{Br()}
        ... USA"))
        <address>John Doe<br />
        Visit us at:<br />
        Example.com<br />
        Box 564, Disneyland<br />
        USA</address>
    """

    tagname = "address"


# TODO: Create doc strings and unit tests from here...


class Area(_LeafTag):
    tagname = "area"


class Article(_CompositeTag):
    tagname = "article"


class Aside(_CompositeTag):
    tagname = "aside"


class Audio(_CompositeTag):
    tagname = "audio"


class B(_CompositeTag):
    tagname = "b"


class Base(_LeafTag):
    tagname = "base"


class BDI(_CompositeTag):
    tagname = "bdi"


class BDO(_CompositeTag):
    tagname = "bdo"


class BlockQuote(_CompositeTag):
    tagname = "blockquote"


class Body(_CompositeTag):
    tagname = "body"


class Br(_LeafTag):
    """Line break: <br>.
    
    Usage:
        >>> repr(Br())
        <br />
    """

    tagname = "br"


class Button(_CompositeTag):
    tagname = "button"


class Canvas(_CompositeTag):
    tagname = "canvas"


class Caption(_CompositeTag):
    tagname = "caption"


class Cite(_CompositeTag):
    tagname = "cite"


class Code(_CompositeTag):
    tagname = "code"


class Col(_LeafTag):
    tagname = "col"


class ColGroup(_CompositeTag):
    tagname = "colgroup"


class Data(_CompositeTag):
    tagname = "data"


class DataList(_CompositeTag):
    tagname = "datalist"


class DD(_CompositeTag):
    tagname = "dd"


class Del(_CompositeTag):
    tagname = "del"


class Details(_CompositeTag):
    tagname = "details"


class DFN(_CompositeTag):
    tagname = "dfn"


class Dialog(_CompositeTag):
    tagname = "dialog"


class Div(_CompositeTag):
    tagname = "div"


class DL(_CompositeTag):
    tagname = "dl"


class DT(_CompositeTag):
    tagname = "dt"


class Em(_CompositeTag):
    tagname = "em"


class Embed(_CompositeTag):
    tagname = "embed"


class FieldSet(_CompositeTag):
    tagname = "fieldset"


class FigCaption(_CompositeTag):
    tagname = "fieldcaption"


class Figure(_CompositeTag):
    tagname = "figure"


class Footer(_CompositeTag):
    tagname = "footer"


class Form(_CompositeTag):
    tagname = "form"


class H1(_CompositeTag):
    tagname = "h1"


class H2(_CompositeTag):
    tagname = "h2"


class H3(_CompositeTag):
    tagname = "h3"


class H4(_CompositeTag):
    tagname = "h4"


class H5(_CompositeTag):
    tagname = "h5"


class H6(_CompositeTag):
    tagname = "h6"


class Head(_CompositeTag):
    tagname = "head"


class Header(_CompositeTag):
    tagname = "header"


class HR(_LeafTag):
    tagname = "hr"


class HTML(_CompositeTag):
    tagname = "html"


class I(_CompositeTag):
    tagname = "i"


class IFrame(_CompositeTag):
    tagname = "iframe"


class Img(_LeafTag):
    tagname = "image"


class Input(_LeafTag):
    tagname = "input"


class Ins(_CompositeTag):
    tagname = "ins"


class Kbd(_CompositeTag):
    tagname = "kbd"


class Label(_CompositeTag):
    tagname = "label"


class Legend(_CompositeTag):
    tagname = "legend"


class LI(_CompositeTag):
    tagname = "li"


class Link(_LeafTag):
    tagname = "link"


class Main(_CompositeTag):
    tagname = "main"


class Map(_CompositeTag):
    tagname = "map"


class Mark(_CompositeTag):
    tagname = "mark"


class Meta(_LeafTag):
    tagname = "meta"


class Meter(_CompositeTag):
    tagname = "meter"


class Nav(_CompositeTag):
    tagname = "nav"


class NoScript(_CompositeTag):
    tagname = "noscript"


class Object(_CompositeTag):
    tagname = "object"


class OL(_CompositeTag):
    tagname = "ol"


class OptGroup(_CompositeTag):
    tagname = "optgroup"


class Option(_CompositeTag):
    tagname = "option"


class Output(_CompositeTag):
    tagname = "output"


class P(_CompositeTag):
    tagname = "p"


class Param(_LeafTag):
    tagname = "param"


class Picture(_CompositeTag):
    tagname = "picture"


class Pre(_CompositeTag):
    tagname = "pre"


class Progress(_CompositeTag):
    tagname = "progress"


class Q(_CompositeTag):
    tagname = "q"


class RP(_CompositeTag):
    tagname = "rp"


class RT(_CompositeTag):
    tagname = "rt"


class Ruby(_CompositeTag):
    tagname = "ruby"


class S(_CompositeTag):
    tagname = "s"


class Samp(_CompositeTag):
    tagname = "samp"


class Script(_SingleChildTag):
    tagname = "script"

    def __call__(self, child: str) -> "Script":
        s = Script(*self.attrs, **self.props)
        s.child = child
        return s


class Section(_CompositeTag):
    tagname = "section"


class Select(_CompositeTag):
    tagname = "select"


class Small(_CompositeTag):
    tagname = "small"


class Source(_LeafTag):
    tagname = "source"


class Span(_CompositeTag):
    tagname = "span"


class Strong(_CompositeTag):
    tagname = "strong"


class Style(_SingleChildTag):
    tagname = "style"

    def __call__(self, child: str) -> "Style":
        s = Style(*self.attrs, **self.props)
        s.child = child
        return s


class Sub(_CompositeTag):
    tagname = "sub"


class Summary(_CompositeTag):
    tagname = "summary"


class Sup(_CompositeTag):
    tagname = "sup"


class SVG(_CompositeTag):
    tagname = "svg"


class Table(_CompositeTag):
    tagname = "table"


class TBody(_CompositeTag):
    tagname = "tbody"


class TD(_CompositeTag):
    tagname = "td"


class Template(_CompositeTag):
    tagname = "template"


class TextArea(_SingleChildTag):
    tagname = "textarea"


class TFoot(_CompositeTag):
    tagname = "tfoot"


class TH(_CompositeTag):
    tagname = "th"


class THead(_CompositeTag):
    tagname = "thead"


class Time(_CompositeTag):
    tagname = "time"


class Title(_SingleChildTag):
    tagname = "title"


class TR(_CompositeTag):
    tagname = "tr"


class Track(_LeafTag):
    tagname = "track"


class U(_CompositeTag):
    tagname = "u"


class UL(_CompositeTag):
    tagname = "ul"


class Var(_CompositeTag):
    tagname = "var"


class Video(_CompositeTag):
    tagname = "video"


class WBr(_LeafTag):
    tagname = "wbr"
