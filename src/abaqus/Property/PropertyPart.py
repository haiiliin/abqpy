from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .CompositeLayup import CompositeLayup
from .MaterialOrientation import MaterialOrientation
from .SectionAssignment import SectionAssignment
from ..Datum.Datum import Datum
from ..Datum.DatumAxis import DatumAxis
from ..Datum.DatumCsys import DatumCsys
from ..Part.PartBase import PartBase
from ..Region.Region import Region
from ..Region.Set import Set
from ..Region.Surface import Surface
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class PropertyPart(PartBase):
    @abaqus_method_doc
    def CompositeLayup(
        self,
        name: str,
        description: str = "",
        offsetType: SymbolicConstant = GLOBAL,
        offsetField: str = "",
        offsetValues: float = 0,
        elementType: SymbolicConstant = SHELL,
        symmetric: Boolean = OFF,
    ) -> CompositeLayup:
        """This method creates a CompositeLayup object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].CompositeLayup

        Parameters
        ----------
        name
            A String specifying the repository key.
        description
            A String specifying a description of the composite layup.
        offsetType
            A SymbolicConstant specifying the method used to define the shell offset. If
            **offsetType** = OFFSET_FIELD the **offsetField** argument is required. This member is valid
            only if **elementType** = SHELL. Possible values are SINGLE_VALUE, MIDDLE_SURFACE,
            TOP_SURFACE, BOTTOM_SURFACE, OFFSET_FIELD, and GLOBAL. The default value is GLOBAL.
        offsetField
            A String specifying The name of the field specifying the offset. This member is valid
            only if **elementType** = SHELL. The default value is an empty string.
        offsetValues
            A Float specifying The offset of the shell section. This member is valid only if
            **elementType** = SHELL. The default value is 0.0.
        elementType
            A SymbolicConstant specifying the type of element in the composite layup. Possible
            values are SHELL, CONTINUUM_SHELL, and SOLID. The default value is SHELL.
        symmetric
            A Boolean specifying whether or not the layup should be made symmetric by the analysis.
            The default value is OFF.

        Returns
        -------
        layup: CompositeLayup
            A :py:class:`~abaqus.Property.CompositeLayup.CompositeLayup` object.

        Raises
        ------
        AbaqusException
        """
        self.compositeLayups[name] = compositeLayup = CompositeLayup(
            name,
            description,
            offsetType,
            offsetField,
            offsetValues,
            elementType,
            symmetric,
        )
        return compositeLayup

    @abaqus_method_doc
    def SectionAssignment(
        self,
        region: Set,
        sectionName: str,
        thicknessAssignment: SymbolicConstant = FROM_SECTION,
        offset: float = 0,
        offsetType: SymbolicConstant = SINGLE_VALUE,
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
        assignment: SectionAssignment
            A :py:class:`~abaqus.Property.SectionAssignment.SectionAssignment` object
        """
        sectionAssignment = SectionAssignment(
            region, sectionName, thicknessAssignment, offset, offsetType, offsetField
        )
        self.sectionAssignments.append(sectionAssignment)
        return sectionAssignment

    @abaqus_method_doc
    def MaterialOrientation(
        self,
        region: Optional[Set] = None,
        localCsys: Optional[DatumCsys] = None, 
        axis: SymbolicConstant = AXIS_1,
        angle: float = 0,
        stackDirection: SymbolicConstant = STACK_3,
        fieldName: str = "",
        orientationType: SymbolicConstant = GLOBAL,
        normalAxisDirection: SymbolicConstant = AXIS_3,
        normalAxisDefinition: SymbolicConstant = NORMAL_VECTOR,
        normalAxisRegion: Optional[Surface] = None,
        normalAxisDatum: Optional[DatumAxis] = None, 
        flipNormalDirection: Boolean = OFF,
        normalAxisVector: tuple = (),
        primaryAxisDirection: SymbolicConstant = AXIS_1,
        primaryAxisDefinition: SymbolicConstant = PRIMARY_VECTOR,
        primaryAxisRegion: Optional[Set] = None,
        primaryAxisDatum: Optional[DatumAxis] = None, 
        flipPrimaryDirection: Boolean = OFF,
        primaryAxisVector: tuple = (),
    ) -> MaterialOrientation:
        """This method creates a MaterialOrientation object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].MaterialOrientation

        Parameters
        ----------
        region
            A :py:class:`~abaqus.Region.Set.Set` object specifying a region for which the material orientation is defined.
        localCsys
            A :py:class:`~abaqus.Datum.DatumCsys.DatumCsys` object specifying the local coordinate system or None, describing the
            material orientation for the given region. In the ODB, this member was previously
            accessible using "csys," but support has now been added for localCsys and the csys
            member will be deprecated.
        axis
            A SymbolicConstant specifying the axis of a datum coordinate system about which an
            additional rotation is applied. For shells this axis is also the shell normal. Possible
            values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_1.
        angle
            A Float specifying the angle of the additional rotation (if accessed from the ODB
            instead of the MDB, it will be a string instead of a float). The default value is 0.0.
        stackDirection
            A SymbolicConstant specifying the stack or thickness direction. Possible values are
            STACK_1, STACK_2, STACK_3, and STACK_ORIENTATION. The default value is STACK_3.
        fieldName
            A String specifying the name of the DiscreteField object specifying the orientation. The
            default value is an empty string.
        orientationType
            A SymbolicConstant specifying the method used to define the material orientation. If
            **orientationType** = SYSTEM, the **region** and **localCsys** arguments are required. If
            **orientationType** = FIELD, the **fieldName** argument is required. Possible values are
            GLOBAL, SYSTEM, FIELD, DISCRETE, and USER. The default value is GLOBAL.
        normalAxisDirection
            A SymbolicConstant specifying the axis that is defined by the normal axis direction for
            a discrete orientation. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default
            value is AXIS_3.
        normalAxisDefinition
            A SymbolicConstant specifying the method used to define the normal axis direction for a
            discrete orientation. Possible values are SURFACE, NORMAL_DATUM, and NORMAL_VECTOR. The
            default value is NORMAL_VECTOR.
        normalAxisRegion
            A :py:class:`~abaqus.Region.Surface.Surface` object specifying a region whose geometric normals define the normal axis for
            the discrete orientation.
        normalAxisDatum
            A :py:class:`~abaqus.Datum.DatumAxis.DatumAxis` object specifying the Datum Axis or None, describing the normal axis
            direction for the discrete orientation.
        flipNormalDirection
            A Boolean specifying the flag to reverse the direction of the defined normal axis
            direction. The default value is OFF.
        normalAxisVector
            A sequence of Floats specifying the vector that defines the direction of the normal axis
            of the discrete orientation.
        primaryAxisDirection
            A SymbolicConstant specifying the axis that is defined by the primary axis direction for
            a discrete orientation. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default
            value is AXIS_1.
        primaryAxisDefinition
            A SymbolicConstant specifying the method used to define the primary axis direction for a
            discrete orientation. Possible values are SURFACE, PRIMARY_DATUM, and PRIMARY_VECTOR.
            The default value is PRIMARY_VECTOR.
        primaryAxisRegion
            A :py:class:`~abaqus.Region.Set.Set` object specifying a region whose geometric tangents define the primary axis for
            the discrete orientation.
        primaryAxisDatum
            A :py:class:`~abaqus.Datum.DatumAxis.DatumAxis` object specifying the Datum Axis or None, describing the primary axis
            direction for the discrete orientation.
        flipPrimaryDirection
            A Boolean specifying the flag to reverse the direction of the defined primary axis
            direction. The default value is OFF.
        primaryAxisVector
            A sequence of Floats specifying the vector that defines the direction of the primary
            axis of the discrete orientation.

        Returns
        -------
        orientation: MaterialOrientation
            A :py:class:`~abaqus.Property.MaterialOrientation.MaterialOrientation` object.
        """
        materialOrientation = MaterialOrientation(
            region,
            localCsys,
            axis,
            angle,
            stackDirection,
            fieldName,
            orientationType,
            normalAxisDirection,
            normalAxisDefinition,
            normalAxisRegion,
            normalAxisDatum,
            flipNormalDirection,
            normalAxisVector,
            primaryAxisDirection,
            primaryAxisDefinition,
            primaryAxisRegion,
            primaryAxisDatum,
            flipPrimaryDirection,
            primaryAxisVector,
        )
        self.materialOrientations.append(materialOrientation)
        return materialOrientation
    
    @abaqus_method_doc
    def assignBeamSectionOrientation(self, region: tuple, method: SymbolicConstant, n1: tuple):
        """This method assigns a beam section orientation to a region of a part.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].assignBeamSectionOrientation

        Parameters
        ----------
        region
            A sequence of geomSequences of Edge objects or a sequence of sequences of
            one-dimensional elements.
        method
            A SymbolicConstant specifying the assignment method. Only a value of N1_COSINES is
            currently supported.
        n1
            A sequence of three Floats specifying the approximate local n1n1-direction of the beam
            cross-section.
        """
        ...

    @abaqus_method_doc
    def assignMaterialOrientation(
        self, region: tuple, localCsys: Datum, axis: SymbolicConstant = AXIS_1, angle: float = 0
    ):
        """This method assigns a material orientation to a region.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].assignMaterialOrientation

        Parameters
        ----------
        region
            A sequence of geomSequences of ConstrainedSketchVertex, Edge, Face, and Cell objects or a sequence of
            sequences of elements.
        localCsys
            A :py:class:`~abaqus.Datum.Datum.Datum` object specifying the local coordinate system or None, indicating the global
            coordinate system.
        axis
            A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
            system about which an additional rotation is applied. For shells this axis is also the
            shell normal. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is
            AXIS_1.
        angle
            A Float specifying the angle of the additional rotation. The default value is 0.0.
        """
        ...

    @abaqus_method_doc
    def assignRebarOrientation(
        self, region: tuple, localCsys: Datum, axis: SymbolicConstant = AXIS_1, angle: float = 0
    ):
        """This method assigns a rebar reference orientation to a region.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].assignRebarOrientation

        Parameters
        ----------
        region
            A sequence of geomSequences of ConstrainedSketchVertex, Edge, Face, and Cell objects or a sequence of
            sequences of elements.
        localCsys
            A :py:class:`~abaqus.Datum.Datum.Datum` object specifying the local coordinate system or None, indicating the global
            coordinate system.
        axis
            A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
            system about which an additional rotation is applied. For shells this axis is also the
            shell normal. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is
            AXIS_1.
        angle
            A Float specifying the angle of the additional rotation. The default value is 0.0.
        """
        ...

    @abaqus_method_doc
    def flipNormal(self, regions: Region, referenceRegion: str = ""):
        """This method flips the normals of shell or membrane elements of an orphan mesh or of
        two-dimensional geometric regions.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].flipNormal

        Parameters
        ----------
        regions
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region on which normals are flipped. For 3D parts, the
            region contains Face objects or two-dimensional triangle or quadrilateral Element
            objects. For axisymmetric parts, the region contains Edge objects or line Elements
            objects.
        referenceRegion
            A two-dimensional element object whose normal is to be matched. If unspecified, all the
            normals associated with the given regions will be flipped. The **referenceRegion**
            argument is applicable only if the argument regions contain a sequence of quadrilateral
            or triangular elements.
        """
        ...

    @abaqus_method_doc
    def flipTangent(self, regions: Region):
        """This method flips the tangents of beam or truss elements of an orphan mesh or of
        one-dimensional geometric regions.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].flipTangent

        Parameters
        ----------
        regions
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region on which normals are flipped. The region contains
            Edge objects or one-dimensional Element objects.
        """
        ...

    @abaqus_method_doc
    def unassignBeamSectionOrientation(self, index: int):
        """This method deletes a beam section orientation assignment.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].unassignBeamSectionOrientation

        Parameters
        ----------
        index
            An Int specifying the number of the beam section orientation assignment to be deleted.
        """
        ...

    @abaqus_method_doc
    def unassignMaterialOrientation(self, index: int):
        """This method deletes a material orientation assignment.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].unassignMaterialOrientation

        Parameters
        ----------
        index
            An Int specifying the number of the material assignment to be deleted.
        """
        ...

    @abaqus_method_doc
    def unassignRebarOrientation(self, index: int):
        """This method deletes a rebar orientation assignment.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].unassignRebarOrientation

        Parameters
        ----------
        index
            An Int specifying the number of the rebar reference orientation assignment to be
            deleted.
        """
        ...
