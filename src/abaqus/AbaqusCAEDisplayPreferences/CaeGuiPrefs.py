from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import Boolean


@abaqus_class_doc
class CaeGuiPrefs:
    """The CaeGuiPrefs object contains the details of the graphical preferences in a
    guiPreferences section of the abaqus_2021.gpr file.

    .. note:: 
        This object can be accessed by::

            import caePrefsAccess
            caePrefsAccess.openGuiPreferences(...)
    """

    #: A String specifying the path to the preferences file.
    fileName:str = ""

    @abaqus_method_doc
    def save(self, backupFile: Boolean = True):
        """This method saves the guiPreferences section specified in the current **fileName**.

        Parameters
        ----------
        backupFile: Boolean
            A Boolean specifying whether Abaqus should save a numbered backup copy of the
            preferences file, **fileName**. Default is True.
        """
        # TODO: Implement this method
        ...

    @abaqus_method_doc
    def saveAs(self, fileName: str):
        """This method saves the guiPreferences settings to the specified location.

        Parameters
        ----------
        fileName: str
            A String specifying the path to the preferences file.
        """
        # TODO: Implement this method
        ...
