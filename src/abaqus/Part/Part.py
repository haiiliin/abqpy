from ..EditMesh.MeshEditPart import MeshEditPart
from ..Mesh.MeshPart import MeshPart
from ..Property.PropertyPart import PropertyPart
from ..Region.RegionPart import RegionPart


class Part(MeshEditPart, MeshPart, PropertyPart, RegionPart):
    """The Part object defines the physical attributes of a structure. Parts are instanced into
    the assembly and positioned before an analysis.

    Attributes
    ----------
    geometryValidity: Boolean
        A Boolean specifying the validity of the geometry of the part. The value is computed,
        but it can be set to ON to perform feature and mesh operations on an invalid part. There
        is no guarantee that such operations will work if the part was originally invalid.
    isOutOfDate: int
        An Int specifying that feature parameters have been modified but that the part has not
        been regenerated. Possible values are 0 and 1.
    timeStamp: float
        A Float specifying when the part was last modified.
    vertices: VertexArray
        A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object specifying all the vertices in the part.
    ignoredVertices: IgnoredVertexArray
        An :py:class:`~abaqus.BasicGeometry.IgnoredVertexArray.IgnoredVertexArray` object specifying all the ignored vertices in the part.
    edges: EdgeArray
        An :py:class:`~abaqus.BasicGeometry.EdgeArray.EdgeArray` object specifying all the edges in the part.
    ignoredEdges: IgnoredEdgeArray
        An :py:class:`~abaqus.BasicGeometry.IgnoredEdgeArray.IgnoredEdgeArray` object specifying all the ignored edges in the part.
    faces: FaceArray
        A :py:class:`~abaqus.BasicGeometry.FaceArray.FaceArray` object specifying all the faces in the part.
    cells: CellArray
        A :py:class:`~abaqus.BasicGeometry.CellArray.CellArray` object specifying all the cells in the part.
    features: dict[str, Feature]
        A repository of :py:class:`~abaqus.Assembly.Feature.Feature` objects specifying all the features in the part.
    featuresById: dict[str, Feature]
        A repository of :py:class:`~abaqus.Assembly.:py:class:`~abaqus.Assembly.:py:class:`~abaqus.Assembly.Feature.Feature`.:py:class:`~abaqus.Assembly.Feature.Feature``.:py:class:`~abaqus.Assembly.:py:class:`~abaqus.Assembly.Feature.Feature`.:py:class:`~abaqus.Assembly.Feature.Feature``` objects specifying all :py:class:`~abaqus.Assembly.:py:class:`~abaqus.Assembly.:py:class:`~abaqus.Assembly.Feature.Feature`.:py:class:`~abaqus.Assembly.Feature.Feature``.:py:class:`~abaqus.Assembly.:py:class:`~abaqus.Assembly.Feature.Feature`.:py:class:`~abaqus.Assembly.Feature.Feature``` objects in :py:class:`~.:py:class:`~.the`` part. The :py:class:`~abaqus.Assembly.:py:class:`~abaqus.Assembly.:py:class:`~abaqus.Assembly.Feature.Feature`.:py:class:`~abaqus.Assembly.Feature.Feature``.:py:class:`~abaqus.Assembly.:py:class:`~abaqus.Assembly.Feature.Feature`.:py:class:`~abaqus.Assembly.Feature.Feature```
        objects in :py:class:`~.:py:class:`~.the`` featuresById repository are :py:class:`~.:py:class:`~.the`` same as :py:class:`~.:py:class:`~.the`` :py:class:`~abaqus.Assembly.:py:class:`~abaqus.Assembly.:py:class:`~abaqus.Assembly.Feature.Feature`.:py:class:`~abaqus.Assembly.Feature.Feature``.:py:class:`~abaqus.Assembly.:py:class:`~abaqus.Assembly.Feature.Feature`.:py:class:`~abaqus.Assembly.Feature.Feature``` objects in :py:class:`~.:py:class:`~.the``
        features repository. However, :py:class:`~.:py:class:`~.the`` key to :py:class:`~.:py:class:`~.the`` objects in :py:class:`~.:py:class:`~.the`` featuresById repository is
        an integer specifying :py:class:`~.:py:class:`~.the`` **ID**, whereas :py:class:`~.:py:class:`~.the`` key to :py:class:`~.:py:class:`~.the`` objects in :py:class:`~.:py:class:`~.the`` features
        repository is a string specifying :py:class:`~.:py:class:`~.the`` **name**.
    datums: list[Datum]
        A repository of :py:class:`~abaqus.Datum.Datum.Datum` objects specifying all the datums in the part.
    elements: MeshElementArray
        A :py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` object specifying all the elements in the part.
    elemFaces: dict[str, MeshFace]
        A repository of :py:class:`~abaqus.Mesh.MeshFace.MeshFace` objects specifying all the element faces in the part. For a
        given element and a given face index within that element, the corresponding :py:class:`~abaqus.Mesh.MeshFace.MeshFace`
        object can be retrieved from the repository by using the key calculated as (i*8 + j),
        where i and j are zero-based element and face indices, respectively.
    elementFaces: MeshFaceArray
        A :py:class:`~abaqus.Mesh.MeshFaceArray.MeshFaceArray` object specifying all the unique element faces in the part.
    nodes: MeshNodeArray
        A :py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` object specifying all the nodes in the part.
    retainedNodes: MeshNodeArray
        A :py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` object specifying all the retained nodes in the substructure part.
    sets: dict[str, Set]
        A repository of :py:class:`~abaqus.Region.Set.Set` objects specifying for more information, see :py:class:`~abaqus.Region.Set.Set`.
    allSets: dict[str, Set]
        A repository of :py:class:`~abaqus.Region.Set.Set` objects specifying the contents of the **all:py:class:`~abaqus.Region.Set.Set`s** repository is the
        same as the contents of the **sets** repository.
    allInternalSets: dict[str, Set]
        A repository of :py:class:`~abaqus.Region.Set.Set` objects specifying picked regions.
    surfaces: dict[str, Surface]
        A repository of :py:class:`~abaqus.Region.Surface.Surface` objects specifying for more information, see :py:class:`~abaqus.Region.Surface.Surface`.
    allSurfaces: dict[str, Surface]
        A repository of :py:class:`~abaqus.Region.Surface.Surface` objects specifying the contents of the **all:py:class:`~abaqus.Region.Surface.Surface`s** repository
        is the same as the contents of the **surfaces** repository.
    allInternalSurfaces: dict[str, Surface]
        A repository of :py:class:`~abaqus.Region.Surface.Surface` objects specifying picked regions.
    skins: dict[str, Skin]
        A repository of :py:class:`~abaqus.Region.Skin.Skin` objects specifying the skins created on the part.
    stringers: dict[str, Stringer]
        A repository of :py:class:`~abaqus.Region.Stringer.Stringer` objects specifying the stringers created on the part.
    referencePoints: ReferencePoints
        A repository of :py:class:`~abaqus.BasicGeometry.ReferencePoint.ReferencePoint` objects.
    engineeringFeatures: EngineeringFeature
        An :py:class:`~abaqus.EngineeringFeature.EngineeringFeature.EngineeringFeature` object.
    sectionAssignments: SectionAssignmentArray
        A :py:class:`~abaqus.Property.SectionAssignmentArray.SectionAssignmentArray` object.
    materialOrientations: MaterialOrientationArray
        A :py:class:`~abaqus.Property.MaterialOrientationArray.MaterialOrientationArray` object.
    compositeLayups: dict[str, CompositeLayup]
        A repository of :py:class:`~abaqus.Property.CompositeLayup.CompositeLayup` objects.
    elemEdges: dict[str, MeshEdge]
        A repository of :py:class:`~abaqus.Mesh.:py:class:`~abaqus.Mesh.MeshEdge.MeshEdge`.:py:class:`~abaqus.Mesh.MeshEdge.MeshEdge`` objects specifying all the element edges in the part. For a
        given element and a given edge index on a given face within that element, the
        corresponding :py:class:`~abaqus.Mesh.:py:class:`~abaqus.Mesh.MeshEdge.MeshEdge`.:py:class:`~abaqus.Mesh.MeshEdge.MeshEdge`` object can be retrieved from the repository by using the key
        calculated as (i*32 + j*4 + k), where i, j, and k are zero-based element, face, and edge
        indices, respectively.
    elementEdges: MeshEdgeArray
        A :py:class:`~abaqus.Mesh.MeshEdgeArray.MeshEdgeArray` object specifying all the unique element edges in the part.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import part
        mdb.models[name].parts[name]

    """

    pass
