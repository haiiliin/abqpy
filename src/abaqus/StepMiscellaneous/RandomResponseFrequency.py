from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class RandomResponseFrequency:
    """A RandomResponseFrequency is an object used to define frequency over a range of modes.
    This page discusses:

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].freq[i]
    """

    #: A Float specifying the lower limit of the frequency range in cycles per time.
    lower: float = None

    #: A Float specifying the upper limit of the frequency range in cycles per time.
    upper: float = None

    #: An Int specifying the number of points between eigenfrequencies at which the response
    #: should be calculated.
    nCalcs: int = None

    #: A Float specifying the bias parameter.
    bias: float = None
