from typing_extensions import Literal
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Region.Set import Set
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import (Boolean, FROM_SECTION, OFF, SINGLE_VALUE,
                                              SymbolicConstant)


@abaqus_class_doc
class SectionAssignment:
    """The SectionAssignment object is used to specify a section assignment on an assembly or
    part. Section assignments on the assembly are limited to connector elements only.

    .. note:: 
        This object can be accessed by::

            import section
            mdb.models[name].parts[name].sectionAssignments[i]
            import assembly
            mdb.models[name].rootAssembly.sectionAssignments[i]
            import odbAccess
            session.odbs[name].parts[name].sectionAssignments[i]
            session.odbs[name].rootAssembly.instances[name].sectionAssignments[i]
            session.odbs[name].rootAssembly.sectionAssignments[i]
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.sectionAssignments[i]
    """

    #: A Boolean specifying whether the section assignment is suppressed or not. The default
    #: value is OFF.
    suppressed: Boolean = OFF

    #: A :py:class:`~abaqus.Region.Set.Set` object specifying the region to which the section is assigned.
    region: Set

    #: A String specifying the name of the section.
    sectionName: str

    #: A SymbolicConstant specifying section thickness assignment method. Possible values are
    #: FROM_SECTION and FROM_GEOMETRY. The default value is FROM_SECTION.
    thicknessAssignment: SymbolicConstant = FROM_SECTION

    #: A Float specifying the offset of the shell section. The default value is 0.0.
    offset: float = 0

    #: A SymbolicConstant specifying the method used to define the shell offset. If
    #: **offsetType** is set to OFFSET_FIELD the **offsetField** must have a value. Possible values
    #: are SINGLE_VALUE, MIDDLE_SURFACE, TOP_SURFACE, BOTTOM_SURFACE, FROM_GEOMETRY, and
    #: OFFSET_FIELD. The default value is SINGLE_VALUE.
    offsetType: SymbolicConstant = SINGLE_VALUE

    #: A String specifying the name of the field specifying the offset. The default value is
    #: "".
    offsetField: str = ""

    @abaqus_method_doc
    def __init__(
        self,
        region: Set,
        sectionName: str,
        thicknessAssignment: Literal[C.FROM_SECTION, C.FROM_GEOMETRY] = FROM_SECTION,
        offset: float = 0,
        offsetType: Literal[C.TOP_SURFACE, C.MIDDLE_SURFACE, C.BOTTOM_SURFACE, C.SINGLE_VALUE, C.FROM_GEOMETRY, C.OFFSET_FIELD] = SINGLE_VALUE,
        offsetField: str = "",
    ):
        """This method creates a SectionAssignment object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].SectionAssignment
                mdb.models[name].rootAssembly.SectionAssignment

        Parameters
        ----------
        region
            A :py:class:`~abaqus.Region.Set.Set` object specifying the region to which the section is assigned.
        sectionName
            A String specifying the name of the section.
        thicknessAssignment
            A SymbolicConstant specifying section thickness assignment method. Possible values are
            FROM_SECTION and FROM_GEOMETRY. The default value is FROM_SECTION.
        offset
            A Float specifying the offset of the shell section. The default value is 0.0.
        offsetType
            A SymbolicConstant specifying the method used to define the shell offset. If
            **offsetType** is set to OFFSET_FIELD the **offsetField** must have a value. Possible values
            are SINGLE_VALUE, MIDDLE_SURFACE, TOP_SURFACE, BOTTOM_SURFACE, FROM_GEOMETRY, and
            OFFSET_FIELD. The default value is SINGLE_VALUE.
        offsetField
            A String specifying the name of the field specifying the offset. The default value is
            "".

        Returns
        -------
        SectionAssignment
            A :py:class:`~abaqus.Property.SectionAssignment.SectionAssignment` object.
        """
        ...

    @abaqus_method_doc
    def resume(self):
        """This method resumes the section assignment that was previously suppressed."""
        ...

    @abaqus_method_doc
    def suppress(self):
        """This method suppresses the section assignment."""
        ...

    @abaqus_method_doc
    def getVertices(self):
        """This method is only valid for connector section assignments. This method returns a
        sequence consisting of tuples of coordinates of the connector's endpoints.

        Returns
        -------
        Sequence[Tuple[float, ...]]
            A sequence of tuples of floats.

        Raises
        ------
        Exception
            An exception is thrown if getVertices() is called on any section assignment except
            connector section assignment. This method is valid only for connector section assignments.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the SectionAssignment object."""
        ...
