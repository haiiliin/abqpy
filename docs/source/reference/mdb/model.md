# Model

Model commands are used to create Abaqus/CAE models. A finished model contains all the data that Abaqus/CAE needs to create and submit an analysis to Abaqus/Standard or Abaqus/Explicit. Models are stored in a model database.

```{toctree}
:caption: Objects in Model
:maxdepth: 1

model/adaptivity
model/amplitude
model/bc
model/calibration
model/constraint
model/field
model/filter
model/interaction
model/load
model/material
model/mesh
model/optimization
model/output
model/part_assembly
model/predefined
model/profile
model/property
model/section
model/sketcher
model/step
```

## Classes

### Model

```{eval-rst}
.. autoclass:: abaqus.Model.Model.Model
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### Other Classes

```{eval-rst}

.. toggle::

    .. autoclass:: abaqus.Model.ModelBase.ModelBase
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Model.KeywordBlock.KeywordBlock
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::
```
