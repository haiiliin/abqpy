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
from ..UtilityAndView.abaqusConstants import (AUTOMATIC, Boolean, FULL_NEWTON, LINEAR, OFF, PERIOD,
                                              PROPAGATED, SOLVER_DEFAULT, STEP, SymbolicConstant,
                                              TRANSIENT)


@abaqus_class_doc
class CoupledThermalElectricStep(AnalysisStep):
    """The CoupledThermalElectricStep object is used to analyze problems where the electrical
    potential and temperature fields must be solved simultaneously.
    The CoupledThermalElectricStep object is derived from the AnalysisStep object.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name]

        The corresponding analysis keywords are:

        - COUPLED THERMAL-ELECTRICAL
                - SOLUTION TECHNIQUE
        - STEP
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and
    #: TRANSIENT. The default value is TRANSIENT.
    response: SymbolicConstant = TRANSIENT

    #: A Float specifying the total time period for the step. The default value is 1.0.
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

    #: A SymbolicConstant specifying the time period to be analyzed in a transient analysis.
    #: Possible values are PERIOD and SS. The default value is PERIOD.
    end: SymbolicConstant = PERIOD

    #: A Float specifying the maximum temperature change to be allowed in an increment in a
    #: transient analysis. The default value is 0.0.
    deltmx: float = 0

    #: A Float specifying the maximum allowable emissivity change with temperature and field
    #: variables during an increment. The default value is 0.1.
    mxdem: float = 0

    #: A SymbolicConstant specifying the type of solution technique. Possible values are
    #: FULL_NEWTON and SEPARATED. The default value is FULL_NEWTON.
    solutionTechnique: SymbolicConstant = FULL_NEWTON

    #: A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
    #: UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
    matrixStorage: SymbolicConstant = SOLVER_DEFAULT

    #: A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
    #: step. The default value is STEP. Possible values are STEP and RAMP.
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
        response: Literal[C.TRANSIENT, C.STEADY_STATE] = TRANSIENT,
        timePeriod: float = 1,
        timeIncrementationMethod: Literal[C.AUTOMATIC, C.FIXED] = AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Optional[float] = None,
        end: Literal[C.SS, C.PERIOD] = PERIOD,
        deltmx: float = 0,
        mxdem: float = 0,
        solutionTechnique: Literal[C.SEPARATED, C.FULL_NEWTON] = FULL_NEWTON,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        amplitude: Literal[C.STEP, C.RAMP] = STEP,
        extrapolation: Literal[C.PARABOLIC, C.NONE, C.LINEAR] = LINEAR,
        maintainAttributes: Boolean = False,
        convertSDI: Literal[C.CONVERT_SDI_OFF, C.PROPAGATED, C.CONVERT_SDI_ON] = PROPAGATED,
    ):
        """This method creates a CoupledThermalElectricStep object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].CoupledThermalElectricStep

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
            A Float specifying the total time period for the step. The default value is 1.0.
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
        end
            A SymbolicConstant specifying the time period to be analyzed in a transient analysis.
            Possible values are PERIOD and SS. The default value is PERIOD.
        deltmx
            A Float specifying the maximum temperature change to be allowed in an increment in a
            transient analysis. The default value is 0.0.
        mxdem
            A Float specifying the maximum allowable emissivity change with temperature and field
            variables during an increment. The default value is 0.1.
        solutionTechnique
            A SymbolicConstant specifying the type of solution technique. Possible values are
            FULL_NEWTON and SEPARATED. The default value is FULL_NEWTON.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. The default value is STEP. Possible values are STEP and RAMP.
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
        CoupledThermalElectricStep
            A :py:class:`~abaqus.Step.CoupledThermalElectricStep.CoupledThermalElectricStep` object.

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
        deltmx: float = 0,
        mxdem: float = 0,
        solutionTechnique: Literal[C.SEPARATED, C.FULL_NEWTON] = FULL_NEWTON,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        amplitude: Literal[C.STEP, C.RAMP] = STEP,
        extrapolation: Literal[C.PARABOLIC, C.NONE, C.LINEAR] = LINEAR,
        convertSDI: Literal[C.CONVERT_SDI_OFF, C.PROPAGATED, C.CONVERT_SDI_ON] = PROPAGATED,
    ):
        """This method modifies the CoupledThermalElectricStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string.
        response
            A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and
            TRANSIENT. The default value is TRANSIENT.
        timePeriod
            A Float specifying the total time period for the step. The default value is 1.0.
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
        end
            A SymbolicConstant specifying the time period to be analyzed in a transient analysis.
            Possible values are PERIOD and SS. The default value is PERIOD.
        deltmx
            A Float specifying the maximum temperature change to be allowed in an increment in a
            transient analysis. The default value is 0.0.
        mxdem
            A Float specifying the maximum allowable emissivity change with temperature and field
            variables during an increment. The default value is 0.1.
        solutionTechnique
            A SymbolicConstant specifying the type of solution technique. Possible values are
            FULL_NEWTON and SEPARATED. The default value is FULL_NEWTON.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
            step. The default value is STEP. Possible values are STEP and RAMP.
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
