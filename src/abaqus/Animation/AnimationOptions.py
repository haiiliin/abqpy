from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ..UtilityAndView.abaqusConstants import (
    Boolean,
    DEFAULT,
    FRAME_BASED,
    HALF_CYCLE,
    LOOP,
    MEDIUM,
    ON,
    SOLID,
    SymbolicConstant,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .._OptionsBase import _OptionsBase


@abaqus_class_doc
class AnimationOptions(_OptionsBase):
    """The AnimationOptions object is used to store values and attributes associated with an
    AnimationController object.
    The AnimationOptions object has no constructor command. Abaqus creates the
    **animationOptions** member when it creates the AnimationController object.

    .. note::
        This object can be accessed by::

            import animation
            session.animationOptions
    """

    #: A SymbolicConstant specifying the animation mode. Possible values are PLAY_ONCE, LOOP,
    #: LOOP_BACKWARD, and SWING. The default value is LOOP.
    mode: SymbolicConstant = LOOP

    #: An Int specifying the animation rate in frames/second. Possible values are 1 ≤
    #: **frameRate** ≤ 100. The default value is 50.
    frameRate: int = 50

    #: A Boolean specifying whether to show the frame counter. The default value is ON.
    frameCounter: Boolean = ON

    #: A SymbolicConstant specifying the relative scaling when the AnimationController object's
    #: **animationType** = SCALE_FACTOR or HARMONIC. Possible values are FULL_CYCLE and HALF_CYCLE.
    #: The default value is HALF_CYCLE.
    relativeScaling: SymbolicConstant = HALF_CYCLE

    #: An Int specifying the number of frames to be used when the AnimationController object's
    #: **animationType** = SCALE_FACTOR or HARMONIC. The default value is 7.
    numScaleFactorFrames: int = 7

    #: A SymbolicConstant specifying whether the time history animation is time based or frame
    #: based. Possible values are FRAME_BASED and TIME_BASED. The default value is FRAME_BASED.
    timeHistoryMode: SymbolicConstant = FRAME_BASED

    #: A Float specifying the maximum time for time based time history animation when
    #: **maxTimeAutoCompute** = False.
    maxTime: Optional[float] = None

    #: A Boolean specifying whether the animation maximum time value should be computed from
    #: the active frames when **timeHistoryMode** is set to TIME_BASED. The default value is ON.
    maxTimeAutoCompute: Boolean = ON

    #: A Float specifying the maximum time when **timeHistoryMode** is set to TIME_BASED and the
    #: **maxTimeAutoCompute** value is True. This value is computed as the maximum time of all
    #: active frames displayed in viewports where the animation is active.
    maxTimeAutoValue: Optional[float] = None

    #: A Float specifying the minimum time for time based time history animation when
    #: **minTimeAutoCompute** = False.
    minTime: Optional[float] = None

    #: A Boolean specifying whether the animation minimum time value should be computed from
    #: the active frames when **timeHistoryMode** is set to TIME_BASED. The default value is ON.
    minTimeAutoCompute: Boolean = ON

    #: A Float specifying the minimum time when **timeHistoryMode** is set to TIME_BASED and the
    #: **minTimeAutoCompute** value is True. This value is computed as the minimum time of all
    #: active frames displayed in viewports where the animation is active.
    minTimeAutoValue: Optional[float] = None

    #: A Float specifying the time increment for frame selection when **timeHistoryMode** is set
    #: to TIME_BASED.
    timeIncrement: Optional[float] = None

    #: A Boolean specifying whether to use the highlight method to draw the time tracker line
    #: and symbols. The default value is ON.
    xyUseHighlightMethod: Boolean = ON

    #: A Boolean specifying whether to show the time tracker line. The default value is ON.
    xyShowLine: Boolean = ON

    #: A SymbolicConstant specifying the **X - Y** time tracker line style. Possible values are
    #: SOLID, DASHED, DOTTED, and DOT_DASH. The default value is SOLID.
    xyLineStyle: SymbolicConstant = SOLID

    #: A SymbolicConstant specifying the **X - Y** time tracker line thickness. Possible values are
    #: VERY_THIN, THIN, MEDIUM, and THICK. The default value is MEDIUM.
    xyLineThickness: SymbolicConstant = MEDIUM

    #: A Boolean specifying whether to show the time tracker symbols. The default value is ON.
    xyShowSymbol: Boolean = ON

    #: A SymbolicConstant specifying the marker type to be used for all animation capable **X - Y**
    #: curve or the SymbolicConstant DEFAULT specifying that the system will take the marker
    #: associated to each curve Possible values are:
    #:
    #: - FILLED_CIRCLE
    #: - FILLED_SQUARE
    #: - FILLED_DIAMOND
    #: - FILLED_TRI
    #: - HOLLOW_CIRCLE
    #: - HOLLOW_SQUARE
    #: - HOLLOW_DIAMOND
    #: - HOLLOW_TRI
    #: - CROSS
    #: - XMARKER
    #: - DEFAULT
    #:
    #: The default value is DEFAULT.
    xySymbolMarker: SymbolicConstant = DEFAULT

    #: A SymbolicConstant specifying the size of the markers. Possible values are SMALL,
    #: MEDIUM, and LARGE. The default value is MEDIUM.
    xySymbolSize: SymbolicConstant = MEDIUM

    #: A String specifying the color used to plot the **X - Y** time tracker line when
    #: **xyUseHighlightMethod** = False. The default value is "Yellow".
    xyLineColor: str = ""

    #: A String specifying the color used to plot **X - Y** time tracker symbols when
    #: **xyUseHighlightMethod** = False. When setting the color to 'Default' the system will take
    #: the color associated to each curve. The default value is "Default".
    xySymbolColor: str = ""

    @abaqus_method_doc
    def setValues(
        self,
        mode: Literal[C.LOOP, C.SWING, C.PLAY_ONCE, C.LOOP_BACKWARD] = LOOP,
        frameRate: int = 50,
        frameCounter: Boolean = ON,
        relativeScaling: Literal[C.HARMONIC, C.SCALE_FACTOR, C.HALF_CYCLE, C.FULL_CYCLE] = HALF_CYCLE,
        numScaleFactorFrames: int = 7,
        timeHistoryMode: Literal[C.FRAME_BASED, C.TIME_BASED] = FRAME_BASED,
        maxTime: Optional[float] = None,
        maxTimeAutoCompute: Boolean = ON,
        minTime: Optional[float] = None,
        minTimeAutoCompute: Boolean = ON,
        timeIncrement: Optional[float] = None,
        xyUseHighlightMethod: Boolean = ON,
        xyShowLine: Boolean = ON,
        xyLineStyle: Literal[C.DASHED, C.SOLID, C.DOT_DASH, C.DOTTED] = SOLID,
        xyLineThickness: Literal[C.THIN, C.THICK, C.VERY_THIN, C.MEDIUM] = MEDIUM,
        xyLineColor: str = "",
        xyShowSymbol: Boolean = ON,
        xySymbolMarker: Literal[
            C.CROSS,
            C.FILLED_DIAMOND,
            C.FILLED_SQUARE,
            C.HOLLOW_CIRCLE,
            C.HOLLOW_TRI,
            C.HOLLOW_SQUARE,
            C.DEFAULT,
            C.FILLED_TRI,
            C.HOLLOW_DIAMOND,
            C.FILLED_CIRCLE,
            C.XMARKER,
        ] = DEFAULT,
        xySymbolSize: Literal[C.SMALL, C.LARGE, C.MEDIUM] = MEDIUM,
        xySymbolColor: str = "",
    ):
        """This method modifies the AnimationOptions object.

        Parameters
        ----------
        mode
            A SymbolicConstant specifying the animation mode. Possible values are PLAY_ONCE, LOOP,
            LOOP_BACKWARD, and SWING. The default value is LOOP.
        frameRate
            An Int specifying the animation rate in frames/second. Possible values are 1 ≤
            **frameRate** ≤ 100. The default value is 50.
        frameCounter
            A Boolean specifying whether to show the frame counter. The default value is ON.
        relativeScaling
            A SymbolicConstant specifying the relative scaling when the AnimationController object's
            **animationType** = SCALE_FACTOR or HARMONIC. Possible values are FULL_CYCLE and HALF_CYCLE.
            The default value is HALF_CYCLE.
        numScaleFactorFrames
            An Int specifying the number of frames to be used when the AnimationController object's
            **animationType** = SCALE_FACTOR or HARMONIC. The default value is 7.
        timeHistoryMode
            A SymbolicConstant specifying whether the time history animation is time based or frame
            based. Possible values are FRAME_BASED and TIME_BASED. The default value is FRAME_BASED.
        maxTime
            A Float specifying the maximum time for time based time history animation when
            **maxTimeAutoCompute** = False.
        maxTimeAutoCompute
            A Boolean specifying whether the animation maximum time value should be computed from
            the active frames when **timeHistoryMode** is set to TIME_BASED. The default value is ON.
        minTime
            A Float specifying the minimum time for time based time history animation when
            **minTimeAutoCompute** = False.
        minTimeAutoCompute
            A Boolean specifying whether the animation minimum time value should be computed from
            the active frames when **timeHistoryMode** is set to TIME_BASED. The default value is ON.
        timeIncrement
            A Float specifying the time increment for frame selection when **timeHistoryMode** is set
            to TIME_BASED.
        xyUseHighlightMethod
            A Boolean specifying whether to use the highlight method to draw the time tracker line
            and symbols. The default value is ON.
        xyShowLine
            A Boolean specifying whether to show the time tracker line. The default value is ON.
        xyLineStyle
            A SymbolicConstant specifying the **X - Y** time tracker line style. Possible values are
            SOLID, DASHED, DOTTED, and DOT_DASH. The default value is SOLID.
        xyLineThickness
            A SymbolicConstant specifying the **X - Y** time tracker line thickness. Possible values are
            VERY_THIN, THIN, MEDIUM, and THICK. The default value is MEDIUM.
        xyLineColor
            A String specifying the color used to plot the **X - Y** time tracker line when
            **xyUseHighlightMethod** = False. The default value is "Yellow".
        xyShowSymbol
            A Boolean specifying whether to show the time tracker symbols. The default value is ON.
        xySymbolMarker
            A SymbolicConstant specifying the marker type to be used for all animation capable **X - Y**
            curve or the SymbolicConstant DEFAULT specifying that the system will take the marker
            associated to each curve Possible values are:

            - FILLED_CIRCLE
            - FILLED_SQUARE
            - FILLED_DIAMOND
            - FILLED_TRI
            - HOLLOW_CIRCLE
            - HOLLOW_SQUARE
            - HOLLOW_DIAMOND
            - HOLLOW_TRI
            - CROSS
            - XMARKER
            - DEFAULT

            The default value is DEFAULT.
        xySymbolSize
            A SymbolicConstant specifying the size of the markers. Possible values are SMALL,
            MEDIUM, and LARGE. The default value is MEDIUM.
        xySymbolColor
            A String specifying the color used to plot **X - Y** time tracker symbols when
            **xyUseHighlightMethod** = False. When setting the color to 'Default' the system will take
            the color associated to each curve. The default value is "Default".
        """
        super().setValues(
            mode=mode,
            frameRate=frameRate,
            frameCounter=frameCounter,
            relativeScaling=relativeScaling,
            numScaleFactorFrames=numScaleFactorFrames,
            timeHistoryMode=timeHistoryMode,
            maxTime=maxTime,
            maxTimeAutoCompute=maxTimeAutoCompute,
            minTime=minTime,
            minTimeAutoCompute=minTimeAutoCompute,
            timeIncrement=timeIncrement,
            xyUseHighlightMethod=xyUseHighlightMethod,
            xyShowLine=xyShowLine,
            xyLineStyle=xyLineStyle,
            xyLineThickness=xyLineThickness,
            xyLineColor=xyLineColor,
            xyShowSymbol=xyShowSymbol,
            xySymbolMarker=xySymbolMarker,
            xySymbolSize=xySymbolSize,
            xySymbolColor=xySymbolColor,
        )
