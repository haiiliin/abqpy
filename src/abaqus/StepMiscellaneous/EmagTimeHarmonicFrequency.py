class EmagTimeHarmonicFrequency:
    """

    Attributes
    ----------
    lower: float
        A Float specifying the lower limit of frequency range or a single frequency, in
        cycles/time.
    upper: float
        A Float specifying the upper limit of frequency range, in cycles/time.
    nPoints: int
        An Int specifying the number of points in the frequency range at which results should be
        given.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import step
        mdb.models[name].steps[name].frequencyRange[i]
    """

    #: A Float specifying the lower limit of frequency range or a single frequency, in
    #: cycles/time.
    lower: float = None

    #: A Float specifying the upper limit of frequency range, in cycles/time.
    upper: float = None

    #: An Int specifying the number of points in the frequency range at which results should be
    #: given.
    nPoints: int = None
