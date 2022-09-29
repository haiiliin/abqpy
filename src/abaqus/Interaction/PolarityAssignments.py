from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class PolarityAssignments:
    """The PolarityAssignments object stores the polarity assignment definition for surfaces in
    ContactExp objects. The PolarityAssignments object has no constructor or members.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name].polarityAssignments

        The corresponding analysis keywords are:

        - CONTACT FORMULATION
    """

    @abaqus_method_doc
    def changeValuesInStep(self, stepName: str, index: int, value: SymbolicConstant):
        """This method allows you to modify polarity assignments already defined on surface pairs
        in a given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the main-secondary assignments are to
            be modified.
        index
            An Int specifying the position of the polarity assignment whose value is to be modified.
        value
            A SymbolicConstant specifying the value of the polarity to be assigned to the surface
            whose index is referenced. Possible values are SPOS, SNEG, and TWO_SIDED.
        """
        ...

    @abaqus_method_doc
    def appendInStep(self, stepName: str, assignments: SymbolicConstant):
        """This method allows you to add polarity assignments to new surface pairs in a given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the polarity assignments are to be
            defined.
        assignments
            A sequence of tuples specifying the polarity assignments. Each tuple contains two
            entries:
            - A region object or the SymbolicConstant GLOBAL specifying the surface to which the
              polarity attribute is assigned.
            - A SymbolicConstant specifying the overriding polarity value to be used for the first
              surface. Possible values of the SymbolicConstant are SPOS, SNEG, and TWO_SIDED.
        """
        ...

    @abaqus_method_doc
    def delete(self, indices: tuple):
        """The delete method allows you to delete existing polarity assignments.

        Parameters
        ----------
        indices
            A sequence of Ints specifying the index of each polarity assignment to delete.
        """
        ...
