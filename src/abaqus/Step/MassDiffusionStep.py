from typing import Dict, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

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
from ..UtilityAndView.abaqusConstants import (
    AUTOMATIC,
    Boolean,
    LINEAR,
    OFF,
    PERIOD,
    PROPAGATED,
    STEP,
    SymbolicConstant,
    TRANSIENT,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class MassDiffusionStep(AnalysisStep):
    """The MassDiffusionStep object is used to control uncoupled transient or steady-state mass
    diffusion analysis.
    The MassDiffusionStep object is derived from the AnalysisStep object.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name]

        The corresponding analysis keywords are:

        - MASS DIFFUSION
        - STEP
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and
    #: TRANSIENT. The default value is TRANSIENT.
    response: SymbolicConstant = TRANSIENT

    #: A Float specifying the total time period. The default value is 1.0.
    timePeriod: float = 1

    #: A SymbolicConstant specifying the time incrementation method to be used. Possible values
    #: are FIXED and AUTOMATIC. The default value is AUTOMATIC.
    timeIncrementationMethod: SymbolicConstant = AUTOMATIC

    #: An Int specifying the maximum number of increments in a step. The default value is 100.
    maxNumInc: int = 100

    #: A Float specifying the initial time increment. The default value is the total time
    #: period for the step.
    initialInc: Optional[float] = None

    #: A Float specifying the minimum time increment allowed. The default value is the smaller
    #: of 0.8 times the initial time increment or 10−5 times the total time period.
    minInc: Optional[float] = None

    #: A Float specifying the maximum time increment allowed. The default value is the total
    #: time period for the step.
    maxInc: Optional[float] = None

    #: A SymbolicConstant specifying the time period to be analyzed in a transient analysis.
    #: Possible values are PERIOD and SS. The default value is PERIOD.
    end: SymbolicConstant = PERIOD

    #: A Float specifying the maximum normalized concentration change to be allowed in an
    #: increment. The default value is 0.0.
    dcmax: float = 0

    #: A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
    #: step. The default is STEP. Possible values are STEP and RAMP.
    amplitude: SymbolicConstant = STEP

    #: A SymbolicConstant specifying the type of extrapolation to use in determining the
    #: incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and
    #: PARABOLIC. The default value is LINEAR.
    extrapolation: SymbolicConstant = LINEAR

    #: A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
    #: occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
    #: CONVERT_SDI_ON. The default value is PROPAGATED.
    convertSDI: SymbolicConstant = PROPAGATED

    #: A String specifying the name of the previous step. The new step appears after this step
    #: in the list of analysis steps.
    previous: str = ""

    #: A String specifying a description of the new step. The default value is an empty string.
    description: str = ""

    #: A SymbolicConstant specifying whether the step has an explicit procedure type
    #: (*procedureType* = ANNEAL, DYNAMIC_EXPLICIT, or DYNAMIC_TEMP_DISPLACEMENT).
    explicit: Optional[SymbolicConstant] = None

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
    procedureType: Optional[SymbolicConstant] = None

    #: A Boolean specifying whether the step is suppressed or not. The default value is OFF.
    suppressed: Boolean = OFF

    #: A repository of FieldOutputRequestState objects.
    fieldOutputRequestState: Dict[str, FieldOutputRequestState] = {}

    #: A repository of HistoryOutputRequestState objects.
    historyOutputRequestState: Dict[str, HistoryOutputRequestState] = {}

    #: A DiagnosticPrint object.
    diagnosticPrint: DiagnosticPrint = DiagnosticPrint()

    #: A Monitor object.
    monitor: Optional[Monitor] = None

    #: A Restart object.
    restart: Restart = Restart()

    #: A repository of AdaptiveMeshConstraintState objects.
    adaptiveMeshConstraintStates: Dict[str, AdaptiveMeshConstraintState] = {}

    #: A repository of AdaptiveMeshDomain objects.
    adaptiveMeshDomains: Dict[str, AdaptiveMeshDomain] = {}

    #: A Control object.
    control: Control = Control()

    #: A SolverControl object.
    solverControl: SolverControl = SolverControl()

    #: A repository of BoundaryConditionState objects.
    boundaryConditionStates: Dict[str, BoundaryConditionState] = {}

    #: A repository of InteractionState objects.
    interactionStates: Optional[int] = None

    #: A repository of LoadState objects.
    loadStates: Dict[str, LoadState] = {}

    #: A repository of LoadCase objects.
    loadCases: Dict[str, LoadCase] = {}

    #: A repository of PredefinedFieldState objects.
    predefinedFieldStates: Dict[str, PredefinedFieldState] = {}

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        previous: str,
        description: str = "",
        response: Literal[C.TRANSIENT, C.STEADY_STATE] = TRANSIENT,
        timePeriod: float = 1,
        timeIncrementationMethod: Literal[C.AUTOMATIC, C.FIXED] = AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Optional[float] = None,
        end: Literal[C.SS, C.PERIOD] = PERIOD,
        dcmax: float = 0,
        amplitude: Literal[C.STEP, C.RAMP] = STEP,
        extrapolation: Literal[C.PARABOLIC, C.NONE, C.LINEAR] = LINEAR,
        maintainAttributes: Boolean = False,
        convertSDI: Literal[C.CONVERT_SDI_OFF, C.PROPAGATED, C.CONVERT_SDI_ON] = PROPAGATED,
    ):
        """This method creates a MassDiffusionStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].MassDiffusionStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        response
            A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and
            TRANSIENT. The default value is TRANSIENT.
        timePeriod
            A Float specifying the total time period. The default value is 1.0.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are FIXED and AUTOMATIC. The default value is AUTOMATIC.
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100.
        initialInc
            A Float specifying the initial time increment. The default value is the total time
            period for the step.
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller
            of 0.8 times the initial time increment or 10−5 times the total time period.
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total
            time period for the step.
        end
            A SymbolicConstant specifying the time period to be analyzed in a transient analysis.
            Possible values are PERIOD and SS. The default value is PERIOD.
        dcmax
            A Float specifying the maximum normalized concentration change to be allowed in an
            increment. The default value is 0.0.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. The default is STEP. Possible values are STEP and RAMP.
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and
            PARABOLIC. The default value is LINEAR.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
            CONVERT_SDI_ON. The default value is PROPAGATED.

        Returns
        -------
        MassDiffusionStep
            A MassDiffusionStep object.

        Raises
        ------
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        description: str = "",
        response: Literal[C.TRANSIENT, C.STEADY_STATE] = TRANSIENT,
        timePeriod: float = 1,
        timeIncrementationMethod: Literal[C.AUTOMATIC, C.FIXED] = AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Optional[float] = None,
        end: Literal[C.SS, C.PERIOD] = PERIOD,
        dcmax: float = 0,
        amplitude: Literal[C.STEP, C.RAMP] = STEP,
        extrapolation: Literal[C.PARABOLIC, C.NONE, C.LINEAR] = LINEAR,
        convertSDI: Literal[C.CONVERT_SDI_OFF, C.PROPAGATED, C.CONVERT_SDI_ON] = PROPAGATED,
    ):
        """This method modifies the MassDiffusionStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string.
        response
            A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and
            TRANSIENT. The default value is TRANSIENT.
        timePeriod
            A Float specifying the total time period. The default value is 1.0.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are FIXED and AUTOMATIC. The default value is AUTOMATIC.
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100.
        initialInc
            A Float specifying the initial time increment. The default value is the total time
            period for the step.
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller
            of 0.8 times the initial time increment or 10−5 times the total time period.
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total
            time period for the step.
        end
            A SymbolicConstant specifying the time period to be analyzed in a transient analysis.
            Possible values are PERIOD and SS. The default value is PERIOD.
        dcmax
            A Float specifying the maximum normalized concentration change to be allowed in an
            increment. The default value is 0.0.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. The default is STEP. Possible values are STEP and RAMP.
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and
            PARABOLIC. The default value is LINEAR.
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
            CONVERT_SDI_ON. The default value is PROPAGATED.

        Raises
        ------
        RangeError
        """
        ...
