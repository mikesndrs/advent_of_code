"""
Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import datetime
import sys

# Sphinx extention to format xarray/pandas summaries
import sphinx_autosummary_accessors
from jinja2.defaults import DEFAULT_FILTERS
from packaging.version import Version

import aoc

print("python exec:", sys.executable)
print("sys.path:", sys.path)

# -- Project information -----------------------------------------------------
# The documented project’s name
project = src_project = PROJECT = "aoc"
PACKAGE = "aoc"

# A copyright statement in the style '2008, Author Name'.
copyright = f"2020-{datetime.datetime.now().year}"
# The author name(s) of the document
author = "Mike Sanders"
src_host = "mikesndrsspam@gmail.com"

# Parse urls here for convenience, to be re-used

# Advent of Code
repo_url = "https://github.com/mikesndrs/advent_of_code"


# Configuration of sphinx.ext.extlinks
# See https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html
# unique name: (base URL, label prefix)
extlinks = {
    "src": (repo_url, "src"),
}

full_version = Version(aoc.__version__)

# version: The major project version, used as the replacement for |version|.
#   For example, for the Python documentation, this may be something like 2.6.
version = full_version.base_version

# release: The full project version, used as the replacement for |release| and
#   e.g. in the HTML templates. For example, for the Python documentation, this
#   may be something like 2.6.0rc1
release = str(full_version)


# -- General configuration ---------------------------------------------------
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",  # To auto-generate docs from Python docstrings
    "sphinx.ext.todo",  # Support for todo items
    "sphinx.ext.napoleon",  # Support for NumPy and Google style docstrings
    "sphinx.ext.intersphinx",  # Generate links to other documentation files
    "sphinx.ext.autosummary",  # For summarizing autodoc-generated files
    "sphinx.ext.extlinks",  # For shortening internal links
    "sphinx.ext.mathjax",  # Render math as images
    "sphinx_immaterial",  # Sphinx immaterial theme
]

todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates", sphinx_autosummary_accessors.templates_path]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = "%Y-%m-%d"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_immaterial"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# and
# https://sphinx-immaterial.readthedocs.io/en/latest/customization.html#confval-html_theme_options
html_theme_options = {
    "repo_url": repo_url,
    "repo_name": "Advent of Code",
    "icon": {
        "repo": "fontawesome/brands/bitbucket",
    },
    "features": [
        # "navigation.expand",
        # "navigation.tabs",
        "navigation.sections",
        "navigation.instant",
        # "header.autohide",
        "navigation.top",
        # "navigation.tracking",
        # "search.highlight",
        # "search.share",
        # "toc.integrate",
        "toc.follow",
        "toc.sticky",
        # "content.tabs.link",
        "announce.dismiss",
    ],
    # "toc_title_is_page_title": True,
    # "globaltoc_collapse": True,
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "indigo",
            "accent": "green",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "light-blue",
            "accent": "lime",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Switch to light mode",
            },
        },
    ],
}

# Shorten Table Of Contents in API documentation
object_description_options = [
    (".*", dict(include_fields_in_toc=False)),
    (".*parameter", dict(include_in_toc=False)),
]

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# '<project> v<release> documentation'.
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = "_static/imaspy_200x200.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ["_static"]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = today_fmt

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, 'Created using Sphinx' is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, '(C) Copyright ...' is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. '.xhtml').
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = "aoc_doc"


# -- Extension configuration -------------------------------------------------
# Configuration of sphinx.ext.autodoc
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
autodoc_typehints = "signature"


# Configuration of sphinx.ext.autosummary
# https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html
autosummary_generate = True


# Configuration of sphinx.ext.napoleon
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
# Support for NumPy and Google style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
# Allow PEP 526 attributes annotations in classes:
napoleon_attr_annotations = True


# Configuration of sphinx.ext.intersphinx
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "packaging": ("https://packaging.pypa.io/en/stable/", None),
}
intersphinx_timeout = 60  # Downloads time out after 1 minute

# Configuration of sphinx.ext.mathjax
# https://www.sphinx-doc.org/en/master/usage/extensions/math.html#module-sphinx.ext.mathjax


def escape_underscores(string):
    return string.replace("_", r"\_")


def setup(app):
    DEFAULT_FILTERS["escape_underscores"] = escape_underscores
    app.add_css_file("aoc.css")