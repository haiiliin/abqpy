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
    DIRECT,
    FULL_NEWTON,
    LINEAR,
    NONE,
    OFF,
    ON,
    PERIOD,
    PROPAGATED,
    SOLVER_DEFAULT,
    STEP,
    SymbolicConstant,
    TRANSIENT,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class SoilsStep(AnalysisStep):
    """The SoilsStep object is used to specify transient (consolidation) or steady-state
    response analysis of partially or fully saturated fluid-filled porous media.
    The SoilsStep object is derived from the AnalysisStep object.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name]

        The corresponding analysis keywords are:

        - SOILS
        - STEP
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and
    #: TRANSIENT. The default value is TRANSIENT.
    response: Literal[C.STEADY_STATE, C.TRANSIENT] = TRANSIENT

    #: A Float specifying the total time period. The default value is 1.0.
    timePeriod: float = 1

    #: A Boolean specifying whether geometric nonlinearities should be accounted for during the
    #: step. The default value is OFF.
    nlgeom: Boolean = OFF

    #: A SymbolicConstant specifying the stabilization type. Possible values are NONE,
    #: DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE.
    stabilizationMethod: Literal[C.NONE, C.DISSIPATED_ENERGY_FRACTION, C.DAMPING_FACTOR] = NONE

    #: A Float specifying the damping intensity of the automatic damping algorithm if the
    #: problem is expected to be unstable, and **stabilizationMethod** is not NONE. The default
    #: value is 2×10⁻⁴.
    stabilizationMagnitude: Optional[float] = None

    #: A Boolean specifying whether a creep response occurs during this step. The default value
    #: is ON.
    creep: Boolean = ON

    #: A SymbolicConstant specifying the time incrementation method to be used. Possible values
    #: are FIXED and AUTOMATIC. The default value is AUTOMATIC.
    timeIncrementationMethod: Literal[C.FIXED, C.AUTOMATIC] = AUTOMATIC

    #: A Float specifying the initial time increment. The default value is the total time
    #: period for the step.
    initialInc: Optional[float] = None

    #: A Float specifying the minimum time increment allowed. The default value is the smaller
    #: of the suggested initial time increment or 10−5 times the total time period.
    minInc: Optional[float] = None

    #: A Float specifying the maximum time increment allowed. The default value is the total
    #: time period for the step.
    maxInc: Optional[float] = None

    #: An Int specifying the maximum number of increments in a step. The default value is 100.
    maxNumInc: int = 100

    #: A SymbolicConstant specifying the time period to be analyzed in a transient analysis.
    #: Possible values are PERIOD and SS. The default value is PERIOD.
    end: Literal[C.SS, C.PERIOD] = PERIOD

    #: None or a Float specifying the maximum pore pressure change permitted in any increment
    #: (in pressure units) in a transient consolidation analysis. The default value is None.
    utol: Optional[float] = None

    #: A Float specifying the maximum allowable difference in the creep strain increment
    #: calculated from the creep strain rates at the beginning and end of the increment. The
    #: default value is 0.0.
    cetol: float = 0

    #: A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
    #: step. The default value is STEP. Possible values are STEP and RAMP.
    amplitude: Literal[C.STEP, C.RAMP] = STEP

    #: A SymbolicConstant specifying the type of extrapolation to use in determining the
    #: incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and
    #: PARABOLIC. The default value is LINEAR.
    extrapolation: Literal[C.PARABOLIC, C.LINEAR] = LINEAR

    #: A SymbolicConstant specifying the type of solver. Possible values are DIRECT and
    #: ITERATIVE. The default value is DIRECT.
    matrixSolver: Literal[C.ITERATIVE, C.DIRECT] = DIRECT

    #: A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
    #: UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
    matrixStorage: Literal[C.SYMMETRIC, C.UNSYMMETRIC, C.SOLVER_DEFAULT] = SOLVER_DEFAULT

    #: A SymbolicConstant specifying the technique used to for solving nonlinear equations.
    #: Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON.
    solutionTechnique: Literal[C.FULL_NEWTON, C.QUASI_NEWTON] = FULL_NEWTON

    #: An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix
    #: is reformed.. The default value is 8.
    reformKernel: int = 8

    #: A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
    #: occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
    #: CONVERT_SDI_ON. The default value is PROPAGATED.
    convertSDI: Literal[C.PROPAGATED, C.CONVERT_SDI_OFF, C.CONVERT_SDI_ON] = PROPAGATED

    #: A Float specifying the maximum allowable ratio of the stabilization energy to the total
    #: strain energy and can be used only if **stabilizationMethod** is not NONE. The default
    #: value is 0.05.
    adaptiveDampingRatio: float = 0

    #: A Boolean specifying whether this step will carry over the damping factors from the
    #: results of the preceding general step. This parameter must be used in conjunction with
    #: the **adaptiveDampingRatio** parameter. The default value is OFF.
    continueDampingFactors: Boolean = OFF

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
        response: Literal[C.STEADY_STATE, C.TRANSIENT] = TRANSIENT,
        timePeriod: float = 1,
        nlgeom: Boolean = OFF,
        stabilizationMethod: Literal[C.NONE, C.DISSIPATED_ENERGY_FRACTION, C.DAMPING_FACTOR] = NONE,
        stabilizationMagnitude: Optional[float] = None,
        creep: Boolean = ON,
        timeIncrementationMethod: Literal[C.FIXED, C.AUTOMATIC] = AUTOMATIC,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Optional[float] = None,
        maxNumInc: int = 100,
        end: Literal[C.SS, C.PERIOD] = PERIOD,
        utol: Optional[float] = None,
        cetol: float = 0,
        amplitude: Literal[C.STEP, C.RAMP] = STEP,
        extrapolation: Literal[C.PARABOLIC, C.LINEAR] = LINEAR,
        matrixSolver: Literal[C.ITERATIVE, C.DIRECT] = DIRECT,
        matrixStorage: Literal[C.SYMMETRIC, C.UNSYMMETRIC, C.SOLVER_DEFAULT] = SOLVER_DEFAULT,
        maintainAttributes: Boolean = False,
        solutionTechnique: Literal[C.FULL_NEWTON, C.QUASI_NEWTON] = FULL_NEWTON,
        reformKernel: int = 8,
        convertSDI: Literal[C.PROPAGATED, C.CONVERT_SDI_OFF, C.CONVERT_SDI_ON] = PROPAGATED,
        adaptiveDampingRatio: float = 0,
        continueDampingFactors: Boolean = OFF,
    ):
        """This method creates a SoilsStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].SoilsStep

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
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the
            step. The default value is OFF.
        stabilizationMethod
            A SymbolicConstant specifying the stabilization type. Possible values are NONE,
            DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE.
        stabilizationMagnitude
            A Float specifying the damping intensity of the automatic damping algorithm if the
            problem is expected to be unstable, and **stabilizationMethod** is not NONE. The default
            value is 2×10⁻⁴.
        creep
            A Boolean specifying whether a creep response occurs during this step. The default value
            is ON.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are FIXED and AUTOMATIC. The default value is AUTOMATIC.
        initialInc
            A Float specifying the initial time increment. The default value is the total time
            period for the step.
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller
            of the suggested initial time increment or 10−5 times the total time period.
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total
            time period for the step.
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100.
        end
            A SymbolicConstant specifying the time period to be analyzed in a transient analysis.
            Possible values are PERIOD and SS. The default value is PERIOD.
        utol
            None or a Float specifying the maximum pore pressure change permitted in any increment
            (in pressure units) in a transient consolidation analysis. The default value is None.
        cetol
            A Float specifying the maximum allowable difference in the creep strain increment
            calculated from the creep strain rates at the beginning and end of the increment. The
            default value is 0.0.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. The default value is STEP. Possible values are STEP and RAMP.
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and
            PARABOLIC. The default value is LINEAR.
        matrixSolver
            A SymbolicConstant specifying the type of solver. Possible values are DIRECT and
            ITERATIVE. The default value is DIRECT.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
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
        adaptiveDampingRatio
            A Float specifying the maximum allowable ratio of the stabilization energy to the total
            strain energy and can be used only if **stabilizationMethod** is not NONE. The default
            value is 0.05.
        continueDampingFactors
            A Boolean specifying whether this step will carry over the damping factors from the
            results of the preceding general step. This parameter must be used in conjunction with
            the **adaptiveDampingRatio** parameter. The default value is OFF.

        Returns
        -------
        SoilsStep
            A SoilsStep object.

        Raises
        ------
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        description: str = "",
        response: Literal[C.STEADY_STATE, C.TRANSIENT] = TRANSIENT,
        timePeriod: float = 1,
        nlgeom: Boolean = OFF,
        stabilizationMethod: Literal[C.NONE, C.DISSIPATED_ENERGY_FRACTION, C.DAMPING_FACTOR] = NONE,
        stabilizationMagnitude: Optional[float] = None,
        creep: Boolean = ON,
        timeIncrementationMethod: Literal[C.FIXED, C.AUTOMATIC] = AUTOMATIC,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Optional[float] = None,
        maxNumInc: int = 100,
        end: Literal[C.SS, C.PERIOD] = PERIOD,
        utol: Optional[float] = None,
        cetol: float = 0,
        amplitude: Literal[C.STEP, C.RAMP] = STEP,
        extrapolation: Literal[C.PARABOLIC, C.LINEAR] = LINEAR,
        matrixSolver: Literal[C.ITERATIVE, C.DIRECT] = DIRECT,
        matrixStorage: Literal[C.SYMMETRIC, C.UNSYMMETRIC, C.SOLVER_DEFAULT] = SOLVER_DEFAULT,
        solutionTechnique: Literal[C.FULL_NEWTON, C.QUASI_NEWTON] = FULL_NEWTON,
        reformKernel: int = 8,
        convertSDI: Literal[C.PROPAGATED, C.CONVERT_SDI_OFF, C.CONVERT_SDI_ON] = PROPAGATED,
        adaptiveDampingRatio: float = 0,
        continueDampingFactors: Boolean = OFF,
    ):
        """This method modifies the SoilsStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string.
        response
            A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and
            TRANSIENT. The default value is TRANSIENT.
        timePeriod
            A Float specifying the total time period. The default value is 1.0.
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the
            step. The default value is OFF.
        stabilizationMethod
            A SymbolicConstant specifying the stabilization type. Possible values are NONE,
            DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE.
        stabilizationMagnitude
            A Float specifying the damping intensity of the automatic damping algorithm if the
            problem is expected to be unstable, and **stabilizationMethod** is not NONE. The default
            value is 2×10⁻⁴.
        creep
            A Boolean specifying whether a creep response occurs during this step. The default value
            is ON.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are FIXED and AUTOMATIC. The default value is AUTOMATIC.
        initialInc
            A Float specifying the initial time increment. The default value is the total time
            period for the step.
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller
            of the suggested initial time increment or 10−5 times the total time period.
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total
            time period for the step.
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100.
        end
            A SymbolicConstant specifying the time period to be analyzed in a transient analysis.
            Possible values are PERIOD and SS. The default value is PERIOD.
        utol
            None or a Float specifying the maximum pore pressure change permitted in any increment
            (in pressure units) in a transient consolidation analysis. The default value is None.
        cetol
            A Float specifying the maximum allowable difference in the creep strain increment
            calculated from the creep strain rates at the beginning and end of the increment. The
            default value is 0.0.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. The default value is STEP. Possible values are STEP and RAMP.
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and
            PARABOLIC. The default value is LINEAR.
        matrixSolver
            A SymbolicConstant specifying the type of solver. Possible values are DIRECT and
            ITERATIVE. The default value is DIRECT.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
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
        adaptiveDampingRatio
            A Float specifying the maximum allowable ratio of the stabilization energy to the total
            strain energy and can be used only if **stabilizationMethod** is not NONE. The default
            value is 0.05.
        continueDampingFactors
            A Boolean specifying whether this step will carry over the damping factors from the
            results of the preceding general step. This parameter must be used in conjunction with
            the **adaptiveDampingRatio** parameter. The default value is OFF.

        Raises
        ------
        RangeError
        """
        ...
