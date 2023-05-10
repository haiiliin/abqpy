from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .._OptionsBase import _OptionsBase
from ..UtilityAndView.abaqusConstants import OFF, UNIFORM, Boolean
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class StreamOptions(_OptionsBase):
    """The StreamOptions object stores values and attributes associated with a stream plot. The
    StreamOptions object has no constructor command. Abaqus creates a
    *defaultOdbDisplay.streamOptions* member when you import the Visualization module.
    Abaqus creates a **StreamOptions** member when it creates the OdbDisplay object, using the
    values from *defaultOdbDisplay.streamOptions*. Abaqus creates the **odbDisplay** member
    when a viewport is created, using the values from **defaultOdbDisplay**.
    StreamOptions objects are accessed in one of two ways:

    - The default stream options. These settings are used as defaults when other
      **streamOptions** members are created. These settings can be set to customize user
      preferences.
    - The stream options associated with a particular viewport.

    .. note::
        This object can be accessed by::

            import visualization
            session.defaultOdbDisplay.streamOptions
            session.viewports[name].layers[name].odbDisplay.streamOptions
            session.viewports[name].odbDisplay.streamOptions
    """

    @abaqus_method_doc
    def setValues(
        self,
        *,
        colorMethod: Literal[C.SPECTRUM, C.UNIFORM, C.CONTINUOUS] = UNIFORM,
        uniformColor: str = "",
        lineThickness: float = 6,
        showArrow: Boolean = OFF,
        numArrows: int = 10,
    ):
        """This method modifies the StreamOptions object.

        Parameters
        ----------
        colorMethod
            A SymbolicConstant specifying the method for coloring stream lines. Possible values are
            UNIFORM, SPECTRUM, and CONTINUOUS. The default value is UNIFORM.
        uniformColor
            A String specifying uniform color of the stream lines. The default value is "#FFFF00".
        lineThickness
            A Float specifying the stream line thickness. The default value is 6.0.
        showArrow
            A Boolean specifying whether to show arrows. The default value is OFF.
        numArrows
            An Int specifying the number of arrows on each stream line. The default value is 10.
        """
        super().setValues(
            colorMethod=colorMethod,
            uniformColor=uniformColor,
            lineThickness=lineThickness,
            showArrow=showArrow,
            numArrows=numArrows,
        )
