from typing import Optional
from abqpy.decorators import abaqus_function_doc
from ..Odb.Odb import Odb
from ..UtilityAndView.abaqusConstants import *

"""This command writes a free body output report to a file. 

"""


@abaqus_function_doc
def writeFreeBodyReport(
    fileName: str,
    append: Boolean,
    step: Optional[int] = None,
    frame: Optional[int] = None,
    stepFrame: SymbolicConstant = SPECIFY,
    odb: Optional[Odb] = None,
):
    """This method writes a FreeBody object to a user-defined ASCII file.

    .. note:: 
        This function can be accessed by::

            session.writeFreeBodyReport

    Parameters
    ----------
    fileName
        A String specifying the name of the file to which the free body output will be written.
    append
        A Boolean specifying whether to append the free body output to an existing file. The
        default value is ON.
    step
        An Int identifying the step from which to obtain values. The default value is the
        current step.
    frame
        An Int identifying the frame from which to obtain values. The default value is the
        current frame.
    stepFrame
        A SymbolicConstant indicating whether to obtain the values from the specified frame or
        from all active frames. Possible values are SPECIFY and ALL. The default value is
        SPECIFY.
    odb
        An :py:class:`~abaqus.Odb.Odb.Odb` object specifying the output database from which data will be read.

    Returns
    -------
    """
    ...
