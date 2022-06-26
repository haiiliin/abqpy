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

    .. autoclassdoc::

Job
~~~

.. autoclass:: abaqus.Job.Job.Job
    :members:

    .. autoclassdoc::

JobFromInputFile
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Job.JobFromInputFile.JobFromInputFile
    :members:

    .. autoclassdoc::

Message
~~~~~~~

.. autoclass:: abaqus.Job.Message.Message
    :members:

    .. autoclassdoc::

MessageArray
~~~~~~~~~~~~

.. autoclass:: abaqus.Job.MessageArray.MessageArray
    :members:

    .. autoclassdoc::

ModelJob
~~~~~~~~

.. autoclass:: abaqus.Job.ModelJob.ModelJob
    :members:

    .. autoclassdoc::

OptimizationProcess
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Job.OptimizationProcess.OptimizationProcess
    :members:

    .. autoclassdoc::

Queue
~~~~~

.. autoclass:: abaqus.Job.Queue.Queue
    :members:
