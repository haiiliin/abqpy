from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Odb import Odb


@abaqus_class_doc
class ScratchOdb:
    """A scratch output database is associated with an open output database and is used to
    store session-related, non-persistent objects, such as Step, Frame and FieldOutput
    objects. Abaqus creates a scratch output database when needed for these non-persistent
    objects during an Abaqus/CAE session. Abaqus deletes the scratch output database when
    the associated output database is closed.

    .. note:: 
        This object can be accessed by::

            import odbAccess
            session.scratchOdbs[name]
    """

    @abaqus_method_doc
    def __init__(self, odb: Odb):
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
        ...
