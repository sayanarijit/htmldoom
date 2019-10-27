__author__ = "Arijit Basu"
__email__ = "sayanarijit@gmail.com"
__homepage__ = "https://github.com/sayanarijit/htmldoom"
__description__ = "An intuitive, high performance HTML rendering framework"

__version__ = "v0.8.0"
__license__ = "MIT"
__all__ = [
    "__author__",
    "__email__",
    "__homepage__",
    "__description__",
    "__version__",
    "__license__",
    "doctype",
    "render",
    "renders",
    "raw",
    "txt",
    "comment",
    "CacheConfig",
    "loadraw",
    "loadtxt",
]

from htmldoom.base import comment, doctype, raw, txt
from htmldoom.conf import CacheConfig
from htmldoom.util import loadraw, loadtxt, render, renders
