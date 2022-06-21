from abaqusConstants import *
from .ConnectorOrientation import ConnectorOrientation
from ..Datum.DatumCsys import DatumCsys
from ..EditMesh.MeshEditAssembly import MeshEditAssembly
from ..Mesh.MeshAssembly import MeshAssembly
from ..Property.PropertyAssembly import PropertyAssembly
from ..Region.RegionAssembly import RegionAssembly
from ..Region.Set import Set


class Assembly(MeshEditAssembly, MeshAssembly, PropertyAssembly, RegionAssembly):
    """An :py:class:`~abaqus.Assembly.Assembly.Assembly` object is a container for instances of parts. The Assembly object has no
    constructor command. Abaqus creates the **rootAssembly** member when a Model object is
    created.

    Attributes
    ----------
    isOutOfDate: int
        An Int specifying that feature parameters have been modified but that the assembly has
        not been regenerated. Possible values are 0 and 1.
    timeStamp: float
        A Float specifying which gives an indication when the assembly was last modified.
    isLocked: int
        An Int specifying whether the assembly is locked or not. Possible values are 0 and 1.
    regenerateConstraintsTogether: Boolean
        A Boolean specifying whether the positioning constraints in the assembly should be
        regenerated together before regenerating other assembly features. The default value is
        ON.If the assembly has position constraint features and you modify the value of
        **regenerateConstraintsTogether**, Abaqus/CAE will regenerate the assembly features.
    vertices: VertexArray
        A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object specifying all the vertices existing at the assembly level. This
        member does not provide access to the vertices at the instance level.
    edges: EdgeArray
        An :py:class:`~abaqus.BasicGeometry.EdgeArray.EdgeArray` object specifying all the edges existing at the assembly level. This member
        does not provide access to the edges at the instance level.
    elements: MeshElementArray
        A :py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` object specifying all the elements existing at the assembly level.
        This member does not provide access to the elements at the instance level.
    nodes: MeshNodeArray
        A :py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` object specifying all the nodes existing at the assembly level. This
        member does not provide access to the nodes at the instance level.
    instances: dict[str, PartInstance]
        A repository of :py:class:`~abaqus.Assembly.PartInstance.PartInstance` objects.
    datums: list[Datum]
        A repository of :py:class:`~abaqus.:py:class:`~abaqus.Datum.Datum.Datum`.:py:class:`~abaqus.Datum.Datum.Datum`.:py:class:`~abaqus.Datum.Datum.Datum`` objects specifying all :py:class:`~abaqus.:py:class:`~abaqus.Datum.Datum.Datum`.:py:class:`~abaqus.Datum.Datum.Datum`.:py:class:`~abaqus.Datum.Datum.Datum`` objects in the assembly.
    features: dict[str, Feature]
        A repository of :py:class:`~abaqus.Assembly.:py:class:`~abaqus.Assembly.Feature.Feature`.:py:class:`~abaqus.Assembly.Feature.Feature`` objects specifying all :py:class:`~abaqus.Assembly.:py:class:`~abaqus.Assembly.Feature.Feature`.:py:class:`~abaqus.Assembly.Feature.Feature`` objects in the assembly.
    featuresById: dict[str, Feature]
        A repository of :py:class:`~abaqus.Feature.Feature.Feature` objects specifying all :py:class:`~abaqus.Feature.Feature.Feature` objects in the assembly. The :py:class:`~abaqus.Feature.Feature.Feature` objects in the featuresById repository are the same as the :py:class:`~abaqus.Feature.Feature.Feature` objects in the features repository. However, the key to the objects in the featuresById repository is an integer specifying the ID, whereas the key to the objects in the features repository is a string specifying the **name**.
    surfaces: dict[str, Surface]
        A repository of :py:class:`~abaqus.Region.Surface.Surface` objects specifying for more information, see [Region
        commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).
    allSurfaces: dict[str, Surface]
        A repository of :py:class:`~abaqus.Region.Surface.Surface` objects specifying for more information, see [Region
        commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).
    allInternalSurfaces: dict[str, Surface]
        A repository of :py:class:`~abaqus.Region.Surface.Surface` objects specifying picked regions.
    sets: dict[str, Set]
        A repository of :py:class:`~abaqus.Region.Set.Set` objects.
    allSets: dict[str, Set]
        A repository of :py:class:`~abaqus.Region.Set.Set` objects specifying for more information, see [Region
        commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).
    allInternalSets: dict[str, Set]
        A repository of :py:class:`~abaqus.Region.Set.Set` objects specifying picked regions.
    skins: dict[str, Skin]
        A repository of :py:class:`~abaqus.Region.Skin.Skin` objects specifying the skins created on the assembly.
    stringers: dict[str, Stringer]
        A repository of :py:class:`~abaqus.Region.Stringer.Stringer` objects specifying the stringers created on the assembly.
    referencePoints: dict[str, ReferencePoint]
        A repository of :py:class:`~abaqus.BasicGeometry.ReferencePoint.ReferencePoint` objects.
    modelInstances: dict[str, ModelInstance]
        A repository of :py:class:`~abaqus.Model.Model.ModelInstance` objects.
    allInstances: dict[str, typing.Union[PartInstance, ModelInstance]]
        A :py:class:`~abaqus.Assembly.PartInstance.PartInstance` object specifying the :py:class:`~abaqus.Assembly.PartInstance.PartInstance`s and A :py:class:`~abaqus.Model.Model.ModelInstance` object specifying
        the :py:class:`~abaqus.Model.Model.ModelInstance`s.
    engineeringFeatures: EngineeringFeature
        An :py:class:`~abaqus.EngineeringFeature.EngineeringFeature.EngineeringFeature` object.
    modelName: str
        A String specifying the name of the model to which the assembly belongs.
    connectorOrientations: ConnectorOrientationArray
        A :py:class:`~abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientationArray` object.
    sectionAssignments: SectionAssignmentArray
        A :py:class:`~abaqus.Property.SectionAssignmentArray.SectionAssignmentArray` object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import assembly
        mdb.models[name].rootAssembly
    """

    def ConnectorOrientation(
        self,
        region: Set,
        localCsys1: DatumCsys = None,
        axis1: SymbolicConstant = AXIS_1,
        angle1: float = 0,
        orient2sameAs1: Boolean = ON,
        localCsys2: DatumCsys = None,
        axis2: SymbolicConstant = AXIS_1,
        angle2: float = 0,
    ) -> ConnectorOrientation:
        """This method creates a ConnectorOrientation object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].rootAssembly.ConnectorOrientation
            session.odbs[name].rootAssembly.ConnectorOrientation

        Parameters
        ----------
        region
            A :py:class:`~abaqus.Region.Set.Set` object specifying the region to which the orientation is assigned.
        localCsys1
            A :py:class:`~abaqus.Datum.DatumCsys.DatumCsys` object specifying the local coordinate system of the first connector point.
            This value may be None, indicating the global coordinate system.
        axis1
            A SymbolicConstant specifying the axis of a datum coordinate system about which an
            additional rotation is applied. Possible values are AXIS_1, AXIS_2, and AXIS_3. The
            default value is AXIS_1.
        angle1
            A Float specifying the angle of the additional rotation. The default value is 0.0.
        orient2sameAs1
            A Boolean specifying whether or not the second connector point is to use the same local
            coordinate system, axis, and angle as the first point. The default value is ON.
        localCsys2
            A :py:class:`~abaqus.Datum.DatumCsys.DatumCsys` object specifying the local coordinate system of the second connector point.
            This value may be None, indicating the global coordinate system.
        axis2
            A SymbolicConstant specifying the axis of a datum coordinate system about which an
            additional rotation is applied. Possible values are AXIS_1, AXIS_2, and AXIS_3. The
            default value is AXIS_1.
        angle2
            A Float specifying the angle of the additional rotation. The default value is 0.0.

        Returns
        -------
        ConnectorOrientation
            A :py:class:`~abaqus.Assembly.ConnectorOrientation.ConnectorOrientation` object.
        """
        connectorOrientation = ConnectorOrientation(
            region, localCsys1, axis1, angle1, orient2sameAs1, localCsys2, axis2, angle2
        )
        self.connectorOrientations.append(connectorOrientation)
        return connectorOrientation
