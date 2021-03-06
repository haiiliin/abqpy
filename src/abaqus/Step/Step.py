from ..Adaptivity.AdaptivityStep import AdaptivityStep
from ..StepOutput.OutputStep import OutputStep


class Step(AdaptivityStep, OutputStep):
    """The Step object stores the parameters that determine the context of the step. The Step
    object is the abstract base type for other Step objects. The Step object has no explicit
    constructor. The methods and members of the Step object are common to all objects
    derived from the Step.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import step
            mdb.models[name].steps[name]
    """
    pass
