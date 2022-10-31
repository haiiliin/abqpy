from abqpy.decorators import abaqus_class_doc

from .RayleighDampingByFrequencyComponentArray import (
    RayleighDampingByFrequencyComponentArray,
)


@abaqus_class_doc
class RayleighDampingByFrequency:
    """A RayleighDampingByFrequency object contains Rayleigh Damping parameters.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].rayleighDampingByFrequency
    """

    #: A RayleighDampingByFrequencyComponentArray object.
    components: RayleighDampingByFrequencyComponentArray = []
