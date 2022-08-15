from ..UtilityAndView.abaqusConstants import *


class InitializationAssignment:
    """The InitializationAssignment object stores the contact initialization assignment
    definition for domain pairs in a ContactStd or ContactExp object. The
    InitializationAssignment object has no constructor or members.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import interaction
            mdb.models[name].interactions[name].initializationAssignments

        The corresponding analysis keywords are:

        - CONTACT INITIALIZATION ASSIGNMENT
    """

    def changeValuesInStep(self, stepName: str, index: int, value: str):
        """This method allows modification of contact initialization assignments to domain pairs
        already defined in a given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the contact initialization assignments
            are to be modified.
        index
            An Int specifying the position of the contact initialization assignment whose value is
            to be modified.
        value
            A String specifying the value of the contact initialization to be assigned to the domain
            pair whose index is referenced.
        """
        ...

    def appendInStep(self, stepName: str, assignments: SymbolicConstant):
        """This method allows addition of contact initialization assignments to new domain pairs in
        a given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which new contact initialization assignments
            are to be defined.
        assignments
            A sequence of tuples specifying the initializations assigned to each surface pair. Each
            tuple contains four entries (fourth entry is for Abaqus/Explicit and is optional):
            - A region object or the SymbolicConstant GLOBAL (for Abaqus/Standard only).
            - A region object or the SymbolicConstant SELF (for Abaqus/Standard only).
            - A String specifying a StdInitialization or ExpInitializationobject associated with this pair of regions.
            - A String specifying a secondary surface type. This entry is applicable only if the ExpInitialization object is defined with **overclosureType** = CLEARANCE and **adjustNodalCoords** = True.
        """
        ...

    def delete(self, indices: tuple):
        """The delete method allows you to delete existing contact initialization assignments from
        a ContactStd or ContactExp object.

        Parameters
        ----------
        indices
            A sequence of Ints specifying the index of each contact initialization assignment to
            delete.
        """
        ...
