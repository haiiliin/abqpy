from abaqusConstants import *


class DisplayGroupInstanceRepository:
    """The DisplayGroupInstanceRepository object stores DisplayGroupInstance objects. In
    addition to all the standard Python repository methods, the DisplayGroupInstance
    repository defines additional methods as described below.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import visualization
            session.viewports[name].layers[name].odbDisplay.displayGroupInstances
            session.viewports[name].odbDisplay.displayGroupInstances
    """

    def syncOptions(self, name: str, updateInstances: Boolean = ON):
        """This method synchronizes the display options stored on the OdbDisplay object with the
        display options stored on the DisplayGroupInstance object.

        Parameters
        ----------
        name
            A String specifying the repository key.
        updateInstances
            A Boolean specifying whether to synchronize the display options on all the
            DisplayGroupInstance objects stored in the DisplayGroupInstanceRepository for which
            **lockOptions** is OFF. The default value of **updateInstances** is ON.
        """
        pass
