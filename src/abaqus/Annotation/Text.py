import typing

from abaqusConstants import *
from .Annotation import Annotation


class Text(Annotation):
    """The Text object stores the text settings and location of a text annotation.
    The Text object is derived from the Annotation object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import annotationToolset
            mdb.annotations[name]
            session.odbs[name].userData.annotations[name]
            session.viewports[name].annotationsToPlot[i]
    """

    #: A Float specifying the width in millimeters of the Text object.
    width: float = None

    #: A Float specifying the height in millimeters of the Text object.
    height: float = None

    #: A String specifying the annotation repository key.
    name: str

    #: A String specifying the text of the Text object. The default value is an empty string.
    text: str = ""

    #: A pair of Floats specifying the **X**- and **Y**-offsets in millimeters of the Text object
    #: from **anchor**. The default value is (0, 0).
    offset: tuple[float] = ()

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
    anchor: typing.Union[SymbolicConstant, float] = BOTTOM_LEFT

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
    referencePoint: typing.Union[SymbolicConstant, float] = BOTTOM_LEFT

    #: A Float specifying the amount of rotation in degrees about **referencePoint**. The default
    #: value is 0.0.
    rotationAngle: float = 0

    #: A String specifying the color of the Text object. Possible string values are any valid
    #: color. The default value is "White".
    color: str = ""

    #: A String specifying the font of the Text object. Possible string values are any valid
    #: font specification. The default value is "-*-verdana-medium-r-normal--120-*".
    font: str = ""

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

    def __init__(
        self,
        name: str,
        text: str = "",
        offset: tuple[float] = (),
        anchor: typing.Union[SymbolicConstant, float] = BOTTOM_LEFT,
        referencePoint: typing.Union[SymbolicConstant, float] = BOTTOM_LEFT,
        rotationAngle: float = 0,
        color: str = "",
        font: str = "",
        backgroundStyle: SymbolicConstant = TRANSPARENT,
        backgroundColor: str = "",
        box: Boolean = OFF,
        justification: SymbolicConstant = JUSTIFY_LEFT,
    ):
        """This method creates a Text object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

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
        pass

    def setValues(
        self,
        text: str = "",
        offset: tuple[float] = (),
        anchor: typing.Union[SymbolicConstant, float] = BOTTOM_LEFT,
        referencePoint: typing.Union[SymbolicConstant, float] = BOTTOM_LEFT,
        rotationAngle: float = 0,
        color: str = "",
        font: str = "",
        backgroundStyle: SymbolicConstant = TRANSPARENT,
        backgroundColor: str = "",
        box: Boolean = OFF,
        justification: SymbolicConstant = JUSTIFY_LEFT,
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
            are:BOTTOM_LEFTBOTTOM_CENTERBOTTOM_RIGHTCENTER_LEFTCENTERCENTER_RIGHTTOP_LEFTTOP_CENTERTOP_RIGHTThe
            default value is BOTTOM_LEFT.
        referencePoint
            A SymbolicConstant or a sequence of Floats specifying a point. The sequence of two
            Floats specifies the **X**- and **Y**-coordinates of the reference point of the Text
            annotation given as percentages of its width and height. The SymbolicConstant indicates
            a relative position. Possible values
            are:BOTTOM_LEFTBOTTOM_CENTERBOTTOM_RIGHTCENTER_LEFTCENTERCENTER_RIGHTTOP_LEFTTOP_CENTERTOP_RIGHTThe
            default value is BOTTOM_LEFT.
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
        pass
