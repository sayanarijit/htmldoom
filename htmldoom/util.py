from functools import lru_cache
from html import escape
from re import sub

from htmldoom.conf import CacheConfig

__all__ = ["render", "double_quote", "fmt_prop"]


@lru_cache(maxsize=CacheConfig.MAXSIZE)
def render(*doms: object) -> str:
    """Use it to render DOM elements.
    
    Example:
        >>> from htmldoom import render
        >>> from htmldoom.elements import p
        >>> 
        >>> print(render(p()("render me"), p()("me too")))
        <p>render me</p><p>me too</p>
    """
    if not doms:
        return ""

    if len(doms) == 1:
        dom = doms[0]
        if callable(dom):
            # Forgot to call with no arguments? no worries...
            dom = dom()
        if isinstance(dom, str):
            return escape(dom)
        if isinstance(dom, bytes):
            return dom.decode()
        raise ValueError(
            f"{dom}: expected either of str, bytes, or a callable but got {type(dom)}"
        )
    return "".join(map(render, doms))


@lru_cache(maxsize=CacheConfig.MAXSIZE)
def double_quote(txt: str) -> str:
    """Double quote strings safely for attributes.
    
    Usage:
        >>> double_quote('abc"xyz')
        '"abc\\"xyz"'
    """
    return '"{}"'.format(txt.replace('"', '\\"'))


@lru_cache(maxsize=CacheConfig.MAXSIZE)
def fmt_prop(key: str, val: str) -> str:
    """Format a key-value pair for an HTML tag."""
    key = key.rstrip("_").replace("_", "-")
    if val is None:
        if sub("[a-zA-Z_]", "", key):
            return double_quote(key)
        return key
    return f"{key}={double_quote(val)}"
