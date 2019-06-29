"""The base"""

from functools import lru_cache
from html import escape

from htmldoom.conf import CacheConfig
from htmldoom.util import fmt_prop
from htmldoom.util import render as _render

__all__ = ["composite_tag", "txt", "raw"]


@lru_cache(maxsize=CacheConfig.MAXSIZE)
def txt(text: str) -> bytes:
    return escape(text).encode()


@lru_cache(maxsize=CacheConfig.MAXSIZE)
def raw(text: str) -> bytes:
    return text.encode()


@lru_cache(maxsize=CacheConfig.MAXSIZE)
def comment(text: str) -> bytes:
    return (f"<!-- {escape(text)} -->").encode()


@lru_cache(maxsize=CacheConfig.MAXSIZE)
def doctype(*attrs: str) -> bytes:
    return (f"<!DOCTYPE {' '.join(fmt_prop(x, None) for x in attrs)}>").encode()


def leaf_tag(tagname: str) -> callable:
    @lru_cache(maxsize=CacheConfig.MAXSIZE)
    def set_props(*bool_props: str, **kv_props: str) -> bytes:

        if bool_props and callable(bool_props[0]):
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


def composite_tag(tagname: str) -> callable:
    @lru_cache(maxsize=CacheConfig.MAXSIZE)
    def set_props(*bool_props: str, **kv_props: str) -> callable:

        if bool_props and callable(bool_props[0]):
            raise ValueError(
                f"{tagname}(!WEIRD THINGS PASSED HERE!): here you pass tag attributes, not child elements."
                f" Follow this syntax: {tagname}(*args, **kwargs)(element1, element2, ...)"
            )

        @lru_cache(maxsize=CacheConfig.MAXSIZE)
        def set_children(*children: tuple) -> bytes:

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
