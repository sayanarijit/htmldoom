import os
from collections import namedtuple
from types import MappingProxyType

from htmldoom.util import loadraw, loadtxt, render
from htmldoom.yaml_loader import loadyaml

EXTENSION_RENDERERS = MappingProxyType(
    {
        "txt": lambda path: render(loadtxt(path)),
        "html": lambda path: render(loadraw(path)),
        "css": lambda path: render(loadraw(path)),
        "js": lambda path: render(loadraw(path)),
        "yml": lambda path: render(loadyaml(path)),
        "yaml": lambda path: render(loadyaml(path)),
    }
)


def loadvalues(path, extension_renderers=None):
    """Scan a directory and load the values in a nested namedtuple.

    Arguments:
        path: Path to the directory of files containing values.
        extension_renderers: A map of file extensions and their renderers.

    Example:
        >>> from htmldoom.value_loader import loadvalues
        >>> 
        >>> values = loadvalues("path/to/values")
        >>> 
        >>> values.foo
        'bar'
    """

    if extension_renderers is None:
        extension_renderers = EXTENSION_RENDERERS

    nodes = {}
    for node in os.listdir(path):
        _path = os.path.join(path, node)
        if os.path.isdir(_path):
            filename, value = node, loadvalues(_path)
        else:
            if node.count(".") != 1:
                raise NameError(f"{_path}: Invalid filename.")

            r_extension, r_filename = node[::-1].split(".", 1)
            filename, extension = r_filename[::-1], r_extension[::-1]

            if extension not in extension_renderers:
                raise TypeError(f"{_path}: No render found for this file type.")

            if filename in nodes:
                raise NameError(f"{_path}: Duplicate file name: {filename}.")

            value = extension_renderers[extension](_path)

        nodes[filename] = value
    return namedtuple("Values", nodes.keys())(**nodes)
