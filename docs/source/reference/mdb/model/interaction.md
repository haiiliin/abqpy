# Interaction

A specific type of interaction object and a specific type of interaction state object are designed for each type of interaction. An interaction object stores the non-propagating data of an interaction as well as a number of instances of the corresponding interaction state object, each of which stores the propagating data of the interaction in a single step. Instances of the interaction state object are created and deleted internally by its corresponding interaction object.

## Create interactions

```{eval-rst}
.. autoclass:: abaqus.Interaction.InteractionModel.InteractionModel
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

```{eval-rst}
.. autoclass:: abaqus.Interaction.InteractionContactControlModel.InteractionContactControlModel
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

```{eval-rst}
.. autoclass:: abaqus.Interaction.InteractionContactInitializationModel.InteractionContactInitializationModel
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

```{eval-rst}
.. autoclass:: abaqus.Interaction.InteractionContactStabilizationModel.InteractionContactStabilizationModel
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

```{eval-rst}
.. autoclass:: abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

```

## Classes

### ContactControl

```{eval-rst}
.. autoclass:: abaqus.Interaction.ContactControl.ContactControl
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ContactDamage

```{eval-rst}
.. autoclass:: abaqus.Interaction.ContactDamage.ContactDamage
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ContactDamping

```{eval-rst}
.. autoclass:: abaqus.Interaction.ContactDamping.ContactDamping
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ContactInitialization

```{eval-rst}
.. autoclass:: abaqus.Interaction.ContactInitialization.ContactInitialization
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ContactProperty

```{eval-rst}
.. autoclass:: abaqus.Interaction.ContactProperty.ContactProperty
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ContactPropertyAssignment

```{eval-rst}
.. autoclass:: abaqus.Interaction.ContactPropertyAssignment.ContactPropertyAssignment
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ContactStabilization

```{eval-rst}
.. autoclass:: abaqus.Interaction.ContactStabilization.ContactStabilization
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### Interaction

```{eval-rst}
.. autoclass:: abaqus.Interaction.Interaction.Interaction
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### InitializationAssignment

```{eval-rst}
.. autoclass:: abaqus.Interaction.InitializationAssignment.InitializationAssignment
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### InteractionProperty

```{eval-rst}
.. autoclass:: abaqus.Interaction.InteractionProperty.InteractionProperty
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### InteractionState

```{eval-rst}
.. autoclass:: abaqus.Interaction.InteractionState.InteractionState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### AcousticImpedance

```{eval-rst}
.. autoclass:: abaqus.Interaction.AcousticImpedance.AcousticImpedance
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### AcousticImpedanceProp

```{eval-rst}
.. autoclass:: abaqus.Interaction.AcousticImpedanceProp.AcousticImpedanceProp
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### AcousticImpedanceState

```{eval-rst}
.. autoclass:: abaqus.Interaction.AcousticImpedanceState.AcousticImpedanceState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ActuatorSensor

```{eval-rst}
.. autoclass:: abaqus.Interaction.ActuatorSensor.ActuatorSensor
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ActuatorSensorProp

```{eval-rst}
.. autoclass:: abaqus.Interaction.ActuatorSensorProp.ActuatorSensorProp
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ActuatorSensorState

```{eval-rst}
.. autoclass:: abaqus.Interaction.ActuatorSensorState.ActuatorSensorState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### CavityRadiation

```{eval-rst}
.. autoclass:: abaqus.Interaction.CavityRadiation.CavityRadiation
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### CavityRadiationProp

```{eval-rst}
.. autoclass:: abaqus.Interaction.CavityRadiationProp.CavityRadiationProp
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### CavityRadiationState

```{eval-rst}
.. autoclass:: abaqus.Interaction.CavityRadiationState.CavityRadiationState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### CohesiveBehavior

```{eval-rst}
.. autoclass:: abaqus.Interaction.CohesiveBehavior.CohesiveBehavior
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ConcentratedFilmCondition

```{eval-rst}
.. autoclass:: abaqus.Interaction.ConcentratedFilmCondition.ConcentratedFilmCondition
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ConcentratedFilmConditionState

```{eval-rst}
.. autoclass:: abaqus.Interaction.ConcentratedFilmConditionState.ConcentratedFilmConditionState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ConcentratedRadiationToAmbient

```{eval-rst}
.. autoclass:: abaqus.Interaction.ConcentratedRadiationToAmbient.ConcentratedRadiationToAmbient
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ConcentratedRadiationToAmbientState

```{eval-rst}
.. autoclass:: abaqus.Interaction.ConcentratedRadiationToAmbientState.ConcentratedRadiationToAmbientState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ContactExp

```{eval-rst}
.. autoclass:: abaqus.Interaction.ContactExp.ContactExp
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ContactStd

```{eval-rst}
.. autoclass:: abaqus.Interaction.ContactStd.ContactStd
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ContactTangentialBehavior

```{eval-rst}
.. autoclass:: abaqus.Interaction.ContactTangentialBehavior.ContactTangentialBehavior
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### CyclicSymmetry

```{eval-rst}
.. autoclass:: abaqus.Interaction.CyclicSymmetry.CyclicSymmetry
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### CyclicSymmetryState

```{eval-rst}
.. autoclass:: abaqus.Interaction.CyclicSymmetryState.CyclicSymmetryState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ElasticFoundation

```{eval-rst}
.. autoclass:: abaqus.Interaction.ElasticFoundation.ElasticFoundation
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ElasticFoundationState

```{eval-rst}
.. autoclass:: abaqus.Interaction.ElasticFoundationState.ElasticFoundationState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ExpContactControl

```{eval-rst}
.. autoclass:: abaqus.Interaction.ExpContactControl.ExpContactControl
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### FilmCondition

```{eval-rst}
.. autoclass:: abaqus.Interaction.FilmCondition.FilmCondition
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### FilmConditionProp

```{eval-rst}
.. autoclass:: abaqus.Interaction.FilmConditionProp.FilmConditionProp
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### FilmConditionState

```{eval-rst}
.. autoclass:: abaqus.Interaction.FilmConditionState.FilmConditionState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### FluidCavity

```{eval-rst}
.. autoclass:: abaqus.Interaction.FluidCavity.FluidCavity
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### FluidCavityProperty

```{eval-rst}
.. autoclass:: abaqus.Interaction.FluidCavityProperty.FluidCavityProperty
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### FluidCavityState

```{eval-rst}
.. autoclass:: abaqus.Interaction.FluidCavityState.FluidCavityState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### FluidExchange

```{eval-rst}
.. autoclass:: abaqus.Interaction.FluidExchange.FluidExchange
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### FluidExchangeProperty

```{eval-rst}
.. autoclass:: abaqus.Interaction.FluidExchangeProperty.FluidExchangeProperty
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### FluidExchangeState

```{eval-rst}
.. autoclass:: abaqus.Interaction.FluidExchangeState.FluidExchangeState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### FluidInflator

```{eval-rst}
.. autoclass:: abaqus.Interaction.FluidInflator.FluidInflator
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### FluidInflatorProperty

```{eval-rst}
.. autoclass:: abaqus.Interaction.FluidInflatorProperty.FluidInflatorProperty
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### FluidInflatorState

```{eval-rst}
.. autoclass:: abaqus.Interaction.FluidInflatorState.FluidInflatorState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### FractureCriterion

```{eval-rst}
.. autoclass:: abaqus.Interaction.FractureCriterion.FractureCriterion
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### GapElectricalConductance

```{eval-rst}
.. autoclass:: abaqus.Interaction.GapElectricalConductance.GapElectricalConductance
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### GapHeatGeneration

```{eval-rst}
.. autoclass:: abaqus.Interaction.GapHeatGeneration.GapHeatGeneration
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### GeometricProperties

```{eval-rst}
.. autoclass:: abaqus.Interaction.GeometricProperties.GeometricProperties
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### IncidentWave

```{eval-rst}
.. autoclass:: abaqus.Interaction.IncidentWave.IncidentWave
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### IncidentWaveProperty

```{eval-rst}
.. autoclass:: abaqus.Interaction.IncidentWaveProperty.IncidentWaveProperty
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### IncidentWaveState

```{eval-rst}
.. autoclass:: abaqus.Interaction.IncidentWaveState.IncidentWaveState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### MainSecondaryAssignment

```{eval-rst}
.. autoclass:: abaqus.Interaction.MainSecondaryAssignment.MainSecondaryAssignment
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### ModelChange

```{eval-rst}
.. autoclass:: abaqus.Interaction.ModelChange.ModelChange
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### NormalBehavior

```{eval-rst}
.. autoclass:: abaqus.Interaction.NormalBehavior.NormalBehavior
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

```

### PressurePenetration

```{eval-rst}
.. autoclass:: abaqus.Interaction.PressurePenetration.PressurePenetration
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### PressurePenetrationState

```{eval-rst}
.. autoclass:: abaqus.Interaction.PressurePenetrationState.PressurePenetrationState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### Radiation

```{eval-rst}
.. autoclass:: abaqus.Interaction.Radiation.Radiation
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### RadiationToAmbient

```{eval-rst}
.. autoclass:: abaqus.Interaction.RadiationToAmbient.RadiationToAmbient
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### RadiationToAmbientState

```{eval-rst}
.. autoclass:: abaqus.Interaction.RadiationToAmbientState.RadiationToAmbientState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### RegionPairs

```{eval-rst}
.. autoclass:: abaqus.Interaction.RegionPairs.RegionPairs
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### SelfContactExp

```{eval-rst}
.. autoclass:: abaqus.Interaction.SelfContactExp.SelfContactExp
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### SelfContactExpState

```{eval-rst}
.. autoclass:: abaqus.Interaction.SelfContactExpState.SelfContactExpState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### SelfContactStd

```{eval-rst}
.. autoclass:: abaqus.Interaction.SelfContactStd.SelfContactStd
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### SelfContactStdState

```{eval-rst}
.. autoclass:: abaqus.Interaction.SelfContactStdState.SelfContactStdState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### SlidingTransitionAssignment

```{eval-rst}
.. autoclass:: abaqus.Interaction.SlidingTransitionAssignment.SlidingTransitionAssignment
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### SmoothingAssignment

```{eval-rst}
.. autoclass:: abaqus.Interaction.SmoothingAssignment.SmoothingAssignment
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### StabilizationAssignment

```{eval-rst}
.. autoclass:: abaqus.Interaction.StabilizationAssignment.StabilizationAssignment
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### StdContactControl

```{eval-rst}
.. autoclass:: abaqus.Interaction.StdContactControl.StdContactControl
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### StdInitialization

```{eval-rst}
.. autoclass:: abaqus.Interaction.StdInitialization.StdInitialization
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### StdStabilization

```{eval-rst}
.. autoclass:: abaqus.Interaction.StdStabilization.StdStabilization
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### StdXplCosimulation

```{eval-rst}
.. autoclass:: abaqus.Interaction.StdXplCosimulation.StdXplCosimulation
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### StdXplCosimulationState

```{eval-rst}
.. autoclass:: abaqus.Interaction.StdXplCosimulationState.StdXplCosimulationState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

```

### SurfaceFeatureAssignment

```{eval-rst}
.. autoclass:: abaqus.Interaction.SurfaceFeatureAssignment.SurfaceFeatureAssignment
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

```

### SurfaceOffsetAssignment

```{eval-rst}
.. autoclass:: abaqus.Interaction.SurfaceOffsetAssignment.SurfaceOffsetAssignment
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### SurfaceThicknessAssignment

```{eval-rst}
.. autoclass:: abaqus.Interaction.SurfaceThicknessAssignment.SurfaceThicknessAssignment
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### SurfaceToSurfaceContactExp

```{eval-rst}
.. autoclass:: abaqus.Interaction.SurfaceToSurfaceContactExp.SurfaceToSurfaceContactExp
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### SurfaceToSurfaceContactStd

```{eval-rst}
.. autoclass:: abaqus.Interaction.SurfaceToSurfaceContactStd.SurfaceToSurfaceContactStd
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### SurfaceToSurfaceExpState

```{eval-rst}
.. autoclass:: abaqus.Interaction.SurfaceToSurfaceExpState.SurfaceToSurfaceExpState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### SurfaceToSurfaceStdState

```{eval-rst}
.. autoclass:: abaqus.Interaction.SurfaceToSurfaceStdState.SurfaceToSurfaceStdState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

```

### ThermalConductance

```{eval-rst}
.. autoclass:: abaqus.Interaction.ThermalConductance.ThermalConductance
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### XFEMCrackGrowth

```{eval-rst}
.. autoclass:: abaqus.Interaction.XFEMCrackGrowth.XFEMCrackGrowth
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### XFEMCrackGrowthState

```{eval-rst}
.. autoclass:: abaqus.Interaction.XFEMCrackGrowthState.XFEMCrackGrowthState
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```
