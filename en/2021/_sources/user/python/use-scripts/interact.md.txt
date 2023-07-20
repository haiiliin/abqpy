# Interacting with Abaqus/Standard and Abaqus/Explicit

The Job commands include methods that allow you to submit jobs to Abaqus/Standard and Abaqus/Explicit. This section describes how you can interact with Abaqus/Standard and Abaqus/Explicit and synchronize your scripts with the analysis job.

## Processing messages from Abaqus/Standard and Abaqus/Explicit

You can use the `addMessageCallback` method to associate an event-driven function with a particular message that is retrieved from Abaqus/Standard or Abaqus/Explicit. When Abaqus/CAE retrieves the specific message from Abaqus/Standard or Abaqus/Explicit, the function executes and takes the necessary action. This type of function is called a callback function. The `addMessageCallback` method specifies which callback function to use for which message.

The arguments to `addMessageCallback` are:

- The name of the job to monitor for messages.
- The message from Abaqus/Standard or Abaqus/Explicit that causes the callback function to execute.
- The name of the callback function.
- An object to pass to the callback function.

These arguments allow you to associate the callback function with both a particular job and a particular message. Alternatively, you can associate the callback function with all jobs and all messages. The commands are described in {doc}`/reference/kernel/messaging`.

The interface definition of the callback function is

```python2
def functionName(jobName, messageType, data, userData)
```

The arguments to the callback function are:

- **jobName**: A String specifying the name of the job to be monitored. You can also use the SymbolicConstant ANY_JOB that specifies that the callback function will monitor messages from all jobs.

- **messageType**: A SymbolicConstant specifying the message type that will call the callback function. You can also use the SymbolicConstant ANY_MESSAGE_TYPE that specifies that all messages will call the callback function. The following is a list of the message types issued by Abaqus/Standard and Abaqus/Explicit:

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

- **data**: A DataObject object containing the message data. The following list describes the members of the DataObject object:

  - **clientHost**: A String specifying the host name of the machine that is running the analysis.

  - **clientName**: A String specifying the name of the client that sent the message. Possible values are

    - "BatchPre" (the input file preprocessor)
    - "Packager" (the Abaqus/Explicit preprocessor packager)
    - "Standard" (the Abaqus/Standard analysis)
    - "Explicit" (the Abaqus/Explicit analysis)
    - "Calculator" (the postprocessing calculator)

  - **phase**: A SymbolicConstant specifying the phase of the analysis. Possible values are

    - BATCHPRE_PHASE
    - PACKAGER_PHASE
    - STANDARD_PHASE
    - EXPLICIT_PHASE
    - CALCULATOR_PHASE
    - HEALER_PHASE

  - **processId**: An Int specifying the process ID of the analysis program.

  - **threadId**: An Int specifying the thread ID of the analysis program. Threads are used for parallel or multiprocessing; in most cases **threadId** is set to zero.

  - **timeStamp**: An Int specifying the time the message was sent in seconds since 00:00:00 UTC, January 1, 1970.

- **userData**: Any Python object or `None`. This object is passed as the **userData** argument to `addMessageCallback`.

The following script is an example of how you can use the messaging capability of the Abaqus Scripting Interface. The callback function will intercept all messages from Abaqus/Standard or Abaqus/Explicit and print the messages in the Abaqus/CAE command line interface. Use the following command to retrieve the example script:

```sh
abaqus fetch job=simpleMonitor
```

To execute the script, do the following:

- From the Abaqus/CAE command line interface type from simpleMonitor import printMessages
- Submit an analysis job as usual.
- To start printing the messages, type `printMessages(ON)` from the Abaqus/CAE command line interface.
- To stop printing the messages, type `printMessages(OFF)` from the Abaqus/CAE command line interface.

```python2
"""
simpleMonitor.py

Print all messages issued during an Abaqus;
analysis to the Abaqus/CAE command line interface
"""

from abaqus import *
from abaqusConstants import *
from jobMessage import ANY_JOB, ANY_MESSAGE_TYPE

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def simpleCB(jobName, messageType, data, userData):
    """
    This callback prints out all the
    members of the data objects
    """

    format = '%-18s  %-18s  %s'

    print 'Message type: %s'%(messageType)
    print
    print 'data members:'
    print format%('member', 'type', 'value')

    members =  dir(data)
    for member in members:
        memberValue = getattr(data, member)
        memberType = type(memberValue).__name__
        print format%(member, memberType, memberValue)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def printMessages(start=ON):
    """
    Switch message printing ON or OFF
    """

    if start:
        monitorManager.addMessageCallback(ANY_JOB,
            ANY_MESSAGE_TYPE, simpleCB, None)
    else:
        monitorManager.removeMessageCallback(ANY_JOB,
            ANY_MESSAGE_TYPE, simpleCB, None)
```

## Waiting for a job to complete

You can use the Job object's `waitForCompletion` method to synchronize your script with a job that has been submitted. If you call the `waitForCompletion` method after you submit a job, the script waits until the analysis is complete before continuing. When the script continues, you should check the status of the job to ensure that the job completed successfully and did not abort. For example, the script described in Reproducing the cantilever beam tutorial uses `waitForCompletion` to ensure that the analysis job has finished executing successfully before the script opens the resulting output database and displays a contour plot of the results.

In the following example, the script submits myJob1 and waits for it to complete before submitting myJob2.

```python2
myJob1 = mdb.Job(name='Job-1')
myJob2 = mdb.Job(name='Job-2')
myJob1.submit()
myJob1.waitForCompletion()
myJob2.submit()
myJob2.waitForCompletion()
```

If you submit more than one job and then issue a `waitForCompletion` statement, Abaqus waits until the job associated with the `waitForCompletion` statement is complete before checking the status of the second job. If the second job has already completed, the `waitForCompletion` method returns immediately. In the following example the script will not check the status of `myJob2` until `myJob1` has completed.

```python2
myJob1 = mdb.Job(name='Job-1')
myJob2 = mdb.Job(name='Job-2')
myJob1.submit()
myJob2.submit()
myJob1.waitForCompletion()
myJob2.waitForCompletion()
```

## An example of a callback function

The following section describes how you can use a callback function as an alternative to the `waitForCompletion` method described in [waiting for a job to complete]. The example uses messaging commands to synchronize a script with an Abaqus/Standard or Abaqus/Explicit analysis. Messaging commands set up a callback function that monitors messages from Abaqus/Standard and Abaqus/Explicit. When the desired message is received, the callback function executes.

he example uses a callback function that responds to all messages from Abaqus/Standard and Abaqus/Explicit. The function decides what action to take based on the messages received from a job called Deform. If the message indicates that the analysis job is complete, the function opens the output database created by the job and displays a default contour plot.

```python2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Define the callback function

from abaqus import *
from abaqusConstants import *

import visualization

def onMessage(jobName, messageType, data, viewport):
if ((messageType==ABORTED) or (messageType==ERROR)):
    print 'Solver problem; stop execution of callback function'
elif (messageType==JOB_COMPLETED):
    odb = visualization.openOdb(path=jobName + '.odb')
    viewport.setValues(displayedObject=odb)
    viewport.odbDisplay.display.setValues(plotState=CONTOURS_ON_DEF)

    viewport.odbDisplay.commonOptions.setValues(renderStyle=FILLED)
```

The following statements show how the example script can be modified to use the callback function. After the first statement is executed, the callback function responds to all messages from the job named `Deform`. The final two statements create the job and submit it for analysis; the example script has now finished executing. When the job is complete, the callback function opens the resulting output database and displays a contour plot.

```python2
...
myJobName = 'Deform'
monitorManager.addMessageCallback(jobName=myJobName,
    messageType=ANY_MESSAGE_TYPE, callback=onMessage,
    userData=myViewport)
myJob = mdb.Job(name=myJobName, model='Beam',
    description=jobDescription)
myJob.submit()
# End of example script.
```

You can use the `removeMessageCallback` method at the end of the callback function to remove it from the system. The arguments to the `removeMessageCallback` method must be identical to the arguments to the corresponding `addMessageCallback` command that set up the callback function.
