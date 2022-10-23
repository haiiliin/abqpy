from typing import Union, overload, Dict, List, Optional, Tuple, Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .AssemblyFeature import AssemblyFeature
from .AssemblyModel import AssemblyModel
from .ConnectorOrientationArray import ConnectorOrientationArray
from .ModelInstance import ModelInstance
from .PartInstance import PartInstance
from ..BasicGeometry.EdgeArray import EdgeArray
from ..BasicGeometry.Face import Face
from ..BasicGeometry.ReferencePoint import ReferencePoint
from ..BasicGeometry.VertexArray import VertexArray
from ..Datum.Datum import Datum
from ..EngineeringFeature.EngineeringFeature import EngineeringFeature
from ..Mesh.MeshElement import MeshElement
from ..Mesh.MeshElementArray import MeshElementArray
from ..Mesh.MeshFace import MeshFace
from ..Mesh.MeshNode import MeshNode
from ..Mesh.MeshNodeArray import MeshNodeArray
from ..Part.Part import Part
from ..Property.SectionAssignmentArray import SectionAssignmentArray
from ..Region.Set import Set
from ..Region.Skin import Skin
from ..Region.Stringer import Stringer
from ..Region.Surface import Surface
from ..UtilityAndView.abaqusConstants import ALL_EDGES, Boolean, LOW, OFF, ON
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class AssemblyBase(AssemblyFeature):
    """An :py:class:`~abaqus.Assembly.Assembly.Assembly` object is a container for instances of parts. The Assembly object has no
    constructor command. Abaqus creates the **rootAssembly** member when a Model object is
    created.

    .. note::
        This object can be accessed by::

            import assembly
            mdb.models[name].rootAssembly
    """

    #: An Int specifying that feature parameters have been modified but that the assembly has
    #: not been regenerated. Possible values are 0 and 1.
    isOutOfDate: Optional[int] = None

    #: A Float specifying which gives an indication when the assembly was last modified.
    timeStamp: Optional[float] = None

    #: An Int specifying whether the assembly is locked or not. Possible values are 0 and 1.
    isLocked: Optional[int] = None

    #: A Boolean specifying whether the positioning constraints in the assembly should be
    #: regenerated together before regenerating other assembly features. The default value is
    #: ON.If the assembly has position constraint features and you modify the value of
    #: **regenerateConstraintsTogether**, Abaqus/CAE will regenerate the assembly features.
    regenerateConstraintsTogether: Boolean = ON

    #: A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object specifying all the vertices existing at the assembly level. This
    #: member does not provide access to the vertices at the instance level.
    vertices: VertexArray = VertexArray([])

    #: An :py:class:`~abaqus.BasicGeometry.EdgeArray.EdgeArray` object specifying all the edges existing at the assembly level. This member
    #: does not provide access to the edges at the instance level.
    edges: EdgeArray = EdgeArray([])

    #: A :py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` object specifying all the elements existing at the assembly level.
    #: This member does not provide access to the elements at the instance level.
    elements: MeshElementArray = MeshElementArray([])

    #: A :py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` object specifying all the nodes existing at the assembly level. This
    #: member does not provide access to the nodes at the instance level.
    nodes: MeshNodeArray = MeshNodeArray([])

    #: A repository of PartInstance objects.
    instances: Dict[str, PartInstance] = {}

    #: A repository of Datum objects specifying all Datum objects in the assembly.
    datums: List[Datum] = []

    #: A repository of Feature objects specifying all Feature objects in the assembly.
    features: Dict[str, AssemblyFeature] = {}

    #: A repository of Feature objects specifying all Feature objects in the assembly.The
    #: Feature objects in the featuresById repository are the same as the Feature objects in
    #: the features repository. However, the key to the objects in the featuresById repository
    #: is an integer specifying the **ID**, whereas the key to the objects in the features
    #: repository is a string specifying the **name**.
    featuresById: Dict[str, AssemblyFeature] = {}

    #: A repository of Surface objects specifying for more information, see [Region
    #: commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).
    surfaces: Dict[str, Surface] = {}

    #: A repository of Surface objects specifying for more information, see [Region
    #: commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).
    allSurfaces: Dict[str, Surface] = {}

    #: A repository of Surface objects specifying picked regions.
    allInternalSurfaces: Dict[str, Surface] = {}

    #: A repository of Set objects.
    sets: Dict[str, Set] = {}

    #: A repository of Set objects specifying for more information, see [Region
    #: commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).
    allSets: Dict[str, Set] = {}

    #: A repository of Set objects specifying picked regions.
    allInternalSets: Dict[str, Set] = {}

    #: A repository of Skin objects specifying the skins created on the assembly.
    skins: Dict[str, Skin] = {}

    #: A repository of Stringer objects specifying the stringers created on the assembly.
    stringers: Dict[str, Stringer] = {}

    #: A repository of ReferencePoint objects.
    referencePoints: Dict[str, ReferencePoint] = {}

    #: A repository of ModelInstance objects.
    modelInstances: Dict[str, ModelInstance] = {}

    #: A :py:class:`~abaqus.Assembly.PartInstance.PartInstance` object specifying the PartInstances and A :py:class:`~abaqus.Assembly.ModelInstance.ModelInstance` object specifying
    #: the ModelInstances.
    allInstances: Dict[str, Union[PartInstance, ModelInstance]] = {}

    #: An :py:class:`~abaqus.EngineeringFeature.EngineeringFeature.EngineeringFeature` object.
    engineeringFeatures: EngineeringFeature = EngineeringFeature()

    #: A String specifying the name of the model to which the assembly belongs.
    modelName: str = ""

    #: A :py:class:`~abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientationArray` object.
    connectorOrientations: ConnectorOrientationArray = []

    #: A :py:class:`~abaqus.Property.SectionAssignmentArray.SectionAssignmentArray` object.
    sectionAssignments: SectionAssignmentArray = []

    @overload
    @abaqus_method_doc
    def Instance(self, name: str, part: Part, autoOffset: Boolean = OFF, dependent: Boolean = OFF) -> PartInstance:
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
        ...

    @overload
    @abaqus_method_doc
    def Instance(self, name: str, model: AssemblyModel, autoOffset: Boolean = OFF) -> ModelInstance:
        """This method creates a ModelInstance object and puts it into the instances repository.

        .. note::
            This function can be accessed by::

                mdb.models[name].rootAssembly.Instance

        Parameters
        ----------
        name
            The repository key. The name must be a valid Abaqus object name.
        model
            A :py:class:`~abaqus.Model.Model.Model` object to be instanced. If the model does not exist, no ModelInstance object is
            created.
        autoOffset
            A Boolean specifying whether to apply an auto offset to the new instance that will
            offset it from existing instances. The default value is OFF.

        Returns
        -------
        ModelInstance
            A :py:class:`~abaqus.Assembly.ModelInstance.ModelInstance` object.
        """
        ...

    @abaqus_method_doc
    def Instance(self, name: str, *args, **kwargs) -> Union[PartInstance, ModelInstance]:
        """This method creates a PartInstance object and puts it into the instances repository.

        .. note::
            This function can be accessed by::

                mdb.models[name].rootAssembly.Instance

        Parameters
        ----------
        name
            A String specifying the repository key. The name must be a valid Abaqus object name.
        kwargs
            Key-value arguments

        Returns
        -------
        PartInstance
            A :py:class:`~abaqus.Assembly.PartInstance.PartInstance` object.
        """
        if "part" in kwargs.keys() or (len(args) > 0 and isinstance(args[0], Part)):
            instance = PartInstance(name, *args, **kwargs)
        else:
            instance = ModelInstance(name, *args, **kwargs)
            self.modelInstances[name] = instance
        self.instances[name] = instance
        self.allInstances[name] = instance
        return instance

    @abaqus_method_doc
    def backup(self):
        """This method makes a backup copy of the features in the assembly. The backup() method is
        used in conjunction with the restore() method.
        """
        ...

    @abaqus_method_doc
    def clearGeometryCache(self):
        """This method deletes the geometry cache. Deleting the geometry cache reduces the amount
        of memory being used.
        """
        ...

    @abaqus_method_doc
    def deleteAllFeatures(self):
        """This method deletes all the features in the assembly."""
        ...

    @abaqus_method_doc
    def deleteFeatures(self, featureNames: tuple):
        """This method deletes specified features from the assembly.

        Parameters
        ----------
        featureNames
            A sequence of Strings specifying the feature names that will be deleted from the
            assembly.
        """
        ...

    @abaqus_method_doc
    def excludeFromSimulation(self, instances: Sequence[PartInstance], exclude: str):
        """This method excludes the specified part instances from the analysis.

        Parameters
        ----------
        instances
            A sequence of PartInstance objects to be excluded from the analysis.
        exclude
            A Bool specifying whether to exclude the selected instances from the analysis or include
            them.
        """
        ...

    @abaqus_method_doc
    def featurelistInfo(self):
        """This method prints the name and status of all the features in the feature lists."""
        ...

    @abaqus_method_doc
    def getMassProperties(
        self,
        regions: str = "",
        relativeAccuracy: Literal[C.LOW, C.MEDIUM, C.HIGH] = LOW,
        useMesh: Boolean = False,
        specifyDensity: Boolean = False,
        density: str = "",
        specifyThickness: Boolean = False,
        thickness: str = "",
        miAboutCenterOfMass: Boolean = True,
        miAboutPoint: Tuple[float, float, float] = ...,
    ):
        """This method returns the mass properties of the assembly, or instances or regions. Only
        beams, trusses, shells, solids, point, nonstructural mass, and rotary inertia elements
        are supported.

        Parameters
        ----------
        regions
            A MeshElementArray, CellArray, FaceArray, EdgeArray, or list of PartInstance objects
            specifying the regions whose mass properties are to be queried. The whole assembly is
            queried by default.
        relativeAccuracy
            A SymbolicConstant specifying the relative accuracy for geometry computation. Possible
            values are LOW, MEDIUM, and HIGH. The default value is LOW.
        useMesh
            A Boolean specifying whether the mesh should be used in the computation if the geometry
            is meshed. The default value is False.
        specifyDensity
            A Boolean specifying whether a user-specified density should be used in regions with
            density errors such as undefined material density. The default value is False.
        density
            A double value specifying the user-specified density value to be used in regions with
            density errors. The user-specified density should be greater than 0.
        specifyThickness
            A Boolean specifying whether a user-specified thickness should be used in regions with
            thickness errors such as undefined thickness. The default value is False.
        thickness
            A double value specifying the user-specified thickness value to be used in regions with
            thickness errors. The user-specified thickness should be greater than 0.
        miAboutCenterOfMass
            A Boolean specifying if the moments of inertia should be evaluated about the center of
            mass. The default value is True.
        miAboutPoint
            A tuple of three floats specifying the coordinates of the point about which to evaluate
            the moment of inertia. By default if the moments of inertia are not being evaluated
            about the center of mass, they will be evaluated about the origin.

        Returns
        -------
        properties: dict
            A Dictionary object with the following items:
            **area**: None or a Float specifying the sum of the area of the specified faces. The area
            is computed only for one side for shells.
            **areaCentroid**: None or a tuple of three Floats representing the coordinates of the area
            centroid.
            **volume**: None or a Float specifying the volume of the specified regions.
            **volumeCentroid**: None or a tuple of three Floats representing the coordinates of the
            volume centroid.
            **massFromMassPerUnitSurfaceArea**: None or a Float specifying the mass due to mass per
            unit surface area.
            **mass**: None or a Float specifying the mass of the specified regions. It is the total
            mass and includes mass from quantities such as mass per unit surface area.
            **centerOfMass**: None or a tuple of three Floats representing the coordinates of the
            center of mass.
            **momentOfInertia**: None or a tuple of six Floats representing the moments of inertia
            about the center of mass or about the point specified.
            **warnings**: A tuple of SymbolicConstants representing the problems encountered while
            computing the mass properties. Possible SymbolicConstants are:
            UNSUPPORTED_ENTITIES: Some unsupported entities exist in the specified regions. The mass
            properties are computed only for beams, trusses, shells, solids, point and
            non-structural mass elements, and rotary inertia elements. The mass properties are not
            computed for axisymmetric elements, springs, connectors, gaskets, or any other elements.
            MISSING_THICKNESS: For some regions, the section definitions are missing thickness
            values.
            ZERO_THICKNESS: For some regions, the section definitions have a zero thickness value.
            VARIABLE_THICKNESS: The nodal thickness or field thickness specified for some regions
            has been ignored.
            NON_APPLICABLE_THICKNESS: For some regions, the thickness value is not applicable to the
            corresponding sections specified on the regions.
            MISSING_DENSITY: For some regions, the section definitions are missing material density
            values.
            MISSING_MATERIAL_DEFINITION: For some regions, the material definition is missing.
            ZERO_DENSITY: For some regions, the section definitions have a zero material density
            value.
            UNSUPPORTED_DENSITY: For some regions, either a negative material density or a
            temperature dependent density has been specified, or the material value is missing for
            one or more plies in the composite section.
            SHELL_OFFSETS: For shells, this method does not account for any offsets specified.
            MISSING_SECTION_DEFINITION: For some regions, the section definition is missing.
            UNSUPPORTED_SECTION_DEFINITION: The section definition provided for some regions is not
            supported.
            REINFORCEMENTS: This method does not account for any reinforcements specified on the
            model.
            SMEARED_PROPERTIES: For regions with composite section assignments, the density is
            smeared across the thickness. The volume centroid and center of mass computations for a
            composite shell use a lumped mass approach where the volume and mass is assumed to be
            lumped in the plane of the shell. As a result of these approximations the volume
            centroid, center of mass and moments of inertia may be slightly inaccurate for regions
            with composite section assignments.
            UNSUPPORTED_NON_STRUCTURAL_MASS_ENTITIES: This method does not account for any
            non-structural mass on wires.
            INCORRECT_MOMENT_OF_INERTIA: For geometry regions with non-structural mass per volume,
            the non-structural mass is assumed to be a point mass at the centroid of the regions.
            Thus, the moments of inertia may be inaccurate as the distribution of the non-structural
            mass is not accounted for. Use the mesh for accurately computing the moments of inertia.
            MISSING_BEAM_ORIENTATIONS: For some regions with beam section assignments, the beam
            section orientations are missing.
            UNSUPPORTED_BEAM_PROFILES: This method supports the Box, Pipe, Circular, Rectangular,
            Hexagonal, Trapezoidal, I, L, T, Arbitrary, and Tapered beam profiles. Any other beam
            profile is not supported.
            TAPERED_BEAM_MI: Moment of inertia calculations for tapered beams are not accurate.
            SUBSTRUCTURE_INCORRECT_PROPERTIES: The user assigned density and thickness is not
            considered for substructures.
        """
        ...

    @abaqus_method_doc
    def getAngle(self, plane1: str, plane2: str, line1: str, line2: str, commonVertex: str = ""):
        """This method returns the angle between the specified entities.

        Parameters
        ----------
        plane1
            A Face, MeshFace, or a Datum object specifying the first plane. The Datum object must
            represent a datum plane. The **plane1** and **line1** arguments are mutually exclusive. One
            of them must be specified.
        plane2
            A Face, MeshFace, or a Datum object specifying the second plane. The Datum object must
            represent a datum plane. The **plane2** and **line2** arguments are mutually exclusive. One
            of them must be specified.
        line1
            An Edge, MeshEdge, or a Datum object specifying the first curve. The Datum object must
            represent a datum axis. The **plane1** and **line1** arguments are mutually exclusive. One
            of them must be specified.
        line2
            An Edge, MeshEdge, or a Datum object specifying the second curve. The Datum object must
            represent a datum axis. The **plane2** and **line2** arguments are mutually exclusive. One
            of them must be specified.
        commonVertex
            If the two selected Edge objects have more than one vertex in common, this ConstrainedSketchVertex object
            specifies the vertex at which to evaluate the angle.

        Returns
        -------
        float
            A Float specifying the angle between the specified entities. If you provide a plane as
            an argument, Abaqus/CAE computes the angle using the normal to the plane.
        """
        ...

    @abaqus_method_doc
    def getCoordinates(self, entity: str):
        """This method returns the coordinates of a specified point.

        Parameters
        ----------
        entity
            A ConstrainedSketchVertex, Datum point, MeshNode, or ReferencePoint specifying the entity to query.

        Returns
        -------
        Tuple[float, float]
            A tuple of three Floats representing the coordinates of the specified point.
        """
        ...

    @abaqus_method_doc
    def getDistance(self, entity1: str, entity2: str, printResults: Boolean = OFF):
        """Depending on the arguments provided, this method returns one of the following:

        - The distance between two points.
        - The minimum distance between a point and an edge.
        - The minimum distance between two edges.

        Parameters
        ----------
        entity1
            A ConstrainedSketchVertex, Datum point, MeshNode, or Edge specifying the first entity from which to
            measure.
        entity2
            A ConstrainedSketchVertex, Datum point, MeshNode, or Edge specifying the second entity to which to
            measure.
        printResults
            A Boolean that determines whether a verbose output is to be printed. The default is True

        Returns
        -------
        float
            A Float specifying the calculated distance.
        """
        ...

    @abaqus_method_doc
    def getFacesAndVerticesOfAttachmentLines(self, edges: EdgeArray):
        """Given an array of edge objects, this method returns a tuple of dictionary objects. Each
        object consists of five members including the attachment line and associated face and
        vertex objects.

        Parameters
        ----------
        edges
            An :py:class:`~abaqus.BasicGeometry.EdgeArray.EdgeArray` object which is a sequence of Edge objects.

        Returns
        -------
        Sequence[dict]
            A tuple of dictionary objects. Each dictionary contains five items with the following keys:

            - **edge**: An :py:class:`~abaqus.BasicGeometry.Edge.Edge` object specifying the attachment line.
            - **startFace**: A :py:class:`~abaqus.BasicGeometry.Face.Face` object specifying the face associated with one end of the
              attachment line.
            - **endFace**: A :py:class:`~abaqus.BasicGeometry.Face.Face` object specifying the face associated with the other end of
              the attachment line.
            - **startVertex**: A :py:class:`~abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertex.ConstrainedSketchVertex`
              object specifying the vertex associated with one end of the attachment line. This end is also associated with the startFace.
            - **endVertex**: A :py:class:`~abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertex.ConstrainedSketchVertex`
              object specifying the vertex associated with the other end of the attachment line. This end is also associated with the endFace.
        """
        ...

    @abaqus_method_doc
    def getSurfaceSections(self, surface: str):
        """This method returns a list of the sections assigned to the regions encompassed by the
        specified surface.

        Parameters
        ----------
        surface
            A string specifying the Surface name.

        Returns
        -------
        Sequence[str]
            A tuple of strings representing the section names. If no section names are found, the
            tuple will contain one empty string.
        """
        ...

    @abaqus_method_doc
    def importEafFile(self, filename: str, ids: tuple = ()):
        """This method imports an assembly from an EAF file into the root assembly.

        Parameters
        ----------
        filename
            A String specifying the path to the EAF file from which to import the assembly.
        ids
            A sequence of Ints. Each Int in the sequence is a unique identifier of the occurrence in
            the assembly tree or component identifier associated with the part in the EAF file. If
            **ids** is an empty sequence, all occurrences or parts will be imported. The default value
            is an empty sequence.
        """
        ...

    @abaqus_method_doc
    def importParasolidFile(self, filename: str, ids: tuple = ()):
        """This method imports an assembly from the Parasolid file into the root assembly.

        Parameters
        ----------
        filename
            A String specifying the path to a Parasolid file from which to import the assembly.
        ids
            A sequence of Ints. Each Int in the sequence is a unique identifier of the occurrence in
            the assembly tree or component identifier associated with the part in the EAF file. If
            **ids** is an empty sequence, all occurrences or parts will be imported. The default value
            is an empty sequence.
        """
        ...

    @abaqus_method_doc
    def importCatiaV5File(self, filename: str, ids: tuple = ()):
        """This method imports an assembly from a CATIA V5 Elysium Neutral file into the root
        assembly.

        Parameters
        ----------
        filename
            A String specifying the path to the CATIA V5 Elysium Neutral file from which to import
            the assembly.
        ids
            A sequence of Ints. Each Int in the sequence is a unique identifier of the occurrence in
            the assembly tree or component identifier associated with the part in the EAF file. If
            **ids** is an empty sequence, all occurrences or parts will be imported. The default value
            is an empty sequence.
        """
        ...

    @abaqus_method_doc
    def importEnfFile(self, filename: str, ids: tuple = ()):
        """This method imports an assembly from an Elysium Neutral file created by Pro/ENGINEER,
        I-DEAS, or CATIA V5 into the root assembly.

        Parameters
        ----------
        filename
            A String specifying the path to the Elysium Neutral file from which to import the
            assembly.
        ids
            A sequence of Ints. Each Int in the sequence is a unique identifier of the occurrence in
            the assembly tree or component identifier associated with the part in the EAF file. If
            **ids** is an empty sequence, all occurrences or parts will be imported. The default value
            is an empty sequence.
        """
        ...

    @abaqus_method_doc
    def importIdeasFile(self, filename: str, ids: tuple = ()):
        """This method imports an assembly from an I-DEAS Elysium Neutral file into the root
        assembly.

        Parameters
        ----------
        filename
            A String specifying the path to the I-DEAS Elysium Neutral file from which to import the
            assembly.
        ids
            A sequence of Ints. Each Int in the sequence is a unique identifier of the occurrence in
            the assembly tree or component identifier associated with the part in the EAF file. If
            **ids** is an empty sequence, all occurrences or parts will be imported. The default value
            is an empty sequence.
        """
        ...

    @abaqus_method_doc
    def importProEFile(self, filename: str, ids: tuple = ()):
        """This method imports an assembly from a Pro/ENGINEER Elysium Neutral file into the root
        assembly.

        Parameters
        ----------
        filename
            A String specifying the path to the Pro/ENGINEER Elysium Neutral file from which to
            import the assembly.
        ids
            A sequence of Ints. Each Int in the sequence is a unique identifier of the occurrence in
            the assembly tree or component identifier associated with the part in the EAF file. If
            **ids** is an empty sequence, all occurrences or parts will be imported. The default value
            is an empty sequence.
        """
        ...

    @abaqus_method_doc
    def makeDependent(self, instances: Sequence[PartInstance]):
        """This method converts the specified part instances from independent to dependent part
        instances.

        Parameters
        ----------
        instances
            A sequence of PartInstance objects to convert to dependent part instances.
        """
        ...

    @abaqus_method_doc
    def makeIndependent(self, instances: Sequence[PartInstance]):
        """This method converts the specified part instances from dependent to independent part
        instances.

        Parameters
        ----------
        instances
            A sequence of PartInstance objects to convert to independent part instances.
        """
        ...

    @abaqus_method_doc
    def printAssignedSections(self):
        """This method prints a summary of assigned connector sections."""
        ...

    @abaqus_method_doc
    def printConnectorOrientations(self):
        """This method prints a summary of connector orientations."""
        ...

    @abaqus_method_doc
    def projectReferencesOntoSketch(
        self,
        sketch: str,
        filter: Literal[C.ALL_EDGES, C.COPLANAR_EDGES] = ALL_EDGES,
        upToFeature: Optional[AssemblyFeature] = None,
        edges: tuple = (),
        vertices: tuple = (),
    ):
        """This method projects the specified edges, vertices, and datum points from the assembly
        onto the specified ConstrainedSketch object. The edges, vertices, and datum points
        appear on the sketch as reference geometry.

        Parameters
        ----------
        sketch
            The ConstrainedSketch object on which the edges, vertices, and datum points are
            projected.
        filter
            A SymbolicConstant specifying how to limit the amount of projection. Possible values are
            ALL_EDGES and COPLANAR_EDGES. If **filter** = COPLANAR_EDGES, edges that are coplanar to the
            sketching plane are the only candidates for projection. The default value is ALL_EDGES.
        upToFeature
            A :py:class:`~abaqus.Feature.Feature.Feature` object specifying a marker in the feature-based history of the part.
            Abaqus/CAE projects onto the sketch only the part entities that were created before the
            feature specified by this marker. By default, all part entities are candidates for
            projection.
        edges
            A sequence of candidate edges to be projected onto the sketch. By default, all edges are
            candidates for projection.
        vertices
            A sequence of candidate vertices to be projected onto the sketch. By default, all
            vertices are candidates for projection.
        """
        ...

    @abaqus_method_doc
    def queryCachedStates(self):
        """This method displays the position of geometric states relative to the sequence of
        features in the assembly cache. The output is displayed in the message area.
        """
        ...

    @abaqus_method_doc
    def regenerate(self):
        """This method regenerates the assembly and brings it up to date with the latest values of
        the assembly parameters. When you modify features of an assembly, it may be convenient
        to postpone regeneration until you make all your changes, since regeneration can be time
        consuming. In contrast, when you modify features of a part that is included in the
        assembly, you should use this command to regenerate the assembly. When you regenerate
        the assembly, it will reflect the changes that you made to the part.
        """
        ...

    @abaqus_method_doc
    def regenerationWarnings(self):
        """This method prints any regeneration warnings associated with the features."""
        ...

    @abaqus_method_doc
    def restore(self):
        """This method restores the parameters of all features in the assembly to the value they
        had before a failed regeneration. Use the restore method after a failed regeneration,
        followed by a regenerate command.
        """
        ...

    @abaqus_method_doc
    def resumeAllFeatures(self):
        """This method resumes all the suppressed features in the part or assembly."""
        ...

    @abaqus_method_doc
    def resumeFeatures(self, featureNames: tuple):
        """This method resumes the specified suppressed features in the assembly.

        Parameters
        ----------
        featureNames
            A sequence of Strings specifying the names of features to resume.
        """
        ...

    @abaqus_method_doc
    def resumeLastSetFeatures(self):
        """This method resumes the last set of features to be suppressed in the assembly."""
        ...

    @abaqus_method_doc
    def rotate(
        self,
        instanceList: Sequence[str],
        axisPoint: Sequence[float],
        axisDirection: Sequence[float],
        angle: float,
    ):
        """This method rotates given instances by the specified amount.

        Parameters
        ----------
        instanceList
            A sequence of Strings specifying the names of instances to rotate.
        axisPoint
            A sequence of three Floats specifying the coordinates of a point on the axis.
        axisDirection
            A sequence of three Floats specifying the direction of the axis.
        angle
            A Float specifying the rotation angle in degrees. Use the right-hand rule to determine
            the direction.
        """
        ...

    @abaqus_method_doc
    def translate(self, instanceList: tuple, vector: tuple):
        """This method translates given instances by the specified amount.

        Parameters
        ----------
        instanceList
            A sequence of Strings specifying the names of instances to translate.
        vector
            A sequence of three Floats specifying a translation vector.
        """
        ...

    @abaqus_method_doc
    def saveGeometryCache(self):
        """This method caches the current geometry, which improves regeneration performance."""
        ...

    @abaqus_method_doc
    def setValues(self, regenerateConstraintsTogether: Boolean):
        """This method modifies the behavior associated with the specified assembly.

        Parameters
        ----------
        regenerateConstraintsTogether
            A Boolean specifying whether the positioning constraints in the assembly should be
            regenerated together before regenerating other assembly features. The default value is
            ON.If the assembly has position constraint features and you modify the value of
            **regenerateConstraintsTogether**, Abaqus/CAE will regenerate the assembly features.

        Raises
        ------
        FeatureError: Regeneration failed
            If one or more features in the assembly fails to regenerate
        """
        ...

    @abaqus_method_doc
    def suppressFeatures(self, featureNames: tuple):
        """This method suppresses specified features.

        Parameters
        ----------
        featureNames
            A sequence of Strings specifying the names of features to suppress in the assembly.
        """
        ...

    @abaqus_method_doc
    def unlinkInstances(self, instances: Sequence[PartInstance]):
        """This method converts the specified PartInstance objects from linked child instances to
        regular instances. The parts associated with the selected instances will be converted to
        regular parts as well.

        Parameters
        ----------
        instances
            A sequence of PartInstance objects to be converted to regular part instances.
        """
        ...

    @abaqus_method_doc
    def writeAcisFile(self, fileName: str, version: Optional[float] = None):
        """This method exports the assembly to a named file in ACIS part (SAT) or assembly (ASAT)
        format.

        Parameters
        ----------
        fileName
            A String specifying the name of the file to which to write. The file name's extension is
            used to determine whether a part or assembly is written. Use the file extension .asat
            for the assembly format.
        version
            A Float specifying the ACIS version. For example, the Float 12.0 corresponds to ACIS
            Version 12.0. The default value is the current version of ACIS.
        """
        ...

    @abaqus_method_doc
    def writeCADParameters(self, paramFile: str, modifiedParams: tuple = (), updatePaths: str = ""):
        """This method writes the parameters that were imported from the CAD system to a parameter
        file.

        Parameters
        ----------
        paramFile
            A String specifying the parameter file name.
        modifiedParams
            A tuple of tuples each containing the part name, the parameter name and the modified
            parameter value. Default is an empty tuple.
        updatePaths
            A Bool specifying whether to update the path of the CAD model file specified in the
            **parameterFile** to the current directory, if the CAD model is present in the current
            directory.
        """
        ...

    @abaqus_method_doc
    def lock(self):
        """This method locks the assembly. Locking the assembly prevents any further changes to the
        assembly that can trigger regeneration of the assembly.
        """
        ...

    @abaqus_method_doc
    def unlock(self):
        """This method unlocks the assembly. Unlocking the assembly allows it to be regenerated
        after any modifications to the assembly.
        """
        ...

    @abaqus_method_doc
    def setMeshNumberingControl(
        self,
        instances: Sequence[PartInstance],
        startNodeLabel: Optional[int] = None,
        startElemLabel: Optional[int] = None,
    ):
        """This method changes the start node and/or element labels on the specified independent
        part instances before or after Abaqus/CAE generates the meshes. For the meshed
        instances, Abaqus/CAE changes the node and/or element labels while preserving the
        original order and incrementation.

        Parameters
        ----------
        instances
            A sequence of PartInstance objects to change the start node and/or element labels.
        startNodeLabel
            A positive Integer specifying the new start node label.
        startElemLabel
            A positive Integer specifying the new start element label.
        """
        ...

    @abaqus_method_doc
    def copyMeshPattern(
        self,
        elements: Sequence[MeshElement] = (),
        faces: Sequence[Face] = (),
        elemFaces: Sequence[MeshFace] = (),
        targetFace: Optional[MeshFace] = None,
        nodes: Sequence[MeshNode] = (),
        coordinates: tuple = (),
    ):
        """This method copies a mesh pattern from a source region consisting of a set of shell
        elements or element faces onto a target face, mapping nodes and elements in a one-one
        correspondence between source and target.

        Parameters
        ----------
        elements
            A sequence of MeshElement objects or a Set object containing elements and specifying the
            source region.
        faces
            A sequence of Face objects that have associated with shell elements or element faces and
            specifying the source region.
        elemFaces
            A sequence of MeshFace objects specifying the source region.
        targetFace
            A :py:class:`~abaqus.Mesh.MeshFace.MeshFace` object specifying the target region. The target face can be of a different
            part instance.
        nodes
            A sequence of MeshNode objects or a Set object containing nodes on the boundary of
            source region which are to be positioned to the boundary of target face.
        coordinates
            A sequence of three-dimensional coordinate tuples specifying the coordinates for each of
            the given nodes. When specified, the number of coordinate tuples must match the number
            of given nodes, and be ordered to correspond to the given nodes in *ascending order*
            according to index. These coordinates are positions of the nodes of a mesh that will be
            the target face corresponding to nodes provided.
        """
        ...

    @abaqus_method_doc
    def smoothNodes(self, nodes: Sequence[MeshNode] = ()):
        """This method smooths the given nodes of a native mesh, moving them locally to a more
        optimal location that improves the quality of the mesh

        Parameters
        ----------
        nodes
            A sequence of MeshNode objects or a Set object containing nodes.
        """
        ...
