from typing import Union, Dict, Optional

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
    ANALYSIS_PRODUCT_DEFAULT,
    AUTOMATIC,
    Boolean,
    DEFAULT,
    FULL_NEWTON,
    OFF,
    PROPAGATED,
    SOLVER_DEFAULT,
    STEP,
    SymbolicConstant,
    VALUE,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class ImplicitDynamicsStep(AnalysisStep):
    """The ImplicitDynamicsStep object is used to provide direct integration of a dynamic
    stress/displacement response in Abaqus/Standard analyses and is generally used for
    nonlinear cases.
    The ImplicitDynamicsStep object is derived from the AnalysisStep object.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name]

        The corresponding analysis keywords are:

        - DYNAMIC
        - STEP
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A Float specifying the total time period of the step. The default value is 1.0.
    timePeriod: float = 1

    #: A Boolean specifying whether geometric nonlinearities should be accounted for during the
    #: step. The default value is based on the previous step.
    nlgeom: Boolean = OFF

    #: A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
    #: UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
    matrixStorage: SymbolicConstant = SOLVER_DEFAULT

    #: A SymbolicConstant specifying the application type of the step. Possible values are
    #: ANALYSIS_PRODUCT_DEFAULT, TRANSIENT_FIDELITY, MODERATE_DISSIPATION, and QUASI_STATIC.
    #: The default value is ANALYSIS_PRODUCT_DEFAULT.
    application: SymbolicConstant = ANALYSIS_PRODUCT_DEFAULT

    #: A Boolean specifying whether an adiabatic stress analysis is to be performed. The
    #: default value is OFF.
    adiabatic: Boolean = OFF

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

    #: The SymbolicConstant DEFAULT or a Float specifying the maximum time increment allowed.
    maxInc: Union[SymbolicConstant, float, None] = None

    #: A SymbolicConstant specifying the way of specifying half-increment residual tolerance
    #: with the automatic time incrementation scheme. Possible values are
    #: ANALYSIS_PRODUCT_DEFAULT, VALUE, and SCALE. The default value is VALUE.
    hafTolMethod: SymbolicConstant = VALUE

    #: None or a Float specifying the half-increment residual tolerance to be used with the
    #: automatic time incrementation scheme. The default value is None.
    haftol: Optional[float] = None

    #: None or a Float specifying the half-increment residual tolerance scale factor to be used
    #: with the automatic time incrementation scheme. The default value is None.
    halfIncScaleFactor: Optional[float] = None

    #: A Boolean specifying whether to suppress calculation of the half-increment residual. The
    #: default value is OFF.
    nohaf: Boolean = OFF

    #: A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
    #: step. Possible values are STEP and RAMP. The default value is STEP.
    amplitude: SymbolicConstant = STEP

    #: The SymbolicConstant DEFAULT or a Float specifying the nondefault value of the numerical
    #: (artificial) damping control parameter, αα, in the implicit operator. Possible values
    #: are −.333 <α< 0. The default value is DEFAULT.
    alpha: Union[SymbolicConstant, float] = DEFAULT

    #: A SymbolicConstant specifying whether accelerations should be calculated or recalculated
    #: at the beginning of the step. Possible values are DEFAULT, BYPASS, and ALLOW. The
    #: default value is DEFAULT.
    initialConditions: SymbolicConstant = DEFAULT

    #: A SymbolicConstant specifying the type of extrapolation to use in determining the
    #: incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR,
    #: PARABOLIC, VELOCITY_PARABOLIC, and ANALYSIS_PRODUCT_DEFAULT. The default value is
    #: ANALYSIS_PRODUCT_DEFAULT.
    extrapolation: SymbolicConstant = ANALYSIS_PRODUCT_DEFAULT

    #: A Boolean specifying whether to accept the solution to an increment after the maximum
    #: number of iterations allowed have been completed, even if the equilibrium tolerances are
    #: not satisfied. The default value is OFF.Warning:You should set **noStop** = OFF only in
    #: special cases when you have a thorough understanding of how to interpret the results.
    noStop: Boolean = OFF

    #: A SymbolicConstant specifying the technique used to for solving nonlinear equations.
    #: Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON.
    solutionTechnique: SymbolicConstant = FULL_NEWTON

    #: An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix
    #: is reformed.. The default value is 8.
    reformKernel: int = 8

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
        timePeriod: float = 1,
        nlgeom: Boolean = OFF,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        application: Literal[
            C.ANALYSIS_PRODUCT_DEFAULT, C.QUASI_STATIC, C.TRANSIENT_FIDELITY, C.MODERATE_DISSIPATION
        ] = ANALYSIS_PRODUCT_DEFAULT,
        adiabatic: Boolean = OFF,
        timeIncrementationMethod: Literal[C.AUTOMATIC, C.FIXED] = AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Union[Literal[C.DEFAULT], float] = DEFAULT,
        hafTolMethod: Literal[C.ANALYSIS_PRODUCT_DEFAULT, C.VALUE, C.SCALE] = VALUE,
        haftol: Optional[float] = None,
        halfIncScaleFactor: Optional[float] = None,
        nohaf: Boolean = OFF,
        amplitude: Literal[C.STEP, C.RAMP] = STEP,
        alpha: Union[Literal[C.DEFAULT], float] = DEFAULT,
        initialConditions: Literal[C.BYPASS, C.DEFAULT, C.ALLOW] = DEFAULT,
        extrapolation: Literal[
            C.ANALYSIS_PRODUCT_DEFAULT, C.PARABOLIC, C.VELOCITY_PARABOLIC, C.NONE, C.LINEAR
        ] = ANALYSIS_PRODUCT_DEFAULT,
        noStop: Boolean = OFF,
        maintainAttributes: Boolean = False,
        solutionTechnique: Literal[C.QUASI_NEWTON, C.FULL_NEWTON] = FULL_NEWTON,
        reformKernel: int = 8,
        convertSDI: Literal[C.CONVERT_SDI_OFF, C.PROPAGATED, C.CONVERT_SDI_ON] = PROPAGATED,
    ):
        """This method creates an ImplicitDynamicsStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].ImplicitDynamicsStep

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
            A Float specifying the total time period of the step. The default value is 1.0.
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the
            step. The default value is based on the previous step.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        application
            A SymbolicConstant specifying the application type of the step. Possible values are
            ANALYSIS_PRODUCT_DEFAULT, TRANSIENT_FIDELITY, MODERATE_DISSIPATION, and QUASI_STATIC.
            The default value is ANALYSIS_PRODUCT_DEFAULT.
        adiabatic
            A Boolean specifying whether an adiabatic stress analysis is to be performed. The
            default value is OFF.
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
            The SymbolicConstant DEFAULT or a Float specifying the maximum time increment allowed.
        hafTolMethod
            A SymbolicConstant specifying the way of specifying half-increment residual tolerance
            with the automatic time incrementation scheme. Possible values are
            ANALYSIS_PRODUCT_DEFAULT, VALUE, and SCALE. The default value is VALUE.
        haftol
            None or a Float specifying the half-increment residual tolerance to be used with the
            automatic time incrementation scheme. The default value is None.
        halfIncScaleFactor
            None or a Float specifying the half-increment residual tolerance scale factor to be used
            with the automatic time incrementation scheme. The default value is None.
        nohaf
            A Boolean specifying whether to suppress calculation of the half-increment residual. The
            default value is OFF.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. Possible values are STEP and RAMP. The default value is STEP.
        alpha
            The SymbolicConstant DEFAULT or a Float specifying the nondefault value of the numerical
            (artificial) damping control parameter, αα, in the implicit operator. Possible values
            are −.333 <α< 0. The default value is DEFAULT.
        initialConditions
            A SymbolicConstant specifying whether accelerations should be calculated or recalculated
            at the beginning of the step. Possible values are DEFAULT, BYPASS, and ALLOW. The
            default value is DEFAULT.
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR,
            PARABOLIC, VELOCITY_PARABOLIC, and ANALYSIS_PRODUCT_DEFAULT. The default value is
            ANALYSIS_PRODUCT_DEFAULT.
        noStop
            A Boolean specifying whether to accept the solution to an increment after the maximum
            number of iterations allowed have been completed, even if the equilibrium tolerances are
            not satisfied. The default value is OFF.Warning:You should set **noStop** = OFF only in
            special cases when you have a thorough understanding of how to interpret the results.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        solutionTechnique
            A SymbolicConstant specifying the technique used to for solving nonlinear equations.
            Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON.
        reformKernel
            An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix
            is reformed.. The default value is 8.
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
            CONVERT_SDI_ON. The default value is PROPAGATED.

        Returns
        -------
        ImplicitDynamicsStep
            An ImplicitDynamicsStep object.

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
        nlgeom: Boolean = OFF,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        application: Literal[
            C.ANALYSIS_PRODUCT_DEFAULT, C.QUASI_STATIC, C.TRANSIENT_FIDELITY, C.MODERATE_DISSIPATION
        ] = ANALYSIS_PRODUCT_DEFAULT,
        adiabatic: Boolean = OFF,
        timeIncrementationMethod: Literal[C.AUTOMATIC, C.FIXED] = AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Union[Literal[C.DEFAULT], float] = DEFAULT,
        hafTolMethod: Literal[C.ANALYSIS_PRODUCT_DEFAULT, C.VALUE, C.SCALE] = VALUE,
        haftol: Optional[float] = None,
        halfIncScaleFactor: Optional[float] = None,
        nohaf: Boolean = OFF,
        amplitude: Literal[C.STEP, C.RAMP] = STEP,
        alpha: Union[Literal[C.DEFAULT], float] = DEFAULT,
        initialConditions: Literal[C.BYPASS, C.DEFAULT, C.ALLOW] = DEFAULT,
        extrapolation: Literal[
            C.ANALYSIS_PRODUCT_DEFAULT, C.PARABOLIC, C.VELOCITY_PARABOLIC, C.NONE, C.LINEAR
        ] = ANALYSIS_PRODUCT_DEFAULT,
        noStop: Boolean = OFF,
        solutionTechnique: Literal[C.QUASI_NEWTON, C.FULL_NEWTON] = FULL_NEWTON,
        reformKernel: int = 8,
        convertSDI: Literal[C.CONVERT_SDI_OFF, C.PROPAGATED, C.CONVERT_SDI_ON] = PROPAGATED,
    ):
        """This method modifies the ImplicitDynamicsStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string.
        timePeriod
            A Float specifying the total time period of the step. The default value is 1.0.
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the
            step. The default value is based on the previous step.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        application
            A SymbolicConstant specifying the application type of the step. Possible values are
            ANALYSIS_PRODUCT_DEFAULT, TRANSIENT_FIDELITY, MODERATE_DISSIPATION, and QUASI_STATIC.
            The default value is ANALYSIS_PRODUCT_DEFAULT.
        adiabatic
            A Boolean specifying whether an adiabatic stress analysis is to be performed. The
            default value is OFF.
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
            The SymbolicConstant DEFAULT or a Float specifying the maximum time increment allowed.
        hafTolMethod
            A SymbolicConstant specifying the way of specifying half-increment residual tolerance
            with the automatic time incrementation scheme. Possible values are
            ANALYSIS_PRODUCT_DEFAULT, VALUE, and SCALE. The default value is VALUE.
        haftol
            None or a Float specifying the half-increment residual tolerance to be used with the
            automatic time incrementation scheme. The default value is None.
        halfIncScaleFactor
            None or a Float specifying the half-increment residual tolerance scale factor to be used
            with the automatic time incrementation scheme. The default value is None.
        nohaf
            A Boolean specifying whether to suppress calculation of the half-increment residual. The
            default value is OFF.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. Possible values are STEP and RAMP. The default value is STEP.
        alpha
            The SymbolicConstant DEFAULT or a Float specifying the nondefault value of the numerical
            (artificial) damping control parameter, αα, in the implicit operator. Possible values
            are −.333 <α< 0. The default value is DEFAULT.
        initialConditions
            A SymbolicConstant specifying whether accelerations should be calculated or recalculated
            at the beginning of the step. Possible values are DEFAULT, BYPASS, and ALLOW. The
            default value is DEFAULT.
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR,
            PARABOLIC, VELOCITY_PARABOLIC, and ANALYSIS_PRODUCT_DEFAULT. The default value is
            ANALYSIS_PRODUCT_DEFAULT.
        noStop
            A Boolean specifying whether to accept the solution to an increment after the maximum
            number of iterations allowed have been completed, even if the equilibrium tolerances are
            not satisfied. The default value is OFF.Warning:You should set **noStop** = OFF only in
            special cases when you have a thorough understanding of how to interpret the results.
        solutionTechnique
            A SymbolicConstant specifying the technique used to for solving nonlinear equations.
            Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON.
        reformKernel
            An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix
            is reformed.. The default value is 8.
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
            CONVERT_SDI_ON. The default value is PROPAGATED.

        Raises
        ------
        RangeError
        """
        ...
