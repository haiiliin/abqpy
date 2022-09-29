from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import (Boolean, NUMBERS, OFF, ON, SymbolicConstant,
                                              TRANSPARENT, XZPLANE)


@abaqus_class_doc
class ViewportAnnotationOptions:
    """The ViewportAnnotationOptions object stores settings that control how annotations are
    rendered in a particular viewport. ViewportAnnotationOptions objects are accessed in one
    of two ways:
    - The default viewport annotations. These settings are used as defaults when other
    **viewportAnnotationOptions** members are created and can be set to customize user
    preferences.
    - The viewport annotations associated with a particular viewport.
    The ViewportAnnotationOptions object has no constructor; Abaqus creates the
    **defaultViewportAnnotationOptions** member when a session is started. When a new viewport
    is created, the settings are copied from the current viewport.

    .. note::
        This object can be accessed by::

            session.defaultViewportAnnotationOptions
            session.viewports[name].viewportAnnotationOptions
    """

    @abaqus_method_doc
    def setValues(
        self,
        triad: Boolean = ON,
        triadPosition: Optional[int] = None,
        triadColor: str = "",
        triadLabels: SymbolicConstant = NUMBERS,
        triadFont: str = "",
        triadSize: int = 4,
        legend: Boolean = ON,
        legendMinMax: Boolean = OFF,
        legendBox: Boolean = ON,
        legendDecimalPlaces: int = 3,
        legendPosition: Optional[int] = None,
        legendFont: str = "",
        legendTextColor: str = "",
        legendBackgroundStyle: SymbolicConstant = TRANSPARENT,
        legendBackgroundColor: str = "",
        title: Boolean = ON,
        titleBox: Boolean = OFF,
        titlePosition: Optional[int] = None,
        titleFont: str = "",
        titleTextColor: str = "",
        titleBackgroundStyle: SymbolicConstant = TRANSPARENT,
        titleBackgroundColor: str = "",
        state: Boolean = ON,
        stateBox: Boolean = OFF,
        statePosition: Optional[int] = None,
        stateFont: str = "",
        stateTextColor: str = "",
        stateBackgroundStyle: SymbolicConstant = TRANSPARENT,
        stateBackgroundColor: str = "",
        compass: Boolean = ON,
        compassScale: float = 0,
        compassPrivilegedPlane: SymbolicConstant = XZPLANE,
    ):
        """This method modifies the ViewportAnnotationOptions object.

        Parameters
        ----------
        triad
            A Boolean specifying whether the view orientation triad is shown. The default value is
            ON.
        triadPosition
            A pair of Ints specifying the position of the view orientation triad as a percentage of
            the viewport size. Possible values are (0, 0) ≤ **triadPosition** ≤ (100, 100). The
            default value is (6, 12).
        triadColor
            A String specifying the color of the view orientation triad. Possible values are any
            valid color. The default value is "White".
        triadLabels
            A SymbolicConstant specifying how the view orientation triad is labeled. Possible values
            are:NUMBERS, specifying the label axes 1, 2, 3.LETTERS, specifying the label axes X, Y,
            Z.The default value is NUMBERS.
        triadFont
            A String specifying the font of the view orientation triad labels. Possible values are
            any valid font. The default value is "-*-verdana-bold-r-normal--120-*".
        triadSize
            An Int specifying the length of each triad axis as a percentage of the viewport size.
            Possible values are 1 ≤ **legendDecimalPlaces** ≤ 50. The default value is 4.
        legend
            A Boolean specifying whether the legend is shown. The default value is ON.
        legendMinMax
            A Boolean specifying whether the minimum and maximum values for **X - Y** and contour plots
            are shown. The default value is OFF.
        legendBox
            A Boolean specifying whether the box around the legend is shown. The default value is
            ON.
        legendDecimalPlaces
            An Int specifying the number of decimal places to display in the legend. Possible values
            are 0 ≤ **legendDecimalPlaces** ≤ 9. The default value is 3.
        legendPosition
            A pair of Ints specifying the position of the legend as a percentage of the viewport
            size. Possible values are (0, 0)≤ **legendPosition** ≤ (100, 100). The default value is
            (2, 98).
        legendFont
            A String specifying the font of the legend labels. Possible values are any valid font.
            The default value is "-*-verdana-medium-r-*-*-*-120-*-*-*-*-iso8859-1".
        legendTextColor
            A String specifying the color of the legend. Possible values are any valid color. The
            default value is "White".
        legendBackgroundStyle
            A SymbolicConstant specifying the legend background style. Possible values are MATCH,
            TRANSPARENT, and OTHER. The default value is TRANSPARENT.The default color when OTHER is
            specified is the background color (black).
        legendBackgroundColor
            A String specifying the color of the legend background. Possible values are any valid
            color. The initial value matches the viewport background.
        title
            A Boolean specifying whether the title block is shown. The default value is ON.
        titleBox
            A Boolean specifying whether the box around the title block is shown. The default value
            is OFF.
        titlePosition
            A pair of Ints specifying the position of the title block as a percentage of the
            viewport size. Possible values are (0, 0) ≤ **titlePosition** ≤ (100, 100). The default
            value is (13, 20).
        titleFont
            A String specifying the font of the title. Possible values are any valid font. The
            default value is "-*-verdana-medium-r-*-*-*-120-*-*-*-*-iso8859-1".
        titleTextColor
            A String specifying the color of the title. Possible values are any valid color. The
            default value is "White".
        titleBackgroundStyle
            A SymbolicConstant specifying the title block background style. Possible values are
            MATCH, TRANSPARENT, and OTHER. The default value is TRANSPARENT.The default color when
            OTHER is specified is the background color (black).
        titleBackgroundColor
            A String specifying the color of the title block background. Possible values are any
            valid color. The initial value matches the viewport background.
        state
            A Boolean specifying whether the state block is shown. The default value is ON.
        stateBox
            A Boolean specifying whether the box around the state block is shown. The default value
            is OFF.
        statePosition
            A pair of Ints specifying the position of the state block as a percentage of the
            viewport size. Possible values are (0, 0) ≤ **statePosition** ≤ (100, 100). The default
            value is (13, 12).
        stateFont
            A String specifying the font of the state label. Possible values are any valid font. The
            default value is "-*-verdana-medium-r-*-*-*-120-*-*-*-*-iso8859-1".
        stateTextColor
            A String specifying the color of the state block label. Possible values are any valid
            color. The default value is "White".
        stateBackgroundStyle
            A SymbolicConstant specifying the state block background style. Possible values are
            MATCH, TRANSPARENT, and OTHER. The default value is TRANSPARENT.The default color when
            OTHER is specified is the background color (black).
        stateBackgroundColor
            A String specifying the color of the state block background. Possible values are any
            valid color. The initial value matches the viewport background.
        compass
            A Boolean specifying whether the 3D Compass is shown. The default value is ON.
        compassScale
            A Float specifying the relative size of the 3D Compass in the viewport. Possible values
            are 0.5 ≤ **compassScale** ≤ 2.0. The default value is 0.8.
        compassPrivilegedPlane
            A SymbolicConstant specifying the plane that will be used for the base of the 3D
            Compass. Possible values are XYPLANE, XZPLANE, and YZPLANE. The default value is
            XZPLANE.

        Raises
        ------
        RangeError
        """
        ...
