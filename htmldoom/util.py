"""Some utility functions."""

from functools import lru_cache
from html import escape
from re import sub

from htmldoom.conf import CacheConfig

__all__ = ["render", "renders", "double_quote", "fmt_prop", "loadtxt", "loadraw"]


@lru_cache(maxsize=CacheConfig.MAXSIZE)
def render(*elements):
    """Use it to render DOM elements.
    
    Example:
        >>> from htmldoom import render
        >>> from htmldoom.elements import p
        >>> 
        >>> print(render(p()("render me"), p()("me too")))
        <p>render me</p><p>me too</p>
    """
    if not elements:
        return ""

    if len(elements) == 1:
        el = elements[0]
        if callable(el):
            # Forgot to call with no arguments? no worries...
            el = el()
        if isinstance(el, str):
            return escape(el)
        if isinstance(el, bytes):
            return el.decode()
        raise ValueError(
            f"{el}: expected either of str, bytes, or a callable but got {type(el)}"
        )
    return "".join(map(render, elements))


@lru_cache(maxsize=CacheConfig.MAXSIZE)
def renders(*elements):
    """Decorator for rendering dynamic elements based on given template.
    
    It improves the performance a lot by pre-compiling the templates.
    Hence, it's highly recommended to use this decorator.

    Example (syntax 1):
        >>> @renders(
        ...     e.p()("{x}"),
        ...     e.p()("another {x}"),
        ... )
        ... def render_paras(data: dict):
        ...     return {"x": data["x"]}
        >>> 
        >>> render_paras({"x": "awesome paragraph"})
        <p>awesome paragraph</p><p>another awesome paragraph</p>
    
    Example (syntax 2):
        >>> render_paras = renders(
        ...     e.p()("{x}"),
        ...     e.p()("another {x}"),
        ... )(lambda data: {"x": data["x"]})
        >>> 
        >>> render_paras({"x": "awesome paragraph"})
        <p>awesome paragraph</p><p>another awesome paragraph</p>
    """
    template = render(*elements)

    def wrapped(func):
        def renderer(*args, **kwargs):
            return template.format(**func(*args, **kwargs))

        return renderer

    return wrapped


@lru_cache(maxsize=CacheConfig.MAXSIZE)
def double_quote(txt):
    """Double quote strings safely for attributes.
    
    Example:
        >>> double_quote('abc"xyz')
        '"abc\\"xyz"'
    """
    return '"{}"'.format(txt.replace('"', '\\"'))


@lru_cache(maxsize=CacheConfig.MAXSIZE)
def fmt_prop(key, val):
    """Format a key-value pair for an HTML tag."""
    key = key.rstrip("_").replace("_", "-")
    if val is None:
        if sub("[a-zA-Z_]", "", key):
            return double_quote(key)
        return key
    return f"{key}={double_quote(val)}"


def loadtxt(path, static=False):
    """Loads raw file data from given path with escaped HTML.

    Arguments:
        path (str): Path to the file to read.
        static (bool):
            If True, all the `{` and `}` will be replaced
            with `{{` and `}}` respectively.

    Example:
        >>> # $ cat path/to/file.html
        >>> # <p>{foo}</p>
        >>> 
        >>> loadtxt("path/to/file.html")
        >>> b'&lt;p&gt;{foo}&lt;/p&gt;'
        >>> 
        >>> loadtxt("path/to/file.html", static=True)
        >>> b'&lt;p&gt;{{foo}}&lt;/p&gt;'
    """
    with open(path) as f:
        data = f.read()
    if static:
        data = data.replace("{", "{{").replace("}", "}}")
    return escape(data).encode()


def loadraw(path, static=False):
    """Loads raw file data from given path with unescaped HTML.

    Arguments:
        path (str): Path to the file to read.
        static (bool):
            If True, all the `{` and `}` will be replaced
            with `{{` and `}}` respectively.

    Example:
        >>> # $ cat path/to/file.html
        >>> # <p>{foo}</p>
        >>> 
        >>> loadtxt("path/to/file.html")
        >>> b'<p>{foo}</p>'
        >>> 
        >>> loadtxt("path/to/file.html", static=True)
        >>> b'<p>{{foo}}</p>'
    """
    with open(path) as f:
        data = f.read()
    if static:
        data = data.replace("{", "{{").replace("}", "}}")
    return data.encode()
