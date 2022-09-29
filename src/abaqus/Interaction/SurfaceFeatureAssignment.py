from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class SurfaceFeatureAssignment:
    """The SurfaceFeatureAssignment object stores the surface feature angle assignment
    definition for surfaces in ContactExp or ContactStd objects. The
    SurfaceFeatureAssignment object has no constructor or members.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name].surfaceFeatureAssignments

        The corresponding analysis keywords are:

        - SURFACE PROPERTY ASSIGNMENT
    """

    @abaqus_method_doc
    def changeValuesInStep(
        self, stepName: str, index: int, value: Union[SymbolicConstant, float]
    ):
        """This method allows modification of surface feature angle assignments already defined on
        surfaces in a given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the surface feature assignments are to
            be modified.
        index
            An Int specifying the position of the surface feature angle assignment whose value is to
            be modified.
        value
            A tuple specifying the value of the surface feature assignments for the surface whose
            index is referenced. Each tuple contains two entries for Abaqus/Standard and three
            entries for Abaqus/Explicit:
            
            - A Float or a SymbolicConstant specifying the overriding surface primary feature angle
              value to be used for the surface. Possible values of the SymbolicConstant are PERIMETER,
              ALL, PICKED, or NONE. The ALL and PICKED values cannot be specified with the GLOBAL
              region constant and can be used only in the Abaqus/Explicit version of general contact.
            - A Float or a SymbolicConstant specifying the overriding surface secondary feature
              angle value to be used for the surface. Possible values of the SymbolicConstant are
              PERIMETER, ALL, PICKED, or NONE. The ALL and PICKED values cannot be specified with the
              GLOBAL region constant and can be used only in the Abaqus/Explicit version of general
              contact.
            - A SymbolicConstant ORIGINAL or CURRENT specifying the configuration.
        """
        ...

    @abaqus_method_doc
    def appendInStep(
        self, stepName: str, assignments: Union[SymbolicConstant, float]
    ):
        """This method allows addition of surface feature angle assignments to new surfaces in a
        given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which new surface feature angle assignments
            are to be defined.
        assignments
            A sequence of tuples specifying the surface feature angle assignments. Each tuple
            contains three entries for Abaqus/Standard and four entries for Abaqus/Explicit:

            - A region or a material object or the SymbolicConstant GLOBAL specifying the surface to
              which the feature angle is assigned.
            - A Float or a SymbolicConstant specifying the overriding surface primary feature angle
              value to be used for the surface. Possible values of the SymbolicConstant are PERIMETER,
              ALL, PICKED, or NONE. The ALL and PICKED values cannot be specified with the GLOBAL
              region constant and can be used only in the Abaqus/Explicit version of general contact.
            - A Float or a SymbolicConstant specifying the overriding surface slave feature
              angle value to be used for the surface. Possible values of the SymbolicConstant are
              PERIMETER, ALL, PICKED, or NONE. The ALL and PICKED values cannot be specified with the
              GLOBAL region constant and can be used only in the Abaqus/Explicit version of general
              contact.
            - A SymbolicConstant ORIGINAL or CURRENT specifying the configuration.
        """
        ...

    @abaqus_method_doc
    def delete(self, indices: tuple):
        """The delete method allows you to delete existing surface feature angle assignments from a
        ContactExp object.

        Parameters
        ----------
        indices
            A sequence of Ints specifying the index of each surface feature angle assignment to
            delete.
        """
        ...
