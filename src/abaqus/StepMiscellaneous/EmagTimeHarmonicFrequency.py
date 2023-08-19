from __future__ import annotations

from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class EmagTimeHarmonicFrequency:
    """

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].frequencyRange[i]
    """

    #: A Float specifying the lower limit of frequency range or a single frequency, in
    #: cycles/time.
    lower: float | None = None

    #: A Float specifying the upper limit of frequency range, in cycles/time.
    upper: float | None = None

    #: An Int specifying the number of points in the frequency range at which results should be
    #: given.
    nPoints: int | None = None
