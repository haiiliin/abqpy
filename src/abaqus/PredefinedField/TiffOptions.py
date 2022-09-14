from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class TiffOptions:
    """The TiffOptions object stores the settings that Abaqus uses when printing in TIFF
    format. The TiffOptions object has no constructor. Abaqus creates the **tiffOptions**
    member when a session is started.

    .. note:: 
        This object can be accessed by::

            session.tiffOptions
    """

    @abaqus_method_doc
    def setValues(self, imageSize: SymbolicConstant = SIZE_ON_SCREEN):
        """This method modifies the TiffOptions object.

        Parameters
        ----------
        imageSize
            The SymbolicConstant SIZE_ON_SCREEN or a pair of Ints specifying the width and height of
            the image in pixels. Possible values are (**minWidth**, **minHeight**) ≤ **imageSize** ≤
            (**maxWidth** and **maxHeight**). The default value is SIZE_ON_SCREEN.
            Note:The minimum value of width and height (**minWidth** and **minHeight** ) is the number
            of pixels that occupy 10 mm at the current screen resolution. The value is typically
            around 50 pixels and may be different for width and height.
            The maximum value of width and height (**maxWidth** and **maxHeight** ) is the largest
            number of pixels supported by the system graphics and will be at least as large as the
            screen dimensions.

        Raises
        ------
        RangeError
            If either the width or height arguments of **imageSize** are out of range (where
            **minWidth** and **minHeight** are the number of pixels corresponding to approximately 10 mm
            for a given display and **maxWidth** and **maxHeight** are the largest allowable number of
            pixels supported by the system graphics).
        RangeError: imageSize must be SIZE_ON_SCREEN or a sequence of 2 Ints in the range
            (minWidth, minHeight) <= (width, height) <= (maxWidth, maxHeight).
        """
        ...
