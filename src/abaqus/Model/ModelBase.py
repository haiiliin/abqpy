from __future__ import annotations

from typing import TYPE_CHECKING

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Adaptivity.AdaptiveMeshConstraint import AdaptiveMeshConstraint
from ..Adaptivity.AdaptiveMeshControl import AdaptiveMeshControl
from ..Adaptivity.RemeshingRule import RemeshingRule
from ..Amplitude.Amplitude import Amplitude
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
    NOT_SET,
    OFF,
    ON,
    STANDARD_EXPLICIT,
    Boolean,
    SymbolicConstant,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .KeywordBlock import KeywordBlock

if TYPE_CHECKING:
    from ..Assembly.Assembly import Assembly


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
    stefanBoltzmann: float | None = None

    #: None or a Float specifying the absolute zero constant. The default value is None.
    absoluteZero: float | None = None

    #: A SymbolicConstant specifying the type of incident wave formulation to be used in
    #: acoustic problems. Possible values are NOT_SET, SCATTERED, and TOTAL. The default value
    #: is NOT_SET.
    waveFormulation: SymbolicConstant = NOT_SET

    #: None or a Float specifying the universal gas constant. The default value is None.
    universalGas: float | None = None

    #: A Boolean specifying whether an input file should be written without parts and
    #: assemblies. The default value is OFF.
    noPartsInputFile: Boolean = OFF

    #: An Int specifying the increment, interval, iteration or cycle where the restart analysis
    #: will start. To select the end of the step use the SymbolicConstant STEP_END.
    restartIncrement: int | SymbolicConstant

    #: A Boolean specifying that the step specified by **restartStep** should be terminated at
    #: the increment specified by **restartIncrement**.
    endRestartStep: Boolean = OFF

    #: A Boolean specifying that a shell global model drives a solid submodel.
    shellToSolid: Boolean = OFF

    #: A Float specifying the time stamp that indicates when the model was last changed.
    lastChangedCount: float | None = None

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
    rootAssembly: Assembly

    #: A repository of Amplitude objects.
    amplitudes: dict[str, Amplitude] = {}

    #: A repository of Profile objects.
    profiles: dict[str, Profile] = {}

    #: A repository of BoundaryCondition objects.
    boundaryConditions: dict[str, BoundaryCondition] = {}

    #: A repository of ConstrainedSketchConstraint objects.
    constraints: dict[str, Constraint] = {}

    #: A repository of AnalyticalField objects.
    analyticalFields: dict[str, AnalyticalField] = {}

    #: A repository of DiscreteField objects.
    discreteFields: dict[str, DiscreteField] = {}

    #: A repository of PredefinedField objects.
    predefinedFields: dict[str, PredefinedField] = {}

    #: A repository of Interaction objects.
    interactions: dict[str, Interaction] = {}

    #: A repository of InteractionProperty objects.
    interactionProperties: dict[str, ContactProperty] = {}

    #: A repository of ContactControl objects.
    contactControls: dict[str, ContactControl] = {}

    #: A repository of ContactInitialization objects.
    contactInitializations: dict[str, ContactInitialization] = {}

    #: A repository of ContactStabilization objects.
    contactStabilizations: dict[str, ContactStabilization] = {}

    #: A tuple of tuples of Strings specifying the linked child PartInstance name in the
    #: current model to the corresponding parent PartInstance name in a different model.
    linkedInstances: tuple = ()

    #: A tuple of tuples of Strings specifying the linked child Part name in the current model
    #: to the corresponding parent Part name in a different model.
    linkedParts: tuple = ()

    #: A repository of Load objects.
    loads: dict[str, Load] = {}

    #: A repository of Material objects.
    materials: dict[str, Material] = {}

    #: A repository of Calibration objects.
    calibrations: dict[str, Calibration] = {}

    #: A repository of Section objects.
    sections: dict[str, Section] = {}

    #: A repository of RemeshingRule objects.
    remeshingRules: dict[str, RemeshingRule] = {}

    #: A repository of ConstrainedSketch objects.
    sketches: dict[str, ConstrainedSketch] = {}

    #: A repository of Part objects.
    parts: dict[str, Part] = {}

    #: A repository of Step objects.
    steps: dict[str, Step] = {}

    #: A FeatureOptions object.
    featureOptions: FeatureOptions = FeatureOptions()

    #: A repository of AdaptiveMeshConstraint objects.
    adaptiveMeshConstraints: dict[str, AdaptiveMeshConstraint] = {}

    #: A repository of AdaptiveMeshControl objects.
    adaptiveMeshControls: dict[str, AdaptiveMeshControl] = {}

    #: A repository of TimePoint objects.
    timePoints: dict[str, TimePoint] = {}

    #: A repository of Filter objects.
    filters: dict[str, Filter] = {}

    #: A repository of IntegratedOutputSection objects.
    integratedOutputSections: dict[str, IntegratedOutputSection] = {}

    #: A repository of FieldOutputRequest objects.
    fieldOutputRequests: dict[str, FieldOutputRequest] = {}

    #: A repository of HistoryOutputRequest objects.
    historyOutputRequests: dict[str, HistoryOutputRequest] = {}

    #: A repository of OptimizationTask objects.
    optimizationTasks: dict[str, OptimizationTask] = {}

    #: A repository of TableCollection objects.
    #:
    #: .. versionadded:: 2020
    #:     The ``tableCollections`` attribute was added.
    tableCollections: dict[str, TableCollection] = {}

    #: A repository of EventSeriesType objects.
    #:
    #: .. versionadded:: 2020
    #:     The ``eventSeriesTypes`` attribute was added.
    eventSeriesTypes: dict[str, EventSeriesType] = {}

    #: A repository of EventSeriesData objects.
    #:
    #: .. versionadded:: 2020
    #:     The ``eventSeriesDatas`` attribute was added.
    eventSeriesDatas: dict[str, EventSeriesData] = {}

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        description: str = "",
        stefanBoltzmann: float | None = None,
        absoluteZero: float | None = None,
        waveFormulation: Literal[C.SCATTERED, C.NOT_SET, C.TOTAL] = NOT_SET,
        modelType: Literal[C.STANDARD_EXPLICIT, C.ELECTROMAGNETIC] = STANDARD_EXPLICIT,
        universalGas: float | None = None,
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
        from ..Assembly.Assembly import Assembly

        self.steps["Initial"] = InitialStep()
        self.rootAssembly = Assembly()

    @abaqus_method_doc
    def setValues(
        self,
        description: str = "",
        noPartsInputFile: Boolean = OFF,
        absoluteZero: float | None = None,
        stefanBoltzmann: float | None = None,
        waveFormulation: Literal[C.SCATTERED, C.NOT_SET, C.TOTAL] = NOT_SET,
        universalGas: float | None = None,
        restartJob: str = "",
        restartStep: str = "",
        restartIncrement: Literal[C.STEP_END] | None = None,
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
