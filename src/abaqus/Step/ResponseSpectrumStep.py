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
from ..StepMiscellaneous.ResponseSpectrumComponentArray import (
    ResponseSpectrumComponentArray,
)
from ..StepMiscellaneous.SolverControl import SolverControl
from ..StepMiscellaneous.StructuralDamping import StructuralDamping
from ..StepMiscellaneous.StructuralDampingByFrequency import (
    StructuralDampingByFrequency,
)
from ..StepOutput.DiagnosticPrint import DiagnosticPrint
from ..StepOutput.FieldOutputRequestState import FieldOutputRequestState
from ..StepOutput.HistoryOutputRequestState import HistoryOutputRequestState
from ..StepOutput.Monitor import Monitor
from ..StepOutput.Restart import Restart


class ResponseSpectrumStep(AnalysisStep):
    """The ResponseSpectrumStep object is used to calculate estimates of peak values of
    displacements and stresses based on user-supplied response spectra and on the natural
    modes of the system.
    The ResponseSpectrumStep object is derived from the AnalysisStep object.

    Attributes
    ----------
    name: str
        A String specifying the repository key.
    comp: SymbolicConstant
        A SymbolicConstant specifying the order and method used to sum the components. Possible
        values are SINGLE_DIRECTION, MULTIPLE_DIRECTION_ABSOLUTE_SUM,
        MULTIPLE_DIRECTION_SRSS_SUM, MULTIPLE_DIRECTION_THIRTY_PERCENT_RULE, and
        MULTIPLE_DIRECTION_FORTY_PERCENT_RULE. The default value is SINGLE_DIRECTION.
    sum: SymbolicConstant
        A SymbolicConstant specifying the method used to sum the components. Possible values are
        ABS, CQC, NRL, SRSS, TENP, DSC, and GRP. The default value is ABS.
    previous: str
        A String specifying the name of the previous step. The new step appears after this step
        in the list of analysis steps.
    description: str
        A String specifying a description of the new step. The default value is an empty string.
    components: ResponseSpectrumComponentArray
        A :py:class:`~abaqus.StepMiscellaneous.ResponseSpectrumComponentArray.ResponseSpectrumComponentArray` object.
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
    structuralDamping: StructuralDamping
        A :py:class:`~abaqus.StepMiscellaneous.StructuralDamping.StructuralDamping` object.
    structuralDampingByFrequency: StructuralDampingByFrequency
        A :py:class:`~abaqus.StepMiscellaneous.StructuralDampingByFrequency.StructuralDampingByFrequency` object.
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

    - RESPONSE SPECTRUM
            - STEP
    """

    # A String specifying the repository key.
    name: str = ""

    # A SymbolicConstant specifying the order and method used to sum the components. Possible
    # values are SINGLE_DIRECTION, MULTIPLE_DIRECTION_ABSOLUTE_SUM,
    # MULTIPLE_DIRECTION_SRSS_SUM, MULTIPLE_DIRECTION_THIRTY_PERCENT_RULE, and
    # MULTIPLE_DIRECTION_FORTY_PERCENT_RULE. The default value is SINGLE_DIRECTION.
    comp: SymbolicConstant = SINGLE_DIRECTION

    # A SymbolicConstant specifying the method used to sum the components. Possible values are
    # ABS, CQC, NRL, SRSS, TENP, DSC, and GRP. The default value is ABS.
    sum: SymbolicConstant = ABS

    # A String specifying the name of the previous step. The new step appears after this step
    # in the list of analysis steps.
    previous: str = ""

    # A String specifying a description of the new step. The default value is an empty string.
    description: str = ""

    # A :py:class:`~abaqus.StepMiscellaneous.ResponseSpectrumComponentArray.ResponseSpectrumComponentArray` object.
    components: ResponseSpectrumComponentArray = ResponseSpectrumComponentArray()

    # A :py:class:`~abaqus.StepMiscellaneous.DirectDamping.DirectDamping` object.
    directDamping: DirectDamping = DirectDamping()

    # A :py:class:`~abaqus.StepMiscellaneous.CompositeDamping.CompositeDamping` object.
    compositeDamping: CompositeDamping = CompositeDamping()

    # A :py:class:`~abaqus.StepMiscellaneous.RayleighDamping.RayleighDamping` object.
    rayleighDamping: RayleighDamping = RayleighDamping()

    # A :py:class:`~abaqus.StepMiscellaneous.DirectDampingByFrequency.DirectDampingByFrequency` object.
    directDampingByFrequency: DirectDampingByFrequency = DirectDampingByFrequency()

    # A :py:class:`~abaqus.StepMiscellaneous.RayleighDampingByFrequency.RayleighDampingByFrequency` object.
    rayleighDampingByFrequency: RayleighDampingByFrequency = (
        RayleighDampingByFrequency()
    )

    # A :py:class:`~abaqus.StepMiscellaneous.StructuralDamping.StructuralDamping` object.
    structuralDamping: StructuralDamping = StructuralDamping()

    # A :py:class:`~abaqus.StepMiscellaneous.StructuralDampingByFrequency.StructuralDampingByFrequency` object.
    structuralDampingByFrequency: StructuralDampingByFrequency = (
        StructuralDampingByFrequency()
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

    # A :py:class:`~abaqus.StepOutput.DiagnosticPrint.DiagnosticPrint` object.
    diagnosticPrint: DiagnosticPrint = DiagnosticPrint()

    # A :py:class:`~abaqus.StepOutput.Monitor.Monitor` object.
    monitor: Monitor = None

    # A :py:class:`~abaqus.StepOutput.Restart.Restart` object.
    restart: Restart = Restart()

    # A repository of AdaptiveMeshConstraintState objects.
    adaptiveMeshConstraintStates: dict[str, AdaptiveMeshConstraintState] = dict[
        str, AdaptiveMeshConstraintState
    ]()

    # A repository of AdaptiveMeshDomain objects.
    adaptiveMeshDomains: dict[str, AdaptiveMeshDomain] = dict[str, AdaptiveMeshDomain]()

    # A :py:class:`~abaqus.StepMiscellaneous.Control.Control` object.
    control: Control = Control()

    # A :py:class:`~abaqus.StepMiscellaneous.SolverControl.SolverControl` object.
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
        components: ResponseSpectrumComponentArray,
        description: str = "",
        comp: SymbolicConstant = SINGLE_DIRECTION,
        sum: SymbolicConstant = ABS,
        directDamping: DirectDamping = None, 
        compositeDamping: CompositeDamping = None, 
        rayleighDamping: RayleighDamping = None, 
        directDampingByFrequency: DirectDampingByFrequency = None, 
        rayleighDampingByFrequency: RayleighDampingByFrequency = None, 
        maintainAttributes: Boolean = False,
    ):
        """This method creates a ResponseSpectrumStep object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].ResponseSpectrumStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        components
            A :py:class:`~abaqus.StepMiscellaneous.ResponseSpectrumComponentArray.ResponseSpectrumComponentArray` object.
        description
            A String specifying a description of the new step. The default value is an empty string.
        comp
            A SymbolicConstant specifying the order and method used to sum the components. Possible
            values are SINGLE_DIRECTION, MULTIPLE_DIRECTION_ABSOLUTE_SUM,
            MULTIPLE_DIRECTION_SRSS_SUM, MULTIPLE_DIRECTION_THIRTY_PERCENT_RULE, and
            MULTIPLE_DIRECTION_FORTY_PERCENT_RULE. The default value is SINGLE_DIRECTION.
        sum
            A SymbolicConstant specifying the method used to sum the components. Possible values are
            ABS, CQC, NRL, SRSS, TENP, DSC, and GRP. The default value is ABS.
        directDamping
            A :py:class:`~abaqus.StepMiscellaneous.DirectDamping.DirectDamping` object.
        compositeDamping
            A :py:class:`~abaqus.StepMiscellaneous.CompositeDamping.CompositeDamping` object.
        rayleighDamping
            A :py:class:`~abaqus.StepMiscellaneous.RayleighDamping.RayleighDamping` object.
        directDampingByFrequency
            A :py:class:`~abaqus.StepMiscellaneous.DirectDampingByFrequency.DirectDampingByFrequency` object.
        rayleighDampingByFrequency
            A :py:class:`~abaqus.StepMiscellaneous.RayleighDampingByFrequency.RayleighDampingByFrequency` object.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.

        Returns
        -------
        A :py:class:`~abaqus.Step.ResponseSpectrumStep.ResponseSpectrumStep` object.

        Raises
        ------
        RangeError
        """
        super().__init__()
        pass

    def setValues(
        self,
        description: str = "",
        comp: SymbolicConstant = SINGLE_DIRECTION,
        sum: SymbolicConstant = ABS,
        directDamping: DirectDamping = None, 
        compositeDamping: CompositeDamping = None, 
        rayleighDamping: RayleighDamping = None, 
        directDampingByFrequency: DirectDampingByFrequency = None, 
        rayleighDampingByFrequency: RayleighDampingByFrequency = None, 
    ):
        """This method modifies the ResponseSpectrumStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string.
        comp
            A SymbolicConstant specifying the order and method used to sum the components. Possible
            values are SINGLE_DIRECTION, MULTIPLE_DIRECTION_ABSOLUTE_SUM,
            MULTIPLE_DIRECTION_SRSS_SUM, MULTIPLE_DIRECTION_THIRTY_PERCENT_RULE, and
            MULTIPLE_DIRECTION_FORTY_PERCENT_RULE. The default value is SINGLE_DIRECTION.
        sum
            A SymbolicConstant specifying the method used to sum the components. Possible values are
            ABS, CQC, NRL, SRSS, TENP, DSC, and GRP. The default value is ABS.
        directDamping
            A :py:class:`~abaqus.StepMiscellaneous.DirectDamping.DirectDamping` object.
        compositeDamping
            A :py:class:`~abaqus.StepMiscellaneous.CompositeDamping.CompositeDamping` object.
        rayleighDamping
            A :py:class:`~abaqus.StepMiscellaneous.RayleighDamping.RayleighDamping` object.
        directDampingByFrequency
            A :py:class:`~abaqus.StepMiscellaneous.DirectDampingByFrequency.DirectDampingByFrequency` object.
        rayleighDampingByFrequency
            A :py:class:`~abaqus.StepMiscellaneous.RayleighDampingByFrequency.RayleighDampingByFrequency` object.

        Raises
        ------
        RangeError
        """
        pass
