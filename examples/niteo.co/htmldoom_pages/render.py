from htmldoom_pages.index import render as _render


def render():
    return _render({"doctitle": "Niteo - Empowering small businesses online since '07"})


if __name__ == "__main__":
    print(render())
