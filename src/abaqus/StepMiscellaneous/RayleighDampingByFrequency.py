from .RayleighDampingByFrequencyComponentArray import (
    RayleighDampingByFrequencyComponentArray,
)


class RayleighDampingByFrequency:
    """A :py:class:`~abaqus.StepMiscellaneous.RayleighDampingByFrequency.RayleighDampingByFrequency` object contains Rayleigh Damping parameters.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import step
            mdb.models[name].steps[name].rayleighDampingByFrequency
    """

    #: A :py:class:`~abaqus.StepMiscellaneous.RayleighDampingByFrequencyComponentArray.RayleighDampingByFrequencyComponentArray` object.
    components: RayleighDampingByFrequencyComponentArray = (
        RayleighDampingByFrequencyComponentArray()
    )
