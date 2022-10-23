from typing_extensions import Literal
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class MainSecondaryAssignment:
    """The MainSecondaryAssignment object stores the main-secondary assignment definition for
    surfaces in ContactExp and ContactStd objects. The MainSecondaryAssignment object has no
    constructor or members.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name].mainSecondaryAssignments

        The corresponding analysis keywords are:

        - CONTACT FORMULATION

    .. versionchanged:: 2022
        The MasterSlaveAssignment class was renamed to MainSecondaryAssignment.
    """

    @abaqus_method_doc
    def changeValuesInStep(self, stepName: str, index: int, value: Literal[C.BALANCED, C.SECONDARY, C.MAIN]):
        """This method allows modification of main-secondary assignments already defined on surface
        pairs in a given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the main-secondary assignments are to
            be modified.
        index
            An Int specifying the position of the main-secondary assignment whose value is to be
            modified.
        value
            A SymbolicConstant specifying the value of the main-secondary role to be assigned to the
            surface whose index is referenced. Possible values are MAIN, SECONDARY, and BALANCED.
            The SymbolicConstant BALANCED can be specified only in an Abaqus/Standard analysis.
        """
        ...

    @abaqus_method_doc
    def appendInStep(self, stepName: str, assignments: Literal[C.BALANCED, C.SECONDARY, C.MAIN, C.GLOBAL]):
        """This method allows addition of main-secondary assignments to new surface pairs in a
        given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the main-secondary assignments are to
            be defined.
        assignments
            A sequence of tuples specifying the main-secondary assignments. Each tuple contains two
            entries:
            
            - A region object or the SymbolicConstant GLOBAL specifying the surface to which the
              main-secondary attribute is assigned.
            - A SymbolicConstant specifying the overriding main-secondary value to be used for the
              first surface. Possible values of the SymbolicConstant are MAIN, SECONDARY, and
              BALANCED. The SymbolicConstant BALANCED can be specified only in an Abaqus/Standard
              analysis.
        """
        ...

    @abaqus_method_doc
    def delete(self, indices: tuple):
        """The delete method allows you to delete existing main-secondary assignments.

        Parameters
        ----------
        indices
            A sequence of Ints specifying the index of each main-secondary assignment to delete.
        """
        ...
