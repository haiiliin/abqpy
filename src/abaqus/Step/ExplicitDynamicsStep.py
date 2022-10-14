from typing import Dict, Optional, Union
from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .AnalysisStep import AnalysisStep
from ..Adaptivity.AdaptiveMeshConstraintState import AdaptiveMeshConstraintState
from ..Adaptivity.AdaptiveMeshDomain import AdaptiveMeshDomain
from ..BoundaryCondition.BoundaryConditionState import BoundaryConditionState
from ..Load.LoadCase import LoadCase
from ..Load.LoadState import LoadState
from ..PredefinedField.PredefinedFieldState import PredefinedFieldState
from ..StepMiscellaneous.Control import Control
from ..StepMiscellaneous.MassScalingArray import MassScalingArray
from ..StepMiscellaneous.SolverControl import SolverControl
from ..StepOutput.DiagnosticPrint import DiagnosticPrint
from ..StepOutput.FieldOutputRequestState import FieldOutputRequestState
from ..StepOutput.HistoryOutputRequestState import HistoryOutputRequestState
from ..StepOutput.Monitor import Monitor
from ..StepOutput.Restart import Restart
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import (AUTOMATIC_GLOBAL, Boolean, OFF, ON, PREVIOUS_STEP,
                                              SymbolicConstant)


@abaqus_class_doc
class ExplicitDynamicsStep(AnalysisStep):
    """The ExplicitDynamicsStep object is used to perform a dynamic stress/displacement
    analysis using explicit integration in Abaqus/Explicit.
    The ExplicitDynamicsStep object is derived from the AnalysisStep object.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name]

        The corresponding analysis keywords are:

        - BULK VISCOSITY
        - DYNAMIC
        - FIXED MASS SCALING
        - BULK VISCOSITY
        - DYNAMIC
        - VARIABLE MASS SCALING
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A Float specifying the total time period for the step. The default value is 1.0.
    timePeriod: float = 1

    #: A Boolean specifying whether geometric nonlinearities should be accounted for during the
    #: step. The default value is ON.
    nlgeom: Boolean = ON

    #: A Boolean specifying that an adiabatic stress analysis is to be performed. The default
    #: value is OFF.
    adiabatic: Boolean = OFF

    #: A SymbolicConstant specifying the time incrementation method to be used. Possible values
    #: are AUTOMATIC_GLOBAL, AUTOMATIC_EBE, FIXED_USER_DEFINED_INC, and FIXED_EBE. The default
    #: value is AUTOMATIC_GLOBAL.
    timeIncrementationMethod: SymbolicConstant = AUTOMATIC_GLOBAL

    #: None or a Float specifying the maximum time increment. If there is no upper limit,
    #: **maxIncrement** = None. This argument is required only when
    #: **timeIncrementationMethod** = AUTOMATIC_GLOBAL or AUTOMATIC_EBE. The default value is None.
    maxIncrement: Optional[float] = None

    #: A Float specifying the factor that is used to scale the time increment. This argument is
    #: required only when **timeIncrementationMethod** = AUTOMATIC_GLOBAL, AUTOMATIC_EBE, or
    #: FIXED_EBE. The default value is 1.0.
    scaleFactor: float = 1

    #: A Float specifying the linear bulk viscosity parameter, b1b1. The default value is 0.06.
    linearBulkViscosity: float = 0

    #: A Float specifying the quadratic bulk viscosity parameter, b2b2. The default value is
    #: 1.2.
    quadBulkViscosity: float = 1

    #: None or a Float specifying the user-defined time increment. This argument is required
    #: only when **timeIncrementationMethod** = FIXED_USER_DEFINED_INC. The default value is None.
    userDefinedInc: Optional[float] = None

    #: A Boolean specifying whether to use the "improved" (*improvedDtMethod* = ON) or
    #: "conservative" (*improvedDtMethod* = OFF) method to estimate the element stable time
    #: increment for three-dimensional continuum elements and elements with plane stress
    #: formulations (shell, membrane, and two-dimensional plane stress elements). The default
    #: value is ON.
    #:
    #: .. versionadded:: 2018
    #:     The `improvedDtMethod` attribute was added.
    improvedDtMethod: Boolean = ON

    #: A String specifying the name of the previous step. The new step appears after this step
    #: in the list of analysis steps.
    previous: str = ""

    #: A String specifying a description of the new step. The default value is an empty string.
    description: str = ""

    #: A :py:class:`~abaqus.StepMiscellaneous.MassScalingArray.MassScalingArray` object specifying mass scaling controls. The default value is
    #: PREVIOUS_STEP.
    massScaling: Union[MassScalingArray, Literal[C.PREVIOUS_STEP]] = PREVIOUS_STEP

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
        nlgeom: Boolean = ON,
        adiabatic: Boolean = OFF,
        timeIncrementationMethod: SymbolicConstant = AUTOMATIC_GLOBAL,
        maxIncrement: Optional[float] = None,
        scaleFactor: float = 1,
        massScaling: Union[MassScalingArray, Literal[C.PREVIOUS_STEP]] = PREVIOUS_STEP,
        linearBulkViscosity: float = 0,
        quadBulkViscosity: float = 1,
        userDefinedInc: Optional[float] = None,
        maintainAttributes: Boolean = False,
        improvedDtMethod: Boolean = ON,
    ):
        """This method creates an ExplicitDynamicsStep object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ExplicitDynamicsStep

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
            A Float specifying the total time period for the step. The default value is 1.0.
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the
            step. The default value is ON.
        adiabatic
            A Boolean specifying that an adiabatic stress analysis is to be performed. The default
            value is OFF.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are AUTOMATIC_GLOBAL, AUTOMATIC_EBE, FIXED_USER_DEFINED_INC, and FIXED_EBE. The default
            value is AUTOMATIC_GLOBAL.
        maxIncrement
            None or a Float specifying the maximum time increment. If there is no upper limit,
            **maxIncrement** = None. This argument is required only when
            **timeIncrementationMethod** = AUTOMATIC_GLOBAL or AUTOMATIC_EBE. The default value is None.
        scaleFactor
            A Float specifying the factor that is used to scale the time increment. This argument is
            required only when **timeIncrementationMethod** = AUTOMATIC_GLOBAL, AUTOMATIC_EBE, or
            FIXED_EBE. The default value is 1.0.
        massScaling
            A :py:class:`~abaqus.StepMiscellaneous.MassScalingArray.MassScalingArray` object specifying mass scaling controls. The default value is
            PREVIOUS_STEP.
        linearBulkViscosity
            A Float specifying the linear bulk viscosity parameter, b1b1. The default value is 0.06.
        quadBulkViscosity
            A Float specifying the quadratic bulk viscosity parameter, b2b2. The default value is
            1.2.
        userDefinedInc
            None or a Float specifying the user-defined time increment. This argument is required
            only when **timeIncrementationMethod** = FIXED_USER_DEFINED_INC. The default value is None.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        improvedDtMethod
            A Boolean specifying whether to use the "improved" (*improvedDtMethod* = ON) or
            "conservative" (*improvedDtMethod* = OFF) method to estimate the element stable time
            increment for three-dimensional continuum elements and elements with plane stress
            formulations (shell, membrane, and two-dimensional plane stress elements). The default
            value is ON.

            .. versionadded:: 2018
                The **improvedDtMethod** argument was added.

        Returns
        -------
        ExplicitDynamicsStep
            An :py:class:`~abaqus.Step.ExplicitDynamicsStep.ExplicitDynamicsStep` object.

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
        nlgeom: Boolean = ON,
        adiabatic: Boolean = OFF,
        timeIncrementationMethod: SymbolicConstant = AUTOMATIC_GLOBAL,
        maxIncrement: Optional[float] = None,
        scaleFactor: float = 1,
        massScaling: Union[MassScalingArray, Literal[C.PREVIOUS_STEP]] = PREVIOUS_STEP,
        linearBulkViscosity: float = 0,
        quadBulkViscosity: float = 1,
        userDefinedInc: Optional[float] = None,
        improvedDtMethod: Boolean = ON,
    ):
        """This method modifies the ExplicitDynamicsStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string.
        timePeriod
            A Float specifying the total time period for the step. The default value is 1.0.
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the
            step. The default value is ON.
        adiabatic
            A Boolean specifying that an adiabatic stress analysis is to be performed. The default
            value is OFF.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are AUTOMATIC_GLOBAL, AUTOMATIC_EBE, FIXED_USER_DEFINED_INC, and FIXED_EBE. The default
            value is AUTOMATIC_GLOBAL.
        maxIncrement
            None or a Float specifying the maximum time increment. If there is no upper limit,
            **maxIncrement** = None. This argument is required only when
            **timeIncrementationMethod** = AUTOMATIC_GLOBAL or AUTOMATIC_EBE. The default value is None.
        scaleFactor
            A Float specifying the factor that is used to scale the time increment. This argument is
            required only when **timeIncrementationMethod** = AUTOMATIC_GLOBAL, AUTOMATIC_EBE, or
            FIXED_EBE. The default value is 1.0.
        massScaling
            A :py:class:`~abaqus.StepMiscellaneous.MassScalingArray.MassScalingArray` object specifying mass scaling controls. The default value is
            PREVIOUS_STEP.
        linearBulkViscosity
            A Float specifying the linear bulk viscosity parameter, b1b1. The default value is 0.06.
        quadBulkViscosity
            A Float specifying the quadratic bulk viscosity parameter, b2b2. The default value is
            1.2.
        userDefinedInc
            None or a Float specifying the user-defined time increment. This argument is required
            only when **timeIncrementationMethod** = FIXED_USER_DEFINED_INC. The default value is None.
        improvedDtMethod
            A Boolean specifying whether to use the "improved" (*improvedDtMethod* = ON) or
            "conservative" (*improvedDtMethod* = OFF) method to estimate the element stable time
            increment for three-dimensional continuum elements and elements with plane stress
            formulations (shell, membrane, and two-dimensional plane stress elements). The default
            value is ON.

            .. versionadded:: 2018
                The **improvedDtMethod** argument was added.

        Raises
        ------
        RangeError
        """
        ...
