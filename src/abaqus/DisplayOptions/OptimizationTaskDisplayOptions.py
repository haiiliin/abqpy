from abaqusConstants import *


class OptimizationTaskDisplayOptions:
    """The OptimizationTaskDisplayOptions object stores settings that specify how assemblies
    are to be displayed in a particular viewport when
    session.viewports[name].assemblyDisplay.optimizationTasks=ON
    The OptimizationTaskDisplayOptions object has no constructor. When you create a new
    viewport, the settings are copied from the current viewport.

    Notes
    -----
    This object can be accessed by:

    .. code-block::

        session.viewports[name].assemblyDisplay.optimizationTaskOptions
        session.viewports[name].layers[name].assemblyDisplay.optimizationTaskOptions
    """

    def setValues(self, topologyTask: Boolean = ON, shapeTask: Boolean = ON):
        """This method modifies the OptimizationTaskDisplayOptions object.

        Parameters
        ----------
        topologyTask
            A Boolean specifying whether topology task symbols are shown. The default value is ON.
        shapeTask
            A Boolean specifying whether shape task symbols are shown. The default value is ON.

        Raises
        ------
        RangeError
        """
        pass
