# Interaction

A specific type of interaction object and a specific type of interaction state object are designed for each type of interaction. An interaction object stores the non-propagating data of an interaction as well as a number of instances of the corresponding interaction state object, each of which stores the propagating data of the interaction in a single step. Instances of the interaction state object are created and deleted internally by its corresponding interaction object.

## Create interactions

```{eval-rst}
.. autoclass:: abaqus.Interaction.InteractionModel.InteractionModel

    .. autoclasstoc::
```

```{eval-rst}
.. autoclass:: abaqus.Interaction.InteractionContactControlModel.InteractionContactControlModel

    .. autoclasstoc::
```

```{eval-rst}
.. autoclass:: abaqus.Interaction.InteractionContactInitializationModel.InteractionContactInitializationModel

    .. autoclasstoc::
```

```{eval-rst}
.. autoclass:: abaqus.Interaction.InteractionContactStabilizationModel.InteractionContactStabilizationModel

    .. autoclasstoc::
```

```{eval-rst}
.. autoclass:: abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel

    .. autoclasstoc::

```

## Classes

```{eval-rst}

.. collapse:: Click here to Expand

    .. autoclass:: abaqus.Interaction.ContactControl.ContactControl

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ContactDamage.ContactDamage

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ContactDamping.ContactDamping

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ContactInitialization.ContactInitialization

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ContactProperty.ContactProperty

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ContactPropertyAssignment.ContactPropertyAssignment

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ContactStabilization.ContactStabilization

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.Interaction.Interaction

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.InitializationAssignment.InitializationAssignment

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.InteractionProperty.InteractionProperty

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.InteractionState.InteractionState

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.AcousticImpedance.AcousticImpedance

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.AcousticImpedanceProp.AcousticImpedanceProp

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.AcousticImpedanceState.AcousticImpedanceState

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ActuatorSensor.ActuatorSensor

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ActuatorSensorProp.ActuatorSensorProp

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ActuatorSensorState.ActuatorSensorState

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.CavityRadiation.CavityRadiation

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.CavityRadiationProp.CavityRadiationProp

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.CavityRadiationState.CavityRadiationState

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.CohesiveBehavior.CohesiveBehavior

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ConcentratedFilmCondition.ConcentratedFilmCondition

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ConcentratedFilmConditionState.ConcentratedFilmConditionState

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ConcentratedRadiationToAmbient.ConcentratedRadiationToAmbient

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ConcentratedRadiationToAmbientState.ConcentratedRadiationToAmbientState

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ContactExp.ContactExp

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ContactStd.ContactStd

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ContactTangentialBehavior.ContactTangentialBehavior

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.CyclicSymmetry.CyclicSymmetry

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.CyclicSymmetryState.CyclicSymmetryState

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ElasticFoundation.ElasticFoundation

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ElasticFoundationState.ElasticFoundationState

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ExpContactControl.ExpContactControl

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FilmCondition.FilmCondition

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FilmConditionProp.FilmConditionProp

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FilmConditionState.FilmConditionState

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FluidCavity.FluidCavity

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FluidCavityProperty.FluidCavityProperty

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FluidCavityState.FluidCavityState

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FluidExchange.FluidExchange

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FluidExchangeProperty.FluidExchangeProperty

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FluidExchangeState.FluidExchangeState

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FluidInflator.FluidInflator

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FluidInflatorProperty.FluidInflatorProperty

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FluidInflatorState.FluidInflatorState

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.FractureCriterion.FractureCriterion

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.GapElectricalConductance.GapElectricalConductance

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.GapHeatGeneration.GapHeatGeneration

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.GeometricProperties.GeometricProperties

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.IncidentWave.IncidentWave

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.IncidentWaveProperty.IncidentWaveProperty

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.IncidentWaveState.IncidentWaveState

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.MainSecondaryAssignment.MainSecondaryAssignment

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.ModelChange.ModelChange

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.NormalBehavior.NormalBehavior

        .. autoclasstoc::


    .. autoclass:: abaqus.Interaction.PressurePenetration.PressurePenetration

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.PressurePenetrationState.PressurePenetrationState

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.Radiation.Radiation

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.RadiationToAmbient.RadiationToAmbient

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.RadiationToAmbientState.RadiationToAmbientState

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.RegionPairs.RegionPairs

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SelfContactExp.SelfContactExp

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SelfContactExpState.SelfContactExpState

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SelfContactStd.SelfContactStd

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SelfContactStdState.SelfContactStdState

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SlidingTransitionAssignment.SlidingTransitionAssignment

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SmoothingAssignment.SmoothingAssignment

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.StabilizationAssignment.StabilizationAssignment

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.StdContactControl.StdContactControl

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.StdInitialization.StdInitialization

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.StdStabilization.StdStabilization

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.StdXplCosimulation.StdXplCosimulation

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.StdXplCosimulationState.StdXplCosimulationState

        .. autoclasstoc::


    .. autoclass:: abaqus.Interaction.SurfaceFeatureAssignment.SurfaceFeatureAssignment

        .. autoclasstoc::


    .. autoclass:: abaqus.Interaction.SurfaceOffsetAssignment.SurfaceOffsetAssignment

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SurfaceThicknessAssignment.SurfaceThicknessAssignment

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SurfaceToSurfaceContactExp.SurfaceToSurfaceContactExp

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SurfaceToSurfaceContactStd.SurfaceToSurfaceContactStd

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SurfaceToSurfaceExpState.SurfaceToSurfaceExpState

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.SurfaceToSurfaceStdState.SurfaceToSurfaceStdState

        .. autoclasstoc::


    .. autoclass:: abaqus.Interaction.ThermalConductance.ThermalConductance

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.XFEMCrackGrowth.XFEMCrackGrowth

        .. autoclasstoc::

    .. autoclass:: abaqus.Interaction.XFEMCrackGrowthState.XFEMCrackGrowthState

        .. autoclasstoc::
```
