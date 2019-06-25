from htmldoom import elements as e
from htmldoom.layouts import Component


class ReadMe(Component):
    """The README.md generator"""

    @property
    def header(self) -> e.H1:
        return e.H1(align="center")("htmldoom")

    @property
    def description(self) -> e.P:
        return e.P(align="center")("Write safer and cleaner HTML using Python")

    def badge(self, href: str, src: str, alt: str) -> e.Span:
        return e.Span()(e.A(href=href)(e.Img(src=src, alt=alt)))

    @property
    def badges(self) -> e.P:
        return e.P(align="center")(
            self.badge(
                href="https://pypi.org/project/htmldoom",
                src="https://img.shields.io/pypi/v/htmldoom.svg",
                alt="PyPI version",
            ),
            b"&nbsp;",
            self.badge(
                href="https://pypi.org/project/htmldoom",
                src="https://img.shields.io/pypi/pyversions/htmldoom.svg",
                alt="PyPI version",
            ),
            b"&nbsp;",
            self.badge(
                href="https://travis-ci.org/sayanarijit/htmldoom",
                src="https://travis-ci.org/sayanarijit/htmldoom.svg?branch=master",
                alt="Build Status",
            ),
            b"&nbsp;",
            self.badge(
                href="https://codecov.io/gh/sayanarijit/htmldoom",
                src="https://codecov.io/gh/sayanarijit/htmldoom/branch/master/graph/badge.svg",
                alt="codecov",
            ),
            b"&nbsp;",
            self.badge(
                href="https://github.com/python/black",
                src="https://img.shields.io/badge/code%20style-black-000000.svg",
                alt="Code style: black",
            ),
        )

    @property
    def example1(self) -> e.P:
        return e.P()(
            e.Pre()(
                ">>> from htmldoom import elements as e\n"
                ">>> \n"
                """>>> e.P(style=e.style(color="red"))("This is a paragraph")\n"""
                """<p style="color:'red';">This is a paragraph</p>"""
            )
        )

    @property
    def example2(self) -> e.P:
        return e.P()(
            e.Pre()(
                ">>> from htmldoom import elements as e\n"
                ">>> from htmldoom.layouts import BaseLayout\n"
                ">>> \n"
                ">>> class MyLayout(BaseLayout):\n"
                "...     @property\n"
                "...     def title(self) -> e.Title:\n"
                '...         return e.Title()(self["title"])\n'
                "...     @property\n"
                "...     def body(self) -> e.Body:\n"
                """...         return e.Body()(f"Welcome {self['user']['name']}")\n\n"""
                "... \n"
                """>>> MyLayout({"title": "foo", "user": {"name": "bar"}})\n"""
                "<!DOCTYPE html>\n"
                "<html><head><title>foo</title></head><body>Welcome bar</body></html>"
            )
        )

    @property
    def more_examples(self) -> e.P:
        return e.P()(
            e.A(href="https://github.com/sayanarijit/htmldoom/tree/master/examples")(
                e.B()("Find more examples here")
            )
        )

    @property
    def usage(self) -> e.P:
        return e.P()(e.H2()("Usage"), self.example1, self.example2, self.more_examples)

    @property
    def q_n_a(self) -> e.P:
        return e.P()(
            e.H2()("Q/A"),
            e.H3()("What is the goal here?"),
            e.P()(
                "The primary goal is to make writing HTML cleaner, easier, safer and intuitive using Python."
            ),
            e.H3()("What about performance?"),
            e.P()(
                (
                    "Although performance is not the primary goal here, it should not be a roadblock."
                    " htmldoom is copying the syntax and properties of "
                ),
                e.A(href="https://elm-lang.org")("elm"),
                (
                    ", an existing fast and purely functional programming language"
                    " that specializes in rendering HTML in virtual doms."
                    " Elm does all the optimisation internally which I'm sure can be"
                    " implemented in Python to a great extent."
                ),
                e.Br(),
                (
                    "All the elements and attributes in htmldoom is supposed to be immutable"
                    " (unless you want to hack it for some reason). Being immutable enables them"
                    " to be cachable and sharable making use of the "
                ),
                e.A(href="https://en.wikipedia.org/wiki/Flyweight_pattern")(
                    "flyweight pattern"
                ),
                ", thus improving the speed of rendering.",
                e.Br(),
                "Furthermore, if we follow the ",
                e.A(
                    href="https://developers.google.com/web/tools/lighthouse/audits/dom-size"
                )("the DOM size recommendations"),
                ", i.e.",
                e.UL()(
                    e.LI()("less than 1500 nodes total."),
                    e.LI()("maximum depth of 32 nodes."),
                    e.LI()("no parent node with more than 60 child nodes."),
                ),
                " htmldoom performs really well (refer to the ",
                e.A(href="#benchmarks")("benchmarks"),
                ").",
            ),
        )

    @property
    def plugins_n_ecosystem(self) -> e.P:
        return e.P()(
            e.H2()("Plugins and ecosystem"),
            e.P()(
                e.UL()(
                    e.LI()(
                        e.A(href="https://github.com/sayanarijit/moodlmth")(
                            e.B()("moodlmth")
                        ),
                        e.Span()(": Convert raw HTML pages into python source code"),
                    )
                ),
                e.UL()(
                    e.LI()(
                        e.A(href="https://github.com/sayanarijit/pyramid_htmldoom")(
                            e.B()("pyramid_htmldoom")
                        ),
                        e.Span()(": htmldoom rendering library plugin for Pyramid"),
                    )
                ),
            ),
        )

    def benchmark(self, title: str, src: str, alt: str) -> e.P:
        return e.P()(e.H3()(title), e.Img(src=src, alt=alt))

    @property
    def benchmarks(self) -> e.P:
        return e.P()(
            e.H2()("Benchmarks"),
            e.P()(
                "Very basic benchmark done using ",
                e.A(
                    href="https://github.com/sayanarijit/htmldoom/blob/master/benchmark/general.py"
                )("this script"),
                " and IPython",
            ),
            self.benchmark(
                title="htmldoom",
                src="https://thepracticaldev.s3.amazonaws.com/i/6dmd4r7lgoqu9wrv4wr9.png",
                alt="htmldoom stats",
            ),
            self.benchmark(
                title="Jinja2",
                src="https://thepracticaldev.s3.amazonaws.com/i/hvvuvybfk5jved6trinr.png",
                alt="Jinja2 stats",
            ),
            self.benchmark(
                title="Mako",
                src="https://thepracticaldev.s3.amazonaws.com/i/xyzdag8221qzoohz1tx9.png",
                alt="Mako stats",
            ),
            self.benchmark(
                title="Chameleon",
                src="https://thepracticaldev.s3.amazonaws.com/i/0j49ln7pa62ivhqzkkuq.png",
                alt="Chameleon stats",
            ),
            e.H3()("Conclusion"),
            e.P()(
                "htmldoom performs best upto a certain number of loops which is generally high enough.",
                e.Br(),
                "NOTE: These measurements are very naive and shows very basic information.",
            ),
        )

    @property
    def contributing(self) -> e.P:
        return e.P()(
            e.H2()("Contributing"),
            e.P()(
                "Check out the ",
                e.A(
                    href="https://github.com/sayanarijit/htmldoom/tree/master/CONTRIBUTING.md"
                )(" contributing guidelines."),
            ),
        )

    def render(self) -> e.Div:
        return e.Div()(
            self.header,
            self.description,
            self.badges,
            self.usage,
            self.q_n_a,
            self.plugins_n_ecosystem,
            self.benchmarks,
            self.contributing,
        )


if __name__ == "__main__":
    readme = ReadMe()
    print(readme)
