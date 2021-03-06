class RayleighDampingByFrequencyComponent:
    """A :py:class:`~abaqus.StepMiscellaneous.RayleighDampingByFrequencyComponent.RayleighDampingByFrequencyComponent` object is used to define Rayleigh damping over a
    range of frequencies.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import step
            mdb.models[name].steps[name].rayleighDampingByFrequency.components[i]
    """

    #: A Float specifying the frequency value in cycles/time.
    frequency: float = None

    #: A Float specifying the mass proportional damping, αM.
    alpha: float = None

    #: A Float specifying the stiffness proportional damping, βM.
    beta: float = None
