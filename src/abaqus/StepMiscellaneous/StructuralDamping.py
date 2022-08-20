from .StructuralDampingComponentArray import StructuralDampingComponentArray
from .._decorators import abaqus_class_doc


@abaqus_class_doc
class StructuralDamping:
    """A :py:class:`~abaqus.StepMiscellaneous.StructuralDamping.StructuralDamping` object contains structural damping parameters.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import step
            mdb.models[name].steps[name].structuralDamping
    """

    #: A :py:class:`~abaqus.StepMiscellaneous.StructuralDampingComponentArray.StructuralDampingComponentArray` object.
    components: StructuralDampingComponentArray = []
