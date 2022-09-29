from typing import Optional

from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class SteadyStateModalFrequency:
    """A SteadyStateModalFrequency is an object used to define frequency over a range of modes.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].frequencyRange[i]
    """

    #: A Float specifying the lower limit of frequency range or a single frequency, in
    #: cycles/time.
    lower: Optional[float] = None

    #: A Float specifying the upper limit of frequency range, in cycles/time.
    upper: Optional[float] = None

    #: An Int specifying the number of points in the frequency range at which results should be
    #: given.
    nPoints: Optional[int] = None

    #: A Float specifying the bias parameter. When results are requested at four or more
    #: frequency points, Abaqus biases the results toward the ends of the intervals to obtain
    #: better resolution. The default value is 3.0.
    bias: float = 3
