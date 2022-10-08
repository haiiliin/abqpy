from typing import Optional, Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import (BEST_FIT, Boolean, CENTER, FIT_TO_VIEWPORT, OFF,
                                              SymbolicConstant)
from .._OptionsBase import _CopyOptionsBase


@abaqus_class_doc
class MovieOptions(_CopyOptionsBase):
    """The MovieOptions object stores settings that control how the movie background for an
    animation is rendered in a particular viewport. MovieOptions objects are accessed from
    the movie options associated with a particular viewport.
    The MovieOptions object has no constructor; Abaqus creates the **movieOptions** member for
    a viewport when the viewport is created using the values in the **movieOptions** member of
    the current viewport.

    .. note::
        This object can be accessed by::

            session.viewports[name].movieOptions
    """
    #: A String specifying the name of the movie. A list of valid movie names is in the
    #: **movies** repository in the **session** object.
    movieName: str = ""

    #: A Boolean specifying whether a movie should be displayed in the viewport during an
    #: animation. The default value is OFF.
    showMovie: Boolean = OFF

    #: A SymbolicConstant specifying which positioning method is used to determine how the
    #: image will be scaled and positioned in the viewport. Possible values are:
    #:
    #: - FIT_TO_VIEWPORT, specifying a display mode where the image is scaled to fit in the
    #:   viewport using the specified **fitMethod**.
    #: - AUTO_ALIGN, specifying a display mode where the
    #:   image is scaled as specified by **xScale** and **yScale** and then positioned in the
    #:   viewport using the specified **alignment**.
    #: - MANUAL, specifying a display mode where the
    #:   image is scaled as specified by **xScale** and **yScale** and then positioned in the
    #:   viewport using the specified **origin**.
    #:
    #: The default value is FIT_TO_VIEWPORT.
    positionMethod: SymbolicConstant = FIT_TO_VIEWPORT

    #: A SymbolicConstant specifying which type of fit is performed to scale and position the
    #: image in the viewport. Possible values are:
    #:
    #: - BEST_FIT, specifying a mode where the image is scaled to completely fit within the
    #:   viewport.
    #: - FIT_WIDTH, specifying a mode where the image width is scaled to match the
    #:   viewport width.
    #: - FIT_HEIGHT, specifying a mode where the image height is scaled to match
    #:   the viewport height.
    #:
    #: The default value is BEST_FIT.
    fitMethod: SymbolicConstant = BEST_FIT

    #: A SymbolicConstant specifying the relative position of the image in the viewport when
    #: **positionMethod** =AUTO_ALIGN. Possible values are:
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
    #: The default value is CENTER.
    alignment: SymbolicConstant = CENTER

    #: A Float specifying the scale applied to the image width. The **xScale** argument is
    #: ignored when **positionMethod** =FIT_TO_VIEWPORT. The default value is 1.0.When **xScale**
    #: is negative, the image is mirrored about its y-axis but its position is not affected.
    xScale: float = 1.0

    #: A Float specifying the scale applied to the image height. The **yScale** argument is
    #: ignored when **positionMethod** =FIT_TO_VIEWPORT. The default value is 1.0.When **yScale**
    #: is negative, the image is mirrored about its x-axis but its position is not affected.
    yScale: float = 1.0

    #: A pair of Floats specifying the **X**- and **Y**-offsets in millimeters from the lower-left
    #: corner of the viewport. The **origin** argument is ignored unless **positionMethod**
    #: =MANUAL. The default value is (0, 0).
    origin: Sequence[float] = (0.0, 0.0)

    #: A Float specifying the translucency factor to use when displaying the image. Possible
    #: values are 0.0 ≤ **translucency** ≤ 1.0 with 0.0 being invisible and 1.0 being opaque.
    #: The default value is 1.0.
    translucency: float = 1.0

    @abaqus_method_doc
    def setValues(
        self,
        movieName: str = "",
        showMovie: Boolean = OFF,
        positionMethod: SymbolicConstant = FIT_TO_VIEWPORT,
        fitMethod: SymbolicConstant = BEST_FIT,
        alignment: SymbolicConstant = CENTER,
        xScale: float = 1.0,
        yScale: float = 1.0,
        origin: Sequence[float] = (0.0, 0.0),
        translucency: float = 1.0,
        options: Optional[str] = None,
    ):
        """This method modifies the MovieOptions object.

        Parameters
        ----------
        movieName
            A String specifying the name of the movie. A list of valid movie names is in the
            **movies** repository in the **session** object.
        showMovie
            A Boolean specifying whether a movie should be displayed in the viewport during an
            animation. The default value is OFF.
        positionMethod
            A SymbolicConstant specifying which positioning method is used to determine how the
            image will be scaled and positioned in the viewport. Possible values are:

            - FIT_TO_VIEWPORT, specifying a display mode where the image is scaled to fit in the
              viewport using the specified **fitMethod**.
            - AUTO_ALIGN, specifying a display mode where the
              image is scaled as specified by **xScale** and **yScale** and then positioned in the
              viewport using the specified **alignment**.
            - MANUAL, specifying a display mode where the
              image is scaled as specified by **xScale** and **yScale** and then positioned in the
              viewport using the specified **origin**.

            The default value is FIT_TO_VIEWPORT.
        fitMethod
            A SymbolicConstant specifying which type of fit is performed to scale and position the
            image in the viewport when **positionMethod** =FIT_TO_VIEWPORT. Possible values are:

            - BEST_FIT, specifying a mode where the image is scaled to completely fit within the
              viewport.
            - FIT_WIDTH, specifying a mode where the image width is scaled to match the
              viewport width.
            - FIT_HEIGHT, specifying a mode where the image height is scaled to match
              the viewport height.

            The default value is BEST_FIT.
        alignment
            A SymbolicConstant specifying the relative position of the image in the viewport when
            **positionMethod** =AUTO_ALIGN. Possible values are:

            - BOTTOM_LEFT
            - BOTTOM_CENTER
            - BOTTOM_RIGHT
            - CENTER_LEFT
            - CENTER
            - CENTER_RIGHT
            - TOP_LEFT
            - TOP_CENTER
            - TOP_RIGHT

            The default value is CENTER.
        xScale
            A Float specifying the scale applied to the movie frame width. The **xScale** argument is
            ignored when **positionMethod** =FIT_TO_VIEWPORT. The default value is 1.0.When **xScale**
            is negative, the movie frame is mirrored about its y-axis but its position is not
            affected.
        yScale
            A Float specifying the scale applied to the movie frame height. The **yScale** argument is
            ignored when **positionMethod** =FIT_TO_VIEWPORT. The default value is 1.0.When **yScale**
            is negative, the movie frame is mirrored about its x-axis but its position is not
            affected.
        origin
            A pair of Floats specifying the*X*- and **Y**-offsets in millimeters from the lower-left
            corner of the viewport. The **origin** argument is ignored unless **positionMethod**
            =MANUAL. The default value is (0, 0).
        translucency
            A Float specifying the translucency factor to use when displaying the movie frame.
            Possible values are 0.0 ≤ **translucency** ≤ 1.0 with 0.0 being invisible and 1.0 being
            opaque. The default value is 1.0.
        options
            None or a MovieOptions object specifying the object from which values are to be copied.
            If other arguments are also supplied to setValues, they will override the values in the
            **options** member. The default value is None.

        Raises
        ------
        RangeError
        """
        super().setValues(
            options=options,
            movieName=movieName,
            showMovie=showMovie,
            positionMethod=positionMethod,
            fitMethod=fitMethod,
            alignment=alignment,
            xScale=xScale,
            yScale=yScale,
            origin=origin,
            translucency=translucency,
        )
