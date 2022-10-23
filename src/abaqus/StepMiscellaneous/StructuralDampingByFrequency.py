from abqpy.decorators import abaqus_class_doc

from .StructuralDampingByFrequencyComponentArray import (
    StructuralDampingByFrequencyComponentArray,
)


@abaqus_class_doc
class StructuralDampingByFrequency:
    """A :py:class:`~abaqus.StepMiscellaneous.StructuralDampingByFrequency.StructuralDampingByFrequency` object contains structural damping parameters.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].structuralDampingByFrequency
    """

    #: A :py:class:`~abaqus.StepMiscellaneous.StructuralDampingByFrequencyComponentArray.StructuralDampingByFrequencyComponentArray` object.
    components: StructuralDampingByFrequencyComponentArray = []
