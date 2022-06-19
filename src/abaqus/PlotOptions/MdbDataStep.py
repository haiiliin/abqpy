from .MdbDataFrameArray import MdbDataFrameArray


class MdbDataStep:
    """The MdbDataStep object.It corresponds to same named step in the cae model.

    Attributes
    ----------
    frames: MdbDataFrameArray
        A :py:class:`~abaqus.PlotOptions.MdbDataFrameArray.MdbDataFrameArray` object specifying the list of frames. The list is read-only. There
        is only one frame in a step.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import visualization
        session.mdbData[name].steps[i]
    """

    # A MdbDataFrameArray object specifying the list of frames. The list is read-only. There
    # is only one frame in a step.
    frames: MdbDataFrameArray = MdbDataFrameArray()
