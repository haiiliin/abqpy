import abqpy.abaqus
from abaqus.Odb.OdbCommands import *
from abaqus.UtilityAndView.BackwardCompatibility import BackwardCompatibility
from abaqus.Odb.OdbSequenceAnalyticSurfaceSegment import OdbSequenceAnalyticSurfaceSegment


def openOdb(path: str, readOnly: Boolean = OFF, readInternalSets: Boolean = OFF) -> Odb:
    """This method opens an existing output database (`.odb`) file and creates a new Odb object.
    You typically execute this method outside of Abaqus/CAE when, in most cases, only one
    output database is open at any time. For example::
    
        import odbAccess
        shockLoadOdb = odbAccess.openOdb(path='myOdb.odb')

    Parameters
    ----------
    path
        A String specifying the path to an existing output database (`.odb`) file.
    readOnly
        A Boolean specifying whether the file will permit only read access or both read and
        write access. The initial value is `False`, indicating that both read and write access
        will be permitted.
    readInternalSets
        A Boolean specifying whether the file will permit access to sets specified as Internal
        on the database. The initial value is `False`, indicating that internal sets will not be
        read.

    Returns
    -------
    Odb
        An :py:class:`~abaqus.Odb.Odb.Odb` object.

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
    abqpy.abaqus.run(cae=False)
    return Odb(path)


def AnalyticSurfaceProfile() -> OdbSequenceAnalyticSurfaceSegment:
    """This method creates a OdbSequenceAnalyticSurfaceSegment object.
    
    Returns
    -------
    OdbSequenceAnalyticSurfaceSegment
        An :py:class:`~abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment` object.
    """
    return OdbSequenceAnalyticSurfaceSegment()


backwardCompatibility = BackwardCompatibility()
