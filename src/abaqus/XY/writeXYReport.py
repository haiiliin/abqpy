from typing import Sequence

from abqpy.decorators import abaqus_function_doc

from ..UtilityAndView.abaqusConstants import ON, Boolean
from .XYData import XYData

"""This method writes an XYData object to a user-defined ASCII file. 

"""


@abaqus_function_doc
def writeXYReport(fileName: str, xyData: Sequence[XYData], appendMode: Boolean = ON):
    """This method writes an XYData object to a user-defined ASCII file.

    .. note::
        This function can be accessed by::

            session.writeXYReport

    Parameters
    ----------
    fileName
        A String specifying the name of the file to which **X - Y** data will be written.
    xyData
        A sequence of XYData objects to be written to the output file.
    appendMode
        A Boolean specifying whether to append the **X - Y** data to the existing file. The default
        value is ON.
    """
    ...
