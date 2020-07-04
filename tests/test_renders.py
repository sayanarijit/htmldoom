from htmldoom import render, renders, elements as e, functions as fn


@renders(e.li()("{item}"))
def render_list_item(item):
    return {"item": item}


@renders(e.p()("{foo}"), e.ul()("{list_items}"))
def render_component():
    return {
        "foo": "bar",
        "list_items": fn.foreach(["a", "b", "c"])(lambda x: render_list_item(x)),
    }


def test_renders():
    assert (
        render(render_component())
        == "<p>bar</p><ul><li>a</li><li>b</li><li>c</li></ul>"
    )
