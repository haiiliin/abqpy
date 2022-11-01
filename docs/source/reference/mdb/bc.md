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

## Other Classes

```{eval-rst}

.. toggle::

    .. autoclass:: abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.AccelerationBaseMotionBC.AccelerationBaseMotionBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.AccelerationBaseMotionBCState.AccelerationBaseMotionBCState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.AccelerationBC.AccelerationBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.AccelerationBCState.AccelerationBCState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.AcousticPressureBC.AcousticPressureBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.AcousticPressureBCState.AcousticPressureBCState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.ConcentrationBCState.ConcentrationBCState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.DisplacementBaseMotionBCState.DisplacementBaseMotionBCState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.DisplacementBC.DisplacementBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.ElectricPotentialBCState.ElectricPotentialBCState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.EulerianBC.EulerianBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.EulerianBCState.EulerianBCState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.FluidCavityPressureBCState.FluidCavityPressureBCState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.MaterialFlowBCState.MaterialFlowBCState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.PorePressureBC.PorePressureBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.PorePressureBCState.PorePressureBCState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.SecondaryBaseBCState.SecondaryBaseBCState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.SubmodelBC.SubmodelBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.SubmodelBCState.SubmodelBCState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.TemperatureBC.TemperatureBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.TemperatureBCState.TemperatureBCState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.TypeBC.TypeBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.TypeBCState.TypeBCState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.VelocityBaseMotionBCState.VelocityBaseMotionBCState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.VelocityBC.VelocityBC
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.VelocityBCState.VelocityBCState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::
```
