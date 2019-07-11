"""All the elements that resides in an HTML DOM.

Example:
    >>> from htmldoom import render, elements as e
    >>> render(e.p(class_="comeclass")("This is a paragraph"))
    <p class="someclass">This is a paragraph</p>
"""

from htmldoom.base import composite_tag, leaf_tag

__all__ = [
    "a",
    "abbr",
    "address",
    "animate",
    "animateMotion",
    "animateTransform",
    "area",
    "article",
    "aside",
    "audio",
    "b",
    "base",
    "bdi",
    "bdo",
    "blockquote",
    "body",
    "br",
    "button",
    "canvas",
    "caption",
    "center",
    "circle",
    "circlePath",
    "cite",
    "code",
    "col",
    "colgroup",
    "color_profile",
    "data",
    "datalist",
    "dd",
    "defs",
    "del_",
    "desc",
    "details",
    "dfn",
    "dialog",
    "discard",
    "div",
    "dl",
    "dt",
    "ellipse",
    "em",
    "embed",
    "feBlend",
    "feColorMatrix",
    "feComponentTransfer",
    "feComposite",
    "feConvolveMatrix",
    "feDiffuseLighting",
    "feDisplacementMap",
    "feDistantLight",
    "feDropShadow",
    "feFlood",
    "feFuncA",
    "feFuncB",
    "feFuncG",
    "feFuncR",
    "feGaussianBlur",
    "feImage",
    "feMerge",
    "feMergeNode",
    "feMorphology",
    "feOffset",
    "fePointLight",
    "feSpecularLighting",
    "feSpotLight",
    "feTile",
    "feTurbulence",
    "fieldset",
    "figcaption",
    "figure",
    "filter_",
    "footer",
    "foreignObject",
    "form",
    "g",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "hatch",
    "hatchpath",
    "head",
    "header",
    "hr",
    "html",
    "i",
    "iframe",
    "image",
    "img",
    "input_",
    "ins",
    "kbd",
    "label",
    "legend",
    "li",
    "line",
    "linearGradient",
    "link",
    "main",
    "map_",
    "mark",
    "marker",
    "mask",
    "meta",
    "metadata",
    "meter",
    "mpath",
    "nav",
    "nobr",
    "noscript",
    "object_",
    "ol",
    "optgroup",
    "option",
    "output",
    "p",
    "param",
    "path",
    "pattern",
    "picture",
    "polygon",
    "polyline",
    "pre",
    "progress",
    "q",
    "radialGradient",
    "rect",
    "rp",
    "rt",
    "ruby",
    "s",
    "samp",
    "script",
    "section",
    "select",
    "set_",
    "small",
    "solidcolor",
    "source",
    "span",
    "stop",
    "strong",
    "style",
    "sub",
    "summary",
    "sup",
    "svg",
    "switch",
    "symbol",
    "table",
    "tbody",
    "td",
    "template",
    "text",
    "textarea",
    "textPath",
    "tfoot",
    "th",
    "thead",
    "time",
    "title",
    "tr",
    "track",
    "tspan",
    "u",
    "ul",
    "use",
    "var",
    "view",
    "video",
    "wbr",
]

a = composite_tag("a")

abbr = composite_tag("abbr")

address = composite_tag("address")

animate = composite_tag("animate")

animateMotion = composite_tag("animateMotion")

animateTransform = composite_tag("animateTransform")

area = leaf_tag("area")

article = composite_tag("article")

aside = composite_tag("aside")

audio = composite_tag("audio")

b = composite_tag("b")

base = leaf_tag("base")

bdi = composite_tag("bdi")

bdo = composite_tag("bdo")

blockquote = composite_tag("blockquote")

body = composite_tag("body")

br = leaf_tag("br")

button = composite_tag("button")

canvas = composite_tag("canvas")

caption = composite_tag("caption")

center = composite_tag("center")

circle = composite_tag("circle")

circlePath = composite_tag("circlePath")

cite = composite_tag("cite")

code = composite_tag("code")

col = leaf_tag("col")

colgroup = composite_tag("colgroup")

color_profile = composite_tag("profile")

data = composite_tag("data")

datalist = composite_tag("datalist")

dd = composite_tag("dd")

defs = composite_tag("defs")

del_ = composite_tag("del")

desc = composite_tag("desc")

details = composite_tag("details")

dfn = composite_tag("dfn")

dialog = composite_tag("dialog")

discard = composite_tag("discard")

div = composite_tag("div")

dl = composite_tag("dl")

dt = composite_tag("dt")

ellipse = composite_tag("ellipse")

em = composite_tag("em")

embed = composite_tag("embed")

feBlend = composite_tag("feBlend")

feColorMatrix = composite_tag("feColorMatrix")

feComponentTransfer = composite_tag("feComponentTransfer")

feComposite = composite_tag("feComposite")

feConvolveMatrix = composite_tag("feConvolveMatrix")

feDiffuseLighting = composite_tag("feDiffuseLighting")

feDisplacementMap = composite_tag("feDisplacementMap")

feDistantLight = composite_tag("feDistantLight")

feDropShadow = composite_tag("feDropShadow")

feFlood = composite_tag("feFlood")

feFuncA = composite_tag("feFuncA")

feFuncB = composite_tag("feFuncB")

feFuncG = composite_tag("feFuncG")

feFuncR = composite_tag("feFuncR")

feGaussianBlur = composite_tag("feGaussianBlur")

feImage = composite_tag("feImage")

feMerge = composite_tag("feMerge")

feMergeNode = composite_tag("feMergeNode")

feMorphology = composite_tag("feMorphology")

feOffset = composite_tag("feOffset")

fePointLight = composite_tag("fePointLight")

feSpecularLighting = composite_tag("feSpecularLighting")

feSpotLight = composite_tag("feSpotLight")

feTile = composite_tag("feTile")

feTurbulence = composite_tag("feTurbulence")

fieldset = composite_tag("fieldset")

figcaption = composite_tag("figcaption")

figure = composite_tag("figure")

filter_ = composite_tag("filter")

footer = composite_tag("footer")

foreignObject = leaf_tag("foreignObject")

form = composite_tag("form")

g = composite_tag("g")

h1 = composite_tag("h1")

h2 = composite_tag("h2")

h3 = composite_tag("h3")

h4 = composite_tag("h4")

h5 = composite_tag("h5")

h6 = composite_tag("h6")

hatch = composite_tag("hatch")

hatchpath = composite_tag("hatchpath")

head = composite_tag("head")

header = composite_tag("header")

hr = leaf_tag("hr")

html = composite_tag("html")

i = composite_tag("i")

iframe = composite_tag("iframe")

image = composite_tag("image")

img = leaf_tag("img")

input_ = leaf_tag("input")

ins = composite_tag("ins")

kbd = composite_tag("kbd")

label = composite_tag("label")

legend = composite_tag("legend")

li = composite_tag("li")

line = composite_tag("line")

linearGradient = composite_tag("linearGradient")

link = leaf_tag("link")

main = composite_tag("main")

map_ = composite_tag("map")

mark = composite_tag("mark")

marker = composite_tag("marker")

mask = composite_tag("mask")

meta = leaf_tag("meta")

metadata = composite_tag("metadata")

meter = leaf_tag("meter")

mpath = composite_tag("mpath")

nav = composite_tag("nav")

nobr = composite_tag("nobr")

noscript = composite_tag("noscript")

object_ = composite_tag("object")

ol = composite_tag("ol")

optgroup = composite_tag("optgroup")

option = composite_tag("option")

output = composite_tag("output")

p = composite_tag("p")

param = leaf_tag("param")

path = composite_tag("path")

pattern = composite_tag("pattern")

picture = composite_tag("picture")

polygon = composite_tag("polygon")

polyline = composite_tag("polyline")

pre = composite_tag("pre")

progress = composite_tag("progress")

q = composite_tag("q")

radialGradient = composite_tag("radialGradient")

rect = composite_tag("rect")

rp = composite_tag("rp")

rt = composite_tag("rt")

ruby = composite_tag("ruby")

s = composite_tag("s")

samp = composite_tag("samp")

script = composite_tag("script")

section = composite_tag("section")

select = composite_tag("select")

set_ = composite_tag("set")

small = composite_tag("small")

solidcolor = composite_tag("solidcolor")

source = leaf_tag("source")

span = composite_tag("span")

stop = composite_tag("stop")

strong = composite_tag("strong")

style = composite_tag("style")

sub = composite_tag("sub")

summary = composite_tag("summary")

sup = composite_tag("sup")

svg = composite_tag("svg")

switch = composite_tag("switch")

symbol = composite_tag("symbol")

table = composite_tag("table")

tbody = composite_tag("tbody")

td = composite_tag("td")

template = composite_tag("template")

text = composite_tag("text")

textarea = composite_tag("textarea")

textPath = composite_tag("textPath")

tfoot = composite_tag("tfoot")

th = composite_tag("th")

thead = composite_tag("thead")

time = composite_tag("time")

title = composite_tag("title")

tr = composite_tag("tr")

track = leaf_tag("track")

tspan = composite_tag("tspan")

u = composite_tag("u")

ul = composite_tag("ul")

use = composite_tag("use")

var = composite_tag("var")

view = composite_tag("view")

video = composite_tag("video")

wbr = leaf_tag("wbr")
