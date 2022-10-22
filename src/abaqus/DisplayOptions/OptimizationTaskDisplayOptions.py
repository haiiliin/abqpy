from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import Boolean, ON


@abaqus_class_doc
class OptimizationTaskDisplayOptions:
    """The OptimizationTaskDisplayOptions object stores settings that specify how assemblies
    are to be displayed in a particular viewport when
    session.viewports[name].assemblyDisplay.optimizationTasks=ON
    The OptimizationTaskDisplayOptions object has no constructor. When you create a new
    viewport, the settings are copied from the current viewport.

    .. note::
        This object can be accessed by::

            session.viewports[name].assemblyDisplay.optimizationTaskOptions
            session.viewports[name].layers[name].assemblyDisplay.optimizationTaskOptions
    """

    @abaqus_method_doc
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
        ...
