import typing

from abaqusConstants import *
from .InteractionContactControlModel import InteractionContactControlModel
from .InteractionContactInitializationModel import InteractionContactInitializationModel
from .InteractionPropertyModel import InteractionPropertyModel
from ..BasicGeometry.ModelDot import ModelDot
from ..Datum.DatumAxis import DatumAxis
from ..Interaction.AcousticImpedance import AcousticImpedance
from ..Interaction.AcousticImpedanceProp import AcousticImpedanceProp
from ..Interaction.ActuatorSensor import ActuatorSensor
from ..Interaction.ActuatorSensorProp import ActuatorSensorProp
from ..Interaction.CavityRadiation import CavityRadiation
from ..Interaction.CavityRadiationProp import CavityRadiationProp
from ..Interaction.ConcentratedFilmCondition import ConcentratedFilmCondition
from ..Interaction.ConcentratedRadiationToAmbient import ConcentratedRadiationToAmbient
from ..Interaction.ContactExp import ContactExp
from ..Interaction.ContactProperty import ContactProperty
from ..Interaction.ContactPropertyAssignment import ContactPropertyAssignment
from ..Interaction.ContactStd import ContactStd
from ..Interaction.CyclicSymmetry import CyclicSymmetry
from ..Interaction.ElasticFoundation import ElasticFoundation
from ..Interaction.ExpContactControl import ExpContactControl
from ..Interaction.FilmCondition import FilmCondition
from ..Interaction.FilmConditionProp import FilmConditionProp
from ..Interaction.FluidCavity import FluidCavity
from ..Interaction.FluidCavityProperty import FluidCavityProperty
from ..Interaction.FluidExchange import FluidExchange
from ..Interaction.FluidExchangeProperty import FluidExchangeProperty
from ..Interaction.IncidentWave import IncidentWave
from ..Interaction.IncidentWaveProperty import IncidentWaveProperty
from ..Interaction.InitializationAssignment import InitializationAssignment
from ..Interaction.MainSecondaryAssignment import MainSecondaryAssignment
from ..Interaction.ModelChange import ModelChange
from ..Interaction.PressurePenetration import PressurePenetration
from ..Interaction.RadiationToAmbient import RadiationToAmbient
from ..Interaction.RegionPairs import RegionPairs
from ..Interaction.SelfContactExp import SelfContactExp
from ..Interaction.SelfContactStd import SelfContactStd
from ..Interaction.SlidingTransitionAssignment import SlidingTransitionAssignment
from ..Interaction.SmoothingAssignment import SmoothingAssignment
from ..Interaction.StabilizationAssignment import StabilizationAssignment
from ..Interaction.StdContactControl import StdContactControl
from ..Interaction.StdInitialization import StdInitialization
from ..Interaction.StdStabilization import StdStabilization
from ..Interaction.StdXplCosimulation import StdXplCosimulation
from ..Interaction.SurfaceFeatureAssignment import SurfaceFeatureAssignment
from ..Interaction.SurfaceOffsetAssignment import SurfaceOffsetAssignment
from ..Interaction.SurfaceThicknessAssignment import SurfaceThicknessAssignment
from ..Interaction.SurfaceToSurfaceContactExp import SurfaceToSurfaceContactExp
from ..Interaction.SurfaceToSurfaceContactStd import SurfaceToSurfaceContactStd
from ..Interaction.XFEMCrackGrowth import XFEMCrackGrowth
from ..Region.Region import Region
from ..Region.RegionArray import RegionArray


class InteractionModel(
    InteractionContactControlModel,
    InteractionContactInitializationModel,
    InteractionPropertyModel,
):
    """Abaqus creates a Model object named `Model-1` when a session is started.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            mdb.models[name]
    """

    def contactDetection(
        self,
        name: str = "",
        createStepName: str = "",
        searchDomain: SymbolicConstant = MODEL,
        defaultType: SymbolicConstant = CONTACT,
        interactionProperty: str = "",
        separationTolerance: float = None,
        extendByAngle: float = 20,
        mergeWithinAngle: float = 20,
        searchSingleInstances: Boolean = OFF,
        nameEachSurfaceFound: Boolean = ON,
        createUnionOfMainSurfaces: Boolean = OFF,
        createUnionOfSecondarySurfaces: Boolean = OFF,
        createUnionOfMainSecondarySurfaces: Boolean = OFF,
        includePlanar: Boolean = ON,
        includeCylindricalSphericalToric: Boolean = ON,
        includeSplineBased: Boolean = ON,
        includeMeshSolid: Boolean = ON,
        includeMeshShell: Boolean = ON,
        includeMeshMembrane: Boolean = OFF,
        includeOverclosed: Boolean = ON,
        includeNonOverlapping: Boolean = OFF,
        meshedGeometrySearchTechnique: SymbolicConstant = USE_GEOMETRY,
        useShellThickness: Boolean = ON,
        surfaceSmoothing: SymbolicConstant = None,
    ):
        """This method uses contact detection to create SurfaceToSurfaceContactStd,
        SurfaceToSurfaceContactExp, and Tie objects.

        Parameters
        ----------
        name
            A String specifying the prefix used to generate repository keys. The default value is
            "CP-"
        createStepName
            A String specifying the name of the step in which the SurfaceToSurfaceContactStd,
            SurfaceToSurfaceContactExp, and Tie objects are created. The default value is "Initial."
        searchDomain
            A SymbolicConstant MODEL or a sequence of Strings specifying the names of instances to
            search. MODEL indicates the whole model is searched. The default value is MODEL.
        defaultType
            A SymbolicConstant specifying the default type of object to create. Possible values are
            CONTACT, CONTACT_STANDARD, CONTACT_EXPLICIT, and TIE. If CONTACT is used, the behavior
            is determined by the type of Step in the model. If an ExplicitDynamicsStep or
            TempDisplacementDynamicsStep exists, then SurfaceToSurfaceContactExp is created by
            default. Otherwise SurfaceToSurfaceContactStd is created by default. The default value
            is CONTACT.
        interactionProperty
            A String specifying the name of the ContactProperty object associated with any
            interactions created.
        separationTolerance
            A Float specifying the maximum separation for considering two surfaces to be candidates
            for contact, where separation is the maximum distance between the points of closest
            approach on the two surfaces. The default value is a function of the model.
        extendByAngle
            None or a Float specifying the angle for extending surface definitions to include
            adjacent faces. The default value is 20.
        mergeWithinAngle
            None or a Float specifying the angle for merging adjacent contact pairs that lie within
            the angle. The default value is 20.
        searchSingleInstances
            A Boolean specifying whether to include surface pairs within a single instance. The
            default value is OFF.
        nameEachSurfaceFound
            A Boolean specifying whether to assign a name to each surface found. The default value
            is ON.
        createUnionOfMainSurfaces
            A Boolean specifying whether to create a surface that is the union of all main surfaces
            found. The default value is OFF.
        createUnionOfSecondarySurfaces
            A Boolean specifying whether to create a surface that is the union of all secondary
            surfaces found. The default value is OFF.
        createUnionOfMainSecondarySurfaces
            A Boolean specifying whether to create a surface that is the union of all main and
            secondary surfaces found. The default value is OFF.
        includePlanar
            A Boolean specifying whether to include planar geometry. The default value is ON.
        includeCylindricalSphericalToric
            A Boolean specifying whether to include cylindrical, spherical, and toric geometry. The
            default value is ON.
        includeSplineBased
            A Boolean specifying whether to include spline-based geometry. The default value is ON.
        includeMeshSolid
            A Boolean specifying whether to include solid mesh entities. The default value is ON.
        includeMeshShell
            A Boolean specifying whether to include shell mesh entities. The default value is ON.
        includeMeshMembrane
            A Boolean specifying whether to include mesh membrane entities. The default value is
            OFF.
        includeOverclosed
            A Boolean specifying whether to include overclosed pairs. The default value is ON.
        includeNonOverlapping
            A Boolean specifying whether to include opposing geometry surfaces that do not overlap.
            The default value is OFF.
        meshedGeometrySearchTechnique
            A SymbolicConstant USE_GEOMETRY or USE_MESH specifying whether to locate pairs in meshed
            geometry using the geometric entities or mesh entities. The default value is
            USE_GEOMETRY.
        useShellThickness
            A Boolean specifying whether to account for shell thickness and offset during contact
            detection. The default value is ON.
        surfaceSmoothing
            A SymbolicConstant specifying whether to use surface smoothing for geometric surfaces in
            SurfaceToSurfaceContactStd interactions. Possible values are NONE and AUTOMATIC. The
            default value isAUTOMATIC.

        Returns
        -------
        None.
        """
        pass

    def getSurfaceSeparation(self):
        """This method returns a list of all possible contacts that can be created using the
        ContactDetection method.

        Returns
        -------
        Tuple of tuples, where each tuple holds information, to be used in contact creation as
        follows:
        
        - A string specifying the name of the main surface used in contact.
        - A string specifying the name of the secondary surface used in contact.
        - A float specifying the separation distance between the main surface and the secondary
          surface.
        - A boolean specifying whether or not contact surfaces are overclosed..
        """
        pass

    def AcousticImpedance(
        self,
        name: str,
        createStepName: str,
        surface: Region,
        definition: SymbolicConstant = TABULAR,
        interactionProperty: str = "",
        nonreflectingType: SymbolicConstant = PLANE,
        radius: float = 1,
        semimajorAxis: float = 1,
        eccentricity: float = 0,
        centerCoordinates: tuple = (),
        directionCosine: tuple = (),
    ) -> AcousticImpedance:
        """This method creates an AcousticImpedance object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].AcousticImpedance

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the AcousticImpedance object is
            created.
        surface
            A :py:class:`~abaqus.Region.Region.Region` object specifying the acoustic boundary surface.
        definition
            A SymbolicConstant specifying the type of acoustic impedance to be defined. Possible
            values are TABULAR and NONREFLECTING. The default value is TABULAR.
        interactionProperty
            A String specifying the AcousticImpedanceProp object associated with this interaction.
        nonreflectingType
            A SymbolicConstant specifying the type of nonreflecting geometry to be defined. Possible
            values are PLANE, IMPROVED, CIRCULAR, SPHERICAL, ELLIPTICAL, and PROLATE. The default
            value is PLANE.This argument is valid only when **definition** = NONREFLECTING.
        radius
            A Float specifying the radius of the circle or sphere defining the boundary surface. The
            default value is 1.0.This argument is valid only when **definition** = NONREFLECTING, and
            **nonreflectingType** = CIRCULAR or SPHERICAL.
        semimajorAxis
            A Float specifying the semimajor axis length of the ellipse or prolate spheroid defining
            the boundary surface. The default value is 1.0.This argument is valid only when
            **definition** = NONREFLECTING, and **nonreflectingType** = ELLIPTICAL or PROLATE.
        eccentricity
            A Float specifying the eccentricity of the ellipse or prolate spheroid defining the
            boundary surface. The default value is 0.0.This argument is valid only when
            **definition** = NONREFLECTING, and **nonreflectingType** = ELLIPTICAL or PROLATE.
        centerCoordinates
            A sequence of three Floats specifying the X, Y, and Z coordinates of the center of the
            ellipse or prolate spheroid defining the boundary surface. The default value is (0, 0,
            0).This argument is valid only when **definition** = NONREFLECTING, and
            **nonreflectingType** = ELLIPTICAL or PROLATE.
        directionCosine
            A sequence of three Floats specifying the X, Y, and Z components of the direction cosine
            of the major axis of the ellipse or prolate spheroid defining the boundary surface. The
            default value is (0, 0, 1).This argument is valid only when **definition** = NONREFLECTING,
            and **nonreflectingType** = ELLIPTICAL or PROLATE.

        Returns
        -------
        AcousticImpedance
            An :py:class:`~abaqus.Interaction.AcousticImpedance.AcousticImpedance` object.
        """
        self.interactions[name] = interaction = AcousticImpedance(
            name,
            createStepName,
            surface,
            definition,
            interactionProperty,
            nonreflectingType,
            radius,
            semimajorAxis,
            eccentricity,
            centerCoordinates,
            directionCosine,
        )
        return interaction

    def AcousticImpedanceProp(
        self,
        name: str,
        tableType: SymbolicConstant,
        table: tuple,
        frequencyDependency: Boolean = OFF,
    ) -> AcousticImpedanceProp:
        """This method creates an AcousticImpedanceProp object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].AcousticImpedanceProp

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.
        tableType
            A SymbolicConstant specifying the type of tabular data to be defined. Possible values
            are IMPEDANCE and ADMITTANCE.
        table
            A sequence of sequences of Floats specifying acoustic impedance properties.If
            **tableType** = IMPEDANCE, each sequence of the table data specifies:The real part of the
            complex impedance.The imaginary part of the complex impedance.Frequency, if the data
            depend on frequency.If **tableType** = ADMITTANCE, each sequence of the table data
            specifies:The real part of the complex admittance.The imaginary part of the complex
            admittance.Frequency, if the data depend on frequency.
        frequencyDependency
            A Boolean specifying whether the **table** data depend on frequency. The default value is
            OFF.

        Returns
        -------
        AcousticImpedanceProp
            An :py:class:`~abaqus.Interaction.AcousticImpedanceProp.AcousticImpedanceProp` object.
        """
        self.interactions[name] = interaction = AcousticImpedanceProp(
            name, tableType, table, frequencyDependency
        )
        return interaction

    def ActuatorSensor(
        self,
        name: str,
        createStepName: str,
        point: Region,
        interactionProperty: str,
        noCoordComponents: int,
        unsymm: Boolean,
        noSolutionDepVar: int,
        userSubUel: str,
        dof: str,
        solutionDepVars: tuple,
    ) -> ActuatorSensor:
        """This method creates an ActuatorSensor object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].ActuatorSensor

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the actuator/sensor interaction is
            created. **createStepName** must be set to 'Initial'.
        point
            A :py:class:`~abaqus.Region.Region.Region` object specifying the point at which the constraint is applied.
        interactionProperty
            A String specifying the ActuatorSensorProp object associated with this interaction.
        noCoordComponents
            An Int specifying the number of coordinate components supplied to the user subroutine
            (UEL).
        unsymm
            A Boolean specifying whether the element matrices are symmetric (ON) or unsymmetric
            (OFF). The default value is OFF.
        noSolutionDepVar
            An Int specifying the number of solution-dependent variables. The default value is 0.
        userSubUel
            A String specifying the name of the user subroutine (UEL) that defines the user element.
        dof
            A String specifying the degrees of freedom, separated by commas.
        solutionDepVars
            A sequence of Floats specifying the initial values of the solution-dependent variables.

        Returns
        -------
        ActuatorSensor
            An :py:class:`~abaqus.Interaction.ActuatorSensor.ActuatorSensor` object.
        """
        self.interactions[name] = interaction = ActuatorSensor(
            name,
            createStepName,
            point,
            interactionProperty,
            noCoordComponents,
            unsymm,
            noSolutionDepVar,
            userSubUel,
            dof,
            solutionDepVars,
        )
        return interaction

    def ActuatorSensorProp(
        self, name: str, realProperties: tuple = (), integerProperties: tuple = ()
    ) -> ActuatorSensorProp:
        """This method creates an ActuatorSensorProp object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].ActuatorSensorProp

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.
        realProperties
            A sequence of Floats specifying the PROPS array used by user subroutine UEL. The default
            value is an empty sequence.
        integerProperties
            A sequence of Ints specifying the JPROPS array used by user subroutine UEL. The default
            value is an empty sequence.

        Returns
        -------
        ActuatorSensorProp
            An :py:class:`~abaqus.Interaction.ActuatorSensorProp.ActuatorSensorProp` object.
        """
        self.interactions[name] = interaction = ActuatorSensorProp(
            name, realProperties, integerProperties
        )
        return interaction

    def CavityRadiation(
        self,
        name: str,
        createStepName: str,
        surfaces: RegionArray,
        surfaceEmissivities: tuple = (),
        ambientTemp: float = None,
        blocking: SymbolicConstant = BLOCKING_ALL,
        blockingSurfaces: RegionArray = None,
        rangeOfView: float = None,
        surfaceReflection: Boolean = ON,
        viewfactorAccurTol: float = 0,
        minInfinitesimalRatio: float = 64,
        numPointsPerEdge: int = 3,
        minLumpedAreaDS: float = 5,
        cyclicSymmetry: Boolean = OFF,
        cyclicImages: int = 2,
        cyclicRotPt: ModelDot = None, 
        cyclicRotEndPt: ModelDot = None, 
        cyclicSymPt: ModelDot = None, 
        periodicSymmetries: int = 0,
        periodicImages_1: int = 2,
        periodicImages_2: int = 2,
        periodicImages_3: int = 2,
        periodicSymAxis_1: str = "",
        periodicSymAxis_2: str = "",
        periodicSymPlane_1: str = "",
        periodicSymPlane_2: str = "",
        periodicSymPlane_3: str = "",
        periodicDistance_1: tuple = (),
        periodicDistance_2: tuple = (),
        periodicDistance_3: tuple = (),
        periodicSymZ: float = None,
        periodicDistZ: float = None,
        reflectionSymmetries: int = 0,
        reflectionSymAxis_1: str = "",
        reflectionSymAxis_2: str = "",
        reflectionSymPlane_1: str = "",
        reflectionSymPlane_2: str = "",
        reflectionSymPlane_3: str = "",
        reflectionSymZ: float = None,
    ) -> CavityRadiation:
        """This method creates a CavityRadiation object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].CavityRadiation

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the cavity radiation interaction
            should be created.
        surfaces
            A :py:class:`~abaqus.Region.RegionArray.RegionArray` object specifying the surfaces for which radiation viewfactor control is
            being specified.
        surfaceEmissivities
            A sequence of Strings specifying the names of the Cavity Radiation properties containing
            the surface emissivity data. One name per specified surface. The emissivity data is
            ignored when **surfaceReflection** = OFF.
        ambientTemp
            None or a Float specifying the reference ambient temperature value, θ0θ0. Specifying a
            value indicates an open cavity. The default value is None.
        blocking
            A SymbolicConstant specifying the blocking checks to be performed in the viewfactor
            calculations. Possible values are BLOCKING_ALL, NO_BLOCKING, and PARTIAL_BLOCKING. The
            default value is BLOCKING_ALL.
        blockingSurfaces
            A :py:class:`~abaqus.Region.RegionArray.RegionArray` object specifying the surfaces that provide blocking inside the cavity.
            This argument applies only when **blocking** = PARTIAL_BLOCKING.
        rangeOfView
            None or a Float specifying the maximum distance between surface facets at which
            viewfactors are calculated. More distant facets are deemed too far apart to exchange
            significant amounts of heat through radiation effects, and the viewfactors between these
            facets are assumed to be zero. If **rangeOfView** = None, there is no upper limit. The
            default value is None.
        surfaceReflection
            A Boolean specifying whether heat reflections are to be included in the cavity radiation
            calculations. The default value is ON.
        viewfactorAccurTol
            A Float specifying the acceptable tolerance for the viewfactor calculations. The default
            value is 0.05.
        minInfinitesimalRatio
            A Float specifying the facet area ratio above which the infinitesimal-to-finite area
            approximation is used for viewfactor calculations. The default value is 64.0.
        numPointsPerEdge
            An Int specifying the number of Gauss integration points to be used along each edge when
            the numerical integration of contour integrals is used for viewfactor calculations. One
            to five integration points are allowed. The default value is 3.
        minLumpedAreaDS
            A Float specifying the nondimensional distance-square value above which the lumped area
            approximation is used for viewfactor calculations. The default value is 5.0.
        cyclicSymmetry
            A Boolean specifying whether cyclic symmetry will be applied. This argument cannot be
            specified for axisymmetric models. The default value is OFF.
        cyclicImages
            An Int specifying the number of cyclically similar images that compose the cavity formed
            as a result of this symmetry. This argument applies only when **cyclicSymmetry** = ON. The
            default value is 2.
        cyclicRotPt
            A :py:class:`~abaqus.BasicGeometry.ModelDot.ModelDot` object specifying the rotation axis point. This argument applies only when
            **cyclicSymmetry** = ON.
        cyclicRotEndPt
            A :py:class:`~abaqus.BasicGeometry.ModelDot.ModelDot` object specifying the rotation axis end point. This argument applies only for
            three-dimensional models, and only when **cyclicSymmetry** = ON.
        cyclicSymPt
            A :py:class:`~abaqus.BasicGeometry.ModelDot.ModelDot` object specifying the symmetry axis end point. This argument applies only
            when **cyclicSymmetry** = ON.
        periodicSymmetries
            An Int specifying the number of periodic symmetries that will be applied. The default
            value is 0.
        periodicImages_1
            An Int specifying the number of repetitions used in the numerical calculation of the
            cavity viewfactors resulting from the first periodic symmetry. The result of this
            symmetry is a cavity composed of the cavity surface defined in the model plus twice the
            value of **periodicImages_1**. This argument applies only when **periodicSymmetries** is
            greater than zero. The default value is 2.
        periodicImages_2
            An Int specifying the number of repetitions used in the numerical calculation of the
            cavity viewfactors resulting from the second periodic symmetry. The result of this
            symmetry is a cavity composed of the cavity surface defined in the model plus twice the
            value of **periodicImages_2**. This argument applies only when **periodicSymmetries** is
            greater than one. The default value is 2.
        periodicImages_3
            An Int specifying the number of repetitions used in the numerical calculation of the
            cavity viewfactors resulting from the third periodic symmetry. The result of this
            symmetry is a cavity composed of the cavity surface defined in the model plus twice the
            value of **periodicImages_3**. This argument applies only when **periodicSymmetries** = 3.
            The default value is 2.
        periodicSymAxis_1
            A straight Edge, a Datum object representing a datum axis, or an ElementEdge object
            indicating the first line of symmetry in two-dimensional models. This argument applies
            only for 2D models, and when **periodicSymmetries** is greater than zero.
        periodicSymAxis_2
            A straight Edge, a Datum object representing a datum axis, or an ElementEdge object
            indicating the second line of symmetry in two-dimensional models. This argument applies
            only for two-dimensional models, and when **periodicSymmetries** = 2.
        periodicSymPlane_1
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating
            the first plane of symmetry in three-dimensional models. This argument applies only for
            three-dimensional models, and when **periodicSymmetries** is greater than zero.
        periodicSymPlane_2
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating
            the second plane of symmetry in three-dimensional models. This argument applies only for
            three-dimensional models, and when **periodicSymmetries** is greater than one.
        periodicSymPlane_3
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating
            the third plane of symmetry in three-dimensional models. This argument applies only for
            three-dimensional models, and when **periodicSymmetries** = 3.
        periodicDistance_1
            A sequence of sequences of Floats specifying the two points of the vector that describes
            the periodic distance for the first periodic symmetry. Each point is defined by a tuple
            of three coordinates indicating its position. This argument applies only when
            **periodicSymmetries** is greater than zero. The default value is an empty sequence.
        periodicDistance_2
            A sequence of sequences of Floats specifying the two points of the vector that describes
            the periodic distance for the second periodic symmetry. Each point is defined by a tuple
            of three coordinates indicating its position. This argument applies only when
            **periodicSymmetries** is greater than one. The default value is an empty sequence.
        periodicDistance_3
            A sequence of sequences of Floats specifying the two points of the vector that describes
            the periodic distance for the third periodic symmetry. Each point is defined by a tuple
            of three coordinates indicating its position. This argument applies only when
            **periodicSymmetries** = 3. The default value is an empty sequence.
        periodicSymZ
            None or a Float specifying the Z value indicating the symmetry reference line in
            axisymmetric models. This argument applies only for axisymmetric models, and when
            **periodicSymmetries** = 1. The default value is None.
        periodicDistZ
            None or a Float specifying the Z value indicating the periodic distance in axisymmetric
            models. This argument applies only for axisymmetric models, and when
            **periodicSymmetries** = 1. The default value is None.
        reflectionSymmetries
            An Int specifying the number of reflection symmetries will be applied. The default value
            is 0.
        reflectionSymAxis_1
            A straight Edge, a Datum object representing a datum axis, or an ElementEdge object
            indicating the first line of symmetry in two-dimensional models. This argument applies
            only for two-dimensional models, and when **reflectionSymmetries** is greater than zero.
        reflectionSymAxis_2
            A straight Edge, a Datum object representing a datum axis, or an ElementEdge object
            indicating the second line of symmetry in two-dimensional models. This argument applies
            only for two-dimensional models, and when **reflectionSymmetries** = 2.
        reflectionSymPlane_1
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating
            the first plane of symmetry in three-dimensional models. This argument applies only for
            three-dimensional models, and when **reflectionSymmetries** is greater than zero.
        reflectionSymPlane_2
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating
            the second plane of symmetry in three-dimensional models. This argument applies only for
            three-dimensional models, and when **reflectionSymmetries** is greater than one.
        reflectionSymPlane_3
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating
            the third plane of symmetry in three-dimensional models. This argument applies only for
            three-dimensional models, and when **reflectionSymmetries** = 3.
        reflectionSymZ
            None or a Float specifying the Z value indicating the symmetry reference line in
            axisymmetric models. This argument applies only for axisymmetric models, and when
            **reflectionSymmetries** = 1. The default value is None.

        Returns
        -------
        CavityRadiation
            A :py:class:`~abaqus.Interaction.CavityRadiation.CavityRadiation` object.
        """
        self.interactions[name] = interaction = CavityRadiation(
            name,
            createStepName,
            surfaces,
            surfaceEmissivities,
            ambientTemp,
            blocking,
            blockingSurfaces,
            rangeOfView,
            surfaceReflection,
            viewfactorAccurTol,
            minInfinitesimalRatio,
            numPointsPerEdge,
            minLumpedAreaDS,
            cyclicSymmetry,
            cyclicImages,
            cyclicRotPt,
            cyclicRotEndPt,
            cyclicSymPt,
            periodicSymmetries,
            periodicImages_1,
            periodicImages_2,
            periodicImages_3,
            periodicSymAxis_1,
            periodicSymAxis_2,
            periodicSymPlane_1,
            periodicSymPlane_2,
            periodicSymPlane_3,
            periodicDistance_1,
            periodicDistance_2,
            periodicDistance_3,
            periodicSymZ,
            periodicDistZ,
            reflectionSymmetries,
            reflectionSymAxis_1,
            reflectionSymAxis_2,
            reflectionSymPlane_1,
            reflectionSymPlane_2,
            reflectionSymPlane_3,
            reflectionSymZ,
        )
        return interaction

    def CavityRadiationProp(
        self,
        name: str,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        property: tuple = (),
    ) -> CavityRadiationProp:
        """This method creates a CavityRadiationProp object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].CavityRadiationProp

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        property
            A sequence of sequences of Floats specifying the following:The emissivity,
            ϵϵ.Temperature, if the data depend on temperature.Value of the first field variable, if
            the data depend on field variables.Value of the second field variable.Etc.

        Returns
        -------
        CavityRadiationProp
            A :py:class:`~abaqus.Interaction.CavityRadiationProp.CavityRadiationProp` object.
        """
        self.interactions[name] = interaction = CavityRadiationProp(
            name, temperatureDependency, dependencies, property
        )
        return interaction

    def ConcentratedFilmCondition(
        self,
        name: str,
        createStepName: str,
        region: Region,
        definition: SymbolicConstant,
        nodalArea: float = 1,
        explicitRegionType: SymbolicConstant = LAGRANGIAN,
        interactionProperty: str = "",
        field: str = "",
        sinkTemperature: float = 0,
        sinkAmplitude: str = "",
        filmCoeff: float = 0,
        filmCoeffAmplitude: str = "",
        sinkFieldName: str = "",
        sinkDistributionType: SymbolicConstant = UNIFORM,
    ) -> ConcentratedFilmCondition:
        """This method creates a ConcentratedFilmCondition object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].ConcentratedFilmCondition

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the ConcentratedFilmCondition object
            is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the concentrated film condition
            interaction is applied. The interaction is applied to each node in the region.
        definition
            A SymbolicConstant specifying how the concentrated film condition is defined. Possible
            values are EMBEDDED_COEFF, PROPERTY_REF, USER_SUB, and FIELD.
        nodalArea
            A Float specifying the area associated with the node where the concentrated film
            condition is applied. The default value is 1.0.
        explicitRegionType
            A SymbolicConstant specifying how the concentrated film condition is applied to the
            boundary of an adaptive mesh domain. Possible values are LAGRANGIAN, SLIDING, and
            EULERIAN. The default value is LAGRANGIAN. This argument applies only during an
            Abaqus/Explicit analysis.
        interactionProperty
            A String specifying the name of the FilmConditionProp object associated with this
            interaction. The **interactionProperty** argument applies only when
            **definition** = PROPERTY_REF. The default value is an empty string.
        field
            A String specifying the name of the AnalyticalField object associated with this
            interaction. The **field** argument applies only when **definition** = FIELD. The default
            value is an empty string.
        sinkTemperature
            A Float specifying the reference sink temperature, θ0θ0. The default value is 0.0.
        sinkAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the
            sink temperature, θ0θ0, with time. The default value is an empty string.Note:Use None in
            an Abaqus/Standard analysis to specify that the reference sink temperature is applied
            immediately at the beginning of the step or linearly over the step. Use None in an
            Abaqus/Explicit analysis to specify that the reference sink temperature is applied
            throughout the step.
        filmCoeff
            A Float specifying the reference film coefficient value, hh. The **filmCoeff** argument
            applies when **definition** = EMBEDDED_COEFF, **definition** = USER_SUB, or **definition** = FIELD.
            The default value is 0.0.
        filmCoeffAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the
            film coefficient, hh, with time. The default value is an empty string.Note:Use None in
            an Abaqus/Standard analysis to specify that the reference film coefficient is applied
            immediately at the beginning of the step or linearly over the step. Use None in an
            Abaqus/Explicit analysis to specify that the reference film coefficient is applied
            throughout the step.
        sinkFieldName
            A String specifying the name of the AnalyticalField or DiscreteField object associated
            with the sink temperature. The **sinkFieldName** argument applies only when
            **sinkDistributionType** = ANALYTICAL_FIELD or **sinkDistributionType** = DISCRETE_FIELD. The
            default value is an empty string.
        sinkDistributionType
            A SymbolicConstant specifying how the sink temperature is distributed. Possible values
            are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM.

        Returns
        -------
        ConcentratedFilmCondition
            A :py:class:`~abaqus.Interaction.ConcentratedFilmCondition.ConcentratedFilmCondition` object.
        """
        self.interactions[name] = interaction = ConcentratedFilmCondition(
            name,
            createStepName,
            region,
            definition,
            nodalArea,
            explicitRegionType,
            interactionProperty,
            field,
            sinkTemperature,
            sinkAmplitude,
            filmCoeff,
            filmCoeffAmplitude,
            sinkFieldName,
            sinkDistributionType,
        )
        return interaction

    def ConcentratedRadiationToAmbient(
        self,
        name: str,
        createStepName: str,
        region: Region,
        ambientTemperature: float,
        ambientTemperatureAmp: str,
        emissivity: float,
        nodalArea: float = 1,
        explicitRegionType: SymbolicConstant = LAGRANGIAN,
        field: str = "",
        distributionType: SymbolicConstant = UNIFORM,
    ) -> ConcentratedRadiationToAmbient:
        """This method creates a ConcentratedRadiationToAmbient object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].ConcentratedRadiationToAmbient

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the ConcentratedRadiationToAmbient
            object is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the concentrated radiation interaction is
            applied. The interaction is applied to each node in the region.
        ambientTemperature
            A Float specifying the reference ambient temperature, θ0θ0.
        ambientTemperatureAmp
            A String specifying the name of the Amplitude object that gives the variation of the
            ambient temperature with time.Note:Use None in an Abaqus/Standard analysis to specify
            that the reference ambient temperature is applied immediately at the beginning of the
            step or linearly over the step. Use None in an Abaqus/Explicit analysis to specify that
            the reference ambient temperature is applied throughout the step.
        emissivity
            A Float specifying the emissivity, ϵϵ.
        nodalArea
            A Float specifying the area associated with the node where the concentrated radiation
            interaction is applied. The default value is 1.0.
        explicitRegionType
            A SymbolicConstant specifying how the concentrated radiation is applied to the boundary
            of an adaptive mesh domain. Possible values are LAGRANGIAN, SLIDING, and EULERIAN. The
            default value is LAGRANGIAN.Note:*explicitRegionType* applies only during an
            Abaqus/Explicit analysis.
        field
            A String specifying the name of the AnalyticalField object associated with this
            interaction. The **field** argument applies only when **distributionType** = ANALYTICAL_FIELD.
            The default value is an empty string.
        distributionType
            A SymbolicConstant specifying how the radiation is defined. Possible values are UNIFORM
            and ANALYTICAL_FIELD. The default value is UNIFORM.

        Returns
        -------
        ConcentratedRadiationToAmbient
            A :py:class:`~abaqus.Interaction.ConcentratedRadiationToAmbient.ConcentratedRadiationToAmbient` object.
        """
        self.interactions[name] = interaction = ConcentratedRadiationToAmbient(
            name,
            createStepName,
            region,
            ambientTemperature,
            ambientTemperatureAmp,
            emissivity,
            nodalArea,
            explicitRegionType,
            field,
            distributionType,
        )
        return interaction

    def ContactExp(
        self,
        name: str,
        createStepName: str,
        useAllstar: Boolean = OFF,
        globalSmoothing: Boolean = ON,
        includedPairs: RegionPairs = None, 
        excludedPairs: RegionPairs = None, 
        contactPropertyAssignments: ContactPropertyAssignment = None, 
        surfaceThicknessAssignments: SurfaceThicknessAssignment = None, 
        surfaceOffsetAssignments: SurfaceOffsetAssignment = None, 
        surfaceFeatureAssignments: SurfaceFeatureAssignment = None, 
        smoothingAssignments: SmoothingAssignment = None, 
        mainSecondaryAssignments: MainSecondaryAssignment = None, 
    ):
        """This method creates a ContactExp object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].ContactExp

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which this contact interaction is created.
        useAllstar
            A Boolean specifying whether the contacting surface pair consists of all exterior faces,
            shell edges, beam segments, analytical rigid surfaces, and, when applicable, Eulerian
            material surfaces.
        globalSmoothing
            A Boolean specifying whether surface smoothing (geometric correction) is automatically
            applied to all eligible surfaces. The default value is ON.
        includedPairs
            A :py:class:`~abaqus.Interaction.RegionPairs.RegionPairs` object specifying the domain pairs included in contact.
        excludedPairs
            A :py:class:`~abaqus.Interaction.RegionPairs.RegionPairs` object specifying the domain pairs excluded from contact.
        contactPropertyAssignments
            A :py:class:`~abaqus.Interaction.ContactPropertyAssignment.ContactPropertyAssignment` object specifying the contact property assignments in the
            contact domain.
        surfaceThicknessAssignments
            A :py:class:`~abaqus.Interaction.SurfaceThicknessAssignment.SurfaceThicknessAssignment` object specifying the surface thickness assignments in the
            contact domain.
        surfaceOffsetAssignments
            A :py:class:`~abaqus.Interaction.SurfaceOffsetAssignment.SurfaceOffsetAssignment` object specifying the surface offset fraction assignments in
            the contact domain.
        surfaceFeatureAssignments
            A :py:class:`~abaqus.Interaction.SurfaceFeatureAssignment.SurfaceFeatureAssignment` object specifying the surface feature angle assignments in
            the contact domain.
        smoothingAssignments
            A :py:class:`~abaqus.Interaction.SmoothingAssignment.SmoothingAssignment` object specifying the surface smoothing assignments in the contact
            domain.
        mainSecondaryAssignments
            A :py:class:`~abaqus.Interaction.MainSecondaryAssignment.MainSecondaryAssignment` object specifying the main-secondary assignments in the
            contact domain.

        Returns
        -------
        ContactExp
            A :py:class:`~abaqus.Interaction.ContactExp.ContactExp` object.
        """
        self.interactions[name] = interaction = ContactExp(
            name,
            createStepName,
            useAllstar,
            globalSmoothing,
            includedPairs,
            excludedPairs,
            contactPropertyAssignments,
            surfaceThicknessAssignments,
            surfaceOffsetAssignments,
            surfaceFeatureAssignments,
            smoothingAssignments,
            mainSecondaryAssignments,
        )
        return interaction

    def ContactProperty(self, name: str) -> ContactProperty:
        """This method creates a ContactProperty object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].ContactProperty

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.

        Returns
        -------
        ContactProperty
            A :py:class:`~abaqus.Interaction.ContactProperty.ContactProperty` object.
        """
        interactionProperties = ContactProperty(name)
        self.interactions[name] = interactionProperties
        self.interactionProperties[name] = interactionProperties
        return interactionProperties

    def ContactStd(
        self,
        name: str,
        createStepName: str,
        useAllstar: Boolean = OFF,
        globalSmoothing: Boolean = ON,
        includedPairs: RegionPairs = None, 
        excludedPairs: RegionPairs = None, 
        contactPropertyAssignments: ContactPropertyAssignment = None, 
        surfaceThicknessAssignments: SurfaceThicknessAssignment = None, 
        surfaceOffsetAssignments: SurfaceOffsetAssignment = None, 
        surfaceFeatureAssignments: SurfaceFeatureAssignment = None, 
        mainSecondaryAssignments: MainSecondaryAssignment = None, 
        initializationAssignments: InitializationAssignment = None, 
        stabilizationAssignments: StabilizationAssignment = None, 
        smoothingAssignments: SmoothingAssignment = None, 
        slidingTransitionAssignments: SlidingTransitionAssignment = None, 
    ) -> ContactStd:
        """This method creates a ContactStd object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].ContactStd

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which this contact interaction is created.
        useAllstar
            A Boolean specifying whether the contacting surface pairs consist of all exterior faces
            in the model.
        globalSmoothing
            A Boolean specifying whether surface smoothing (geometric correction) is automatically
            applied to all eligible surfaces. The default value is ON.
        includedPairs
            A :py:class:`~abaqus.Interaction.RegionPairs.RegionPairs` object specifying the domain pairs included in contact.
        excludedPairs
            A :py:class:`~abaqus.Interaction.RegionPairs.RegionPairs` object specifying the domain pairs excluded from contact.
        contactPropertyAssignments
            A :py:class:`~abaqus.Interaction.ContactPropertyAssignment.ContactPropertyAssignment` object specifying the contact property assignments in the
            contact domain.
        surfaceThicknessAssignments
            A :py:class:`~abaqus.Interaction.SurfaceThicknessAssignment.SurfaceThicknessAssignment` object specifying the surface thickness assignments in the
            contact domain.
        surfaceOffsetAssignments
            A :py:class:`~abaqus.Interaction.SurfaceOffsetAssignment.SurfaceOffsetAssignment` object specifying the surface offset fraction assignments in
            the contact domain.
        surfaceFeatureAssignments
            A :py:class:`~abaqus.Interaction.SurfaceFeatureAssignment.SurfaceFeatureAssignment` object specifying the surface feature angle assignments in
            the contact domain.
        mainSecondaryAssignments
            A :py:class:`~abaqus.Interaction.MainSecondaryAssignment.MainSecondaryAssignment` object specifying the main-secondary assignments in the
            contact domain.
        initializationAssignments
            An :py:class:`~abaqus.Interaction.InitializationAssignment.InitializationAssignment` object specifying the contact initialization assignments in
            the contact domain.
        stabilizationAssignments
            A :py:class:`~abaqus.Interaction.StabilizationAssignment.StabilizationAssignment` object specifying the contact stabilization assignments in the
            contact domain.
        smoothingAssignments
            A :py:class:`~abaqus.Interaction.SmoothingAssignment.SmoothingAssignment` object specifying the surface smoothing assignments in the contact
            domain.
        slidingTransitionAssignments
            A SlidingTransitionAssignments object specifying the sliding transition assignments in
            the contact domain.

        Returns
        -------
        ContactStd
            A :py:class:`~abaqus.Interaction.ContactStd.ContactStd` object.
        """
        self.interactions[name] = interaction = ContactStd(
            name,
            createStepName,
            useAllstar,
            globalSmoothing,
            includedPairs,
            excludedPairs,
            contactPropertyAssignments,
            surfaceThicknessAssignments,
            surfaceOffsetAssignments,
            surfaceFeatureAssignments,
            mainSecondaryAssignments,
            initializationAssignments,
            stabilizationAssignments,
            smoothingAssignments,
            slidingTransitionAssignments,
        )
        return interaction

    def CyclicSymmetry(
        self,
        name: str,
        createStepName: str,
        main: Region,
        secondary: Region,
        repetitiveSectors: int,
        axisPoint1: Region,
        axisPoint2: Region,
        extractedNodalDiameter: SymbolicConstant = ALL_NODAL_DIAMETER,
        lowestNodalDiameter: int = 0,
        highestNodalDiameter: int = 0,
        excitationNodalDiameter: int = 0,
        adjustTie: Boolean = ON,
        positionTolerance: float = 0,
        positionToleranceMethod: SymbolicConstant = COMPUTED_TOLERANCE,
    ) -> CyclicSymmetry:
        """This method creates a CyclicSymmetry object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].CyclicSymmetry

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the cyclic symmetry interaction should
            be created.
        main
            A :py:class:`~abaqus.Region.Region.Region` object specifying the main surface.
        secondary
            A :py:class:`~abaqus.Region.Region.Region` object specifying the secondary surface.
        repetitiveSectors
            An Int specifying the total number of sectors in the cyclic symmetric model.
        axisPoint1
            A :py:class:`~abaqus.Region.Region.Region` object specifying the first point of the axis of symmetry. The region should
            contain exactly one mesh node, vertex, interesting point, reference point, or datum
            point. In a two-dimensional model **axisPoint1** is the only point used to define the axis
            of symmetry.
        axisPoint2
            A :py:class:`~abaqus.Region.Region.Region` object specifying the second point of the axis of symmetry. The region should
            contain exactly one mesh node, vertex, interesting point, reference point, or datum
            point. This point is ignored in a two-dimensional model.
        extractedNodalDiameter
            A SymbolicConstant specifying whether Abaqus should extract all possible nodal diameters
            or the nodal diameters between the user-specified values for **lowestNodalDiameter** and
            **highestNodalDiameter**. Possible values are ALL_NODAL_DIAMETER and
            SPECIFIED_NODAL_DIAMETER. The default value is ALL_NODAL_DIAMETER.
        lowestNodalDiameter
            An Int specifying the lowest nodal diameter to be used in the eigenfrequency analysis.
            The default value is 0.
        highestNodalDiameter
            An Int specifying the highest nodal diameter to be used in the eigenfrequency analysis.
            This argument value should be less than or equal to the half of the total number of
            sectors (as specified in the **repetitiveSectors** parameter). The default value is 0.
        excitationNodalDiameter
            An Int specifying the nodal diameter for which the modal-based steady-state dynamic
            analysis will be performed. This value should be greater than or equal to the lowest
            nodal diameter (specified in the **lowestNodalDiameter** parameter), and less than or
            equal to the highest nodal diameter (specified in the **highestNodalDiameter** parameter).
            The default value is 0.
        adjustTie
            A Boolean specifying whether or not to adjust the secondary surface of the cyclic
            symmetry to tie it to the main surface. The default value is ON.
        positionTolerance
            A Float specifying the position tolerance. The*positionTolerance* argument applies only
            when **positionToleranceMethod** = SPECIFY_TOLERANCE. The default value is 0.0.
        positionToleranceMethod
            A SymbolicConstant specifying the method used to determine the position tolerance.
            Possible values are COMPUTED_TOLERANCE and SPECIFY_TOLERANCE. The default value is
            COMPUTED_TOLERANCE.

        Returns
        -------
        CyclicSymmetry
            A :py:class:`~abaqus.Interaction.CyclicSymmetry.CyclicSymmetry` object.
        """
        self.interactions[name] = interaction = CyclicSymmetry(
            name,
            createStepName,
            main,
            secondary,
            repetitiveSectors,
            axisPoint1,
            axisPoint2,
            extractedNodalDiameter,
            lowestNodalDiameter,
            highestNodalDiameter,
            excitationNodalDiameter,
            adjustTie,
            positionTolerance,
            positionToleranceMethod,
        )
        return interaction

    def ElasticFoundation(
        self, name: str, createStepName: str, surface: Region, stiffness: float
    ) -> ElasticFoundation:
        """This method creates an ElasticFoundation object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].ElasticFoundation

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the ElasticFoundation object is
            created. **createStepName** must be set to 'Initial'.
        surface
            A :py:class:`~abaqus.Region.Region.Region` object specifying the surface to which the foundation applies.
        stiffness
            A Float specifying the foundation stiffness per area (or per length for beams).

        Returns
        -------
        ElasticFoundation
            An :py:class:`~abaqus.Interaction.ElasticFoundation.ElasticFoundation` object.
        """
        self.interactions[name] = interaction = ElasticFoundation(
            name, createStepName, surface, stiffness
        )
        return interaction

    def ExpContactControl(
        self,
        name: str,
        globTrkChoice: SymbolicConstant = DEFAULT,
        globTrkInc: int = None,
        fastLocalTrk: Boolean = ON,
        scalePenalty: float = 1,
        warpCheckPeriod: int = 20,
        warpCutoff: float = 20,
    ) -> ExpContactControl:
        """This method creates an ExpContactControl object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].ExpContactControl

        Parameters
        ----------
        name
            A String specifying the contact controls repository key.
        globTrkChoice
            A SymbolicConstant specifying whether or not the default value will be used for the
            maximum number of increments between global contact searches. Possible values are
            DEFAULT and SPECIFY. The default value is DEFAULT.
        globTrkInc
            An Int specifying the maximum number of increments between global contact searches. The
            **globTrkInc** argument applies only when **globTrkChoice** = SPECIFY. The default value is
            100 for surface-to-surface contact and 4 for self-contact.
        fastLocalTrk
            A Boolean specifying whether to use the more computationally efficient local tracking
            method. The default value is ON.
        scalePenalty
            A Float specifying the factor by which Abaqus/Explicit will scale the default penalty
            stiffness to obtain the stiffnesses used for the penalty contact pairs. The default
            value is 1.0.
        warpCheckPeriod
            An Int specifying the number of increments between checks for highly warped facets on
            main surfaces. The default value is 20.
        warpCutoff
            A Float specifying the out-of-plane warping angle (in degrees), at which a facet will be
            considered to be highly warped. The default value is 20.0.

        Returns
        -------
        ExpContactControl
            An :py:class:`~abaqus.Interaction.ExpContactControl.ExpContactControl` object.

        Raises
        ------
        RangeError
        """
        self.interactions[name] = interaction = ExpContactControl(
            name,
            globTrkChoice,
            globTrkInc,
            fastLocalTrk,
            scalePenalty,
            warpCheckPeriod,
            warpCutoff,
        )
        return interaction

    def FilmCondition(
        self,
        name: str,
        createStepName: str,
        surface: Region,
        definition: SymbolicConstant,
        interactionProperty: str = "",
        sinkTemperature: float = 0,
        sinkAmplitude: str = "",
        filmCoeff: float = 0,
        filmCoeffAmplitude: str = "",
        field: str = "",
        sinkFieldName: str = "",
        sinkDistributionType: SymbolicConstant = UNIFORM,
    ) -> FilmCondition:
        """This method creates a FilmCondition object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].FilmCondition

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the FilmCondition object is created.
        surface
            A :py:class:`~abaqus.Region.Region.Region` object specifying the name of the surface to which the film condition
            interaction is applied.
        definition
            A SymbolicConstant specifying how the film condition is defined. Possible values are
            EMBEDDED_COEFF, PROPERTY_REF, USER_SUB, and FIELD.
        interactionProperty
            A String specifying the name of the FilmConditionProp object associated with this
            interaction. The **interactionProperty** argument applies only when
            **definition** = PROPERTY_REF. The default value is an empty string.
        sinkTemperature
            A Float specifying the reference sink temperature, θ0θ0. The default value is 0.0.
        sinkAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the
            sink temperature, θ0θ0, with time. The default value is an empty string.Note:Use empty
            string in an Abaqus/Standard analysis to specify that the reference sink temperature is
            applied immediately at the beginning of the step or linearly over the step. Use empty
            string in an Abaqus/Explicit analysis to specify that the reference sink temperature is
            applied throughout the step.
        filmCoeff
            A Float specifying the reference film coefficient value, hh. The **filmCoeff** argument
            applies when **definition** = EMBEDDED_COEFF, **definition** = USER_SUB, or **definition** = FIELD.
            The default value is 0.0.
        filmCoeffAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the
            film coefficient, hh, with time. The default value is an empty string. Note: Use empty
            string in an Abaqus/Standard analysis to specify that the reference film coefficient is
            applied immediately at the beginning of the step or linearly over the step. Use empty
            string in an Abaqus/Explicit analysis to specify that the reference film coefficient is
            applied throughout the step.
        field
            A String specifying the name of the AnalyticalField object associated with this
            interaction. The **field** argument applies only when **definition** = FIELD. The default
            value is an empty string.
        sinkFieldName
            A String specifying the name of the AnalyticalField or DiscreteField object associated
            with the sink temperature. The **sinkFieldName** argument applies only when
            **sinkDistributionType** = ANALYTICAL_FIELD or **sinkDistributionType** = DISCRETE_FIELD. The
            default value is an empty string.
        sinkDistributionType
            A SymbolicConstant specifying how the sink temperature is distributed. Possible values
            are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM.

        Returns
        -------
        FilmCondition
            A :py:class:`~abaqus.Interaction.FilmCondition.FilmCondition` object.
        """
        self.interactions[name] = interaction = FilmCondition(
            name,
            createStepName,
            surface,
            definition,
            interactionProperty,
            sinkTemperature,
            sinkAmplitude,
            filmCoeff,
            filmCoeffAmplitude,
            field,
            sinkFieldName,
            sinkDistributionType,
        )
        return interaction

    def FilmConditionProp(
        self,
        name: str,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        property: tuple = (),
    ) -> FilmConditionProp:
        """This method creates a FilmConditionProp object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].FilmConditionProp

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        property
            A sequence of sequences of Floats specifying the following:
            
            - The film coefficient, hh.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        Returns
        -------
        FilmConditionProp
            A :py:class:`~abaqus.Interaction.FilmConditionProp.FilmConditionProp` object.
        """
        self.interactions[name] = interaction = FilmConditionProp(
            name, temperatureDependency, dependencies, property
        )
        return interaction

    def FluidCavity(
        self,
        name: str,
        createStepName: str,
        cavityPoint: Region,
        cavitySurface: Region,
        interactionProperty: str,
        ambientPressure: float = 0,
        thickness: float = 1,
        useAdiabatic: Boolean = OFF,
        checkNormals: Boolean = ON,
    ) -> FluidCavity:
        """This method creates an FluidCavity object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].FluidCavity

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the FluidCavity object is created.
        cavityPoint
            A :py:class:`~abaqus.Region.Region.Region` object specifying the fluid cavity reference point.
        cavitySurface
            A :py:class:`~abaqus.Region.Region.Region` object specifying the surface forming the boundary of the fluid cavity.
        interactionProperty
            A String specifying the FluidCavityProperty object associated with this interaction.
        ambientPressure
            A Float specifying the magnitude of the ambient pressure. The default value is 0.0.
        thickness
            A Float specifying the out-of-plane thickness of the surface for two-dimensional models.
            This argument is valid only when using two-dimensional models. The default value is 1.0.
        useAdiabatic
            A Boolean specifying whether adiabatic behavior is assumed for the ideal gas. This
            argument is valid only when **interactionProperty** specifies a pneumatic definition. The
            default value is OFF.
        checkNormals
            A Boolean specifying whether the analysis will check the consistency of the surface
            normals. The default value is ON.

        Returns
        -------
        FluidCavity
            A :py:class:`~abaqus.Interaction.FluidCavity.FluidCavity` object.
        """
        self.interactions[name] = interaction = FluidCavity(
            name,
            createStepName,
            cavityPoint,
            cavitySurface,
            interactionProperty,
            ambientPressure,
            thickness,
            useAdiabatic,
            checkNormals,
        )
        return interaction

    def FluidCavityProperty(
        self,
        name: str,
        definition: SymbolicConstant = HYDRAULIC,
        fluidDensity: float = None,
        molecularWeight: float = None,
        useExpansion: Boolean = OFF,
        expansionTempDep: Boolean = OFF,
        expansionDependencies: int = 0,
        referenceTemperature: float = 0,
        expansionTable: tuple = (),
        useBulkModulus: Boolean = OFF,
        bulkModulusTempDep: Boolean = OFF,
        bulkModulusDependencies: int = 0,
        bulkModulusTable: tuple = (),
        useCapacity: Boolean = OFF,
        capacityType: SymbolicConstant = POLYNOMIAL,
        capacityTempDep: Boolean = OFF,
        capacityDependencies: int = 0,
        capacityTable: tuple = (),
    ) -> FluidCavityProperty:
        """This method creates a FluidCavityProperty object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].FluidCavityProperty

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.
        definition
            A SymbolicConstant specifying the type of fluid cavity property to be defined. Possible
            values are HYDRAULIC and PNEUMATIC. The default value is HYDRAULIC.
        fluidDensity
            None or a Float specifying the reference fluid density. This argument is applicable only
            when **definition** = HYDRAULIC, and is required in that case. The default value is None.
        molecularWeight
            None or a Float specifying the molecular weight of the ideal gas species. This argument
            is applicable only when **definition** = PNEUMATIC, and is required in that case. The
            default value is None.
        useExpansion
            A Boolean specifying whether thermal expansion coefficients will be defined. This
            argument is applicable only when **definition** = HYDRAULIC. The default value is OFF.
        expansionTempDep
            A Boolean specifying whether the thermal fluid expansion data will have temperature
            dependency. This argument is applicable only when **definition** = HYDRAULIC and when
            **useExpansion** = True. The default value is OFF.
        expansionDependencies
            An Int specifying the number of field variable dependencies in the thermal fluid
            expansion data. This argument is applicable only when **definition** = HYDRAULIC and when
            **useExpansion** = True. The default value is 0.
        referenceTemperature
            A Float specifying the reference temperature for the coefficient of thermal expansion.
            This argument is applicable only when **definition** = HYDRAULIC, when **useExpansion** = True,
            and when either **expansionTempDep** = True or when **expansionDependencies** is greater than
            0. The default value is 0.0.
        expansionTable
            A sequence of sequences of Floats specifying the thermal expansion coefficients. This
            argument is applicable only when **definition** = HYDRAULIC and when **useExpansion** = True.
            Each sequence contains the following data:
            
            - The mean coefficient of thermal expansion.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        useBulkModulus
            A Boolean specifying whether fluid bulk modulus values will be defined. This argument is
            applicable only when **definition** = HYDRAULIC. The default value is OFF.
        bulkModulusTempDep
            A Boolean specifying whether the fluid bulk modulus data will have temperature
            dependency. This argument is applicable only when **definition** = HYDRAULIC and when
            **useBulkModulus** = True. The default value is OFF.
        bulkModulusDependencies
            An Int specifying the number of field variable dependencies in the fluid bulk modulus
            data. This argument is applicable only when **definition** = HYDRAULIC and when
            **useBulkModulus** = True. The default value is 0.
        bulkModulusTable
            A sequence of sequences of Floats specifying the fluid bulk modulus values. This
            argument is applicable only when **definition** = HYDRAULIC and when **useBulkModulus** = True.
            Each sequence contains the following data:
            
            - The fluid bulk modulus.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        useCapacity
            A Boolean specifying whether molar heat capacity values will be defined. This argument
            is applicable only when **definition** = PNEUMATIC. The default value is OFF.
        capacityType
            A SymbolicConstant specifying the method to define the molar heat capacity. Possible
            values are POLYNOMIAL and TABULAR. The default value is POLYNOMIAL.
        capacityTempDep
            A Boolean specifying whether the molar heat capacity data will have temperature
            dependency. This argument is applicable only when **definition** = PNEUMATIC, when
            **useCapacity** = True, and when **capacityType** = TABULAR. The default value is OFF.
        capacityDependencies
            An Int specifying the number of field variable dependencies in the molar heat capacity
            data. This argument is applicable only when **definition** = PNEUMATIC, when
            **useCapacity** = True, and when **capacityType** = TABULAR. The default value is 0.
        capacityTable
            A sequence of sequences of Floats specifying the molar heat capacity values in the form
            of a polynomial expression. This argument is applicable only when
            **definition** = PNEUMATIC, when **useCapacity** = True, and when **capacityType** = POLYNOMIAL. In
            this form, only one sequence is specified and that sequence contains the following data:
            
            - The first molar heat capacity coefficient.
            - The second molar heat capacity coefficient.
            - The third molar heat capacity coefficient.
            - The fourth molar heat capacity coefficient.
            - The fifth molar heat capacity coefficient.
              
            Alternatively, the sequence data may specify the molar heat capacity values at constant
            pressure for an ideal gas species. This argument is applicable only when
            **definition** = PNEUMATIC, when **useCapacity** = True, and when **capacityType** = TABULAR. Each
            sequence contains the following data:
            
            - The molar heat capacity at constant pressure.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        Returns
        -------
        FluidCavityProperty
            A :py:class:`~abaqus.Interaction.FluidCavityProperty.FluidCavityProperty` object.
        """
        self.interactions[name] = interaction = FluidCavityProperty(
            name,
            definition,
            fluidDensity,
            molecularWeight,
            useExpansion,
            expansionTempDep,
            expansionDependencies,
            referenceTemperature,
            expansionTable,
            useBulkModulus,
            bulkModulusTempDep,
            bulkModulusDependencies,
            bulkModulusTable,
            useCapacity,
            capacityType,
            capacityTempDep,
            capacityDependencies,
            capacityTable,
        )
        return interaction

    def FluidExchange(
        self,
        name: str,
        createStepName: str,
        firstCavity: str,
        interactionProperty: str,
        definition: SymbolicConstant = TO_ENVIRONMENT,
        secondCavity: str = "",
        exchangeArea: float = 1,
    ) -> FluidExchange:
        """This method creates an FluidExchange object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].FluidExchange

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the FluidExchange object is created.
        firstCavity
            A String specifying the first FluidCavity object associated with this interaction. This
            will be the only cavity specified if **definition** = TO_ENVIRONMENT.
        interactionProperty
            A String specifying the FluidExchangeProperty object associated with this interaction.
        definition
            A SymbolicConstant specifying the type of fluid exchange to be defined. Possible values
            are TO_ENVIRONMENT and BETWEEN_CAVITIES. The default value is TO_ENVIRONMENT.
        secondCavity
            A String specifying the second FluidCavity object associated with this interaction. This
            argument is applicable only when **definition** = BETWEEN_CAVITIES.
        exchangeArea
            A Float specifying the effective exchange area. The default value is 1.0.

        Returns
        -------
        FluidExchange
            A :py:class:`~abaqus.Interaction.FluidExchange.FluidExchange` object.
        """
        self.interactions[name] = interaction = FluidExchange(
            name,
            createStepName,
            firstCavity,
            interactionProperty,
            definition,
            secondCavity,
            exchangeArea,
        )
        return interaction

    def FluidExchangeProperty(
        self,
        name: str,
        dataTable: tuple,
        definition: SymbolicConstant = BULK_VISCOSITY,
        pressureDependency: Boolean = OFF,
        temperatureDependency: Boolean = OFF,
        fieldDependencies: int = 0,
    ) -> FluidExchangeProperty:
        """This method creates a FluidExchangeProperty object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].FluidExchangeProperty

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.
        dataTable
            A sequence of sequences of Floats specifying the viscous and hydrodynamic resistance
            coefficients when **definition** = BULK_VISCOSITY. Each sequence contains the following
            data:
            
            - The viscous resistance coefficient.
            - The hydrodynamic resistance coefficient.
            - The average absolute pressure, if the data depend on pressure.
            - The average temperature, if the data depend on temperature.
            - The value of the first field variable, if the data depend on field variables.
            - The value of the second field variable.
            - Etc.
            
            Alternatively, the sequence data may specify the mass flow rate. This is applicable only
            when **definition** = MASS_FLUX. In this form, only one sequence is specified and that
            sequence contains the following data:
            
            - The mass flow rate per unit area.
            
            Alternatively, the sequence data may specify the mass rate leakage. This is applicable
            only when **definition** = MASS_RATE_LEAK. Each sequence contains the following data:
              
            - The absolute value of the mass flow rate per unit area. (The first tabular value
              entered must always be zero.)
            - The absolute value of the pressure difference. (The first tabular value entered must
              always be zero.)
            - The average absolute pressure, if the data depend on pressure.
            - The average temperature, if the data depend on temperature.
            - The value of the first field variable, if the data depend on field variables.
            - The value of the second field variable.
            - Etc.
            
            Alternatively, the sequence data may specify the volume flow rate. This is applicable
            only when **definition** = VOL_FLUX. In this form, only one sequence is specified and that
            sequence contains the following data:
            
            - The volumetric flow rate per unit area.
              Alternatively, the sequence data may specify the volume rate leakage. This is applicable
              only when **definition** = VOL_RATE_LEAK. Each sequence contains the following data:
            
            - The absolute value of the volumetric flow rate per unit area. (The first tabular value
              entered must always be zero.)
            - The absolute value of the pressure difference. (The first tabular value entered must
              always be zero.)
            - The average absolute pressure, if the data depend on pressure.
            - The average temperature, if the data depend on temperature.
            - The value of the first field variable, if the data depend on field variables.
            - The value of the second field variable.
            - Etc.
        definition
            A SymbolicConstant specifying the type of fluid exchange property to be defined.
            Possible values are BULK_VISCOSITY, MASS_FLUX, MASS_RATE_LEAK, VOL_FLUX, and
            VOL_RATE_LEAK. The default value is BULK_VISCOSITY.
        pressureDependency
            A Boolean specifying whether the data will have pressure dependency. This argument is
            applicable only when **definition** = BULK_VISCOSITY, or when **definition** = MASS_RATE_LEAK,
            or when **definition** = VOL_RATE_LEAK. The default value is OFF.
        temperatureDependency
            A Boolean specifying whether the data will have temperature dependency. This argument is
            applicable only when **definition** = BULK_VISCOSITY, or when **definition** = MASS_RATE_LEAK,
            or when **definition** = VOL_RATE_LEAK. The default value is OFF.
        fieldDependencies
            An Int specifying the number of field variable dependencies in the data. This argument
            is applicable only when **definition** = BULK_VISCOSITY, or when
            **definition** = MASS_RATE_LEAK, or when **definition** = VOL_RATE_LEAK. The default value is 0.

        Returns
        -------
        FluidExchangeProperty
            A :py:class:`~abaqus.Interaction.FluidExchangeProperty.FluidExchangeProperty` object.
        """
        self.interactions[name] = interaction = FluidExchangeProperty(
            name,
            dataTable,
            definition,
            pressureDependency,
            temperatureDependency,
            fieldDependencies,
        )
        return interaction

    def IncidentWave(
        self,
        name: str,
        createStepName: str,
        sourcePoint: Region,
        standoffPoint: Region,
        surface: Region,
        interactionProperty: str,
        definition: SymbolicConstant = PRESSURE,
        amplitude: str = "",
        imaginaryAmplitude: str = "",
        surfaceNormal: tuple = (),
        initialDepth: float = None,
        referenceMagnitude: float = None,
        detonationTime: float = None,
        magnitudeFactor: float = 1,
    ) -> IncidentWave:
        """This method creates an IncidentWave object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].IncidentWave

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the IncidentWave object is created.
        sourcePoint
            A :py:class:`~abaqus.Region.Region.Region` object specifying the incident wave source point.
        standoffPoint
            A :py:class:`~abaqus.Region.Region.Region` object specifying the incident wave standoff point.This argument is not valid
            when **definition** = CONWEP.
        surface
            A :py:class:`~abaqus.Region.Region.Region` object specifying the surface defining the incident wave interaction. In
            problems involving fluid/surface boundaries, both the fluid surface and the solid
            surface comprising the boundary must have an incident wave interaction specified.
        interactionProperty
            A String specifying the IncidentWaveProperty object associated with this interaction.
        definition
            A SymbolicConstant specifying the type of incident wave to be defined. The value must be
            PRESSURE for linear perturbation steps. An Explicit step is required when the value is
            set to CONWEP. Possible values are PRESSURE, ACCELERATION, UNDEX, and CONWEP. The
            default value is PRESSURE.
        amplitude
            A String specifying the name of the Amplitude object that defines the fluid pressure
            time history at the standoff point, if **definition** = PRESSURE. If
            **definition** = ACCELERATION, then this string specifies the name of the Amplitude object
            that defines the fluid particle acceleration time history at the standoff point. This
            member can be specified only if **definition** = PRESSURE or ACCELERATION. The default value
            is an empty string.
        imaginaryAmplitude
            A String specifying the name of the Amplitude object that defines the imaginary
            component of the fluid pressure time history at the standoff point. This member is
            applicable only for linear perturbation steps and if **definition** = PRESSURE. The default
            value is an empty string.
        surfaceNormal
            A sequence of three Floats specifying the X, Y, and Z components of the direction cosine
            of the fluid surface normal.This argument is valid only when **definition** = UNDEX.
        initialDepth
            None or a Float specifying the initial depth of the UNDEX bubble. The default value is
            None.This argument is valid only when **definition** = UNDEX.
        referenceMagnitude
            A Float specifying the reference magnitude.This argument is not valid when
            **definition** = CONWEP.
        detonationTime
            A Float specifying the time of detonation, given in total time.This argument is valid
            only when **definition** = CONWEP.
        magnitudeFactor
            A Float specifying the magnitude scale factor. The default value is 1.0.This argument is
            valid only when **definition** = CONWEP.

        Returns
        -------
        IncidentWave
            An :py:class:`~abaqus.Interaction.IncidentWave.IncidentWave` object.
        """
        self.interactions[name] = interaction = IncidentWave(
            name,
            createStepName,
            sourcePoint,
            standoffPoint,
            surface,
            interactionProperty,
            definition,
            amplitude,
            imaginaryAmplitude,
            surfaceNormal,
            initialDepth,
            referenceMagnitude,
            detonationTime,
            magnitudeFactor,
        )
        return interaction

    def IncidentWaveProperty(
        self,
        name: str,
        definition: SymbolicConstant = PLANAR,
        propagationModel: SymbolicConstant = ACOUSTIC,
        soundSpeed: float = None,
        fluidDensity: float = None,
        specificHeatRatio: float = None,
        gravity: float = None,
        atmosphericPressure: float = None,
        dragCoefficient: float = None,
        dragExponent: float = 2,
        waveEffects: Boolean = ON,
        chargeDensity: float = None,
        chargeMass: float = None,
        constantK1: float = None,
        constantK2: float = None,
        constantA: float = None,
        constantB: float = None,
        constantKc: float = None,
        duration: float = None,
        maximumSteps: int = 1500,
        relativeStepControl: float = None,
        absoluteStepControl: float = None,
        stepControlExponent: float = 0,
        genDecayA: float = 0,
        genDecayB: float = 0,
        genDecayC: float = 0,
        seedNumber: int = None,
        massTNT: float = None,
        massFactor: float = 1,
        lengthFactor: float = 1,
        timeFactor: float = 1,
        pressureFactor: float = 1,
    ) -> IncidentWaveProperty:
        """This method creates an IncidentWaveProperty object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].IncidentWaveProperty

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.
        definition
            A SymbolicConstant specifying the type of wave to be defined. Possible values are
            PLANAR, SPHERICAL, DIFFUSE, AIR_BLAST, and SURFACE_BLAST. The default value is PLANAR.
        propagationModel
            A SymbolicConstant specifying the spherical propagation model. Possible values are
            ACOUSTIC, UNDEX_CHARGE, and GENERALIZED_DECAY. The default value is ACOUSTIC.This
            argument is valid only when **definition** = SPHERICAL.
        soundSpeed
            A Float specifying the speed of sound in the fluid.This argument is not valid when
            **definition** = AIR_BLAST or when **definition** = SURFACE_BLAST.
        fluidDensity
            A Float specifying the fluid mass density.This argument is not valid when
            **definition** = AIR_BLAST or when **definition** = SURFACE_BLAST.
        specificHeatRatio
            None or a Float specifying the ratio of specific heats for gas. The default value is
            None.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        gravity
            None or a Float specifying the acceleration due to gravity. The default value is
            None.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        atmosphericPressure
            None or a Float specifying the atmospheric pressure. The default value is None.This
            argument is valid only when **definition** = SPHERICAL and **propagationModel** = UNDEX_CHARGE.
        dragCoefficient
            None or a Float specifying the fluid drag coefficient. The default value is None.This
            argument is valid only when **definition** = SPHERICAL and **propagationModel** = UNDEX_CHARGE.
        dragExponent
            A Float specifying the fluid drag exponent. The default value is 2.0.This argument is
            valid only when **definition** = SPHERICAL and **propagationModel** = UNDEX_CHARGE.
        waveEffects
            A Boolean specifying whether or not to include wave effects in the fluid and gas. The
            default value is ON.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        chargeDensity
            None or a Float specifying the density of the charge material. The default value is
            None.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        chargeMass
            None or a Float specifying the mass of the charge material. The default value is
            None.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        constantK1
            None or a Float specifying the charge material constant K. The default value is
            None.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        constantK2
            None or a Float specifying the charge material constant k. The default value is
            None.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        constantA
            None or a Float specifying the charge material constant A. The default value is
            None.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        constantB
            None or a Float specifying the charge material constant B. The default value is
            None.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        constantKc
            None or a Float specifying the charge material constant Kc. The default value is
            None.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        duration
            None or a Float specifying the time duration for the bubble simulation. The default
            value is None.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        maximumSteps
            An Int specifying the maximum number of time steps for the bubble simulation. The
            default value is 1500.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        relativeStepControl
            A Float specifying the relative step size control parameter. The default value is
            1×10-11.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        absoluteStepControl
            A Float specifying the absolute step size control parameter. The default value is
            1×10-11.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        stepControlExponent
            A Float specifying the step size control exponent. The default value is 0.2.This
            argument is valid only when **definition** = SPHERICAL and **propagationModel** = UNDEX_CHARGE.
        genDecayA
            A Float specifying the constant A associated with the generalized decay propagation
            model. The default value is 0.0.This argument is valid only when **definition** = SPHERICAL
            and **propagationModel** = GENERALIZED_DECAY.
        genDecayB
            A Float specifying the constant B associated with the generalized decay propagation
            model. The default value is 0.0.This argument is valid only when **definition** = SPHERICAL
            and **propagationModel** = GENERALIZED_DECAY.
        genDecayC
            A Float specifying the constant C associated with the generalized decay propagation
            model. The default value is 0.0.This argument is valid only when **definition** = SPHERICAL
            and **propagationModel** = GENERALIZED_DECAY.
        seedNumber
            An Int specifying the seed number (N) for the diffuse source calculation. N2 sources
            will be used in the simulation.This argument is valid only when **definition** = DIFFUSE.
        massTNT
            A Float specifying the equivalent mass of TNT, in any preferred mass unit.This argument
            is valid only when **definition** = AIR_BLAST or **definition** = SURFACE_BLAST.
        massFactor
            A Float specifying the multiplication factor to convert from the preferred mass unit to
            kilograms. The default value is 1.0.This argument is valid only when
            **definition** = AIR_BLAST or **definition** = SURFACE_BLAST.
        lengthFactor
            A Float specifying the multiplication factor to convert from the analysis length unit to
            meters. The default value is 1.0.This argument is valid only when **definition** = AIR_BLAST
            or **definition** = SURFACE_BLAST.
        timeFactor
            A Float specifying the multiplication factor to convert from the analysis time unit to
            seconds. The default value is 1.0.This argument is valid only when
            **definition** = AIR_BLAST or **definition** = SURFACE_BLAST.
        pressureFactor
            A Float specifying the multiplication factor to convert from the analysis pressure unit
            to pascals. The default value is 1.0.This argument is valid only when
            **definition** = AIR_BLAST or **definition** = SURFACE_BLAST.

        Returns
        -------
        IncidentWaveProperty
            An :py:class:`~abaqus.Interaction.IncidentWaveProperty.IncidentWaveProperty` object.
        """
        self.interactions[name] = interaction = IncidentWaveProperty(
            name,
            definition,
            propagationModel,
            soundSpeed,
            fluidDensity,
            specificHeatRatio,
            gravity,
            atmosphericPressure,
            dragCoefficient,
            dragExponent,
            waveEffects,
            chargeDensity,
            chargeMass,
            constantK1,
            constantK2,
            constantA,
            constantB,
            constantKc,
            duration,
            maximumSteps,
            relativeStepControl,
            absoluteStepControl,
            stepControlExponent,
            genDecayA,
            genDecayB,
            genDecayC,
            seedNumber,
            massTNT,
            massFactor,
            lengthFactor,
            timeFactor,
            pressureFactor,
        )
        return interaction

    def ModelChange(
        self,
        name: str,
        createStepName: str,
        isRestart: Boolean = OFF,
        regionType: SymbolicConstant = GEOMETRY,
        region: Region = None,
        activeInStep: Boolean = OFF,
        includeStrain: Boolean = OFF,
    ) -> ModelChange:
        """This method creates a ModelChange object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].ModelChange

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the ModelChange object is created.
        isRestart
            A Boolean specifying whether this interaction is being used solely to indicate that
            model change may be required in a subsequent restart analysis (either for elements or
            contact pairs). The default value is OFF.
        regionType
            A SymbolicConstant specifying the region selection type. This argument is valid only
            when **isRestart** = False. Possible values are GEOMETRY, SKINS, STRINGERS, and ELEMENTS.
            The default value is GEOMETRY.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the elements to be removed or reactivated. This argument is
            valid only when **isRestart** = False.
        activeInStep
            A Boolean specifying whether elements are being removed or reactivated. This argument is
            valid only when **isRestart** = False. The default value is OFF.
        includeStrain
            A Boolean specifying whether stress/displacement elements are reactivated with strain.
            This argument is valid only when **isRestart** = False and when **activeInStep** = True. The
            default value is OFF.

        Returns
        -------
        ModelChange
            A :py:class:`~abaqus.Interaction.ModelChange.ModelChange` object.
        """
        self.interactions[name] = interaction = ModelChange(
            name,
            createStepName,
            isRestart,
            regionType,
            region,
            activeInStep,
            includeStrain,
        )
        return interaction

    def PressurePenetration(
        self,
        name: str,
        createStepName: str,
        contactInteraction: str,
        mainPoints: RegionArray,
        secondaryPoints: RegionArray,
        penetrationPressure: float,
        criticalPressure: float,
        amplitude: str = UNSET,
        penetrationTime: float = 0,
    ) -> PressurePenetration:
        """This method creates a PressurePenetration object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].PressurePenetration

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the PressurePenetration object is
            created.
        contactInteraction
            A String specifying the name of the Surface-to-surface contact (Standard) interaction.
        mainPoints
            A :py:class:`~abaqus.Region.RegionArray.RegionArray` object specifying the points on the main surface that are exposed to the
            fluid.
        secondaryPoints
            A :py:class:`~abaqus.Region.RegionArray.RegionArray` object specifying the points on the secondary surface that are exposed to
            the fluid.
        penetrationPressure
            A tuple of Floats specifying the fluid pressure magnitude. For steady state dynamic
            analyses, a tuple of Complexes specifying the fluid pressure magnitude.
        criticalPressure
            A tuple of Floats specifying the critical contact pressure below which fluid penetration
            starts to occur.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the **amplitude** argument only if it is valid for the specified step.
        penetrationTime
            A Float specifying the fraction of the current step time over which the fluid pressure
            on newly penetrated contact surface segments is ramped up to the current magnitude. The
            default value is 0.001.

        Returns
        -------
        PressurePenetration
            A :py:class:`~abaqus.Interaction.PressurePenetration.PressurePenetration` object.
        """
        self.interactions[name] = interaction = PressurePenetration(
            name,
            createStepName,
            contactInteraction,
            mainPoints,
            secondaryPoints,
            penetrationPressure,
            criticalPressure,
            amplitude,
            penetrationTime,
        )
        return interaction

    def RadiationToAmbient(
        self,
        name: str,
        createStepName: str,
        surface: Region,
        emissivity: float,
        field: str = "",
        distributionType: SymbolicConstant = UNIFORM,
        radiationType: SymbolicConstant = AMBIENT,
        ambientTemperature: float = 0,
        ambientTemperatureAmp: str = "",
    ) -> RadiationToAmbient:
        """This method creates a RadiationToAmbient object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].RadiationToAmbient

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the RadiationToAmbient object is
            created.
        surface
            A :py:class:`~abaqus.Region.Region.Region` object specifying the surface to which the radiation interaction is applied.
        emissivity
            A Float specifying the emissivity, ϵϵ.
        field
            A String specifying the name of the AnalyticalField object associated with this
            interaction. The **field** argument applies only when **distributionType** = ANALYTICAL_FIELD.
            The default value is an empty string.
        distributionType
            A SymbolicConstant specifying how the radiation is distributed. This argument applies
            only when **radiationType** = AMBIENT. Possible values are UNIFORM and ANALYTICAL_FIELD. The
            default value is UNIFORM.
        radiationType
            A SymbolicConstant specifying whether to use the default surface radiation behavior, or
            the cavity radiation approximation. Possible values are AMBIENT and CAVITY. The default
            value is AMBIENT.
        ambientTemperature
            A Float specifying the reference ambient temperature, θ0θ0. This argument applies only
            when **radiationType** = AMBIENT. The default value is 0.0.
        ambientTemperatureAmp
            A String specifying the name of the Amplitude object that gives the variation of the
            ambient temperature with time.Note:Use None in an Abaqus/Standard analysis to specify
            that the reference ambient temperature is applied immediately at the beginning of the
            step or linearly over the step. Use None in an Abaqus/Explicit analysis to specify that
            the reference ambient temperature is applied throughout the step. This argument applies
            only when **radiationType** = AMBIENT.

        Returns
        -------
        RadiationToAmbient
            A :py:class:`~abaqus.Interaction.RadiationToAmbient.RadiationToAmbient` object.
        """
        self.interactions[name] = interaction = RadiationToAmbient(
            name,
            createStepName,
            surface,
            emissivity,
            field,
            distributionType,
            radiationType,
            ambientTemperature,
            ambientTemperatureAmp,
        )
        return interaction

    def SelfContactExp(
        self,
        name: str,
        createStepName: str,
        surface: Region,
        interactionProperty: str,
        mechanicalConstraint: SymbolicConstant = KINEMATIC,
        contactControls: str = "",
    ) -> SelfContactExp:
        """This method creates a SelfContactExp object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].SelfContactExp

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the SelfContactExp object is created.
        surface
            A :py:class:`~abaqus.Region.Region.Region` object specifying the surface where self-contact is defined.
        interactionProperty
            A String specifying the name of the ContactProperty object associated with this
            interaction.
        mechanicalConstraint
            A SymbolicConstant specifying the mechanical constraint formulation. Possible values are
            KINEMATIC and PENALTY. The default value is KINEMATIC.
        contactControls
            A String specifying the name of the ContactControl object associated with this
            interaction. An empty string indicates that the default contact controls will be used.
            The default value is an empty string.

        Returns
        -------
        SelfContactExp
            A :py:class:`~abaqus.Interaction.SelfContactExp.SelfContactExp` object.
        """
        self.interactions[name] = interaction = SelfContactExp(
            name,
            createStepName,
            surface,
            interactionProperty,
            mechanicalConstraint,
            contactControls,
        )
        return interaction

    def SelfContactStd(
        self,
        name: str,
        createStepName: str,
        surface: Region,
        interactionProperty: str,
        enforcement: SymbolicConstant = SURFACE_TO_SURFACE,
        thickness: Boolean = ON,
        smooth: float = 0,
        contactControls: str = "",
    ) -> SelfContactStd:
        """This method creates a SelfContactStd object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].SelfContactStd

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the SelfContactStd object is created.
        surface
            A :py:class:`~abaqus.Region.Region.Region` object specifying the surface where self-contact is defined.
        interactionProperty
            A String specifying the name of the ContactProperty object associated with this
            interaction.
        enforcement
            A SymbolicConstant specifying the discretization method. Possible values are
            NODE_TO_SURFACE and SURFACE_TO_SURFACE. The default value is SURFACE_TO_SURFACE.
        thickness
            A Boolean specifying whether shell/membrane element thickness is considered. The default
            value is ON.This argument in valid only when **enforcement** = SURFACE_TO_SURFACE.
        smooth
            A Float specifying the degree of smoothing used for deformable or rigid main surfaces
            involved when **enforcement** = NODE_TO_SURFACE. The value given must lie between 0.0 and
            0.5. The default value is 0.2.
        contactControls
            A String specifying the name of the ContactControl object associated with this
            interaction. An empty string indicates that the default contact controls will be used.
            The default value is an empty string.

        Returns
        -------
        SelfContactStd
            A :py:class:`~abaqus.Interaction.SelfContactStd.SelfContactStd` object.
        """
        self.interactions[name] = interaction = SelfContactStd(
            name,
            createStepName,
            surface,
            interactionProperty,
            enforcement,
            thickness,
            smooth,
            contactControls,
        )
        return interaction

    def StdContactControl(
        self,
        name: str,
        stiffnessScaleFactor: float = 1,
        penetrationTolChoice: SymbolicConstant = RELATIVE,
        relativePenetrationTolerance: float = None,
        absolutePenetrationTolerance: float = None,
        frictionOnset: SymbolicConstant = None,
        automaticTolerances: Boolean = OFF,
        maxchp: int = 0,
        perrmx: float = 0,
        uerrmx: float = 0,
        stabilizeChoice: SymbolicConstant = NONE,
        dampFactor: float = 1,
        dampCoef: float = 0,
        tangFraction: float = 1,
        eosFraction: float = 0,
        zeroDampingChoice: SymbolicConstant = COMPUTE,
        zeroDamping: float = None,
        enforceWithLagrangeMultipliers: SymbolicConstant = DEFAULT,
    ) -> StdContactControl:
        """This method creates an StdContactControl object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].StdContactControl

        Parameters
        ----------
        name
            A String specifying the contact controls repository key.
        stiffnessScaleFactor
            A Float specifying the factor by which Abaqus/Standard will scale the default penalty
            stiffness to obtain the stiffnesses used for the contact pairs. Only contact
            interactions defined with augmented Lagrangian surface behavior will be affected by this
            argument. The default value is 1.0.
        penetrationTolChoice
            A SymbolicConstant specifying whether the allowable penetration is an absolute value or
            a value relative to the characteristic contact surface face dimension. Only contact
            interactions defined with augmented Lagrangian surface behavior will be affected by this
            argument. Possible values are RELATIVE and ABSOLUTE. The default value is RELATIVE.
        relativePenetrationTolerance
            A Float specifying the ratio of the allowable penetration to the characteristic contact
            surface face dimension. The float values represent percentages (e.g.: 0.001=0.1%). Only
            contact interactions defined with augmented Lagrangian surface behavior will be affected
            by this argument. The default value is 10-3.The **relativePenetrationTolerance** argument
            applies only when **penetrationTolChoice** = RELATIVE. The **relativePenetrationTolerance**
            and **absolutePenetrationTolerance** arguments are mutually exclusive.
        absolutePenetrationTolerance
            None or a Float specifying the allowable penetration. Only contact interactions defined
            with augmented Lagrangian surface behavior will be affected by this argument. The
            **absolutePenetrationTolerance** argument applies only when
            **penetrationTolChoice** = ABSOLUTE. The **relativePenetrationTolerance** and
            **absolutePenetrationTolerance** arguments are mutually exclusive. The default value is
            None.
        frictionOnset
            A SymbolicConstant specifying when the application of friction occurs. Possible values
            are:
            
            - IMMEDIATE, specifying the friction is included in the increment when contact occurs.
            - DELAYED, specifying the application of friction is delayed until the increment after
              contact occurs.
        automaticTolerances
            A Boolean specifying whether Abaqus/Standard should automatically compute an overclosure
            tolerance and a separation tolerance to prevent chattering in contact. The default value
            is OFF.The **automaticTolerances** argument cannot be used with the **maxchp**, **perrmx**,
            and **uerrmx** arguments.
        maxchp
            An Int specifying the maximum number of points that are permitted to violate contact
            conditions in any increment. The default value is 0.Either the **perrmx** or the **uerrmx**
            argument must be specified in conjunction with the **maxchp** argument.
        perrmx
            A Float specifying the maximum value of tensile stress (tensile force in GAP- or
            ITT-type contact elements) allowed to be transmitted at a contact point. The default
            value is 0.0.The **perrmx** argument must be specified in conjunction with the **maxchp**
            argument.
        uerrmx
            A Float specifying the maximum overclosure distance allowed at a secondary node that is
            considered to be open. The default value is 0.0.The **uerrmx** argument must be specified
            in conjunction with the **maxchp** argument.
        stabilizeChoice
            A SymbolicConstant specifying whether or not viscous damping will be specified, and if
            so, how it will be specified. Possible values are NONE, AUTOMATIC, and COEFFICIENT. The
            default value is NONE.
        dampFactor
            A Float specifying the value of the damping factor. This value is multiplied by the
            calculated damping coefficient. The default value is 1.0.This argument is only valid
            when **stabilizeChoice** = AUTOMATIC.
        dampCoef
            A Float specifying the damping coefficient. The default value is 0.0.This argument is
            only valid when **stabilizeChoice** = COEFFICIENT.
        tangFraction
            A Float specifying the tangential stabilization as a fraction of the normal
            stabilization (damping). The default value is 1.0.This argument is valid only if
            **stabilizeChoice** = AUTOMATIC or COEFFICIENT.
        eosFraction
            A Float specifying the fraction of the damping that remains at the end of the step. The
            default value is 0.0.This argument is valid only if **stabilizeChoice** = AUTOMATIC or
            COEFFICIENT.
        zeroDampingChoice
            A SymbolicConstant specifying how the zero-damping clearance will be specified. Possible
            values are COMPUTE and SPECIFY. The default value is COMPUTE.This argument is valid only
            if **stabilizeChoice** = AUTOMATIC or COEFFICIENT.
        zeroDamping
            None or a Float specifying the clearance at which damping becomes zero. This argument is
            valid only when **zeroDampingChoice** = SPECIFY. This argument is valid only if
            **stabilizeChoice** = AUTOMATIC or COEFFICIENT. The default value is None.
        enforceWithLagrangeMultipliers
            A SymbolicConstant specifying whether to enforce the contact constraints with Lagrange
            multipliers. Possible values are DEFAULT, ENFORCEMENT_OFF, and ENFORCEMENT_ON. The
            default value is DEFAULT.

        Returns
        -------
        StdContactControl
            A :py:class:`~abaqus.Interaction.StdContactControl.StdContactControl` object.

        Raises
        ------
        RangeError
        """
        self.interactions[name] = interaction = StdContactControl(
            name,
            stiffnessScaleFactor,
            penetrationTolChoice,
            relativePenetrationTolerance,
            absolutePenetrationTolerance,
            frictionOnset,
            automaticTolerances,
            maxchp,
            perrmx,
            uerrmx,
            stabilizeChoice,
            dampFactor,
            dampCoef,
            tangFraction,
            eosFraction,
            zeroDampingChoice,
            zeroDamping,
            enforceWithLagrangeMultipliers,
        )
        return interaction

    def StdInitialization(
        self,
        name: str,
        overclosureType: SymbolicConstant = ADJUST,
        interferenceDistance: float = None,
        clearanceDistance: float = None,
        openingTolerance: float = None,
        overclosureTolerance: float = None,
    ) -> StdInitialization:
        """This method creates a StdInitialization object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].StdInitialization

        Parameters
        ----------
        name
            A String specifying the contact initialization repository key.
        overclosureType
            A SymbolicConstant specifying the type of overclosure to be defined. Possible values are
            ADJUST, INTERFERENCE, and CLEARANCE. The default value is ADJUST.
        interferenceDistance
            None or a Float specifying the interference distance. This argument is valid only when
            **overclosureType** = INTERFERENCE. The default value is None.
        clearanceDistance
            None or a Float specifying the initial clearance distance. This argument is valid only
            when **overclosureType** = CLEARANCE, and must be specified in that case. The default value
            is None.
        openingTolerance
            None or a Float specifying the distance tolerance within which initial openings will
            undergo strain-free adjustments. This argument is not valid when
            **overclosureType** = INTERFERENCE unless a value has been specified for
            **interferenceDistance**. The default value is None.
        overclosureTolerance
            None or a Float specifying the distance tolerance within which initial overclosures will
            undergo strain-free adjustments.. The default value is None.

        Returns
        -------
        StdInitialization
            A :py:class:`~abaqus.Interaction.StdInitialization.StdInitialization` object.

        Raises
        ------
        RangeError
        """
        self.interactions[name] = interaction = StdInitialization(
            name,
            overclosureType,
            interferenceDistance,
            clearanceDistance,
            openingTolerance,
            overclosureTolerance,
        )
        return interaction

    def StdStabilization(
        self,
        name: str,
        zeroDistance: float = None,
        reductionFactor: float = 0,
        scaleFactor: float = 1,
        tangentialFactor: float = 0,
        amplitude: str = "",
        reset: Boolean = OFF,
    ) -> StdStabilization:
        """This method creates a StdStabilization object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].StdStabilization

        Parameters
        ----------
        name
            A String specifying the contact stabilization repository key.
        zeroDistance
            None or a Float specifying the clearance distance at which the stabilization becomes
            zero. The default value is None.
        reductionFactor
            A Float specifying the factor by which the analysis will reduce the contact
            stabilization coefficient per increment. The default value is 0.1.
        scaleFactor
            A Float specifying the factor by which the analysis will scale the contact stabilization
            coefficient. The default value is 1.0.
        tangentialFactor
            A Float specifying the factor that scales the contact stabilization coefficient in the
            tangential direction. The default value is 0.0.
        amplitude
            A String specifying the name of the Amplitude object that defines a time-dependent scale
            factor for contact stabilization over the step. The default value is an empty string.
        reset
            A Boolean specifying whether to cancel carryover effects from contact stabilization
            specifications involving nondefault amplitudes that appeared in previous steps. The
            default value is OFF.

        Returns
        -------
        StdStabilization
            A :py:class:`~abaqus.Interaction.StdStabilization.StdStabilization` object.

        Raises
        ------
        RangeError
        """
        self.interactions[name] = interaction = StdStabilization(
            name,
            zeroDistance,
            reductionFactor,
            scaleFactor,
            tangentialFactor,
            amplitude,
            reset,
        )
        return interaction

    def StdXplCosimulation(
        self,
        name: str,
        createStepName: str,
        region: Region,
        incrementation: SymbolicConstant = ALLOW_SUBCYCLING,
        stepSize: float = 0,
        stepSizeDefinition: SymbolicConstant = DEFAULT,
    ) -> StdXplCosimulation:
        """This method creates a StdXplCosimulation object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].StdXplCosimulation

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the StdXplCosimulation object is
            created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the import and export region upon which the co-simulation
            exchanges data with the coupled analysis program.
        incrementation
            A SymbolicConstant specifying whether the analysis programs use the same time increments
            or one is allowed to use more time increments than the other before exchanging data.
            Possible values are ALLOW_SUBCYCLING and LOCKSTEP. The default value is
            ALLOW_SUBCYCLING.
        stepSize
            A Float specifying the size of the increments to be used by Abaqus/Standard and
            Abaqus/Explicit. The default value is 0.0.
        stepSizeDefinition
            A SymbolicConstant specifying whether the increment size is the analysis default or a
            supplied variable. Possible values are DEFAULT and SPECIFIED. The default value is
            DEFAULT.

        Returns
        -------
        StdXplCosimulation
            A :py:class:`~abaqus.Interaction.StdXplCosimulation.StdXplCosimulation` object.
        """
        self.interactions[name] = interaction = StdXplCosimulation(
            name, createStepName, region, incrementation, stepSize, stepSizeDefinition
        )
        return interaction

    def SurfaceToSurfaceContactExp(
        self,
        name: str,
        createStepName: str,
        main: Region,
        secondary: Region,
        sliding: SymbolicConstant,
        interactionProperty: str,
        mechanicalConstraint: SymbolicConstant = KINEMATIC,
        weightingFactorType: SymbolicConstant = DEFAULT,
        weightingFactor: float = 0,
        contactControls: str = "",
        initialClearance: typing.Union[SymbolicConstant, float] = OMIT,
        halfThreadAngle: str = None,
        pitch: str = None,
        majorBoltDiameter: typing.Union[SymbolicConstant, float] = COMPUTED,
        meanBoltDiameter: typing.Union[SymbolicConstant, float] = COMPUTED,
        datumAxis: DatumAxis = None, 
        useReverseDatumAxis: Boolean = OFF,
        clearanceRegion: Region = None,
    ) -> SurfaceToSurfaceContactExp:
        """This method creates a SurfaceToSurfaceContactExp object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].SurfaceToSurfaceContactExp

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the SurfaceToSurfaceContactExp object
            is created.
        main
            A :py:class:`~abaqus.Region.Region.Region` object specifying the main surface.
        secondary
            A :py:class:`~abaqus.Region.Region.Region` object specifying the secondary surface.
        sliding
            A SymbolicConstant specifying the contact formulation. Possible values are FINITE and
            SMALL.
        interactionProperty
            A String specifying the name of the ContactProperty object associated with this
            interaction.
        mechanicalConstraint
            A SymbolicConstant specifying the mechanical constraint formulation. Possible values are
            KINEMATIC and PENALTY. The default value is KINEMATIC.
        weightingFactorType
            A SymbolicConstant specifying the weighting for node-to-face contact. Possible values
            are DEFAULT and SPECIFIED. The default value is DEFAULT.
        weightingFactor
            A Float specifying the weighting factor for the contact surfaces when
            **weightingFactorType** = SPECIFIED. The default value is 0.0.
        contactControls
            A String specifying the name of the ContactControl object associated with this
            interaction. An empty string indicates that the default contact controls will be used.
            The default value is an empty string.
        initialClearance
            A SymbolicConstant or a Float specifying the initial clearance at regions of contact.
            Possible values are OMIT and COMPUTED. The default value is OMIT.
        halfThreadAngle
            None or a sequence of Floats specifying the half thread angle used for bolt clearance.
            The default value is None.
        pitch
            None or a sequence of Floats specifying the pitch used for bolt clearance. The default
            value is None.
        majorBoltDiameter
            The SymbolicConstant COMPUTED or a Float specifying the major diameter of the bolt used
            for bolt clearance. The default value is COMPUTED.
        meanBoltDiameter
            The SymbolicConstant COMPUTED or a Float specifying the mean diameter of the bolt used
            for bolt clearance. The default value is COMPUTED.
        datumAxis
            A :py:class:`~abaqus.Datum.DatumAxis.DatumAxis` object specifying the orientation of the bolt hole when specifying bolt
            clearance.
        useReverseDatumAxis
            A Boolean specifying whether to reverse the bolt clearance direction given by the datum
            axis. The default value is OFF.
        clearanceRegion
            A :py:class:`~abaqus.Region.Region.Region` object specifying the contact region for which clearance is specified.

        Returns
        -------
        SurfaceToSurfaceContactExp
            A :py:class:`~abaqus.Interaction.SurfaceToSurfaceContactExp.SurfaceToSurfaceContactExp` object.
        """
        self.interactions[name] = interaction = SurfaceToSurfaceContactExp(
            name,
            createStepName,
            main,
            secondary,
            sliding,
            interactionProperty,
            mechanicalConstraint,
            weightingFactorType,
            weightingFactor,
            contactControls,
            initialClearance,
            halfThreadAngle,
            pitch,
            majorBoltDiameter,
            meanBoltDiameter,
            datumAxis,
            useReverseDatumAxis,
            clearanceRegion,
        )
        return interaction

    def SurfaceToSurfaceContactStd(
        self,
        name: str,
        createStepName: str,
        master: Region,
        slave: Region,
        sliding: SymbolicConstant,
        interactionProperty: str,
        interferenceType: SymbolicConstant = NONE,
        overclosure: float = 0,
        interferenceDirectionType: SymbolicConstant = COMPUTED,
        direction: tuple = (),
        amplitude: str = "",
        smooth: float = 0,
        hcrit: float = 0,
        extensionZone: float = 0,
        adjustMethod: SymbolicConstant = NONE,
        adjustTolerance: float = 0,
        adjustSet: Region = None,
        enforcement: SymbolicConstant = SURFACE_TO_SURFACE,
        thickness: Boolean = ON,
        contactControls: str = "",
        tied: Boolean = OFF,
        initialClearance: typing.Union[SymbolicConstant, float] = OMIT,
        halfThreadAngle: str = None,
        pitch: str = None,
        majorBoltDiameter: typing.Union[SymbolicConstant, float] = COMPUTED,
        meanBoltDiameter: typing.Union[SymbolicConstant, float] = COMPUTED,
        datumAxis: DatumAxis = None, 
        useReverseDatumAxis: Boolean = OFF,
        clearanceRegion: Region = None,
        surfaceSmoothing: SymbolicConstant = NONE,
        bondingSet: Region = None,
    ) -> SurfaceToSurfaceContactStd:
        """This method creates a SurfaceToSurfaceContactStd object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].SurfaceToSurfaceContactStd

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the SurfaceToSurfaceContactStd object
            is created.
        master
            A :py:class:`~abaqus.Region.Region.Region` object specifying the main surface.
        slave
            A :py:class:`~abaqus.Region.Region.Region` object specifying the secondary surface.
        sliding
            A SymbolicConstant specifying the contact formulation. Possible values are FINITE and
            SMALL.
        interactionProperty
            A String specifying the name of the ContactProperty object associated with this
            interaction.
        interferenceType
            A SymbolicConstant specifying the type of time-dependent allowable interference for
            contact pairs and contact elements. Possible values are:
            
            - NONE, specifying no allowable contact interference.
            - SHRINK_FIT.
            - UNIFORM.
            
            The default value is NONE.
        overclosure
            A Float specifying the maximum overclosure distance allowed. This argument applies only
            when **interferenceType** = UNIFORM. The default value is 0.0.
        interferenceDirectionType
            A SymbolicConstant specifying the method used to determine the interference direction.
            Possible values are COMPUTED and DIRECTION_COSINE. The default value is COMPUTED.
        direction
            A sequence of three Floats specifying the following:
            
            - XX-direction cosine of the interference direction vector.
            - YY-direction cosine of the interference direction vector.
            - ZZ-direction cosine of the interference direction vector.
            
            This argument is required only when **interferenceDirectionType** = DIRECTION_COSINE.
        amplitude
            A String specifying the name of the amplitude curve that defines the magnitude of the
            prescribed interference during the step. Use None to specify that the prescribed
            interference is applied immediately at the beginning of the step and ramped down to zero
            linearly over the step.
        smooth
            A Float specifying the degree of smoothing used for deformable or rigid main surfaces
            involved when **enforcement** = NODE_TO_SURFACE. The value given must lie between 0.0 and
            0.5. The default value is 0.2.
        hcrit
            A Float specifying the distance by which a secondary node must penetrate the main
            surface before Abaqus/Standard abandons the current increment and tries again with a
            smaller increment. The default value is 0.0.
        extensionZone
            A Float specifying a fraction of the end segment or facet edge length by which the main
            surface is to be extended to avoid numerical round-off errors associated with contact
            modeling. The value given must lie between 0.0 and 0.2. The default value is 0.1.
        adjustMethod
            A SymbolicConstant specifying the adjust method. Possible values are NONE, OVERCLOSED,
            TOLERANCE, and SET. The default value is NONE.
        adjustTolerance
            A Float specifying the adjust tolerance. The default value is 0.0.
        adjustSet
            A :py:class:`~abaqus.Region.Region.Region` object specifying the Set object to which the adjustment is to be applied.
        enforcement
            A SymbolicConstant specifying the discretization method. Possible values are
            NODE_TO_SURFACE and SURFACE_TO_SURFACE. The default value is SURFACE_TO_SURFACE.
        thickness
            A Boolean specifying whether shell/membrane element thickness is considered. The default
            value is ON.This argument is not valid when **sliding** = FINITE and
            **enforcement** = NODE_TO_SURFACE.
        contactControls
            A String specifying the name of the ContactControl object associated with this
            interaction. The empty string indicates that the default contact controls will be used.
            The default value is an empty string.
        tied
            A Boolean specifying whether the surfaces are to be "tied" together for the duration of
            the simulation. The default value is OFF.
        initialClearance
            A SymbolicConstant or a Float specifying the initial clearance at regions of contact.
            Possible values are OMIT and COMPUTED. The default value is OMIT.
        halfThreadAngle
            None or a sequence of Floats specifying the half thread angle used for bolt clearance.
            The default value is None.
        pitch
            None or a sequence of Floats specifying the pitch used for bolt clearance. The default
            value is None.
        majorBoltDiameter
            The SymbolicConstant COMPUTED or a Float specifying the major diameter of the bolt used
            for bolt clearance. The default value is COMPUTED.
        meanBoltDiameter
            The SymbolicConstant COMPUTED or a Float specifying the mean diameter of the bolt used
            for bolt clearance. The default value is COMPUTED.
        datumAxis
            A :py:class:`~abaqus.Datum.DatumAxis.DatumAxis` object specifying the orientation of the bolt hole when specifying bolt
            clearance.
        useReverseDatumAxis
            A Boolean specifying whether to reverse the bolt clearance direction given by the datum
            axis. The default value is OFF.
        clearanceRegion
            A :py:class:`~abaqus.Region.Region.Region` object specifying the contact region for which clearance is specified.
        surfaceSmoothing
            A SymbolicConstant specifying whether to use surface smoothing for geometric surfaces in
            SurfaceToSurfaceContactStd interactions. Possible values are AUTOMATIC and NONE. The
            default value is NONE.
        bondingSet
            A :py:class:`~abaqus.Region.Region.Region` object specifying the secondary node sub-set for bonding, used only when the
            contact property CohesiveBehavior option specifies use.

        Returns
        -------
        SurfaceToSurfaceContactStd
            A :py:class:`~abaqus.Interaction.SurfaceToSurfaceContactStd.SurfaceToSurfaceContactStd` object.
        """
        self.interactions[name] = interaction = SurfaceToSurfaceContactStd(
            name,
            createStepName,
            master,
            slave,
            sliding,
            interactionProperty,
            interferenceType,
            overclosure,
            interferenceDirectionType,
            direction,
            amplitude,
            smooth,
            hcrit,
            extensionZone,
            adjustMethod,
            adjustTolerance,
            adjustSet,
            enforcement,
            thickness,
            contactControls,
            tied,
            initialClearance,
            halfThreadAngle,
            pitch,
            majorBoltDiameter,
            meanBoltDiameter,
            datumAxis,
            useReverseDatumAxis,
            clearanceRegion,
            surfaceSmoothing,
            bondingSet,
        )
        return interaction

    def XFEMCrackGrowth(
        self, name: str, createStepName: str, crackName: str, allowGrowth: Boolean = ON
    ) -> XFEMCrackGrowth:
        """This method creates an XFEMCrackGrowth object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].XFEMCrackGrowth

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the XFEMCrackGrowth object is created.
        crackName
            A String specifying the XFEMCrack object associated with this interaction.
        allowGrowth
            A Boolean specifying whether the crack is allowed to grow (propagate) during this
            analysis step. The default value is ON.

        Returns
        -------
        XFEMCrackGrowth
            A :py:class:`~abaqus.Interaction.XFEMCrackGrowth.XFEMCrackGrowth` object.
        """
        self.interactions[name] = interaction = XFEMCrackGrowth(
            name, createStepName, crackName, allowGrowth
        )
        return interaction
