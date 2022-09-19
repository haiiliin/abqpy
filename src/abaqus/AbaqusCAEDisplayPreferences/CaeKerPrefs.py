import typing

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class CaeKerPrefs:
    """The CaeKerPrefs object contains the details of the sessionOptions.

    .. note:: 
        This object can be accessed by::

            import caePrefsAccess
            caePrefsAccess.openSessionOptions(...)
    """

    #: A String specifying the path to the preferences file that the CaeKerPrefs object
    #: represents.
    fileName: str = ""

    @abaqus_method_doc
    def save(self, backupFile: Boolean = OFF):
        """This method saves the sessionOptions in the current **fileName**.

        Parameters
        ----------
        backupFile: Boolean
            A Boolean specifying whether save a numbered backup copy of the preferences file,
            **fileName**. Default is True.
        """
        # TODO: Implement this method
        ...
    
    @abaqus_method_doc
    def saveAs(self, fileName: str = '', directory: typing.Literal[CURRENT, HOME] = HOME):
        """This method saves the sessionOptions to the specified location.

        Parameters
        ----------
        fileName: str
            A String specifying the path to the preferences file.
        directory: SymbolicConstant
            A SymbolicConstant specifying the location of the preferences file. Possible values
            are:

            - CURRENT to open the preferences file in the current directory 
              (caePrefsAccess.CURRENT)
            - HOME to open the preferences file in your home directory 
              (caePrefsAccess.HOME)
            
            The default value is HOME. Either **fileName** or **directory** must be
            supplied. The **fileName** or **directory** arguments are mutually exclusive.
        """
        # TODO: Implement this method
        ...
