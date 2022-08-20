from ..UtilityAndView.abaqusConstants import *
from .._decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class OdbDataFrame:
    """The OdbDataFrame object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import visualization
            session.odbData[name].steps[i].frames[i]
    """

    @abaqus_method_doc
    def setValues(self, activateFrame: Boolean, update: Boolean = OFF):
        """This method modifies the OdbDataFrame object.

        Parameters
        ----------
        activateFrame
            A Boolean specifying whether to activate the frame.
        update
            A Boolean specifying whether to update the model. The default value is ON
        """
        # TODO: Implement this method
        ...
