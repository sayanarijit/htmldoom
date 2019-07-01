import json

from htmldoom_pages.index import render as _render

with open("news.json") as f:
    news = json.load(f)


def render(count: int = 500):
    return _render({"news": {i: news for i in range(count)}})


if __name__ == "__main__":
    print(render())
