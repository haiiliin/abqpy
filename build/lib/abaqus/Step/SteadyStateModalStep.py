from typing import Dict, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .AnalysisStep import AnalysisStep
from ..Adaptivity.AdaptiveMeshConstraintState import AdaptiveMeshConstraintState
from ..Adaptivity.AdaptiveMeshDomain import AdaptiveMeshDomain
from ..BoundaryCondition.BoundaryConditionState import BoundaryConditionState
from ..Load.LoadCase import LoadCase
from ..Load.LoadState import LoadState
from ..PredefinedField.PredefinedFieldState import PredefinedFieldState
from ..StepMiscellaneous.CompositeDamping import CompositeDamping
from ..StepMiscellaneous.Control import Control
from ..StepMiscellaneous.DirectDamping import DirectDamping
from ..StepMiscellaneous.DirectDampingByFrequency import DirectDampingByFrequency
from ..StepMiscellaneous.RayleighDamping import RayleighDamping
from ..StepMiscellaneous.RayleighDampingByFrequency import RayleighDampingByFrequency
from ..StepMiscellaneous.SolverControl import SolverControl
from ..StepMiscellaneous.SteadyStateModalFrequencyArray import (
    SteadyStateModalFrequencyArray,
)
from ..StepMiscellaneous.StructuralDamping import StructuralDamping
from ..StepMiscellaneous.StructuralDampingByFrequency import (
    StructuralDampingByFrequency,
)
from ..StepOutput.DiagnosticPrint import DiagnosticPrint
from ..StepOutput.FieldOutputRequestState import FieldOutputRequestState
from ..StepOutput.HistoryOutputRequestState import HistoryOutputRequestState
from ..StepOutput.Monitor import Monitor
from ..StepOutput.Restart import Restart
from ..UtilityAndView.abaqusConstants import Boolean, LOGARITHMIC, OFF, ON, SymbolicConstant


@abaqus_class_doc
class SteadyStateModalStep(AnalysisStep):
    """he SteadyStateModalStep object is used to calculate the linearized steady-state response
    of the system to harmonic excitation.
    The SteadyStateModalStep object is derived from the AnalysisStep object.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name]

        The corresponding analysis keywords are:

        - DAMPING
        - MODAL DAMPING
        - STEADY STATE DYNAMICS
        - STEP
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A SymbolicConstant specifying whether a logarithmic or linear scale is used for output.
    #: Possible values are LOGARITHMIC and LINEAR. The default value is LOGARITHMIC.
    scale: SymbolicConstant = LOGARITHMIC

    #: A Boolean specifying whether to subdivide each frequency range using the
    #: eigenfrequencies of the system. The default value is ON.
    subdivideUsingEigenfrequencies: Boolean = ON

    #: A String specifying the name of the previous step. The new step appears after this step
    #: in the list of analysis steps.
    previous: str = ""

    #: A String specifying a description of the new step. The default value is an empty string.
    description: str = ""

    #: A :py:class:`~abaqus.StepMiscellaneous.SteadyStateModalFrequencyArray.SteadyStateModalFrequencyArray` object.
    frequencyRange: SteadyStateModalFrequencyArray = []

    #: A :py:class:`~abaqus.StepMiscellaneous.DirectDamping.DirectDamping` object.
    directDamping: DirectDamping = DirectDamping()

    #: A :py:class:`~abaqus.StepMiscellaneous.CompositeDamping.CompositeDamping` object.
    compositeDamping: CompositeDamping = CompositeDamping()

    #: A :py:class:`~abaqus.StepMiscellaneous.RayleighDamping.RayleighDamping` object.
    rayleighDamping: RayleighDamping = RayleighDamping()

    #: A :py:class:`~abaqus.StepMiscellaneous.StructuralDamping.StructuralDamping` object.
    structuralDamping: StructuralDamping = StructuralDamping()

    #: A :py:class:`~abaqus.StepMiscellaneous.DirectDampingByFrequency.DirectDampingByFrequency` object.
    directDampingByFrequency: DirectDampingByFrequency = DirectDampingByFrequency()

    #: A :py:class:`~abaqus.StepMiscellaneous.RayleighDampingByFrequency.RayleighDampingByFrequency` object.
    rayleighDampingByFrequency: RayleighDampingByFrequency = (
        RayleighDampingByFrequency()
    )

    #: A :py:class:`~abaqus.StepMiscellaneous.StructuralDampingByFrequency.StructuralDampingByFrequency` object.
    structuralDampingByFrequency: StructuralDampingByFrequency = (
        StructuralDampingByFrequency()
    )

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
        frequencyRange: SteadyStateModalFrequencyArray,
        description: str = "",
        scale: SymbolicConstant = LOGARITHMIC,
        directDamping: Optional[DirectDamping] = None, 
        compositeDamping: Optional[CompositeDamping] = None, 
        rayleighDamping: Optional[RayleighDamping] = None, 
        structuralDamping: Optional[StructuralDamping] = None, 
        directDampingByFrequency: Optional[DirectDampingByFrequency] = None, 
        rayleighDampingByFrequency: Optional[RayleighDampingByFrequency] = None, 
        structuralDampingByFrequency: Optional[StructuralDampingByFrequency] = None, 
        maintainAttributes: Boolean = False,
        subdivideUsingEigenfrequencies: Boolean = ON,
    ):
        """This method creates a SteadyStateModalStep object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].SteadyStateModalStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        frequencyRange
            A :py:class:`~abaqus.StepMiscellaneous.SteadyStateModalFrequencyArray.SteadyStateModalFrequencyArray` object.
        description
            A String specifying a description of the new step. The default value is an empty string.
        scale
            A SymbolicConstant specifying whether a logarithmic or linear scale is used for output.
            Possible values are LOGARITHMIC and LINEAR. The default value is LOGARITHMIC.
        directDamping
            A :py:class:`~abaqus.StepMiscellaneous.DirectDamping.DirectDamping` object.
        compositeDamping
            A :py:class:`~abaqus.StepMiscellaneous.CompositeDamping.CompositeDamping` object.
        rayleighDamping
            A :py:class:`~abaqus.StepMiscellaneous.RayleighDamping.RayleighDamping` object.
        structuralDamping
            A :py:class:`~abaqus.StepMiscellaneous.StructuralDamping.StructuralDamping` object.
        directDampingByFrequency
            A :py:class:`~abaqus.StepMiscellaneous.DirectDampingByFrequency.DirectDampingByFrequency` object.
        rayleighDampingByFrequency
            A :py:class:`~abaqus.StepMiscellaneous.RayleighDampingByFrequency.RayleighDampingByFrequency` object.
        structuralDampingByFrequency
            A :py:class:`~abaqus.StepMiscellaneous.StructuralDampingByFrequency.StructuralDampingByFrequency` object.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        subdivideUsingEigenfrequencies
            A Boolean specifying whether to subdivide each frequency range using the
            eigenfrequencies of the system. The default value is ON.

        Returns
        -------
        SteadyStateModalStep
            A :py:class:`~abaqus.Step.SteadyStateModalStep.SteadyStateModalStep` object.

        Raises
        ------
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        description: str = "",
        scale: SymbolicConstant = LOGARITHMIC,
        directDamping: Optional[DirectDamping] = None, 
        compositeDamping: Optional[CompositeDamping] = None, 
        rayleighDamping: Optional[RayleighDamping] = None, 
        structuralDamping: Optional[StructuralDamping] = None, 
        directDampingByFrequency: Optional[DirectDampingByFrequency] = None, 
        rayleighDampingByFrequency: Optional[RayleighDampingByFrequency] = None, 
        structuralDampingByFrequency: Optional[StructuralDampingByFrequency] = None, 
        subdivideUsingEigenfrequencies: Boolean = ON,
    ):
        """This method modifies the SteadyStateModalStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string.
        scale
            A SymbolicConstant specifying whether a logarithmic or linear scale is used for output.
            Possible values are LOGARITHMIC and LINEAR. The default value is LOGARITHMIC.
        directDamping
            A :py:class:`~abaqus.StepMiscellaneous.DirectDamping.DirectDamping` object.
        compositeDamping
            A :py:class:`~abaqus.StepMiscellaneous.CompositeDamping.CompositeDamping` object.
        rayleighDamping
            A :py:class:`~abaqus.StepMiscellaneous.RayleighDamping.RayleighDamping` object.
        structuralDamping
            A :py:class:`~abaqus.StepMiscellaneous.StructuralDamping.StructuralDamping` object.
        directDampingByFrequency
            A :py:class:`~abaqus.StepMiscellaneous.DirectDampingByFrequency.DirectDampingByFrequency` object.
        rayleighDampingByFrequency
            A :py:class:`~abaqus.StepMiscellaneous.RayleighDampingByFrequency.RayleighDampingByFrequency` object.
        structuralDampingByFrequency
            A :py:class:`~abaqus.StepMiscellaneous.StructuralDampingByFrequency.StructuralDampingByFrequency` object.
        subdivideUsingEigenfrequencies
            A Boolean specifying whether to subdivide each frequency range using the
            eigenfrequencies of the system. The default value is ON.

        Raises
        ------
        RangeError
        """
        ...
