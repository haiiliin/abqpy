# Adaptivity

The Adaptivity commands are used to define objects, perform analyses, and calculate new meshes for Arbitrary Lagrangian Eularian (ALE) adaptive smoothing (adaptive meshing) and varying topology adaptivity (adaptive remeshing).

## Create adaptivity mesh control features

```{eval-rst}
.. autoclass:: abaqus.Adaptivity.AdaptivityModel.AdaptivityModel
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

```

## Create adaptivity mesh state features

```{eval-rst}
.. autoclass:: abaqus.Adaptivity.AdaptivityStep.AdaptivityStep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

```

## Create features for AdaptivityIteration

```{eval-rst}
.. autoclass:: abaqus.Adaptivity.AdaptivityIteration.AdaptivityIteration
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

```

## Other Classes

```{eval-rst}

.. toggle::

    .. automembers:: abaqus.Adaptivity
        :recursive:
        :exclude: AdaptivityModel, AdaptivityStep, AdaptivityIteration
```
