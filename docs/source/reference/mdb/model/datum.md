# Datum

Datum commands return Feature objects and inherit the methods of Feature objects. For more details, see Feature commands. Datums can be created using methods on a Part or Assembly object.

Each command also creates a Datum object in the corresponding datum repository. The Datum object is used as an argument to other commands, such as Part and Partition commands.

## Other Classes

```{eval-rst}

.. toggle::

    .. autoclass:: abaqus.Datum.Datum.Datum
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Datum.DatumAxis.DatumAxis
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Datum.DatumCsys.DatumCsys
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Datum.DatumPlane.DatumPlane
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Datum.DatumPoint.DatumPoint
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::
```
