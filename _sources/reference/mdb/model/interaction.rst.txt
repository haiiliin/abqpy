===========
Interaction
===========

A specific type of interaction object and a specific type of interaction state object are designed for each type of interaction. An interaction object stores the non-propagating data of an interaction as well as a number of instances of the corresponding interaction state object, each of which stores the propagating data of the interaction in a single step. Instances of the interaction state object are created and deleted internally by its corresponding interaction object.

Create interactions
-------------------

.. autoclass:: abaqus.Interaction.InteractionModel.InteractionModel
    :members:


Object features
---------------

ContactControl
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ContactControl.ContactControl
    :members:

ContactDamage
~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ContactDamage.ContactDamage
    :members:

ContactDamping
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ContactDamping.ContactDamping
    :members:

ContactInitialization
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ContactInitialization.ContactInitialization
    :members:

ContactProperty
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ContactProperty.ContactProperty
    :members:

ContactPropertyAssignment
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ContactPropertyAssignment.ContactPropertyAssignment
    :members:

ContactStabilization
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ContactStabilization.ContactStabilization
    :members:

Interaction
~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.Interaction.Interaction
    :members:

InitializationAssignment
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.InitializationAssignment.InitializationAssignment
    :members:

InteractionProperty
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.InteractionProperty.InteractionProperty
    :members:

InteractionState
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.InteractionState.InteractionState
    :members:

AcousticImpedance
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.AcousticImpedance.AcousticImpedance
    :members:

AcousticImpedanceProp
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.AcousticImpedanceProp.AcousticImpedanceProp
    :members:

AcousticImpedanceState
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.AcousticImpedanceState.AcousticImpedanceState
    :members:

ActuatorSensor
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ActuatorSensor.ActuatorSensor
    :members:

ActuatorSensorProp
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ActuatorSensorProp.ActuatorSensorProp
    :members:

ActuatorSensorState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ActuatorSensorState.ActuatorSensorState
    :members:

CavityRadiation
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.CavityRadiation.CavityRadiation
    :members:

CavityRadiationProp
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.CavityRadiationProp.CavityRadiationProp
    :members:

CavityRadiationState
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.CavityRadiationState.CavityRadiationState
    :members:

CohesiveBehavior
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.CohesiveBehavior.CohesiveBehavior
    :members:

ConcentratedFilmCondition
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ConcentratedFilmCondition.ConcentratedFilmCondition
    :members:

ConcentratedFilmConditionState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ConcentratedFilmConditionState.ConcentratedFilmConditionState
    :members:

ConcentratedRadiationToAmbient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ConcentratedRadiationToAmbient.ConcentratedRadiationToAmbient
    :members:

ConcentratedRadiationToAmbientState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ConcentratedRadiationToAmbientState.ConcentratedRadiationToAmbientState
    :members:

ContactExp
~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ContactExp.ContactExp
    :members:

ContactStd
~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ContactStd.ContactStd
    :members:

ContactTangentialBehavior
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ContactTangentialBehavior.ContactTangentialBehavior
    :members:

CyclicSymmetry
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.CyclicSymmetry.CyclicSymmetry
    :members:

CyclicSymmetryState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.CyclicSymmetryState.CyclicSymmetryState
    :members:

ElasticFoundation
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ElasticFoundation.ElasticFoundation
    :members:

ElasticFoundationState
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ElasticFoundationState.ElasticFoundationState
    :members:

ExpContactControl
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ExpContactControl.ExpContactControl
    :members:

FilmCondition
~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.FilmCondition.FilmCondition
    :members:

FilmConditionProp
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.FilmConditionProp.FilmConditionProp
    :members:

FilmConditionState
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.FilmConditionState.FilmConditionState
    :members:

FluidCavity
~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.FluidCavity.FluidCavity
    :members:

FluidCavityProperty
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.FluidCavityProperty.FluidCavityProperty
    :members:

FluidCavityState
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.FluidCavityState.FluidCavityState
    :members:

FluidExchange
~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.FluidExchange.FluidExchange
    :members:

FluidExchangeProperty
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.FluidExchangeProperty.FluidExchangeProperty
    :members:

FluidExchangeState
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.FluidExchangeState.FluidExchangeState
    :members:

FractureCriterion
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.FractureCriterion.FractureCriterion
    :members:

GapElectricalConductance
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.GapElectricalConductance.GapElectricalConductance
    :members:

GapHeatGeneration
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.GapHeatGeneration.GapHeatGeneration
    :members:

GeometricProperties
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.GeometricProperties.GeometricProperties
    :members:

IncidentWave
~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.IncidentWave.IncidentWave
    :members:

IncidentWaveProperty
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.IncidentWaveProperty.IncidentWaveProperty
    :members:

IncidentWaveState
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.IncidentWaveState.IncidentWaveState
    :members:

MainSecondaryAssignment
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.MainSecondaryAssignment.MainSecondaryAssignment
    :members:

ModelChange
~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ModelChange.ModelChange
    :members:

NormalBehavior
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.NormalBehavior.NormalBehavior
    :members:


PressurePenetration
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.PressurePenetration.PressurePenetration
    :members:

PressurePenetrationState
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.PressurePenetrationState.PressurePenetrationState
    :members:

Radiation
~~~~~~~~~

.. autoclass:: abaqus.Interaction.Radiation.Radiation
    :members:

RadiationToAmbient
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.RadiationToAmbient.RadiationToAmbient
    :members:

RadiationToAmbientState
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.RadiationToAmbientState.RadiationToAmbientState
    :members:

RegionPairs
~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.RegionPairs.RegionPairs
    :members:

SelfContactExp
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.SelfContactExp.SelfContactExp
    :members:

SelfContactExpState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.SelfContactExpState.SelfContactExpState
    :members:

SelfContactStd
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.SelfContactStd.SelfContactStd
    :members:

SelfContactStdState
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.SelfContactStdState.SelfContactStdState
    :members:

SlidingTransitionAssignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.SlidingTransitionAssignment.SlidingTransitionAssignment
    :members:

SmoothingAssignment
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.SmoothingAssignment.SmoothingAssignment
    :members:

StabilizationAssignment
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.StabilizationAssignment.StabilizationAssignment
    :members:

StdContactControl
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.StdContactControl.StdContactControl
    :members:

StdInitialization
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.StdInitialization.StdInitialization
    :members:

StdStabilization
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.StdStabilization.StdStabilization
    :members:

StdXplCosimulation
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.StdXplCosimulation.StdXplCosimulation
    :members:

StdXplCosimulationState
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.StdXplCosimulationState.StdXplCosimulationState
    :members:


SurfaceFeatureAssignment
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.SurfaceFeatureAssignment.SurfaceFeatureAssignment
    :members:


SurfaceOffsetAssignment
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.SurfaceOffsetAssignment.SurfaceOffsetAssignment
    :members:

SurfaceThicknessAssignment
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.SurfaceThicknessAssignment.SurfaceThicknessAssignment
    :members:

SurfaceToSurfaceContactExp
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.SurfaceToSurfaceContactExp.SurfaceToSurfaceContactExp
    :members:

SurfaceToSurfaceContactStd
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.SurfaceToSurfaceContactStd.SurfaceToSurfaceContactStd
    :members:

SurfaceToSurfaceExpState
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.SurfaceToSurfaceExpState.SurfaceToSurfaceExpState
    :members:

SurfaceToSurfaceStdState
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.SurfaceToSurfaceStdState.SurfaceToSurfaceStdState
    :members:


ThermalConductance
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.ThermalConductance.ThermalConductance
    :members:

XFEMCrackGrowth
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.XFEMCrackGrowth.XFEMCrackGrowth
    :members:

XFEMCrackGrowthState
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.XFEMCrackGrowthState.XFEMCrackGrowthState
    :members:

