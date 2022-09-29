from typing import Union

from abqpy.decorators import abaqus_class_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class OptimizationObjective:
    """An OptimizationObjective is an object used to define objectives in an objective
    function.

    .. note:: 
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].objectiveFunctions[name].objectives[i]
    """

    #: A Boolean specifying whether the objective is suppressed or not. The default value is
    #: OFF.
    suppress: Boolean = OFF

    #: A Float specifying the weight applied to the design response value. The default value is
    #: 1.0.
    weight: float = 1

    #: The SymbolicConstant DEFAULT or a Float specifying the reference value used in
    #: evaluating a design response. For topology optimization, DEFAULT> indicates the
    #: reference value is 0. For shape optimization, DEFAULT indicates the reference value is
    #: the nodal average. The default value is DEFAULT.
    referenceValue: Union[SymbolicConstant, float] = DEFAULT

    #: A String specifying the name of the design response.
    designResponse: str = ""
