from typing import Optional
from abqpy.decorators import abaqus_class_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class SelectedProbeValues:
    """The SelectedProbeValues object has no constructor. The SelectedProbeValues object is
    created when you import the Visualization module.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.selectedProbeValues
    """

    #: An Int specifying the length of the **values** member.
    length: Optional[int] = None

    #: A Boolean specifying whether any probe values have been selected (as is necessary prior
    #: to writing to a file).
    fieldOutputAvailable: Boolean = OFF

    #: A tuple of tuples of Floats specifying the selected probe values.
    values: Optional[float] = None

    #: A tuple of Floats specifying the last sequence of the **values** member.
    lastValues: tuple = ()
