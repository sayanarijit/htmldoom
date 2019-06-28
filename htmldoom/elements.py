"""All the elements that resides in an HTML DOM.

Example:
    >>> from htmldoom.elements import p
    >>> render(p(style="color: 'red'")("This is a paragraph"))
    <p style="color: 'red'">This is a paragraph</p>
"""

from functools import lru_cache

from htmldoom.base import composite_tag, leaf_tag
from htmldoom.conf import MAX_CACHE_SIZE


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def a(*attrs: str, **props: str) -> str:
    return "a"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def abbr(*attrs: str, **props: str) -> str:
    return "abbr"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def address(*attrs: str, **props: str) -> str:
    return "address"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def animate(*attrs: str, **props: str) -> str:
    return "animate"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def animateMotion(*attrs: str, **props: str) -> str:
    return "animateMotion"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def animateTransform(*attrs: str, **props: str) -> str:
    return "animateTransform"


@leaf_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def area(*attrs: str, **props: str) -> str:
    return "area"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def article(*attrs: str, **props: str) -> str:
    return "article"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def aside(*attrs: str, **props: str) -> str:
    return "aside"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def audio(*attrs: str, **props: str) -> str:
    return "audio"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def b(*attrs: str, **props: str) -> str:
    return "b"


@leaf_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def base(*attrs: str, **props: str) -> str:
    return "base"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def bdi(*attrs: str, **props: str) -> str:
    return "bdi"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def bdo(*attrs: str, **props: str) -> str:
    return "bdo"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def blockquote(*attrs: str, **props: str) -> str:
    return "blockquote"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def body(*attrs: str, **props: str) -> str:
    return "body"


@leaf_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def br(*attrs: str, **props: str) -> str:
    return "br"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def button(*attrs: str, **props: str) -> str:
    return "button"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def canvas(*attrs: str, **props: str) -> str:
    return "canvas"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def caption(*attrs: str, **props: str) -> str:
    return "caption"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def center(*attrs: str, **props: str) -> str:
    return "center"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def circle(*attrs: str, **props: str) -> str:
    return "circle"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def circlePath(*attrs: str, **props: str) -> str:
    return "circlePath"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def cite(*attrs: str, **props: str) -> str:
    return "cite"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def code(*attrs: str, **props: str) -> str:
    return "code"


@leaf_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def col(*attrs: str, **props: str) -> str:
    return "col"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def colgroup(*attrs: str, **props: str) -> str:
    return "colgroup"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def color_profile(*attrs: str, **props: str) -> str:
    return "color-profile"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def data(*attrs: str, **props: str) -> str:
    return "data"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def datalist(*attrs: str, **props: str) -> str:
    return "datalist"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def dd(*attrs: str, **props: str) -> str:
    return "dd"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def defs(*attrs: str, **props: str) -> str:
    return "defs"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def del_(*attrs: str, **props: str) -> str:
    return "del"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def desc(*attrs: str, **props: str) -> str:
    return "desc"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def details(*attrs: str, **props: str) -> str:
    return "details"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def dfn(*attrs: str, **props: str) -> str:
    return "dfn"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def dialog(*attrs: str, **props: str) -> str:
    return "dialog"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def discard(*attrs: str, **props: str) -> str:
    return "discard"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def div(*attrs: str, **props: str) -> str:
    return "div"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def dl(*attrs: str, **props: str) -> str:
    return "dl"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def dt(*attrs: str, **props: str) -> str:
    return "dt"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def ellipse(*attrs: str, **props: str) -> str:
    return "ellipse"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def em(*attrs: str, **props: str) -> str:
    return "em"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def embed(*attrs: str, **props: str) -> str:
    return "embed"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feBlend(*attrs: str, **props: str) -> str:
    return "feBlend"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feColorMatrix(*attrs: str, **props: str) -> str:
    return "feColorMatrix"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feComponentTransfer(*attrs: str, **props: str) -> str:
    return "feComponentTransfer"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feComposite(*attrs: str, **props: str) -> str:
    return "feComposite"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feConvolveMatrix(*attrs: str, **props: str) -> str:
    return "feConvolveMatrix"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feDiffuseLighting(*attrs: str, **props: str) -> str:
    return "feDiffuseLighting"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feDisplacementMap(*attrs: str, **props: str) -> str:
    return "feDisplacementMap"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feDistantLight(*attrs: str, **props: str) -> str:
    return "feDistantLight"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feDropShadow(*attrs: str, **props: str) -> str:
    return "feDropShadow"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feFlood(*attrs: str, **props: str) -> str:
    return "feFlood"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feFuncA(*attrs: str, **props: str) -> str:
    return "feFuncA"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feFuncB(*attrs: str, **props: str) -> str:
    return "feFuncB"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feFuncG(*attrs: str, **props: str) -> str:
    return "feFuncG"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feFuncR(*attrs: str, **props: str) -> str:
    return "feFuncR"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feGaussianBlur(*attrs: str, **props: str) -> str:
    return "feGaussianBlur"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feImage(*attrs: str, **props: str) -> str:
    return "feImage"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feMerge(*attrs: str, **props: str) -> str:
    return "feMerge"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feMergeNode(*attrs: str, **props: str) -> str:
    return "feMergeNode"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feMorphology(*attrs: str, **props: str) -> str:
    return "feMorphology"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feOffset(*attrs: str, **props: str) -> str:
    return "feOffset"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def fePointLight(*attrs: str, **props: str) -> str:
    return "fePointLight"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feSpecularLighting(*attrs: str, **props: str) -> str:
    return "feSpecularLighting"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feSpotLight(*attrs: str, **props: str) -> str:
    return "feSpotLight"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feTile(*attrs: str, **props: str) -> str:
    return "feTile"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def feTurbulence(*attrs: str, **props: str) -> str:
    return "feTurbulence"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def fieldset(*attrs: str, **props: str) -> str:
    return "fieldset"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def figcaption(*attrs: str, **props: str) -> str:
    return "figcaption"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def figure(*attrs: str, **props: str) -> str:
    return "figure"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def filter(*attrs: str, **props: str) -> str:
    return "filter"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def footer(*attrs: str, **props: str) -> str:
    return "footer"


@leaf_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def foreignObject(*attrs: str, **props: str) -> str:
    return "foreignObject"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def form(*attrs: str, **props: str) -> str:
    return "form"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def g(*attrs: str, **props: str) -> str:
    return "g"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def h1(*attrs: str, **props: str) -> str:
    return "h1"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def h2(*attrs: str, **props: str) -> str:
    return "h2"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def h3(*attrs: str, **props: str) -> str:
    return "h3"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def h4(*attrs: str, **props: str) -> str:
    return "h4"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def h5(*attrs: str, **props: str) -> str:
    return "h5"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def h6(*attrs: str, **props: str) -> str:
    return "h6"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def hatch(*attrs: str, **props: str) -> str:
    return "hatch"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def hatchpath(*attrs: str, **props: str) -> str:
    return "hatchpath"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def head(*attrs: str, **props: str) -> str:
    return "head"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def header(*attrs: str, **props: str) -> str:
    return "header"


@leaf_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def hr(*attrs: str, **props: str) -> str:
    return "hr"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def html(*attrs: str, **props: str) -> str:
    return "html"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def i(*attrs: str, **props: str) -> str:
    return "i"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def iframe(*attrs: str, **props: str) -> str:
    return "iframe"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def image(*attrs: str, **props: str) -> str:
    return "image"


@leaf_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def img(*attrs: str, **props: str) -> str:
    return "img"


@leaf_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def input(*attrs: str, **props: str) -> str:
    return "input"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def ins(*attrs: str, **props: str) -> str:
    return "ins"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def kbd(*attrs: str, **props: str) -> str:
    return "kbd"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def label(*attrs: str, **props: str) -> str:
    return "label"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def legend(*attrs: str, **props: str) -> str:
    return "legend"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def li(*attrs: str, **props: str) -> str:
    return "li"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def line(*attrs: str, **props: str) -> str:
    return "line"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def linearGradient(*attrs: str, **props: str) -> str:
    return "linearGradient"


@leaf_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def link(*attrs: str, **props: str) -> str:
    return "link"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def main(*attrs: str, **props: str) -> str:
    return "main"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def map(*attrs: str, **props: str) -> str:
    return "map"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def mark(*attrs: str, **props: str) -> str:
    return "mark"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def marker(*attrs: str, **props: str) -> str:
    return "marker"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def mask(*attrs: str, **props: str) -> str:
    return "mask"


@leaf_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def meta(*attrs: str, **props: str) -> str:
    return "meta"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def metadata(*attrs: str, **props: str) -> str:
    return "metadata"


@leaf_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def meter(*attrs: str, **props: str) -> str:
    return "meter"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def mpath(*attrs: str, **props: str) -> str:
    return "mpath"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def nav(*attrs: str, **props: str) -> str:
    return "nav"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def nobr(*attrs: str, **props: str) -> str:
    return "nobr"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def noscript(*attrs: str, **props: str) -> str:
    return "noscript"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def object(*attrs: str, **props: str) -> str:
    return "object"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def ol(*attrs: str, **props: str) -> str:
    return "ol"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def optgroup(*attrs: str, **props: str) -> str:
    return "optgroup"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def option(*attrs: str, **props: str) -> str:
    return "option"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def output(*attrs: str, **props: str) -> str:
    return "output"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def p(*attrs: str, **props: str) -> str:
    return "p"


@leaf_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def param(*attrs: str, **props: str) -> str:
    return "param"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def path(*attrs: str, **props: str) -> str:
    return "path"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def pattern(*attrs: str, **props: str) -> str:
    return "pattern"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def picture(*attrs: str, **props: str) -> str:
    return "picture"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def polygon(*attrs: str, **props: str) -> str:
    return "polygon"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def polyline(*attrs: str, **props: str) -> str:
    return "polyline"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def pre(*attrs: str, **props: str) -> str:
    return "pre"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def progress(*attrs: str, **props: str) -> str:
    return "progress"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def q(*attrs: str, **props: str) -> str:
    return "q"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def radialGradient(*attrs: str, **props: str) -> str:
    return "radialGradient"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def rect(*attrs: str, **props: str) -> str:
    return "rect"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def rp(*attrs: str, **props: str) -> str:
    return "rp"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def rt(*attrs: str, **props: str) -> str:
    return "rt"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def ruby(*attrs: str, **props: str) -> str:
    return "ruby"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def s(*attrs: str, **props: str) -> str:
    return "s"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def samp(*attrs: str, **props: str) -> str:
    return "samp"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def script(*attrs: str, **props: str) -> str:
    return "script"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def section(*attrs: str, **props: str) -> str:
    return "section"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def select(*attrs: str, **props: str) -> str:
    return "select"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def set(*attrs: str, **props: str) -> str:
    return "set"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def small(*attrs: str, **props: str) -> str:
    return "small"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def solidcolor(*attrs: str, **props: str) -> str:
    return "solidcolor"


@leaf_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def source(*attrs: str, **props: str) -> str:
    return "source"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def span(*attrs: str, **props: str) -> str:
    return "span"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def stop(*attrs: str, **props: str) -> str:
    return "stop"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def strong(*attrs: str, **props: str) -> str:
    return "strong"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def style(*attrs: str, **props: str) -> str:
    return "style"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def sub(*attrs: str, **props: str) -> str:
    return "sub"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def summary(*attrs: str, **props: str) -> str:
    return "summary"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def sup(*attrs: str, **props: str) -> str:
    return "sup"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def svg(*attrs: str, **props: str) -> str:
    return "svg"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def switch(*attrs: str, **props: str) -> str:
    return "switch"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def symbol(*attrs: str, **props: str) -> str:
    return "symbol"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def table(*attrs: str, **props: str) -> str:
    return "table"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def tbody(*attrs: str, **props: str) -> str:
    return "tbody"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def td(*attrs: str, **props: str) -> str:
    return "td"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def template(*attrs: str, **props: str) -> str:
    return "template"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def text(*attrs: str, **props: str) -> str:
    return "text"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def textarea(*attrs: str, **props: str) -> str:
    return "textarea"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def textPath(*attrs: str, **props: str) -> str:
    return "textPath"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def tfoot(*attrs: str, **props: str) -> str:
    return "tfoot"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def th(*attrs: str, **props: str) -> str:
    return "th"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def thead(*attrs: str, **props: str) -> str:
    return "thead"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def time(*attrs: str, **props: str) -> str:
    return "time"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def title(*attrs: str, **props: str) -> str:
    return "title"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def tr(*attrs: str, **props: str) -> str:
    return "tr"


@leaf_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def track(*attrs: str, **props: str) -> str:
    return "track"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def tspan(*attrs: str, **props: str) -> str:
    return "tspan"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def u(*attrs: str, **props: str) -> str:
    return "u"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def ul(*attrs: str, **props: str) -> str:
    return "ul"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def use(*attrs: str, **props: str) -> str:
    return "use"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def var(*attrs: str, **props: str) -> str:
    return "var"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def view(*attrs: str, **props: str) -> str:
    return "view"


@composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def video(*attrs: str, **props: str) -> str:
    return "video"


@leaf_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def wbr(*attrs: str, **props: str) -> str:
    return "wbr"
