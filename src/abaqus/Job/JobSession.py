from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Queue import Queue
from ..Session.SessionBase import SessionBase
from ..UtilityAndView.abaqusConstants import ALL, Boolean, OFF, ON, SymbolicConstant


@abaqus_class_doc
class JobSession(SessionBase):

    @abaqus_method_doc
    def Queue(
        self,
        name: str,
        queueName: str,
        hostName: str = "",
        fileCopy: Boolean = ON,
        directory: str = "",
        driver: str = "",
        remotePlatform: SymbolicConstant = "Linux",
        filesToCopy: str = ALL,
        deleteAfterCopy: Boolean = OFF,
        description: str = "",
    ) -> Queue:
        """This method creates a Queue object.
        Note:Remote queues are available only on Linux platforms.

        .. note:: 
            This function can be accessed by::

                session.Queue

        Parameters
        ----------
        name
            A String specifying the name of the new Queue object.
        queueName
            A String specifying the name of the remote analysis queue.
        hostName
            A String specifying the name of the remote host. The default value is an empty string.
        fileCopy
            A Boolean specifying if the results files are to be copied from the remote machine to
            the local machine. The default value is ON.
        directory
            A String specifying the remote location for the execution of the simulation. The default
            value is an empty string.
        driver
            A String specifying the designation of the remote driver. The default value is "abaqus".
        remotePlatform
            A SymbolicConstant specifying the type of operating system on the remote machine. The
            default value is Linux.
        filesToCopy
            A list of Strings specifying the files to be copied from the remote location to the
            local machine, or ALL. Strings specified in a list are the extensions of the job files
            that will be copied, such as ('log', 'dat', 'msg', 'sta', 'odb'). The default value is
            ALL.
        deleteAfterCopy
            A Boolean specifying whether remote files are to be deleted after they are copied to the
            local machine. The default value is OFF.
        description
            A String specifying a description of the queue. The default value is an empty string.

        Returns
        -------
        Queue
            A :py:class:`~abaqus.Job.Queue.Queue` object.

        Raises
        ------
        Remote queue host name is not set
            If **fileCopy** = ON and **hostName** is empty.
        Directory in which to run the job on the remote computer is not set
            If **fileCopy** = ON and **directory** is empty.
        """
        self.queues[name] = queue = Queue(
            name,
            queueName,
            hostName,
            fileCopy,
            directory,
            driver,
            remotePlatform,
            filesToCopy,
            deleteAfterCopy,
            description,
        )
        return queue
