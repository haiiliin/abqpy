from typing import Sequence, Union

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Odb.UserDataBase import UserDataBase
from ..UtilityAndView.abaqusConstants import (
    BOTTOM_LEFT,
    FILLED_ARROW,
    JUSTIFY_LEFT,
    NONE,
    OFF,
    SOLID,
    TRANSPARENT,
    VERY_THIN,
    Boolean,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .Arrow import Arrow
from .Text import Text


@abaqus_class_doc
class AnimationUserData(UserDataBase):
    @abaqus_method_doc
    def Arrow(
        self,
        name: str,
        startPoint: Sequence[float] = (0.0, 0.0),
        endPoint: Sequence[float] = (0.0, 0.0),
        startAnchor: Union[
            Literal[
                C.CENTER_RIGHT,
                C.TOP_CENTER,
                C.BOTTOM_RIGHT,
                C.BOTTOM_LEFT,
                C.CENTER,
                C.TOP_RIGHT,
                C.CENTER_LEFT,
                C.TOP_LEFT,
                C.BOTTOM_CENTER,
            ],
            float,
        ] = BOTTOM_LEFT,
        endAnchor: Union[
            Literal[
                C.CENTER_RIGHT,
                C.TOP_CENTER,
                C.BOTTOM_RIGHT,
                C.BOTTOM_LEFT,
                C.CENTER,
                C.TOP_RIGHT,
                C.CENTER_LEFT,
                C.TOP_LEFT,
                C.BOTTOM_CENTER,
            ],
            float,
        ] = BOTTOM_LEFT,
        startHeadStyle: Literal[
            C.FILLED_DIAMOND,
            C.FILLED_SQUARE,
            C.HOLLOW_CIRCLE,
            C.HOLLOW_SQUARE,
            C.FILLED_ARROW,
            C.HOLLOW_DIAMOND,
            C.ARROW,
            C.NONE,
            C.FILLED_CIRCLE,
        ] = NONE,
        endHeadStyle: Literal[
            C.FILLED_DIAMOND,
            C.FILLED_SQUARE,
            C.HOLLOW_CIRCLE,
            C.HOLLOW_SQUARE,
            C.FILLED_ARROW,
            C.HOLLOW_DIAMOND,
            C.ARROW,
            C.NONE,
            C.FILLED_CIRCLE,
        ] = FILLED_ARROW,
        startGap: float = 0.0,
        endGap: float = 0.0,
        color: str = "White",
        lineStyle: Literal[C.DASHED, C.SOLID, C.DOT_DASH, C.DOTTED] = SOLID,
        lineThickness: Literal[C.THIN, C.THICK, C.VERY_THIN, C.MEDIUM] = VERY_THIN,
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
            A pair of Floats specifying the start point **X**  and **Y** offsets in millimeters from
            **startAnchor**. The default value is (0, 0).
        endPoint
            A pair of Floats specifying the end point **X**  and **Y** offsets in millimeters from
            **endAnchor**. The default value is (0, 0).
        startAnchor
            A SymbolicConstant or a sequence of Floats specifying a point. A sequence of two Floats
            specifies the **X**  and **Y** coordinates as percentages of the viewport width and height.
            A sequence of three Floats specifies the **X**, **Y**, and **Z** coordinates of a point in
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
            specifies the **X**  and **Y** coordinates as percentages of the viewport width and height.
            A Sequence of three Floats specifies the **X**, **Y**, and **Z** coordinates of a point in
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
            An Arrow object.
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
        offset: Sequence[float] = (),
        anchor: Union[
            Literal[
                C.CENTER_RIGHT,
                C.TOP_CENTER,
                C.BOTTOM_RIGHT,
                C.BOTTOM_LEFT,
                C.CENTER,
                C.TOP_RIGHT,
                C.CENTER_LEFT,
                C.TOP_LEFT,
                C.BOTTOM_CENTER,
            ],
            float,
        ] = BOTTOM_LEFT,
        referencePoint: Union[
            Literal[
                C.CENTER_RIGHT,
                C.TOP_CENTER,
                C.BOTTOM_RIGHT,
                C.BOTTOM_LEFT,
                C.CENTER,
                C.TOP_RIGHT,
                C.CENTER_LEFT,
                C.TOP_LEFT,
                C.BOTTOM_CENTER,
            ],
            float,
        ] = BOTTOM_LEFT,
        rotationAngle: float = 0,
        color: str = "White",
        font: str = "-*-verdana-medium-r-normal--120-*",
        backgroundStyle: Literal[C.OTHER, C.MATCH, C.TRANSPARENT] = TRANSPARENT,
        backgroundColor: str = "",
        box: Boolean = OFF,
        justification: Literal[C.JUSTIFY_CENTER, C.JUSTIFY_LEFT, C.JUSTIFY_RIGHT] = JUSTIFY_LEFT,
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
            A pair of Floats specifying the **X**  and **Y** offsets in millimeters of the Text object
            from **anchor**. The default value is (0, 0).
        anchor
            A SymbolicConstant or a sequence of Floats specifying a point. A sequence of two Floats
            specifies the **X**  and **Y** coordinates as percentages of the viewport width and height.
            A Sequence of three Floats specifies the **X**, **Y**, and **Z** coordinates of a point in
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
            Floats specifies the **X**  and **Y** coordinates of the reference point of the Text
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
            A Text object.
        """
        self.annotations[name] = tex = Text(
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
        return tex
