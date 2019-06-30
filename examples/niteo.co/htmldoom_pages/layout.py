from htmldoom import base as b
from htmldoom import elements as e
from htmldoom import render as _render
from htmldoom import renders

doctype = _render(b.doctype("html"))


@renders(e.title()("{doctitle}"))
def render_title(data: dict) -> dict:
    return {"doctitle": data["doctitle"]}


@renders(
    e.head()(
        "{title}",
        e.meta(
            name="description",
            content=(
                "Niteo is a decade old SaaS studio full of bright ideas, "
                "building smart   solutions that empower small businesses online."
            ),
        ),
        e.meta(charset="utf-8"),
        e.meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        e.meta(name="twitter:card", content="summary_large_image"),
        e.meta(
            name="twitter:title",
            content="Niteo - Empowering small businesses online since '07",
        ),
        e.meta(
            name="twitter:description",
            content=(
                "Niteo is a decade old SaaS studio full of bright ideas, "
                "building smart   solutions that empower small businesses online."
            ),
        ),
        e.meta(name="twitter:site", content="@teamniteo"),
        e.meta(
            name="twitter:image",
            content="https://niteo.co/static_niteo_co/images/social/homepage.png",
        ),
        e.meta(property_="og:type", content="website"),
        e.meta(content="https://niteo.co/", property_="og:url"),
        e.meta(
            property_="og:title",
            content="Niteo - Empowering small businesses online since '07",
        ),
        e.meta(
            property_="og:description",
            content="Niteo is a decade old SaaS studio full of bright ideas, building smart   solutions that empower small businesses online.",
        ),
        e.meta(
            property_="og:image",
            content="https://niteo.co/static_niteo_co/images/social/homepage.png",
        ),
        e.meta(property_="og:image:width", content="1200"),
        e.meta(property_="og:image:height", content="630"),
        e.link(
            rel="apple-touch-icon",
            sizes="180x180",
            href="https://niteo.co/static_niteo_co/images/favicon/apple-touch-icon.png",
        ),
        e.link(
            rel="icon",
            type_="image/png",
            sizes="32x32",
            href="https://niteo.co/static_niteo_co/images/favicon/favicon-32x32.png",
        ),
        e.link(
            rel="icon",
            type_="image/png",
            sizes="16x16",
            href="https://niteo.co/static_niteo_co/images/favicon/favicon-16x16.png",
        ),
        e.link(
            rel="manifest",
            href="https://niteo.co/static_niteo_co/images/favicon/site.webmanifest",
        ),
        e.link(
            rel="mask-icon",
            href="https://niteo.co/static_niteo_co/images/favicon/safari-pinned-tab.svg",
            color="#5bbad5",
        ),
        e.link(
            rel="shortcut icon",
            href="https://niteo.co/static_niteo_co/images/favicon/favicon.ico",
        ),
        e.meta(name="msapplication-TileColor", content="#00aba9"),
        e.meta(
            name="msapplication-config",
            content="https://niteo.co/static_niteo_co/images/favicon/browserconfig.xml",
        ),
        e.meta(name="theme-color", content="#ffffff"),
        e.link(href="https://niteo.co/static_niteo_co/main.css", rel="stylesheet"),
        e.script(
            crossorigin="anonymous", src="/fanstatic/minisites/jquery-2.2.4.min.js"
        ),
    )
)
def render_head(data: dict, title_renderer: callable = render_title) -> dict:
    return {"title": title_renderer(data=data)}


@renders(e.body()("{contents}"))
def render_body(data) -> None:
    raise NotImplementedError("You are trying to render a base layout.")


@renders(e.html(lang="en", prefix="og: http://ogp.me/ns#")("{head}", "{body}"))
def render_html(
    data: dict,
    title_renderer: callable = render_title,
    head_renderer: callable = render_head,
    body_renderer: callable = render_body,
) -> dict:
    return {
        "head": head_renderer(data=data, title_renderer=render_title),
        "body": body_renderer(data=data),
    }


@renders("{doctype}{html}")
def render_document(
    data: dict,
    title_renderer: callable = render_title,
    head_renderer: callable = render_head,
    body_renderer: callable = render_body,
    html_renderer: callable = render_html,
) -> dict:
    return {
        "doctype": doctype,
        "html": html_renderer(
            data=data,
            title_renderer=title_renderer,
            head_renderer=head_renderer,
            body_renderer=body_renderer,
        ),
    }


def render(data: dict) -> str:
    return render_document(data=data)


if __name__ == "__main__":
    print(render({}))
