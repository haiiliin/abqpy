from abqpy.decorators import abaqus_function_doc

from ..UtilityAndView.abaqusConstants import Boolean

"""The Python module redentABQ is a wrapper around the Python redent module. The module 
makes the indentation in a Python text file consistent. 
The module can be run as a script from a command prompt using the following statement: 
abaqus Python -m redentABQ [options] pathToFile 
where the following options are available to customize the redentABQ process: 
- `-b`: Create a backup of the selected file if any modifications are made. 
- `-i`: Specify a number of spaces to be used for indentation. 
- `-t`: Test the newly indented file after any changes are made. 
For more information on running the **abaqus Python** execution procedure, see Python 
execution. 

.. note::

    Theses functions can be accessed by::

        import redentABQ

"""


@abaqus_function_doc
def indentFile(path: str, indent: str = "", backup: Boolean = False, runTest: Boolean = False):
    """This method outputs the indented file to the terminal window or backs up the specified file and replaces
    it.

    Parameters
    ----------
    path
        A String specifying the file to be processed.
    indent
        A String specifying the amount of indentation to be used. The default value is four
        spaces of indentation. Custom indentation strings must be flanked by quotation marks ("
        ").
    backup
        A Boolean specifying whether to back up the file specified in the **path** argument if
        changes are made. The default value is False.
    runTest
        A Boolean specifying whether to test the newly indented file to ensure that it is
        semantically the same after any changes. The default value is False.

    Returns
    -------
    Boolean
        A Boolean. True, if the indentation is successful; otherwise, False.
    """
    ...
