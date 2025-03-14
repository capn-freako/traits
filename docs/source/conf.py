# (C) Copyright 2005-2025 Enthought, Inc., Austin, TX
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in LICENSE.txt and may be redistributed only under
# the conditions described in the aforementioned license. The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
#
# Thanks for using Enthought open source!

# Traits documentation build configuration file, created by
# sphinx-quickstart on Tue Jul 22 10:52:03 2008.
#
# This file is execfile()d with the current directory set to its containing
# dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed
# automatically).
#
# All configuration values have a default value; values that are commented out
# serve to show the default value.

import os
import sys


# The docset build will use slightly different formatting rules
BUILD_DOCSET = bool(os.environ.get("BUILD_DOCSET"))

# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
sys.path.append(os.path.abspath("../../"))


# General configuration
# ---------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "traits.util.trait_documenter",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General substitutions.
project = "traits"
copyright = """\
(C) Copyright 2005-2025 Enthought, Inc., Austin, TX
All rights reserved.
"""

# The default replacements for |version| and |release|, also used in various
# other places throughout the built documents.
version_info = {}
traits_init_path = os.path.join("..", "..", "traits", "__init__.py")
with open(traits_init_path, "r", encoding="utf-8") as version_module:
    version_code = compile(version_module.read(), "__init__.py", "exec")
    exec(version_code, version_info)

# "release" is the full version string, including the bugfix portion and any
# modifiers. "version" is of the form "6.2" and is what's used in titles.
release = version_info["__version__"]
version = ".".join(release.split(".")[:2])

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = "%B %d, %Y"

# List of documents that shouldn't be included in the build.
# unused_docs = []

# List of directories, relative to source directories, that shouldn't be
# searched for source files.
# exclude_dirs = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# Options for the autodoc extension.
autodoc_default_options = {
    "members": None,
}

autodoc_member_order = "bysource"

# Options for HTML output
# -----------------------

# Use enthought-sphinx-theme if available
try:
    import enthought_sphinx_theme

    html_theme_path = [enthought_sphinx_theme.theme_path]
    html_theme = "enthought"

    html_static_path = []
    templates_path = []

except ImportError as exc:
    import warnings

    msg = """Can't find Enthought Sphinx Theme, using default.
                Exception was: {}
                Enthought Sphinx Theme can be installed from PyPI or EDM"""
    warnings.warn(RuntimeWarning(msg.format(exc)))

    # Use old defaults if enthought-sphinx-theme not available

    # The name of an image file (within the static path) to place at the top
    # of the sidebar.
    html_logo = os.path.join("_static", "e-logo-rev.png")

    # The name of an image file (within the static path) to use as favicon of
    # the docs.  This file should be a Windows icon file (.ico) being 16x16
    # or 32x32 pixels large.
    html_favicon = os.path.join("_static", "et.ico")

    # The style sheet to use for HTML and HTML Help pages. A file of that name
    # must exist either in Sphinx' static/ path, or in one of the custom paths
    # given in html_static_path.
    html_style = "default.css"

    # Add any paths that contain custom static files (such as style sheets)
    # here, relative to this directory. They are copied after the builtin
    # static files, so a file named "default.css" will overwrite the builtin
    # "default.css".
    html_static_path = ["_static"]

    # Add any paths that contain templates here, relative to this directory.
    templates_path = ["_templates"]


# When using docset browsers like Dash and Zeal the side bar is redundant.
if BUILD_DOCSET:
    html_theme_options = {"nosidebar": "true"}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Traits {version} Documentation".format(version=version)

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = "%b %d, %Y"

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
# html_copy_source = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = "Traitsdoc"


# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
# latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author,
#  document class [howto/manual]).
latex_documents = [
    (
        "index",
        "Traits.tex",
        "Traits {version} User Manual".format(version=version),
        "Enthought, Inc.",
        "manual",
    )
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = "enthought_logo.jpg"
latex_logo = "e-logo-rev.png"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_use_modindex = True

# Options for Texinfo output
# --------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "traits",
        "Traits {version} User Manual".format(version=version),
        "Enthought, Inc.",
        "Traits",
        "Explicitly typed attributes for Python.",
        "Python",
    )
]

# Options for intersphinx extension
# ---------------------------------

intersphinx_mapping = {
    "pyface": ("https://docs.enthought.com/pyface", None),
    "python": ("https://docs.python.org/3", None),
    "traitsui": ("https://docs.enthought.com/traitsui", None),
}
