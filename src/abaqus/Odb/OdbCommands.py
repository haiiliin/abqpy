from typing import Sequence, Tuple

from abqpy.decorators import abaqus_function_doc

from ..UtilityAndView.abaqusConstants import OFF, Boolean
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .FieldOutput import FieldOutput
from .Odb import Odb
from .OdbSequenceAnalyticSurfaceSegment import OdbSequenceAnalyticSurfaceSegment

"""The Odb commands do the following: 

- Determine if an output database (.odb) file needs to be upgraded to the current 
  release. 
- Determine the extreme value for an output variable over a number of fields; for 
  example, over a number of load cases. 
- Open an existing output database file and create a new Odb object. 
- Upgrade an output database file to the current release and write the upgraded output 
  database to a new file. 
"""


@abaqus_function_doc
def isUpgradeRequiredForOdb(upgradeRequiredOdbPath: str):
    """This method determines if an output database file needs to be upgraded to the current release. You can
    access this method using either of the following techniques:

    - From a script running outside Abaqus/CAE. For example::

        import odbAccess
        needsUpgrade = odbAccess.isUpgradeRequiredForOdb(
            upgradeRequiredOdbPath='myOdb.odb')

    - From the Visualization module in Abaqus/CAE. For example::

        import visualization
        needsUpgrade = session.isUpgradeRequiredForOdb(upgradeRequiredOdbPath='myOdb.odb')

    Parameters
    ----------
    upgradeRequiredOdbPath
        An String specifying the path to an output database file to test. The test determines if
        the output database needs to be upgraded to the current release.

    Returns
    -------
    Boolean
        A Boolean indicating the result of the test. A value of True indicates that the output
        database needs to be upgraded to the current release.
    """
    ...


@abaqus_function_doc
def maxEnvelope() -> Sequence[Tuple[FieldOutput, FieldOutput]]:
    """Retrieve the maximum value of an output variable over a number of fields.

    Returns
    -------
    Sequence[FieldOutput]
        A sequence of two fieldOutput objects. The first fieldOutput object contains the maximum
        value. The second fieldOutput object contains the index of the field containing the
        maximum value. The index follows the order in which fields are positioned in the list of
        fieldOutput objects provided as the argument to the function.

    Raises
    ------
    OdbError
    TypeError
        This function takes no keyword arguments.
    """
    return ((FieldOutput("", "", C.SCALAR), FieldOutput("", "", C.SCALAR)),)


@abaqus_function_doc
def minEnvelope() -> Sequence[Tuple[FieldOutput, FieldOutput]]:
    """Retrieve the minimum value of an output variable over a number of fields.

    Returns
    -------
    Sequence[tuple[FieldOutput, FieldOutput]]
        A sequence of two fieldOutput objects. The first fieldOutput object contains the minimum
        value. The second fieldOutput object contains the index of the field containing the
        minimum value. The index follows the order in which fields are positioned in the list of
        fieldOutput objects provided as the argument to the function.

    Raises
    ------
    OdbError
    TypeError
        This function takes no keyword arguments.
    """
    return ((FieldOutput("", "", C.SCALAR), FieldOutput("", "", C.SCALAR)),)


@abaqus_function_doc
def openOdb(path: str, readOnly: Boolean = OFF, readInternalSets: Boolean = OFF) -> Odb:
    """This method opens an existing output database (`.odb`) file and creates a new Odb object. You typically
    execute this method outside of Abaqus/CAE when, in most cases, only one output database is open at any time.
    For example::

        import odbAccess
        shockLoadOdb = odbAccess.openOdb(path='myOdb.odb')

    Parameters
    ----------
    path
        A String specifying the path to an existing output database (`.odb`) file.
    readOnly
        A Boolean specifying whether the file will permit only read access or both read and
        write access. The initial value is ``False``, indicating that both read and write access
        will be permitted.
    readInternalSets
        A Boolean specifying whether the file will permit access to sets specified as Internal
        on the database. The initial value is ``False``, indicating that internal sets will not be
        read.

    Returns
    -------
    Odb
        An Odb object.

    Raises
    ------
    OdbError: The database is from a previous release of Abaqus.
        If the output database was generated by a previous release of Abaqus and needs
        upgrading. Run `abaqus upgrade -job <newFilename> -odb <oldFileName>` to upgrade it.
    OdbError: Abaqus installation must be upgraded before this output database can be
    opened.
        If the output database was generated by a newer release of Abaqus, and the
        installation of Abaqus needs upgrading.
    """
    return Odb(path)


@abaqus_function_doc
def upgradeOdb(existingOdbPath: str, upgradedOdbPath: str):
    """This method upgrades an existing Odb object to the current release and writes the upgraded version of the
    Odb object to a file. In addition, Abaqus/CAE writes information about the status of the upgrade to a log
    (.log) file. You can access this method using either of the following techniques:

    - From a script running outside Abaqus/CAE. For example::

        import odbAccess
        odbAccess.upgradeOdb(existingOdbPath='oldOdb', upgradedOdbPath='upgradedOdb')

    - From the session object in Abaqus/CAE. For example::

        import visualization
        session.upgradeOdb(existingOdbPath='oldOdb', upgradedOdbPath='upgradedOdb')

    Parameters
    ----------
    existingOdbPath
        An String specifying the path to the file containing the output database to be upgraded.
    upgradedOdbPath
        An String specifying the path to the file that will contain the upgraded output
        database.

    Raises
    ------
    OdbError: cannot convert database
        If the output database upgrade fails.
    """
    ...


# The following method was originally in the ``OdbSequenceAnalyticSurfaceSegment`` page documentation
# But it accessed only in ``odbAccess`` module, which is importing `abaqus.Odb.OdbCommands`
def AnalyticSurfaceProfile() -> OdbSequenceAnalyticSurfaceSegment:
    """This method creates a OdbSequenceAnalyticSurfaceSegment object.

    Path::

        odbAccess.AnalyticSurfaceProfile()

    Returns
    -------
    OdbSequenceAnalyticSurfaceSegment
        An OdbSequenceAnalyticSurfaceSegment object.
    """
    return OdbSequenceAnalyticSurfaceSegment()
