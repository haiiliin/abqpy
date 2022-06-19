from abaqusConstants import *
from .AnalysisStep import AnalysisStep
from ..Adaptivity.AdaptiveMeshConstraintState import AdaptiveMeshConstraintState
from ..Adaptivity.AdaptiveMeshDomain import AdaptiveMeshDomain
from ..BoundaryCondition.BoundaryConditionState import BoundaryConditionState
from ..Load.LoadCase import LoadCase
from ..Load.LoadState import LoadState
from ..PredefinedField.PredefinedFieldState import PredefinedFieldState
from ..StepMiscellaneous.CompositeDamping import CompositeDamping
from ..StepMiscellaneous.Control import Control
from ..StepMiscellaneous.DirectDamping import DirectDamping
from ..StepMiscellaneous.DirectDampingByFrequency import DirectDampingByFrequency
from ..StepMiscellaneous.RayleighDamping import RayleighDamping
from ..StepMiscellaneous.RayleighDampingByFrequency import RayleighDampingByFrequency
from ..StepMiscellaneous.SolverControl import SolverControl
from ..StepOutput.DiagnosticPrint import DiagnosticPrint
from ..StepOutput.FieldOutputRequestState import FieldOutputRequestState
from ..StepOutput.HistoryOutputRequestState import HistoryOutputRequestState
from ..StepOutput.Monitor import Monitor
from ..StepOutput.Restart import Restart


class ModalDynamicsStep(AnalysisStep):
    """The ModalDynamicsStep object is used to provide dynamic time history response as a
    linear perturbation procedure using modal superposition.
    The ModalDynamicsStep object is derived from the AnalysisStep object.

    Attributes
    ----------
    name: str
        A String specifying the repository key.
    continueAnalysis: Boolean
        A Boolean specifying that the step starts with zero initial conditions. The default
        value is OFF.
    timePeriod: float
        A Float specifying the total time period. The default value is 1.0.
    incSize: float
        A Float specifying the time increment to be used. The default value is 1.0.
    amplitude: SymbolicConstant
        A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
        step. Possible values are STEP and RAMP. The default value is STEP.
    previous: str
        A String specifying the name of the previous step. The new step appears after this step
        in the list of analysis steps.
    description: str
        A String specifying a description of the new step. The default value is an empty string.
    directDamping: DirectDamping
        A :py:class:`~abaqus.StepMiscellaneous.DirectDamping.DirectDamping` object.
    compositeDamping: CompositeDamping
        A :py:class:`~abaqus.StepMiscellaneous.CompositeDamping.CompositeDamping` object.
    rayleighDamping: RayleighDamping
        A :py:class:`~abaqus.StepMiscellaneous.RayleighDamping.RayleighDamping` object.
    directDampingByFrequency: DirectDampingByFrequency
        A :py:class:`~abaqus.StepMiscellaneous.DirectDampingByFrequency.DirectDampingByFrequency` object.
    rayleighDampingByFrequency: RayleighDampingByFrequency
        A :py:class:`~abaqus.StepMiscellaneous.RayleighDampingByFrequency.RayleighDampingByFrequency` object.
    explicit: SymbolicConstant
        A SymbolicConstant specifying whether the step has an explicit procedure type
        (**procedureType=ANNEAL**, DYNAMIC_EXPLICIT, or DYNAMIC_TEMP_DISPLACEMENT).
    perturbation: Boolean
        A Boolean specifying whether the step has a perturbation procedure type.
    nonmechanical: Boolean
        A Boolean specifying whether the step has a mechanical procedure type.
    procedureType: SymbolicConstant
        A SymbolicConstant specifying the Abaqus procedure. Possible values are:
            - ANNEAL
            - BUCKLE
            - COMPLEX_FREQUENCY
            - COUPLED_TEMP_DISPLACEMENT
            - COUPLED_THERMAL_ELECTRIC
            - DIRECT_CYCLIC
            - DYNAMIC_IMPLICIT
            - DYNAMIC_EXPLICIT
            - DYNAMIC_SUBSPACE
            - DYNAMIC_TEMP_DISPLACEMENT
            - COUPLED_THERMAL_ELECTRICAL_STRUCTURAL
            - FREQUENCY
            - GEOSTATIC
            - HEAT_TRANSFER
            - MASS_DIFFUSION
            - MODAL_DYNAMICS
            - RANDOM_RESPONSE
            - RESPONSE_SPECTRUM
            - SOILS
            - STATIC_GENERAL
            - STATIC_LINEAR_PERTURBATION
            - STATIC_RIKS
            - STEADY_STATE_DIRECT
            - STEADY_STATE_MODAL
            - STEADY_STATE_SUBSPACE
            - VISCO
    suppressed: Boolean
        A Boolean specifying whether the step is suppressed or not. The default value is OFF.
    fieldOutputRequestState: dict[str, FieldOutputRequestState]
        A repository of :py:class:`~abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState` objects.
    historyOutputRequestState: dict[str, HistoryOutputRequestState]
        A repository of :py:class:`~abaqus.StepOutput.HistoryOutputRequestState.HistoryOutputRequestState` objects.
    diagnosticPrint: DiagnosticPrint
        A :py:class:`~abaqus.StepOutput.DiagnosticPrint.DiagnosticPrint` object.
    monitor: Monitor
        A :py:class:`~abaqus.StepOutput.Monitor.Monitor` object.
    restart: Restart
        A :py:class:`~abaqus.StepOutput.Restart.Restart` object.
    adaptiveMeshConstraintStates: dict[str, AdaptiveMeshConstraintState]
        A repository of :py:class:`~abaqus.Adaptivity.AdaptiveMeshConstraintState.AdaptiveMeshConstraintState` objects.
    adaptiveMeshDomains: dict[str, AdaptiveMeshDomain]
        A repository of :py:class:`~abaqus.Adaptivity.AdaptiveMeshDomain.AdaptiveMeshDomain` objects.
    control: Control
        A :py:class:`~abaqus.StepMiscellaneous.Control.Control` object.
    solverControl: SolverControl
        A :py:class:`~abaqus.StepMiscellaneous.SolverControl.SolverControl` object.
    boundaryConditionStates: dict[str, BoundaryConditionState]
        A repository of :py:class:`~abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState` objects.
    interactionStates: int
        A repository of :py:class:`~abaqus.Interaction.InteractionState.InteractionState` objects.
    loadStates: dict[str, LoadState]
        A repository of :py:class:`~abaqus.Load.LoadState.LoadState` objects.
    loadCases: dict[str, LoadCase]
        A repository of :py:class:`~abaqus.Load.LoadCase.LoadCase` objects.
    predefinedFieldStates: dict[str, PredefinedFieldState]
        A repository of :py:class:`~abaqus.PredefinedField.PredefinedFieldState.PredefinedFieldState` objects.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import step
        mdb.models[name].steps[name]

    The corresponding analysis keywords are:

    - DAMPING
            - MODAL DAMPING
            - MODAL DYNAMIC
            - STEP

    """

    # A String specifying the repository key.
    name: str = ""

    # A Boolean specifying that the step starts with zero initial conditions. The default
    # value is OFF.
    continueAnalysis: Boolean = OFF

    # A Float specifying the total time period. The default value is 1.0.
    timePeriod: float = 1

    # A Float specifying the time increment to be used. The default value is 1.0.
    incSize: float = 1

    # A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
    # step. Possible values are STEP and RAMP. The default value is STEP.
    amplitude: SymbolicConstant = STEP

    # A String specifying the name of the previous step. The new step appears after this step
    # in the list of analysis steps.
    previous: str = ""

    # A String specifying a description of the new step. The default value is an empty string.
    description: str = ""

    # A DirectDamping object.
    directDamping: DirectDamping = DirectDamping()

    # A CompositeDamping object.
    compositeDamping: CompositeDamping = CompositeDamping()

    # A RayleighDamping object.
    rayleighDamping: RayleighDamping = RayleighDamping()

    # A DirectDampingByFrequency object.
    directDampingByFrequency: DirectDampingByFrequency = DirectDampingByFrequency()

    # A RayleighDampingByFrequency object.
    rayleighDampingByFrequency: RayleighDampingByFrequency = (
        RayleighDampingByFrequency()
    )

    # A SymbolicConstant specifying whether the step has an explicit procedure type
    # (*procedureType*=ANNEAL, DYNAMIC_EXPLICIT, or DYNAMIC_TEMP_DISPLACEMENT).
    explicit: SymbolicConstant = None

    # A Boolean specifying whether the step has a perturbation procedure type.
    perturbation: Boolean = OFF

    # A Boolean specifying whether the step has a mechanical procedure type.
    nonmechanical: Boolean = OFF

    # A SymbolicConstant specifying the Abaqus procedure. Possible values are:
    # - ANNEAL
    # - BUCKLE
    # - COMPLEX_FREQUENCY
    # - COUPLED_TEMP_DISPLACEMENT
    # - COUPLED_THERMAL_ELECTRIC
    # - DIRECT_CYCLIC
    # - DYNAMIC_IMPLICIT
    # - DYNAMIC_EXPLICIT
    # - DYNAMIC_SUBSPACE
    # - DYNAMIC_TEMP_DISPLACEMENT
    # - COUPLED_THERMAL_ELECTRICAL_STRUCTURAL
    # - FREQUENCY
    # - GEOSTATIC
    # - HEAT_TRANSFER
    # - MASS_DIFFUSION
    # - MODAL_DYNAMICS
    # - RANDOM_RESPONSE
    # - RESPONSE_SPECTRUM
    # - SOILS
    # - STATIC_GENERAL
    # - STATIC_LINEAR_PERTURBATION
    # - STATIC_RIKS
    # - STEADY_STATE_DIRECT
    # - STEADY_STATE_MODAL
    # - STEADY_STATE_SUBSPACE
    # - VISCO
    procedureType: SymbolicConstant = None

    # A Boolean specifying whether the step is suppressed or not. The default value is OFF.
    suppressed: Boolean = OFF

    # A repository of FieldOutputRequestState objects.
    fieldOutputRequestState: dict[str, FieldOutputRequestState] = dict[
        str, FieldOutputRequestState
    ]()

    # A repository of HistoryOutputRequestState objects.
    historyOutputRequestState: dict[str, HistoryOutputRequestState] = dict[
        str, HistoryOutputRequestState
    ]()

    # A DiagnosticPrint object.
    diagnosticPrint: DiagnosticPrint = DiagnosticPrint()

    # A Monitor object.
    monitor: Monitor = None

    # A Restart object.
    restart: Restart = Restart()

    # A repository of AdaptiveMeshConstraintState objects.
    adaptiveMeshConstraintStates: dict[str, AdaptiveMeshConstraintState] = dict[
        str, AdaptiveMeshConstraintState
    ]()

    # A repository of AdaptiveMeshDomain objects.
    adaptiveMeshDomains: dict[str, AdaptiveMeshDomain] = dict[str, AdaptiveMeshDomain]()

    # A Control object.
    control: Control = Control()

    # A SolverControl object.
    solverControl: SolverControl = SolverControl()

    # A repository of BoundaryConditionState objects.
    boundaryConditionStates: dict[str, BoundaryConditionState] = dict[
        str, BoundaryConditionState
    ]()

    # A repository of InteractionState objects.
    interactionStates: int = None

    # A repository of LoadState objects.
    loadStates: dict[str, LoadState] = dict[str, LoadState]()

    # A repository of LoadCase objects.
    loadCases: dict[str, LoadCase] = dict[str, LoadCase]()

    # A repository of PredefinedFieldState objects.
    predefinedFieldStates: dict[str, PredefinedFieldState] = dict[
        str, PredefinedFieldState
    ]()

    def __init__(
        self,
        name: str,
        previous: str,
        description: str = "",
        continueAnalysis: Boolean = OFF,
        timePeriod: float = 1,
        incSize: float = 1,
        directDamping: DirectDamping = None, 
        compositeDamping: CompositeDamping = None, 
        rayleighDamping: RayleighDamping = None, 
        amplitude: SymbolicConstant = STEP,
        maintainAttributes: Boolean = False,
        directDampingByFrequency: DirectDampingByFrequency = None, 
        rayleighDampingByFrequency: RayleighDampingByFrequency = None, 
    ):
        """This method creates a ModalDynamicsStep object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].ModalDynamicsStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        continueAnalysis
            A Boolean specifying that the step starts with zero initial conditions. The default
            value is OFF.
        timePeriod
            A Float specifying the total time period. The default value is 1.0.
        incSize
            A Float specifying the time increment to be used. The default value is 1.0.
        directDamping
            A DirectDamping object.
        compositeDamping
            A CompositeDamping object.
        rayleighDamping
            A RayleighDamping object.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. Possible values are STEP and RAMP. The default value is STEP.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        directDampingByFrequency
            A DirectDampingByFrequency object.
        rayleighDampingByFrequency
            A RayleighDampingByFrequency object.

        Returns
        -------
            A ModalDynamicsStep object.

        Raises
        ------
        RangeError
        """
        super().__init__()
        pass

    def setValues(
        self,
        description: str = "",
        continueAnalysis: Boolean = OFF,
        timePeriod: float = 1,
        incSize: float = 1,
        directDamping: DirectDamping = None, 
        compositeDamping: CompositeDamping = None, 
        rayleighDamping: RayleighDamping = None, 
        amplitude: SymbolicConstant = STEP,
        directDampingByFrequency: DirectDampingByFrequency = None, 
        rayleighDampingByFrequency: RayleighDampingByFrequency = None, 
    ):
        """This method modifies the ModalDynamicsStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string.
        continueAnalysis
            A Boolean specifying that the step starts with zero initial conditions. The default
            value is OFF.
        timePeriod
            A Float specifying the total time period. The default value is 1.0.
        incSize
            A Float specifying the time increment to be used. The default value is 1.0.
        directDamping
            A DirectDamping object.
        compositeDamping
            A CompositeDamping object.
        rayleighDamping
            A RayleighDamping object.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. Possible values are STEP and RAMP. The default value is STEP.
        directDampingByFrequency
            A DirectDampingByFrequency object.
        rayleighDampingByFrequency
            A RayleighDampingByFrequency object.

        Raises
        ------
        RangeError
        """
        pass
