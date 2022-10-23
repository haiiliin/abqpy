from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .StopCondition import StopCondition
from ..UtilityAndView.abaqusConstants import ADD, LESS_THAN, MAXIMUM, MODEL, MOVEMENT, PREVIOUS, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class LocalStopCondition(StopCondition):
    """The LocalStopCondition object defines a local stop condition.
    The LocalStopCondition object is derived from the StopCondition object.

    .. note::
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].stopConditions[name]
    """

    #: A String specifying the stop condition repository key.
    name: str

    #: A Float specifying the factor used to modify the reference value.
    referenceFactor: float

    #: A SymbolicConstant specifying the operation used to compare the selected value to the
    #: reference value. Possible values are LESS_THAN, LESS_THAN_EQUAL, EQUAL,
    #: GREATER_THAN_EQUAL, and GREATER_THAN. The default value is LESS_THAN.
    comparisonOperation: SymbolicConstant = LESS_THAN

    #: A SymbolicConstant specifying the variable identifier of the compared value. Possible
    #: values are:
    #:
    #: - ABSOLUTE_GROWTH_MOVEMENT
    #: - ABSOLUTE_SHRINK_MOVEMENT
    #: - GROWTH_MOVEMENT
    #: - SHRINK_MOVEMENT
    #: - MOVEMENT
    #: - TOTAL_ABSOLUTE_MOVEMENT
    #: - EQUIV_STRESS
    #: - FREE_TASK_REGION_EQUIV_STRESS
    #: - RESTRICTED_TASK_REGION_EQUIV_STRESS
    #: - SURFACE_POINT_EQUIV_STRESS
    #: - TASK_REGION_EQUIV_STRESS
    #:
    #: The default value is MOVEMENT.
    identifier: SymbolicConstant = MOVEMENT

    #: A SymbolicConstant specifying the operation used to evaluate values in the region.
    #: Possible values are MAXIMUM, MINIMUM, and SUM. The default value is MAXIMUM.
    identifierOperation: SymbolicConstant = MAXIMUM

    #: A SymbolicConstant specifying the iteration from which a value is compared to the
    #: reference value. Possible values are FIRST and PREVIOUS. The default value is PREVIOUS.
    referenceDesignCycle: SymbolicConstant = PREVIOUS

    #: A SymbolicConstant specifying the operation used to modify the reference value by the
    #: reference factor. Possible values are ADD, DIVIDE, MULTIPLY, and SUBTRACT. The default
    #: value is ADD.
    referenceOperation: SymbolicConstant = ADD

    #: The SymbolicConstant MODEL or a Region object specifying the region to which the stop
    #: condition is applied. The default value is MODEL.
    region: SymbolicConstant = MODEL

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        referenceFactor: float,
        comparisonOperation: Literal[
            C.EQUAL, C.GREATER_THAN_EQUAL, C.LESS_THAN_EQUAL, C.LESS_THAN, C.GREATER_THAN
        ] = LESS_THAN,
        identifier: Literal[
            C.TOTAL_ABSOLUTE_MOVEMENT,
            C.GROWTH_MOVEMENT,
            C.SURFACE_POINT_EQUIV_STRESS,
            C.ABSOLUTE_GROWTH_MOVEMENT,
            C.TASK_REGION_EQUIV_STRESS,
            C.SHRINK_MOVEMENT,
            C.RESTRICTED_TASK_REGION_EQUIV_STRESS,
            C.EQUIV_STRESS,
            C.MOVEMENT,
            C.FREE_TASK_REGION_EQUIV_STRESS,
            C.ABSOLUTE_SHRINK_MOVEMENT,
        ] = MOVEMENT,
        identifierOperation: Literal[C.SUM, C.MINIMUM, C.MAXIMUM] = MAXIMUM,
        referenceDesignCycle: Literal[C.PREVIOUS, C.FIRST] = PREVIOUS,
        referenceOperation: Literal[C.MULTIPLY, C.DIVIDE, C.SUBTRACT, C.ADD] = ADD,
        region: Literal[C.MODEL] = MODEL,
    ):
        """This method creates a LocalStopCondition object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].LocalStopCondition

        Parameters
        ----------
        name
            A String specifying the stop condition repository key.
        referenceFactor
            A Float specifying the factor used to modify the reference value.
        comparisonOperation
            A SymbolicConstant specifying the operation used to compare the selected value to the
            reference value. Possible values are LESS_THAN, LESS_THAN_EQUAL, EQUAL,
            GREATER_THAN_EQUAL, and GREATER_THAN. The default value is LESS_THAN.
        identifier
            A SymbolicConstant specifying the variable identifier of the compared value. Possible
            values are:
            - ABSOLUTE_GROWTH_MOVEMENT
            - ABSOLUTE_SHRINK_MOVEMENT
            - GROWTH_MOVEMENT
            - SHRINK_MOVEMENT
            - MOVEMENT
            - TOTAL_ABSOLUTE_MOVEMENT
            - EQUIV_STRESS
            - FREE_TASK_REGION_EQUIV_STRESS
            - RESTRICTED_TASK_REGION_EQUIV_STRESS
            - SURFACE_POINT_EQUIV_STRESS
            - TASK_REGION_EQUIV_STRESS

            The default value is MOVEMENT.
        identifierOperation
            A SymbolicConstant specifying the operation used to evaluate values in the region.
            Possible values are MAXIMUM, MINIMUM, and SUM. The default value is MAXIMUM.
        referenceDesignCycle
            A SymbolicConstant specifying the iteration from which a value is compared to the
            reference value. Possible values are FIRST and PREVIOUS. The default value is PREVIOUS.
        referenceOperation
            A SymbolicConstant specifying the operation used to modify the reference value by the
            reference factor. Possible values are ADD, DIVIDE, MULTIPLY, and SUBTRACT. The default
            value is ADD.
        region
            The SymbolicConstant MODEL or a Region object specifying the region to which the stop
            condition is applied. The default value is MODEL.

        Returns
        -------
        LocalStopCondition
            A :py:class:`~abaqus.Optimization.LocalStopCondition.LocalStopCondition` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        comparisonOperation: Literal[
            C.EQUAL, C.GREATER_THAN_EQUAL, C.LESS_THAN_EQUAL, C.LESS_THAN, C.GREATER_THAN
        ] = LESS_THAN,
        identifier: Literal[
            C.TOTAL_ABSOLUTE_MOVEMENT,
            C.GROWTH_MOVEMENT,
            C.SURFACE_POINT_EQUIV_STRESS,
            C.ABSOLUTE_GROWTH_MOVEMENT,
            C.TASK_REGION_EQUIV_STRESS,
            C.SHRINK_MOVEMENT,
            C.RESTRICTED_TASK_REGION_EQUIV_STRESS,
            C.EQUIV_STRESS,
            C.MOVEMENT,
            C.FREE_TASK_REGION_EQUIV_STRESS,
            C.ABSOLUTE_SHRINK_MOVEMENT,
        ] = MOVEMENT,
        identifierOperation: Literal[C.SUM, C.MINIMUM, C.MAXIMUM] = MAXIMUM,
        referenceDesignCycle: Literal[C.PREVIOUS, C.FIRST] = PREVIOUS,
        referenceOperation: Literal[C.MULTIPLY, C.DIVIDE, C.SUBTRACT, C.ADD] = ADD,
        region: Literal[C.MODEL] = MODEL,
    ):
        """This method modifies the LocalStopCondition object.

        Parameters
        ----------
        comparisonOperation
            A SymbolicConstant specifying the operation used to compare the selected value to the
            reference value. Possible values are LESS_THAN, LESS_THAN_EQUAL, EQUAL,
            GREATER_THAN_EQUAL, and GREATER_THAN. The default value is LESS_THAN.
        identifier
            A SymbolicConstant specifying the variable identifier of the compared value. Possible
            values are:
            - ABSOLUTE_GROWTH_MOVEMENT
            - ABSOLUTE_SHRINK_MOVEMENT
            - GROWTH_MOVEMENT
            - SHRINK_MOVEMENT
            - MOVEMENT
            - TOTAL_ABSOLUTE_MOVEMENT
            - EQUIV_STRESS
            - FREE_TASK_REGION_EQUIV_STRESS
            - RESTRICTED_TASK_REGION_EQUIV_STRESS
            - SURFACE_POINT_EQUIV_STRESS
            - TASK_REGION_EQUIV_STRESS

            The default value is MOVEMENT.
        identifierOperation
            A SymbolicConstant specifying the operation used to evaluate values in the region.
            Possible values are MAXIMUM, MINIMUM, and SUM. The default value is MAXIMUM.
        referenceDesignCycle
            A SymbolicConstant specifying the iteration from which a value is compared to the
            reference value. Possible values are FIRST and PREVIOUS. The default value is PREVIOUS.
        referenceOperation
            A SymbolicConstant specifying the operation used to modify the reference value by the
            reference factor. Possible values are ADD, DIVIDE, MULTIPLY, and SUBTRACT. The default
            value is ADD.
        region
            The SymbolicConstant MODEL or a Region object specifying the region to which the stop
            condition is applied. The default value is MODEL.
        """
        ...
