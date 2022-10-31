from abqpy.decorators import abaqus_class_doc

from .DirectDampingComponentArray import DirectDampingComponentArray


@abaqus_class_doc
class DirectDamping:
    """A DirectDamping object contains direct modal damping parameters.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].directDamping
    """

    #: A DirectDampingComponentArray object.
    components: DirectDampingComponentArray = []
