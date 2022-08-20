from ..Animation.AnimationSession import AnimationSession
from ..DisplayGroup.DisplayGroupSession import DisplayGroupSession
from ..FieldReport.FieldReportSession import FieldReportSession
from ..Job.JobSession import JobSession
from ..Odb.OdbSession import OdbSession
from ..PathAndProbe.PathSession import PathSession
from ..XY.XYSession import XYSession
from .._decorators import abaqus_class_doc


@abaqus_class_doc
class Session(
    AnimationSession,
    DisplayGroupSession,
    FieldReportSession,
    JobSession,
    OdbSession,
    PathSession,
    XYSession,
):
    """The Session object has no constructor. Abaqus creates the **session** member when a
    session is started.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            session
    """

    ...
