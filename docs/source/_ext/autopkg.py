import functools
from importlib import metadata

from docutils import nodes
from sphinx.application import Sphinx


def version_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    """Role for version numbers.
    
    Parameters
    ----------
    name : str
        The local name of the interpreted role, the role name actually used in the document.
    rawtext : str
        A string containing the entire interpreted text input, including the role and markup. 
        Return it as a problematic node linked to a system message if a problem is encountered.
    text : str
        The interpreted text content.
    lineno : int
        The line number where the text block containing the interpreted text begins.
    inliner : `docutils.parsers.rst.states.Inliner`
        The docutils.parsers.rst.states.Inliner object that called role_fn. It contains the 
        several attributes useful for error reporting and document tree access.
    options : dict
        A dictionary of directive options for customization (from the "role" directive), to 
        be interpreted by the role function. Used for additional attributes for the generated elements and other functionality.
    content : list
        A list of strings, the directive content for customization (from the "role" directive). 
        To be interpreted by the role function.
        
    Returns
    -------
    list[Node]
        A list of nodes which will be inserted into the document tree at the point where the 
        interpreted role was encountered (can be an empty list).
    list[str]
        A list of system messages, which will be inserted into the document tree immediately 
        after the end of the current block (can also be empty).
    """
    version = '.'.join(metadata.version(text).split('.')[:3])
    node = nodes.Text(f"{text}=={version}", f"{text}=={version}")
    return [node], []
    

def setup(app: Sphinx):
    app.add_role('autopkg', version_role)
    return {'version': '0.0.1', 'parallel_read_safe': True}
