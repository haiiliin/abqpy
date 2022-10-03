from abqpy.decorators import abaqus_class_doc
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


@abaqus_class_doc
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

    .. note:: 
        This object can be accessed by::

            mdb.models[name]

        The corresponding analysis keywords are:

        - PHYSICAL CONSTANTS
    """

    ...
