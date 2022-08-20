from .DirectDampingByFrequencyComponentArray import (
    DirectDampingByFrequencyComponentArray,
)
from .._decorators import abaqus_class_doc


@abaqus_class_doc
class DirectDampingByFrequency:
    """A :py:class:`~abaqus.StepMiscellaneous.DirectDampingByFrequency.DirectDampingByFrequency` object contains direct damping parameters.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import step
            mdb.models[name].steps[name].directDampingByFrequency
    """

    #: A :py:class:`~abaqus.StepMiscellaneous.DirectDampingByFrequencyComponentArray.DirectDampingByFrequencyComponentArray` object.
    components: DirectDampingByFrequencyComponentArray = []
