import typing

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import *
from .._OptionsBase import _OptionsBase


@abaqus_class_doc
class Movie(_OptionsBase):
    """The Movie object is used to store values and attributes associated with a movie file.
    Upon creation, the Movie object is added to the session.movies repository.

    .. note:: 
        This object can be accessed by::

            import animation
            session.movies[name]
    """

    #: An Int specifying the width of the movie in pixels.
    width: typing.Optional[int] = None

    #: An Int specifying the height of the movie in pixels.
    height: typing.Optional[int] = None

    #: An Int specifying the total number of frames on the movie file.
    numFrames: typing.Optional[int] = None

    #: A Float specifying the duration of the movie in seconds.
    duration: typing.Optional[float] = None

    #: An Int specifying the memory taken by the movie frames as selected.
    memory: typing.Optional[int] = None

    #: A String specifying the repository name for the movie.
    name: str

    #: A String specifying the file from which the movie is to be read. The file extension must
    #: be specified and indicates the movie format (.avi, .mov, .mpeg, or .wmv).
    fileName: str

    #: An Int specifying the first frame to be displayed from this movie. The default value is
    #: 0.
    startFrame: int = 0

    #: An Int specifying the last frame to be displayed from this movie. A negative number will
    #: indicate reverse numbering: -1 is the last frame of the movie. The default value is −1.
    endFrame: typing.Optional[int] = None

    #: An Int specifying the global timeline frame number that corresponds to **startFrame**. A
    #: value of 0 will indicate the first frame to be displayed in the viewport. The default
    #: value is 0.
    timelineStartFrame: int = 0

    #: An Int specifying the global timeline frame number that corresponds to **endFrame**. A
    #: negative number will indicate reverse numbering: -1 indicates the last frame to be
    #: displayed in the viewport. The default value is −1.
    timelineEndFrame: typing.Optional[int] = None

    #: A Float specifying the global timeline time that corresponds to the time of
    #: **startFrame**. The default value is 0.0.
    timelineStartTime: float = 0

    #: The SymbolicConstant END_FRAME_TIME or a Float specifying the global timeline time that
    #: corresponds to the time of **endFrame**. The SymbolicConstant END_FRAME_TIME indicates the
    #: time in this movie corresponding to **endFrame**. The default value is END_FRAME_TIME.
    timelineEndTime: typing.Union[SymbolicConstant, float] = END_FRAME_TIME

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        fileName: str,
        startFrame: int = 0,
        endFrame: typing.Optional[int] = None,
        timelineStartFrame: int = 0,
        timelineEndFrame: typing.Optional[int] = None,
        timelineStartTime: float = 0,
        timelineEndTime: typing.Union[SymbolicConstant, float] = END_FRAME_TIME,
    ):
        """This method creates a Movie object from the contents of the specified file.

        .. note:: 
            This function can be accessed by::

                session.Movie

        Parameters
        ----------
        name
            A String specifying the repository name for the movie.
        fileName
            A String specifying the file from which the movie is to be read. The file extension must
            be specified and indicates the movie format (.avi, .mov, .mpeg, or .wmv).
        startFrame
            An Int specifying the first frame to be displayed from this movie. The default value is
            0.
        endFrame
            An Int specifying the last frame to be displayed from this movie. A negative number will
            indicate reverse numbering: -1 is the last frame of the movie. The default value is −1.
        timelineStartFrame
            An Int specifying the global timeline frame number that corresponds to **startFrame**. A
            value of 0 will indicate the first frame to be displayed in the viewport. The default
            value is 0.
        timelineEndFrame
            An Int specifying the global timeline frame number that corresponds to **endFrame**. A
            negative number will indicate reverse numbering: -1 indicates the last frame to be
            displayed in the viewport. The default value is −1.
        timelineStartTime
            A Float specifying the global timeline time that corresponds to the time of
            **startFrame**. The default value is 0.0.
        timelineEndTime
            The SymbolicConstant END_FRAME_TIME or a Float specifying the global timeline time that
            corresponds to the time of **endFrame**. The SymbolicConstant END_FRAME_TIME indicates the
            time in this movie corresponding to **endFrame**. The default value is END_FRAME_TIME.

        Returns
        -------
        Movie
            A :py:class:`~abaqus.Animation.Movie.Movie` object.

        Raises
        ------
        ValueError: Unable to open movie file
            If **fileName** does not exist or can not be read.
        ValueError: Unsupported movie format
            If **fileName** references an unsupported movie file format.
        ValueError: Unable to decode movie file
            If the contents of **fileName** are corrupt or can not be decoded.
        """
        self.name = name
        self.fileName = fileName
        self.startFrame = startFrame
        self.endFrame = endFrame
        self.timelineStartFrame = timelineStartFrame
        self.timelineEndFrame = timelineEndFrame
        self.timelineStartTime = timelineStartTime
        self.timelineEndTime = timelineEndTime

    @abaqus_method_doc
    def setValues(
        self,
        startFrame: int = 0,
        endFrame: typing.Optional[int] = None,
        timelineStartFrame: int = 0,
        timelineEndFrame: typing.Optional[int] = None,
        timelineStartTime: float = 0,
        timelineEndTime: typing.Union[SymbolicConstant, float] = END_FRAME_TIME,
    ):
        """This method modifies the Movie object.

        Parameters
        ----------
        startFrame
            An Int specifying the first frame to be displayed from this movie. The default value is
            0.
        endFrame
            An Int specifying the last frame to be displayed from this movie. A negative number will
            indicate reverse numbering: -1 is the last frame of the movie. The default value is −1.
        timelineStartFrame
            An Int specifying the global timeline frame number that corresponds to **startFrame**. A
            value of 0 will indicate the first frame to be displayed in the viewport. The default
            value is 0.
        timelineEndFrame
            An Int specifying the global timeline frame number that corresponds to **endFrame**. A
            negative number will indicate reverse numbering: -1 indicates the last frame to be
            displayed in the viewport. The default value is −1.
        timelineStartTime
            A Float specifying the global timeline time that corresponds to the time of
            **startFrame**. The default value is 0.0.
        timelineEndTime
            The SymbolicConstant END_FRAME_TIME or a Float specifying the global timeline time that
            corresponds to the time of **endFrame**. The SymbolicConstant END_FRAME_TIME indicates the
            time in this movie corresponding to **endFrame**. The default value is END_FRAME_TIME.

        Raises
        ------
        RangeError: startFrame must be an Integer in the range: 0 to numFrames-1
            If **startFrame**,*endFrame*,*timelineStartFrame*,*timelineEndFrame*,*timelineStartTime*,
            or*timelineEndTime* are outside their respective valid range.
        """
        super().setValues(
            startFrame=startFrame,
            endFrame=endFrame,
            timelineStartFrame=timelineStartFrame,
            timelineEndFrame=timelineEndFrame,
            timelineStartTime=timelineStartTime,
            timelineEndTime=timelineEndTime,
        )
