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
            " components, it might surpass the performance of traditional template rendering engines.",
        ),
        e.p()(
            e.b()("WARNING: "),
            "It performs a ",
            e.code()('"{rendered_elements}".format(**returned_data)'),
            ". So each `{` or `}` in the compile-time code needs to be",
            " escaped with `{{` or `}}`.",
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
            " htmldoom uses pure functions with hashable input parameters as elements.",
            " Hence, it makes effective use of caching internally. It also offers friendly a",
            " mechanism to pre-render the static parts of the page using the `@renders` decorator",
            " when it compiles to bytecode. ",
            e.br(),
            "Also since it helps you (probably forces you) to refactor the webpage",
            " into multiple render functions, you are free to use whatever optimisation",
            " you prefer. Try putting an `@lru_cache` in a render function?",
        ),
        e.h3()("Is there any benchmark?"),
        e.p()(
            e.a(href="https://github.com/sayanarijit/htmldoom/blob/master/examples")(
                e.b()("Refer to the benchmarks here.")
            )
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
