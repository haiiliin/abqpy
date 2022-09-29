from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class ImageAnimation:
    """The ImageAnimation object is used to build frame by frame animation.

    .. note:: 
        This object can be accessed by::

            import animation
            session.imageAnimation
    """

    #: A String specifying the file to which the animation frames is to be written.
    fileName: str = ""

    @abaqus_method_doc
    def __init__(self, fileName: str, format: SymbolicConstant):
        """This method creates an ImageAnimation object from the specified filename and format.

        .. note:: 
            This function can be accessed by::

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
        self.fileName = fileName

    @abaqus_method_doc
    def writeFrame(self, canvasObjects: tuple = ()):
        """This method adds a frame to the ImageAnimation object.

        Parameters
        ----------
        canvasObjects
            A sequence specifying the canvas objects to capture. The default is to capture all
            canvas objects.
        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def close(self):
        """This method closes the ImageAnimation object."""
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def closed(self):
        """This method indicates if the ImageAnimation is open or closed for writing animation
        frames.
        """
        # TODO: implement this method
        ...
