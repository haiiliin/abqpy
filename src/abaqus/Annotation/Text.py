from typing import Union, Optional, Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Annotation import Annotation
from ..UtilityAndView.abaqusConstants import BOTTOM_LEFT, Boolean, JUSTIFY_LEFT, OFF, SymbolicConstant, TRANSPARENT
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .._OptionsBase import _OptionsBase


@abaqus_class_doc
class Text(Annotation, _OptionsBase):
    """The Text object stores the text settings and location of a text annotation.
    The Text object is derived from the Annotation object.

    .. note::
        This object can be accessed by::

            import annotationToolset
            mdb.annotations[name]
            session.odbs[name].userData.annotations[name]
            session.viewports[name].annotationsToPlot[i]
    """

    #: A Float specifying the width in millimeters of the Text object.
    width: Optional[float] = None

    #: A Float specifying the height in millimeters of the Text object.
    height: Optional[float] = None

    #: A String specifying the annotation repository key.
    name: str

    #: A String specifying the text of the Text object. The default value is an empty string.
    text: str = ""

    #: A pair of Floats specifying the **X**- and **Y**-offsets in millimeters of the Text object
    #: from **anchor**. The default value is (0, 0).
    offset: Sequence[float] = (0.0, 0.0)

    #: A SymbolicConstant or a sequence of Floats specifying a point. A sequence of two Floats
    #: specifies the **X**- and **Y** coordinates as percentages of the viewport width and height.
    #: A Sequence of three Floats specifies the **X**-, **Y**-, and **Z**-coordinates of a point in
    #: the model coordinate system. A SymbolicConstant specifies a relative position. Possible
    #: values are:
    #:
    #: - BOTTOM_LEFT
    #: - BOTTOM_CENTER
    #: - BOTTOM_RIGHT
    #: - CENTER_LEFT
    #: - CENTER
    #: - CENTER_RIGHT
    #: - TOP_LEFT
    #: - TOP_CENTER
    #: - TOP_RIGHT
    #:
    #: The default value is BOTTOM_LEFT.
    anchor: Union[SymbolicConstant, float] = BOTTOM_LEFT

    #: A SymbolicConstant or a sequence of Floats specifying a point. The sequence of two
    #: Floats specifies the **X**- and **Y**-coordinates of the reference point of the Text
    #: annotation given as percentages of its width and height. The SymbolicConstant indicates
    #: a relative position. Possible values are:
    #:
    #: - BOTTOM_LEFT
    #: - BOTTOM_CENTER
    #: - BOTTOM_RIGHT
    #: - CENTER_LEFT
    #: - CENTER
    #: - CENTER_RIGHT
    #: - TOP_LEFT
    #: - TOP_CENTER
    #: - TOP_RIGHT
    #:
    #: The default value is BOTTOM_LEFT.
    referencePoint: Union[SymbolicConstant, float] = BOTTOM_LEFT

    #: A Float specifying the amount of rotation in degrees about **referencePoint**. The default
    #: value is 0.0.
    rotationAngle: float = 0.0

    #: A String specifying the color of the Text object. Possible string values are any valid
    #: color. The default value is "White".
    color: str = "White"

    #: A String specifying the font of the Text object. Possible string values are any valid
    #: font specification. The default value is "-*-verdana-medium-r-normal--120-*".
    font: str = "-*-verdana-medium-r-normal--120-*"

    #: A SymbolicConstant specifying the Text object background style. Possible values are
    #: MATCH, TRANSPARENT, and OTHER. The default value is TRANSPARENT.
    backgroundStyle: SymbolicConstant = TRANSPARENT

    #: A String specifying the color of the Text object background. Possible string values are
    #: any valid color. The default value matches the viewport background.
    backgroundColor: str = ""

    #: A Boolean specifying whether the box around the text is shown. The default value is OFF.
    box: Boolean = OFF

    #: A SymbolicConstant specifying the Text object justification for multiline text. Possible
    #: values are JUSTIFY_LEFT, JUSTIFY_CENTER, and JUSTIFY_RIGHT. The default value is
    #: JUSTIFY_LEFT.
    justification: SymbolicConstant = JUSTIFY_LEFT

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        text: str = "",
        offset: Sequence[float] = (0.0, 0.0),
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
        rotationAngle: float = 0.0,
        color: str = "White",
        font: str = "-*-verdana-medium-r-normal--120-*",
        backgroundStyle: Literal[C.OTHER, C.MATCH, C.TRANSPARENT] = TRANSPARENT,
        backgroundColor: str = "",
        box: Boolean = OFF,
        justification: Literal[C.JUSTIFY_CENTER, C.JUSTIFY_LEFT, C.JUSTIFY_RIGHT] = JUSTIFY_LEFT,
    ):
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
        super().__init__()
        self.name = name
        self.text = text
        self.offset = offset
        self.anchor = anchor
        self.referencePoint = referencePoint
        self.rotationAngle = rotationAngle
        self.color = color
        self.font = font
        self.backgroundStyle = backgroundStyle
        self.backgroundColor = backgroundColor
        self.box = box
        self.justification = justification

    @abaqus_method_doc
    def setValues(
        self,
        text: str = "",
        offset: Sequence[float] = (0.0, 0.0),
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
        rotationAngle: float = 0.0,
        color: str = "White",
        font: str = "-*-verdana-medium-r-normal--120-*",
        backgroundStyle: Literal[C.OTHER, C.MATCH, C.TRANSPARENT] = TRANSPARENT,
        backgroundColor: str = "",
        box: Boolean = OFF,
        justification: Literal[C.JUSTIFY_CENTER, C.JUSTIFY_LEFT, C.JUSTIFY_RIGHT] = JUSTIFY_LEFT,
    ):
        """This method modifies the Text object.

        Parameters
        ----------
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
            values
            are:

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
            a relative position. Possible values
            are:

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

        """
        super().setValues(
            text=text,
            offset=offset,
            anchor=anchor,
            referencePoint=referencePoint,
            rotationAngle=rotationAngle,
            color=color,
            font=font,
            backgroundStyle=backgroundStyle,
            backgroundColor=backgroundColor,
            box=box,
            justification=justification,
        )
