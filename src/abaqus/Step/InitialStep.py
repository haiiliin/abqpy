from abaqusConstants import *
from .AnalysisStep import AnalysisStep
from ..Adaptivity.AdaptiveMeshConstraintState import AdaptiveMeshConstraintState
from ..Adaptivity.AdaptiveMeshDomain import AdaptiveMeshDomain
from ..BoundaryCondition.BoundaryConditionState import BoundaryConditionState
from ..Load.LoadCase import LoadCase
from ..Load.LoadState import LoadState
from ..PredefinedField.PredefinedFieldState import PredefinedFieldState
from ..StepMiscellaneous.Control import Control
from ..StepMiscellaneous.SolverControl import SolverControl
from ..StepOutput.DiagnosticPrint import DiagnosticPrint
from ..StepOutput.FieldOutputRequestState import FieldOutputRequestState
from ..StepOutput.HistoryOutputRequestState import HistoryOutputRequestState
from ..StepOutput.Monitor import Monitor
from ..StepOutput.Restart import Restart


class InitialStep(AnalysisStep):
    """The InitialStep object is a placeholder that you cannot create, delete, or modify. The
    InitialStep object exists in every model by default and is used to allow the preexisting
    boundary conditions and interactions to be defined in the model.
    The InitialStep object is derived from the AnalysisStep object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import step
            mdb.models[name].steps[name]
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A SymbolicConstant specifying whether the step has an explicit procedure type
    #: (*procedureType*=ANNEAL, DYNAMIC_EXPLICIT, or DYNAMIC_TEMP_DISPLACEMENT).
    explicit: SymbolicConstant = None

    #: A Boolean specifying whether the step has a perturbation procedure type.
    perturbation: Boolean = OFF

    #: A Boolean specifying whether the step has a mechanical procedure type.
    nonmechanical: Boolean = OFF

    #: A SymbolicConstant specifying the Abaqus procedure. Possible values are:
    #: 
    #: - ANNEAL
    #: - BUCKLE
    #: - COMPLEX_FREQUENCY
    #: - COUPLED_TEMP_DISPLACEMENT
    #: - COUPLED_THERMAL_ELECTRIC
    #: - DIRECT_CYCLIC
    #: - DYNAMIC_IMPLICIT
    #: - DYNAMIC_EXPLICIT
    #: - DYNAMIC_SUBSPACE
    #: - DYNAMIC_TEMP_DISPLACEMENT
    #: - COUPLED_THERMAL_ELECTRICAL_STRUCTURAL
    #: - FREQUENCY
    #: - GEOSTATIC
    #: - HEAT_TRANSFER
    #: - MASS_DIFFUSION
    #: - MODAL_DYNAMICS
    #: - RANDOM_RESPONSE
    #: - RESPONSE_SPECTRUM
    #: - SOILS
    #: - STATIC_GENERAL
    #: - STATIC_LINEAR_PERTURBATION
    #: - STATIC_RIKS
    #: - STEADY_STATE_DIRECT
    #: - STEADY_STATE_MODAL
    #: - STEADY_STATE_SUBSPACE
    #: - VISCO
    procedureType: SymbolicConstant = None

    #: A Boolean specifying whether the step is suppressed or not. The default value is OFF.
    suppressed: Boolean = OFF

    #: A repository of FieldOutputRequestState objects.
    fieldOutputRequestState: dict[str, FieldOutputRequestState] = dict[
        str, FieldOutputRequestState
    ]()

    #: A repository of HistoryOutputRequestState objects.
    historyOutputRequestState: dict[str, HistoryOutputRequestState] = dict[
        str, HistoryOutputRequestState
    ]()

    #: A :py:class:`~abaqus.StepOutput.DiagnosticPrint.DiagnosticPrint` object.
    diagnosticPrint: DiagnosticPrint = DiagnosticPrint()

    #: A :py:class:`~abaqus.StepOutput.Monitor.Monitor` object.
    monitor: Monitor = None

    #: A :py:class:`~abaqus.StepOutput.Restart.Restart` object.
    restart: Restart = Restart()

    #: A repository of AdaptiveMeshConstraintState objects.
    adaptiveMeshConstraintStates: dict[str, AdaptiveMeshConstraintState] = dict[
        str, AdaptiveMeshConstraintState
    ]()

    #: A repository of AdaptiveMeshDomain objects.
    adaptiveMeshDomains: dict[str, AdaptiveMeshDomain] = dict[str, AdaptiveMeshDomain]()

    #: A :py:class:`~abaqus.StepMiscellaneous.Control.Control` object.
    control: Control = Control()

    #: A :py:class:`~abaqus.StepMiscellaneous.SolverControl.SolverControl` object.
    solverControl: SolverControl = SolverControl()

    #: A repository of BoundaryConditionState objects.
    boundaryConditionStates: dict[str, BoundaryConditionState] = dict[
        str, BoundaryConditionState
    ]()

    #: A repository of InteractionState objects.
    interactionStates: int = None

    #: A repository of LoadState objects.
    loadStates: dict[str, LoadState] = dict[str, LoadState]()

    #: A repository of LoadCase objects.
    loadCases: dict[str, LoadCase] = dict[str, LoadCase]()

    #: A repository of PredefinedFieldState objects.
    predefinedFieldStates: dict[str, PredefinedFieldState] = dict[
        str, PredefinedFieldState
    ]()
