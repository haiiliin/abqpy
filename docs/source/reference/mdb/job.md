# Job

The Job object is the abstract base type for other Job objects. The Job object has no explicit constructor. The methods and members of the Job object are common to all objects derived from Job.

## Create jobs

```{eval-rst}
.. automethod:: abaqus.Job.JobMdb.JobMdb.Job
    :noindex:

```

## Create queues in Session

```{eval-rst}
.. automethod:: abaqus.Job.JobSession.JobSession.Queue

```

## Other Classes

```{eval-rst}

.. toggle::

    .. autoclass:: abaqus.Job.Coexecution.Coexecution
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Job.Job.Job
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Job.JobFromInputFile.JobFromInputFile
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Job.Message.Message
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Job.MessageArray.MessageArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Job.ModelJob.ModelJob
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Job.OptimizationProcess.OptimizationProcess
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Job.Queue.Queue
        :members:
        :special-members: __init__
        :show-inheritance:
```
