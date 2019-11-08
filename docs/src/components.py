from htmldoom import doctype, renders
from htmldoom.yaml_loader import loadyaml as ly

LAYOUTS_DIR = "docs/src/layouts"


@renders(doctype("html"), ly(f"{LAYOUTS_DIR}/fullpage.yml", "default"))
def document(**values):
    """The document renderer."""
    return values
