from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .._OptionsBase import _OptionsBase
from ..UtilityAndView.abaqusConstants import SIZE_ON_SCREEN, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class PngOptions(_OptionsBase):
    """The PngOptions object stores the settings that Abaqus uses when printing in PNG format.

    The PngOptions object has no constructor. Abaqus creates the **pngOptions** member when a session is
    started.
    """

    #: The SymbolicConstant SIZE_ON_SCREEN or a pair of Ints specifying the width and height of
    #: the image in pixels. Possible values are (**minWidth**, **minHeight**) ≤ **imageSize** ≤
    #: (**maxWidth** and **maxHeight**). The default value is SIZE_ON_SCREEN.
    #: Note: The minimum value of width and height (**minWidth** and **minHeight**) is the number
    #: of pixels that occupy 10 mm at the current screen resolution. The value is typically
    #: around 50pixels and may be different for width and height.
    #: The maximum value of width and height (**maxWidth** and **maxHeight**) is the largest
    #: number of pixels supported by the system graphics and will be at least as large as the
    #: screen dimensions.
    imageSize: SymbolicConstant = SIZE_ON_SCREEN

    @abaqus_method_doc
    def setValues(self, *, imageSize: Literal[C.SIZE_ON_SCREEN] = SIZE_ON_SCREEN):
        """This method modifies the PngOptions object.

        Parameters
        ----------
        imageSize
            The SymbolicConstant SIZE_ON_SCREEN or a pair of Ints specifying the width and height of
            the image in pixels. Possible values are (**minWidth**, **minHeight**) ≤ **imageSize** ≤
            (**maxWidth** and **maxHeight**). The default value is SIZE_ON_SCREEN.
            Note: The minimum value of width and height (**minWidth** and **minHeight**) is the number
            of pixels that occupy 10 mm at the current screen resolution. The value is typically
            around 50 pixels and may be different for width and height.
            The maximum value of width and height (**maxWidth** and **maxHeight**) is the largest
            number of pixels supported by the system graphics and will be at least as large as the
            screen dimensions.

        Raises
        ------
        RangeError
            imageSize must be SIZE_ON_SCREEN or a sequence of 2 Ints in the range
            (minWidth, minHeight) <= (width, height) <= (maxWidth, maxHeight)
            If either the width or height arguments of **imageSize** are out of range (where
            **minWidth** and **minHeight** are the number of pixels corresponding to approximately 10 mm
            for a given display and **maxWidth** and **maxHeight** are the largest allowable number of
            pixels supported by the system graphics).
        """
        super().setValues(imageSize=imageSize)
