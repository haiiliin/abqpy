# Section

The Section commands are used to create sections and profiles with their associated properties and behavior. The various section objects are all derived from the Section object. The various profile objects are all derived from the Profile object. See Property commands for the property assignment commands.

```{toctree}
:caption: Objects in Section
:maxdepth: 1

section/connector
```

## Create sections

### In Mdb

```{eval-rst}
.. autoclass:: abaqus.Section.SectionModel.SectionModel
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

```

### In Odb

```{eval-rst}
.. autoclass:: abaqus.Section.SectionOdb.SectionOdb
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

```

## Other Classes

```{eval-rst}

.. toggle::

    .. automembers:: abaqus.Section
        :recursive:
        :exclude: SectionModel, SectionOdb
```
