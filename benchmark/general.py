import sys

from chameleon import PageTemplate
from jinja2 import Template
from mako.template import Template as MakoTemplate

from htmldoom import render
from htmldoom.elements import body, div, footer, head, html, p, title
from htmldoom.functions import Case, Error, switch

j2tmpl = """\
<html>
    <head><title>benchmark test</title></head>
    <body>
        <div>Printing odd paragraphs with till {{n}}</div>
        <div>
            {% for i in range(1, n+1) %}
                {% if i % 2 == 0 %}
                    <p style="color: blue">{{i}} is even</p>
                {% else %}
                    <p style="color: red">{{i}} is odd</p>
                {% endif %}
            {% endfor %}
        </div>
        <div>This is it then...</div>
    </body>
</html>
"""

chameltmpl = """\
<html>
    <head><title>benchmark test</title></head>
    <body>
        <div>Printing odd paragraphs with till ${n}</div>
        <div>
            <div tal:repeat="i range(n)">
                <p tal:condition="i % 2 == 0" style="color: blue">${i} is even</p>
                <p tal:condition="i % 2 == 1" style="color: red">${i} is odd</p>
            </div>
        </div>
        <div>This is it then...</div>
    </body>
</html>
"""

makotmpl = """\
<html>
    <head><title>benchmark test</title></head>
    <body>
        <div>Printing odd paragraphs with till ${n}</div>
        <div>
        % for i in range(1, n+1):
            % if i % 2 == 0:
                <p style="color: blue">${i} is even</p>
            % else:
                <p style="color: red">${i} is odd</p>
            % endif
        % endfor
        </div>
        <div>This is it then...</div>
    </body>
</html>
"""


def htmldoom(n):
    def even_or_odd(i):
        if i % 2 == 0:
            return p(style="color: blue")(f"{i} is even")
        return p(style="color: red")(f"{i} is odd")

    return render(
        html()(
            head()(title()("benchmark test")),
            title()(
                div()(
                    div()(f"Printing odd paragraphs with till {n}"),
                    *map(even_or_odd, range(n)),
                    footer()("This is it then..."),
                )
            ),
        )
    )


def jinja2(n):
    return Template(j2tmpl).render(n=n)


def chameleon(n):
    return PageTemplate(chameltmpl)(n=n)


def mako(n):
    return MakoTemplate(makotmpl).render(n=n)


if __name__ == "__main__":
    engine, count = sys.argv[1:]
    count = int(count)
    (
        lambda x: switch(
            {
                x == "htmldoom": lambda: htmldoom(count),
                x == "mako": lambda: mako(count),
                x == "jinja2": lambda: jinja2(count),
                x == "chameleon": lambda: chameleon(count),
                Case.DEFAULT: lambda: Error.throw(ValueError(x)),
            }
        )
    )(engine)
