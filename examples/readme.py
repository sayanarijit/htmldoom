from htmldoom import elements as e

doc = e.Body()(
    e.Section()(
        e.H1()("htmldoom"),
        e.P()("Write safer and cleaner HTML using Python"),
        e.P()(
            e.Span()(
                e.A(href="https://pypi.org/project/htmldoom")(
                    e.Img(
                        src="https://img.shields.io/pypi/v/htmldoom.svg",
                        alt="PyPI version",
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
        ),
    )
)

print(doc)
