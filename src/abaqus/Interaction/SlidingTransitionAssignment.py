from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class SlidingTransitionAssignment:
    """The SlidingTransitionAssignment object stores the sliding transition assignment
    definition for surfaces in ContactStd objects. The SlidingTransitionAssignment object
    has no constructor or members.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name].slidingTransitionAssignments

        The corresponding analysis keywords are:

        - CONTACT FORMULATION
    """

    @abaqus_method_doc
    def changeValuesInStep(self, stepName: str, index: int, value: SymbolicConstant):
        """This method allows you to modify sliding transition assignments already defined on
        surface pairs in a given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the sliding transition assignments are
            to be modified.
        index
            An Int specifying the position of the sliding transition assignment whose value is to be
            modified.
        value
            A SymbolicConstant specifying the value of the smoothness of the surface-to-surface
            formulation on sliding to be assigned to the surface whose index is referenced. Possible
            values are ELEMENT_ORDER_SMOOTHING, LINEAR_SMOOTHING, and QUADRATIC_SMOOTHING.
        """
        ...

    @abaqus_method_doc
    def appendInStep(self, stepName: str, assignments: SymbolicConstant):
        """This method allows you to add sliding transition assignments to new surface pairs in a
        given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the sliding transition assignments are
            to be defined.
        assignments
            A sequence of tuples specifying the sliding transition assignments. Each tuple contains
            two entries:A region object or the SymbolicConstant GLOBAL specifying the surface to
            which the sliding transition attribute is assigned.A SymbolicConstant specifying the
            overriding the smoothness value to be used for the first surface. Possible values of the
            SymbolicConstant are ELEMENT_ORDER_SMOOTHING, LINEAR_SMOOTHING, and QUADRATIC_SMOOTHING.
        """
        ...

    @abaqus_method_doc
    def delete(self, indices: tuple):
        """The delete method allows you to delete existing sliding transition assignments.

        Parameters
        ----------
        indices
            A sequence of Ints specifying the index of each sliding transition assignment to delete.
        """
        ...
