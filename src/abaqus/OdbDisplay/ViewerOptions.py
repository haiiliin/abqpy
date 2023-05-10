from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import ON, Boolean


@abaqus_class_doc
class ViewerOptions:
    """The ViewerOptions object specifies options to set the result caching parameters. The ViewerOptions object
    has no constructor. Abaqus creates the **viewerOptions** member when a session is started.

    .. note::
        This object can be accessed by::

            import visualization
            session.viewerOptions
    """

    @abaqus_method_doc
    def setValues(
        self,
        primaryVariableCaching: Boolean = ON,
        deformedVariableCaching: Boolean = ON,
        cutVariableCaching: Boolean = ON,
        odbUpdateChecking: Boolean = ON,
        odbUpdateCheckInterval: int = 0,
    ):
        """This method modifies the ViewerOptions object.

        Parameters
        ----------
        primaryVariableCaching
            A Boolean specifying whether results are currently cached. Caching improves the
            performance of subsequent access. The default value is ON.
        deformedVariableCaching
            A Boolean specifying whether deformation vectors are currently cached. Caching improves
            the performance of subsequent access. The default value is ON.
        cutVariableCaching
            A Boolean specifying whether the values used for displaying cut models are currently
            cached. Caching improves the performance of subsequent access. The default value is ON.
        odbUpdateChecking
            A Boolean specifying whether the current .odb file should be checked for updates.
            Setting **odbUpdateChecking** to OFF can improve Viewer performance when accessing data
            from a remote file. The default value is ON.
        odbUpdateCheckInterval
            An Int specifying the minimum time between status checks (in seconds). The default value
            is 0.
        """
        ...
