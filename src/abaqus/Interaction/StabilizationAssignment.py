from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class StabilizationAssignment:
    """The StabilizationAssignment object stores the contact stabilization assignment
    definition for domain pairs in a ContactStd object. The StabilizationAssignment object
    has no constructor or members.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name].stabilizationAssignments

        The corresponding analysis keywords are:

        - CONTACT STABILIZATION
    """

    @abaqus_method_doc
    def changeValuesInStep(self, stepName: str, index: int, value: str):
        """This method allows modification of contact stabilization assignments to domain pairs
        already defined in a given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the contact stabilization assignments
            are to be modified.
        index
            An Int specifying the position of the contact stabilization assignment whose value is to
            be modified.
        value
            A String specifying the value of the contact stabilization to be assigned to the domain
            pair whose index is referenced.
        """
        ...

    @abaqus_method_doc
    def appendInStep(self, stepName: str, assignments: SymbolicConstant):
        """This method allows addition of contact stabilization assignments to new domain pairs in
        a given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which new contact stabilization assignments
            are to be defined.
        assignments
            A sequence of tuples specifying the stabilizations assigned to each surface pair. Each
            tuple contains three entries:
            - A region object or the SymbolicConstant GLOBAL.
            - A region object or the SymbolicConstant SELF.
            - A String specifying a StdStabilization object associated with this pair of regions.
        """
        ...

    @abaqus_method_doc
    def delete(self, indices: tuple):
        """The delete method allows you to delete existing contact stabilization assignments from a
        ContactStd object.

        Parameters
        ----------
        indices
            A sequence of Ints specifying the index of each contact stabilization assignment to
            delete.
        """
        ...
