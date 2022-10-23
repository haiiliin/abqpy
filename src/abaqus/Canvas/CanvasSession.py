from typing import Tuple

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Viewport import Viewport
from ..Session.SessionBase import SessionBase
from ..UtilityAndView.abaqusConstants import Boolean, ON, SYSTEM
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class CanvasSession(SessionBase):
    
    @abaqus_method_doc
    def Viewport(
        self,
        name: str,
        origin: Tuple[float, float] = (0.0, 0.0),
        width: float = 120.0,
        height: float = 80.0,
        border: Boolean = ON,
        titleBar: Boolean = ON,
        titleStyle: Literal[C.CUSTOM, C.SYSTEM] = SYSTEM,
        customTitleString: str = "",
    ):
        """This method creates a Viewport object with the specified origin and dimensions.

        .. note:: 
            This function can be accessed by::

                session.Viewport

        Parameters
        ----------
        name
            A String specifying the repository key.
        origin
            A pair of Floats specifying the **X**- and **Y**-coordinates in millimeters in the canvas
            coordinate system of the lower left corner of the viewport. The default origin is (0,
            0).
        width
            A Float specifying the width in millimeters of the viewport. Possible values are 30 ≤
            **width** ≤ (*maxWidth*). The default value is 120.0. Note: The maximum value of width
            (*maxWidth*) is the width of the screen in millimeters.
        height
            A Float specifying the height in millimeters of the viewport. This height includes the
            title bar. Possible values are 30 ≤ **height** ≤ (*maxHeight*). The default value is
            80.0. Note: The maximum value of height (*maxHeight*) is the height of the screen in
            millimeters.
        border
            A Boolean specifying whether the viewport border is visible in a printed image. The
            default value is ON.
        titleBar
            A Boolean specifying whether the viewport title should be displayed in a printed image.
            The default value is ON.If **border** = OFF, the title will not be visible, even if
            **titleBar** =ON.
        titleStyle
            A SymbolicConstant specifying which title to use for the viewport title. Possible values
            are CUSTOM and SYSTEM. The default value is SYSTEM.If **titleStyle** = CUSTOM,
            **customTitleString** will be used. If **titleStyle** =  SYSTEM, a system-generated string
            will be used.
        customTitleString
            A String specifying the viewport title when **titleStyle** =CUSTOM. The default value is
            an empty string.

        Returns
        -------
        Viewport
            A :py:class:`~abaqus.Canvas.Viewport.Viewport` object.

        Raises
        ------
        SystemError: the current viewport may not be deleted
            If the user attempts to delete the only viewport.
        RangeError: width must be a Float in the range: 30 <= width <= **maxWidth**
            If **width** is out of range.
        RangeError: height must be a Float in the range: 30 <= width <= **maxHeight**
            If **height** is out of range.
        """
        self.viewports[name] = viewport = Viewport(
            name, origin, width, height, border, titleBar, titleStyle, customTitleString
        )
        return viewport
