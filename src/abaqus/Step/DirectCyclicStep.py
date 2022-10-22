from typing_extensions import Literal
from typing import Dict, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

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
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import (AUTOMATIC, Boolean, DEFAULT, LINEAR, NONE, OFF,
                                              PROPAGATED, SOLVER_DEFAULT, SymbolicConstant)


@abaqus_class_doc
class DirectCyclicStep(AnalysisStep):
    """The DirectCyclicStep object is used to provide a direct cyclic procedure for nonlinear,
    non-isothermal quasi-static analysis. It can also be used to predict progressive damage
    and failure for ductile bulk materials and/or to predict delamination/debonding growth
    at the interfaces in laminated composites in a low-cycle fatigue analysis.
    The DirectCyclicStep object is derived from the AnalysisStep object.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name]

        The corresponding analysis keywords are:

        - DIRECT CYCLIC
        - STEP
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A Float specifying the time of single loading cycle. The default value is 1.0.
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
    #: of the suggested initial time increment or 10−5 times the total time period.
    minInc: Optional[float] = None

    #: A Float specifying the maximum time increment allowed. The default value is the total
    #: time period for the step.
    maxInc: Optional[float] = None

    #: An Int specifying the maximum number of iterations in a step. The default value is 200.
    maxNumIterations: int = 200

    #: An Int specifying the initial number of terms in the Fourier series. The default value
    #: is 11.
    initialTerms: int = 11

    #: An Int specifying the maximum number of terms in the Fourier series. The default value
    #: is 25.
    maxTerms: int = 25

    #: An Int specifying the increment in number of terms in the Fourier series. The default
    #: value is 5.
    termsIncrement: int = 5

    #: A Float specifying the maximum temperature change to be allowed in an increment. The
    #: default value is 0.0.
    deltmx: float = 0

    #: A Float specifying the maximum difference in the creep strain increment calculated from
    #: the creep strain rates at the beginning and end of the increment. The default value is
    #: 0.0.
    cetol: float = 0

    #: A Boolean specifying whether to include low-cycle fatigue analysis. The default value is
    #: OFF.
    fatigue: Boolean = OFF

    #: A Boolean specifying whether the displacement solution in the Fourier series obtained in
    #: the previous direct cyclic step is used as the starting values for the current step. The
    #: default value is OFF.
    continueAnalysis: Boolean = OFF

    #: An Int specifying the minimum number of cycles over which the damage is extrapolated
    #: forward. The default value is 100.
    minCycleInc: int = 100

    #: An Int specifying the maximum number of cycles over which the damage is extrapolated
    #: forward. The default value is 1000.
    maxCycleInc: int = 1000

    #: The SymbolicConstant DEFAULT or an Int specifying the maximum number of cycles allowed
    #: in a step or DEFAULT. A value of 1 plus half of the maximum number of cycles will be
    #: used if DEFAULT is specified. The default value is DEFAULT.
    maxNumCycles: SymbolicConstant = DEFAULT

    #: A Float specifying the maximum extrapolated damage increment. The default value is 1.0.
    damageExtrapolationTolerance: float = 1

    #: A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
    #: UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
    matrixStorage: SymbolicConstant = SOLVER_DEFAULT

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

    #: None or a String specifying a String specifying the name of a time point object used to
    #: determine at which times the response of the structure will be evaluated. The default
    #: value is NONE.
    timePoints: str = NONE

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

    #: A :py:class:`~abaqus.StepOutput.DiagnosticPrint.DiagnosticPrint` object.
    diagnosticPrint: DiagnosticPrint = DiagnosticPrint()

    #: A :py:class:`~abaqus.StepOutput.Monitor.Monitor` object.
    monitor: Optional[Monitor] = None

    #: A :py:class:`~abaqus.StepOutput.Restart.Restart` object.
    restart: Restart = Restart()

    #: A repository of AdaptiveMeshConstraintState objects.
    adaptiveMeshConstraintStates: Dict[str, AdaptiveMeshConstraintState] = {}

    #: A repository of AdaptiveMeshDomain objects.
    adaptiveMeshDomains: Dict[str, AdaptiveMeshDomain] = {}

    #: A :py:class:`~abaqus.StepMiscellaneous.Control.Control` object.
    control: Control = Control()

    #: A :py:class:`~abaqus.StepMiscellaneous.SolverControl.SolverControl` object.
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
        timePeriod: float = 1,
        timeIncrementationMethod: Literal[C.AUTOMATIC, C.FIXED] = AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Optional[float] = None,
        maxNumIterations: int = 200,
        initialTerms: int = 11,
        maxTerms: int = 25,
        termsIncrement: int = 5,
        deltmx: float = 0,
        cetol: float = 0,
        timePoints: str = NONE,
        fatigue: Boolean = OFF,
        continueAnalysis: Boolean = OFF,
        minCycleInc: int = 100,
        maxCycleInc: int = 1000,
        maxNumCycles: Literal[C.DEFAULT] = DEFAULT,
        damageExtrapolationTolerance: float = 1,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        extrapolation: Literal[C.PARABOLIC, C.NONE, C.LINEAR] = LINEAR,
        maintainAttributes: Boolean = False,
        convertSDI: Literal[C.CONVERT_SDI_OFF, C.PROPAGATED, C.CONVERT_SDI_ON] = PROPAGATED,
    ):
        """This method creates a DirectCyclicStep object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].DirectCyclicStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        timePeriod
            A Float specifying the time of single loading cycle. The default value is 1.0.
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
            of the suggested initial time increment or 10−5 times the total time period.
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total
            time period for the step.
        maxNumIterations
            An Int specifying the maximum number of iterations in a step. The default value is 200.
        initialTerms
            An Int specifying the initial number of terms in the Fourier series. The default value
            is 11.
        maxTerms
            An Int specifying the maximum number of terms in the Fourier series. The default value
            is 25.
        termsIncrement
            An Int specifying the increment in number of terms in the Fourier series. The default
            value is 5.
        deltmx
            A Float specifying the maximum temperature change to be allowed in an increment. The
            default value is 0.0.
        cetol
            A Float specifying the maximum difference in the creep strain increment calculated from
            the creep strain rates at the beginning and end of the increment. The default value is
            0.0.
        timePoints
            None or a String specifying a String specifying the name of a time point object used to
            determine at which times the response of the structure will be evaluated. The default
            value is NONE.
        fatigue
            A Boolean specifying whether to include low-cycle fatigue analysis. The default value is
            OFF.
        continueAnalysis
            A Boolean specifying whether the displacement solution in the Fourier series obtained in
            the previous direct cyclic step is used as the starting values for the current step. The
            default value is OFF.
        minCycleInc
            An Int specifying the minimum number of cycles over which the damage is extrapolated
            forward. The default value is 100.
        maxCycleInc
            An Int specifying the maximum number of cycles over which the damage is extrapolated
            forward. The default value is 1000.
        maxNumCycles
            The SymbolicConstant DEFAULT or an Int specifying the maximum number of cycles allowed
            in a step or DEFAULT. A value of 1 plus half of the maximum number of cycles will be
            used if DEFAULT is specified. The default value is DEFAULT.
        damageExtrapolationTolerance
            A Float specifying the maximum extrapolated damage increment. The default value is 1.0.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
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
        DirectCyclicStep
            A :py:class:`~abaqus.Step.DirectCyclicStep.DirectCyclicStep` object.

        Raises
        ------
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        description: str = "",
        timePeriod: float = 1,
        timeIncrementationMethod: Literal[C.AUTOMATIC, C.FIXED] = AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Optional[float] = None,
        maxNumIterations: int = 200,
        initialTerms: int = 11,
        maxTerms: int = 25,
        termsIncrement: int = 5,
        deltmx: float = 0,
        cetol: float = 0,
        timePoints: str = NONE,
        fatigue: Boolean = OFF,
        continueAnalysis: Boolean = OFF,
        minCycleInc: int = 100,
        maxCycleInc: int = 1000,
        maxNumCycles: Literal[C.DEFAULT] = DEFAULT,
        damageExtrapolationTolerance: float = 1,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        extrapolation: Literal[C.PARABOLIC, C.NONE, C.LINEAR] = LINEAR,
        convertSDI: Literal[C.CONVERT_SDI_OFF, C.PROPAGATED, C.CONVERT_SDI_ON] = PROPAGATED,
    ):
        """This method modifies the DirectCyclicStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string.
        timePeriod
            A Float specifying the time of single loading cycle. The default value is 1.0.
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
            of the suggested initial time increment or 10−5 times the total time period.
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total
            time period for the step.
        maxNumIterations
            An Int specifying the maximum number of iterations in a step. The default value is 200.
        initialTerms
            An Int specifying the initial number of terms in the Fourier series. The default value
            is 11.
        maxTerms
            An Int specifying the maximum number of terms in the Fourier series. The default value
            is 25.
        termsIncrement
            An Int specifying the increment in number of terms in the Fourier series. The default
            value is 5.
        deltmx
            A Float specifying the maximum temperature change to be allowed in an increment. The
            default value is 0.0.
        cetol
            A Float specifying the maximum difference in the creep strain increment calculated from
            the creep strain rates at the beginning and end of the increment. The default value is
            0.0.
        timePoints
            None or a String specifying a String specifying the name of a time point object used to
            determine at which times the response of the structure will be evaluated. The default
            value is NONE.
        fatigue
            A Boolean specifying whether to include low-cycle fatigue analysis. The default value is
            OFF.
        continueAnalysis
            A Boolean specifying whether the displacement solution in the Fourier series obtained in
            the previous direct cyclic step is used as the starting values for the current step. The
            default value is OFF.
        minCycleInc
            An Int specifying the minimum number of cycles over which the damage is extrapolated
            forward. The default value is 100.
        maxCycleInc
            An Int specifying the maximum number of cycles over which the damage is extrapolated
            forward. The default value is 1000.
        maxNumCycles
            The SymbolicConstant DEFAULT or an Int specifying the maximum number of cycles allowed
            in a step or DEFAULT. A value of 1 plus half of the maximum number of cycles will be
            used if DEFAULT is specified. The default value is DEFAULT.
        damageExtrapolationTolerance
            A Float specifying the maximum extrapolated damage increment. The default value is 1.0.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
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
