"""Helpers to render YAML data into HTML components.

Find the examples YAML formats in: tests/assets/yaml_components/valid.yml
Or the `VALID_FORMAT` variable in this module.
"""

from functools import lru_cache

from yaml import SafeLoader, dump, load

from htmldoom import render
from htmldoom.base import composite_tag, leaf_tag, txt
from htmldoom.conf import CacheConfig

VALID_FORMAT = """
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
                f"Some examples for you:\n{VALID_FORMAT}"
            )

    if inner is None:
        return leaf_tag(tagname)(*bool_props, **kv_props)
    return composite_tag(tagname)(*bool_props, **kv_props)(inner)


def parse(data):
    """Parses given data data into HTML elements.

    Arguments:
        data union(str, bytes, dict, list):
            Data to parse.

    Examples:
        >>> from htmldoom.yaml_loader import parse
        >>> 
        >>> parse({
        ...     "div": [
        ...         {"class": "row"},
        ...         [
        ...             "This is an element.",
        ...             " ",
        ...             {"i": [["*"]]},
        ...         ],
        ...     ]
        ... })
        b'<div class="row">This is an element. <i>*</i></div>'
    """

    if isinstance(data, dict):

        if len(data) != 1:
            raise ValueError(
                "\n{invalid}^^^ Invalid format. Valid format is:\n{valid}".format(
                    invalid=dump(data, indent=2), valid=VALID_FORMAT
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
                    "\n{invalid}^^^ Invalid format. Valid format is:\n{valid}".format(
                        invalid=dump(data, indent=2), valid=VALID_FORMAT
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
                "\n{invalid}^^^ Invalid format. Valid format is:\n{valid}".format(
                    invalid=dump(data, indent=2), valid=VALID_FORMAT
                )
            )

        return _to_element(tagname, attributes, inner)

    if isinstance(data, list):
        return render(*[parse(x) for x in data if x is not None]).encode()

    return render(data).encode()


@lru_cache(maxsize=CacheConfig.MAXSIZE)
def loadyaml(path, directive=None, static=False):
    """Loads given YAML file/directive into HTML

    Arguments:
        path (str): Path to the YAML file.
        directive (optional(str)):
            Dot (.) separated values to find component definition.
            If not specified, the whole content of the file is assumed
            to be the component definition.
        static (bool):
            If True, all the `{` and `}` will be replaced
            with `{{` and `}}` respectively.
    
    Examples:
        >>> from htmldoom.yaml_loader import loadyaml
        >>> 
        >>> loadyaml("/path/to/component.yml")
        b'<p>{foo}</p>'
        >>> 
        >>> loadyaml("/path/to/components.yml", static=True)
        b'<p>{foo}</p>'
        >>> 
        >>> loadyaml("/path/to/components.yml", "paragraph.myfav", static=True)
        b'<p>{foo}</p>'
        >>> 
        >>> loadyaml("/path/to/components.yml", ("paragraph", "case", True))
        b'<p>{foo}</p>'
    """
    with open(path) as f:
        elements = load(f, Loader=SafeLoader)

    if isinstance(directive, str):
        directive = directive.split(".")

    if directive:
        for node in directive:
            elements = elements[node]

    if elements is None:
        raise ValueError(
            f"Invalid format here: {path} Valid format is:\n{VALID_FORMAT}"
        )

    data = parse(elements)
    if static:
        data = data.decode().replace("{", "{{").replace("}", "}}").encode()
    return data
