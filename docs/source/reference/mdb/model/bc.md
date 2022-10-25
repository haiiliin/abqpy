# Boundary Condition

A specific type of boundary condition object and a specific type of boundary condition state object are designed for each type of boundary condition. A BoundaryCondition object stores the non-propagating data of a boundary condition as well as a number of instances of the corresponding BoundaryConditionState object, each of which stores the propagating data of the boundary condition in a single step. Instances of the BoundaryConditionState object are created and deleted internally by its corresponding BoundaryCondition object.

## Create boundary conditions

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

```

## Classes

### BoundaryCondition

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### BoundaryConditionState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### AccelerationBaseMotionBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.AccelerationBaseMotionBC.AccelerationBaseMotionBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### AccelerationBaseMotionBCState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.AccelerationBaseMotionBCState.AccelerationBaseMotionBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### AccelerationBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.AccelerationBC.AccelerationBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### AccelerationBCState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.AccelerationBCState.AccelerationBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### AcousticPressureBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.AcousticPressureBC.AcousticPressureBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### AcousticPressureBCState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.AcousticPressureBCState.AcousticPressureBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ConcentrationBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ConcentrationBCState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.ConcentrationBCState.ConcentrationBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ConnAccelerationBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ConnAccelerationBCState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ConnDisplacementBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ConnDisplacementBCState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ConnVelocityBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ConnVelocityBCState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### DisplacementBaseMotionBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### DisplacementBaseMotionBCState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.DisplacementBaseMotionBCState.DisplacementBaseMotionBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### DisplacementBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.DisplacementBC.DisplacementBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### DisplacementBCState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ElectricPotentialBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ElectricPotentialBCState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.ElectricPotentialBCState.ElectricPotentialBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### EulerianBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.EulerianBC.EulerianBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### EulerianBCState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.EulerianBCState.EulerianBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### EulerianMotionBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### EulerianMotionBCState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### FluidCavityPressureBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### FluidCavityPressureBCState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.FluidCavityPressureBCState.FluidCavityPressureBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### MagneticVectorPotentialBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### MaterialFlowBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### MaterialFlowBCState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.MaterialFlowBCState.MaterialFlowBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### PorePressureBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.PorePressureBC.PorePressureBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### PorePressureBCState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.PorePressureBCState.PorePressureBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### RetainedNodalDofsBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### SecondaryBaseBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### SecondaryBaseBCState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.SecondaryBaseBCState.SecondaryBaseBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### SubmodelBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.SubmodelBC.SubmodelBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### SubmodelBCState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.SubmodelBCState.SubmodelBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### TemperatureBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.TemperatureBC.TemperatureBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### TemperatureBCState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.TemperatureBCState.TemperatureBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### TypeBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.TypeBC.TypeBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### TypeBCState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.TypeBCState.TypeBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### VelocityBaseMotionBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### VelocityBaseMotionBCState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.VelocityBaseMotionBCState.VelocityBaseMotionBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### VelocityBC

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.VelocityBC.VelocityBC
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### VelocityBCState

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.VelocityBCState.VelocityBCState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```
