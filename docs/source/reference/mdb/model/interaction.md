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

## Other Classes

```{eval-rst}

.. toggle::

    .. autoclass:: abaqus.Interaction.ContactControl.ContactControl
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ContactDamage.ContactDamage
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ContactDamping.ContactDamping
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ContactInitialization.ContactInitialization
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ContactProperty.ContactProperty
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ContactPropertyAssignment.ContactPropertyAssignment
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ContactStabilization.ContactStabilization
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.Interaction.Interaction
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.InitializationAssignment.InitializationAssignment
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.InteractionProperty.InteractionProperty
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.InteractionState.InteractionState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.AcousticImpedance.AcousticImpedance
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.AcousticImpedanceProp.AcousticImpedanceProp
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.AcousticImpedanceState.AcousticImpedanceState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ActuatorSensor.ActuatorSensor
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ActuatorSensorProp.ActuatorSensorProp
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ActuatorSensorState.ActuatorSensorState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.CavityRadiation.CavityRadiation
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.CavityRadiationProp.CavityRadiationProp
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.CavityRadiationState.CavityRadiationState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.CohesiveBehavior.CohesiveBehavior
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ConcentratedFilmCondition.ConcentratedFilmCondition
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ConcentratedFilmConditionState.ConcentratedFilmConditionState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ConcentratedRadiationToAmbient.ConcentratedRadiationToAmbient
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ConcentratedRadiationToAmbientState.ConcentratedRadiationToAmbientState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ContactExp.ContactExp
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ContactStd.ContactStd
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ContactTangentialBehavior.ContactTangentialBehavior
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.CyclicSymmetry.CyclicSymmetry
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.CyclicSymmetryState.CyclicSymmetryState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ElasticFoundation.ElasticFoundation
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ElasticFoundationState.ElasticFoundationState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ExpContactControl.ExpContactControl
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FilmCondition.FilmCondition
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FilmConditionProp.FilmConditionProp
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FluidCavity.FluidCavity
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FluidCavityProperty.FluidCavityProperty
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FluidCavityState.FluidCavityState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FluidExchange.FluidExchange
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FluidExchangeProperty.FluidExchangeProperty
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FluidExchangeState.FluidExchangeState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FluidInflator.FluidInflator
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FluidInflatorProperty.FluidInflatorProperty
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FluidInflatorState.FluidInflatorState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FractureCriterion.FractureCriterion
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.GapElectricalConductance.GapElectricalConductance
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.GapHeatGeneration.GapHeatGeneration
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.GeometricProperties.GeometricProperties
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.IncidentWave.IncidentWave
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.IncidentWaveProperty.IncidentWaveProperty
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.IncidentWaveState.IncidentWaveState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.MasterSlaveAssignment.MasterSlaveAssignment
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ModelChange.ModelChange
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.NormalBehavior.NormalBehavior
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::


    .. autoclass:: abaqus.Interaction.PressurePenetration.PressurePenetration
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.PressurePenetrationState.PressurePenetrationState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.Radiation.Radiation
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.RadiationToAmbient.RadiationToAmbient
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.RadiationToAmbientState.RadiationToAmbientState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.RegionPairs.RegionPairs
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SelfContactExp.SelfContactExp
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SelfContactExpState.SelfContactExpState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SelfContactStd.SelfContactStd
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SelfContactStdState.SelfContactStdState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SlidingTransitionAssignment.SlidingTransitionAssignment
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SmoothingAssignment.SmoothingAssignment
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.StabilizationAssignment.StabilizationAssignment
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.StdContactControl.StdContactControl
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.StdInitialization.StdInitialization
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.StdStabilization.StdStabilization
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.StdXplCosimulation.StdXplCosimulation
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.StdXplCosimulationState.StdXplCosimulationState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::


    .. autoclass:: abaqus.Interaction.SurfaceFeatureAssignment.SurfaceFeatureAssignment
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::


    .. autoclass:: abaqus.Interaction.SurfaceOffsetAssignment.SurfaceOffsetAssignment
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SurfaceThicknessAssignment.SurfaceThicknessAssignment
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SurfaceToSurfaceContactExp.SurfaceToSurfaceContactExp
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SurfaceToSurfaceContactStd.SurfaceToSurfaceContactStd
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SurfaceToSurfaceExpState.SurfaceToSurfaceExpState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SurfaceToSurfaceStdState.SurfaceToSurfaceStdState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::


    .. autoclass:: abaqus.Interaction.ThermalConductance.ThermalConductance
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.XFEMCrackGrowth.XFEMCrackGrowth
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.XFEMCrackGrowthState.XFEMCrackGrowthState
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::
```
