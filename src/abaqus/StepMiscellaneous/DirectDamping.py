from .DirectDampingComponentArray import DirectDampingComponentArray
from .._decorators import abaqus_class_doc


@abaqus_class_doc
class DirectDamping:
    """A :py:class:`~abaqus.StepMiscellaneous.DirectDamping.DirectDamping` object contains direct modal damping parameters.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import step
            mdb.models[name].steps[name].directDamping
    """

    #: A :py:class:`~abaqus.StepMiscellaneous.DirectDampingComponentArray.DirectDampingComponentArray` object.
    components: DirectDampingComponentArray = []
