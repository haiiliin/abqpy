from typing import Union

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class SurfaceCrushTriggerAssignment:
    """The SurfaceCrushTriggerAssignment object stores the surface crush trigger assignment
    definition for surfaces in ContactExp objects. The SurfaceCrushTriggerAssignment object
    has no constructor or members.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name].surfaceCrushTriggerAssignments

        The corresponding analysis keywords are:

        - SURFACE PROPERTY ASSIGNMENT

    .. versionadded:: 2021
        The `SurfaceCrushTriggerAssignment` class was added.
    """

    @abaqus_method_doc
    def changeValuesInStep(
        self, stepName: str, index: int, value: Union[SymbolicConstant, float]
    ):
        """This method allows modification of surface crush trigger assignments already defined on
        surfaces in a given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the surface crush trigger assignments
            are to be modified.
        index
            An Int specifying the position of the surface crush trigger assignment whose value is to
            be modified.
        value
            A tuple specifying the value of the surface crush trigger assignments for the surface
            whose index is referenced. Each tuple contains three entries:
            - A SymbolicConstant specifying the trigger option to be used for the surface. Possible
            values of the SymbolicConstant are TRIGGER, NO_TRIGGER, or NO_CRUSH.
            - A Float specifying the crush stress value to be used for the surface.
            - A Float specifying the crush initiation angle value to be used for the surface.
            - A Float specifying the crush continuation angle value to be used for the surface.
        """
        ...

    @abaqus_method_doc
    def appendInStep(
        self, stepName: str, assignments: Union[SymbolicConstant, float]
    ):
        """This method allows addition of surface crush trigger assignments to new surfaces in a
        given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which new surface crush trigger assignments
            are to be defined.
        assignments
            A sequence of tuples specifying the surface crush trigger assignments. Each tuple
            contains four entries:
            - A region or a material object or the SymbolicConstant GLOBAL specifying the surface to
            which the feature angle is assigned.
            - A SymbolicConstant specifying the trigger option to be used for the surface. Possible
            values of the SymbolicConstant are TRIGGER, NO_TRIGGER, or NO_CRUSH.
            - A Float specifying the crush stress value to be used for the surface.
            - A Float specifying the crush initiation angle value to be used for the surface.
            - A Float specifying the crush continuation angle value to be used for the surface.
        """
        ...

    @abaqus_method_doc
    def delete(self, indices: tuple):
        """The delete method allows you to delete existing surface crush trigger assignments from a
        ContactExp object.

        Parameters
        ----------
        indices
            A sequence of Ints specifying the index of each surface crush trigger assignment to
            delete.
        """
        ...
