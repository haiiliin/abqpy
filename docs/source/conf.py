# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

import inspect
import os
import re
import sys
import typing

import abqpy

project = "abqpy"
copyright = "2022, WANG Hailin"
author = "WANG Hailin"

release = abqpy.__version__
major, minor, patch, *_ = release.split(".")
version = major

sys.path.insert(0, os.path.abspath("../../src"))
sys.path.insert(0, os.path.abspath("./_ext"))

# For multiple languages
locale_dirs = [f"locale/{major}"]  # path is example but recommended.
gettext_compact = False  # optional.

# -- General configuration ---------------------------------------------------

# Environment variables
os.environ["ABQPY_MAKE_DOCS"] = "true"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "autoclasstoc",
    "automembers",
    "changes",
    "classdocumenter",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.linkcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
    "sphinx_codeautolink",
    "sphinx_comments",
    "sphinx_design",
    "sphinx_gallery.gen_gallery",
    "sphinx_togglebutton",
    "sphinx_toolbox.confval",
    "sphinx_toolbox.more_autodoc.overloads",
    "sphinxcontrib.programoutput",
    "hoverxref.extension",
    "myst_parser",
    "version",
    "autoapi.extension",
]

# changes configuration
changes_write_to = "CHANGES.md"
changes_versions = [str(v) for v in range(int(major), 2015, -1)]

# sphinx-comments
comments_config = {
    "utterances": {
        "repo": "haiiliin/abqpy",
    }
}

# automembers configuration
automembers_autodoc_options = [
    ":members:",
    ":show-inheritance:",
]

# MyST configuration
myst_enable_extensions = [
    "colon_fence",
]

# AutoAPI configuration
autoapi_dirs = ["../../src/abqpy"]
autoapi_ignore = ["*_version.py"]
autoapi_options = [
    "members",
    "undoc-members",
    "private-members",
    "show-inheritance",
    "show-module-summary",
    "special-members",
    # 'imported-members',
]
autoapi_template_dir = "_autoapi_templates"

# Default behavior for code block concatenation for sphinx_codeautolink
codeautolink_concat_default = False

# Suppress warnings
suppress_warnings = [
    "app.add_directive",
]

intersphinx_mapping = {
    "jinjia2": ("https://jinja.palletsprojects.com/en/3.0.x/", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "pytest": ("https://pytest.org/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "readthedocs": ("https://docs.readthedocs.io/en/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
}

# Hoverxref configuration
hoverxref_auto_ref = True
hoverxref_domains = ["py"]
hoverxref_roles = [
    "numref",
    "confval",
    "setting",
    "option",
    "doc",  # Documentation pages
    "term",  # Glossary terms
]
hoverxref_role_types = {
    "doc": "modal",  # for whole docs
    "mod": "modal",  # for Python Sphinx Domain
    "class": "tooltip",  # for Python Sphinx Domain
    "func": "tooltip",  # for Python Sphinx Domain
    "meth": "tooltip",  # for Python Sphinx Domain
    "attr": "tooltip",  # for Python Sphinx Domain
    "exc": "tooltip",  # for Python Sphinx Domain
    "obj": "tooltip",  # for Python Sphinx Domain
    "ref": "tooltip",  # for hoverxref_auto_ref config
    "confval": "tooltip",  # for custom object
    "term": "tooltip",  # for glossaries
    "numref": "tooltip",
}
hoverxref_intersphinx = [
    "numpy",
    "pytest",
    "python",
    "readthedocs",
]

# Sphinx gallery configuration
sphinx_gallery_conf = {
    "examples_dirs": "../../examples",
    "gallery_dirs": "examples",
    "filename_pattern": "/.+\.py",
    "plot_gallery": False,
}

# Show short type hints for user-defined classes and defaults for parameters
python_use_unqualified_type_names = True
autodoc_typehints_format = "short"
typehints_defaults = "comma"
typehints_document_rtype = False
autodoc_default_options = {
    "undoc-members": False,
}

add_module_names = False

# Figure numbering
numfig = True

# True to convert the type definitions in the docstrings as references. Defaults to False.
napoleon_preprocess_types = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["locale/README.md", "_autoapi_templates"]

# -- Options for HTML output -------------------------------------------------

# Get the sphinx theme from the branch name
default_theme = "sphinx_rtd_theme"
html_themes = {
    "sphinx-rtd-theme": "sphinx_rtd_theme",
    "sphinx-book-theme": "sphinx_book_theme",
    "furo": "furo",
}
try:
    import git

    branch = git.repo.Repo("../../").active_branch.name
except Exception:
    branch = "2023"
    if os.environ.get("READTHEDOCS_VERSION_TYPE", None) == "branch":
        branch = os.environ.get("READTHEDOCS_VERSION_NAME", "2023")

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = os.environ.get("SPHINX_THEME", None) or html_themes.get(branch, default_theme)

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
if html_theme == "sphinx_book_theme":
    html_theme_options = {
        "repository_url": "https://github.com/haiiliin/abqpy",
        "use_source_button": True,
        "path_to_docs": "docs/source",
        "repository_branch": branch,
        "use_edit_page_button": True,
        "use_repository_button": True,
        "use_issues_button": True,
    }
elif html_theme == "sphinx_rtd_theme":
    html_theme_options = {}
    html_sidebars = {
        "*": ["versions.html"],
    }
elif html_theme == "furo":
    html_theme_options = {}

# Logo
# html_logo = "_static/3ds-dark.svg"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# -- Options for LaTeX output -------------------------------------------------

# If true, add page references after internal references. This is very useful
# for printed copies of the manual. Default is False.
latex_show_pagerefs = True

# Control whether to display URL addresses. This is very useful for printed
# copies of the manual. The setting can have the following values:
# 'no' - do not display URLs (default)
# 'footnote' - display URLs in footnotes
# 'inline' - display URLs inline in parentheses
latex_show_urls = "footnote"

# If given, this must be the name of an image file (relative to the
# configuration directory) that is the logo of the docs. It is placed at the
# top of the title page. Default: None.
latex_logo = None

# The “theme” that the LaTeX output should use. It is a collection of settings
# for LaTeX output (ex. document class, top level sectioning unit and so on).
# As a built-in LaTeX themes, manual and howto are bundled.
# manual
# A LaTeX theme for writing a manual. It imports the report document class
# (Japanese documents use jsbook).
# howto
# A LaTeX theme for writing an article. It imports the article document class
# (Japanese documents use jreport rather). latex_appendices is available only for this theme.
# It defaults to 'manual'.
latex_theme = "manual"

autoclass_content = "both"

latex_toplevel_sectioning = "part"
latex_engine = "xelatex"
latex_use_xindy = False
latex_elements = {
    "preamble": "\\usepackage[UTF8]{ctex}\n\\setcounter{tocdepth}{3}\n\\setcounter{secnumdepth}{5}",
    "printindex": "\\def\\twocolumn[#1]{#1}\\printindex",
}


# linkcode source
def linkcode_resolve(domain: str, info: dict[str, typing.Union[str, list[str]]]):
    """Resolve linkcode source

    Parameters
    ----------
    domain : str
        specifies the language domain the object is in
    info : dict[str, str | list[str]]
        a dictionary with the following keys guaranteed to be present (dependent on the domain)

        - py: module (name of the module), fullname (name of the object)
        - c: names (list of names for the object)
        - cpp: names (list of names for the object)
        - javascript: object (name of the object), fullname (name of the item)

    Returns
    -------
    source url of the object
    """
    if domain != "py":
        return None

    modname = info["module"]
    fullname = info["fullname"]

    filename = modname.replace(".", "/")
    baseurl = f"https://github.com/haiiliin/abqpy/blob/{major}/src/{filename}.py"

    submod = sys.modules.get(modname)
    if submod is None:
        return baseurl

    obj = submod
    for part in fullname.split("."):
        try:
            obj = getattr(obj, part)
        except Exception:
            return baseurl
    try:
        source, lineno = inspect.getsourcelines(obj)
    except TypeError:
        # Find source line for an attribute, the obj is None
        attr = fullname.split(".")[-1]
        obj = submod
        for part in fullname.split(".")[:-1]:
            try:
                obj = getattr(obj, part)
            except Exception:
                return baseurl
        source, lineno = inspect.getsourcelines(obj)
        attr_sources: list[str] = re.findall(rf"\n(    {attr}: [\w\W]+?)\n\n", "\n".join(source))
        if len(attr_sources) > 0:
            attr_source = attr_sources[0].splitlines()

            def find_line_number(string: str, text: list[str]):
                for line_number, line in enumerate(text):
                    if string in line:
                        return line_number

            index = find_line_number(attr_source[0], source)
            for row in range(index - 1, -1, -1):
                if source[row].startswith("    #: "):
                    attr_source.insert(0, source[row])
                else:
                    break
            lineno += find_line_number(attr_source[0], source)
            source = attr_source
    except Exception:
        return baseurl

    return baseurl + f"#L{lineno}-L{lineno + len(source) - 1}"


############################
# SETUP THE RTD LOWER-LEFT #
############################
html_context = dict(display_lower_left=True)

# GET REPO_NAME
REPO_NAME = os.environ.get("REPO_NAME", "abqpy")

# GET CURRENT_LANGUAGE
current_language = os.environ.get("LANGUAGE", "en")

# tell the theme which language to we're currently building
html_context["current_language"] = current_language

# GET CURRENT_VERSION
current_version = os.environ.get("VERSION", branch)

# tell the theme which version we're currently on ('current_version' affects
# the lower-left rtd menu and 'version' affects the logo-area version)
html_context["current_version"] = html_context["version"] = current_version

# POPULATE LINKS TO OTHER LANGUAGES
language_aliases = {
    "en": "English",
    "zh_CN": "简体中文",
}
html_context["languages"] = [(lang, f"/{REPO_NAME}/{lang}/{current_version}/", language_aliases.get(lang, lang))
                             for lang in ("en", "zh_CN")]  # fmt: skip

# POPULATE LINKS TO OTHER VERSIONS
branches = [str(v) for v in range(2023, 2015, -1)]
branches += ["latest", "sphinx-book-theme", "furo"]
html_context['versions'] = [(ver, f'/{REPO_NAME}/{current_language}/{ver}/', ver)
                            for ver in [branch for branch in branches]]  # fmt: skip

# POPULATE LINKS TO OTHER FORMATS/DOWNLOADS
html_context["downloads"] = [
    (
        fmt,
        f"/{REPO_NAME}/{current_language}/{current_version}/{project}-docs-{current_language}-{current_version}.{fmt}",
    )
    for fmt in ("pdf", "epub")
]
