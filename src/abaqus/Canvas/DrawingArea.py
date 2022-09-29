from typing import Optional, Tuple

from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class DrawingArea:
    """The DrawingArea object specifies the location and size of the drawing area used for
    placement of viewports.

    .. note::
        This object can be accessed by::

            session.drawingArea
    """

    #: A Float specifying the width in millimeters.
    width: Optional[float] = None

    #: A Float specifying the height in millimeters.
    height: Optional[float] = None

    #: A pair of Floats specifying the coordinates of the bottom left hand corner in
    #: millimeters.
    origin: Tuple[float, ...] = (0.0, 0.0)
