from .CompositeDampingComponentArray import CompositeDampingComponentArray


class CompositeDamping:
    """A :py:class:`~abaqus.StepMiscellaneous.CompositeDamping.CompositeDamping` object contains composite modal damping parameters.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import step
            mdb.models[name].steps[name].compositeDamping
    """

    #: A :py:class:`~abaqus.StepMiscellaneous.CompositeDampingComponentArray.CompositeDampingComponentArray` object.
    components: CompositeDampingComponentArray = CompositeDampingComponentArray()
