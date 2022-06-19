from .StructuralDampingByFrequencyComponentArray import (
    StructuralDampingByFrequencyComponentArray,
)


class StructuralDampingByFrequency:
    """A StructuralDampingByFrequency object contains structural damping parameters.

    Attributes
    ----------
    components: StructuralDampingByFrequencyComponentArray
        A :py:class:`~abaqus.StepMiscellaneous.StructuralDampingByFrequencyComponentArray.StructuralDampingByFrequencyComponentArray` object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import step
        mdb.models[name].steps[name].structuralDampingByFrequency

    """

    # A StructuralDampingByFrequencyComponentArray object.
    components: StructuralDampingByFrequencyComponentArray = (
        StructuralDampingByFrequencyComponentArray()
    )
