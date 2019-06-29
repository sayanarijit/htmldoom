"""The README.md generator"""

from htmldoom import elements as e
from htmldoom import render


def badge(href: str, src: str, alt: str):
    return e.span()(e.a(href=href)(e.img(src=src, alt=alt)))


readme = (
    e.h1(align="center")("htmldoom"),
    e.p(align="center")("An intuitive, high performance HTML rendering framework"),
    e.p(align="center")(
        badge(
            href="https://pypi.org/project/htmldoom",
            src="https://img.shields.io/pypi/v/htmldoom.svg",
            alt="PyPI version",
        ),
        b"&nbsp;",
        badge(
            href="https://pypi.org/project/htmldoom",
            src="https://img.shields.io/pypi/pyversions/htmldoom.svg",
            alt="PyPI version",
        ),
        b"&nbsp;",
        badge(
            href="https://travis-ci.org/sayanarijit/htmldoom",
            src="https://travis-ci.org/sayanarijit/htmldoom.svg?branch=master",
            alt="Build Status",
        ),
        b"&nbsp;",
        badge(
            href="https://codecov.io/gh/sayanarijit/htmldoom",
            src="https://codecov.io/gh/sayanarijit/htmldoom/branch/master/graph/badge.svg",
            alt="codecov",
        ),
        b"&nbsp;",
        badge(
            href="https://github.com/python/black",
            src="https://img.shields.io/badge/code%20style-black-000000.svg",
            alt="Code style: black",
        ),
    ),
    e.h2()("Usage"),
    e.p()(
        e.h2()("A basic tag"),
        e.pre()(
            ">>> from htmldoom import render, elements as e\n"
            ">>> \n"
            """>>> print(render(e.p(style="color='red'")("This is a paragraph")))\n"""
            """<p style="color:'red';">This is a paragraph</p>"""
        ),
    ),
    e.p()(
        e.h2()("A functional style foreach loop with a switch case"),
        e.pre()(
            ">>> from htmldoom import elements as e\n"
            ">>> from htmldoom import functions as fn\n"
            ">>> \n"
            '>>> tuple(fn.foreach(["good", "bad", "evil"])(\n'
            "...     lambda x: fn.switch({\n"
            '...         x == "good": lambda: e.span(style="color: green")(f"this is {x}"),\n'
            '...         x == "bad": lambda: e.span(style="color: yellow")(f"this is {x}"),\n'
            '...         x == "evil": lambda: e.span(style="color: red")(f"this is {x}"),\n'
            "...         fn.Case.DEFAULT: lambda: fn.Error.throw(ValueError(x)),\n"
            "...     })\n"
            "... ))\n"
            """(b'<span style="color: green">this is good</span>',\n"""
            """ b'<span style="color: yellow">this is bad</span>',\n"""
            """ b'<span style="color: red">this is evil</span>')\n"""
        ),
    ),
    e.p()(
        e.a(href="https://github.com/sayanarijit/htmldoom/tree/master/examples")(
            e.b()("Find more examples here")
        )
    ),
    e.p()(
        e.h2()("Q/A"),
        e.h3()("What is the goal here?"),
        e.p()(
            "The primary goal is to make writing HTML pages cleaner, easier, safer and intuitive using Python."
        ),
        e.h3()("What about performance?"),
        e.p()(
            (
                "Although performance is not the primary goal here, it should not be a roadblock."
                " htmldoom is copying the syntax and some of the rendering properties of "
            ),
            e.a(href="https://elm-lang.org")("elm"),
            (
                ", an existing fast and purely functional programming language"
                " that specializes in rendering HTML in virtual doms."
                " Elm does all the optimisation internally, which I'm believe can be"
                " implemented in Python to a great extent."
            ),
            e.br(),
            "Furthermore, if we follow the ",
            e.a(
                href="https://developers.google.com/web/tools/lighthouse/audits/dom-size"
            )("the DOM size recommendations"),
            ", i.e.",
            e.ul()(
                e.li()("less than 1500 nodes total."),
                e.li()("maximum depth of 32 nodes."),
                e.li()("no parent node with more than 60 child nodes."),
            ),
            " htmldoom should perform really well.",
        ),
    ),
    e.p()(
        e.h2()("Plugins and ecosystem"),
        e.p()(
            e.ul()(
                e.li()(
                    e.a(href="https://github.com/sayanarijit/moodlmth")(
                        e.b()("moodlmth")
                    ),
                    e.span()(": Convert raw HTML pages into python source code"),
                )
            ),
            e.ul()(
                e.li()(
                    e.a(href="https://github.com/sayanarijit/pyramid_htmldoom")(
                        e.b()("pyramid_htmldoom")
                    ),
                    e.span()(": htmldoom rendering library plugin for Pyramid"),
                )
            ),
        ),
    ),
    e.p()(
        e.h2()("Contributing"),
        e.p()(
            "Check out the ",
            e.a(
                href="https://github.com/sayanarijit/htmldoom/tree/master/CONTRIBUTING.md"
            )(" contributing guidelines."),
        ),
    ),
)


if __name__ == "__main__":
    print(render(*readme))
