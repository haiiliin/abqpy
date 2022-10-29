# Boundary Condition

A specific type of boundary condition object and a specific type of boundary condition state object are designed for each type of boundary condition. A BoundaryCondition object stores the non-propagating data of a boundary condition as well as a number of instances of the corresponding BoundaryConditionState object, each of which stores the propagating data of the boundary condition in a single step. Instances of the BoundaryConditionState object are created and deleted internally by its corresponding BoundaryCondition object.

## Create boundary conditions

```{eval-rst}
.. autoclass:: abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel

    .. autoclasstoc::

```

## Classes

```{eval-rst}

.. collapse:: Click here to Expand

    .. autoclass:: abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.AccelerationBaseMotionBC.AccelerationBaseMotionBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.AccelerationBaseMotionBCState.AccelerationBaseMotionBCState

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.AccelerationBC.AccelerationBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.AccelerationBCState.AccelerationBCState

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.AcousticPressureBC.AcousticPressureBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.AcousticPressureBCState.AcousticPressureBCState

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.ConcentrationBCState.ConcentrationBCState

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.DisplacementBaseMotionBCState.DisplacementBaseMotionBCState

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.DisplacementBC.DisplacementBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.ElectricPotentialBCState.ElectricPotentialBCState

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.EulerianBC.EulerianBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.EulerianBCState.EulerianBCState

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.FluidCavityPressureBCState.FluidCavityPressureBCState

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.MaterialFlowBCState.MaterialFlowBCState

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.PorePressureBC.PorePressureBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.PorePressureBCState.PorePressureBCState

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.SecondaryBaseBCState.SecondaryBaseBCState

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.SubmodelBC.SubmodelBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.SubmodelBCState.SubmodelBCState

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.TemperatureBC.TemperatureBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.TemperatureBCState.TemperatureBCState

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.TypeBC.TypeBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.TypeBCState.TypeBCState

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.VelocityBaseMotionBCState.VelocityBaseMotionBCState

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.VelocityBC.VelocityBC

        .. autoclasstoc::

    .. autoclass:: abaqus.BoundaryCondition.VelocityBCState.VelocityBCState

        .. autoclasstoc::
```
