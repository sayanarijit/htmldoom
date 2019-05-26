from htmldoom import elements as e

doc = e.Div()(
    e.H1(align="center")("htmldoom"),
    e.P(align="center")("Write safer and cleaner HTML using Python"),
    e.P(align="center")(
        e.Span()(
            e.A(href="https://pypi.org/project/htmldoom")(
                e.Img(
                    src="https://img.shields.io/pypi/v/htmldoom.svg", alt="PyPI version"
                )
            )
        ),
        b"&nbsp;",
        e.Span()(
            e.A(href="https://travis-ci.org/sayanarijit/htmldoom")(
                e.Img(
                    src="https://travis-ci.org/sayanarijit/htmldoom.svg?branch=master",
                    alt="Build Status",
                )
            )
        ),
        b"&nbsp;",
        e.Span()(
            e.A(href="https://codecov.io/gh/sayanarijit/htmldoom")(
                e.Img(
                    src="https://codecov.io/gh/sayanarijit/htmldoom/branch/master/graph/badge.svg",
                    alt="codecov",
                )
            )
        ),
        b"&nbsp;",
        e.Span()(
            e.A(href="https://github.com/python/black")(
                e.Img(
                    src="https://img.shields.io/badge/code%20style-black-000000.svg",
                    alt="Code style: black",
                )
            )
        ),
    ),
)

print(doc)
