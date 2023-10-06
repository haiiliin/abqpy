from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Session.SessionBase import SessionBase
from .Odb import Odb
from .ScratchOdb import ScratchOdb
from ..UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class OdbSession(SessionBase):
    @abaqus_method_doc
    def ScratchOdb(self, odb: Odb) -> ScratchOdb:
        """This method creates a new ScratchOdb object.

        .. note::
            This function can be accessed by::

                session.ScratchOdb

        Parameters
        ----------
        odb
            An Odb object specifying the output database with which to associate.

        Returns
        -------
        ScratchOdb
            A ScratchOdb object.
        """
        self.scratchOdbs["odb"] = scratchOdb = ScratchOdb(odb)
        return scratchOdb

    # The following method was originally in the ``OdbCommands`` page documentation
    # But it accessed only by ``session`` object.
    @abaqus_method_doc
    def openOdb(self, name: str, path: str = "", readOnly: Boolean = OFF) -> Odb:
        """This method opens an existing output database (`.odb`) file and creates a new Odb object. This method
        is accessed only via the session object inside Abaqus/CAE and adds the new Odb object to the
        session.odbs repository. This method allows you to open multiple output databases at the same time and
        to use the repository key to specify a particular output database. For example::

            import visualization
            session.openOdb(name='myOdb', path='stress.odb', readOnly=True)

        Parameters
        ----------
        name
            A String specifying the repository key. If the ``name`` is not the same as the ``path`` to the
            output database (`.odb`) file, the ``path`` must be specified as well. Additionally, to
            support backwards compatibility of the interface, if the ``name`` parameter is omitted,
            the ``path`` and ``name`` will be presumed to be the same.
        path
            A String specifying the path to an existing output database (`.odb`) file.
        readOnly
            A Boolean specifying whether the file will permit only read access or both read and
            write access. The initial value is TRUE when the output database file is opened from
            Abaqus/CAE, indicating that only read access will be permitted.

        Returns
        -------
        Odb
            An Odb object.

        Raises
        ------
        OdbError
            The database is from a previous release of Abaqus, If the output database was generated by a previous release of Abaqus and needs
            upgrading, Run  `abaqus upgrade -job <newFilename> -odb <oldFileName>` to upgrade it.
        OdbError
            Abaqus installation must be upgraded before this output database can be opened, If the output database was generated by a newer release of Abaqus, and the
            installation of Abaqus needs upgrading.
        AbaqusError: Cannot open file <filename>
            If the file is not a valid database.
        """
        self.odbs[name] = odb = Odb(name)
        return odb

    @abaqus_method_doc
    def upgradeOdb(self, existingOdbPath: str, upgradedOdbPath: str):
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
