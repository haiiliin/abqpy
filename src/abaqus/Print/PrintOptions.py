from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ..UtilityAndView.abaqusConstants import Boolean, COLOR, OFF, ON, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .._OptionsBase import _OptionsBase


@abaqus_class_doc
class PrintOptions(_OptionsBase):
    """The PrintOptions object stores the common settings that Abaqus uses for all print
    methods. The PrintOptions object has no constructor. Abaqus creates the **printOptions**
    member when a session is started.

    .. note:: 
        This object can be accessed by::

            session.printOptions
    """

    #: A SymbolicConstant specifying how the image is rendered. Possible values are
    #: BLACK_AND_WHITE, GREYSCALE, and COLOR. The default value is COLOR.
    rendition: SymbolicConstant = COLOR

    #: A Boolean specifying whether the output includes the viewport border and title. The
    #: default value is ON.
    vpDecorations: Boolean = ON

    #: A Boolean specifying whether the output includes viewport backgrounds. The default value is
    #: OFF.
    vpBackground: Boolean = OFF

    #: A Boolean specifying whether the output includes the view compass. The default value is OFF.
    compass: Boolean = OFF

    #: A String specifying the default print command that will be used by the printToPrinter method
    #: if no **printCommand** argument is provided. The default value is "lpr".
    printCommand: str = "lpr"

    #: A Boolean specifying whether to delete the temporary files created when an image is printed.
    #: The default value is ON. You should set the **deleteTemporaryFiles** argument to False if your
    #: printer does not support print spooling.
    deleteTemporaryFiles: Boolean = ON

    #: A Boolean specifying whether the raster image printed is reduced from true color to 256 colors
    #: to reduce file size. The quality of the image will be compromised. The default value is OFF.
    reduceColors: Boolean = OFF

    @abaqus_method_doc
    def setValues(
        self,
        *,
        rendition: Literal[C.COLOR, C.GREYSCALE, C.BLACK_AND_WHITE] = COLOR,
        vpDecorations: Boolean = ON,
        vpBackground: Boolean = OFF,
        compass: Boolean = OFF,
        printCommand: str = "lpr",
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
            printed. The default value is ON. You should set the **deleteTemporaryFiles** argument to
            False if your printer does not support print spooling.
        reduceColors
            A Boolean specifying whether the raster image printed is reduced from true color to 256
            colors to reduce file size. The quality of the image will be compromised. The default
            value is OFF.
        """
        super().setValues(
            rendition=rendition,
            vpDecorations=vpDecorations,
            vpBackground=vpBackground,
            compass=compass,
            printCommand=printCommand,
            deleteTemporaryFiles=deleteTemporaryFiles,
            reduceColors=reduceColors,
        )
