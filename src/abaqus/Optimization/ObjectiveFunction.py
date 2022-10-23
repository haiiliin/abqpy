from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .OptimizationObjectiveArray import OptimizationObjectiveArray
from ..UtilityAndView.abaqusConstants import MINIMIZE, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class ObjectiveFunction:
    """The ObjectiveFunction object defines the objective of the optimization.

    .. note:: 
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].objectiveFunctions[name]
    """

    #: Optimization objectives
    objectives: OptimizationObjectiveArray = []

    #: A String specifying the objective function repository key.
    name: str

    #: An :py:class:`~abaqus.Optimization.OptimizationObjectiveArray.OptimizationObjectiveArray` object.
    objectives: OptimizationObjectiveArray

    #: A SymbolicConstant specifying the target of the objective function. Possible values are
    #: MINIMIZE, MAXIMIZE, and MINIMIZE_MAXIMUM. The default value is MINIMIZE.
    target: SymbolicConstant = MINIMIZE

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        objectives: OptimizationObjectiveArray,
        target: Literal[C.MINIMIZE_MAXIMUM, C.MINIMIZE, C.MAXIMIZE] = MINIMIZE,
    ):
        """This method creates an ObjectiveFunction object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].ObjectiveFunction

        Parameters
        ----------
        name
            A String specifying the objective function repository key.
        objectives
            An :py:class:`~abaqus.Optimization.OptimizationObjectiveArray.OptimizationObjectiveArray` object.
        target
            A SymbolicConstant specifying the target of the objective function. Possible values are
            MINIMIZE, MAXIMIZE, and MINIMIZE_MAXIMUM. The default value is MINIMIZE.

        Returns
        -------
        ObjectiveFunction
            An :py:class:`~abaqus.Optimization.ObjectiveFunction.ObjectiveFunction` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, target: Literal[C.MINIMIZE_MAXIMUM, C.MINIMIZE, C.MAXIMIZE] = MINIMIZE):
        """This method modifies the ObjectiveFunction object.

        Parameters
        ----------
        target
            A SymbolicConstant specifying the target of the objective function. Possible values are
            MINIMIZE, MAXIMIZE, and MINIMIZE_MAXIMUM. The default value is MINIMIZE.

        Raises
        ------
        RangeError
        """
        ...
