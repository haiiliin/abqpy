===
Job
===

The Job object is the abstract base type for other Job objects. The Job object has no explicit constructor. The methods and members of the Job object are common to all objects derived from Job.


Create jobs
-----------

.. automethod:: abaqus.Job.JobMdb.JobMdb.Job
    :members:

Create queues in Session
------------------------

.. automethod:: abaqus.Job.JobSession.JobSession.Queue


Features of the job
-------------------

Coexecution
~~~~~~~~~~~

.. autoclass:: abaqus.Job.Coexecution.Coexecution
    :members:

Job
~~~

.. autoclass:: abaqus.Job.Job.Job
    :members:

JobFromInputFile
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Job.JobFromInputFile.JobFromInputFile
    :members:

Message
~~~~~~~

.. autoclass:: abaqus.Job.Message.Message
    :members:

MessageArray
~~~~~~~~~~~~

.. autoclass:: abaqus.Job.MessageArray.MessageArray
    :members:

ModelJob
~~~~~~~~

.. autoclass:: abaqus.Job.ModelJob.ModelJob
    :members:

OptimizationProcess
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Job.OptimizationProcess.OptimizationProcess
    :members:

Queue
~~~~~

.. autoclass:: abaqus.Job.Queue.Queue
    :members:
