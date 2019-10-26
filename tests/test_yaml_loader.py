import pytest

from htmldoom import elements as e
from htmldoom import render
from htmldoom.base import composite_tag, leaf_tag
from htmldoom.yaml_loader import EXAMPLE_FORMAT
from htmldoom.yaml_loader import loadyaml as ly

YAML_COMPONENTS = "tests/assets/yaml_components/correct.yml"
YAML_INCORRECT_COMPONENTS = "tests/assets/yaml_components/incorrect.yml"


def test_loadyaml():
    my_alert = ly("tests/assets/yaml_components/red_alert.yml")
    your_alert = e.div()(
        e.span("boolattr", style="background-color: red", class_="alert")(
            "This is an Alert!"
        ),
        e.i(class_="horror"),
    )
    assert my_alert == your_alert


def test_components_leaf_tag_empty():
    my_tag = ly(YAML_COMPONENTS, "leaf_tag.empty")
    your_tag = leaf_tag("sometag")()
    assert my_tag == your_tag


def test_components_leaf_tag_with_attrs():
    my_tag = ly(YAML_COMPONENTS, "leaf_tag.with_attrs")
    your_tag = leaf_tag("sometag")(class_="row")
    assert my_tag == your_tag


def test_components_leaf_tag_with_multiple_tags():
    my_tag = render(ly(YAML_COMPONENTS, "leaf_tag.with_multiple_tags"))
    your_tag = render(leaf_tag("sometag")(), "\n", leaf_tag("sometag")())
    assert my_tag == your_tag


def test_components_composite_tag_empty():
    my_tag = ly(YAML_COMPONENTS, "composite_tag.empty")
    your_tag = composite_tag("sometag")()()
    assert my_tag == your_tag


def test_components_composite_tag_with_attrs():
    my_tag = ly(YAML_COMPONENTS, "composite_tag.with_attrs")
    your_tag = composite_tag("sometag")(class_="row")()
    assert my_tag == your_tag


def test_components_composite_tag_vals():
    my_tag = ly(YAML_COMPONENTS, "composite_tag.with_vals")
    your_tag = composite_tag("sometag")()("val1", "val2")
    assert my_tag == your_tag


def test_components_composite_tag_vals():
    my_tag = ly(YAML_COMPONENTS, "composite_tag.with_attrs_and_vals")
    your_tag = composite_tag("sometag")(class_="row")("val1", "val2")
    assert my_tag == your_tag


def test_components_composite_tag_vals():
    my_tag = ly(YAML_COMPONENTS, "composite_tag.with_nested_tag")
    your_tag = composite_tag("sometag")(class_="row")(e.i()("val"))
    assert my_tag == your_tag


def test_components_leaf_tag_with_multiple_tags():
    my_tag = render(ly(YAML_COMPONENTS, "composite_tag.with_multiple_tags"))
    your_tag = render(
        composite_tag("sometag")()("1"), "\n", composite_tag("sometag")()("2")
    )
    assert my_tag == your_tag


def test_incorrect_format():
    for i in range(12):
        with pytest.raises(ValueError) as e:
            ly(YAML_INCORRECT_COMPONENTS, str(i))
        assert EXAMPLE_FORMAT in str(e.value)
