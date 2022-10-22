from typing_extensions import Literal
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class SlidingFormulationAssignment:
    """The SlidingFormulationAssignment object stores the sliding formulation assignment
    definition for surfaces in ContactStd objects. The SlidingFormulationAssignment object
    has no constructor or members.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name].slidingFormulationAssignments

        The corresponding analysis keywords are:

        - CONTACT FORMULATION

    .. versionadded:: 2021
        The `SlidingFormulationAssignment` class was added.
    """

    @abaqus_method_doc
    def changeValuesInStep(self, stepName: str, index: int, value: Literal[C.SMALL_SLIDING, C.NONE]):
        """This method allows you to modify sliding formulation assignments already defined on
        surface pairs in a given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the sliding formulation assignments
            are to be modified.
        index
            An Int specifying the position of the sliding formulation assignment whose value is to
            be modified.
        value
            A SymbolicConstant specifying the value of the smoothness of the surface-to-surface
            formulation on sliding to be assigned to the surface whose index is referenced. Possible
            values are NONE and SMALL_SLIDING.
        """
        ...

    @abaqus_method_doc
    def appendInStep(self, stepName: str, assignments: Literal[C.SMALL_SLIDING, C.NONE, C.GLOBAL]):
        """This method allows you to add sliding formulation assignments to new surface pairs in a
        given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the sliding formulation assignments
            are to be defined.
        assignments
            A sequence of tuples specifying the sliding formulation assignments. Each tuple contains
            two entries:A region object or the SymbolicConstant GLOBAL specifying the surface to
            which the sliding formulation attribute is assigned.A SymbolicConstant specifying the
            overriding the smoothness value to be used for the first surface. Possible values of the
            SymbolicConstant are NONE and SMALL_SLIDING.
        """
        ...

    @abaqus_method_doc
    def delete(self, indices: tuple):
        """The delete method allows you to delete existing sliding formulation assignments.

        Parameters
        ----------
        indices
            A sequence of Ints specifying the index of each sliding formulation assignment to
            delete.
        """
        ...
