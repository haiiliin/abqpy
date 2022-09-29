from typing import Tuple, Union

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Arrow import Arrow
from .Text import Text
from ..Odb.UserDataBase import UserDataBase
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class AnimationUserData(UserDataBase):
    @abaqus_method_doc
    def Arrow(
        self,
        name: str,
        startPoint: Tuple[float, ...] = (0.0, 0.0),
        endPoint: Tuple[float, ...] = (0.0, 0.0),
        startAnchor: Union[SymbolicConstant, float] = BOTTOM_LEFT,
        endAnchor: Union[SymbolicConstant, float] = BOTTOM_LEFT,
        startHeadStyle: SymbolicConstant = NONE,
        endHeadStyle: SymbolicConstant = FILLED_ARROW,
        startGap: float = 0.0,
        endGap: float = 0.0,
        color: str = "White",
        lineStyle: SymbolicConstant = SOLID,
        lineThickness: SymbolicConstant = VERY_THIN,
    ) -> Arrow:
        """This method creates an Arrow object.

        .. note:: 
            This function can be accessed by::

                mdb.Arrow
                session.odbs[name].userData.Arrow

        Parameters
        ----------
        name
            A String specifying the annotation repository key.
        startPoint
            A pair of Floats specifying the start point **X**- and **Y**-offsets in millimeters from
            **startAnchor**. The default value is (0, 0).
        endPoint
            A pair of Floats specifying the end point **X**- and **Y**-offsets in millimeters from
            **endAnchor**. The default value is (0, 0).
        startAnchor
            A SymbolicConstant or a sequence of Floats specifying a point. A sequence of two Floats
            specifies the **X**- and **Y**-coordinates as percentages of the viewport width and height.
            A sequence of three Floats specifies the **X**-, **Y**-, and **Z**-coordinates of a point in
            the model coordinate system. A SymbolicConstant indicates a relative position. Possible
            values are:
            
            - BOTTOM_LEFT,,
            - BOTTOM_CENTER
            - BOTTOM_RIGHT
            - CENTER_LEFT
            - CENTER
            - CENTER_RIGHT
            - TOP_LEFT
            - TOP_CENTER
            - TOP_RIGHT
                
            The default value is BOTTOM_LEFT.
        endAnchor
            A SymbolicConstant or a sequence of Floats specifying a point. A sequence of two Floats
            specifies the **X**- and **Y**-coordinates as percentages of the viewport width and height.
            A Sequence of three Floats specifies the **X**-, **Y**-, and **Z**-coordinates of a point in
            the model coordinate system. A SymbolicConstant indicates a relative position. Possible
            values are:
            
            - BOTTOM_LEFT
            - BOTTOM_CENTER
            - BOTTOM_RIGHT
            - CENTER_LEFT
            - CENTER
            - CENTER_RIGHT
            - TOP_LEFT
            - TOP_CENTER
            - TOP_RIGHT
                
            The default value is BOTTOM_LEFT.
        startHeadStyle
            A SymbolicConstant specifying the style of the start head. Possible values are:
            
            - ARROW
            - FILLED_ARROW
            - HOLLOW_CIRCLE
            - FILLED_CIRCLE
            - HOLLOW_DIAMOND
            - FILLED_DIAMOND
            - HOLLOW_SQUARE
            - FILLED_SQUARE
            - NONE
            
            The default value is NONE.
        endHeadStyle
            A SymbolicConstant specifying the style of the end head. Possible values are:
            
            - ARROW
            - FILLED_ARROW
            - HOLLOW_CIRCLE
            - FILLED_CIRCLE
            - HOLLOW_DIAMOND
            - FILLED_DIAMOND
            - HOLLOW_SQUARE
            - FILLED_SQUARE
            - NONE
            
            The default value is FILLED_ARROW.
        startGap
            A Float specifying the distance in millimeters between the arrow start point and the
            arrow start head. The default value is 0.0.
        endGap
            A Float specifying the distance in millimeters between the arrow end point and the arrow
            end head. The default value is 0.0.
        color
            A String specifying the color of the arrow. Possible string values are any valid color.
            The default value is "White".
        lineStyle
            A SymbolicConstant specifying the line style of the arrow. Possible values are SOLID,
            DASHED, DOTTED, and DOT_DASH. The default value is SOLID.
        lineThickness
            A SymbolicConstant specifying the line thickness of the arrow. Possible values are
            VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.

        Returns
        -------
        Arrow
            An :py:class:`~abaqus.Annotation.Arrow.Arrow` object.
        """
        self.annotations[name] = arrow = Arrow(
            name,
            startPoint,
            endPoint,
            startAnchor,
            endAnchor,
            startHeadStyle,
            endHeadStyle,
            startGap,
            endGap,
            color,
            lineStyle,
            lineThickness,
        )
        return arrow

    @abaqus_method_doc
    def Text(
        self,
        name: str,
        text: str = "",
        offset: Tuple[float, ...] = (),
        anchor: Union[SymbolicConstant, float] = BOTTOM_LEFT,
        referencePoint: Union[SymbolicConstant, float] = BOTTOM_LEFT,
        rotationAngle: float = 0,
        color: str = "White",
        font: str = "-*-verdana-medium-r-normal--120-*",
        backgroundStyle: SymbolicConstant = TRANSPARENT,
        backgroundColor: str = "",
        box: Boolean = OFF,
        justification: SymbolicConstant = JUSTIFY_LEFT,
    ) -> Text:
        """This method creates a Text object.

        .. note:: 
            This function can be accessed by::

                mdb.Text
                session.odbs[name].userData.Text

        Parameters
        ----------
        name
            A String specifying the annotation repository key.
        text
            A String specifying the text of the Text object. The default value is an empty string.
        offset
            A pair of Floats specifying the **X**- and **Y**-offsets in millimeters of the Text object
            from **anchor**. The default value is (0, 0).
        anchor
            A SymbolicConstant or a sequence of Floats specifying a point. A sequence of two Floats
            specifies the **X**- and **Y** coordinates as percentages of the viewport width and height.
            A Sequence of three Floats specifies the **X**-, **Y**-, and **Z**-coordinates of a point in
            the model coordinate system. A SymbolicConstant specifies a relative position. Possible
            values are:
            
            - BOTTOM_LEFT
            - BOTTOM_CENTER
            - BOTTOM_RIGHT
            - CENTER_LEFT
            - CENTER
            - CENTER_RIGHT
            - TOP_LEFT
            - TOP_CENTER
            - TOP_RIGHT
            
            The default value is BOTTOM_LEFT.
        referencePoint
            A SymbolicConstant or a sequence of Floats specifying a point. The sequence of two
            Floats specifies the **X**- and **Y**-coordinates of the reference point of the Text
            annotation given as percentages of its width and height. The SymbolicConstant indicates
            a relative position. Possible values are:
            
            - BOTTOM_LEFT
            - BOTTOM_CENTER
            - BOTTOM_RIGHT
            - CENTER_LEFT
            - CENTER
            - CENTER_RIGHT
            - TOP_LEFT
            - TOP_CENTER
            - TOP_RIGHT
                
            The default value is BOTTOM_LEFT.
        rotationAngle
            A Float specifying the amount of rotation in degrees about **referencePoint**. The default
            value is 0.0.
        color
            A String specifying the color of the Text object. Possible string values are any valid
            color. The default value is "White".
        font
            A String specifying the font of the Text object. Possible string values are any valid
            font specification. The default value is "-*-verdana-medium-r-normal--120-*".
        backgroundStyle
            A SymbolicConstant specifying the Text object background style. Possible values are
            MATCH, TRANSPARENT, and OTHER. The default value is TRANSPARENT.
        backgroundColor
            A String specifying the color of the Text object background. Possible string values are
            any valid color. The default value matches the viewport background.
        box
            A Boolean specifying whether the box around the text is shown. The default value is OFF.
        justification
            A SymbolicConstant specifying the Text object justification for multiline text. Possible
            values are JUSTIFY_LEFT, JUSTIFY_CENTER, and JUSTIFY_RIGHT. The default value is
            JUSTIFY_LEFT.

        Returns
        -------
        Text
            A :py:class:`~abaqus.Annotation.Text.Text` object.
        """
        self.annotations[name] = text = Text(
            name,
            text,
            offset,
            anchor,
            referencePoint,
            rotationAngle,
            color,
            font,
            backgroundStyle,
            backgroundColor,
            box,
            justification,
        )
        return text
