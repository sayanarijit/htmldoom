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
            ">>> print(render(\n"
            '...     e.textarea("required", class_="input")("text")\n'
            "... ))\n"
            '<textarea required class="input">text</textarea>'
        ),
    ),
    e.p()(
        e.h2()("A fast dynamic elements rendering mechanism"),
        e.p()("Choose whichever syntax suits you:"),
        e.h3()("Syntax 1"),
        e.pre()(
            ">>> from htmldoom import renders, elements as e\n"
            ">>> \n"
            ">>> @renders(\n"
            '...     e.p()("{x}"),\n'
            '...     e.p()("another {x}"),\n'
            "... )\n"
            "... def render_paras(data: dict) -> dict:\n"
            '...     return {"x": data["x"]}\n'
            ">>> \n"
            '>>> render_paras({"x": "awesome paragraph"})\n'
            "<p>awesome paragraph</p><p>another awesome paragraph</p>\n"
        ),
        e.h3()("Syntax 2"),
        e.pre()(
            ">>> from htmldoom import renders, elements as e\n"
            ">>> \n"
            ">>> render_paras = renders(\n"
            '...     e.p()("{x}"),\n'
            '...     e.p()("another {x}"),\n'
            '... )(lambda data: {"x": data["x"]})\n'
            ">>> \n"
            '>>> render_paras({"x": "awesome paragraph"})\n'
            "<p>awesome paragraph</p><p>another awesome paragraph</p>\n"
        ),
        e.p()(
            e.b()("NOTE: "),
            "This mechanism compiles the template when the file loads and reuse it.",
            e.br(),
            e.pre()(b"renders( -- compile-time code -- )( -- runtime code -- )"),
            e.br(),
            "The more execution you move from runtime to compile-time, the faster it gets.",
            e.br(),
            "If you properly use this mechanism and refractor your dynamic pages into smaller"
            " components, it will surpass the performance of traditional template rendering engines.",
        ),
        e.p()(
            e.b()("WARNING: "),
            "It performs a ",
            e.code()('"{rendered_elements}".format(**returned_data)'),
            ". So be careful about where you put which code.",
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
            "The primary goal is to make writing dynamic HTML pages "
            "cleaner, easier, safer and intuitive in Python."
        ),
        e.h3()("What about performance?"),
        e.p()(
            "Although performance is not the primary goal here, it should not be a roadblock.",
            " htmldoom is copying the syntax and some of the rendering properties of ",
            e.a(href="https://elm-lang.org")("elm"),
            ", an existing fast and purely functional programming language",
            " that specializes in rendering HTML in virtual doms.",
            " Elm does all the optimisation internally, which I believe can be",
            " implemented in Python to a great extent.",
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
            e.br(),
            " htmldoom should perform really well.",
            e.br(),
            "Also since it's all Python, the power is in your hands to make"
            " all the optimisations possible at the lowest level.",
        ),
        e.h3()("Still worried about performance. Is there any benchmark?"),
        e.p()(
            "Basic benchmarks are done and it shows that htmldoom performs better than traditional",
            " rendering engines without explicitly making any optimisation.",
            e.br(),
            e.a(href="https://github.com/sayanarijit/htmldoom/blob/master/examples")(
                e.b()("Refer to the benchmarks here.")
            ),
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
