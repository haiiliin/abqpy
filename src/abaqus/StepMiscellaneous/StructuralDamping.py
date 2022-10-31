from abqpy.decorators import abaqus_class_doc

from .StructuralDampingComponentArray import StructuralDampingComponentArray


@abaqus_class_doc
class StructuralDamping:
    """A StructuralDamping object contains structural damping parameters.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].structuralDamping
    """

    #: A StructuralDampingComponentArray object.
    components: StructuralDampingComponentArray = []
