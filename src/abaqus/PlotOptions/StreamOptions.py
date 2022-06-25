from abaqusConstants import *


class StreamOptions:
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
        This object can be accessed by:

        .. code-block:: python

            import visualization
            session.defaultOdbDisplay.streamOptions
            session.viewports[name].layers[name].odbDisplay.streamOptions
            session.viewports[name].odbDisplay.streamOptions
    """

    def setValues(
        self,
        colorMethod: SymbolicConstant = UNIFORM,
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
        pass
