"""Built-in layouts."""

from htmldoom import elements as e

import typing as t


class BaseLayout:
    """HTML layout for a basic page.

    Usage:
        >>> from htmldoom import elements as e
        >>> from htmldoom.layouts import BaseLayout
        >>> 
        >>> class MyLayout(BaseLayout):
        ...     @property
        ...     def title(self) -> e.Title:
        ...         return e.Title(self.data["title"])
        ...     @property
        ...     def body(self) -> e.Body:
        ...         return e.Body(f"Welcome {self.data['user']['name']}")
        ... 
        ... MyLayout({"title": "foo", "user": {"name": "bar"}})
        '<!DOCTYPE html>\n<html><head><title>foo</title></head><body>Welcome bar</body></html>'
    """

    def __init__(self, data: t.Any = None) -> None:
        self.data = data

    @property
    def doctype(self) -> e.DocType:
        """Doctype."""
        return e.DocType("html")

    @property
    def title(self) -> e.Title:
        """Document title."""
        return e.Title()

    @property
    def head(self) -> e.Head:
        """Document head"""
        return e.Head()(self.title)

    @property
    def body(self) -> e.Body:
        """Document body"""
        return e.Body()

    def __repr__(self) -> str:
        return f"{self.doctype}\n{e.HTML()(self.head, self.body)}"
