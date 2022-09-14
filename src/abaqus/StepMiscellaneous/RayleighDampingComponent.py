from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class RayleighDampingComponent:
    """A :py:class:`~abaqus.StepMiscellaneous.RayleighDampingComponent.RayleighDampingComponent` object is used to define Rayleigh damping over a range of
    modes.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].rayleighDamping.components[i]
    """

    #: An Int specifying the mode number of the lowest mode of a range.
    start: int = None

    #: An Int specifying the mode number of the highest mode of a range.
    end: int = None

    #: A Float specifying the mass proportional damping, αM.
    alpha: float = None

    #: A Float specifying the stiffness proportional damping, βM.
    beta: float = None
