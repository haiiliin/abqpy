from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class MasterSlaveAssignment:
    """The MasterSlaveAssignment object stores the master-slave assignment definition for
    surfaces in ContactExp and ContactStd objects. The MasterSlaveAssignment object has no
    constructor or members.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name].masterSlaveAssignments

        The corresponding analysis keywords are:

        - CONTACT FORMULATION
    """

    @abaqus_method_doc
<<<<<<< HEAD:src/abaqus/Interaction/MasterSlaveAssignment.py
    def changeValuesInStep(self, stepName: str, index: int, value: SymbolicConstant):
        """This method allows modification of master-slave assignments already defined on surface
=======
    def changeValuesInStep(self, stepName: str, index: int, value: Literal[C.BALANCED, C.SECONDARY, C.MAIN]):
        """This method allows modification of main-secondary assignments already defined on surface
>>>>>>> 9cc45e870 ([typing]: Including remaining `Literal` in all modules (#3004)):src/abaqus/Interaction/MainSecondaryAssignment.py
        pairs in a given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the master-slave assignments are to
            be modified.
        index
            An Int specifying the position of the master-slave assignment whose value is to be
            modified.
        value
            A SymbolicConstant specifying the value of the master-slave role to be assigned to the
            surface whose index is referenced. Possible values are MAIN, SECONDARY, and BALANCED.
            The SymbolicConstant BALANCED can be specified only in an Abaqus/Standard analysis.
        """
        ...

    @abaqus_method_doc
<<<<<<< HEAD:src/abaqus/Interaction/MasterSlaveAssignment.py
    def appendInStep(self, stepName: str, assignments: SymbolicConstant):
        """This method allows addition of master-slave assignments to new surface pairs in a
=======
    def appendInStep(self, stepName: str, assignments: Literal[C.BALANCED, C.SECONDARY, C.MAIN, C.GLOBAL]):
        """This method allows addition of main-secondary assignments to new surface pairs in a
>>>>>>> 9cc45e870 ([typing]: Including remaining `Literal` in all modules (#3004)):src/abaqus/Interaction/MainSecondaryAssignment.py
        given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the master-slave assignments are to
            be defined.
        assignments
            A sequence of tuples specifying the master-slave assignments. Each tuple contains two
            entries:
            
            - A region object or the SymbolicConstant GLOBAL specifying the surface to which the
              master-slave attribute is assigned.
            - A SymbolicConstant specifying the overriding master-slave value to be used for the
              first surface. Possible values of the SymbolicConstant are MAIN, SECONDARY, and
              BALANCED. The SymbolicConstant BALANCED can be specified only in an Abaqus/Standard
              analysis.
        """
        ...

    @abaqus_method_doc
    def delete(self, indices: tuple):
        """The delete method allows you to delete existing master-slave assignments.

        Parameters
        ----------
        indices
            A sequence of Ints specifying the index of each master-slave assignment to delete.
        """
        ...
