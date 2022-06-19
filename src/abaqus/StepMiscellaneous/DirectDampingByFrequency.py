from .DirectDampingByFrequencyComponentArray import (
    DirectDampingByFrequencyComponentArray,
)


class DirectDampingByFrequency:
    """A DirectDampingByFrequency object contains direct damping parameters.

    Attributes
    ----------
    components: DirectDampingByFrequencyComponentArray
        A :py:class:`~abaqus.StepMiscellaneous.DirectDampingByFrequencyComponentArray.DirectDampingByFrequencyComponentArray` object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import step
        mdb.models[name].steps[name].directDampingByFrequency
    """

    # A DirectDampingByFrequencyComponentArray object.
    components: DirectDampingByFrequencyComponentArray = (
        DirectDampingByFrequencyComponentArray()
    )
