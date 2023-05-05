from abqpy.decorators import abaqus_class_doc

from ..Animation.AnimationSession import AnimationSession
from ..Canvas.CanvasSession import CanvasSession
from ..DisplayGroup.DisplayGroupSession import DisplayGroupSession
from ..FieldReport.FieldReportSession import FieldReportSession
from ..Job.JobSession import JobSession
from ..Odb.OdbSession import OdbSession
from ..PathAndProbe.PathSession import PathSession
from ..XY.XYSession import XYSession


@abaqus_class_doc
class Session(
    AnimationSession,
    CanvasSession,
    DisplayGroupSession,
    FieldReportSession,
    JobSession,
    OdbSession,
    PathSession,
    XYSession,
):
    """The Session object has no constructor. Abaqus creates the **session** member when a session is started.

    .. note::
        This object can be accessed by::

            session
    """

    ...
