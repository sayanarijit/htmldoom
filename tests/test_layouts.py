from htmldoom.layouts import BaseLayout
from htmldoom import elements as e

import unittest


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
