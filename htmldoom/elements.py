import re
from functools import lru_cache
from html import escape

MAX_CACHE_SIZE = 12800


@lru_cache(maxsize=MAX_CACHE_SIZE)
def _double_quote(txt: str) -> str:
    """Double quote strings safely for attributes.
    
    Usage:
        >>> double_quote('abc"xyz')
        '"abc\\"xyz"'
    """
    return '"{}"'.format(txt.replace('"', '\\"'))


@lru_cache(maxsize=MAX_CACHE_SIZE)
def _fmt_prop(key: str, val: str) -> str:
    """Format a key-value pair for an HTML tag."""
    if val is None:
        if re.sub("[a-zA-Z_]", "", key):
            return double_quote(key)
        return key
    return f"{key}={_double_quote(val)}"


@lru_cache(maxsize=MAX_CACHE_SIZE)
def _render(func: callable) -> str:
    return func()


@lru_cache(maxsize=MAX_CACHE_SIZE)
def _composite_tag(func: callable) -> callable:
    tagname = func()

    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def wrapped(*attrs: str, **props: str) -> callable:
        @lru_cache(maxsize=MAX_CACHE_SIZE)
        def wrapped(*children: tuple) -> str:
            @lru_cache(maxsize=MAX_CACHE_SIZE)
            def wrapped():

                if not attrs and not props:
                    return f"<{tagname}>{''.join(map(_render, children))}</{tagname}>"

                if not props:
                    return (
                        f"<{tagname} {' '.join(_fmt_prop(x, None) for x in attrs)}>"
                        f"{''.join(map(_render, children))}</{tagname}>"
                    )
                if not attrs:
                    return (
                        f"<{tagname} {' '.join(_fmt_prop(k, v) for k, v in props.items())}>"
                        f"{''.join(map(_render, children))}</{tagname}>"
                    )

                return (
                    f"<{tagname} {' '.join(_fmt_prop(x, None) for x in attrs)}"
                    f" {' '.join(_fmt_prop(k, v) for k, v in props.items())}>"
                    f"{''.join(map(_render, children))}</{tagname}>"
                )

            return wrapped

        return wrapped

    return wrapped


@lru_cache(maxsize=MAX_CACHE_SIZE)
def _norrmalize_props(*attrs: str, **props: str) -> tuple:
    result = dict({x: None for x in attrs}, **props)
    return tuple(result.items())


@lru_cache(maxsize=MAX_CACHE_SIZE)
def _txt(text: str) -> callable:
    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def wrapped() -> str:
        return escape(text)

    return wrapped


@lru_cache(maxsize=MAX_CACHE_SIZE)
def _raw(text: str) -> callable:
    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def wrapped() -> str:
        return text

    return wrapped


@_composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def p(*attrs: str, **props: str) -> str:
    return "p"


@_composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def div(*attrs: str, **props: str) -> str:
    return "div"


@_composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def body(*attrs: str, **props: str) -> str:
    return "body"


@_composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def footer(*attrs: str, **props: str) -> str:
    return "footer"


@_composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def title(*attrs: str, **props: str) -> str:
    return "title"


@_composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def head(*attrs: str, **props: str) -> str:
    return "head"


@_composite_tag
@lru_cache(maxsize=MAX_CACHE_SIZE)
def html(*attrs: str, **props: str) -> str:
    return "html"
