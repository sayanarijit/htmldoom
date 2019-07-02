import json

from jinja2 import FileSystemLoader
from jinja2.environment import Environment

env = Environment()
env.loader = FileSystemLoader(".")
jinja2_renderer = env.get_template("jinja2_pages/index.html")

with open("news.json") as f:
    news = json.load(f)


def render(count=500):
    return jinja2_renderer.render({"news": {i: news for i in range(count)}})


if __name__ == "__main__":
    print(render())
