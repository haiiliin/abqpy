from abaqusConstants import *


class OdbDataFrame:
    """The OdbDataFrame object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import visualization
            session.odbData[name].steps[i].frames[i]
    """

    def setValues(self, activateFrame: Boolean, update: Boolean = OFF):
        """This method modifies the OdbDataFrame object.

        Parameters
        ----------
        activateFrame
            A Boolean specifying whether to activate the frame.
        update
            A Boolean specifying whether to update the model. The default value is ON
        """
        pass
