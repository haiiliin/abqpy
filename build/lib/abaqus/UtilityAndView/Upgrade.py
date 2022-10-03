from abqpy.decorators import abaqus_function_doc
from ..UtilityAndView.abaqusConstants import BOTH, Boolean, EARLIEST, LATEST, SymbolicConstant

"""The upgradeScript module allows you to upgrade scripts from one release of Abaqus to a 
later release. The upgradeScript module allows you to upgrade over several releases at 
one time. It also allows you to upgrade only kernel commands, only GUI commands, or 
both. 

.. note:: 
    This object can be accessed by::

        import upgradeScript

"""


@abaqus_function_doc
def upgradeScript(
    fileNames: str,
    searchSubdirectories: Boolean = True,
    backup: Boolean = True,
    preview: Boolean = True,
    diffExecutable: str = False,
    logFileName: str = "asiUpgrade",
    fromVersion: str = EARLIEST,
    toVersion: str = LATEST,
    scriptType: SymbolicConstant = BOTH,
):
    """This function can be used to upgrade a directory, a file, or a list of both directories
    and files. You can preview the changes before you choose to upgrade the file. A user
    interface to this function is available via the Plug-ins menu. For more information, see
    Upgrading a script. You can also use a simpler interface from the command line to
    upgrade scripts. For more information, see the summary of changed commands at the end of
    this guide.

    .. note:: 
        This function can be accessed by::

            upgradeScript.upgradeScript

    Parameters
    ----------
    fileNames
        A String or sequence of Strings specifying the files or directories to upgrade. If a
        directory path is found, it will be searched for files with the suffix .py or .guiLog.
        If **searchSubdirectories** is True, any directories found within a directory will also be
        searched.
    searchSubdirectories
        A Boolean specifying whether to search any subdirectories (if the file name is a
        directory). If **searchSubdirectories** is True, the command will search the
        subdirectories of any directory in **fileNames**. If **searchSubdirectories** is False, the
        command will search the directory but not the subdirectories. The default value is True.
    backup
        A Boolean specifying whether to make backups of the files. The default value is True.
        This argument is ignored if **preview** is set.
    preview
        A Boolean specifying whether to preview the changes to the file instead of changing the
        file. If **preview** is True, display a preview of the file changes. The default value is
        True.By default, the preview is displayed in a web browser. The **diffExecutable**
        argument allows you to specify a different application in which to preview the changes.
    diffExecutable
        A String specifying the application used to display the differences between the script
        and the upgraded script. The default value is an empty string, and the differences are
        displayed by a web browser. Examples of values for **diffExecutable** are winmerge and
        diff. This argument is ignored if **preview** is False.
    logFileName
        A String specifying the name of the log file where any warnings and changes found during
        the upgrade are written. The default value is asiUpgrade.log.
    fromVersion
        A String specifying the Abaqus release from which to upgrade. The default value is
        EARLIEST.
    toVersion
        A String specifying the Abaqus release to which to upgrade. The default value is LATEST.
    scriptType
        A SymbolicConstant specifying the type of scripting commands to be upgraded. Possible
        values are KERNEL, GUI, or BOTH. If **scriptType** is KERNEL only Abaqus Scripting
        Interface commands will be upgraded; if **scriptType** is GUI only Abaqus GUI Toolkit
        commands will be upgraded. The default value is BOTH.

    Returns
    -------
    int
        The number of changes made or, if **preview** was used, the number of changes that would
        have been made.
    """
    ...
