from typing import Dict, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

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
from ..UtilityAndView.abaqusConstants import Boolean, DEFAULT, OFF, SOLVER_DEFAULT, SUBSPACE, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class BuckleStep(AnalysisStep):
    """The BuckleStep object controls eigenvalue buckling estimation.
    The BuckleStep object is derived from the AnalysisStep object.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name]

        The corresponding analysis keywords are:

        - BUCKLE
        - STEP
    """

    #: A String specifying the repository key.
    name: str = ""

    #: An Int specifying the number of eigenvalues to be estimated.
    numEigen: Optional[int] = None

    #: A SymbolicConstant specifying the eigensolver. Possible values are SUBSPACE and LANCZOS.
    #: The default value is SUBSPACE.
    eigensolver: SymbolicConstant = SUBSPACE

    #: None or a Float specifying the minimum eigenvalue of interest. The default value is
    #: None.
    minEigen: Optional[float] = None

    #: None or a Float specifying the maximum eigenvalue of interest. The default value is
    #: None.
    maxEigen: Optional[float] = None

    #: An Int specifying the number of vectors used in the iteration. The default value is the
    #: minimum of (2*n*, **n** + 8), where **n** is the number of eigenvalues requested.
    vectors: Optional[int] = None

    #: An Int specifying the maximum number of iterations. The default value is 30.
    maxIterations: int = 30

    #: The SymbolicConstant DEFAULT or an Int specifying the size of the Lanczos block steps.
    #: The default value is DEFAULT.
    blockSize: SymbolicConstant = DEFAULT

    #: The SymbolicConstant DEFAULT or an Int specifying the maximum number of Lanczos block
    #: steps within each Lanczos run. The default value is DEFAULT. Note: *minEigen*,
    #: **blockSize**, and **maxBlocks** are ignored unless **eigensolver** = LANCZOS.
    maxBlocks: SymbolicConstant = DEFAULT

    #: A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
    #: UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
    matrixStorage: SymbolicConstant = SOLVER_DEFAULT

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

    #: A DiagnosticPrint object.
    diagnosticPrint: DiagnosticPrint = DiagnosticPrint()

    #: A Monitor object.
    monitor: Optional[Monitor] = None

    #: A Restart object.
    restart: Restart = Restart()

    #: A repository of AdaptiveMeshConstraintState objects.
    adaptiveMeshConstraintStates: Dict[str, AdaptiveMeshConstraintState] = {}

    #: A repository of AdaptiveMeshDomain objects.
    adaptiveMeshDomains: Dict[str, AdaptiveMeshDomain] = {}

    #: A Control object.
    control: Control = Control()

    #: A SolverControl object.
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
        numEigen: int,
        description: str = "",
        eigensolver: Literal[C.LANCZOS, C.SUBSPACE] = SUBSPACE,
        minEigen: Optional[float] = None,
        maxEigen: Optional[float] = None,
        vectors: Optional[int] = None,
        maxIterations: int = 30,
        blockSize: Literal[C.DEFAULT] = DEFAULT,
        maxBlocks: Literal[C.LANCZOS, C.DEFAULT] = DEFAULT,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
        maintainAttributes: Boolean = False,
    ):
        """This method creates a BuckleStep object.

        .. note::
            This function can be accessed by::

                mdb.models[name].BuckleStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        numEigen
            An Int specifying the number of eigenvalues to be estimated.
        description
            A String specifying a description of the new step. The default value is an empty string.
        eigensolver
            A SymbolicConstant specifying the eigensolver. Possible values are SUBSPACE and LANCZOS.
            The default value is SUBSPACE.
        minEigen
            None or a Float specifying the minimum eigenvalue of interest. The default value is
            None.
        maxEigen
            None or a Float specifying the maximum eigenvalue of interest. The default value is
            None.
        vectors
            An Int specifying the number of vectors used in the iteration. The default value is the
            minimum of (2*n*, **n** + 8), where **n** is the number of eigenvalues requested.
        maxIterations
            An Int specifying the maximum number of iterations. The default value is 30.
        blockSize
            The SymbolicConstant DEFAULT or an Int specifying the size of the Lanczos block steps.
            The default value is DEFAULT.
        maxBlocks
            The SymbolicConstant DEFAULT or an Int specifying the maximum number of Lanczos block
            steps within each Lanczos run. The default value is DEFAULT. Note: *minEigen*,
            **blockSize**, and **maxBlocks** are ignored unless **eigensolver** = LANCZOS.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.

        Returns
        -------
        BuckleStep
            A BuckleStep object.

        Raises
        ------
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        description: str = "",
        eigensolver: Literal[C.LANCZOS, C.SUBSPACE] = SUBSPACE,
        minEigen: Optional[float] = None,
        maxEigen: Optional[float] = None,
        vectors: Optional[int] = None,
        maxIterations: int = 30,
        blockSize: Literal[C.DEFAULT] = DEFAULT,
        maxBlocks: Literal[C.LANCZOS, C.DEFAULT] = DEFAULT,
        matrixStorage: Literal[C.SYMMETRIC, C.SOLVER_DEFAULT, C.UNSYMMETRIC] = SOLVER_DEFAULT,
    ):
        """This method modifies the BuckleStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string.
        eigensolver
            A SymbolicConstant specifying the eigensolver. Possible values are SUBSPACE and LANCZOS.
            The default value is SUBSPACE.
        minEigen
            None or a Float specifying the minimum eigenvalue of interest. The default value is
            None.
        maxEigen
            None or a Float specifying the maximum eigenvalue of interest. The default value is
            None.
        vectors
            An Int specifying the number of vectors used in the iteration. The default value is the
            minimum of (2*n*, **n** + 8), where **n** is the number of eigenvalues requested.
        maxIterations
            An Int specifying the maximum number of iterations. The default value is 30.
        blockSize
            The SymbolicConstant DEFAULT or an Int specifying the size of the Lanczos block steps.
            The default value is DEFAULT.
        maxBlocks
            The SymbolicConstant DEFAULT or an Int specifying the maximum number of Lanczos block
            steps within each Lanczos run. The default value is DEFAULT. Note: *minEigen*,
            **blockSize**, and **maxBlocks** are ignored unless **eigensolver** = LANCZOS.
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.

        Raises
        ------
        RangeError
        """
        ...
