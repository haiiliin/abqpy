from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class ContactPropertyAssignment:
    """The ContactPropertyAssignment object stores the contact property assignment definition
    for domain pairs in ContactExp and ContactStd objects. The ContactPropertyAssignment
    object has no constructor or members.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name].contactPropertyAssignments

        The corresponding analysis keywords are:

        - CONTACT PROPERTY ASSIGNMENT
    """

    @abaqus_method_doc
    def changeValuesInStep(self, stepName: str, index: int, value: str):
        """This method allows modification of contact property assignments to domain pairs already
        defined in a given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the contact property assignments are
            to be modified.
        index
            An Int specifying the position of the contact property assignment whose value is to be
            modified.
        value
            A String specifying the value of the contact property to be assigned to the domain pair
            whose index is referenced.
        """
        ...

    @abaqus_method_doc
    def appendInStep(self, stepName: str, assignments: SymbolicConstant):
        """This method allows addition of contact property assignments to new domain pairs in a
        given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which new contact property assignments are
            to be defined.
        assignments
            A sequence of tuples specifying the properties assigned to each surface pair. Each tuple
            contains three entries:

            - A region or a material object or the SymbolicConstant GLOBAL.
            - A region or a material object or the SymbolicConstant SELF. When used with a ContactExp
              object, this parameter can also be a string that references an Eulerian material
              surface.
            - A String specifying a ContactProperty object associated with this pair of
              regions.

            .. versionchanged:: 2021
                Update descriptions of the three entries in the tuple.
        """
        ...

    @abaqus_method_doc
    def delete(self, indices: tuple, surfPair: SymbolicConstant):
        """The delete method allows you to delete existing contact property assignments.

        Parameters
        ----------
        indices
            A sequence of Ints specifying the index of each contact property assignment to delete.
            The **indices** and **surfPair** arguments are mutually exclusive.
        surfPair
            A sequence of tuples specifying the surface pair of each contact property assignment to
            delete. Each tuple contains two entries:

            - A region or a material object or the SymbolicConstant GLOBAL.
            - A region or a material object or the SymbolicConstant SELF. When
              used with a ContactExp object, this parameter can also be a string that references an
              Eulerian material surface.

            **surfPair** and **indices** arguments are mutually exclusive.

            .. versionchanged:: 2021
                Update descriptions of the two entries in the tuple.
        """
        ...
