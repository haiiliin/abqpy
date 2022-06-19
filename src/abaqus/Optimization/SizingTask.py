from abaqusConstants import *
from .DesignResponse import DesignResponse
from .GeometricRestriction import GeometricRestriction
from .ObjectiveFunction import ObjectiveFunction
from .OptimizationConstraint import OptimizationConstraint
from .OptimizationTask import OptimizationTask
from .StopCondition import StopCondition


class SizingTask(OptimizationTask):
    """The SizingTask object defines a Sizing task.
    The SizingTask object is derived from the OptimizationTask object.

    Attributes
    ----------
    designResponses: dict[str, DesignResponse]
        A repository of :py:class:`~abaqus.Optimization.DesignResponse.DesignResponse` objects.
    objectiveFunctions: dict[str, ObjectiveFunction]
        A repository of :py:class:`~abaqus.Optimization.ObjectiveFunction.ObjectiveFunction` objects.
    optimizationConstraints: dict[str, OptimizationConstraint]
        A repository of :py:class:`~abaqus.Optimization.OptimizationConstraint.OptimizationConstraint` objects.
    geometricRestrictions: dict[str, GeometricRestriction]
        A repository of :py:class:`~abaqus.Optimization.GeometricRestriction.GeometricRestriction` objects.
    stopConditions: dict[str, StopCondition]
        A repository of :py:class:`~abaqus.Optimization.StopCondition.StopCondition` objects.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import optimization
        mdb.models[name].optimizationTasks[name]
    """

    # A repository of DesignResponse objects.
    designResponses: dict[str, DesignResponse] = dict[str, DesignResponse]()

    # A repository of ObjectiveFunction objects.
    objectiveFunctions: dict[str, ObjectiveFunction] = dict[str, ObjectiveFunction]()

    # A repository of OptimizationConstraint objects.
    optimizationConstraints: dict[str, OptimizationConstraint] = dict[
        str, OptimizationConstraint
    ]()

    # A repository of GeometricRestriction objects.
    geometricRestrictions: dict[str, GeometricRestriction] = dict[
        str, GeometricRestriction
    ]()

    # A repository of StopCondition objects.
    stopConditions: dict[str, StopCondition] = dict[str, StopCondition]()

    def __init__(
        self,
        name: str,
        elementThicknessDeltaStopCriteria: float = 0,
        freezeBoundaryConditionRegions: Boolean = OFF,
        freezeLoadRegions: Boolean = ON,
        modeTrackingRegion: str = MODEL,
        numFulfilledStopCriteria: int = 2,
        numTrackedModes: int = 5,
        objectiveFunctionDeltaStopCriteria: float = 0,
        stopCriteriaDesignCycle: int = 4,
        thicknessMoveLimit: float = 0,
        thicknessUpdateStrategy: SymbolicConstant = NORMAL,
        groupOperator: Boolean = OFF,
    ):
        """This method creates a SizingTask object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

                      mdb.models[name].SizingTask

        Parameters
        ----------
        name
            A String specifying the optimization task repository key.
        elementThicknessDeltaStopCriteria
            A Float specifying the stop criteria based on the change in element thickness. The
            default value is 0.5 × 10–2.
        freezeBoundaryConditionRegions
            A Boolean specifying whether to exclude elements with boundary conditions from the
            optimization. The default value is OFF.
        freezeLoadRegions
            A Boolean specifying whether to exclude elements with loads and elements with loaded
            nodes from the optimization. The default value is ON.
        modeTrackingRegion
            The SymbolicConstatnt MODEL or a Region object specifying the region to use for mode
            tracking. The default value is MODEL.
        numFulfilledStopCriteria
            An Int specifying the number of stop criteria. The default value is 2.
        numTrackedModes
            An Int specifying the number of modes included in mode tracking. The default value is 5.
        objectiveFunctionDeltaStopCriteria
            A Float specifying the stop criteria based on the change in objective function. The
            default value is 0.001.
        stopCriteriaDesignCycle
            An Int specifying the first design cycle used to evaluate convergence criteria. The
            default value is 4.
        thicknessMoveLimit
            A Float specifying the maximum change in thickness per design cycle. The default value
            is 0.25.
        thicknessUpdateStrategy
            A SymbolicConstant specifying the strategy for how the thickness is updated in the
            method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and AGGRESSIVE.
            The default value is NORMAL.
        groupOperator
            A Boolean specifying whether the group in the design response will be evaluated using
            the existing algorithm or a new algorithm based on Abaqus sensitivities. The default
            value of False means that the existing algorithm will be used.

        Returns
        -------
            A SizingTask object.
        """
        super().__init__()
        pass

    def setValues(
        self,
        abaqusSensitivities: Boolean = True,
        elementThicknessDeltaStopCriteria: float = 0,
        freezeBoundaryConditionRegions: Boolean = OFF,
        freezeLoadRegions: Boolean = ON,
        modeTrackingRegion: str = MODEL,
        numFulfilledStopCriteria: int = 2,
        numTrackedModes: int = 5,
        objectiveFunctionDeltaStopCriteria: float = 0,
        stopCriteriaDesignCycle: int = 4,
        thicknessMoveLimit: float = 0,
        thicknessUpdateStrategy: SymbolicConstant = NORMAL,
        groupOperator: Boolean = OFF,
    ):
        """This method modifies the SizingTask object.

        Parameters
        ----------
        abaqusSensitivities
            A Boolean specifying whether to use Abaqus to compute the design responses and their
            sensitivities. The default value is True.
        elementThicknessDeltaStopCriteria
            A Float specifying the stop criteria based on the change in element thickness. The
            default value is 0.5 × 10–2.
        freezeBoundaryConditionRegions
            A Boolean specifying whether to exclude elements with boundary conditions from the
            optimization. The default value is OFF.
        freezeLoadRegions
            A Boolean specifying whether to exclude elements with loads and elements with loaded
            nodes from the optimization. The default value is ON.
        modeTrackingRegion
            The SymbolicConstatnt MODEL or a Region object specifying the region to use for mode
            tracking. The default value is MODEL.
        numFulfilledStopCriteria
            An Int specifying the number of stop criteria. The default value is 2.
        numTrackedModes
            An Int specifying the number of modes included in mode tracking. The default value is 5.
        objectiveFunctionDeltaStopCriteria
            A Float specifying the stop criteria based on the change in objective function. The
            default value is 0.001.
        stopCriteriaDesignCycle
            An Int specifying the first design cycle used to evaluate convergence criteria. The
            default value is 4.
        thicknessMoveLimit
            A Float specifying the maximum change in thickness per design cycle. The default value
            is 0.25.
        thicknessUpdateStrategy
            A SymbolicConstant specifying the strategy for how the thickness is updated in the
            method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and AGGRESSIVE.
            The default value is NORMAL.
        groupOperator
            A Boolean specifying whether the group in the design response will be evaluated using
            the existing algorithm or a new algorithm based on Abaqus sensitivities. The default
            value of False means that the existing algorithm will be used.
        """
        pass
