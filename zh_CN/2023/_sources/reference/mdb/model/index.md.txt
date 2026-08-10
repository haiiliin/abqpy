# Model

Model commands are used to create Abaqus/CAE models. A finished model contains all the data that Abaqus/CAE needs to create and submit an analysis to Abaqus/Standard or Abaqus/Explicit. Models are stored in a model database.

```{toctree}
:caption: Objects in Model
:maxdepth: 1

adaptivity
amplitude
bc
calibration
constraint
field
filter
interaction
load
material
mesh
optimization
output
part_assembly/index
predefined
profile
property
section/index
sketcher
step/index
```

## Classes

### Model

```{eval-rst}
.. autoclass:: abaqus.Model.Model.Model
    :members:
    :show-inheritance:

    .. autoclasstoc::
```

### Other Classes

```{eval-rst}

.. toggle::

    .. automembers:: abaqus.Model
        :recursive:
        :exclude: Model

    .. placeholder for empty members
```
