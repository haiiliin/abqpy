from typing_extensions import Literal
from typing import Union, Tuple, Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Material.Material import Material
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class SurfaceOffsetAssignment:
    """The SurfaceOffsetAssignment object stores the surface offset fraction assignment
    definition for surfaces in ContactExp and ContactStd objects. The
    SurfaceOffsetAssignment object has no constructor or members.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name].surfaceOffsetAssignments

        The corresponding analysis keywords are:

        - SURFACE PROPERTY ASSIGNMENT
    """

    @abaqus_method_doc
    def changeValuesInStep(
        self, stepName: str, index: int, value: Union[Literal[C.SPOS, C.ORIGINAL, C.SNEG], float]
    ):
        """This method allows modification of surface offset fraction assignments already defined
        on surfaces in a given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the surface offset assignments are to
            be modified.
        index
            An Int specifying the position of the surface offset fraction assignment whose value is
            to be modified.
        value
            A tuple specifying the value of the surface offset assignments for the surface whose
            index is referenced. Each tuple contains one entry:
            
            - A Float or a SymbolicConstant specifying the surface offset fraction value to be used
              for the surface. Possible values of the SymbolicConstant are ORIGINAL, SPOS, and SNEG.
        """
        ...

    @abaqus_method_doc
    def appendInStep(
        self, stepName: str,
        assignments: Sequence[Tuple[Union[Region, Material, Literal[C.SPOS, C.ORIGINAL, C.SNEG, C.GLOBAL]], float]],
    ):
        """This method allows addition of surface offset fraction assignments to new surfaces in a
        given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which new surface offset fraction
            assignments are to be defined.
        assignments
            A sequence of tuples specifying the surface offset fraction assignments. Each tuple
            contains two entries:

            - A region or a material object or the SymbolicConstant GLOBAL specifying the surface to
              which the offset fraction is assigned.
            - A Float or a SymbolicConstant specifying the surface offset fraction value to be used
              for the surface. Possible values of the SymbolicConstant are ORIGINAL, SPOS, and SNEG.

            .. versionchanged:: 2021
                The first entry in the tuple can be a material object now.
        """
        ...

    @abaqus_method_doc
    def delete(self, indices: tuple):
        """The delete method allows you to delete existing surface offset fraction assignments.

        Parameters
        ----------
        indices
            A sequence of Ints specifying the index of each surface offset fraction assignment to
            delete.
        """
        ...
