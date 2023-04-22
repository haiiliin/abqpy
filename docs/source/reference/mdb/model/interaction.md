# Interaction

A specific type of interaction object and a specific type of interaction state object are designed for each type of interaction. An interaction object stores the non-propagating data of an interaction as well as a number of instances of the corresponding interaction state object, each of which stores the propagating data of the interaction in a single step. Instances of the interaction state object are created and deleted internally by its corresponding interaction object.

## Create interactions

```{eval-rst}
.. autoclass:: abaqus.Interaction.InteractionModel.InteractionModel
    :members:
    :show-inheritance:

    .. autoclasstoc::
```

```{eval-rst}
.. autoclass:: abaqus.Interaction.InteractionContactControlModel.InteractionContactControlModel
    :members:
    :show-inheritance:

    .. autoclasstoc::
```

```{eval-rst}
.. autoclass:: abaqus.Interaction.InteractionContactInitializationModel.InteractionContactInitializationModel
    :members:
    :show-inheritance:

    .. autoclasstoc::
```

```{eval-rst}
.. autoclass:: abaqus.Interaction.InteractionContactStabilizationModel.InteractionContactStabilizationModel
    :members:
    :show-inheritance:

    .. autoclasstoc::
```

```{eval-rst}
.. autoclass:: abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel
    :members:
    :show-inheritance:

    .. autoclasstoc::

```

## Other Classes

```{eval-rst}

.. toggle::

    .. automembers:: abaqus.Interaction
        :recursive:
        :exclude: InteractionModel, InteractionContactControlModel, InteractionContactInitializationModel, InteractionContactStabilizationModel, InteractionPropertyModel

    .. placeholder for empty members
```
