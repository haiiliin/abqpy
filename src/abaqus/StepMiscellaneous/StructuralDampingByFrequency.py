from .StructuralDampingByFrequencyComponentArray import (
    StructuralDampingByFrequencyComponentArray,
)


class StructuralDampingByFrequency:
    """A :py:class:`~abaqus.StepMiscellaneous.StructuralDampingByFrequency.StructuralDampingByFrequency` object contains structural damping parameters.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import step
            mdb.models[name].steps[name].structuralDampingByFrequency
    """

    #: A :py:class:`~abaqus.StepMiscellaneous.StructuralDampingByFrequencyComponentArray.StructuralDampingByFrequencyComponentArray` object.
    components: StructuralDampingByFrequencyComponentArray = (
        StructuralDampingByFrequencyComponentArray()
    )
