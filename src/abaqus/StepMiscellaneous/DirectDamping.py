from .DirectDampingComponentArray import DirectDampingComponentArray


class DirectDamping:
    """A DirectDamping object contains direct modal damping parameters.

    Attributes
    ----------
    components: DirectDampingComponentArray
        A :py:class:`~abaqus.StepMiscellaneous.DirectDampingComponentArray.DirectDampingComponentArray` object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import step
        mdb.models[name].steps[name].directDamping

    """

    # A DirectDampingComponentArray object.
    components: DirectDampingComponentArray = DirectDampingComponentArray()
