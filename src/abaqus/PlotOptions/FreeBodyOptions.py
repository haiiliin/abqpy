from typing_extensions import Literal
from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import (Boolean, MODEL_SIZE, OFF, ON, RESULTANT, SCIENTIFIC,
                                              SymbolicConstant)
from .._OptionsBase import _OptionsBase


@abaqus_class_doc
class FreeBodyOptions(_OptionsBase):
    """The FreeBodyOptions object stores values and attributes associated with a free body
    plot. The FreeBodyOptions object has no constructor command. Abaqus creates a
    *defaultOdbDisplay.freeBodyOptions* member when you import the Visualization module.
    Abaqus creates a **FreeBodyOptions** member when it creates the OdbDisplay object, using
    the values from *defaultOdbDisplay.freeBodyOptions*. Abaqus creates the **odbDisplay**
    member when a viewport is created, using the values from **defaultOdbDisplay**.
    FreeBodyOptions objects are accessed in one of two ways:
    - The default free body options. These settings are used as defaults when other
    **freeBodyOptions** members are created. These settings can be set to customize user
    preferences.
    - The free body options associated with a particular viewport.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.defaultOdbDisplay.freeBodyOptions
            session.viewports[name].layers[name].odbDisplay.freeBodyOptions
            session.viewports[name].odbDisplay.freeBodyOptions
    """

    @abaqus_method_doc
    def setValues(
        self,
        *,
        comp1ColorF: str = "",
        comp1ColorM: str = "",
        comp2ColorF: str = "",
        comp2ColorM: str = "",
        comp3ColorF: str = "",
        comp3ColorM: str = "",
        resultantColorF: str = "",
        resultantColorM: str = "",
        textColorF: str = "",
        textColorM: str = "",
        textFontF: str = "",
        textFontM: str = "",
        numberFormatF: Literal[C.SCIENTIFIC, C.ENGINEERING, C.FIXED] = SCIENTIFIC,
        numberFormatM: Literal[C.SCIENTIFIC, C.ENGINEERING, C.FIXED] = SCIENTIFIC,
        scaleModeF: Literal[C.SCREEN_SIZE, C.MODEL_SIZE] = MODEL_SIZE,
        scaleModeM: Literal[C.SCREEN_SIZE, C.MODEL_SIZE] = MODEL_SIZE,
        vectorDisplay: Literal[C.RESULTANT, C.COMPONENT] = RESULTANT,
        numDigitsF: int = 3,
        numDigitsM: int = 3,
        sizePercentageF: float = 10,
        sizePercentageM: float = 10,
        thresholdF: Optional[float] = None,
        thresholdM: Optional[float] = None,
        drawLabelF: Boolean = ON,
        drawLabelM: Boolean = ON,
        showComp1F: Boolean = ON,
        showComp1M: Boolean = ON,
        showComp2F: Boolean = ON,
        showComp2M: Boolean = ON,
        showComp3F: Boolean = ON,
        showComp3M: Boolean = ON,
        showForce: Boolean = ON,
        showMoment: Boolean = ON,
        constantLengthArrow: Boolean = OFF,
    ):
        """This method modifies the FreeBodyOptions object.

        Parameters
        ----------
        comp1ColorF
            A String specifying color of the first force component. The default value is "#FF1932".
        comp1ColorM
            A String specifying color of the first moment component. The default value is "#0000FF".
        comp2ColorF
            A String specifying color of the second force component. The default value is "#FF1932".
        comp2ColorM
            A String specifying color of the second moment component. The default value is
            "#0000FF".
        comp3ColorF
            A String specifying color of the third force component. The default value is "#FF1932".
        comp3ColorM
            A String specifying color of the third moment component. The default value is "#0000FF".
        resultantColorF
            A String specifying color of the resultant force. The default value is "#FF1932".
        resultantColorM
            A String specifying color of the resultant moment. The default value is "#0000FF".
        textColorF
            A String specifying text color for force. The default value is "Yellow".
        textColorM
            A String specifying text color for moment. The default value is "Yellow".
        textFontF
            A String specifying text font for force. The default value is "verdana".
        textFontM
            A String specifying text font for moment. The default value is "verdana".
        numberFormatF
            A SymbolicConstant specifying the number format for force. Possible values are
            SCIENTIFIC, FIXED, and ENGINEERING. The default value is SCIENTIFIC.
        numberFormatM
            A SymbolicConstant specifying the number format for moment. Possible values are
            SCIENTIFIC, FIXED, and ENGINEERING. The default value is SCIENTIFIC.
        scaleModeF
            A SymbolicConstant specifying the size scaling mode for force. Possible values are
            MODEL_SIZE and SCREEN_SIZE. The default value is MODEL_SIZE.
        scaleModeM
            A SymbolicConstant specifying the size scaling mode for moment. Possible values are
            MODEL_SIZE and SCREEN_SIZE. The default value is MODEL_SIZE.
        vectorDisplay
            A SymbolicConstant specifying the vector display mode. Possible values are RESULTANT and
            COMPONENT. The default value is RESULTANT.
        numDigitsF
            An Int specifying the number of digits in the force label. The default value is 3.
        numDigitsM
            An Int specifying the number of digits in the moment label. The default value is 3.
        sizePercentageF
            A Float specifying the size of the force symbol as a percentage of the screen or model.
            The default value is 10.0.
        sizePercentageM
            A Float specifying the size of the moment symbol as a percentage of the screen or model.
            The default value is 10.0.
        thresholdF
            A Float specifying the force threshold value. The default value is 10-6.
        thresholdM
            A Float specifying the moment threshold value. The default value is 10-6.
        drawLabelF
            A Boolean specifying whether to draw force labels. The default value is ON.
        drawLabelM
            A Boolean specifying whether to draw moment labels. The default value is ON.
        showComp1F
            A Boolean specifying whether to show the first force component. The default value is ON.
        showComp1M
            A Boolean specifying whether to show the first moment component. The default value is
            ON.
        showComp2F
            A Boolean specifying whether to show the second force component. The default value is
            ON.
        showComp2M
            A Boolean specifying whether to show the second moment component. The default value is
            ON.
        showComp3F
            A Boolean specifying whether to show the third force component. The default value is ON.
        showComp3M
            A Boolean specifying whether to show the third moment component. The default value is
            ON.
        showForce
            A Boolean specifying whether to show forces. The default value is ON.
        showMoment
            A Boolean specifying whether to show moments. The default value is ON.
        constantLengthArrow
            A Boolean specifying whether to use a constant length for all arrows. The default value
            is OFF.
        """
        ...
