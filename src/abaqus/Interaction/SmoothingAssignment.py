from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class SmoothingAssignment:
    """The SmoothingAssignment object stores the surface smoothing assignment definition for
    surfaces in ContactExp and ContactStd objects. The SmoothingAssignment object has no
    constructor or members.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name].smoothingAssignments

        The corresponding analysis keywords are:

        - SURFACE PROPERTY ASSIGNMENT
    """

    @abaqus_method_doc
    def changeValuesInStep(
        self, stepName: str, index: int, value: Literal[C.TOROIDAL, C.SPHERICAL, C.REVOLUTION, C.NONE]
    ):
        """This method allows modification of surface smoothing assignments already defined on
        surfaces in a given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the surface smoothing assignments are
            to be modified.
        index
            An Int specifying the position of the surface smoothing assignment whose value is to be
            modified.
        value
            A tuple specifying the value of the surface smoothing assignments for the surface whose
            index is referenced. Each tuple contains one entry:A SymbolicConstant specifying the
            surface smoothing value to be used for the surface. Possible values of the
            SymbolicConstant are NONE, REVOLUTION, SPHERICAL, and TOROIDAL.
        """
        ...

    @abaqus_method_doc
    def appendInStep(self, stepName: str, assignments: Literal[C.TOROIDAL, C.SPHERICAL, C.REVOLUTION, C.NONE]):
        """This method allows addition of surface smoothing assignments to new surfaces in a given
        step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which new surface smoothing assignments are
            to be defined.
        assignments
            A sequence of tuples specifying the surface smoothing assignments. Each tuple contains
            two entries:

            - A region object specifying the surface to which the smoothing is assigned.
            - A SymbolicConstant specifying the surface smoothing value to be used for the surface.
              Possible values of the SymbolicConstant are NONE, REVOLUTION, SPHERICAL, and TOROIDAL.
        """
        ...

    @abaqus_method_doc
    def delete(self, indices: tuple):
        """The delete method allows you to delete existing surface smoothing assignments from
        ContactExp and ContactStd objects.

        Parameters
        ----------
        indices
            A sequence of Ints specifying the index of each surface smoothing assignment to delete.
        """
        ...
