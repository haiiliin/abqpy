from typing import Dict, List, Optional, Sequence, Tuple

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

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
from ..UtilityAndView.abaqusConstants import (
    BOUNDARY_ONLY,
    GEOMETRY,
    OFF,
    SUPPRESS,
    Boolean,
    SymbolicConstant,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class PartInstance:
    """A PartInstance object is an instance of a Part object.

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

    #: A Part object specifying the instanced part.
    part: Optional[Part] = None

    #: A repository of Set objects specifying the sets created on the part. For more
    #: information, see Region commands.
    sets: Dict[str, Set] = {}

    #: A repository of Surface objects specifying the surfaces created on the part. For more
    #: information, see Region commands.
    surfaces: Dict[str, Surface] = {}

    #: A repository of Skin objects specifying the skins created on the part. For more
    #: information, see Region commands.
    skins: Dict[str, Skin] = {}

    #: A repository of Stringer objects specifying the stringers created on the part. For more
    #: information, see Region commands.
    stringers: Dict[str, Stringer] = {}

    #: A VertexArray object.
    vertices: VertexArray = VertexArray([])

    #: An IgnoredVertexArray object.
    ignoredVertices: IgnoredVertexArray = []

    #: An EdgeArray object.
    edges: EdgeArray = EdgeArray([])

    #: An IgnoredEdgeArray object.
    ignoredEdges: IgnoredEdgeArray = []

    #: A FaceArray object.
    faces: FaceArray = FaceArray([])

    #: A CellArray object.
    cells: CellArray = CellArray([])

    #: A repository of Datum objects.
    datums: List[Datum] = []

    #: A MeshElementArray object.
    elements: MeshElementArray = MeshElementArray([])

    #: A MeshNodeArray object.
    nodes: MeshNodeArray = MeshNodeArray([])

    #: A repository of MeshFace objects specifying all the element faces in the part instance.
    #: For a given element and a given face index within that element, the corresponding
    #: MeshFace object can be retrieved from the repository by using the key calculated as
    # (i*8 + j), where i and j are zero-based element and face indices, respectively.
    elemFaces: Dict[str, MeshFace] = {}

    #: A MeshFaceArray object.
    elementFaces: MeshFaceArray = MeshFaceArray([])

    #: A repository of MeshEdge objects specifying all the element edges in the part instance.
    #: For a given element and a given edge index on a given face within that element, the
    #: corresponding MeshEdge object can be retrieved from the repository by using the key
    #: calculated as (i*32 + j*4 + k), where i, j, and k are zero-based element, face, and edge
    #: indices, respectively.
    elemEdges: Dict[str, MeshEdge] = {}

    #: A MeshEdgeArray object.
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
            A Part object to be instanced. If the part does not exist, no PartInstance object is
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
            A PartInstance object.
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
    def checkGeometry(self, detailed: Boolean = OFF, level: Optional[int] = None):
        """This method checks the validity of the geometry of the part instance and prints a count of all
        topological entities on the part instance (faces, edges, vertices, etc.).

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
        Exception
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
        """This method translates an instance along the specified direction until it is in contact with a fixed
        instance.

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
            A Feature object
        """
        ...

    @abaqus_method_doc
    def ConvertConstraints(self):
        """This method converts the position constraints of an instance to absolute positions.

        The method deletes the constraint features on the instance but preserves the position in space.
        """
        ...

    @abaqus_method_doc
    def getPosition(self):
        """This method prints the sum of the translations and rotations applied to the PartInstance object."""
        ...

    @abaqus_method_doc
    def getRotation(self):
        """This method returns a tuple including the point of rotation, axis of rotation, and rotation angle (in
        degrees).

        Returns
        -------
        tuple
            A tuple including the point of rotation, axis of rotation, and rotation angle (in
            degrees).
        """
        ...

    @abaqus_method_doc
    def getTranslation(self) -> Tuple[float, float, float]:
        """This method returns a tuple of three Floats representing translation in the **X**, **Y**, and **Z**
        directions.

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
            A Part object specifying which Part will be instanced in place of the original Part.
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
            A sequence of three Floats specifying the **X**, **Y**, and **Z** coordinates of a point on
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
        """This method translates an instance along the specified direction until it is in contact with a fixed
        instance.

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
            A Feature object
        """
        ...
