from htmldoom import base as b
from htmldoom import elements as e
from htmldoom import render as _render
from htmldoom import renders


@renders(
    e.html(op="news")(
        e.head()(
            e.meta(name="referrer", content="origin"),
            e.meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            e.link(
                rel="stylesheet", type_="text/css", href="news.css?9UnLxU8WHV0ou3hRwndX"
            ),
            e.link(rel="shortcut icon", href="favicon.ico"),
            e.link(
                rel="alternate", type_="application/rss+xml", title="RSS", href="rss"
            ),
            e.title()("Hacker News"),
        ),
        e.body()(
            e.center()(
                e.table(
                    id_="hnmain",
                    border="0",
                    cellpadding="0",
                    cellspacing="0",
                    width="85%",
                    bgcolor="#f6f6ef",
                )(
                    e.tr()(
                        e.td(bgcolor="#ff6600")(
                            e.table(
                                border="0",
                                cellpadding="0",
                                cellspacing="0",
                                width="100%",
                                style="padding:2px",
                            )(
                                e.tr()(
                                    e.td(style="width:18px;padding-right:4px")(
                                        e.a(href="https://news.ycombinator.com")(
                                            e.img(
                                                src="y18.gif",
                                                width="18",
                                                height="18",
                                                style="border:1px white solid;",
                                            )
                                        )
                                    ),
                                    e.td(style="line-height:12pt; height:10px;")(
                                        e.span(class_="pagetop")(
                                            e.b(class_="hnname")(
                                                e.a(href="news")("Hacker News ")
                                            ),
                                            e.a(href="newest")("new"),
                                            " | ",
                                            e.a(href="front")("past"),
                                            " | ",
                                            e.a(href="newcomments")("comments"),
                                            " | ",
                                            e.a(href="ask")("ask"),
                                            " | ",
                                            e.a(href="show")("show"),
                                            " | ",
                                            e.a(href="jobs")("jobs"),
                                            " | ",
                                            e.a(href="submit")("submit"),
                                        )
                                    ),
                                    e.td(style="text-align:right;padding-right:4px;")(
                                        e.span(class_="pagetop")(
                                            e.a(href="login?goto=news")("login")
                                        )
                                    ),
                                )
                            )
                        )
                    ),
                    e.tr("title", id_="pagespace", style="height:10px"),
                    e.tr()(
                        e.td()(
                            e.table(
                                border="0",
                                cellpadding="0",
                                cellspacing="0",
                                class_="itemlist",
                            )(
                                "{newslist}",
                                e.tr(class_="morespace", style="height:10px"),
                                e.tr()(
                                    e.td(colspan="2"),
                                    e.td(class_="title")(
                                        e.a(
                                            href="news?p=2",
                                            class_="morelink",
                                            rel="next",
                                        )("More")
                                    ),
                                ),
                            )
                        )
                    ),
                    e.tr()(
                        e.td()(
                            e.img(src="s.gif", height="10", width="0"),
                            e.table(width="100%", cellspacing="0", cellpadding="1")(
                                e.tr()(e.td(bgcolor="#ff6600"))
                            ),
                            e.br(),
                            e.center()(
                                e.a(href="https://www.startupschool.org")(
                                    " Registration is open for Startup School 2019. Classes start July 22nd. "
                                )
                            ),
                            e.br(),
                            e.center()(
                                e.span(class_="yclinks")(
                                    e.a(href="newsguidelines.html")("Guidelines"),
                                    " | ",
                                    e.a(href="newsfaq.html")("FAQ"),
                                    " | ",
                                    e.a(href="mailto:hn@ycombinator.com")("Support"),
                                    " | ",
                                    e.a(href="https://github.com/HackerNews/API")(
                                        "API"
                                    ),
                                    " | ",
                                    e.a(href="security.html")("Security"),
                                    " | ",
                                    e.a(href="lists")("Lists"),
                                    " | ",
                                    e.a(href="bookmarklet.html", rel="nofollow")(
                                        "Bookmarklet"
                                    ),
                                    " | ",
                                    e.a(href="http://www.ycombinator.com/legal/")(
                                        "Legal"
                                    ),
                                    " | ",
                                    e.a(href="http://www.ycombinator.com/apply/")(
                                        "Apply to YC"
                                    ),
                                    " | ",
                                    e.a(href="mailto:hn@ycombinator.com")("Contact"),
                                ),
                                e.br(),
                                e.br(),
                                e.form(action="//hn.algolia.com/", method="get")(
                                    "Search: ",
                                    e.input_(
                                        "value",
                                        type_="text",
                                        name="q",
                                        size="17",
                                        autocorrect="off",
                                        spellcheck="false",
                                        autocapitalize="off",
                                        autocomplete="false",
                                    ),
                                ),
                            ),
                        )
                    ),
                )
            )
        ),
        e.script(type_="text/javascript", src="hn.js?9UnLxU8WHV0ou3hRwndX"),
    )
)
def render_document(data, news_renderer):
    return {
        "newslist": "".join(
            news_renderer(rank=k + 1, news=v) for k, v in data["news"].items()
        )
    }
