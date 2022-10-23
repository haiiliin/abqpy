from typing import Dict, List, Optional, Sequence, Tuple

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ..BasicGeometry.CellArray import CellArray
from ..BasicGeometry.EdgeArray import EdgeArray
from ..BasicGeometry.FaceArray import FaceArray
from ..BasicGeometry.IgnoredEdgeArray import IgnoredEdgeArray
from ..BasicGeometry.IgnoredVertexArray import IgnoredVertexArray
from ..BasicGeometry.ReferencePoint import ReferencePoint
from ..BasicGeometry.VertexArray import VertexArray
from ..Datum.Datum import Datum
from ..Mesh.MeshEdge import MeshEdge
from ..Mesh.MeshEdgeArray import MeshEdgeArray
from ..Mesh.MeshElementArray import MeshElementArray
from ..Mesh.MeshFace import MeshFace
from ..Mesh.MeshFaceArray import MeshFaceArray
from ..Mesh.MeshNodeArray import MeshNodeArray
from ..Part.Part import Part
from ..Region.Set import Set
from ..Region.Skin import Skin
from ..Region.Stringer import Stringer
from ..Region.Surface import Surface
from ..UtilityAndView.abaqusConstants import BOUNDARY_ONLY, Boolean, GEOMETRY, OFF, SUPPRESS, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class PartInstance:
    """A :py:class:`~abaqus.Assembly.PartInstance.PartInstance` object is an instance of a Part object.

    .. note::
        This object can be accessed by::

            import assembly
            mdb.models[name].rootAssembly.allInstances[name]
            mdb.models[name].rootAssembly.instances[name]
    """

    #: A String specifying the repository key. The name must be a valid Abaqus object name.
    name: str = ""

    #: A Boolean specifying whether the part instance is dependent or independent. If
    #: **dependent** = OFF, the part instance is independent. The default value is OFF.
    dependent: Boolean = OFF

    #: A Boolean specifying whether the part instance is excluded from the simulation. If
    #: **excludedFromSimulation** = ON, the part instance is excluded from the simulation. The
    #: default value is OFF.
    excludedFromSimulation: Boolean = OFF

    #: A Boolean specifying the validity of the geometry of the instance. The value is
    #: computed, but it can be set to ON to perform feature and mesh operations on an invalid
    #: instance. There is no guarantee that such operations will work if the instance was
    #: originally invalid.
    geometryValidity: Boolean = OFF

    #: A SymbolicConstant specifying the part type. Possible values are DEFORMABLE_BODY,
    #: EULERIAN, DISCRETE_RIGID_SURFACE, and ANALYTIC_RIGID_SURFACE.
    analysisType: Optional[SymbolicConstant] = None

    #: An Int specifying the reference node number. This member is valid only if
    #: **analysisType** = DISCRETE_RIGID_SURFACE or ANALYTIC_RIGID_SURFACE.
    referenceNode: Optional[int] = None

    #: A :py:class:`~abaqus.Part.Part.Part` object specifying the instanced part.
    part: Optional[Part] = None

    #: A repository of Set objects specifying the sets created on the part. For more
    #: information, see [Region
    #: commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).
    sets: Dict[str, Set] = {}

    #: A repository of Surface objects specifying the surfaces created on the part. For more
    #: information, see [Region
    #: commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).
    surfaces: Dict[str, Surface] = {}

    #: A repository of Skin objects specifying the skins created on the part. For more
    #: information, see [Region
    #: commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).
    skins: Dict[str, Skin] = {}

    #: A repository of Stringer objects specifying the stringers created on the part. For more
    #: information, see [Region
    #: commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).
    stringers: Dict[str, Stringer] = {}

    #: A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object.
    vertices: VertexArray = VertexArray([])

    #: An :py:class:`~abaqus.BasicGeometry.IgnoredVertexArray.IgnoredVertexArray` object.
    ignoredVertices: IgnoredVertexArray = []

    #: An :py:class:`~abaqus.BasicGeometry.EdgeArray.EdgeArray` object.
    edges: EdgeArray = EdgeArray([])

    #: An :py:class:`~abaqus.BasicGeometry.IgnoredEdgeArray.IgnoredEdgeArray` object.
    ignoredEdges: IgnoredEdgeArray = []

    #: A :py:class:`~abaqus.BasicGeometry.FaceArray.FaceArray` object.
    faces: FaceArray = FaceArray([])

    #: A :py:class:`~abaqus.BasicGeometry.CellArray.CellArray` object.
    cells: CellArray = CellArray([])

    #: A repository of Datum objects.
    datums: List[Datum] = []

    #: A :py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` object.
    elements: MeshElementArray = MeshElementArray([])

    #: A :py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` object.
    nodes: MeshNodeArray = MeshNodeArray([])

    #: A repository of MeshFace objects specifying all the element faces in the part instance.
    #: For a given element and a given face index within that element, the corresponding
    #: MeshFace object can be retrieved from the repository by using the key calculated as (i*8
    #: + j), where i and j are zero-based element and face indices, respectively.
    elemFaces: Dict[str, MeshFace] = {}

    #: A :py:class:`~abaqus.Mesh.MeshFaceArray.MeshFaceArray` object.
    elementFaces: MeshFaceArray = MeshFaceArray([])

    #: A repository of MeshEdge objects specifying all the element edges in the part instance.
    #: For a given element and a given edge index on a given face within that element, the
    #: corresponding MeshEdge object can be retrieved from the repository by using the key
    #: calculated as (i*32 + j*4 + k), where i, j, and k are zero-based element, face, and edge
    #: indices, respectively.
    elemEdges: Dict[str, MeshEdge] = {}

    #: A :py:class:`~abaqus.Mesh.MeshEdgeArray.MeshEdgeArray` object.
    elementEdges: MeshEdgeArray = MeshEdgeArray([])

    #: A repository of ReferencePoint objects.
    referencePoints: Dict[str, ReferencePoint] = {}

    #: A String specifying the name of the part from which the instance was created.
    partName: str = ""

    @abaqus_method_doc
    def __init__(self, name: str, part: Part, autoOffset: Boolean = OFF, dependent: Boolean = OFF):
        """This method creates a PartInstance object and puts it into the instances repository.

        .. note::
            This function can be accessed by::

                mdb.models[name].rootAssembly.Instance

        Parameters
        ----------
        name
            A String specifying the repository key. The name must be a valid Abaqus object name.
        part
            A :py:class:`~abaqus.Part.Part.Part` object to be instanced. If the part does not exist, no PartInstance object is
            created.
        autoOffset
            A Boolean specifying whether to apply an auto offset to the new part instance that will
            offset it from existing part instances. The default value is OFF.
        dependent
            A Boolean specifying whether the part instance is dependent or independent. If
            **dependent** = OFF, the part instance is independent. The default value is OFF.

        Returns
        -------
        PartInstance
            A :py:class:`~abaqus.Assembly.PartInstance.PartInstance` object.
        """
        self.vertices = part.vertices
        self.ignoredEdges = part.ignoredEdges
        self.faces = part.faces
        self.cells = part.cells
        self.datums = part.datums
        self.elements = part.elements
        self.elemFaces = part.elemFaces
        self.elementFaces = part.elementFaces
        self.nodes = part.nodes
        self.sets = part.sets
        self.surfaces = part.surfaces
        self.skins = part.skins
        self.stringers = part.stringers
        self.referencePoints = part.referencePoints
        self.elemEdges = part.elemEdges
        self.elementEdges = part.elementEdges

    @abaqus_method_doc
    def InstanceFromBooleanCut(
        self,
        name: str,
        instanceToBeCut: str,
        cuttingInstances: Sequence["PartInstance"],
        originalInstances: Literal[C.SUPPRESS, C.DELETE] = SUPPRESS,
    ):
        """This method creates a PartInstance in the instances repository after subtracting or
        cutting the geometries of a group of part instances from that of a base part instance.

        .. note::
            This function can be accessed by::

                mdb.models[name].rootAssembly.Instance

        Parameters
        ----------
        name
            A String specifying the repository key. The name must be a valid Abaqus object name.
        instanceToBeCut
            A PartInstance specifying the base instance from which to cut other instances.
        cuttingInstances
            A sequence of PartInstance objects specifying the instances with which to cut the base
            instance.
        originalInstances
            A SymbolicConstant specifying whether the original instances should be suppressed or
            deleted after the merge operation. Possible values are SUPPRESS or DELETE. The default
            value is SUPPRESS.

        Returns
        -------
        PartInstance
            A :py:class:`~abaqus.Assembly.PartInstance.PartInstance` object.
        """
        ...

    @abaqus_method_doc
    def InstanceFromBooleanMerge(
        self,
        name: str,
        instances: Sequence["PartInstance"],
        keepIntersections: Boolean = False,
        originalInstances: Literal[C.SUPPRESS, C.DELETE] = SUPPRESS,
        domain: Literal[C.MESH, C.BOTH, C.GEOMETRY] = GEOMETRY,
        mergeNodes: Literal[C.MESH, C.ALL, C.BOUNDARY_ONLY, C.NONE] = BOUNDARY_ONLY,
        nodeMergingTolerance: Optional[float] = None,
        removeDuplicateElements: Boolean = True,
    ):
        """This method creates a PartInstance in the instances repository after merging two or more
        part instances.

        .. note::
            This function can be accessed by::

                mdb.models[name].rootAssembly.Instance

        Parameters
        ----------
        name
            A String specifying the repository key. The name must be a valid Abaqus object name.
        instances
            A sequence of PartInstance objects specifying the part instances to merge.
        keepIntersections
            A Boolean specifying whether the boundary intersections of Abaqus native part instances
            should be retained after the merge operation. The default value is False.
        originalInstances
            A SymbolicConstant specifying whether the original instances should be suppressed or
            deleted after the merge operation. Possible values are SUPPRESS or DELETE. The default
            value is SUPPRESS.
        domain
            A SymbolicConstant specifying whether geometry or mesh of the specified part instances
            is to be merged. Possible values are GEOMETRY, MESH or BOTH. The default value is
            GEOMETRY.
        mergeNodes
            A SymbolicConstant specifying which nodes of the specified part instances should be
            considered for merging. This argument is only applicable if **domain** is MESH. Possible
            values are BOUNDARY_ONLY, ALL, or NONE. The default value is BOUNDARY_ONLY.
        nodeMergingTolerance
            A Float specifying the maximum distance between nodes of the specified part instances
            that will be merged and replaced with a single node in the new part. The location of the
            new node is the average position of the deleted nodes. This argument is only applicable
            if **domain** is MESH. The default value is 10-6.
        removeDuplicateElements
            A Boolean specifying whether elements with the same connectivity in the new part will be
            merged into a single element. This argument is only applicable if **domain** is MESH. The
            default value is True.

        Returns
        -------
        PartInstance
            A :py:class:`~abaqus.Assembly.PartInstance.PartInstance` object.
        """
        ...

    @abaqus_method_doc
    def LinearInstancePattern(
        self,
        instanceList: tuple,
        number1: int,
        spacing1: float,
        number2: int,
        spacing2: float,
        direction1: tuple = (),
        direction2: tuple = (),
    ) -> Sequence["PartInstance"]:
        """This method creates multiple PartInstance objects in a linear pattern and puts them into
        the instances repository.

        .. note::
            This function can be accessed by::

                mdb.models[name].rootAssembly.Instance

        Parameters
        ----------
        instanceList
            A sequence of Strings specifying the names of instances to pattern.
        number1
            An Int specifying the total number of instances, including the original instances, that
            appear along the first direction in the pattern.
        spacing1
            A Float specifying the spacing between instances along the first direction in the
            pattern.
        number2
            An Int specifying the total number of instances, including the original instances, that
            appear along the second direction in the pattern.
        spacing2
            A Float specifying the spacing between instances along the second direction in the
            pattern.
        direction1
            A sequence of three Floats specifying a vector along the first direction. The default
            value is (1.0, 0.0, 0.0).
        direction2
            A sequence of three Floats specifying a vector along the second direction. The default
            value is (0.0, 1.0, 0.0).

        Returns
        -------
        Sequence[PartInstance]
            A sequence of :py:class:`~abaqus.Assembly.PartInstance.PartInstance` objects.
        """
        ...

    @abaqus_method_doc
    def RadialInstancePattern(
        self,
        instanceList: tuple,
        number: int,
        totalAngle: float,
        point: Sequence[float] = (),
        axis: Sequence[float] = (),
    ):
        """This method creates multiple PartInstance objects in a radial pattern and puts them into
        the instances repository.

        .. note::
            This function can be accessed by::

                mdb.models[name].rootAssembly.Instance

        Parameters
        ----------
        instanceList
            A sequence of Strings specifying the names of instances to pattern.
        number
            An Int specifying the total number of instances, including the original instances, that
            appear in the radial pattern.
        totalAngle
            A Float specifying the total angle in degrees between the first and last instance in the
            pattern. A positive angle corresponds to a counter-clockwise direction. The values 360°
            and -360° represent a special case where the pattern makes a full circle. In this case,
            because the copy would overlay the original, the copy is not placed at the last
            position. Possible values are -360.0 ≤ **totalAngle** ≤ 360.0.
        point
            A sequence of three Floats specifying the center of the radial pattern. The default
            value is (0.0, 0.0, 0.0).
        axis
            A sequence of three Floats specifying the central axis of the radial pattern. The
            default value is (0.0, 0.0, 1.0).

        Returns
        -------
        Sequence[PartInstance]
            A sequence of PartInstance objects.
        """
        ...

    @abaqus_method_doc
    def checkGeometry(self, detailed: Boolean = OFF, level: Optional[int] = None):
        """This method checks the validity of the geometry of the part instance and prints a count
        of all topological entities on the part instance (faces, edges, vertices, etc.).

        Parameters
        ----------
        detailed
            A Boolean specifying whether detailed output will be printed to the replay file. The
            default value is OFF.
        level
            An Int specifying which level of checking is performed. Values can range from 20 to 70,
            with higher values reporting less and less important errors. The default value is 20,
            which reports all critical errors. When the default value is used, the stored validity
            status is updated to agree with the result of this check.

        Raises
        ------
        An exception is thrown if this is a dependent part instance and **level** was either not
        specified or was set to 20, because the validity status cannot be updated for a
        dependent part instance. In this case, this command should be called on the Part
        instead. The geometry of dependent part instances cannot be changed.
        """
        ...

    @abaqus_method_doc
    def Contact(
        self,
        movableList: tuple,
        fixedList: tuple,
        direction: tuple,
        clearance: float,
        isFaceEdges: Boolean = OFF,
    ):
        """This method translates an instance along the specified direction until it is in contact
        with a fixed instance.

        Parameters
        ----------
        movableList
            A sequence of Face or Edge objects on the part instance to be moved.
        fixedList
            A sequence of Face or Edge objects on the part instance to remain fixed.
        direction
            A sequence of three Floats specifying the direction of contact.
        clearance
            A Float specifying the distance between the two faces along the direction of contact.
        isFaceEdges
            A Boolean specifying how Abaqus calculates the contact. If **isFaceEdges** is OFF, contact
            is computed from the movable face to the fixed face. If **isFaceEdges** is ON, contact is
            computed using only the edges of the movable face and not its interior. The default
            value is OFF.

        Returns
        -------
        feature: Feature
            A :py:class:`~abaqus.Feature.Feature.Feature` object
        """
        ...

    @abaqus_method_doc
    def ConvertConstraints(self):
        """This method converts the position constraints of an instance to absolute positions. The
        method deletes the constraint features on the instance but preserves the position in
        space.
        """
        ...

    @abaqus_method_doc
    def getPosition(self):
        """This method prints the sum of the translations and rotations applied to the PartInstance
        object.
        """
        ...

    @abaqus_method_doc
    def getRotation(self):
        """This method returns a tuple including the point of rotation, axis of rotation, and
        rotation angle (in degrees).

        Returns
        -------
        tuple
            A tuple including the point of rotation, axis of rotation, and rotation angle (in
            degrees).
        """
        ...

    @abaqus_method_doc
    def getTranslation(self) -> Tuple[float, float, float]:
        """This method returns a tuple of three Floats representing translation in the **X**-, **Y**-,
        and **Z**-directions.

        Returns
        -------
        Tuple[float, float, float]
            A tuple of three Floats representing the translation.
        """
        ...

    @abaqus_method_doc
    def replace(self, instanceOf: Part, applyConstraints: Boolean = True):
        """This method replaces one instance with an instance of another part.

        Parameters
        ----------
        instanceOf
            A :py:class:`~abaqus.Part.Part.Part` object specifying which Part will be instanced in place of the original Part.
        applyConstraints
            A Boolean specifying whether to apply existing constraints on the new instance or to
            position the new instance in the same place as the original instance. The default value
            is True. A value of False indicates that constraints applies to the instance are deleted
            will be deleted from the feature list.
        """
        ...

    @abaqus_method_doc
    def rotateAboutAxis(self, axisPoint: Sequence[float], axisDirection: Sequence[float], angle: float):
        """This method translates an instance by the specified amount.

        Parameters
        ----------
        axisPoint
            A sequence of three Floats specifying the **X**-, **Y**-, and **Z**-coordinates of a point on
            the axis.
        axisDirection
            A sequence of three Floats specifying the direction vector of the axis.
        angle
            A Float specifying the rotation angle in degrees. Use the right-hand rule to determine
            the direction.
        """
        ...

    @abaqus_method_doc
    def translate(self, vector: tuple):
        """This method translates an instance by the specified amount.

        Parameters
        ----------
        vector
            A sequence of three Floats specifying a translation vector.
        """
        ...

    @abaqus_method_doc
    def translateTo(
        self,
        movableList: tuple,
        fixedList: tuple,
        direction: tuple,
        clearance: float,
        vector: tuple = (),
    ):
        """This method translates an instance along the specified direction until it is in contact
        with a fixed instance.

        Parameters
        ----------
        movableList
            A sequence of Face or Edge objects on the part instance to be moved.
        fixedList
            A sequence of Face or Edge objects on the part instances to remain fixed.
        direction
            A sequence of three Floats specifying the direction of contact.
        clearance
            A Float specifying the distance between the two faces along the direction of contact.
        vector
            A sequence of three Floats specifying a translation vector. If this argument is
            specified, the movable instance will be translated by the specified amount without
            solving for the actual contact.

        Returns
        -------
        feature: Feature
            A :py:class:`~abaqus.Feature.Feature.Feature` object
        """
        ...
