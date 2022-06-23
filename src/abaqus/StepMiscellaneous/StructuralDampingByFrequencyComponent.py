class StructuralDampingByFrequencyComponent:
    """A :py:class:`~abaqus.StepMiscellaneous.StructuralDampingByFrequencyComponent.StructuralDampingByFrequencyComponent` object is used to define structural damping over
    a range of frequencies.

    Attributes
    ----------
    frequency: float
        A Float specifying the frequency value in cycles/time.
    factor: float
        A Float specifying the damping factor, s.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import step
        mdb.models[name].steps[name].structuralDampingByFrequency.components[i]
    """

    #: A Float specifying the frequency value in cycles/time.
    frequency: float = None

    #: A Float specifying the damping factor, s.
    factor: float = None
