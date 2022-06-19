from .StructuralDampingComponentArray import StructuralDampingComponentArray


class StructuralDamping:
    """A StructuralDamping object contains structural damping parameters.

    Attributes
    ----------
    components: StructuralDampingComponentArray
        A :py:class:`~abaqus.StepMiscellaneous.StructuralDampingComponentArray.StructuralDampingComponentArray` object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import step
        mdb.models[name].steps[name].structuralDamping

    """

    # A StructuralDampingComponentArray object.
    components: StructuralDampingComponentArray = StructuralDampingComponentArray()
