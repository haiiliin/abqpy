from __future__ import annotations

from typing import Optional

from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class StructuralDampingByFrequencyComponent:
    """A StructuralDampingByFrequencyComponent object is used to define structural damping over a range of
    frequencies.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].structuralDampingByFrequency.components[i]
    """

    #: A Float specifying the frequency value in cycles/time.
    frequency: Optional[float] = None

    #: A Float specifying the damping factor, s.
    factor: Optional[float] = None
