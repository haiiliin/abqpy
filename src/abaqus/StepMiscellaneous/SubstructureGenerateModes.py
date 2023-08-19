from __future__ import annotations

from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class SubstructureGenerateModes:
    """A SubstructureGenerateModes object is used to define the modes to be used in a modal dynamic analysis.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].modeRange[i]
    """

    #: An Int specifying the mode number of the lowest mode of a range.
    start: int | None = None

    #: An Int specifying the mode number of the highest mode of a range.
    end: int | None = None

    #: An Int specifying the increment used to define the intermediate mode numbers beginning
    #: from the lowest mode to the highest mode.
    increment: int | None = None
