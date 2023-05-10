from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .._OptionsBase import _OptionsBase
from ..UtilityAndView.abaqusConstants import OFF, ON, Boolean


@abaqus_class_doc
class ImageAnimationOptions(_OptionsBase):
    """The ImageAnimationOptions object is used to store values and attributes associated with saving viewport
    animations. The ImageAnimationOptions object has no constructor. Abaqus creates the
    **imageAnimationOptions** member when the animation module is imported.

    .. note::
        This object can be accessed by::

            import animation
            session.imageAnimationOptions
    """

    #: An Int specifying the frame rate to record on the saved animation file. The effective
    #: frame rate in frames per second will be obtained by dividing the given frame rate by the
    #: time scale.
    frameRate: Optional[int] = None

    #: An Int specifying the time scale to apply to the frame rate.
    vpDecorations: Boolean = ON

    #: A Boolean specifying whether to capture viewport backgrounds. The default value is OFF.
    vpBackground: Boolean = OFF

    #: A Boolean specifying whether to capture the view compass. The default value is OFF.
    compass: Boolean = OFF

    @abaqus_method_doc
    def setValues(
        self,
        frameRate: Optional[int] = None,
        timeScale: Optional[int] = None,
        vpDecorations: Boolean = ON,
        vpBackground: Boolean = OFF,
        compass: Boolean = OFF,
    ):
        """This method modifies the ImageAnimationOptions object.

        Parameters
        ----------
        frameRate
            An Int specifying the frame rate to record on the saved animation file. The effective
            frame rate in frames per second will be obtained by dividing the given frame rate by the
            time scale.
        timeScale
            An Int specifying the time scale to apply to the frame rate.
        vpDecorations
            A Boolean specifying whether to capture the viewport border and title. The default value
            is ON.
        vpBackground
            A Boolean specifying whether to capture viewport backgrounds. The default value is OFF.
        compass
            A Boolean specifying whether to capture the view compass. The default value is OFF.
        """
        super().setValues(
            frameRate=frameRate,
            timeScale=timeScale,
            vpDecorations=vpDecorations,
            vpBackground=vpBackground,
            compass=compass,
        )
