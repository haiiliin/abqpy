from __future__ import annotations

from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class DirectDampingByFrequencyComponent:
    """A DirectDampingByFrequencyComponent object is used to define direct damping over a range of frequencies.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].directDampingByFrequency.components[i]
    """

    #: A Float specifying the frequency value in cycles/time.
    frequency: float | None = None

    #: A Float specifying the fraction of critical damping.
    fraction: float | None = None
