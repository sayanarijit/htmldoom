htmldoom
========
[![Documentation](https://api.netlify.com/api/v1/badges/8bedc4f4-508a-494d-8160-02f6a76d4b04/deploy-status)](https://app.netlify.com/sites/htmldoom/deploys)
[![PyPI version](https://img.shields.io/pypi/v/htmldoom.svg)](https://pypi.org/project/htmldoom)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/htmldoom.svg)](https://pypi.org/project/htmldoom)
[![Build Status](https://travis-ci.org/sayanarijit/htmldoom.svg?branch=master)](https://travis-ci.org/sayanarijit/htmldoom)
[![codecov](https://codecov.io/gh/sayanarijit/htmldoom/branch/master/graph/badge.svg)](https://codecov.io/gh/sayanarijit/htmldoom)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)


Introducing htmldoom
-----------------------
[htmldoom](https://github.com/sayanarijit/htmldoom) is an HTML rendering framework for Python that helps you define your
HTML documents, templates, layouts and contents in an organised way, gives you
the flexibility to use many different syntaxes, option to declare and debug
different components and pages separately and more... all without making you
worry about the runtime performance.


How does it work?
-----------------
Understanding the working principle will get pretty intuitive if we go one
feature at a time. Let's start with HTML escaping.


### HTML escaping
In the center of htmldoom's functionality is the HTML escaping logic. Texts to
be escaped are represented using `str`, while texts that should not be escaped
are represented using `bytes`. The `htmldoom.renders()` function receives the
texts as inputs, then for each input, it decides whether to escape it or not
based on if it is `str` or `bytes` and returns the rendered text in `str` format.

We can use `htmldoom.txt()` to convert some string into HTML escaped text, and
`htmldoom.raw()` to convert some string into HTML unescaped text. It should be
noted that both the functions will return text formatted in `bytes` which can be
passed to the `htmldoom.render()` to render it back to `str`.


### HTML elements
HTML elements or tags can be defined using the `htmldoom.composite_tag()` and
the `htmldoom.leaf_tag()` functions. Any tag that can have child elements (e.g.
`<p></p>`) are defined using `htmldoom.composite_tag()`.

For example:

	p = composite_tag("p")

Tags that cannot have child elements are defined using `htmldoom.leaf_tag()`.

For example:
	
	input_ = leaf_tag("input")

So when we call `p(class_="red")("foo", "bar")` or `input_(type_="button")`,
we get `bytes` encoded `<p class="red">foobar</p>` or
`<input type="button" />` respectively. The `htmldoom.render()` function will
render them back to `str`.


### HTML components / layouts
HTML components i.e. combination of several elements (tags and texts) can be
defined using the `@htmldoom.renders()` decorator like below.

	from htmldoom import renders, elements as e

	@renders(
	    e.p(class_="red")("{key1}", "{key2}"),
	    e._input(type_="button")
	)
	def my_component(value1, value2):
	    return {"key1": value1, "key2": value2}

Now we can render the component by calling it with the required arguments e.g.
	
	my_document(value1="&amp;", value2=b"&amp;")

This will return a `bytes` encoded text. The `value1` will be escaped to `&amp;amp;` since
it is `str`. `value2` is in `bytes`, hence it will remain the same and wil be
rendered in the browser as `&`.

Calling this will return `bytes` encoded text

	<p class="red">foobar</p><input type="button" />

which can be rendered into string using `htmldoom.render()`.

This mechanism renders the template text during module load time. Hence there should be
no performance drop in runtime.

> NOTE: It is important to note that every `{` and `}` should be escaped with `{{` and
`}}` when it is not being used as a placeholder for some variable.

It is also possible to define the components using `yaml` syntax like below.

	some:
	  demo:
	    p:
	    - class: red
	    - - "{key1}"
	      - "{key2}"
	    input:
	    - type: button

And then define the component renderer like below.

	from htmldoom import renders
	from htmldoom.yaml_loader import loadyaml

	@renders(loadyaml("path/to/component.yaml", ("some", "demo")))
	def my_component(value1, value2):
	    return {"key1": value1, "key2": value2}

We can also use escaped and raw loaders with the `htmldoom.loadtxt()` and `htmldoom.loadraw()`
functions respectively. We only need to pass the file path as shown in the `yaml` example.

We can use the same syntax to define reusable layouts.


### Separating values from templates
htmldoom provides us with a friendly way to separate values from layouts or components
templates. The `htmldoom.value_loader.loadvalues()` function scans the given directory and
returns a nested namedtuple with the file or directory names as element names and the loaded
contents as the values. We can pass this to components like below.

	from htmldoom import renders, elements as e
	from htmldoom.value_loader import loadvalues

	values = loadvalues("path/to/values")

	@renders(
	    e.p()("{v.title}"),
	    e.p()("{v.content.line1}")
	    e.p()("{v.content.line2}")
	    e.p()("{v.content.line3}")
	)
	def my_component():
	    return {"v": values}

So we need a directory structure like below.

	values
	├── title.txt
	└── content
	    ├── line1.txt
	    ├── line2.html
	    └── line3.yml

As you mught have guessed, this can load the values based of file types. You can use
your own renderer for file types such as `md` or `rst` by extending the
`htmldoom.value_loader.EXTENSION_RENDERERS` map and passing is to the
`htmldoom.value_loader.loadvalues()` function like below.

	from htmldoom import raw
	from htmldoom.value_loader import loadvalues, EXTENSION_RENDERERS

	def markdown_to_html(path):
	    """Some function that reads the file, converts the content to HTML,
	    and returns the converted data as string.
	    """
	    # The logic goes here...

	MY_EXTENSION_RENDERERS = dict(
	    md=lambda path: raw(markdown_to_html(path)),
	    **EXTENSION_RENDERERS
	)

	values = loadvalues("path/to/values", extension_renderers=MY_EXTENSION_RENDERERS)

In fact, this documentation is generated using the same method.
