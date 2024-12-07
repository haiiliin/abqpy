from __future__ import annotations

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .InteractionProperty import InteractionProperty


@abaqus_class_doc
class WearSurfacePropertyAssignment(InteractionProperty):
    """The WearSurfacePropertyAssignment object stores the wear surface property assignment definition for domain
    pairs in ContactExp and ContactStd objects. The WearSurfacePropertyAssignment object has no constructor or
    members.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name].wearSurfacePropertyAssignments

    .. versionadded:: 2025
        The ``WearSurfacePropertyAssignment`` class was added.
    """

    @abaqus_method_doc
    def changeValuesInStep(
        self,
        stepName: str,
        index: int,
        value: str,
    ):
        """This method allows modification of contact property assignments to domain pairs already defined in a given
        step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the contact property assignments are to be modified.
        index
            An Int specifying the position of the contact property assignment whose value is to be modified.
        value
            A String specifying the value of the wear surface property to be assigned to the domain pair whose index is referenced.
        """
        super().__init__()
