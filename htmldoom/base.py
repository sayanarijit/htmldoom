"""The base"""

from functools import lru_cache
from html import escape

from htmldoom.conf import MAX_CACHE_SIZE
from htmldoom.util import fmt_prop
from htmldoom.util import render as _render

__all__ = ["composite_tag", "txt", "raw"]


@lru_cache(maxsize=MAX_CACHE_SIZE)
def txt(text: str) -> callable:
    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def render() -> str:
        return escape(text)

    return render


@lru_cache(maxsize=MAX_CACHE_SIZE)
def raw(text: str) -> callable:
    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def render() -> str:
        return text

    return render


@lru_cache(maxsize=MAX_CACHE_SIZE)
def comment(text: str) -> callable:
    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def render() -> str:
        return "<!-- {escape(text)} -->"

    return render


@lru_cache(maxsize=MAX_CACHE_SIZE)
def doctype(*attrs: str) -> callable:
    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def render() -> str:
        return "<!DOCTYPE {fmt_prop(x, None) for x in attrs} >"

    return render


@lru_cache(maxsize=MAX_CACHE_SIZE)
def leaf_tag(func: callable) -> callable:
    tagname = func()

    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def set_props(*bool_props: str, **kv_props: str) -> callable:
        @lru_cache(maxsize=MAX_CACHE_SIZE)
        def render():

            if not bool_props and not kv_props:
                return f"<{tagname} />"

            if not kv_props:
                return (
                    f"<{tagname} {' '.join(fmt_prop(x, None) for x in bool_props)} />"
                )
            if not bool_props:
                return f"<{tagname} {' '.join(fmt_prop(k, v) for k, v in kv_props.items())} />"

            return (
                f"<{tagname} {' '.join(fmt_prop(x, None) for x in bool_props)}"
                f" {' '.join(fmt_prop(k, v) for k, v in kv_props.items())} />"
            )

        return render

    return set_props


@lru_cache(maxsize=MAX_CACHE_SIZE)
def composite_tag(func: callable) -> callable:
    tagname = func()

    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def set_props(*bool_props: str, **kv_props: str) -> callable:
        @lru_cache(maxsize=MAX_CACHE_SIZE)
        def set_children(*children: tuple) -> str:
            @lru_cache(maxsize=MAX_CACHE_SIZE)
            def render():

                if not bool_props and not kv_props:
                    return f"<{tagname}>{_render(*children)}</{tagname}>"

                if not kv_props:
                    return (
                        f"<{tagname} {' '.join(fmt_prop(x, None) for x in bool_props)}>"
                        f"{_render(*children)}</{tagname}>"
                    )
                if not bool_props:
                    return (
                        f"<{tagname} {' '.join(fmt_prop(k, v) for k, v in kv_props.items())}>"
                        f"{_render(*children)}</{tagname}>"
                    )

                return (
                    f"<{tagname} {' '.join(fmt_prop(x, None) for x in bool_props)}"
                    f" {' '.join(fmt_prop(k, v) for k, v in kv_props.items())}>"
                    f"{_render(*children)}</{tagname}>"
                )

            return render

        return set_children

    return set_props
