"""The base of htmldoom.

All the important objects here are also available in __init__.py so that
you can just do `from htmldoom import composite_tag`.
"""

from functools import lru_cache
from html import escape

from htmldoom.conf import CacheConfig
from htmldoom.util import fmt_prop
from htmldoom.util import render as _render

__all__ = ["doctype", "composite_tag", "leaf_tag", "txt", "raw", "comment"]


@lru_cache(maxsize=CacheConfig.MAXSIZE)
def txt(text):
    """Convert to HTML escaped element.

    Example:
        >>> txt("<p></p>")
        b'&lt;p&gt;&lt;/p&gt;'
    """
    return escape(text).encode()


@lru_cache(maxsize=CacheConfig.MAXSIZE)
def raw(text):
    """Convert to HTML unescaped element (use with caution).

    Example:
        >>> raw("<p></p>")
        b'<p></p>'
    """
    return text.encode()


@lru_cache(maxsize=CacheConfig.MAXSIZE)
def comment(text):
    return (f"<!-- {escape(text)} -->").encode()


@lru_cache(maxsize=CacheConfig.MAXSIZE)
def doctype(*attrs):
    return (f"<!DOCTYPE {' '.join(fmt_prop(x, None) for x in attrs)}>").encode()


def leaf_tag(tagname):
    """Use it to create tags that cannot have child elements.
    
    Example:
        >>> mytag = leaf_tag("mytag")
        >>> mytag(foo="bar")
        b'<mytag foo="bar" />'
    """

    @lru_cache(maxsize=CacheConfig.MAXSIZE)
    def set_props(*bool_props, **kv_props):

        if bool_props and (callable(bool_props[0]) or isinstance(bool_props[0], bytes)):
            raise ValueError(
                f"{tagname}(!WEIRD THINGS PASSED HERE!): here you pass tag attributes, not child elements."
                " By the way, this is a leaf tag i.e. Doesn't support child elements."
            )

        if not bool_props and not kv_props:
            return (f"<{tagname} />").encode()

        if not kv_props:
            return (
                f"<{tagname} {' '.join(fmt_prop(x, None) for x in bool_props)} />"
            ).encode()
        if not bool_props:
            return (
                f"<{tagname} {' '.join(fmt_prop(k, v) for k, v in kv_props.items())} />"
            ).encode()

        return (
            f"<{tagname} {' '.join(fmt_prop(x, None) for x in bool_props)}"
            f" {' '.join(fmt_prop(k, v) for k, v in kv_props.items())} />"
        ).encode()

    return set_props


def composite_tag(tagname):
    """Use it to create tags that can have one or multiple child tags.
    
    Example:
        >>> clipboard_copy = composite_tag("clipboard-copy")
        >>> clipboard_copy(value="foo")("Copy Me")
        b'<clipboard-copy value="foo">Copy Me</clipboard_copy>'
    """

    @lru_cache(maxsize=CacheConfig.MAXSIZE)
    def set_props(*bool_props, **kv_props):

        if bool_props and (callable(bool_props[0]) or isinstance(bool_props[0], bytes)):
            raise ValueError(
                f"{tagname}(!WEIRD THINGS PASSED HERE!): here you pass tag attributes, not child elements."
                f" Follow this syntax: {tagname}(*args, **kwargs)(element1, element2, ...)"
            )

        @lru_cache(maxsize=CacheConfig.MAXSIZE)
        def set_children(*children):

            if not bool_props and not kv_props:
                return (f"<{tagname}>{_render(*children)}</{tagname}>").encode()

            if not kv_props:
                return (
                    f"<{tagname} {' '.join(fmt_prop(x, None) for x in bool_props)}>"
                    f"{_render(*children)}</{tagname}>"
                ).encode()
            if not bool_props:
                return (
                    f"<{tagname} {' '.join(fmt_prop(k, v) for k, v in kv_props.items())}>"
                    f"{_render(*children)}</{tagname}>"
                ).encode()

            return (
                f"<{tagname} {' '.join(fmt_prop(x, None) for x in bool_props)}"
                f" {' '.join(fmt_prop(k, v) for k, v in kv_props.items())}>"
                f"{_render(*children)}</{tagname}>"
            ).encode()

        return set_children

    return set_props
