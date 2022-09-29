import typing
from abqpy.decorators import abaqus_class_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class HistoryVariable:
    """The HistoryVariable object stores history data.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.odbData[name].historyVariables[i]
    """

    #: A String specifying the history request label. This String is read-only.
    name: str = ""

    #: A String specifying the legend text. This String is read-only.
    legendLabel: str = ""

    #: A tuple of (String, Int, SymbolicConstant) tuples specifying the steps. This sequence is
    #: read-only. Each inner sequence contains the following elements:*stepLabel*: A String
    #: specifying the step label. *stepNumber*: An Int specifying the step
    #: number. *procedureDomain*: A SymbolicConstant specifying the analysis type of the step,
    #: which can have these values: “TIME,” “FREQUENCY,” or “MODAL.”
    steps: typing.Optional[SymbolicConstant] = None
