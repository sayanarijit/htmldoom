"""Built-in layouts."""

import typing as t
from types import MappingProxyType

from htmldoom import elements as e

__all__ = ["BaseLayout", "Component"]


class BaseLayout:
    """HTML layout for a basic page.

    Optional arguments:
        data: Dynamic data to render.

    Usage:
        >>> from htmldoom import elements as e
        >>> from htmldoom.layouts import BaseLayout
        >>> 
        >>> class MyLayout(BaseLayout):
        ...     @property
        ...     def title(self) -> e.Title:
        ...         return e.Title()(self["title"])
        ...     @property
        ...     def body(self) -> e.Body:
        ...         return e.Body()(f"Welcome {self['user']['name']}")
        ... 
        >>> MyLayout({"title": "foo", "user": {"name": "bar"}})
        <!DOCTYPE html>
        <html><head><title>foo</title></head><body>Welcome bar</body></html>
    """

    def __init__(self, data: t.Optional[t.Mapping[object, object]] = None) -> None:
        self.data: MappingProxyType = MappingProxyType(data or {})

    @property
    def doctype(self) -> e.DocType:
        """Doctype."""
        return e.DocType("html")

    @property
    def title(self) -> e.Title:
        """Document title."""
        return e.Title()

    @property
    def html(self) -> e.HTML:
        """Document HTML"""
        return e.HTML()(self.head, self.body)

    @property
    def head(self) -> e.Head:
        """Document head"""
        return e.Head()(self.title)

    @property
    def body(self) -> e.Body:
        """Document body"""
        return e.Body()

    def __getitem__(self, name: object) -> object:
        return self.data[name]

    def render(self) -> t.Tuple[e.DocType, e.HTML]:
        return self.doctype, self.html

    def __repr__(self) -> str:
        return "\n".join(map(str, self.render()))


class Component:
    """HTML component.
    
    Optional arguments:
        data: Dynamic data to render.

    Usage:
        >>> from htmldoom import elements as e
        >>> from htmldoom.layouts import Component
        >>> 
        >>> class MyForm(Component):
        ...     @property
        ...     def textbox(self) -> e.Input:
        ...         return e.Input()
        ...     @property
        ...     def submit_btn(self) -> e.Button:
        ...         return e.Button()("update" if self["submitted"] else "submit")
        ...     def render(self) -> e.Form:
        ...         return e.Form()(self.textbox, e.Br(), self.submit_btn)
        ... 
        >>> MyForm({"submitted": False})
        <form><input /><br /><button>submit</button></form>
    """

    def __init__(self, data: t.Optional[t.Mapping[object, object]] = None) -> None:
        self.data: MappingProxyType = MappingProxyType(data or {})

    def __getitem__(self, name: object) -> object:
        return self.data[name]

    def render(self) -> object:
        return e._Text(str(self.data))

    def __repr__(self) -> str:
        return str(self.render())
