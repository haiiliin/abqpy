import typing

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
from ..StepMiscellaneous.SteadyStateDirectFrequencyArray import (
    SteadyStateDirectFrequencyArray,
)
from ..StepOutput.DiagnosticPrint import DiagnosticPrint
from ..StepOutput.FieldOutputRequestState import FieldOutputRequestState
from ..StepOutput.HistoryOutputRequestState import HistoryOutputRequestState
from ..StepOutput.Monitor import Monitor
from ..StepOutput.Restart import Restart
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class SteadyStateDirectStep(AnalysisStep):
    """The SteadyStateDirectStep object is used to calculate the linearized steady-state
    response of the system to harmonic excitation in terms of the physical degrees of
    freedom of the model.
    The SteadyStateDirectStep object is derived from the AnalysisStep object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import step
            mdb.models[name].steps[name]

        The corresponding analysis keywords are:

        - STEADY STATE DYNAMICS
        - STEP
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A SymbolicConstant specifying whether damping terms are to be ignored so that a real,
    #: rather than a complex, system matrix is factored. Possible values are REAL_ONLY and
    #: COMPLEX. The default value is COMPLEX.
    factorization: SymbolicConstant = COMPLEX

    #: A SymbolicConstant specifying whether a logarithmic or linear scale is used for output.
    #: Possible values are LOGARITHMIC and LINEAR. The default value is LOGARITHMIC.
    scale: SymbolicConstant = LOGARITHMIC

    #: A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
    #: UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
    matrixStorage: SymbolicConstant = SOLVER_DEFAULT

    #: A Boolean specifying whether to subdivide each frequency range using the
    #: eigenfrequencies of the system. The default value is OFF.
    subdivideUsingEigenfrequencies: Boolean = OFF

    #: A Boolean specifying whether to add to the damping matrix contributions due to friction
    #: effects. The default value is OFF.
    frictionDamping: Boolean = OFF

    #: A String specifying the name of the previous step. The new step appears after this step
    #: in the list of analysis steps.
    previous: str = ""

    #: A String specifying a description of the new step. The default value is an empty string.
    description: str = ""

    #: A :py:class:`~abaqus.StepMiscellaneous.SteadyStateDirectFrequencyArray.SteadyStateDirectFrequencyArray` object.
    frequencyRange: SteadyStateDirectFrequencyArray = []

    #: A SymbolicConstant specifying whether the step has an explicit procedure type
    #: (*procedureType* = ANNEAL, DYNAMIC_EXPLICIT, or DYNAMIC_TEMP_DISPLACEMENT).
    explicit: SymbolicConstant = None

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
    procedureType: SymbolicConstant = None

    #: A Boolean specifying whether the step is suppressed or not. The default value is OFF.
    suppressed: Boolean = OFF

    #: A repository of FieldOutputRequestState objects.
    fieldOutputRequestState: typing.Dict[str, FieldOutputRequestState] = {}

    #: A repository of HistoryOutputRequestState objects.
    historyOutputRequestState: typing.Dict[str, HistoryOutputRequestState] = {}

    #: A :py:class:`~abaqus.StepOutput.DiagnosticPrint.DiagnosticPrint` object.
    diagnosticPrint: DiagnosticPrint = DiagnosticPrint()

    #: A :py:class:`~abaqus.StepOutput.Monitor.Monitor` object.
    monitor: Monitor = None

    #: A :py:class:`~abaqus.StepOutput.Restart.Restart` object.
    restart: Restart = Restart()

    #: A repository of AdaptiveMeshConstraintState objects.
    adaptiveMeshConstraintStates: typing.Dict[str, AdaptiveMeshConstraintState] = {}

    #: A repository of AdaptiveMeshDomain objects.
    adaptiveMeshDomains: typing.Dict[str, AdaptiveMeshDomain] = {}

    #: A :py:class:`~abaqus.StepMiscellaneous.Control.Control` object.
    control: Control = Control()

    #: A :py:class:`~abaqus.StepMiscellaneous.SolverControl.SolverControl` object.
    solverControl: SolverControl = SolverControl()

    #: A repository of BoundaryConditionState objects.
    boundaryConditionStates: typing.Dict[str, BoundaryConditionState] = {}

    #: A repository of InteractionState objects.
    interactionStates: int = None

    #: A repository of LoadState objects.
    loadStates: typing.Dict[str, LoadState] = {}

    #: A repository of LoadCase objects.
    loadCases: typing.Dict[str, LoadCase] = {}

    #: A repository of PredefinedFieldState objects.
    predefinedFieldStates: typing.Dict[str, PredefinedFieldState] = {}

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        previous: str,
        frequencyRange: SteadyStateDirectFrequencyArray,
        description: str = "",
        factorization: SymbolicConstant = COMPLEX,
        scale: SymbolicConstant = LOGARITHMIC,
        matrixStorage: SymbolicConstant = SOLVER_DEFAULT,
        maintainAttributes: Boolean = False,
        subdivideUsingEigenfrequencies: Boolean = OFF,
        frictionDamping: Boolean = OFF,
    ):
        """This method creates a SteadyStateDirectStep object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].SteadyStateDirectStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        frequencyRange
            A :py:class:`~abaqus.StepMiscellaneous.SteadyStateDirectFrequencyArray.SteadyStateDirectFrequencyArray` object.
        description
            A String specifying a description of the new step. The default value is an empty string.
        factorization
            A SymbolicConstant specifying whether damping terms are to be ignored so that a real,
            rather than a complex, system matrix is factored. Possible values are REAL_ONLY and
            COMPLEX. The default value is COMPLEX.
        scale
            A SymbolicConstant specifying whether a logarithmic or linear scale is used for output.
            Possible values are LOGARITHMIC and LINEAR. The default value is LOGARITHMIC.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        subdivideUsingEigenfrequencies
            A Boolean specifying whether to subdivide each frequency range using the
            eigenfrequencies of the system. The default value is OFF.
        frictionDamping
            A Boolean specifying whether to add to the damping matrix contributions due to friction
            effects. The default value is OFF.

        Returns
        -------
        SteadyStateDirectStep
            A :py:class:`~abaqus.Step.SteadyStateDirectStep.SteadyStateDirectStep` object.

        Raises
        ------
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        description: str = "",
        factorization: SymbolicConstant = COMPLEX,
        scale: SymbolicConstant = LOGARITHMIC,
        matrixStorage: SymbolicConstant = SOLVER_DEFAULT,
        subdivideUsingEigenfrequencies: Boolean = OFF,
        frictionDamping: Boolean = OFF,
    ):
        """This method modifies the SteadyStateDirectStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string.
        factorization
            A SymbolicConstant specifying whether damping terms are to be ignored so that a real,
            rather than a complex, system matrix is factored. Possible values are REAL_ONLY and
            COMPLEX. The default value is COMPLEX.
        scale
            A SymbolicConstant specifying whether a logarithmic or linear scale is used for output.
            Possible values are LOGARITHMIC and LINEAR. The default value is LOGARITHMIC.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        subdivideUsingEigenfrequencies
            A Boolean specifying whether to subdivide each frequency range using the
            eigenfrequencies of the system. The default value is OFF.
        frictionDamping
            A Boolean specifying whether to add to the damping matrix contributions due to friction
            effects. The default value is OFF.

        Raises
        ------
        RangeError
        """
        ...
