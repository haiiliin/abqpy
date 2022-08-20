from .MdbDataFrameArray import MdbDataFrameArray
from .._decorators import abaqus_class_doc


@abaqus_class_doc
class MdbDataStep:
    """The MdbDataStep object.It corresponds to same named step in the cae model.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import visualization
            session.mdbData[name].steps[i]
    """

    #: A :py:class:`~abaqus.PlotOptions.MdbDataFrameArray.MdbDataFrameArray` object specifying the list of frames.
    #: The list is read-only. There
    #: is only one frame in a step.
    frames: MdbDataFrameArray = []
