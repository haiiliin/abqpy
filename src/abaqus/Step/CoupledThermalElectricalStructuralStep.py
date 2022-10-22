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
from ..UtilityAndView.abaqusConstants import (AUTOMATIC, Boolean, IMPLICIT, LINEAR, NONE, OFF,
                                              PROPAGATED, SOLVER_DEFAULT, STEP, SymbolicConstant,
                                              TRANSIENT)


@abaqus_class_doc
class CoupledThermalElectricalStructuralStep(AnalysisStep):
    """The CoupledThermalElectricalStructuralStep object is used to analyze problems where the
    simultaneous solution of the temperature, stress/displacement and electrical fields is
    necessary.
    The CoupledThermalElectricalStructuralStep object is derived from the AnalysisStep
    object.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name]

        The corresponding analysis keywords are:

        - COUPLED TEMPERATURE-DISPLACEMENT
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

    #: A Boolean specifying whether geometric nonlinearities should be accounted for during the
    #: step. The default value is OFF.
    nlgeom: Boolean = OFF

    #: A SymbolicConstant specifying the stabilization type. Possible values are NONE,
    #: DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE.
    stabilizationMethod: SymbolicConstant = NONE

    #: A Float specifying the damping intensity of the automatic damping algorithm if the
    #: problem is expected to be unstable and **stabilizationMethod** ≠ NONE. The default value is
    #: 2×10-4.
    stabilizationMagnitude: Optional[float] = None

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

    #: A Float specifying the maximum temperature change to be allowed in an increment in a
    #: transient analysis. The default value is 0.0.
    deltmx: float = 0

    #: A Float specifying the maximum difference in the creep strain increment calculated from
    #: the creep strain rates at the beginning and end of the increment. The default value is
    #: 0.0.
    cetol: float = 0

    #: A SymbolicConstant specifying the type of integration to be used for creep and swelling
    #: effects throughout the step. Possible values are IMPLICIT, EXPLICIT, and NONE. The
    #: default value is IMPLICIT.
    creepIntegration: SymbolicConstant = IMPLICIT

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
        nlgeom: Boolean = OFF,
        stabilizationMethod: Literal[C.DAMPING_FACTOR, C.DISSIPATED_ENERGY_FRACTION, C.NONE] = NONE,
        stabilizationMagnitude: Optional[float] = None,
        timeIncrementationMethod: Literal[C.AUTOMATIC, C.FIXED] = AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Optional[float] = None,
        deltmx: float = 0,
        cetol: float = 0,
        creepIntegration: Literal[C.EXPLICIT, C.IMPLICIT, C.NONE] = IMPLICIT,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        amplitude: Literal[C.STEP, C.RAMP] = STEP,
        extrapolation: Literal[C.PARABOLIC, C.NONE, C.LINEAR] = LINEAR,
        maintainAttributes: Boolean = False,
        convertSDI: Literal[C.CONVERT_SDI_OFF, C.PROPAGATED, C.CONVERT_SDI_ON] = PROPAGATED,
        adaptiveDampingRatio: float = 0,
        continueDampingFactors: Boolean = OFF,
    ):
        """This method creates a CoupledThermalElectricalStructuralStep object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].CoupledThermalElectricalStructuralStep

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
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the
            step. The default value is OFF.
        stabilizationMethod
            A SymbolicConstant specifying the stabilization type. Possible values are NONE,
            DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE.
        stabilizationMagnitude
            A Float specifying the damping intensity of the automatic damping algorithm if the
            problem is expected to be unstable and **stabilizationMethod** ≠ NONE. The default value is
            2×10-4.
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
        deltmx
            A Float specifying the maximum temperature change to be allowed in an increment in a
            transient analysis. The default value is 0.0.
        cetol
            A Float specifying the maximum difference in the creep strain increment calculated from
            the creep strain rates at the beginning and end of the increment. The default value is
            0.0.
        creepIntegration
            A SymbolicConstant specifying the type of integration to be used for creep and swelling
            effects throughout the step. Possible values are IMPLICIT, EXPLICIT, and NONE. The
            default value is IMPLICIT.
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
        CoupledThermalElectricalStructuralStep
            A :py:class:`~abaqus.Step.CoupledThermalElectricalStructuralStep.CoupledThermalElectricalStructuralStep` object.

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
        nlgeom: Boolean = OFF,
        stabilizationMethod: Literal[C.DAMPING_FACTOR, C.DISSIPATED_ENERGY_FRACTION, C.NONE] = NONE,
        stabilizationMagnitude: Optional[float] = None,
        timeIncrementationMethod: Literal[C.AUTOMATIC, C.FIXED] = AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Optional[float] = None,
        deltmx: float = 0,
        cetol: float = 0,
        creepIntegration: Literal[C.EXPLICIT, C.IMPLICIT, C.NONE] = IMPLICIT,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        amplitude: Literal[C.STEP, C.RAMP] = STEP,
        extrapolation: Literal[C.PARABOLIC, C.NONE, C.LINEAR] = LINEAR,
        convertSDI: Literal[C.CONVERT_SDI_OFF, C.PROPAGATED, C.CONVERT_SDI_ON] = PROPAGATED,
        adaptiveDampingRatio: float = 0,
        continueDampingFactors: Boolean = OFF,
    ):
        """This method modifies the CoupledThermalElectricalStructuralStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string.
        response
            A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and
            TRANSIENT. The default value is TRANSIENT.
        timePeriod
            A Float specifying the total time period for the step. The default value is 1.0.
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the
            step. The default value is OFF.
        stabilizationMethod
            A SymbolicConstant specifying the stabilization type. Possible values are NONE,
            DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE.
        stabilizationMagnitude
            A Float specifying the damping intensity of the automatic damping algorithm if the
            problem is expected to be unstable and **stabilizationMethod** ≠ NONE. The default value is
            2×10-4.
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
        deltmx
            A Float specifying the maximum temperature change to be allowed in an increment in a
            transient analysis. The default value is 0.0.
        cetol
            A Float specifying the maximum difference in the creep strain increment calculated from
            the creep strain rates at the beginning and end of the increment. The default value is
            0.0.
        creepIntegration
            A SymbolicConstant specifying the type of integration to be used for creep and swelling
            effects throughout the step. Possible values are IMPLICIT, EXPLICIT, and NONE. The
            default value is IMPLICIT.
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
