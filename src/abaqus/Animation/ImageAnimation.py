from abaqusConstants import *


class ImageAnimation:
    """The ImageAnimation object is used to build frame by frame animation.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import animation
            session.imageAnimation
    """

    #: A String specifying the file to which the animation frames is to be written.
    fileName: str = ""

    def __init__(self, fileName: str, format: SymbolicConstant):
        """This method creates an ImageAnimation object from the specified filename and format.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                session.ImageAnimation

        Parameters
        ----------
        fileName
            A String specifying the name of the animation file to generate.
        format
            A SymbolicConstant specifying the format of the generated file. Possible values are AVI,
            QUICKTIME.

        Returns
        -------
        ImageAnimation
            An :py:class:`~abaqus.Animation.ImageAnimation.ImageAnimation` object.
        """
        pass

    def writeFrame(self, canvasObjects: tuple = ()):
        """This method adds a frame to the ImageAnimation object.

        Parameters
        ----------
        canvasObjects
            A sequence specifying the canvas objects to capture. The default is to capture all
            canvas objects.
        """
        pass

    def close(self):
        """This method closes the ImageAnimation object."""
        pass

    def closed(self):
        """This method indicates if the ImageAnimation is open or closed for writing animation
        frames.
        """
        pass
