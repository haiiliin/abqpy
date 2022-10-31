from abqpy.decorators import abaqus_class_doc

from .RayleighDampingComponentArray import RayleighDampingComponentArray


@abaqus_class_doc
class RayleighDamping:
    """A RayleighDamping object contains Rayleigh Damping parameters.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].rayleighDamping
    """

    #: A RayleighDampingComponentArray object.
    components: RayleighDampingComponentArray = []
