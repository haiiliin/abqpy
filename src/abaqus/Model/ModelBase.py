from typing import Dict, Optional

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Adaptivity.AdaptiveMeshConstraint import AdaptiveMeshConstraint
from ..Adaptivity.AdaptiveMeshControl import AdaptiveMeshControl
from ..Adaptivity.RemeshingRule import RemeshingRule
from ..Amplitude.Amplitude import Amplitude
from ..Assembly.Assembly import Assembly
from ..BeamSectionProfile.Profile import Profile
from ..BoundaryCondition.BoundaryCondition import BoundaryCondition
from ..Calibration.Calibration import Calibration
from ..Constraint.Constraint import Constraint
from ..Feature.FeatureOptions import FeatureOptions
from ..Field.AnalyticalField import AnalyticalField
from ..Field.DiscreteField import DiscreteField
from ..Filter.Filter import Filter
from ..Interaction.ContactControl import ContactControl
from ..Interaction.ContactInitialization import ContactInitialization
from ..Interaction.ContactProperty import ContactProperty
from ..Interaction.ContactStabilization import ContactStabilization
from ..Interaction.Interaction import Interaction
from ..Load.Load import Load
from ..Material.Material import Material
from ..Optimization.OptimizationTask import OptimizationTask
from ..Part.Part import Part
from ..PredefinedField.PredefinedField import PredefinedField
from ..Section.Section import Section
from ..Sketcher.ConstrainedSketch import ConstrainedSketch
from ..Step.InitialStep import InitialStep
from ..Step.Step import Step
from ..StepOutput.FieldOutputRequest import FieldOutputRequest
from ..StepOutput.HistoryOutputRequest import HistoryOutputRequest
from ..StepOutput.IntegratedOutputSection import IntegratedOutputSection
from ..StepOutput.TimePoint import TimePoint
from ..TableCollection.EventSeriesData import EventSeriesData
from ..TableCollection.EventSeriesType import EventSeriesType
from ..TableCollection.TableCollection import TableCollection
from ..UtilityAndView.abaqusConstants import (
    B31,
    C3D8I,
    C3D10,
    NOT_SET,
    OFF,
    ON,
    PRESERVE_SECTION,
    S4,
    STANDARD_EXPLICIT,
    Boolean,
    SymbolicConstant,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .KeywordBlock import KeywordBlock


@abaqus_class_doc
class ModelBase:
    """Abaqus creates a Model object named `Model-1` when a session is started.

    .. note::
        This object can be accessed by::

            mdb.models[name]

        The corresponding analysis keywords are:

        - PHYSICAL CONSTANTS
    """

    #: A String specifying the repository key.
    name: str = ""

    #: None or a Float specifying the Stefan-Boltzmann constant. The default value is None.
    stefanBoltzmann: Optional[float] = None

    #: None or a Float specifying the absolute zero constant. The default value is None.
    absoluteZero: Optional[float] = None

    #: A SymbolicConstant specifying the type of incident wave formulation to be used in
    #: acoustic problems. Possible values are NOT_SET, SCATTERED, and TOTAL. The default value
    #: is NOT_SET.
    waveFormulation: SymbolicConstant = NOT_SET

    #: None or a Float specifying the universal gas constant. The default value is None.
    universalGas: Optional[float] = None

    #: A Boolean specifying whether an input file should be written without parts and
    #: assemblies. The default value is OFF.
    noPartsInputFile: Boolean = OFF

    #: An Int specifying the increment, interval, iteration or cycle where the restart analysis
    #: will start. To select the end of the step use the SymbolicConstant STEP_END.
    restartIncrement: Optional[SymbolicConstant] = None

    #: A Boolean specifying that the step specified by **restartStep** should be terminated at
    #: the increment specified by **restartIncrement**.
    endRestartStep: Boolean = OFF

    #: A Boolean specifying that a shell global model drives a solid submodel.
    shellToSolid: Boolean = OFF

    #: A Float specifying the time stamp that indicates when the model was last changed.
    lastChangedCount: Optional[float] = None

    #: A String specifying the purpose and contents of the Model object. The default value is
    #: an empty string.
    description: str = ""

    #: A String specifying the name of the job that generated the restart data.
    restartJob: str = ""

    #: A String specifying the name of the step where the restart analysis will start.
    restartStep: str = ""

    #: A String specifying the name of the job that generated the results for the global model.
    globalJob: str = ""

    #: A boolean specifying the status of constraints created in a model, in the model which
    #: instances this model.
    copyConstraints: Boolean = OFF

    #: A boolean specifying the status of connectors created in a model, in the model which
    #: instances this model.
    copyConnectors: Boolean = OFF

    #: A boolean specifying the status of interactions created in a model, in the model which
    #: instances this model.
    copyInteractions: Boolean = OFF

    #: A KeywordBlock object.
    keywordBlock: KeywordBlock = KeywordBlock()

    #: An Assembly object.
    rootAssembly: Assembly = Assembly()

    #: A repository of Amplitude objects.
    amplitudes: Dict[str, Amplitude] = {}

    #: A repository of Profile objects.
    profiles: Dict[str, Profile] = {}

    #: A repository of BoundaryCondition objects.
    boundaryConditions: Dict[str, BoundaryCondition] = {}

    #: A repository of ConstrainedSketchConstraint objects.
    constraints: Dict[str, Constraint] = {}

    #: A repository of AnalyticalField objects.
    analyticalFields: Dict[str, AnalyticalField] = {}

    #: A repository of DiscreteField objects.
    discreteFields: Dict[str, DiscreteField] = {}

    #: A repository of PredefinedField objects.
    predefinedFields: Dict[str, PredefinedField] = {}

    #: A repository of Interaction objects.
    interactions: Dict[str, Interaction] = {}

    #: A repository of InteractionProperty objects.
    interactionProperties: Dict[str, ContactProperty] = {}

    #: A repository of ContactControl objects.
    contactControls: Dict[str, ContactControl] = {}

    #: A repository of ContactInitialization objects.
    contactInitializations: Dict[str, ContactInitialization] = {}

    #: A repository of ContactStabilization objects.
    contactStabilizations: Dict[str, ContactStabilization] = {}

    #: A tuple of tuples of Strings specifying the linked child PartInstance name in the
    #: current model to the corresponding parent PartInstance name in a different model.
    linkedInstances: tuple = ()

    #: A tuple of tuples of Strings specifying the linked child Part name in the current model
    #: to the corresponding parent Part name in a different model.
    linkedParts: tuple = ()

    #: A repository of Load objects.
    loads: Dict[str, Load] = {}

    #: A repository of Material objects.
    materials: Dict[str, Material] = {}

    #: A repository of Calibration objects.
    calibrations: Dict[str, Calibration] = {}

    #: A repository of Section objects.
    sections: Dict[str, Section] = {}

    #: A repository of RemeshingRule objects.
    remeshingRules: Dict[str, RemeshingRule] = {}

    #: A repository of ConstrainedSketch objects.
    sketches: Dict[str, ConstrainedSketch] = {}

    #: A repository of Part objects.
    parts: Dict[str, Part] = {}

    #: A repository of Step objects.
    steps: Dict[str, Step] = {}

    #: A FeatureOptions object.
    featureOptions: FeatureOptions = FeatureOptions()

    #: A repository of AdaptiveMeshConstraint objects.
    adaptiveMeshConstraints: Dict[str, AdaptiveMeshConstraint] = {}

    #: A repository of AdaptiveMeshControl objects.
    adaptiveMeshControls: Dict[str, AdaptiveMeshControl] = {}

    #: A repository of TimePoint objects.
    timePoints: Dict[str, TimePoint] = {}

    #: A repository of Filter objects.
    filters: Dict[str, Filter] = {}

    #: A repository of IntegratedOutputSection objects.
    integratedOutputSections: Dict[str, IntegratedOutputSection] = {}

    #: A repository of FieldOutputRequest objects.
    fieldOutputRequests: Dict[str, FieldOutputRequest] = {}

    #: A repository of HistoryOutputRequest objects.
    historyOutputRequests: Dict[str, HistoryOutputRequest] = {}

    #: A repository of OptimizationTask objects.
    optimizationTasks: Dict[str, OptimizationTask] = {}

    #: A repository of TableCollection objects.
    #:
    #: .. versionadded:: 2020
    #:     The ``tableCollections`` attribute was added.
    tableCollections: Dict[str, TableCollection] = {}

    #: A repository of EventSeriesType objects.
    #:
    #: .. versionadded:: 2020
    #:     The ``eventSeriesTypes`` attribute was added.
    eventSeriesTypes: Dict[str, EventSeriesType] = {}

    #: A repository of EventSeriesData objects.
    #:
    #: .. versionadded:: 2020
    #:     The ``eventSeriesDatas`` attribute was added.
    eventSeriesDatas: Dict[str, EventSeriesData] = {}

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        description: str = "",
        stefanBoltzmann: Optional[float] = None,
        absoluteZero: Optional[float] = None,
        waveFormulation: Literal[C.SCATTERED, C.NOT_SET, C.TOTAL] = NOT_SET,
        modelType: Literal[C.STANDARD_EXPLICIT, C.ELECTROMAGNETIC] = STANDARD_EXPLICIT,
        universalGas: Optional[float] = None,
        copyConstraints: Boolean = ON,
        copyConnectors: Boolean = ON,
        copyInteractions: Boolean = ON,
    ):
        """This method creates a Model object.

        .. note::
            This function can be accessed by::

                mdb.Model

        Parameters
        ----------
        name
            A String specifying the repository key.
        description
            A String specifying the purpose and contents of the Model object. The default value is
            an empty string.
        stefanBoltzmann
            None or a Float specifying the Stefan-Boltzmann constant. The default value is None.
        absoluteZero
            None or a Float specifying the absolute zero constant. The default value is None.
        waveFormulation
            A SymbolicConstant specifying the type of incident wave formulation to be used in
            acoustic problems. Possible values are NOT_SET, SCATTERED, and TOTAL. The default value
            is NOT_SET.
        modelType
            A SymbolicConstant specifying the analysis model type. Possible values are
            STANDARD_EXPLICIT and ELECTROMAGNETIC. The default is STANDARD_EXPLICIT.
        universalGas
            None or a Float specifying the universal gas constant. The default value is None.
        copyConstraints
            A boolean specifying whether to copy the constraints created in the model to the model
            that instances this model. The default value is ON.
        copyConnectors
            A boolean specifying whether to copy the connectors created in the model to the model
            that instances this model. The default value is ON.
        copyInteractions
            A boolean specifying whether to copy the interactions created in the model to the model
            that instances this model. The default value is ON.

        Returns
        -------
        Model
            A Model object.
        """
        self.steps["Initial"] = InitialStep()

    @abaqus_method_doc
    def ModelFromInputFile(self, name: str, inputFileName: str):
        """This method creates a Model object by reading the keywords in an input file and creating the
        corresponding Abaqus/CAE objects.

        .. note::
            This function can be accessed by::

                mdb.Model

        Parameters
        ----------
        name
            A String specifying the repository key.
        inputFileName
            A String specifying the name of the input file (including the .inp extension) to be
            parsed into the new model. This String can also be the full path to the input file if it
            is located in another directory.

        Returns
        -------
        Model
            A Model object.
        """
        ...

    @abaqus_method_doc
    def ModelFromOdbFile(self, name: str, odbFileName: str):
        """This method creates a Model object by reading an output database and creating any corresponding
        Abaqus/CAE objects.

        .. note::
            This function can be accessed by::

                mdb.Model

        Parameters
        ----------
        name
            A String specifying the repository key.
        odbFileName
            A String specifying the name of the output database file (including the .odb extension)
            to be read into the new model. This String can also be the full path to the output
            database file if it is located in another directory.

        Returns
        -------
        Model
            A Model object.
        """
        ...

    @abaqus_method_doc
    def ModelFromNastranFile(
        self,
        modelName: str,
        inputFileName: str,
        sectionConsolidation: Literal[C.PRESERVE_SECTION, C.GROUP_BY_MATERIAL, C.NONE] = PRESERVE_SECTION,
        preIntegratedShell: Boolean = OFF,
        weightMassScaling: Boolean = ON,
        loadCases: Boolean = ON,
        coupleBeamOffsets: Boolean = ON,
        cbar: str = B31,
        cquad4: str = S4,
        chexa: str = C3D8I,
        ctetra: str = C3D10,
        keepTranslatedFiles: Boolean = ON,
    ):
        """This method creates a Model object by reading the keywords in a Nastran bulk data file or Nastran
        input file and creating any corresponding Abaqus/CAE objects. The default values is discussed in
        following and can be defined alternatively in the Abaqus environment file as the one used for the
        translator from Nastran to Abaqus. For more information, see Translating Nastran data to Abaqus files.

        .. note::
            This function can be accessed by::

                mdb.Model

        Parameters
        ----------
        modelName
            A String specifying the repository key.
        inputFileName
            A String specifying the name of the Nastran input file (including the .bdf, .dat, .nas,
            .nastran, .blk, .bulk extension) to be read into the new model. This String can also be
            the full path to the Nastran input file if it is located in another directory.
        sectionConsolidation
            A SymbolicConstant specifying the method used to create shell section. Possible values
            are PRESERVE_SECTION, GROUP_BY_MATERIAL, and NONE. If PRESERVE_SECTION is used, an
            Abaqus section is created corresponding to each shell property ID. If GROUP_BY_MATERIAL
            is used, a single Abaqus section is created for all homogeneous elements referencing the
            same material. In both cases, material orientations and offsets are created using
            discrete fields. If NONE is used, a separate shell section is created for each
            combination of orientation, material offset, and/or thickness. The default is
            PRESERVE_SECTION.
        preIntegratedShell
            A Boolean specifying whether the pre-integrated shell section is created in default for
            shell element. The default value is OFF.
        weightMassScaling
            A Boolean specifying whether the value on the Nastran data line PARAM, WTMASS is used as
            a multiplier for all density, mass, and rotary inertia values created in the Abaqus
            input file. The default value is ON.
        loadCases
            A Boolean specifying whether each SUBCASE for linear static analyses is translated to a
            LOAD CASE option, and all such LOAD CASE options are grouped in a single STEP option.
            The default value is ON.
        coupleBeamOffsets
            A Boolean specifying whether to translate the beam element connectivity to newly created
            nodes at the offset location and rigidly coupling the new and original nodes. If not,
            beam element offsets are translated to the CENTROID and SHEAR CENTER options, which are
            suboptions of the BEAM GENERAL SECTION option. The default value is ON. When the beam
            element references a PBARL or PBEAML property or if the beam offset has a significant
            component in the direction of the beam axis, the setting for this argument is always ON.
        cbar
            A String specifying the 2-node beam that is created from CBAR and CBEAM elements.
            Possible values are B31 and B33. The default is B31.
        cquad4
            A String specifying the 4-node shell that is created from CQUAD4 elements. Possible
            values are S4 and S4R. The default is S4. If a reduced-integration element is chosen,
            the enhanced hourglass formulation is applied automatically.
        chexa
            A String specifying the 8-node brick that is created from CHEXA elements. Possible
            values are C3D8I, C3D8 and C3D8R. The default is C3D8I. If a reduced-integration element
            is chosen, the enhanced hourglass formulation is applied automatically.
        ctetra
            A String specifying the 10-node tetrahedron that is created from CTETRA elements.
            Possible values are C3D10 and C3D10M. The default is C3D10.
        keepTranslatedFiles
            A Boolean specifying whether to keep the generated Abaqus input file after the model is
            created from the Nastran input file. The default value is ON.

        Returns
        -------
        Model
            A Model object.
        """
        ...

    @abaqus_method_doc
    def setValues(
        self,
        description: str = "",
        noPartsInputFile: Boolean = OFF,
        absoluteZero: Optional[float] = None,
        stefanBoltzmann: Optional[float] = None,
        waveFormulation: Literal[C.SCATTERED, C.NOT_SET, C.TOTAL] = NOT_SET,
        universalGas: Optional[float] = None,
        restartJob: str = "",
        restartStep: str = "",
        restartIncrement: Optional[Literal[C.STEP_END]] = None,
        endRestartStep: Boolean = OFF,
        globalJob: str = "",
        shellToSolid: Boolean = OFF,
        copyConstraints: Boolean = OFF,
        copyConnectors: Boolean = OFF,
        copyInteractions: Boolean = OFF,
    ):
        """This method modifies the Model object.

        Parameters
        ----------
        description
            A String specifying the purpose and contents of the Model object. The default value is
            an empty string.
        noPartsInputFile
            A Boolean specifying whether an input file should be written without parts and
            assemblies. The default value is OFF.
        absoluteZero
            None or a Float specifying the absolute zero constant. The default value is None.
        stefanBoltzmann
            None or a Float specifying the Stefan-Boltzmann constant. The default value is None.
        waveFormulation
            A SymbolicConstant specifying the type of incident wave formulation to be used in
            acoustic problems. Possible values are NOT_SET, SCATTERED, and TOTAL. The default value
            is NOT_SET.
        universalGas
            None or a Float specifying the universal gas constant. The default value is None.
        restartJob
            A String specifying the name of the job that generated the restart data.
        restartStep
            A String specifying the name of the step where the restart analysis will start.
        restartIncrement
            An Int specifying the increment, interval, iteration or cycle where the restart analysis
            will start. To select the end of the step use the SymbolicConstant STEP_END.
        endRestartStep
            A Boolean specifying that the step specified by **restartStep** should be terminated at
            the increment specified by **restartIncrement**.
        globalJob
            A String specifying the name of the job that generated the results for the global model.
        shellToSolid
            A Boolean specifying that a shell global model drives a solid submodel.
        copyConstraints
            A Boolean specifying whether to copy the constraints created in the model to the model
            that instances this model.
        copyConnectors
            A Boolean specifying whether to copy the connectors created in the model to the model
            that instances this model
        copyInteractions
            A Boolean specifying whether to copy the interactions created in the model to the model
            that instances this model.
        """
        ...
