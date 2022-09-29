import typing

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
from ..StepMiscellaneous.RandomResponseFrequencyArray import (
    RandomResponseFrequencyArray,
)
from ..StepMiscellaneous.RayleighDamping import RayleighDamping
from ..StepMiscellaneous.RayleighDampingByFrequency import RayleighDampingByFrequency
from ..StepMiscellaneous.SolverControl import SolverControl
from ..StepMiscellaneous.StructuralDamping import StructuralDamping
from ..StepMiscellaneous.StructuralDampingByFrequency import (
    StructuralDampingByFrequency,
)
from ..StepOutput.DiagnosticPrint import DiagnosticPrint
from ..StepOutput.FieldOutputRequestState import FieldOutputRequestState
from ..StepOutput.HistoryOutputRequestState import HistoryOutputRequestState
from ..StepOutput.Monitor import Monitor
from ..StepOutput.Restart import Restart
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class RandomResponseStep(AnalysisStep):
    """The RandomResponseStep object is used to give the linearized response of a model to
    random excitation.
    The RandomResponseStep object is derived from the AnalysisStep object.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name]

        The corresponding analysis keywords are:

        - DAMPING
        - MODAL DAMPING
        - RANDOM RESPONSE
        - STEP
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A SymbolicConstant specifying the frequency scale. Possible values are LINEAR and LOG.
    #: The default value is LOG.
    scale: SymbolicConstant = LOG

    #: A String specifying the name of the previous step. The new step appears after this step
    #: in the list of analysis steps.
    previous: str = ""

    #: A String specifying a description of the new step. The default value is an empty string.
    description: str = ""

    #: A :py:class:`~abaqus.StepMiscellaneous.RandomResponseFrequencyArray.RandomResponseFrequencyArray` object specifying frequencies over ranges of modes.
    freq: RandomResponseFrequencyArray = []

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
    explicit: typing.Optional[SymbolicConstant] = None

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
    procedureType: typing.Optional[SymbolicConstant] = None

    #: A Boolean specifying whether the step is suppressed or not. The default value is OFF.
    suppressed: Boolean = OFF

    #: A repository of FieldOutputRequestState objects.
    fieldOutputRequestState: typing.Dict[str, FieldOutputRequestState] = {}

    #: A repository of HistoryOutputRequestState objects.
    historyOutputRequestState: typing.Dict[str, HistoryOutputRequestState] = {}

    #: A :py:class:`~abaqus.StepOutput.DiagnosticPrint.DiagnosticPrint` object.
    diagnosticPrint: DiagnosticPrint = DiagnosticPrint()

    #: A :py:class:`~abaqus.StepOutput.Monitor.Monitor` object.
    monitor: typing.Optional[Monitor] = None

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
    interactionStates: typing.Optional[int] = None

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
        freq: RandomResponseFrequencyArray,
        description: str = "",
        scale: SymbolicConstant = LOG,
        directDamping: typing.Optional[DirectDamping] = None, 
        compositeDamping: typing.Optional[CompositeDamping] = None, 
        rayleighDamping: typing.Optional[RayleighDamping] = None, 
        structuralDamping: typing.Optional[StructuralDamping] = None, 
        directDampingByFrequency: typing.Optional[DirectDampingByFrequency] = None, 
        rayleighDampingByFrequency: typing.Optional[RayleighDampingByFrequency] = None, 
        structuralDampingByFrequency: typing.Optional[StructuralDampingByFrequency] = None, 
        maintainAttributes: Boolean = False,
    ):
        """This method creates a RandomResponseStep object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].RandomResponseStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        freq
            A :py:class:`~abaqus.StepMiscellaneous.RandomResponseFrequencyArray.RandomResponseFrequencyArray` object specifying frequencies over ranges of modes.
        description
            A String specifying a description of the new step. The default value is an empty string.
        scale
            A SymbolicConstant specifying the frequency scale. Possible values are LINEAR and LOG.
            The default value is LOG.
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

        Returns
        -------
        RandomResponseStep
            A :py:class:`~abaqus.Step.RandomResponseStep.RandomResponseStep` object.

        Raises
        ------
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        description: str = "",
        scale: SymbolicConstant = LOG,
        directDamping: typing.Optional[DirectDamping] = None, 
        compositeDamping: typing.Optional[CompositeDamping] = None, 
        rayleighDamping: typing.Optional[RayleighDamping] = None, 
        structuralDamping: typing.Optional[StructuralDamping] = None, 
        directDampingByFrequency: typing.Optional[DirectDampingByFrequency] = None, 
        rayleighDampingByFrequency: typing.Optional[RayleighDampingByFrequency] = None, 
        structuralDampingByFrequency: typing.Optional[StructuralDampingByFrequency] = None, 
    ):
        """This method modifies the RandomResponseStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string.
        scale
            A SymbolicConstant specifying the frequency scale. Possible values are LINEAR and LOG.
            The default value is LOG.
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

        Raises
        ------
        RangeError
        """
        ...
