from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class MonitorMgr:
    """An instance of the MonitorMgr object is created when you import the abaqus module. No
    other instance of the MonitorMgr object is required. (This MonitorMgr object is not to
    be confused with the degree of freedom (DOF) monitor that is constructed from the Step
    object.)

    .. note:: 
        This object can be accessed by::

            monitorManager
    """

    @abaqus_method_doc
    def addMessageCallback(
        self,
        jobName: str,
        messageType: SymbolicConstant,
        callback: SymbolicConstant,
        userData: str = "",
    ):
        """This method specifies a callback function that will be called when the specified message
        is received from the analysis product.
        For more information, see An example of a callback function.

        Parameters
        ----------
        jobName
            A String specifying the name of the job to be monitored or the SymbolicConstant ANY_JOB.
        messageType
            A SymbolicConstant specifying which message type will call this callback. Possible
            values are: 
            
            - ABORTED
            - ANY_JOB
            - ANY_MESSAGE_TYPE
            - COMPLETED
            - END_STEP
            - ERROR
            - HEADING
            - HEALER_JOB
            - HEALER_TYPE
            - INTERRUPTED
            - ITERATION
            - JOB_ABORTED
            - JOB_COMPLETED
            - JOB_INTERRUPTED
            - JOB_SUBMITTED
            - MONITOR_DATA
            - ODB_FILE
            - ODB_FRAME
            - SIMULATION_ABORTED
            - SIMULATION_COMPLETED
            - SIMULATION_INTERRUPTED
            - SIMULATION_SUBMITTED
            - STARTED
            - STATUS
            - STEP
            - WARNING
            
        callback
            A Python function to be called. The interface definition of the callback function is
            `def onMessage(jobName, messageType, data, userData)` **jobName** is a
            String. **messageType** is a SymbolicConstant with possible values as listed previously for
            the addMessageCallback method. **data** is a DataObject object. **userData** is the object
            passed as the **userData** argument to the addMessageCallback method.
        userData
            Any Python object or None. This object is passed to the callback function.
        """
        ...

    @abaqus_method_doc
    def removeMessageCallback(
        self, jobName: str, messageType: SymbolicConstant, callback: str, userData: str
    ):
        """This method removes a callback function. You specify the callback function to remove
        using the same arguments you used to add the callback.

        Parameters
        ----------
        jobName
            A String specifying the name of the job to be monitored or the SymbolicConstant ANY_JOB.
        messageType
            A SymbolicConstant specifying which message type will call this callback. Possible
            values are:
            - ABORTED
            - ANY_JOB
            - ANY_MESSAGE_TYPE
            - COMPLETED
            - END_STEP
            - ERROR
            - HEADING
            - HEALER_JOB
            - HEALER_TYPE
            - INTERRUPTED
            - ITERATION
            - JOB_ABORTED
            - JOB_COMPLETED
            - JOB_INTERRUPTED
            - JOB_SUBMITTED
            - MONITOR_DATA
            - ODB_FILE
            - ODB_FRAME
            - SIMULATION_ABORTED
            - SIMULATION_COMPLETED
            - SIMULATION_INTERRUPTED
            - SIMULATION_SUBMITTED
            - STARTED
            - STATUS
            - STEP
            - WARNING
        callback
            A Python function to be called; it must be the same as the **callback** argument specified
            in the original call to addMessageCallback.
        userData
            Any Python object or None; it must be the same as the **userData** argument specified in
            the original call to addMessageCallback.
        """
        ...

    @abaqus_method_doc
    def checkMonitorStatus(self):
        """This method raises a MonitorError exception if the monitoring status is not ENABLED.

        Raises
        ------
        MonitorError
            Status is not ENABLED
        """
        ...
