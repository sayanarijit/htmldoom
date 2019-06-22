import unittest

from htmldoom import elements as e
from htmldoom.layouts import BaseLayout, Component


class TestComponent(unittest.TestCase):
    def test_render(self):
        class Form(Component):
            @property
            def textbox(self) -> e.Input:
                return e.Input()

            @property
            def submit_btn(self) -> e.Button:
                return e.Button()("update" if self.data["submitted"] else "submit")

            @property
            def render(self) -> e.Form:
                return e.Form()(self.textbox, self.submit_btn)

        form1 = Form({"submitted": False})
        form2 = Form({"submitted": True})

        assert repr(form1) == "<form><input /><button>submit</button></form>"
        assert repr(form2) == "<form><input /><button>update</button></form>"


class TestBaseLayout(unittest.TestCase):
    def test_default(self):
        layout = BaseLayout()
        html = (
            "<!DOCTYPE html>\n"
            "<html>"
            "<head><title></title></head>"
            "<body></body>"
            "</html>"
        )
        assert repr(layout) == html

    def test_custom(self):
        html = (
            "<!DOCTYPE html>\n"
            "<html>"
            "<head><title>foo</title></head>"
            "<body>Welcome bar</body>"
            "</html>"
        )

        class MyLayout(BaseLayout):
            @property
            def title(self) -> e.Title:
                return e.Title()(self.data["title"])

            @property
            def body(self) -> e.Body:
                return e.Body()(f"Welcome {self.data['user']['name']}")

        layout = MyLayout({"title": "foo", "user": {"name": "bar"}})
        assert repr(layout) == html


if __name__ == "__main__":
    unittest.main()
