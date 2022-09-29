from typing import Optional, Union

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Movie import Movie
from ..Session.SessionBase import SessionBase
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class AnimationSession(SessionBase):
    """The following commands operate on Session objects. For more information about the
    Session object, see Session object.

    .. note:: 
        This object can be accessed by::

            import animation
    """

    @abaqus_method_doc
    def writeImageAnimation(
        self, fileName: str, format: SymbolicConstant, canvasObjects: tuple = ()
    ):
        """This method writes the animations present in the list of canvas objects to a file. It
        generates an animation file using the given file name and file format and uses the
        values in the appropriate options object.

        Parameters
        ----------
        fileName
            A String specifying the name of the animation file to generate.
        format
            A SymbolicConstant specifying the format of the generated file. Possible values are AVI,
            QUICKTIME, VRML, and COMPRESSED_VRML.
        canvasObjects
            A sequence specifying the canvas objects to capture. The default behavior is to capture
            all canvas objects.
        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def Movie(
        self,
        name: str,
        fileName: str,
        startFrame: int = 0,
        endFrame: Optional[int] = None,
        timelineStartFrame: int = 0,
        timelineEndFrame: Optional[int] = None,
        timelineStartTime: float = 0,
        timelineEndTime: Union[SymbolicConstant, float] = END_FRAME_TIME,
    ) -> Movie:
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
        ValueError: Unsupported movie format.
            If **fileName** references an unsupported movie file format
        ValueError: Unable to decode movie file
            If the contents of **fileName** are corrupt or can not be decoded.
        """
        self.movies[name] = movie = Movie(
            name,
            fileName,
            startFrame,
            endFrame,
            timelineStartFrame,
            timelineEndFrame,
            timelineStartTime,
            timelineEndTime,
        )
        return movie
