from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class MeshEditOptions:
    """The MeshEditOptions object stores settings that specify the behavior when editing meshes
    on parts or part instances.
    The MeshEditOptions object has no constructor. Abaqus creates the **MeshEditOptions**
    member when a session is started.

    .. note::
        This object can be accessed by::

            mdb.meshEditOptions
    """

    @abaqus_method_doc
    def setValues(
        self,
        maxUndoCacheElements: float = 0,
        enableUndo: Boolean = OFF,
        _suspendUndo: Boolean = OFF,
    ):
        """This method modifies the MeshEditOptions object.

        Parameters
        ----------
        maxUndoCacheElements
            A Float specifying the maximum allowable mesh edit undo cache size in millions of
            elements. If this value is set to at least the number of elements on a given part or
            part instance, at least one level of undo/redo capability is assured for subsequent mesh
            edit operations on that part or part instance. The default value is 0.0.
        enableUndo
            A Boolean specifying whether undo/redo of mesh edit operations will be enabled. If
            **enableUndo** =OFF any existing cache for undo/redo operations will be cleared for all
            parts and assemblies in all models. The default value is OFF.
        _suspendUndo
            A Boolean specifying the suspension of undo/redo for mesh edit operations. When
            undo/redo is suspended, undo/redo will not be available after subsequent mesh edit
            operations on a given part or part instances. Any pre-existing cache for mesh edit
            operations on other parts or assemblies in any model will be unaffected. The default
            value is OFF.If you change the value of **enableUndo** to True, Abaqus sets **_suspendUndo**
            to False.
        """
        ...
