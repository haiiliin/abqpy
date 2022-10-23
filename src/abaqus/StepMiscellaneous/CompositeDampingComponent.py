from typing import Optional

from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class CompositeDampingComponent:
    """A :py:class:`~abaqus.StepMiscellaneous.CompositeDampingComponent.CompositeDampingComponent` object is used to define composite damping over a range of
    modes.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].compositeDamping.components[i]
    """

    #: An Int specifying the mode number of the lowest mode of a range.
    start: Optional[int] = None

    #: An Int specifying the mode number of the highest mode of a range.
    end: Optional[int] = None
