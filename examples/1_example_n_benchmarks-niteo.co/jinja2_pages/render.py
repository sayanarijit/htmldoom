from jinja2 import FileSystemLoader
from jinja2.environment import Environment

env = Environment()
env.loader = FileSystemLoader(".")
jinja2_renderer = env.get_template("jinja2_pages/index.html")


def render():
    return jinja2_renderer.render(
        {"doctitle": "Niteo - Empowering small businesses online since '07"}
    )


if __name__ == "__main__":
    print(render())
