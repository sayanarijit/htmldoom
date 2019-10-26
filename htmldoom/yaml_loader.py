"""Helpers to render YAML data into HTML components.

Find the examples YAML formats in: tests/assets/yaml_components/correct.yml
Or the `EXAMPLE_FORMAT` variable in this module.
"""

from functools import lru_cache

from yaml import SafeLoader, dump, load

from htmldoom import render
from htmldoom.base import composite_tag, leaf_tag
from htmldoom.conf import CacheConfig

EXAMPLE_FORMAT = """
* Leaf tag: <tagname />
----------------------------
tagname: [{}]
----------------------------

OR

* Composite tag: <tagname></tagname>
----------------------------
tagname: [[]]
----------------------------

OR

* Leaf tag with attributes: <tagname attribute1 attribute2="attrval" />
----------------------------
tagname: [{ attribute1: true, attribute2: attrval }]
----------------------------

OR

Composite tag with attributes: <tagname attribute1 attribute2="attrval"></tagname>
----------------------------
tagname: [{ attribute1: true, attribute2: attrval }, []]
----------------------------

OR

Composite tag with values: <tagname>value1 value2</tagname>
----------------------------
tagname: [[ value1, " ", value2 ]]
----------------------------

OR

Composite tag with attributes and values: <tagname attribute1 attribute2="attrval">value1 value2</tagname>
----------------------------
tagname:
- attribute1: true
  attribute2: attrval
- - value1
  - " "
  - value2
----------------------------
"""


def _to_element(tagname, attributes=None, inner=None):
    """Format given values into an HTML elements."""

    if not attributes:
        if inner is None:
            return leaf_tag(tagname)()
        return composite_tag(tagname)()(inner)

    bool_props, kv_props = [], {}
    for k, v in attributes.items():
        if v is True:
            bool_props.append(k)
        elif isinstance(v, str):
            kv_props[k] = v
        else:
            raise ValueError(
                f"{kv_props}\n^^^ `{v}`: Expected `str` but got `{type(v)}`. "
                f"Some examples for you:\n{EXAMPLE_FORMAT}"
            )

    if inner is None:
        return leaf_tag(tagname)(*bool_props, **kv_props)
    return composite_tag(tagname)(*bool_props, **kv_props)(inner)


def parse(data):
    """Parses given data data into HTML elements."""

    if isinstance(data, dict):

        if len(data) != 1:
            raise ValueError(
                "\n{wrong}^^^ Incorrect format. Correct format is:\n{correct}".format(
                    wrong=dump(data, indent=2), correct=EXAMPLE_FORMAT
                )
            )

        tagname, values = list(data.items())[0]
        attributes, inner = None, None

        if isinstance(values, list) and len(values) == 1:
            val = values[0]

            if isinstance(val, dict):
                attributes = val
            elif isinstance(val, list):
                inner = parse(val)
            else:
                raise ValueError(
                    "\n{wrong}^^^ Incorrect format. Correct format is:\n{correct}".format(
                        wrong=dump(data, indent=2), correct=EXAMPLE_FORMAT
                    )
                )

        elif (
            isinstance(values, list)
            and len(values) == 2
            and isinstance(values[0], dict)
            and isinstance(values[1], list)
        ):
            attributes, inner = values
            if inner is not None:
                inner = parse(inner)

        else:
            raise ValueError(
                "\n{wrong}^^^ Incorrect format. Correct format is:\n{correct}".format(
                    wrong=dump(data, indent=2), correct=EXAMPLE_FORMAT
                )
            )

        return _to_element(tagname, attributes, inner)

    if isinstance(data, list):
        return render(*map(parse, data)).encode()

    return data


@lru_cache(maxsize=CacheConfig.MAXSIZE)
def loadyaml(path, directive=None):
    """Loads given YAML file/directive into HTML

    Arguments:
        path (str): Path to the YAML file.
        directive (optional(str)):
            Dot (.) separated values to find component definition.
            If not specified, the whole content of the file is assumed
            to be the component definition.
    
    Examples:
        >>> loadyaml("/path/to/components.yml")
        # Loads the whole file as HTML component.
        # Example file: "{ p: }"

        >>> loadyaml("/path/to/components.yml", "paragraph")
        # Loads the component defined in "paragraph" directive in the file.
        # Example file: "{paragraph: {p: [{class: row}, ["This is a para"]]}}"
        
        >>> loadyaml("/path/to/components.yml", "paragraphs.first")
        # Loads the component defined in "paragraph.first" directive in the file.
        # Example file: "{paragraph: {first: {p: [{class: row}, ["This is the first para"]]}}}"
    """
    with open(path) as f:
        elements = load(f, Loader=SafeLoader)

    if directive is not None:
        nodes = directive.split(".")
        for node in nodes:
            elements = elements[node]

    return parse(elements)
