from typing import Optional
from abqpy.decorators import abaqus_class_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class Message:
    """The Message object contains information about a given phase of the simulation. Job
    messages are not returned if a script is run without the Abaqus/CAE GUI (using the noGUI
    option).

    .. note:: 
        This object can be accessed by::

            import job
            mdb.coexecutions[name].jobs[name].messages[i]
            mdb.jobs[name].messages[i]
    """

    #: A SymbolicConstant specifying the type of message. Possible values are:
    #: 
    #: - ABORTED
    #: - ANY_JOB
    #: - ANY_MESSAGE_TYPE
    #: - COMPLETED
    #: - END_STEP
    #: - ERROR
    #: - HEADING
    #: - HEALER_JOB
    #: - HEALER_TYPE
    #: - INTERRUPTED
    #: - ITERATION
    #: - JOB_ABORTED
    #: - JOB_COMPLETED
    #: - JOB_INTERRUPTED
    #: - JOB_SUBMITTED
    #: - MONITOR_DATA
    #: - ODB_FILE
    #: - ODB_FRAME
    #: - STARTED
    #: - STATE_FRAME
    #: - STATUS
    #: - STEP
    #: - WARNING
    type: Optional[SymbolicConstant] = None

    #: A Dictionary object specifying the data returned by the analysis product. The value
    #: depends on the message returned. For a list of the possible entries, see the members of
    #: DataObject.
    data: Optional[dict] = None
