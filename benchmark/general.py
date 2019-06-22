from chameleon import PageTemplate
from jinja2 import Template
from mako.template import Template as MakoTemplate

from htmldoom import elements as e


def odd_paragraphs(n):
    paras = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            paras.append(e.P(style="color: blue")(f"{i} is even"))
        else:
            paras.append(e.P(style="color: red")(f"{i} is odd"))
    return paras


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
    e.HTML()(
        e.Head()(e.Title()("benchmark test")),
        e.Body()(
            e.Div()(
                e.Div()(f"Printing odd paragraphs with till {n}"),
                e.Div()(*odd_paragraphs(n)),
                e.Footer()("This is it then..."),
            )
        ),
    )


def jinja2(n):
    Template(j2tmpl).render(n=n)


def chameleon(n):
    PageTemplate(chameltmpl)(n=n)


def mako(n):
    MakoTemplate(makotmpl).render(n=n)
