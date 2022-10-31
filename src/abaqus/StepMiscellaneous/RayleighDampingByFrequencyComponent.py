from typing import Optional

from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class RayleighDampingByFrequencyComponent:
    """A RayleighDampingByFrequencyComponent object is used to define Rayleigh damping over a
    range of frequencies.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].rayleighDampingByFrequency.components[i]
    """

    #: A Float specifying the frequency value in cycles/time.
    frequency: Optional[float] = None

    #: A Float specifying the mass proportional damping, αM.
    alpha: Optional[float] = None

    #: A Float specifying the stiffness proportional damping, βM.
    beta: Optional[float] = None
