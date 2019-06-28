from functools import lru_cache
from re import sub

from htmldoom.conf import MAX_CACHE_SIZE

__all__ = ["render", "double_quote", "fmt_prop"]


@lru_cache(maxsize=MAX_CACHE_SIZE)
def render(*doms: callable) -> str:
    if not doms:
        return ""
    if len(doms) == 1:
        return doms[0]()
    return "".join(map(render, doms))


@lru_cache(maxsize=MAX_CACHE_SIZE)
def double_quote(txt: str) -> str:
    """Double quote strings safely for attributes.
    
    Usage:
        >>> double_quote('abc"xyz')
        '"abc\\"xyz"'
    """
    return '"{}"'.format(txt.replace('"', '\\"'))


@lru_cache(maxsize=MAX_CACHE_SIZE)
def fmt_prop(key: str, val: str) -> str:
    """Format a key-value pair for an HTML tag."""
    if val is None:
        if sub("[a-zA-Z_]", "", key):
            return double_quote(key)
        return key
    return f"{key}={double_quote(val)}"
