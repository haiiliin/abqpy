from .RayleighDampingComponentArray import RayleighDampingComponentArray
from .._decorators import abaqus_class_doc


@abaqus_class_doc
class RayleighDamping:
    """A :py:class:`~abaqus.StepMiscellaneous.RayleighDamping.RayleighDamping` object contains Rayleigh Damping parameters.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import step
            mdb.models[name].steps[name].rayleighDamping
    """

    #: A :py:class:`~abaqus.StepMiscellaneous.RayleighDampingComponentArray.RayleighDampingComponentArray` object.
    components: RayleighDampingComponentArray = []
