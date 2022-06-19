from abaqusConstants import *


class StopConditionDisplayOptions:
    """The StopConditionDisplayOptions object stores settings that specify how assemblies are
    to be displayed in a particular viewport when
    session.viewports[name].assemblyDisplay.stopConditions=ON
    The StopConditionDisplayOptions object has no constructor. When you create a new
    viewport, the settings are copied from the current viewport.

    Notes
    -----
    This object can be accessed by:

    .. code-block::

        session.viewports[name].assemblyDisplay.stopConditionOptions
        session.viewports[name].layers[name].assemblyDisplay.stopConditionOptions
    """

    def setValues(self, localStopCondition: Boolean = ON):
        """This method modifies the StopConditionDisplayOptions object.

        Parameters
        ----------
        localStopCondition
            A Boolean specifying whether local stop condition symbols are shown. The default value
            is ON.

        Raises
        ------
        RangeError
        """
        pass
