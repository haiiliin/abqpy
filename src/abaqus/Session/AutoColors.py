from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class AutoColors:
    """The AutoColors object defines a color palette.

    .. note::
        This object can be accessed by::

            session.autoColors
    """

    @abaqus_method_doc
    def setValues(self, colors: tuple):
        """This method changes the color palette.

        Parameters
        ----------
        colors
            A sequence of Strings specifying the colors of the palette. Strings must be named colors
            or represent red, green, blue components in hexadecimal form. For instance, '#FF0000'
            for red, '#00FF00' for green and '#0000FF' for blue
        """
        ...
