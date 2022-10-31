from abqpy.decorators import abaqus_class_doc

from .DirectDampingByFrequencyComponentArray import (
    DirectDampingByFrequencyComponentArray,
)


@abaqus_class_doc
class DirectDampingByFrequency:
    """A DirectDampingByFrequency object contains direct damping parameters.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].directDampingByFrequency
    """

    #: A DirectDampingByFrequencyComponentArray object.
    components: DirectDampingByFrequencyComponentArray = []
