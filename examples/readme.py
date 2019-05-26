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
    e.P()(
        e.H2()("Usage"),
        e.P()(
            e.Pre()(
                ">>> from htmldoom import elements as e\n"
                ">>> \n"
                """>>> e.P(style=e.css(color="red"))("This is a paragraph")\n"""
                """<p style="color: 'red';">This is a paragraph</p>"""
            )
        ),
        e.P()(
            e.Pre()(
                ">>> from htmldoom import elements as e\n"
                ">>> from htmldoom.layouts import BaseLayout\n"
                ">>> \n"
                ">>> class MyLayout(BaseLayout):\n"
                "...     @property\n"
                "...     def title(self) -> e.Title:\n"
                '...         return e.Title(self.data["title"])\n'
                "...     @property\n"
                "...     def body(self) -> e.Body:\n"
                """...         return e.Body(f"Welcome {self.data['user']['name']}")\n\n"""
                "... \n"
                """>>> MyLayout({"title": "foo", "user": {"name": "bar"}})\n"""
                "<!DOCTYPE html>\n"
                "<html><head><title>foo</title></head><body>Welcome bar</body></html>"
            )
        ),
        e.P()(
            e.A(href="https://github.com/sayanarijit/htmldoom/tree/master/examples")(
                "Find more examples here"
            )
        ),
    ),
    e.P()(
        e.H2()("Benchmarks"),
        e.P()(
            "Very basic benchmark done using ",
            e.A(
                href="https://github.com/sayanarijit/htmldoom/blob/master/benchmark/general.py"
            )("this script"),
            " and IPython",
        ),
        e.H3()("htmldoom"),
        e.Img(
            src="https://thepracticaldev.s3.amazonaws.com/i/dc0pruqhyvi1jk5zxyi9.png",
            alt="htmldoom stats",
        ),
        e.H3()("Jinja2"),
        e.Img(
            src="https://thepracticaldev.s3.amazonaws.com/i/hvvuvybfk5jved6trinr.png",
            alt="Jinja2 stats",
        ),
        e.H3()("Mako"),
        e.Img(
            src="https://thepracticaldev.s3.amazonaws.com/i/xyzdag8221qzoohz1tx9.png",
            alt="Mako stats",
        ),
        e.H3()("Chameleon"),
        e.Img(
            src="https://thepracticaldev.s3.amazonaws.com/i/0j49ln7pa62ivhqzkkuq.png",
            alt="Chameleon stats",
        ),
        e.H3()("Conclusion"),
        e.P()(
            "htmldoom performs best upto a certain number of recursions which is generally high enough."
            " These measurements are very naive and shows very basic information. Some templating engines might have"
            " performance optimizations (such caching) enabled by default. However, In case of htmldoom, it's"
            " upto to developer (for now) to optimize it."
        ),
    ),
)

print(doc)
