import pytest

from htmldoom import elements as e
from htmldoom import render
from htmldoom.base import composite_tag, leaf_tag
from htmldoom.yaml_loader import VALID_FORMAT
from htmldoom.yaml_loader import loadyaml as ly

YAML_COMPONENTS = "tests/assets/yaml_components/valid.yml"
YAML_INVALID_COMPONENTS = "tests/assets/yaml_components/invalid.yml"


def test_loadyaml_dynamic():
    my_alert = ly("tests/assets/yaml_components/red_alert.yml")
    your_alert = e.div()(
        e.span("boolattr", style="background-color: red", class_="alert")(
            "This is an Alert"
        ),
        e.i(class_="horror")("{!}"),
    )
    assert my_alert == your_alert


def test_loadyaml_static():
    my_alert = ly("tests/assets/yaml_components/red_alert.yml", static=True)
    your_alert = e.div()(
        e.span("boolattr", style="background-color: red", class_="alert")(
            "This is an Alert"
        ),
        e.i(class_="horror")("{{!}}"),
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


def test_invalid_format():
    for i in range(13):
        with pytest.raises(ValueError) as e:
            ly(YAML_INVALID_COMPONENTS, str(i))
        assert VALID_FORMAT in str(e.value)
