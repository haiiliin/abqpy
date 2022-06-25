from abaqusConstants import *


class PrintOptions:
    """The PrintOptions object stores the common settings that Abaqus uses for all print
    methods. The PrintOptions object has no constructor. Abaqus creates the **printOptions**
    member when a session is started.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            session.printOptions
    """

    def setValues(
        self,
        rendition: SymbolicConstant = COLOR,
        vpDecorations: Boolean = ON,
        vpBackground: Boolean = OFF,
        compass: Boolean = OFF,
        printCommand: str = "",
        deleteTemporaryFiles: Boolean = ON,
        reduceColors: Boolean = OFF,
    ):
        """This method modifies the PrintOptions object.

        Parameters
        ----------
        rendition
            A SymbolicConstant specifying how the image is rendered. Possible values are
            BLACK_AND_WHITE, GREYSCALE, and COLOR. The default value is COLOR.
        vpDecorations
            A Boolean specifying whether the output includes the viewport border and title. The
            default value is ON.
        vpBackground
            A Boolean specifying whether the output includes viewport backgrounds. The default value
            is OFF.
        compass
            A Boolean specifying whether the output includes the view compass The default value is
            OFF.
        printCommand
            A String specifying the default print command that will be used by the printToPrinter
            method if no **printCommand** argument is provided. The default value is "lpr".
        deleteTemporaryFiles
            A Boolean specifying whether to delete the temporary files created when an image is
            printed. The default value is ON.You should set the **deleteTemporaryFiles** argument to
            False if your printer does not support print spooling.
        reduceColors
            A Boolean specifying whether the raster image printed is reduced from true color to 256
            colors to reduce file size. The quality of the image will be compromised. The default
            value is OFF.
        """
        pass
