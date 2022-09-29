from typing import Dict, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .AnalysisStep import AnalysisStep
from ..Adaptivity.AdaptiveMeshConstraintState import AdaptiveMeshConstraintState
from ..Adaptivity.AdaptiveMeshDomain import AdaptiveMeshDomain
from ..BoundaryCondition.BoundaryConditionState import BoundaryConditionState
from ..Load.LoadCase import LoadCase
from ..Load.LoadState import LoadState
from ..PredefinedField.PredefinedFieldState import PredefinedFieldState
from ..Region.Region import Region
from ..StepMiscellaneous.Control import Control
from ..StepMiscellaneous.SolverControl import SolverControl
from ..StepMiscellaneous.SubstructureGenerateFrequencyArray import (
    SubstructureGenerateFrequencyArray,
)
from ..StepMiscellaneous.SubstructureGenerateModesArray import (
    SubstructureGenerateModesArray,
)
from ..StepOutput.DiagnosticPrint import DiagnosticPrint
from ..StepOutput.FieldOutputRequestState import FieldOutputRequestState
from ..StepOutput.HistoryOutputRequestState import HistoryOutputRequestState
from ..StepOutput.Monitor import Monitor
from ..StepOutput.Restart import Restart
from ..UtilityAndView.abaqusConstants import Boolean, NONE, OFF, SymbolicConstant, WHOLE_MODEL


@abaqus_class_doc
class SubstructureGenerateStep(AnalysisStep):
    """TheSubstructureGenerateStep object is used to generate a substructure.
    The SubstructureGenerateStep object is derived from the AnalysisStep object.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name]

        The corresponding analysis keywords are:

        - SUBSTRUCTURE GENERATE
        - STEP
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A SymbolicConstant specifying the subtructure recovery to be computed. Possible values
    #: are WHOLE_MODEL, REGION, and NONE. The default value is WHOLE_MODEL.
    recoveryMatrix: SymbolicConstant = WHOLE_MODEL

    #: A Float specifying the frequency at which to evaluate the frequency dependent
    #: properties. The default value is 0.0.
    frequency: float = 0

    #: A SymbolicConstant specifying the eigenmodes to be retained. Possible values are
    #: MODE_RANGE, FREQUENCY_RANGE, and NONE. The default value is NONE.
    retainedEigenmodesMethod: SymbolicConstant = NONE

    #: A SymbolicConstant specifying the field to which the global damping factors should be
    #: applied. Possible values are ALL, ACOUSTIC, MECHANICAL, and NONE. The default value is
    #: NONE.
    globalDampingField: SymbolicConstant = NONE

    #: A Float specifying the factor to create global Rayleigh mass proportional damping. The
    #: default value is 0.0.
    alphaDampingRatio: float = 0

    #: A Float specifying the factor to create global Rayleigh stiffness proportional damping.
    #: The default value is 0.0.
    betaDampingRatio: float = 0

    #: A Float specifying the factor to create frequency-independent stiffness proportional
    #: structural damping. The default value is 0.0.
    structuralDampingRatio: float = 0

    #: A SymbolicConstant specifying the damping control to include the viscous damping matrix.
    #: Possible values are ELEMENT, FACTOR, COMBINED, and NONE. The default value is NONE.
    viscousDampingControl: SymbolicConstant = NONE

    #: A SymbolicConstant specifying the damping control to include the structural damping
    #: matrix. Possible values are ELEMENT, FACTOR, COMBINED, and NONE. The default value is
    #: NONE.
    structuralDampingControl: SymbolicConstant = NONE

    #: A String specifying the name of the previous step. The new step appears after this step
    #: in the list of analysis steps.
    previous: str = ""

    #: A String specifying a description of the new step. The default value is an empty string.
    description: str = ""

    #: A String specifying a unique identifier for the substructure. The default value is an
    #: empty string.
    substructureIdentifier: str = ""

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region for substructure recovery. This argument is
    #: required when **recoveryMatrix** = REGION.
    recoveryRegion: Region = Region()

    #: A :py:class:`~abaqus.StepMiscellaneous.SubstructureGenerateFrequencyArray.SubstructureGenerateFrequencyArray` object.
    frequencyRange: SubstructureGenerateFrequencyArray = []

    #: A :py:class:`~abaqus.StepMiscellaneous.SubstructureGenerateModesArray.SubstructureGenerateModesArray` object.
    modeRange: SubstructureGenerateModesArray = []

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
        substructureIdentifier: int,
        description: str = "",
        recoveryMatrix: SymbolicConstant = WHOLE_MODEL,
        recoveryRegion: Optional[Region] = None,
        computeGravityLoadVectors: Boolean = False,
        computeReducedMassMatrix: Boolean = False,
        computeReducedStructuralDampingMatrix: Boolean = False,
        computeReducedViscousDampingMatrix: Boolean = False,
        evaluateFrequencyDependentProperties: Boolean = False,
        frequency: float = 0,
        retainedEigenmodesMethod: SymbolicConstant = NONE,
        modeRange: Optional[SubstructureGenerateModesArray] = None,
        frequencyRange: Optional[SubstructureGenerateFrequencyArray] = None,
        globalDampingField: SymbolicConstant = NONE,
        alphaDampingRatio: float = 0,
        betaDampingRatio: float = 0,
        structuralDampingRatio: float = 0,
        viscousDampingControl: SymbolicConstant = NONE,
        structuralDampingControl: SymbolicConstant = NONE,
    ):
        """This method creates a SubstructureGenerateStep object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].SubstructureGenerateStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        substructureIdentifier
            An Integer specifying a unique identifier for the substructure.
        description
            A String specifying a description of the new step. The default value is an empty string.
        recoveryMatrix
            A SymbolicConstant specifying the subtructure recovery to be computed. Possible values
            are WHOLE_MODEL, REGION, and NONE. The default value is WHOLE_MODEL.
        recoveryRegion
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region for substructure recovery. This argument is
            required when **recoveryMatrix** = REGION.
        computeGravityLoadVectors
            A Boolean specifying whether to compute the gravity load vectors. The default value is
            False.
        computeReducedMassMatrix
            A Boolean specifying whether to compute the reduced mass matrix. The default value is
            False.
        computeReducedStructuralDampingMatrix
            A Boolean specifying whether to compute the reduced structural damping matrix. The
            default value is False.
        computeReducedViscousDampingMatrix
            A Boolean specifying whether to compute the reduced viscous damping matrix. The default
            value is False.
        evaluateFrequencyDependentProperties
            A Boolean specifying whether to evaluate the frequency dependent properties. The default
            value is False.
        frequency
            A Float specifying the frequency at which to evaluate the frequency dependent
            properties. The default value is 0.0.
        retainedEigenmodesMethod
            A SymbolicConstant specifying the eigenmodes to be retained. Possible values are
            MODE_RANGE, FREQUENCY_RANGE, and NONE. The default value is NONE.
        modeRange
            A :py:class:`~abaqus.StepMiscellaneous.SubstructureGenerateModesArray.SubstructureGenerateModesArray` object.
        frequencyRange
            A :py:class:`~abaqus.StepMiscellaneous.SubstructureGenerateFrequencyArray.SubstructureGenerateFrequencyArray` object.
        globalDampingField
            A SymbolicConstant specifying the field to which the global damping factors should be
            applied. Possible values are ALL, ACOUSTIC, MECHANICAL, and NONE. The default value is
            NONE.
        alphaDampingRatio
            A Float specifying the factor to create global Rayleigh mass proportional damping. The
            default value is 0.0.
        betaDampingRatio
            A Float specifying the factor to create global Rayleigh stiffness proportional damping.
            The default value is 0.0.
        structuralDampingRatio
            A Float specifying the factor to create frequency-independent stiffness proportional
            structural damping. The default value is 0.0.
        viscousDampingControl
            A SymbolicConstant specifying the damping control to include the viscous damping matrix.
            Possible values are ELEMENT, FACTOR, COMBINED, and NONE. The default value is NONE.
        structuralDampingControl
            A SymbolicConstant specifying the damping control to include the structural damping
            matrix. Possible values are ELEMENT, FACTOR, COMBINED, and NONE. The default value is
            NONE.

        Returns
        -------
        SubstructureGenerateStep
            A :py:class:`~abaqus.Step.SubstructureGenerateStep.SubstructureGenerateStep` object.

        Raises
        ------
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        description: str = "",
        recoveryMatrix: SymbolicConstant = WHOLE_MODEL,
        recoveryRegion: Optional[Region] = None,
        computeGravityLoadVectors: Boolean = False,
        computeReducedMassMatrix: Boolean = False,
        computeReducedStructuralDampingMatrix: Boolean = False,
        computeReducedViscousDampingMatrix: Boolean = False,
        evaluateFrequencyDependentProperties: Boolean = False,
        frequency: float = 0,
        retainedEigenmodesMethod: SymbolicConstant = NONE,
        modeRange: Optional[SubstructureGenerateModesArray] = None,
        frequencyRange: Optional[SubstructureGenerateFrequencyArray] = None,
        globalDampingField: SymbolicConstant = NONE,
        alphaDampingRatio: float = 0,
        betaDampingRatio: float = 0,
        structuralDampingRatio: float = 0,
        viscousDampingControl: SymbolicConstant = NONE,
        structuralDampingControl: SymbolicConstant = NONE,
    ):
        """This method modifies the SubstructureGenerateStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string.
        recoveryMatrix
            A SymbolicConstant specifying the subtructure recovery to be computed. Possible values
            are WHOLE_MODEL, REGION, and NONE. The default value is WHOLE_MODEL.
        recoveryRegion
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region for substructure recovery. This argument is
            required when **recoveryMatrix** = REGION.
        computeGravityLoadVectors
            A Boolean specifying whether to compute the gravity load vectors. The default value is
            False.
        computeReducedMassMatrix
            A Boolean specifying whether to compute the reduced mass matrix. The default value is
            False.
        computeReducedStructuralDampingMatrix
            A Boolean specifying whether to compute the reduced structural damping matrix. The
            default value is False.
        computeReducedViscousDampingMatrix
            A Boolean specifying whether to compute the reduced viscous damping matrix. The default
            value is False.
        evaluateFrequencyDependentProperties
            A Boolean specifying whether to evaluate the frequency dependent properties. The default
            value is False.
        frequency
            A Float specifying the frequency at which to evaluate the frequency dependent
            properties. The default value is 0.0.
        retainedEigenmodesMethod
            A SymbolicConstant specifying the eigenmodes to be retained. Possible values are
            MODE_RANGE, FREQUENCY_RANGE, and NONE. The default value is NONE.
        modeRange
            A :py:class:`~abaqus.StepMiscellaneous.SubstructureGenerateModesArray.SubstructureGenerateModesArray` object.
        frequencyRange
            A :py:class:`~abaqus.StepMiscellaneous.SubstructureGenerateFrequencyArray.SubstructureGenerateFrequencyArray` object.
        globalDampingField
            A SymbolicConstant specifying the field to which the global damping factors should be
            applied. Possible values are ALL, ACOUSTIC, MECHANICAL, and NONE. The default value is
            NONE.
        alphaDampingRatio
            A Float specifying the factor to create global Rayleigh mass proportional damping. The
            default value is 0.0.
        betaDampingRatio
            A Float specifying the factor to create global Rayleigh stiffness proportional damping.
            The default value is 0.0.
        structuralDampingRatio
            A Float specifying the factor to create frequency-independent stiffness proportional
            structural damping. The default value is 0.0.
        viscousDampingControl
            A SymbolicConstant specifying the damping control to include the viscous damping matrix.
            Possible values are ELEMENT, FACTOR, COMBINED, and NONE. The default value is NONE.
        structuralDampingControl
            A SymbolicConstant specifying the damping control to include the structural damping
            matrix. Possible values are ELEMENT, FACTOR, COMBINED, and NONE. The default value is
            NONE.

        Raises
        ------
        RangeError
        """
        ...
