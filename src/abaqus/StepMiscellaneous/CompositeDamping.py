from abqpy.decorators import abaqus_class_doc

from .CompositeDampingComponentArray import CompositeDampingComponentArray


@abaqus_class_doc
class CompositeDamping:
    """A :py:class:`~abaqus.StepMiscellaneous.CompositeDamping.CompositeDamping` object contains composite modal damping parameters.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].compositeDamping
    """

    #: A :py:class:`~abaqus.StepMiscellaneous.CompositeDampingComponentArray.CompositeDampingComponentArray` object.
    components: CompositeDampingComponentArray = []
