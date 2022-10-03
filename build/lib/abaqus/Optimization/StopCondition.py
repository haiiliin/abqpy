from abqpy.decorators import abaqus_class_doc
from ..UtilityAndView.abaqusConstants import MODEL, SymbolicConstant


@abaqus_class_doc
class StopCondition:
    """The StopCondition object is the abstract base type for other StopCondition objects. The
    StopCondition object has no explicit constructor. The methods and members of the
    StopCondition object are common to all objects derived from StopCondition.

    .. note:: 
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].stopConditions[name]
    """

    #: A String specifying the stop condition repository key.
    name: str = ""

    #: The SymbolicConstant MODEL or a Region object specifying the region to which the stop
    #: condition is applied. The default value is MODEL.
    region: SymbolicConstant = MODEL
