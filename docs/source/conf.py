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

import git
import pkg_resources

project = 'abqpy'
copyright = '2022, WANG Hailin'
author = 'WANG Hailin'

# The full version, including alpha/beta/rc tags
_default_version = '2023.0.0-dev'
try:
    version = pkg_resources.get_distribution('abqpy').version[:4]
    if not version.startswith('20'):
        version = _default_version[:4]
except pkg_resources.DistributionNotFound:
    version = _default_version[:4]
release = version

# For multiple languages
locale_dirs = ['locales/']   # path is example but recommended.
gettext_compact = False     # optional.

# -- General configuration ---------------------------------------------------

# Add source code
sys.path.insert(0, os.path.abspath('../../src'))
os.environ['ABQPY_MAKE_DOCS'] = 'true'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_toolbox.more_autodoc.overloads',
    'autoclasstoc',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.linkcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx_copybutton',
    'sphinx_autodoc_typehints',
    'sphinx_codeautolink',
    'sphinx_toolbox.confval',
    'hoverxref.extension',
]

# Default behavior for code block concatenation for sphinx_codeautolink
codeautolink_concat_default = False

# Suppress warnings
suppress_warnings = [
    'app.add_directive',
]

intersphinx_mapping = {
    'numpy': ('https://numpy.org/doc/stable/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'pytest': ('https://pytest.org/en/stable/', None),
    'python': ('https://docs.python.org/3/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'jinjia2': ('https://jinja.palletsprojects.com/en/3.0.x/', None),
}

# Hoverxref configuration
hoverxref_auto_ref = True
hoverxref_domains = ["py"]
hoverxref_roles = [
    'numref',
    'confval',
    'setting',
    "option",
    "doc",  # Documentation pages
    "term",  # Glossary terms
]
hoverxref_role_types = {
    "mod": "modal",  # for Python Sphinx Domain
    "doc": "modal",  # for whole docs
    "class": "tooltip",  # for Python Sphinx Domain
    "ref": "tooltip",  # for hoverxref_auto_ref config
    "confval": "tooltip",  # for custom object
    "term": "tooltip",  # for glossaries
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
    if domain != 'py':
        return None

    modname = info['module']
    fullname = info['fullname']

    filename = modname.replace('.', '/')
    try:
        branch_name = git.repo.Repo('../../').active_branch.name
    except Exception:
        branch_name = version[:4]
    baseurl = f'https://github.com/haiiliin/abqpy/blob/{branch_name}/src/{filename}.py'

    submod = sys.modules.get(modname)
    if submod is None:
        return baseurl

    obj = submod
    for part in fullname.split('.'):
        try:
            obj = getattr(obj, part)
        except Exception:
            return baseurl
    try:
        source, lineno = inspect.getsourcelines(obj)
    except TypeError:
        # Find source line for an attribute, the obj is None
        attr = fullname.split('.')[-1]
        obj = submod
        for part in fullname.split('.')[:-1]:
            try:
                obj = getattr(obj, part)
            except Exception:
                return baseurl
        source, lineno = inspect.getsourcelines(obj)
        attr_sources: list[str] = re.findall(rf'\n(    {attr}: [\w\W]+?)\n\n', '\n'.join(source))
        if len(attr_sources) > 0:
            attr_source = attr_sources[0].splitlines()

            def find_line_number(string: str, text: list[str]):
                for line_number, line in enumerate(text):
                    if string in line:
                        return line_number

            index = find_line_number(attr_source[0], source)
            for row in range(index - 1, -1, -1):
                if source[row].startswith('    #: '):
                    attr_source.insert(0, source[row])
                else:
                    break
            lineno += find_line_number(attr_source[0], source)
            source = attr_source
    except Exception:
        return baseurl

    return baseurl + f'#L{lineno}-L{lineno + len(source) - 1}'


# Show short type hints for user-defined classes and defaults for parameters
python_use_unqualified_type_names = True
autodoc_typehints_format = 'short'
typehints_defaults = 'comma'
typehints_document_rtype = False

autodoc_default_options = {
    'undoc-members': False,
}

add_module_names = False

# Figure numbering
numfig = True

# True to convert the type definitions in the docstrings as references. Defaults to False.
napoleon_preprocess_types = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'pydata_sphinx_theme'

# Logo
# html_logo = "_static/3ds-dark.svg"

html_sidebars = {
    "**": ["search-field.html", "sidebar-nav-bs.html"]
}

html_theme_options = {
    'navigation_depth': 9,
    "github_url": "https://github.com/haiiliin/abqpy",
    "icon_links": [
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/abqpy",
            "icon": "_static/PyPI_logo.svg",
            "type": "local",
        },
        {
            "name": "Anaconda",
            "url": "https://anaconda.org/haiiliin/abqpy",
            "icon": "_static/anaconda.svg",
            "type": "local",
        },
        {
            "name": "Read the Docs",
            "url": "https://readthedocs.org/projects/abqpy/",
            "icon": "_static/rtd-logo-dark.svg",
            "type": "local",
        },
   ],
    "switcher": {
        "json_url": "https://docs.abqpy.com/_static/versions.json",
        "version_match": version,
    },
    "navbar_end": ["version-switcher", "theme-switcher", "navbar-icon-links"],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for LaTeX output -------------------------------------------------

# If true, add page references after internal references. This is very useful
# for printed copies of the manual. Default is False.
latex_show_pagerefs = True

# Control whether to display URL addresses. This is very useful for printed
# copies of the manual. The setting can have the following values:
# 'no' - do not display URLs (default)
# 'footnote' - display URLs in footnotes
# 'inline' - display URLs inline in parentheses
latex_show_urls = 'footnote'

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
latex_theme = 'manual'

# autoclass_content = 'both'

latex_toplevel_sectioning = 'part'
latex_engine = 'xelatex'
latex_use_xindy = False
latex_elements = {
    'preamble': '\\usepackage[UTF8]{ctex}\n\\setcounter{tocdepth}{3}\n\\setcounter{secnumdepth}{5}',
    'printindex': '\\def\\twocolumn[#1]{#1}\\printindex',
}
