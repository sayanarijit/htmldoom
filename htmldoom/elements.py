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

__all__ = [
    "double_quote",
    "render_element",
    "css",
    "style",
    "_RawText",
    "_Text",
    "_Declaration",
    "_Comment",
    "DocType",
    "_Tag",
    "_LeafTag",
    "_SingleChildTag",
    "_CompositeTag",
    "_new_adhoc_composite_tag",
    "A",
    "Abbr",
    "Address",
    "Animate",
    "AnimateMotion",
    "AnimateTransform",
    "Area",
    "Article",
    "Aside",
    "Audio",
    "B",
    "Base",
    "BDI",
    "BDO",
    "BlockQuote",
    "Body",
    "Br",
    "Button",
    "Canvas",
    "Caption",
    "Center",
    "Circle",
    "CirclePath",
    "Cite",
    "Code",
    "Col",
    "ColGroup",
    "Color_Profile",
    "Data",
    "DataList",
    "DD",
    "Defs",
    "Del",
    "Desc",
    "Details",
    "DFN",
    "Dialog",
    "Discard",
    "Div",
    "DL",
    "DT",
    "Ellipse",
    "Em",
    "Embed",
    "FeBlend",
    "FeColorMatrix",
    "FeComponentTransfer",
    "FeComposite",
    "FeConvolveMatrix",
    "FeDiffuseLighting",
    "FeDisplacementMap",
    "FeDistantLight",
    "FeDropShadow",
    "FeFlood",
    "FeFuncA",
    "FeFuncB",
    "FeFuncG",
    "FeFuncR",
    "FeGaussianBlur",
    "FeImage",
    "FeMerge",
    "FeMergeNode",
    "FeMorphology",
    "FeOffset",
    "FePointLight",
    "FeSpecularLighting",
    "FeSpotLight",
    "FeTile",
    "FeTurbulence",
    "FieldSet",
    "FigCaption",
    "Figure",
    "Filter",
    "Footer",
    "ForeignObject",
    "Form",
    "G",
    "H1",
    "H2",
    "H3",
    "H4",
    "H5",
    "H6",
    "Hatch",
    "Hatchpath",
    "Head",
    "Header",
    "HR",
    "HTML",
    "I",
    "IFrame",
    "Image",
    "Img",
    "Input",
    "Ins",
    "Kbd",
    "Label",
    "Legend",
    "LI",
    "Line",
    "LinearGradient",
    "Link",
    "Main",
    "Map",
    "Mark",
    "Marker",
    "Mask",
    "Meta",
    "Metadata",
    "Meter",
    "Mpath",
    "Nav",
    "NoBr",
    "NoScript",
    "Object",
    "OL",
    "OptGroup",
    "Option",
    "Output",
    "P",
    "Param",
    "Path",
    "Pattern",
    "Picture",
    "Polygon",
    "Polyline",
    "Pre",
    "Progress",
    "Q",
    "RadialGradient",
    "Rect",
    "RP",
    "RT",
    "Ruby",
    "S",
    "Samp",
    "Script",
    "Section",
    "Select",
    "Set",
    "Small",
    "Solidcolor",
    "Source",
    "Span",
    "Stop",
    "Strong",
    "Style",
    "Sub",
    "Summary",
    "Sup",
    "SVG",
    "Switch",
    "Symbol",
    "Table",
    "TBody",
    "TD",
    "Template",
    "Text",
    "TextArea",
    "TextPath",
    "TFoot",
    "TH",
    "THead",
    "Time",
    "Title",
    "TR",
    "Track",
    "TSpan",
    "U",
    "UL",
    "Use",
    "Var",
    "View",
    "Video",
    "WBr",
]

# I have no idea why it performs best with worst hash functions. TODO: some research.
MAX_CACHE_SIZE = 12800

_ElementType = t.Union["_RawText", "_Text", "_Declaration", "_Tag"]  # type: ignore
_NaiveElementType = t.Union[str, bytes, _ElementType]  # type: ignore


@lru_cache(maxsize=MAX_CACHE_SIZE)
def double_quote(txt: str) -> str:
    """Double quote strings safely for attributes.
    
    Usage:
        >>> double_quote('abc"xyz')
        '"abc\\"xyz"'
    """
    return '"{}"'.format(txt.replace('"', '\\"'))


@lru_cache(maxsize=MAX_CACHE_SIZE)
def render_element(element: _ElementType) -> str:
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


def css(**code: t.Dict[str, t.Union[str, t.Collection[str]]]) -> str:
    """Helps rendering CSS code.
    
    Usage:
        >>> css(**{
        ...     "p": {"color": "red"},
        ...     ".center": {"text-align": "center"},
        ... })
	"p{color:'red';}.center{text-align:'center';}"
    """
    return "".join(f"{k}{{{style(**(code[k]))}}}" for k in code)


def style(**code: t.Union[str, t.Collection[str]]) -> str:
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
        self.value: str
        super().__setattr__("value", value)

    def __setattr__(self, name: str, value: object) -> None:
        raise AttributeError("can't set attribute")

    def __eq__(self, other: object) -> bool:
        return isinstance(other, type(self)) and self.value == other.value

    def __hash__(self) -> int:
        return hash("{type(self)}:{self.value}")

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
        self.value: str
        super().__setattr__("value", value)

    def __setattr__(self, name: str, value: object) -> None:
        raise AttributeError("can't set attribute")

    def __eq__(self, other: object) -> bool:
        return isinstance(other, type(self)) and self.value == other.value

    def __hash__(self) -> int:
        return hash("{type(self)}:{self.value}")

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
        self.value: str
        super().__setattr__("value", value)

    def __setattr__(self, name: str, value: object) -> None:
        raise AttributeError("can't set attribute")

    def __eq__(self, other: object) -> bool:
        return isinstance(other, type(self)) and self.value == other.value

    def __hash__(self) -> int:
        return hash("{type(self)}:{self.value}")

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
        self.attrs: t.Tuple[str]
        super().__setattr__("attrs", attrs)

    def __setattr__(self, name: str, value: object) -> None:
        raise AttributeError("can't set attribute")

    def __eq__(self, other: object) -> bool:
        return isinstance(other, type(self)) and self.attrs == other.attrs

    def __hash__(self) -> int:
        return hash("{type(self)}:{self.attrs}")

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
        self.attrs: t.Tuple[str]
        self.props: t.Mapping[str, str]
        super().__setattr__("attrs", attrs)
        super().__setattr__("props", MappingProxyType(props))

    def __setattr__(self, name: str, value: object) -> None:
        raise AttributeError("can't set attribute")

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, type(self))
            and self.attrs == other.attrs
            and self.props == other.props
        )

    def __hash__(self) -> int:
        return hash("{type(self)}:{self.attrs}:{self.props}")

    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def _repr(self) -> str:
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

    def __repr__(self) -> str:
        return self._repr()


class _LeafTag(_Tag):
    """Derive from this class to create tag that cannot have children.

    Example:
        >>> class MyTag(_LeafTag):
        ...     tagname = "mytag"
        ... 
        >>> MyTag("x", y="z")
        <mytag x y="z" />
    """

    pass


_SingleChildTagType = t.TypeVar("_SingleChildTagType", bound="_SingleChildTag")


class _SingleChildTag(_Tag):
    """Derive from this class to create tag that can have only one child.
    
    Example:
        >>> class MyTag(_SingleChildTag):
        ...     tagname = "mytag"
        ... 
        >>> MyTag("x", y="z")("foo")
        <mytag x y="z">foo</mytag>
    """

    __slots__ = ["attrs", "props", "child"]

    def __init__(self, *attrs: str, **props: str) -> None:
        self.child: _ElementType
        super().__init__(*attrs, **props)
        super().__class__.__setattr__(self, "child", _Text(""))

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, type(self))
            and self.attrs == other.attrs
            and self.props == other.props
            and self.child == other.child
        )

    def __hash__(self) -> int:
        return hash("{type(self)}:{self.attrs}:{self.props}:{self.child}")

    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def __call__(self, child: _NaiveElementType) -> _SingleChildTagType:
        _child: _NaiveElementType = child
        if isinstance(child, str):
            _child = _Text(child)
        elif isinstance(child, bytes):
            _child = _RawText(child.decode("utf-8"))
        tag = type(self)(*self.attrs, **self.props)
        super(type(tag), tag).__class__.__setattr__(tag, "child", _child)
        return tag

    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def _repr(self) -> str:
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

    def __repr__(self) -> str:
        return self._repr()


_CompositeTagType = t.TypeVar("_CompositeTagType", bound="_CompositeTag")


class _CompositeTag(_Tag):
    """Derive from this class to create tag that can have children.
    
    Example:
        >>> class MyTag(_SingleChildTag):
        ...     tagname = "mytag"
        ... 
        >>> MyTag("x", y="z")("foo ", MyTag()("bar"))
        <mytag x y="z">foo <mytag>bar</mytag></mytag>
    """

    __slots__ = ["attrs", "props", "children"]

    def __init__(self: _CompositeTagType, *attrs: str, **props: str) -> None:
        self.attrs: t.Tuple[str]
        self.props: t.Mapping[str, str]
        self.children: t.Tuple[_ElementType]
        super().__init__(*attrs, **props)
        super().__class__.__setattr__(self, "children", tuple())

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, type(self))
            and self.attrs == other.attrs
            and self.props == other.props
            and self.children == other.children
        )

    def __hash__(self) -> int:
        return hash("{type(self)}:{self.attrs}:{self.props}:{self.children}")

    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def __call__(self, *children: _NaiveElementType) -> _CompositeTagType:
        _children: t.List[_ElementType] = []
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

    def __repr__(self) -> str:
        return render_element(self)


@lru_cache(maxsize=MAX_CACHE_SIZE)
def _new_adhoc_composite_tag(tagname: str):
    """Use it to create any custom composite tag when you don't have any other option.

    A better way to create custom tag is to subclass base tags like `_CompositeTag`,
    `_LeafTag`, or `_SingleChildTag`.

    Example:
        >>> Clipboard_Copy = _new_adhoc_composite_tag("clipboard-copy")
        >>> Clipboard_Copy(value="foo")("Copy Me")
        <clipboard-copy value="foo">Copy Me</clipboard-copy>
    """

    return type(tagname, (_CompositeTag,), {"tagname": tagname})


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
class Animate(_CompositeTag):
    tagname = "animate"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class AnimateMotion(_CompositeTag):
    tagname = "animateMotion"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class AnimateTransform(_CompositeTag):
    tagname = "animateTransform"


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
class Center(_CompositeTag):
    tagname = "center"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Circle(_CompositeTag):
    tagname = "circle"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class CirclePath(_CompositeTag):
    tagname = "circlePath"


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
class Color_Profile(_CompositeTag):
    tagname = "color-profile"


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
class Defs(_CompositeTag):
    tagname = "defs"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Del(_CompositeTag):
    tagname = "del"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Desc(_CompositeTag):
    tagname = "desc"


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
class Discard(_CompositeTag):
    tagname = "discard"


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
class Ellipse(_CompositeTag):
    tagname = "ellipse"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Em(_CompositeTag):
    tagname = "em"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Embed(_CompositeTag):
    tagname = "embed"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeBlend(_CompositeTag):
    tagname = "feBlend"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeColorMatrix(_CompositeTag):
    tagname = "feColorMatrix"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeComponentTransfer(_CompositeTag):
    tagname = "feComponentTransfer"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeComposite(_CompositeTag):
    tagname = "feComposite"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeConvolveMatrix(_CompositeTag):
    tagname = "feConvolveMatrix"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeDiffuseLighting(_CompositeTag):
    tagname = "feDiffuseLighting"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeDisplacementMap(_CompositeTag):
    tagname = "feDisplacementMap"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeDistantLight(_CompositeTag):
    tagname = "feDistantLight"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeDropShadow(_CompositeTag):
    tagname = "feDropShadow"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeFlood(_CompositeTag):
    tagname = "feFlood"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeFuncA(_CompositeTag):
    tagname = "feFuncA"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeFuncB(_CompositeTag):
    tagname = "feFuncB"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeFuncG(_CompositeTag):
    tagname = "feFuncG"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeFuncR(_CompositeTag):
    tagname = "feFuncR"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeGaussianBlur(_CompositeTag):
    tagname = "feGaussianBlur"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeImage(_CompositeTag):
    tagname = "feImage"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeMerge(_CompositeTag):
    tagname = "feMerge"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeMergeNode(_CompositeTag):
    tagname = "feMergeNode"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeMorphology(_CompositeTag):
    tagname = "feMorphology"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeOffset(_CompositeTag):
    tagname = "feOffset"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FePointLight(_CompositeTag):
    tagname = "fePointLight"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeSpecularLighting(_CompositeTag):
    tagname = "feSpecularLighting"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeSpotLight(_CompositeTag):
    tagname = "feSpotLight"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeTile(_CompositeTag):
    tagname = "feTile"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FeTurbulence(_CompositeTag):
    tagname = "feTurbulence"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FieldSet(_CompositeTag):
    tagname = "fieldset"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class FigCaption(_CompositeTag):
    tagname = "figcaption"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Figure(_CompositeTag):
    tagname = "figure"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Filter(_CompositeTag):
    tagname = "filter"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Footer(_CompositeTag):
    tagname = "footer"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class ForeignObject(_LeafTag):
    tagname = "foreignObject"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Form(_CompositeTag):
    tagname = "form"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class G(_CompositeTag):
    tagname = "g"


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
class Hatch(_CompositeTag):
    tagname = "hatch"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Hatchpath(_CompositeTag):
    tagname = "hatchpath"


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
class Image(_CompositeTag):
    tagname = "image"


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
class Line(_CompositeTag):
    tagname = "line"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class LinearGradient(_CompositeTag):
    tagname = "linearGradient"


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
class Marker(_CompositeTag):
    tagname = "marker"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Mask(_CompositeTag):
    tagname = "mask"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Meta(_LeafTag):
    tagname = "meta"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Metadata(_CompositeTag):
    tagname = "metadata"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Meter(_LeafTag):
    tagname = "meter"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Mpath(_CompositeTag):
    tagname = "mpath"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Nav(_CompositeTag):
    tagname = "nav"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class NoBr(_CompositeTag):
    tagname = "nobr"


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


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Param(_LeafTag):
    tagname = "param"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Path(_CompositeTag):
    tagname = "path"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Pattern(_CompositeTag):
    tagname = "pattern"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Picture(_CompositeTag):
    tagname = "picture"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Polygon(_CompositeTag):
    tagname = "polygon"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Polyline(_CompositeTag):
    tagname = "polyline"


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
class RadialGradient(_CompositeTag):
    tagname = "radialGradient"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Rect(_CompositeTag):
    tagname = "rect"


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

    def __call__(self, child: str) -> _SingleChildTagType:
        s: Script = type(self)(*self.attrs, **self.props)
        super(type(s), s).__class__.__setattr__(s, "child", _RawText(child))
        return s


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Section(_CompositeTag):
    tagname = "section"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Select(_CompositeTag):
    tagname = "select"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Set(_CompositeTag):
    tagname = "set"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Small(_CompositeTag):
    tagname = "small"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Solidcolor(_CompositeTag):
    tagname = "solidcolor"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Source(_LeafTag):
    tagname = "source"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Span(_CompositeTag):
    tagname = "span"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Stop(_CompositeTag):
    tagname = "stop"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Strong(_CompositeTag):
    tagname = "strong"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Style(_SingleChildTag):
    tagname = "style"

    def __call__(self, child: str) -> _SingleChildTagType:
        s: Style = type(self)(*self.attrs, **self.props)
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
class Switch(_CompositeTag):
    tagname = "switch"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Symbol(_CompositeTag):
    tagname = "symbol"


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
class Text(_CompositeTag):
    tagname = "text"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class TextArea(_SingleChildTag):
    tagname = "textarea"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class TextPath(_CompositeTag):
    tagname = "textPath"


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
class TSpan(_CompositeTag):
    tagname = "tspan"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class U(_CompositeTag):
    tagname = "u"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class UL(_CompositeTag):
    tagname = "ul"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Use(_CompositeTag):
    tagname = "use"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Var(_CompositeTag):
    tagname = "var"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class View(_CompositeTag):
    tagname = "view"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class Video(_CompositeTag):
    tagname = "video"


@lru_cache(maxsize=MAX_CACHE_SIZE)
class WBr(_LeafTag):
    tagname = "wbr"
