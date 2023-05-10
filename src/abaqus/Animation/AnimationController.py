from typing import Optional

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .._OptionsBase import _OptionsBase
from ..UtilityAndView.abaqusConstants import NONE, STOP, UNLIMITED, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class AnimationController(_OptionsBase):
    """The AnimationController object controls all object-based animation to be displayed in
    the viewports. The AnimationController object has no constructor. Abaqus creates the
    **animationController** member when it creates the Session object.

    .. note::
        This object can be accessed by::

            import animation
            session.viewports[name].animationController
    """

    #: A SymbolicConstant specifying the type of movie to play. Possible values are
    #: SCALE_FACTOR, HARMONIC, TIME_HISTORY, and NONE. The default value is NONE.
    animationType: SymbolicConstant = NONE

    #: A SymbolicConstant specifying the state of the animation controller. Possible values are
    #: STOP and PLAY. The default value is STOP.
    state: SymbolicConstant = STOP

    @abaqus_method_doc
    def play(self, duration: Literal[C.UNLIMITED] = UNLIMITED):
        """This method begins the animation.

        Parameters
        ----------
        duration
            The SymbolicConstant UNLIMITED or an Int specifying how many seconds to play the
            animation. The default value is UNLIMITED.

        Raises
        ------
        AnimationError
            animationType not set, If **animationType** = NONE:
        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def stop(self):
        """This method stops the animation."""
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def incrementFrame(self):
        """This method increments the animation frame."""
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def decrementFrame(self):
        """This method decrements the animation frame."""
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def showFrame(self, frame: Optional[int] = None, value: Optional[float] = None):
        """This method renders the specified frame of the animation.

        Parameters
        ----------
        frame
            An Int specifying the frame number.
        value
            A Float specifying the frame: for **animationType** = TIME_HISTORY the frame with the time
            nearest to this value, for **animationType** = HARMONIC the frame with the angle nearest to
            this value, for **animationType** = SCALE_FACTOR the frame with the scale value nearest to
            this value.
        """
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def showFirstFrame(self):
        """This method renders the first frame of the animation."""
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def showLastFrame(self):
        """This method renders the last frame of the animation."""
        # TODO: implement this method
        ...

    @abaqus_method_doc
    def setValues(self, animationType: Literal[C.HARMONIC, C.SCALE_FACTOR, C.TIME_HISTORY, C.NONE] = NONE):
        """This method modifies the AnimationController object.

        Parameters
        ----------
        animationType
            A SymbolicConstant specifying the type of movie to play. Possible values are
            SCALE_FACTOR, HARMONIC, TIME_HISTORY, and NONE. The default value is NONE.

        Raises
        ------
        RangeError
        """
        super().setValues(animationType=animationType)
