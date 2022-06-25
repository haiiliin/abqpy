from .Odb import Odb
from .ScratchOdb import ScratchOdb
from ..Session.SessionBase import SessionBase


class OdbSession(SessionBase):
    def ScratchOdb(self, odb: Odb) -> ScratchOdb:
        """This method creates a new ScratchOdb object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                session.ScratchOdb

        Parameters
        ----------
        odb
            An :py:class:`~abaqus.Odb.Odb.Odb` object specifying the output database with which to associate.

        Returns
        -------
        ScratchOdb
            A :py:class:`~abaqus.Odb.ScratchOdb.ScratchOdb` object.
        """
        self.scratchOdbs["odb"] = scratchOdb = ScratchOdb(odb)
        return scratchOdb
