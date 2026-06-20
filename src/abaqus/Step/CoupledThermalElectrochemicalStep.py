from __future__ import annotations

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

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
from ..UtilityAndView.abaqusConstants import OFF, Boolean, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .AnalysisStep import AnalysisStep


@abaqus_class_doc
class CoupledThermalElectrochemicalStep(AnalysisStep):
    """The CoupledThermalElectrochemicalStep object is used to analyze problems where the
    electrical potential, ion concentration, and temperature fields must be solved
    simultaneously.
    The CoupledThermalElectrochemicalStep object is derived from the AnalysisStep object.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name]

        The corresponding analysis keywords are:

        - COUPLED THERMAL-ELECTROCHEMICAL
        - SOLUTION TECHNIQUE
        - STEP

    .. versionadded:: 2025
        The ``CoupledThermalElectrochemicalStep`` class was added.
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and
    #: TRANSIENT. The default value is TRANSIENT.
    response: SymbolicConstant = C.TRANSIENT

    #: A Float specifying the total time period for the step. The default value is 1.0.
    timePeriod: float = 1.0

    #: A SymbolicConstant specifying the time incrementation method to be used. Possible
    #: values are FIXED and AUTOMATIC. The default value is AUTOMATIC.
    timeIncrementationMethod: SymbolicConstant = C.AUTOMATIC

    #: An Int specifying the maximum number of increments in a step. The default value is 100.
    maxNumInc: int = 100

    #: A Float specifying the initial time increment. The default value is the total time period
    #: for the step.
    initialInc: float | None = None

    #: A Float specifying the minimum time increment allowed. The default value is the smaller of
    #: the suggested initial time increment or 10−5 times the total time period.
    minInc: float | None = None

    #: A Float specifying the maximum time increment allowed. The default value is the total time
    #: period for the step.
    maxInc: float | None = None

    #: A Float specifying the maximum temperature change to be allowed in an increment in a
    #: transient analysis. The default value is 0.0.
    deltmx: float = 0.0

    #: A SymbolicConstant specifying the type of solution technique. Possible values are
    #: FULL_NEWTON and SEPARATED. The default value is FULL_NEWTON.
    solutionTechnique: SymbolicConstant = C.FULL_NEWTON

    #: A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
    #: UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
    matrixStorage: SymbolicConstant = C.SOLVER_DEFAULT

    #: A SymbolicConstant specifying the amplitude variation for loading magnitudes during the
    #: step. The default value is STEP. Possible values are STEP and RAMP.
    amplitude: SymbolicConstant = C.STEP

    #: A SymbolicConstant specifying the type of extrapolation to use in determining the
    #: incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and
    #: PARABOLIC. The default value is LINEAR.
    extrapolation: SymbolicConstant = C.LINEAR

    #: A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
    #: occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
    #: CONVERT_SDI_ON. The default value is PROPAGATED.
    convertSDI: SymbolicConstant = C.PROPAGATED

    #: A String specifying the name of the previous step. The new step appears after this step in
    #: the list of analysis steps.
    previous: str = ""

    #: A String specifying a description of the new step. The default value is an empty string.
    description: str = ""

    #: A SymbolicConstant specifying whether the step has an explicit procedure type
    #: (procedureType=ANNEAL, DYNAMIC_EXPLICIT, or DYNAMIC_TEMP_DISPLACEMENT).
    explicit: SymbolicConstant

    #: A Boolean specifying whether the step has a perturbation procedure type.
    perturbation: Boolean = OFF

    #: A Boolean specifying whether the step has a mechanical procedure type.
    nonmechanical: Boolean = OFF

    #: A SymbolicConstant specifying the Abaqus procedure.
    procedureType: SymbolicConstant

    #: A Boolean specifying whether the step is suppressed or not. The default value is OFF.
    suppressed: Boolean = OFF

    #: A repository of FieldOutputRequestState objects.
    fieldOutputRequestState: dict[str, FieldOutputRequestState] = {}

    #: A repository of HistoryOutputRequestState objects.
    historyOutputRequestState: dict[str, HistoryOutputRequestState] = {}

    #: A DiagnosticPrint object.
    diagnosticPrint: DiagnosticPrint = DiagnosticPrint()

    #: A Monitor object.
    monitor: Monitor | None = None

    #: A Restart object.
    restart: Restart = Restart()

    #: A repository of AdaptiveMeshConstraintState objects.
    adaptiveMeshConstraintStates: dict[str, AdaptiveMeshConstraintState] = {}

    #: A repository of AdaptiveMeshDomain objects.
    adaptiveMeshDomains: dict[str, AdaptiveMeshDomain] = {}

    #: A Control object.
    control: Control = Control()

    #: A SolverControl object.
    solverControl: SolverControl = SolverControl()

    #: A repository of BoundaryConditionState objects.
    boundaryConditionStates: dict[str, BoundaryConditionState] = {}

    #: A repository of InteractionState objects.
    interactionStates: int | None = None

    #: A repository of LoadState objects.
    loadStates: dict[str, LoadState] = {}

    #: A repository of LoadCase objects.
    loadCases: dict[str, LoadCase] = {}

    #: A repository of PredefinedFieldState objects.
    predefinedFieldStates: dict[str, PredefinedFieldState] = {}

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        previous: str,
        description: str = "",
        response: Literal[C.STEADY_STATE, C.TRANSIENT] = C.TRANSIENT,
        timePeriod: float = 1.0,
        timeIncrementationMethod: Literal[C.FIXED, C.AUTOMATIC] = C.AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: float | None = None,
        minInc: float | None = None,
        maxInc: float | None = None,
        deltmx: float = 0.0,
        solutionTechnique: Literal[C.FULL_NEWTON, C.SEPARATED] = C.FULL_NEWTON,
        matrixStorage: Literal[C.SYMMETRIC, C.UNSYMMETRIC, C.SOLVER_DEFAULT] = C.SOLVER_DEFAULT,
        amplitude: Literal[C.STEP, C.RAMP] = C.STEP,
        extrapolation: Literal[C.NONE, C.LINEAR, C.PARABOLIC] = C.LINEAR,
        maintainAttributes: bool = False,
        convertSDI: Literal[C.PROPAGATED, C.CONVERT_SDI_OFF, C.CONVERT_SDI_ON] = C.PROPAGATED,
    ):
        """This method creates a CoupledThermalElectrochemicalStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].CoupledThermalElectrochemicalStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step in
            the list of analysis steps.
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
            A Float specifying the initial time increment. The default value is the total time period
            for the step.
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller of
            the suggested initial time increment or 10−5 times the total time period.
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total time
            period for the step.
        deltmx
            A Float specifying the maximum temperature change to be allowed in an increment in a
            transiant analysis. The default value is 0.0.
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
            A Boolean specifying whether to retain attributes from an existing step with the same name.
            The default value is False.
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and
            CONVERT_SDI_ON. The default value is PROPAGATED.

        Returns
        -------
        CoupledThermalElectrochemicalStep
            A CoupledThermalElectrochemicalStep object.

        Exceptions
        ----------
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        description: str = "",
        response: Literal[C.STEADY_STATE, C.TRANSIENT] = C.TRANSIENT,
        timePeriod: float = 1.0,
        timeIncrementationMethod: Literal[C.FIXED, C.AUTOMATIC] = C.AUTOMATIC,
        maxNumInc: int = 100,
        initialInc: float | None = None,
        minInc: float | None = None,
        maxInc: float | None = None,
        deltmx: float = 0.0,
        solutionTechnique: Literal[C.FULL_NEWTON, C.SEPARATED] = C.FULL_NEWTON,
        matrixStorage: Literal[C.SYMMETRIC, C.UNSYMMETRIC, C.SOLVER_DEFAULT] = C.SOLVER_DEFAULT,
        amplitude: Literal[C.STEP, C.RAMP] = C.STEP,
        extrapolation: Literal[C.NONE, C.LINEAR, C.PARABOLIC] = C.LINEAR,
        convertSDI: Literal[C.PROPAGATED, C.CONVERT_SDI_OFF, C.CONVERT_SDI_ON] = C.PROPAGATED,
    ):
        """This method modifies the CoupledThermalElectrochemicalStep object.

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
            A Float specifying the initial time increment. The default value is the total time period
            for the step.
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller of
            the suggested initial time increment or 10−5 times the total time period.
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total time
            period for the step.
        deltmx
            A Float specifying the maximum temperature change to be allowed in an increment in a
            transient analysis. The default value is 0.0.
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

        Exceptions
        ----------
        RangeError
        """
        ...
