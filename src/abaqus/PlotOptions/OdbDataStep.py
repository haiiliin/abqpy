from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .OdbDataFrameArray import OdbDataFrameArray
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class OdbDataStep:
    """The OdbDataStep object.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.odbData[name].steps[i]
    """

    #: An :py:class:`~abaqus.PlotOptions.OdbDataFrameArray.OdbDataFrameArray` object specifying the list of frames. The list is read-only.
    frames: OdbDataFrameArray = []

    @abaqus_method_doc
    def setValues(self, activateFrames: Boolean, update: Boolean = OFF):
        """This method modifies the OdbDataStep object.

        Parameters
        ----------
        activateFrames
            A Boolean specifying whether to activate all the frames in the step.
        update
            A Boolean specifying whether to update the model. The default value is ON
        """
        # TODO: Implement this method
        ...
