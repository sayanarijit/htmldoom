from htmldoom import base as b
from htmldoom import elements as e
from htmldoom import render as _render
from htmldoom import renders
from htmldoom_pages.layout import render_document


@renders(
    e.tr(class_="spacer", style="height:5px"),
    e.tr(class_="athing", id_="{id}")(
        e.td(align="right", valign="top", class_="title")(
            e.span(class_="rank")("{rank}.")
        ),
        e.td(valign="top", class_="votelinks")(
            e.center()(
                e.a(id_="up_{id}", href="vote?id={id}&how=up&goto=news")(
                    e.div(class_="votearrow", title="upvote")
                )
            )
        ),
        e.td(class_="title")(
            e.a(href="{href}", class_="storylink")("{title}"),
            e.span(class_="sitebit comhead")(
                " (",
                e.a(href="from?site={from_url}")(
                    e.span(class_="sitestr")("{from_name}")
                ),
                ")",
            ),
        ),
    ),
    e.tr()(
        e.td(colspan="2"),
        e.td(class_="subtext")(
            e.span(class_="score", id_="score_{id}")("{score} points"),
            " by ",
            e.a(href="user?id={username}", class_="hnuser")("{username}"),
            " ",
            e.span(class_="age")(e.a(href="item?id=20320212")("{timeago}")),
            " ",
            e.span(id_="unv_{id}"),
            " | ",
            e.a(href="hide?id={id}&goto=news")("hide"),
            " | ",
            e.a(href="item?id={id}")("{comments_count} comments"),
            " ",
        ),
    ),
    e.tr(class_="spacer", style="height:5px"),
)
def render_news(rank: int, news: dict) -> dict:
    return dict(news, rank=rank)


def render(data: dict) -> str:
    return render_document(data=data, news_renderer=render_news)


if __name__ == "__main__":
    import json

    with open("news.json") as f:
        news = json.load(f)

    print(_render({"news": {i: news for i in range(500)}}))
