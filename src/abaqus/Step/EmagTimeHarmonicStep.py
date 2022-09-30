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
from ..StepMiscellaneous.EmagTimeHarmonicFrequencyArray import (
    EmagTimeHarmonicFrequencyArray,
)
from ..StepMiscellaneous.SolverControl import SolverControl
from ..StepOutput.DiagnosticPrint import DiagnosticPrint
from ..StepOutput.FieldOutputRequestState import FieldOutputRequestState
from ..StepOutput.HistoryOutputRequestState import HistoryOutputRequestState
from ..StepOutput.Monitor import Monitor
from ..StepOutput.Restart import Restart
from ..UtilityAndView.abaqusConstants import Boolean, COMPLEX, OFF, SOLVER_DEFAULT, SymbolicConstant


@abaqus_class_doc
class EmagTimeHarmonicStep(AnalysisStep):
    """The EmagTimeHarmonicStep object is used to calculate the electromagnetic response of the
    system to harmonic excitation of the model.
    The EmagTimeHarmonicStep object is derived from the AnalysisStep object.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name]

        The corresponding analysis keywords are:

        - ELECTROMAGNETIC TIME HARMONIC
        - STEP
    """

    #: A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
    #: UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
    matrixStorage: SymbolicConstant = SOLVER_DEFAULT

    #: A Boolean specifying whether to subdivide each frequency range using the
    #: eigenfrequencies of the system. The default value is OFF.
    subdivideUsingEigenfrequencies: Boolean = OFF

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

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the previous step. The new step appears after this step
    #: in the list of analysis steps.
    previous: str

    #: An :py:class:`~abaqus.StepMiscellaneous.EmagTimeHarmonicFrequencyArray.EmagTimeHarmonicFrequencyArray` object.
    frequencyRange: EmagTimeHarmonicFrequencyArray

    #: A String specifying a description of the new step. The default value is an empty string.
    description: str = ""

    #: A SymbolicConstant specifying whether damping terms are to be ignored so that a real,
    #: rather than a complex, system matrix is factored. Possible values are REAL_ONLY and
    #: COMPLEX. The default value is COMPLEX.
    factorization: SymbolicConstant = COMPLEX

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        previous: str,
        frequencyRange: EmagTimeHarmonicFrequencyArray,
        description: str = "",
        factorization: SymbolicConstant = COMPLEX,
    ):
        """This method creates a EmagTimeHarmonicStep object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].EmagTimeHarmonicStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        frequencyRange
            An :py:class:`~abaqus.StepMiscellaneous.EmagTimeHarmonicFrequencyArray.EmagTimeHarmonicFrequencyArray` object.
        description
            A String specifying a description of the new step. The default value is an empty string.
        factorization
            A SymbolicConstant specifying whether damping terms are to be ignored so that a real,
            rather than a complex, system matrix is factored. Possible values are REAL_ONLY and
            COMPLEX. The default value is COMPLEX.

        Returns
        -------
        EmagTimeHarmonicStep
            An :py:class:`~abaqus.Step.EmagTimeHarmonicStep.EmagTimeHarmonicStep` object.

        Raises
        ------
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self, description: str = "", factorization: SymbolicConstant = COMPLEX
    ):
        """This method modifies the EmagTimeHarmonicStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string.
        factorization
            A SymbolicConstant specifying whether damping terms are to be ignored so that a real,
            rather than a complex, system matrix is factored. Possible values are REAL_ONLY and
            COMPLEX. The default value is COMPLEX.

        Raises
        ------
        RangeError
        """
        ...
