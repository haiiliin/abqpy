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
from ..StepMiscellaneous.ResponseSpectrumComponentArray import (
    ResponseSpectrumComponentArray,
)
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
from ..UtilityAndView.abaqusConstants import ABS, Boolean, OFF, SINGLE_DIRECTION, SymbolicConstant


@abaqus_class_doc
class ResponseSpectrumStep(AnalysisStep):
    """The ResponseSpectrumStep object is used to calculate estimates of peak values of
    displacements and stresses based on user-supplied response spectra and on the natural
    modes of the system.
    The ResponseSpectrumStep object is derived from the AnalysisStep object.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name]

        The corresponding analysis keywords are:

        - RESPONSE SPECTRUM
        - STEP
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A SymbolicConstant specifying the order and method used to sum the components. Possible
    #: values are SINGLE_DIRECTION, MULTIPLE_DIRECTION_ABSOLUTE_SUM,
    #: MULTIPLE_DIRECTION_SRSS_SUM, MULTIPLE_DIRECTION_THIRTY_PERCENT_RULE, and
    #: MULTIPLE_DIRECTION_FORTY_PERCENT_RULE. The default value is SINGLE_DIRECTION.
    comp: SymbolicConstant = SINGLE_DIRECTION

    #: A SymbolicConstant specifying the method used to sum the components. Possible values are
    #: ABS, CQC, NRL, SRSS, TENP, DSC, and GRP. The default value is ABS.
    sum: SymbolicConstant = ABS

    #: A String specifying the name of the previous step. The new step appears after this step
    #: in the list of analysis steps.
    previous: str = ""

    #: A String specifying a description of the new step. The default value is an empty string.
    description: str = ""

    #: A :py:class:`~abaqus.StepMiscellaneous.ResponseSpectrumComponentArray.ResponseSpectrumComponentArray` object.
    components: ResponseSpectrumComponentArray = []

    #: A :py:class:`~abaqus.StepMiscellaneous.DirectDamping.DirectDamping` object.
    directDamping: DirectDamping = DirectDamping()

    #: A :py:class:`~abaqus.StepMiscellaneous.CompositeDamping.CompositeDamping` object.
    compositeDamping: CompositeDamping = CompositeDamping()

    #: A :py:class:`~abaqus.StepMiscellaneous.RayleighDamping.RayleighDamping` object.
    rayleighDamping: RayleighDamping = RayleighDamping()

    #: A :py:class:`~abaqus.StepMiscellaneous.DirectDampingByFrequency.DirectDampingByFrequency` object.
    directDampingByFrequency: DirectDampingByFrequency = DirectDampingByFrequency()

    #: A :py:class:`~abaqus.StepMiscellaneous.RayleighDampingByFrequency.RayleighDampingByFrequency` object.
    rayleighDampingByFrequency: RayleighDampingByFrequency = (
        RayleighDampingByFrequency()
    )

    #: A :py:class:`~abaqus.StepMiscellaneous.StructuralDamping.StructuralDamping` object.
    structuralDamping: StructuralDamping = StructuralDamping()

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
        components: ResponseSpectrumComponentArray,
        description: str = "",
        comp: SymbolicConstant = SINGLE_DIRECTION,
        sum: SymbolicConstant = ABS,
        directDamping: Optional[DirectDamping] = None, 
        compositeDamping: Optional[CompositeDamping] = None, 
        rayleighDamping: Optional[RayleighDamping] = None, 
        directDampingByFrequency: Optional[DirectDampingByFrequency] = None, 
        rayleighDampingByFrequency: Optional[RayleighDampingByFrequency] = None, 
        maintainAttributes: Boolean = False,
    ):
        """This method creates a ResponseSpectrumStep object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ResponseSpectrumStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        components
            A :py:class:`~abaqus.StepMiscellaneous.ResponseSpectrumComponentArray.ResponseSpectrumComponentArray` object.
        description
            A String specifying a description of the new step. The default value is an empty string.
        comp
            A SymbolicConstant specifying the order and method used to sum the components. Possible
            values are SINGLE_DIRECTION, MULTIPLE_DIRECTION_ABSOLUTE_SUM,
            MULTIPLE_DIRECTION_SRSS_SUM, MULTIPLE_DIRECTION_THIRTY_PERCENT_RULE, and
            MULTIPLE_DIRECTION_FORTY_PERCENT_RULE. The default value is SINGLE_DIRECTION.
        sum
            A SymbolicConstant specifying the method used to sum the components. Possible values are
            ABS, CQC, NRL, SRSS, TENP, DSC, and GRP. The default value is ABS.
        directDamping
            A :py:class:`~abaqus.StepMiscellaneous.DirectDamping.DirectDamping` object.
        compositeDamping
            A :py:class:`~abaqus.StepMiscellaneous.CompositeDamping.CompositeDamping` object.
        rayleighDamping
            A :py:class:`~abaqus.StepMiscellaneous.RayleighDamping.RayleighDamping` object.
        directDampingByFrequency
            A :py:class:`~abaqus.StepMiscellaneous.DirectDampingByFrequency.DirectDampingByFrequency` object.
        rayleighDampingByFrequency
            A :py:class:`~abaqus.StepMiscellaneous.RayleighDampingByFrequency.RayleighDampingByFrequency` object.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.

        Returns
        -------
        ResponseSpectrumStep
            A :py:class:`~abaqus.Step.ResponseSpectrumStep.ResponseSpectrumStep` object.

        Raises
        ------
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        description: str = "",
        comp: SymbolicConstant = SINGLE_DIRECTION,
        sum: SymbolicConstant = ABS,
        directDamping: Optional[DirectDamping] = None, 
        compositeDamping: Optional[CompositeDamping] = None, 
        rayleighDamping: Optional[RayleighDamping] = None, 
        directDampingByFrequency: Optional[DirectDampingByFrequency] = None, 
        rayleighDampingByFrequency: Optional[RayleighDampingByFrequency] = None, 
    ):
        """This method modifies the ResponseSpectrumStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string.
        comp
            A SymbolicConstant specifying the order and method used to sum the components. Possible
            values are SINGLE_DIRECTION, MULTIPLE_DIRECTION_ABSOLUTE_SUM,
            MULTIPLE_DIRECTION_SRSS_SUM, MULTIPLE_DIRECTION_THIRTY_PERCENT_RULE, and
            MULTIPLE_DIRECTION_FORTY_PERCENT_RULE. The default value is SINGLE_DIRECTION.
        sum
            A SymbolicConstant specifying the method used to sum the components. Possible values are
            ABS, CQC, NRL, SRSS, TENP, DSC, and GRP. The default value is ABS.
        directDamping
            A :py:class:`~abaqus.StepMiscellaneous.DirectDamping.DirectDamping` object.
        compositeDamping
            A :py:class:`~abaqus.StepMiscellaneous.CompositeDamping.CompositeDamping` object.
        rayleighDamping
            A :py:class:`~abaqus.StepMiscellaneous.RayleighDamping.RayleighDamping` object.
        directDampingByFrequency
            A :py:class:`~abaqus.StepMiscellaneous.DirectDampingByFrequency.DirectDampingByFrequency` object.
        rayleighDampingByFrequency
            A :py:class:`~abaqus.StepMiscellaneous.RayleighDampingByFrequency.RayleighDampingByFrequency` object.

        Raises
        ------
        RangeError
        """
        ...
