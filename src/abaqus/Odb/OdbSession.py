from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Odb import Odb
from .ScratchOdb import ScratchOdb
from ..Session.SessionBase import SessionBase


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
            An :py:class:`~abaqus.Odb.Odb.Odb` object specifying the output database with which to associate.

        Returns
        -------
        ScratchOdb
            A :py:class:`~abaqus.Odb.ScratchOdb.ScratchOdb` object.
        """
        self.scratchOdbs["odb"] = scratchOdb = ScratchOdb(odb)
        return scratchOdb
