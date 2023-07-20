# Load

A specific type of load object and a specific type of load state object are designed for each type of load. A load object stores the nonpropagating data of a load as well as a number of instances of the corresponding load state object, each of which stores the propagating data of the load in a single step. Instances of the load state object are created and deleted internally by its corresponding load object.

Load Case commands are used for configuring load cases in specific types of steps that may use them.

## Load

The Load object is the abstract base type for other Load objects. The Load object has no explicit constructor. The methods and members of the Load object are common to all objects derived from Load.

### Create loads

```{eval-rst}
.. autoclass:: abaqus.Load.LoadModel.LoadModel
    :members:
    :show-inheritance:

    .. autoclasstoc::

```

### Other Classes

```{eval-rst}

.. toggle::

    .. automembers:: abaqus.Load
        :recursive:
        :exclude: LoadModel

    .. placeholder for empty members
```
