import typing

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Annotation import Annotation
from ..UtilityAndView.abaqusConstants import *
from .._OptionsBase import _OptionsBase


@abaqus_class_doc
class Arrow(Annotation, _OptionsBase):
    """The Arrow object stores the visual settings and location of an arrow annotation.
    The Arrow object is derived from the Annotation object.

    .. note:: 
        This object can be accessed by::

            import annotationToolset
            mdb.annotations[name]
            session.odbs[name].userData.annotations[name]
            session.viewports[name].annotationsToPlot[i]
    """

    #: A String specifying the annotation repository key.
    name: str

    #: A pair of Floats specifying the start point **X**- and **Y**-offsets in millimeters from
    #: **startAnchor**. The default value is (0, 0).
    startPoint: typing.Tuple[float, ...] = (0.0, 0.0)

    #: A pair of Floats specifying the end point **X**- and **Y**-offsets in millimeters from
    #: **endAnchor**. The default value is (0, 0).
    endPoint: typing.Tuple[float, ...] = (0.0, 0.0)

    #: A SymbolicConstant or a sequence of Floats specifying a point. A sequence of two Floats
    #: specifies the **X**- and **Y**-coordinates as percentages of the viewport width and height.
    #: A sequence of three Floats specifies the **X**-, **Y**-, and **Z**-coordinates of a point in
    #: the model coordinate system. A SymbolicConstant indicates a relative position. Possible
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
    startAnchor: typing.Union[SymbolicConstant, float] = BOTTOM_LEFT

    #: A SymbolicConstant or a sequence of Floats specifying a point. A sequence of two Floats
    #: specifies the **X**- and **Y**-coordinates as percentages of the viewport width and height.
    #: A Sequence of three Floats specifies the **X**-, **Y**-, and **Z**-coordinates of a point in
    #: the model coordinate system. A SymbolicConstant indicates a relative position. Possible
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
    endAnchor: typing.Union[SymbolicConstant, float] = BOTTOM_LEFT

    #: A SymbolicConstant specifying the style of the start head. Possible values are:
    #: 
    #: - ARROW
    #: - FILLED_ARROW
    #: - HOLLOW_CIRCLE
    #: - FILLED_CIRCLE
    #: - HOLLOW_DIAMOND
    #: - FILLED_DIAMOND
    #: - HOLLOW_SQUARE
    #: - FILLED_SQUARE
    #: - NONE
    #: 
    #: The default value is NONE.
    startHeadStyle: SymbolicConstant = NONE

    #: A SymbolicConstant specifying the style of the end head. Possible values are:
    #: 
    #: - ARROW
    #: - FILLED_ARROW
    #: - HOLLOW_CIRCLE
    #: - FILLED_CIRCLE
    #: - HOLLOW_DIAMOND
    #: - FILLED_DIAMOND
    #: - HOLLOW_SQUARE
    #: - FILLED_SQUARE
    #: - NONE
    #: 
    #: The default value is FILLED_ARROW.
    endHeadStyle: SymbolicConstant = FILLED_ARROW

    #: A Float specifying the distance in millimeters between the arrow start point and the
    #: arrow start head. The default value is 0.0.
    startGap: float = 0.0

    #: A Float specifying the distance in millimeters between the arrow end point and the arrow
    #: end head. The default value is 0.0.
    endGap: float = 0.0

    #: A String specifying the color of the arrow. Possible string values are any valid color.
    #: The default value is "White".
    color: str = "White"

    #: A SymbolicConstant specifying the line style of the arrow. Possible values are SOLID,
    #: DASHED, DOTTED, and DOT_DASH. The default value is SOLID.
    lineStyle: SymbolicConstant = SOLID

    #: A SymbolicConstant specifying the line thickness of the arrow. Possible values are
    #: VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.
    lineThickness: SymbolicConstant = VERY_THIN

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        startPoint: typing.Tuple[float, ...] = (0.0, 0.0),
        endPoint: typing.Tuple[float, ...] = (0.0, 0.0),
        startAnchor: typing.Union[SymbolicConstant, float] = BOTTOM_LEFT,
        endAnchor: typing.Union[SymbolicConstant, float] = BOTTOM_LEFT,
        startHeadStyle: SymbolicConstant = NONE,
        endHeadStyle: SymbolicConstant = FILLED_ARROW,
        startGap: float = 0.0,
        endGap: float = 0.0,
        color: str = "White",
        lineStyle: SymbolicConstant = SOLID,
        lineThickness: SymbolicConstant = VERY_THIN,
    ):
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
        super().__init__()
        self.name = name
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.startAnchor = startAnchor
        self.endAnchor = endAnchor
        self.startHeadStyle = startHeadStyle
        self.endHeadStyle = endHeadStyle
        self.startGap = startGap
        self.endGap = endGap
        self.color = color
        self.lineStyle = lineStyle
        self.lineThickness = lineThickness

    @abaqus_method_doc
    def translateStartPoint(self, x: float = None, y: float = None):
        """This method translates the start point of the Arrow object on the viewport plane.

        Parameters
        ----------
        x
            A Float specifying the **X** translation amount in millimeters.
        y
            A Float specifying the*Y* translation amount in millimeters.

        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def translateEndPoint(self, x: float = None, y: float = None):
        """This method translates the end point of the Arrow object on the viewport plane.

        Parameters
        ----------
        x
            A Float specifying the **X** translation amount in millimeters.
        y
            A Float specifying the*Y* translation amount in millimeters.

        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def setValues(
        self,
        startPoint: typing.Tuple[float, ...] = (0.0, 0.0),
        endPoint: typing.Tuple[float, ...] = (0.0, 0.0),
        startAnchor: typing.Union[SymbolicConstant, float] = BOTTOM_LEFT,
        endAnchor: typing.Union[SymbolicConstant, float] = BOTTOM_LEFT,
        startHeadStyle: SymbolicConstant = NONE,
        endHeadStyle: SymbolicConstant = FILLED_ARROW,
        startGap: float = 0.0,
        endGap: float = 0.0,
        color: str = "White",
        lineStyle: SymbolicConstant = SOLID,
        lineThickness: SymbolicConstant = VERY_THIN,
    ):
        """This method modifies the Arrow object.

        Parameters
        ----------
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

            The
            default value is BOTTOM_LEFT.
        endAnchor
            A SymbolicConstant or a sequence of Floats specifying a point. A sequence of two Floats
            specifies the **X**- and **Y**-coordinates as percentages of the viewport width and height.
            A Sequence of three Floats specifies the **X**-, **Y**-, and **Z**-coordinates of a point in
            the model coordinate system. A SymbolicConstant indicates a relative position. Possible
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

            The
            default value is BOTTOM_LEFT.
        startHeadStyle
            A SymbolicConstant specifying the style of the start head. Possible values
            are:

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
            A SymbolicConstant specifying the style of the end head. Possible values
            are:

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

        """
        super().setValues(
            startPoint=startPoint,
            endPoint=endPoint,
            startAnchor=startAnchor,
            endAnchor=endAnchor,
            startHeadStyle=startHeadStyle,
            endHeadStyle=endHeadStyle,
            startGap=startGap,
            endGap=endGap,
            color=color,
            lineStyle=lineStyle,
            lineThickness=lineThickness,
        )
