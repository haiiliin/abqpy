from typing import Dict, Optional, Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .AnalyticSurface import AnalyticSurface
from .AnalyticSurfaceSegment import AnalyticSurfaceSegment
from .BeamOrientationArray import BeamOrientationArray
from .OdbDatumCsys import OdbDatumCsys
from .OdbMeshElementArray import OdbMeshElementArray
from .OdbMeshNodeArray import OdbMeshNodeArray
from .OdbPart import OdbPart
from .OdbRigidBodyArray import OdbRigidBodyArray
from .OdbSet import OdbSet
from .RebarOrientationArray import RebarOrientationArray
from ..Property.MaterialOrientationArray import MaterialOrientationArray
from ..Property.SectionAssignmentArray import SectionAssignmentArray
from ..Section.Section import Section
from ..UtilityAndView.abaqusConstants import (AXIS_1, Boolean, INPUT, OFF, PROPAGATED, STACK_3,
                                              SymbolicConstant)


@abaqus_class_doc
class OdbInstanceBase:
    """A part instance is the usage of a part within an assembly.

    .. note:: 
        This object can be accessed by::

            import odbAccess
            session.odbs[name].rootAssembly.instances[name]
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance
    """

    #: A String specifying the instance name.
    name: str = ""

    #: A SymbolicConstant specifying the type of the Part object. Only a value of
    #: DEFORMABLE_BODY is currently supported.
    type: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the dimensionality of the Part object. Possible values are
    #: THREE_D, TWO_D_PLANAR, AXISYMMETRIC, and UNKNOWN_DIMENSION.
    embeddedSpace: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the state of the Instance as modified by the analysis.
    #: This member is only present if the Instance is part of the RootAssemblyState tree.
    #: Possible values are:PROPAGATED, specifying that the value is the same as the previous
    #: frame or the original rootAssembly.MODIFIED, specifying that the geometry of the
    #: instance has been changed at this frame.The default value is PROPAGATED.
    resultState: SymbolicConstant = PROPAGATED

    #: An :py:class:`~abaqus.Odb.OdbMeshNodeArray.OdbMeshNodeArray` object.
    nodes: OdbMeshNodeArray = []

    #: An :py:class:`~abaqus.Odb.OdbMeshElementArray.OdbMeshElementArray` object.
    elements: OdbMeshElementArray = []

    #: A repository of OdbSet objects specifying node sets.
    nodeSets: Dict[str, OdbSet] = {}

    #: A repository of OdbSet objects specifying element sets.
    elementSets: Dict[str, OdbSet] = {}

    #: A repository of OdbSet objects specifying surfaces.
    surfaces: Dict[str, OdbSet] = {}

    #: A :py:class:`~abaqus.Property.SectionAssignmentArray.SectionAssignmentArray` object.
    sectionAssignments: SectionAssignmentArray = []

    #: An :py:class:`~abaqus.Odb.OdbRigidBodyArray.OdbRigidBodyArray` object.
    rigidBodies: OdbRigidBodyArray = []

    #: A :py:class:`~abaqus.Odb.BeamOrientationArray.BeamOrientationArray` object.
    beamOrientations: BeamOrientationArray = []

    #: A :py:class:`~abaqus.Property.MaterialOrientationArray.MaterialOrientationArray` object.
    materialOrientations: MaterialOrientationArray = []

    #: A :py:class:`~abaqus.Odb.RebarOrientationArray.RebarOrientationArray` object.
    rebarOrientations: RebarOrientationArray = []

    #: An :py:class:`~abaqus.Odb.AnalyticSurface.AnalyticSurface` object specifying analytic Surface defined on the instance.
    analyticSurface: AnalyticSurface = AnalyticSurface()

    @abaqus_method_doc
    def __init__(self, name: str, object: OdbPart, localCoordSystem: tuple = ()):
        """This method creates an OdbInstance object from an OdbPart object.

        .. note:: 
            This function can be accessed by::

                session.odbs[name].rootAssembly.Instance

        Parameters
        ----------
        name
            A String specifying the instance name.
        object
            An :py:class:`~abaqus.Odb.OdbPart.OdbPart` object.
        localCoordSystem
            A sequence of sequences of three Floats specifying the rotation and translation of the
            part instance in the global Cartesian coordinate system. The first three sequences
            specify the new local coordinate system with its center at the origin.The first sequence
            specifies a point on the 1-axis.The second sequence specifies a point on the 2-axis.The
            third sequence specifies a point on the 3-axis.The fourth sequence specifies the
            translation of the local coordinate system from the origin to its intended location.For
            example, the following sequence moves a part 10 units in the **X**-direction with no
            rotation: `localCoordSystem = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (10, 0, 0))`The following
            sequence moves a part 5 units in the **X**-direction with rotation:
            `localCoordSystem = ((0, 1, 0), (1, 0, 0), (0, 0, 1), (5, 0, 0))` transforms a part
            containing the two points `Pt1= (1,0,0) Pt2= (2,0,0)` to `Pt1 = (0, 6, 0) Pt2 = (0, 7, 0)`

        Returns
        -------
        OdbInstance
            An :py:class:`~abaqus.Odb.OdbInstance.OdbInstance` object.
        """
        ...

    @abaqus_method_doc
    def assignBeamOrientation(
        self, region: str, method: SymbolicConstant, vector: tuple
    ):
        """This method assigns a beam section orientation to a region of a part instance.

        Parameters
        ----------
        region
            An OdbSet specifying a region on an instance.
        method
            A SymbolicConstant specifying the assignment method. Only a value of N1_COSINES is
            currently supported.
        vector
            A sequence of three Floats specifying the approximate local n1n1-direction of the beam
            cross-section.
        """
        ...

    @abaqus_method_doc
    def assignMaterialOrientation(
        self,
        region: str,
        localCsys: OdbDatumCsys,
        axis: SymbolicConstant = AXIS_1,
        angle: float = 0,
        stackDirection: SymbolicConstant = STACK_3,
    ):
        """This method assigns a material orientation to a region of a part instance.

        Parameters
        ----------
        region
            An OdbSet specifying a region on an instance.
        localCsys
            An :py:class:`~abaqus.Odb.OdbDatumCsys.OdbDatumCsys` object specifying the local coordinate system or None, indicating the
            global coordinate system.
        axis
            A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
            system about which an additional rotation is applied. For shells this axis is also the
            shell normal. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is
            AXIS_1.
        angle
            A Float specifying the angle of the additional rotation. The default value is 0.0.
        stackDirection
            A SymbolicConstant specifying the stack or thickness direction of the material. Possible
            values are STACK_1, STACK_2, STACK_3, and STACK_ORIENTATION. The default value is
            STACK_3.
        """
        ...

    @abaqus_method_doc
    def assignRebarOrientation(
        self,
        region: str,
        localCsys: OdbDatumCsys,
        axis: SymbolicConstant = AXIS_1,
        angle: float = 0,
    ):
        """This method assigns a rebar reference orientation to a region of a part instance.

        Parameters
        ----------
        region
            An OdbSet specifying a region on an instance.
        localCsys
            An :py:class:`~abaqus.Odb.OdbDatumCsys.OdbDatumCsys` object specifying the local coordinate system or None, indicating the
            global coordinate system.
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
    def getElementFromLabel(self, label: int):
        """This method is used to retrieved an element with a specific label from an instance
        object.

        Parameters
        ----------
        label
            An Int specifying the element label.

        Returns
        -------
        OdbMeshElement
            An :py:class:`~abaqus.Odb.OdbMeshElement.OdbMeshElement` object.

        Raises
        ------
        OdbError: Invalid element label
            If no element with the specified label exists.
        """
        ...

    @abaqus_method_doc
    def getNodeFromLabel(self, label: int):
        """This method is used to retrieved a node with a specific label from an instance object.

        Parameters
        ----------
        label
            An Int specifying the node label.

        Returns
        -------
        OdbMeshNode
            An OdbMeshNode object.

        Raises
        ------
        OdbError: Invalid node label
            If no node with the specified label exists.
        """
        ...

    @abaqus_method_doc
    def assignSection(self, region: str, section: Section):
        """This method is used to assign a section to a region on an instance.

        Parameters
        ----------
        region
            An OdbSet specifying a region on an instance.
        section
            A :py:class:`~abaqus.Section.Section.Section` object.

        Raises
        ------
        OdbError: Section assignment requires element set
            If **region** is not an element set.
        OdbError: Section assignment requires element set from this part instance
            If the element set is not from the current instance.
        """
        ...

    @abaqus_method_doc
    def AnalyticRigidSurf2DPlanar(
        self, name: str, profile: Sequence[AnalyticSurfaceSegment], filletRadius: str = 0
    ):
        """This method is used to define a two-dimensional AnalyticSurface object on the instance.

        Parameters
        ----------
        name
            The name of the analytic surface.
        profile
            A sequence of AnalyticSurfaceSegment objects or an OdbSequenceAnalyticSurfaceSegment
            object.
        filletRadius
            A Double specifying the radius of curvature to smooth discontinuities between adjoining
            segments. The default value is 0.0.

        Raises
        ------
        OdbError: 2D-Planar Analytic Rigid Surface can be defined only if the instance is of 
        type TWO_D_PLANAR or AXISYMMETRIC.
            If OdbPart associated with the part instance is of type THREE_D.
              
        """
        ...

    @abaqus_method_doc
    def AnalyticRigidSurfExtrude(
        self,
        name: str,
        profile: Sequence[AnalyticSurfaceSegment],
        filletRadius: str = 0,
        localCoordData: tuple = (),
    ):
        """This method is used to define a three-dimensional cylindrical AnalyticSurface on the
        instance.

        Parameters
        ----------
        name
            The name of the analytic surface.
        profile
            A sequence of AnalyticSurfaceSegment objects or an OdbSequenceAnalyticSurfaceSegment
            object.
        filletRadius
            A Double specifying the radius of curvature to smooth discontinuities between adjoining
            segments. The default value is 0.0.
        localCoordData
            A sequence of sequences of Floats specifying the global coordinates of points used to
            define the local coordinate system.

        Raises
        ------
        OdbError: Analytic Rigid Surface of type CYLINDER can be defined only if the instance is 
        of type THREE_D
            If OdbPart associated with the part instance is not of type THREE_D.
              
        """
        ...

    @abaqus_method_doc
    def AnalyticRigidSurfRevolve(
        self,
        name: str,
        profile: Sequence[AnalyticSurfaceSegment],
        filletRadius: str = 0,
        localCoordData: tuple = (),
    ):
        """This method is used to define a three-dimensional AnalyticSurface of revolution on the
        instance.

        Parameters
        ----------
        name
            The name of the analytic surface.
        profile
            A sequence of AnalyticSurfaceSegment objects or an OdbSequenceAnalyticSurfaceSegment
            object.
        filletRadius
            A Double specifying the radius of curvature to smooth discontinuities between adjoining
            segments. The default value is 0.0.
        localCoordData
            A sequence of sequences of Floats specifying the global coordinates of points used to
            define the local coordinate system.

        Raises
        ------
        OdbError: Analytic Rigid Surface of type REVOLUTION can be defined only if the
        instance is of type THREE_D
            If OdbPart associated with the part instance is not of type THREE_D.
              
        """
        ...

    @abaqus_method_doc
    def RigidBody(
        self,
        referenceNode: str,
        position: str = INPUT,
        isothermal: Boolean = OFF,
        elset: str = "",
        pinNodes: str = "",
        tieNodes: str = "",
        analyticSurface: str = "",
    ):
        """This method defines an OdbRigidBody on the instance.

        Parameters
        ----------
        referenceNode
            An OdbSet specifying the reference node assigned to the rigid body.
        position
            A symbolic constant specify if the location of the reference node is to be defined by
            the user. Possible values are INPUT, and CENTER_OF_MASS. The default value is INPUT.
        isothermal
            A Boolean specifying an isothermal rigid body. The default value is OFF. This parameter
            is used only for a fully-coupled thermal stress analysis.
        elset
            An OdbSet specifying an element set assigned to the rigid body.
        pinNodes
            An OdbSet specifying pin-type nodes assigned to the rigid body.
        tieNodes
            An OdbSet specifying tie-type nodes assigned to the rigid body.
        analyticSurface
            An AnalyticSurface specifying the Analytic Rigid Surface assigned to the rigid body.

        Raises
        ------
        OdbError: Rigid body definition requires a node set
            If **referenceNode** is not a node set.
        """
        ...
