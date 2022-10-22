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
from ..UtilityAndView.abaqusConstants import (AUTOMATIC, Boolean, DIRECT, FULL_NEWTON, OFF,
                                              PROPAGATED, SOLVER_DEFAULT, SymbolicConstant)


@abaqus_class_doc
class GeostaticStep(AnalysisStep):
    """The GeostaticStep object is used to verify that the geostatic stress field is in
    equilibrium with the applied loads and boundary conditions on the model and to iterate,
    if needed, to obtain equilibrium.
    The GeostaticStep object is derived from the AnalysisStep object.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name]

        The corresponding analysis keywords are:

        - GEOSTATIC
        - STEP
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A Boolean specifying whether geometric nonlinearities should be accounted for during the
    #: step. The default value is OFF.
    nlgeom: Boolean = OFF

    #: A SymbolicConstant specifying the type of solver. Possible values are DIRECT and
    #: ITERATIVE. The default value is DIRECT.
    matrixSolver: SymbolicConstant = DIRECT

    #: A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
    #: UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
    matrixStorage: SymbolicConstant = SOLVER_DEFAULT

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

    #: None or a Float specifying the tolerance for maximum change of displacements. The
    #: default value is None.
    utol: Optional[float] = None

    #: A Float specifying the total time period. The default value is 1.0.Note:This parameter
    #: is ignored unless **timeIncrementationMethod** = AUTOMATIC.
    timePeriod: float = 1

    #: A SymbolicConstant specifying the time incrementation method to be used. Possible values
    #: are FIXED and AUTOMATIC. The default value is AUTOMATIC.
    timeIncrementationMethod: SymbolicConstant = AUTOMATIC
    #: A Float specifying the initial time increment. The default value is the total time
    #: period for the step.Note:This parameter is ignored unless
    #: **timeIncrementationMethod** = AUTOMATIC.
    initialInc: Optional[float] = None

    #: A Float specifying the minimum time increment allowed. The default value is the smaller
    #: of the suggested initial time increment or 10−5 times the total time period.Note:This
    #: parameter is ignored unless **timeIncrementationMethod** = AUTOMATIC.
    minInc: Optional[float] = None

    #: A Float specifying the maximum time increment allowed. The default value is the total
    #: time period for the step.Note:This parameter is ignored unless
    #: **timeIncrementationMethod** = AUTOMATIC.
    maxInc: Optional[float] = None

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
        nlgeom: Boolean = OFF,
        matrixSolver: SymbolicConstant = DIRECT,
        matrixStorage: SymbolicConstant = SOLVER_DEFAULT,
        maintainAttributes: Boolean = False,
        solutionTechnique: SymbolicConstant = FULL_NEWTON,
        reformKernel: int = 8,
        convertSDI: SymbolicConstant = PROPAGATED,
        utol: Optional[float] = None,
        timePeriod: float = 1,
        timeIncrementationMethod: SymbolicConstant = AUTOMATIC,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Optional[float] = None,
    ):
        """This method creates a GeostaticStep object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].GeostaticStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the
            step. The default value is OFF.
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
        utol
            None or a Float specifying the tolerance for maximum change of displacements. The
            default value is None.
        timePeriod
            A Float specifying the total time period. The default value is 1.0.Note:This parameter
            is ignored unless **timeIncrementationMethod** = AUTOMATIC.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are FIXED and AUTOMATIC. The default value is AUTOMATIC.
        initialInc
            A Float specifying the initial time increment. The default value is the total time
            period for the step.Note:This parameter is ignored unless
            **timeIncrementationMethod** = AUTOMATIC.
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller
            of the suggested initial time increment or 10−5 times the total time period.Note:This
            parameter is ignored unless **timeIncrementationMethod** = AUTOMATIC.
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total
            time period for the step.Note:This parameter is ignored unless
            **timeIncrementationMethod** = AUTOMATIC.

        Returns
        -------
        GeostaticStep
            A :py:class:`~abaqus.Step.GeostaticStep.GeostaticStep` object.

        Raises
        ------
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        description: str = "",
        nlgeom: Boolean = OFF,
        matrixSolver: SymbolicConstant = DIRECT,
        matrixStorage: SymbolicConstant = SOLVER_DEFAULT,
        solutionTechnique: SymbolicConstant = FULL_NEWTON,
        reformKernel: int = 8,
        convertSDI: SymbolicConstant = PROPAGATED,
        utol: Optional[float] = None,
        timePeriod: float = 1,
        timeIncrementationMethod: SymbolicConstant = AUTOMATIC,
        initialInc: Optional[float] = None,
        minInc: Optional[float] = None,
        maxInc: Optional[float] = None,
    ):
        """This method modifies the GeostaticStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string.
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the
            step. The default value is OFF.
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
        utol
            None or a Float specifying the tolerance for maximum change of displacements. The
            default value is None.
        timePeriod
            A Float specifying the total time period. The default value is 1.0.Note:This parameter
            is ignored unless **timeIncrementationMethod** = AUTOMATIC.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are FIXED and AUTOMATIC. The default value is AUTOMATIC.
        initialInc
            A Float specifying the initial time increment. The default value is the total time
            period for the step.Note:This parameter is ignored unless
            **timeIncrementationMethod** = AUTOMATIC.
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller
            of the suggested initial time increment or 10−5 times the total time period.Note:This
            parameter is ignored unless **timeIncrementationMethod** = AUTOMATIC.
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total
            time period for the step.Note:This parameter is ignored unless
            **timeIncrementationMethod** = AUTOMATIC.

        Raises
        ------
        RangeError
        """
        ...
