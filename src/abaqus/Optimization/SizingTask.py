import typing

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .DesignResponse import DesignResponse
from .GeometricRestriction import GeometricRestriction
from .ObjectiveFunction import ObjectiveFunction
from .OptimizationConstraint import OptimizationConstraint
from .OptimizationTask import OptimizationTask
from .StopCondition import StopCondition
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class SizingTask(OptimizationTask):
    """The SizingTask object defines a Sizing task.
    The SizingTask object is derived from the OptimizationTask object.

    .. note:: 
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name]
    """

    #: A repository of DesignResponse objects.
    designResponses: typing.Dict[str, DesignResponse] = {}

    #: A repository of ObjectiveFunction objects.
    objectiveFunctions: typing.Dict[str, ObjectiveFunction] = {}

    #: A repository of OptimizationConstraint objects.
    optimizationConstraints: typing.Dict[str, OptimizationConstraint] = {}

    #: A repository of GeometricRestriction objects.
    geometricRestrictions: typing.Dict[str, GeometricRestriction] = {}

    #: A repository of StopCondition objects.
    stopConditions: typing.Dict[str, StopCondition] = {}

    #: A String specifying the optimization task repository key.
    name: str

    #: A Boolean specifying whether to use Abaqus to compute the design responses and their
    #: sensitivities. The default value is False.
    #:
    #: .. versionadded:: 2019
    #:     The `abaqusSensitivities` attribute was added.
    abaqusSensitivities: Boolean = False

    #: A Float specifying the stop criteria based on the change in element thickness. The
    #: default value is 0.5 × 10-2.
    elementThicknessDeltaStopCriteria: float = 0

    #: A Boolean specifying whether to exclude elements with boundary conditions from the
    #: optimization. The default value is OFF.
    freezeBoundaryConditionRegions: Boolean = OFF

    #: A Boolean specifying whether to exclude elements with loads and elements with loaded
    #: nodes from the optimization. The default value is ON.
    freezeLoadRegions: Boolean = ON

    #: The SymbolicConstatnt MODEL or a Region object specifying the region to use for mode
    #: tracking. The default value is MODEL.
    modeTrackingRegion: str = MODEL

    #: An Int specifying the number of stop criteria. The default value is 2.
    numFulfilledStopCriteria: int = 2

    #: An Int specifying the number of modes included in mode tracking. The default value is 5.
    numTrackedModes: int = 5

    #: A Float specifying the stop criteria based on the change in objective function. The
    #: default value is 0.001.
    objectiveFunctionDeltaStopCriteria: float = 0

    #: An Int specifying the first design cycle used to evaluate convergence criteria. The
    #: default value is 4.
    stopCriteriaDesignCycle: int = 4

    #: A Float specifying the maximum change in thickness per design cycle. The default value
    #: is 0.25.
    thicknessMoveLimit: float = 0

    #: A SymbolicConstant specifying the strategy for how the thickness is updated in the
    #: method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and AGGRESSIVE.
    #: The default value is NORMAL.
    thicknessUpdateStrategy: SymbolicConstant = NORMAL

    #: A Boolean specifying whether the group in the design response will be evaluated using
    #: the existing algorithm or a new algorithm based on Abaqus sensitivities. The default
    #: value of False means that the existing algorithm will be used.
    #:
    #: .. versionadded:: 2022
    #:     The `groupSensitivities` attribute was added.
    groupOperator: Boolean = OFF

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
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
        """This method creates a SizingTask object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].SizingTask

        Parameters
        ----------
        name
            A String specifying the optimization task repository key.
        abaqusSensitivities
            A Boolean specifying whether to use Abaqus to compute the design responses and their
            sensitivities. The default value is True.

            .. versionadded:: 2019
                The `abaqusSensitivities` argument was added.
        elementThicknessDeltaStopCriteria
            A Float specifying the stop criteria based on the change in element thickness. The
            default value is 0.5 × 10-2.
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

            .. versionadded:: 2022
                The `groupOperator` argument was added.

        Returns
        -------
        SizingTask
            A :py:class:`~abaqus.Optimization.SizingTask.SizingTask` object.
        """
        super().__init__()

    @abaqus_method_doc
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

            .. versionadded:: 2019
                The `abaqusSensitivities` argument was added.
        elementThicknessDeltaStopCriteria
            A Float specifying the stop criteria based on the change in element thickness. The
            default value is 0.5 × 10-2.
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

            .. versionadded:: 2022
                The `groupOperator` argument was added.
        """
        ...
