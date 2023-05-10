from typing import Dict

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import (
    MODEL,
    NORMAL,
    OFF,
    ON,
    Boolean,
    SymbolicConstant,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .DesignResponse import DesignResponse
from .GeometricRestriction import GeometricRestriction
from .ObjectiveFunction import ObjectiveFunction
from .OptimizationConstraint import OptimizationConstraint
from .OptimizationTask import OptimizationTask
from .StopCondition import StopCondition


@abaqus_class_doc
class SizingTask(OptimizationTask):
    """The SizingTask object defines a Sizing task. The SizingTask object is derived from the OptimizationTask
    object.

    .. note::
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name]
    """

    #: A repository of DesignResponse objects.
    designResponses: Dict[str, DesignResponse] = {}

    #: A repository of ObjectiveFunction objects.
    objectiveFunctions: Dict[str, ObjectiveFunction] = {}

    #: A repository of OptimizationConstraint objects.
    optimizationConstraints: Dict[str, OptimizationConstraint] = {}

    #: A repository of GeometricRestriction objects.
    geometricRestrictions: Dict[str, GeometricRestriction] = {}

    #: A repository of StopCondition objects.
    stopConditions: Dict[str, StopCondition] = {}

    #: A String specifying the optimization task repository key.
    name: str

    #: A Float specifying the stop criteria based on the change in element thickness. The
    #: default value is 0.5 x 10⁻².
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

    @abaqus_method_doc
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
        thicknessUpdateStrategy: Literal[C.AGGRESSIVE, C.NORMAL, C.CONSERVATIVE] = NORMAL,
    ):
        """This method creates a SizingTask object.

        .. note::
            This function can be accessed by::

                mdb.models[name].SizingTask

        Parameters
        ----------
        name
            A String specifying the optimization task repository key.
        elementThicknessDeltaStopCriteria
            A Float specifying the stop criteria based on the change in element thickness. The
            default value is 0.5 x 10⁻².
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

        Returns
        -------
        SizingTask
            A SizingTask object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        elementThicknessDeltaStopCriteria: float = 0,
        freezeBoundaryConditionRegions: Boolean = OFF,
        freezeLoadRegions: Boolean = ON,
        modeTrackingRegion: str = MODEL,
        numFulfilledStopCriteria: int = 2,
        numTrackedModes: int = 5,
        objectiveFunctionDeltaStopCriteria: float = 0,
        stopCriteriaDesignCycle: int = 4,
        thicknessMoveLimit: float = 0,
        thicknessUpdateStrategy: Literal[C.AGGRESSIVE, C.NORMAL, C.CONSERVATIVE] = NORMAL,
    ):
        """This method modifies the SizingTask object.

        Parameters
        ----------
        elementThicknessDeltaStopCriteria
            A Float specifying the stop criteria based on the change in element thickness. The
            default value is 0.5 x 10⁻².
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
        """
        ...
