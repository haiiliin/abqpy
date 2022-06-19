from ..Adaptivity.AdaptivityModel import AdaptivityModel
from ..Amplitude.AmplitudeModel import AmplitudeModel
from ..Assembly.AssemblyModel import AssemblyModel
from ..BeamSectionProfile.BeamSectionProfileModel import BeamSectionProfileModel
from ..BoundaryCondition.BoundaryConditionModel import BoundaryConditionModel
from ..Calibration.CalibrationModel import CalibrationModel
from ..Constraint.ConstraintModel import ConstraintModel
from ..Filter.FilterModel import FilterModel
from ..Interaction.InteractionModel import InteractionModel
from ..Load.LoadModel import LoadModel
from ..Material.MaterialModel import MaterialModel
from ..Optimization.OptimizationTaskModel import OptimizationTaskModel
from ..Part.PartModel import PartModel
from ..PredefinedField.PredefinedFieldModel import PredefinedFieldModel
from ..Section.SectionModel import SectionModel
from ..Sketcher.SketchModel import SketchModel
from ..Step.StepModel import StepModel
from ..StepOutput.OutputModel import OutputModel


class Model(
    AdaptivityModel,
    AmplitudeModel,
    AssemblyModel,
    BoundaryConditionModel,
    CalibrationModel,
    ConstraintModel,
    FilterModel,
    InteractionModel,
    LoadModel,
    MaterialModel,
    OptimizationTaskModel,
    PartModel,
    PredefinedFieldModel,
    BeamSectionProfileModel,
    OutputModel,
    SectionModel,
    SketchModel,
    StepModel,
):
    """Abaqus creates a Model object named `Model-1` when a session is started.

    Attributes
    ----------
    name: str
        A String specifying the repository key.
    stefanBoltzmann: float
        None or a Float specifying the Stefan-Boltzmann constant. The default value is None.
    absoluteZero: float
        None or a Float specifying the absolute zero constant. The default value is None.
    waveFormulation: SymbolicConstant
        A SymbolicConstant specifying the type of incident wave formulation to be used in
        acoustic problems. Possible values are NOT_SET, SCATTERED, and TOTAL. The default value
        is NOT_SET.
    universalGas: float
        None or a Float specifying the universal gas constant. The default value is None.
    noPartsInputFile: Boolean
        A Boolean specifying whether an input file should be written without parts and
        assemblies. The default value is OFF.
    restartIncrement: SymbolicConstant
        An Int specifying the increment, interval, iteration or cycle where the restart analysis
        will start. To select the end of the step use the SymbolicConstant STEP_END.
    endRestartStep: Boolean
        A Boolean specifying that the step specified by **restartStep** should be terminated at
        the increment specified by **restartIncrement**.
    shellToSolid: Boolean
        A Boolean specifying that a shell global model drives a solid submodel.
    lastChangedCount: float
        A Float specifying the time stamp that indicates when the model was last changed.
    description: str
        A String specifying the purpose and contents of the :py:class:`~abaqus.Model.Model.Model` object. The default value is
        an empty string.
    restartJob: str
        A String specifying the name of the job that generated the restart data.
    restartStep: str
        A String specifying the name of the step where the restart analysis will start.
    globalJob: str
        A String specifying the name of the job that generated the results for the global model.
    copyConstraints: Boolean
        A boolean specifying the status of constraints created in a model, in the model which
        instances this model.
    copyConnectors: Boolean
        A boolean specifying the status of connectors created in a model, in the model which
        instances this model.
    copyInteractions: Boolean
        A boolean specifying the status of interactions created in a model, in the model which
        instances this model.
    keywordBlock: KeywordBlock
        A :py:class:`~abaqus.Model.KeywordBlock.KeywordBlock` object.
    rootAssembly: Assembly
        An :py:class:`~abaqus.Assembly.Assembly.Assembly` object.
    amplitudes: dict[str, Amplitude]
        A repository of :py:class:`~abaqus.Amplitude.Amplitude.Amplitude` objects.
    profiles: dict[str, Profile]
        A repository of :py:class:`~abaqus.BeamSectionProfile.Profile.Profile` objects.
    boundaryConditions: dict[str, BoundaryCondition]
        A repository of :py:class:`~abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition` objects.
    constraints: dict[str, Constraint]
        A repository of :py:class:`~abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint` objects.
    analyticalFields: dict[str, AnalyticalField]
        A repository of :py:class:`~abaqus.Field.AnalyticalField.AnalyticalField` objects.
    discreteFields: dict[str, DiscreteField]
        A repository of :py:class:`~abaqus.Field.DiscreteField.DiscreteField` objects.
    predefinedFields: dict[str, PredefinedField]
        A repository of :py:class:`~abaqus.PredefinedField.PredefinedField.PredefinedField` objects.
    interactions: dict[str, Interaction]
        A repository of :py:class:`~abaqus.Interaction.Interaction.Interaction` objects.
    interactionProperties: dict[str, ContactProperty]
        A repository of :py:class:`~abaqus.Interaction.InteractionProperty.InteractionProperty` objects.
    contactControls: dict[str, ContactControl]
        A repository of :py:class:`~abaqus.Interaction.ContactControl.ContactControl` objects.
    contactInitializations: dict[str, ContactInitialization]
        A repository of :py:class:`~abaqus.Interaction.ContactInitialization.ContactInitialization` objects.
    contactStabilizations: dict[str, ContactStabilization]
        A repository of :py:class:`~abaqus.Interaction.ContactStabilization.ContactStabilization` objects.
    linkedInstances: tuple
        A tuple of tuples of Strings specifying the linked child PartInstance name in the
        current model to the corresponding parent PartInstance name in a different model.
    linkedParts: tuple
        A tuple of tuples of Strings specifying the linked child Part name in the current model
        to the corresponding parent Part name in a different model.
    loads: dict[str, Load]
        A repository of :py:class:`~abaqus.Load.Load.Load` objects.
    materials: dict[str, Material]
        A repository of :py:class:`~abaqus.Material.Material.Material` objects.
    calibrations: dict[str, Calibration]
        A repository of :py:class:`~abaqus.BoundaryCondition.Calibration.Calibration` objects.
    sections: dict[str, Section]
        A repository of :py:class:`~abaqus.Section.Section.Section` objects.
    remeshingRules: dict[str, RemeshingRule]
        A repository of :py:class:`~abaqus.Adaptivity.RemeshingRule.RemeshingRule` objects.
    sketches: dict[str, ConstrainedSketch]
        A repository of :py:class:`~abaqus.Sketcher.ConstrainedSketch.ConstrainedSketch` objects.
    parts: dict[str, Part]
        A repository of :py:class:`~abaqus.Part.Part.Part` objects.
    steps: dict[str, Step]
        A repository of :py:class:`~abaqus.Step.Step.Step` objects.
    featureOptions: FeatureOptions
        A :py:class:`~abaqus.Feature.FeatureOptions.FeatureOptions` object.
    adaptiveMeshConstraints: dict[str, AdaptiveMeshConstraint]
        A repository of :py:class:`~abaqus.Adaptivity.AdaptiveMeshConstraint.AdaptiveMeshConstraint` objects.
    adaptiveMeshControls: dict[str, AdaptiveMeshControl]
        A repository of :py:class:`~abaqus.Adaptivity.AdaptiveMeshControl.AdaptiveMeshControl` objects.
    timePoints: dict[str, TimePoint]
        A repository of :py:class:`~abaqus.StepOutput.TimePoint.TimePoint` objects.
    filters: dict[str, Filter]
        A repository of :py:class:`~abaqus.Filter.Filter.Filter` objects.
    integratedOutputSections: dict[str, IntegratedOutputSection]
        A repository of :py:class:`~abaqus.StepOutput.IntegratedOutputSection.IntegratedOutputSection` objects.
    fieldOutputRequests: dict[str, FieldOutputRequest]
        A repository of :py:class:`~abaqus.StepOutput.FieldOutputRequest.FieldOutputRequest` objects.
    historyOutputRequests: dict[str, HistoryOutputRequest]
        A repository of :py:class:`~abaqus.StepOutput.HistoryOutputRequest.HistoryOutputRequest` objects.
    optimizationTasks: dict[str, OptimizationTask]
        A repository of :py:class:`~abaqus.Optimization.OptimizationTask.OptimizationTask` objects.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        mdb.models[name]

    The corresponding analysis keywords are:

    - PHYSICAL CONSTANTS

    """

    pass
