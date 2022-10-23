from abqpy.decorators import abaqus_class_doc

from ..Adaptivity.AdaptivityStep import AdaptivityStep
from ..StepOutput.OutputStep import OutputStep
from ..TableCollection.TableCollectionStep import TableCollectionStep


@abaqus_class_doc
class Step(AdaptivityStep, OutputStep, TableCollectionStep):
    """The Step object stores the parameters that determine the context of the step. The Step
    object is the abstract base type for other Step objects. The Step object has no explicit
    constructor. The methods and members of the Step object are common to all objects
    derived from the Step.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name]
    """

    ...
