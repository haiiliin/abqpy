# Material

The Material commands are used to define the materials in a model.

## Create materials

### In Mdb

```{eval-rst}
.. autoclass:: abaqus.Material.MaterialModel.MaterialModel
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### In Odb

```{eval-rst}
.. autoclass:: abaqus.Material.MaterialOdb.MaterialOdb
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

```

## Assign properties to the material

```{eval-rst}
.. autoclass:: abaqus.Material.Material.Material
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

```

## Other Classes

```{eval-rst}

.. collapse:: Click here to Expand

    .. autoclass:: abaqus.Material.Density.Density.Density
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.HyperElastic.Hyperelastic.Hyperelastic
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.HyperElastic.HyperFoam.Hyperfoam.Hyperfoam
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.CombinedTestData.CombinedTestData
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.Hysteresis.Hysteresis
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.Viscoelastic.Viscoelastic
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.HypoElastic.Hypoelastic.Hypoelastic
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.Linear.Elastic.Elastic
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.Linear.FailStrain.FailStrain
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.Linear.FailStress.FailStress
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.LowDensityFoam.LowDensityFoam.LowDensityFoam
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.Porous.PorousElastic.PorousElastic
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.SuperElastic.SuperElasticity.SuperElasticity
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Eos.DetonationPoint.DetonationPoint
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Eos.Eos.Eos
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Eos.EosCompaction.EosCompaction
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. automodule:: abaqus.Material.evaluateMaterial
        :members:
        :special-members: __init__
        :show-inheritance:

    .. autoclass:: abaqus.Material.Gap.GapConductance.GapConductance
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Gap.GapConvection.GapConvection
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Gap.GapFlow.GapFlow
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Gap.GapRadiation.GapRadiation
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Gasket.ContactArea.ContactArea
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Gasket.GasketMembraneElastic.GasketMembraneElastic
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Gasket.GasketThicknessBehavior.GasketThicknessBehavior
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Gasket.GasketTransverseShearElastic.GasketTransverseShearElastic
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.Acoustic.AcousticMedium.AcousticMedium
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.Electromagnetic.Dielectric.Dielectric
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.Electromagnetic.ElectricalConductivity.ElectricalConductivity
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.Electromagnetic.MagneticPermeability.MagneticPermeability
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.Electromagnetic.Piezoelectric.Piezoelectric
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.HeatTransfer.Conductivity.Conductivity
        :members:
        :special-members: __init__
        :show-inheritance:

<<<<<<< HEAD


=======
        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.HeatTransfer.HeatGeneration.HeatGeneration
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.HeatTransfer.InelasticHeatFraction.InelasticHeatFraction
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.HeatTransfer.JouleHeatFraction.JouleHeatFraction
        :members:
        :special-members: __init__
        :show-inheritance:
>>>>>>> 27c50e7e ([docs]: Collapse unimportant classes (#3425))

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.HeatTransfer.LatentHeat.LatentHeat
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

<<<<<<< HEAD
### Gasket


#### ContactArea
=======
    .. autoclass:: abaqus.Material.Others.HeatTransfer.SpecificHeat.SpecificHeat
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.MassDiffusion.Diffusivity.Diffusivity
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.MassDiffusion.PressureEffect.PressureEffect
        :members:
        :special-members: __init__
        :show-inheritance:
>>>>>>> 27c50e7e ([docs]: Collapse unimportant classes (#3425))

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.MassDiffusion.Solubility.Solubility
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.MassDiffusion.SoretEffect.SoretEffect
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.Mechanical.Damping.Damping
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.Mechanical.Expansion.Expansion
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.Mechanical.PoreFluidExpansion.PoreFluidExpansion
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.Mechanical.Viscosity.Trs.Trs
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.Mechanical.Viscosity.Viscosity.Viscosity
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.PoreFluidFlow.FluidLeakoff.FluidLeakoff
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.PoreFluidFlow.Gel.Gel
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.PoreFluidFlow.MoistureSwelling.MoistureSwelling.MoistureSwelling
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.Permeability.Permeability
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.SaturationDependence.SaturationDependence
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.VelocityDependence.VelocityDependence
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.PoreFluidFlow.PorousBulkModuli.PorousBulkModuli
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.PoreFluidFlow.Sorption.Sorption
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.User.Depvar.Depvar
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.User.UserDefinedField.UserDefinedField
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.User.UserMaterial.UserMaterial
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.User.UserOutputVariables.UserOutputVariables
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.BrittleCracking.BrittleCracking
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.BrittleFailure.BrittleFailure
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.BrittleShear.BrittleShear
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.Concrete.Concrete
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteCompressionDamage.ConcreteCompressionDamage
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteCompressionHardening.ConcreteCompressionHardening
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteDamagedPlasticity.ConcreteDamagedPlasticity
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteTensionDamage.ConcreteTensionDamage
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteTensionStiffening.ConcreteTensionStiffening
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.FailureRatios.FailureRatios
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.ShearRetention.ShearRetention
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.TensionStiffening.TensionStiffening
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Creep.Creep.Creep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.CriticalStateClay.ClayHardening.ClayHardening
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.CriticalStateClay.ClayPlasticity.ClayPlasticity
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.CrushableFoam.CrushableFoam.CrushableFoam
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

<<<<<<< HEAD
    .. autoclasstoc::
```

##### Viscosity

###### Trs

```{eval-rst}
.. autoclass:: abaqus.Material.Others.Mechanical.Viscosity.Trs.Trs
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

###### Viscosity

```{eval-rst}
.. autoclass:: abaqus.Material.Others.Mechanical.Viscosity.Viscosity.Viscosity
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### PoreFluidFlow

##### FluidLeakoff

```{eval-rst}
.. autoclass:: abaqus.Material.Others.PoreFluidFlow.FluidLeakoff.FluidLeakoff
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### Gel

```{eval-rst}
.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Gel.Gel
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### MoistureSwelling

###### MoistureSwelling

```{eval-rst}
.. autoclass:: abaqus.Material.Others.PoreFluidFlow.MoistureSwelling.MoistureSwelling.MoistureSwelling
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### Permeability

###### Permeability

```{eval-rst}
.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.Permeability.Permeability
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

###### SaturationDependence

```{eval-rst}
.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.SaturationDependence.SaturationDependence
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

###### VelocityDependence

```{eval-rst}
.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.VelocityDependence.VelocityDependence
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### PorousBulkModuli

```{eval-rst}
.. autoclass:: abaqus.Material.Others.PoreFluidFlow.PorousBulkModuli.PorousBulkModuli
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### Sorption

```{eval-rst}
.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Sorption.Sorption
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### User

##### Depvar

```{eval-rst}
.. autoclass:: abaqus.Material.Others.User.Depvar.Depvar
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### UserDefinedField

```{eval-rst}
.. autoclass:: abaqus.Material.Others.User.UserDefinedField.UserDefinedField
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### UserMaterial

```{eval-rst}
.. autoclass:: abaqus.Material.Others.User.UserMaterial.UserMaterial
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### UserOutputVariables

```{eval-rst}
.. autoclass:: abaqus.Material.Others.User.UserOutputVariables.UserOutputVariables
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### Plastic

#### Concrete

##### BrittleCracking

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.Concrete.BrittleCracking.BrittleCracking
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### BrittleFailure

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.Concrete.BrittleFailure.BrittleFailure
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### BrittleShear

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.Concrete.BrittleShear.BrittleShear
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### Concrete

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.Concrete.Concrete.Concrete
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### ConcreteCompressionDamage

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteCompressionDamage.ConcreteCompressionDamage
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### ConcreteCompressionHardening

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteCompressionHardening.ConcreteCompressionHardening
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### ConcreteDamagedPlasticity

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteDamagedPlasticity.ConcreteDamagedPlasticity
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### ConcreteTensionDamage

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteTensionDamage.ConcreteTensionDamage
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### ConcreteTensionStiffening

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteTensionStiffening.ConcreteTensionStiffening
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### FailureRatios

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.Concrete.FailureRatios.FailureRatios
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### ShearRetention

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.Concrete.ShearRetention.ShearRetention
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### TensionStiffening

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.Concrete.TensionStiffening.TensionStiffening
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### Creep

##### Creep

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.Creep.Creep.Creep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### CriticalStateClay

##### ClayHardening

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.CriticalStateClay.ClayHardening.ClayHardening
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### ClayPlasticity

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.CriticalStateClay.ClayPlasticity.ClayPlasticity
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### CrushableFoam

##### CrushableFoam

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.CrushableFoam.CrushableFoam.CrushableFoam
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### CrushableFoamHardening

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.CrushableFoam.CrushableFoamHardening.CrushableFoamHardening
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### DruckerPrager

##### Extended

###### DruckerPrager

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPrager.DruckerPrager
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

###### DruckerPragerCreep

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPragerCreep.DruckerPragerCreep
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

###### DruckerPragerHardening

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPragerHardening.DruckerPragerHardening
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

###### TriaxialTestData

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.TriaxialTestData.TriaxialTestData
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### ModifiedCap

###### CapCreepCohesion

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapCreepCohesion.CapCreepCohesion
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

###### CapCreepConsolidation

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapCreepConsolidation.CapCreepConsolidation
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

###### CapHardening

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapHardening.CapHardening
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

###### CapPlasticity

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapPlasticity.CapPlasticity
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

#### Metal

##### Annealing

###### AnnealTemperature

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.Metal.Annealing.AnnealTemperature.AnnealTemperature
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

##### CastIron

###### CastIronCompressionHardening

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronCompressionHardening.CastIronCompressionHardening
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

###### CastIronPlasticity

```{eval-rst}
.. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronPlasticity.CastIronPlasticity
    :members:
    :special-members: __init__
    :show-inheritance:
=======
    .. autoclass:: abaqus.Material.Plastic.CrushableFoam.CrushableFoamHardening.CrushableFoamHardening
        :members:
        :special-members: __init__
        :show-inheritance:
>>>>>>> 27c50e7e ([docs]: Collapse unimportant classes (#3425))

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.CrushStress.CrushStress.CrushStress
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.CrushStress.CrushStressVelocityFactor.CrushStressVelocityFactor
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPrager.DruckerPrager
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPragerCreep.DruckerPragerCreep
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPragerHardening.DruckerPragerHardening
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.TriaxialTestData.TriaxialTestData
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapCreepCohesion.CapCreepCohesion
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapCreepConsolidation.CapCreepConsolidation
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapHardening.CapHardening
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapPlasticity.CapPlasticity
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.Annealing.AnnealTemperature.AnnealTemperature
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronCompressionHardening.CastIronCompressionHardening
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronPlasticity.CastIronPlasticity
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronTensionHardening.CastIronTensionHardening
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.Cyclic.CycledPlastic.CycledPlastic
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.Cyclic.CyclicHardening.CyclicHardening
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.Deformation.DeformationPlasticity.DeformationPlasticity
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.ORNL.Ornl.Ornl
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.Porous.PorousFailureCriteria.PorousFailureCriteria
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.Porous.PorousMetalPlasticity.PorousMetalPlasticity
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.Porous.VoidNucleation.VoidNucleation
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

<<<<<<< HEAD
### ProgressiveDamageFailure


#### DamageEvolution
=======
    .. autoclass:: abaqus.Material.Plastic.Metal.RateDependent.RateDependent.RateDependent
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.TwoLayerViscoPlasticity.Viscous.Viscous
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.MohrCoulomb.MohrCoulombHardening.MohrCoulombHardening
        :members:
        :special-members: __init__
        :show-inheritance:
>>>>>>> 27c50e7e ([docs]: Collapse unimportant classes (#3425))

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.MohrCoulomb.MohrCoulombPlasticity.MohrCoulombPlasticity
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.MohrCoulomb.TensionCutOff.TensionCutOff
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Plastic.Plastic
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Potential.Potential
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.SuperElastic.SuperElasticHardening.SuperElasticHardening
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.SuperElastic.SuperElasticHardeningModifications.SuperElasticHardeningModifications
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Swelling.Swelling.Swelling
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.TensileFailure.TensileFailure
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageEvolution.DamageEvolution
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageStabilization.DamageStabilization
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageStabilizationCohesive.DamageStabilizationCohesive
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Ratios.Ratios
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Regularization.Regularization
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.TestData.BiaxialTestData.BiaxialTestData
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.TestData.BiaxialTestDataArray.BiaxialTestDataArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.TestData.MullinsEffect.MullinsEffect
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.TestData.PlanarTestData.PlanarTestData
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.TestData.PlanarTestDataArray.PlanarTestDataArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.TestData.ShearTestData.ShearTestData
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.TestData.SimpleShearTestData.SimpleShearTestData
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.TestData.UniaxialTestData.UniaxialTestData
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.TestData.UniaxialTestDataArray.UniaxialTestDataArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

<<<<<<< HEAD
    .. autoclasstoc::
=======
    .. autoclass:: abaqus.Material.TestData.VolumetricTestData.VolumetricTestData
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Multiscale.MeanFieldHomogenization.MeanFieldHomogenization
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Multiscale.MeanFieldInclusion.MeanFieldInclusion
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Multiscale.MeanFieldMatrix.MeanFieldMatrix
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Multiscale.MeanFieldVoid.MeanFieldVoid
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::
>>>>>>> 27c50e7e ([docs]: Collapse unimportant classes (#3425))
```
