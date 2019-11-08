import os
from types import MappingProxyType

import markdown2

import htmldoom
from components import document
from htmldoom import loadtxt, render
from htmldoom.value_loader import EXTENSION_RENDERERS, loadvalues

SRC_DIR = "docs/src"
DIST_DIR = "docs/static"


def md_to_html(path):
    with open(path) as f:
        html = markdown2.markdown(f.read())
    return html


EXTENSION_RENDERERS = dict(md=md_to_html, **EXTENSION_RENDERERS)


def render_page(page):
    """Render a page."""

    common_values = loadvalues(f"{SRC_DIR}/values")
    page_values = loadvalues(
        f"{SRC_DIR}/pages/{page}", extension_renderers=EXTENSION_RENDERERS
    )
    return render(document(p=page_values, c=common_values))


def main():
    """Generate the static docs."""

    if not os.path.exists(DIST_DIR):
        os.mkdir(DIST_DIR)

    for page in os.listdir(f"{SRC_DIR}/pages"):
        doc = render_page(page)
        with open(f"{DIST_DIR}/{page}.html", "w") as f:
            f.write(doc)


if __name__ == "__main__":
    main()
