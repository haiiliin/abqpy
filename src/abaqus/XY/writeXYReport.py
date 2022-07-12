from abaqusConstants import *
from .XYData import XYData

"""This method writes an XYData object to a user-defined ASCII file. 

"""


def writeXYReport(fileName: str, xyData: tuple[XYData], appendMode: Boolean = ON):
    """This method writes an XYData object to a user-defined ASCII file.

    .. note:: 
        This function can be accessed by:

        .. code-block:: python

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
    pass
