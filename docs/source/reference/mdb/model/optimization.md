# Optimization

Optimization commands are used to perform topology, shape, or sizing optimization of your model given a set of objectives and a set of restrictions.

## Create optimization tasks

```{eval-rst}
.. autoclass:: abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

## Assign features to optimization tasks

```{eval-rst}
.. autoclass:: abaqus.Optimization.OptimizationTask.OptimizationTask
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

```

## Other Classes

```{eval-rst}

.. toggle::

    .. autoclass:: abaqus.Optimization.BeadFixedRegion.BeadFixedRegion
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.BeadGrowth.BeadGrowth
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.BeadPenetrationCheck.BeadPenetrationCheck
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.BeadPlanarSymmetry.BeadPlanarSymmetry
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.BeadPointSymmetry.BeadPointSymmetry
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.BeadRotationalSymmetry.BeadRotationalSymmetry
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.BeadTask.BeadTask
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.DesignDirection.DesignDirection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.DesignResponse.DesignResponse
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.DrillControl.DrillControl
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.FixedRegion.FixedRegion
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.FrozenArea.FrozenArea
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.GeometricRestriction.GeometricRestriction
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.Growth.Growth
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.LocalStopCondition.LocalStopCondition
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.ObjectiveFunction.ObjectiveFunction
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.OptimizationConstraint.OptimizationConstraint
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.OptimizationObjective.OptimizationObjective
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.OptimizationObjectiveArray.OptimizationObjectiveArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.PenetrationCheck.PenetrationCheck
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.ShapeMemberSize.ShapeMemberSize
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.ShapeTask.ShapeTask
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.SizingClusterAreas.SizingClusterAreas
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.SizingFrozenArea.SizingFrozenArea
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.SizingMemberSize.SizingMemberSize
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.SizingPlanarSymmetry.SizingPlanarSymmetry
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.SizingTask.SizingTask
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.SlideRegionControl.SlideRegionControl
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.StampControl.StampControl
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.StepOption.StepOption
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.StepOptionArray.StepOptionArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.StopCondition.StopCondition
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.TopologyMemberSize.TopologyMemberSize
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.TopologyMillingControl.TopologyMillingControl
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.TopologyPointSymmetry.TopologyPointSymmetry
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.TopologyTask.TopologyTask
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Optimization.TurnControl.TurnControl
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::
```
