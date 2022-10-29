# Material

The Material commands are used to define the materials in a model.

## Create materials

### In Mdb

```{eval-rst}
.. autoclass:: abaqus.Material.MaterialModel.MaterialModel

    .. autoclasstoc::
```

### In Odb

```{eval-rst}
.. autoclass:: abaqus.Material.MaterialOdb.MaterialOdb

    .. autoclasstoc::

```

## Assign properties to the material

```{eval-rst}
.. autoclass:: abaqus.Material.Material.Material

    .. autoclasstoc::

```

## Classes

```{eval-rst}

.. collapse:: Click here to Expand

    .. autoclass:: abaqus.Material.Density.Density.Density

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.HyperElastic.Hyperelastic.Hyperelastic

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.HyperElastic.HyperFoam.Hyperfoam.Hyperfoam

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.CombinedTestData.CombinedTestData

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.Hysteresis.Hysteresis

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.Viscoelastic.Viscoelastic

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.HypoElastic.Hypoelastic.Hypoelastic

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.Linear.Elastic.Elastic

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.Linear.FailStrain.FailStrain

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.Linear.FailStress.FailStress

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.LowDensityFoam.LowDensityFoam.LowDensityFoam

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.Porous.PorousElastic.PorousElastic

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Elastic.SuperElastic.SuperElasticity.SuperElasticity

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Eos.DetonationPoint.DetonationPoint

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Eos.Eos.Eos

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Eos.EosCompaction.EosCompaction

        .. autoclasstoc::

    .. automodule:: abaqus.Material.evaluateMaterial

    .. autoclass:: abaqus.Material.Gap.GapConductance.GapConductance

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Gap.GapConvection.GapConvection

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Gap.GapFlow.GapFlow

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Gap.GapRadiation.GapRadiation

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Gasket.ContactArea.ContactArea

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Gasket.GasketMembraneElastic.GasketMembraneElastic

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Gasket.GasketThicknessBehavior.GasketThicknessBehavior

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Gasket.GasketTransverseShearElastic.GasketTransverseShearElastic

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.Acoustic.AcousticMedium.AcousticMedium

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.Electromagnetic.Dielectric.Dielectric

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.Electromagnetic.ElectricalConductivity.ElectricalConductivity

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.Electromagnetic.MagneticPermeability.MagneticPermeability

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.Electromagnetic.Piezoelectric.Piezoelectric

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.HeatTransfer.Conductivity.Conductivity

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.HeatTransfer.HeatGeneration.HeatGeneration

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.HeatTransfer.InelasticHeatFraction.InelasticHeatFraction

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.HeatTransfer.JouleHeatFraction.JouleHeatFraction

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.HeatTransfer.LatentHeat.LatentHeat

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.HeatTransfer.SpecificHeat.SpecificHeat

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.MassDiffusion.Diffusivity.Diffusivity

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.MassDiffusion.PressureEffect.PressureEffect

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.MassDiffusion.Solubility.Solubility

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.MassDiffusion.SoretEffect.SoretEffect

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.Mechanical.Damping.Damping

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.Mechanical.Expansion.Expansion

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.Mechanical.PoreFluidExpansion.PoreFluidExpansion

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.Mechanical.Viscosity.Trs.Trs

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.Mechanical.Viscosity.Viscosity.Viscosity

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.PoreFluidFlow.FluidLeakoff.FluidLeakoff

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.PoreFluidFlow.Gel.Gel

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.PoreFluidFlow.MoistureSwelling.MoistureSwelling.MoistureSwelling

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.Permeability.Permeability

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.SaturationDependence.SaturationDependence

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.VelocityDependence.VelocityDependence

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.PoreFluidFlow.PorousBulkModuli.PorousBulkModuli

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.PoreFluidFlow.Sorption.Sorption

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.User.Depvar.Depvar

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.User.UserDefinedField.UserDefinedField

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.User.UserMaterial.UserMaterial

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Others.User.UserOutputVariables.UserOutputVariables

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.BrittleCracking.BrittleCracking

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.BrittleFailure.BrittleFailure

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.BrittleShear.BrittleShear

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.Concrete.Concrete

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteCompressionDamage.ConcreteCompressionDamage

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteCompressionHardening.ConcreteCompressionHardening

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteDamagedPlasticity.ConcreteDamagedPlasticity

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteTensionDamage.ConcreteTensionDamage

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteTensionStiffening.ConcreteTensionStiffening

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.FailureRatios.FailureRatios

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.ShearRetention.ShearRetention

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Concrete.TensionStiffening.TensionStiffening

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Creep.Creep.Creep

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.CriticalStateClay.ClayHardening.ClayHardening

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.CriticalStateClay.ClayPlasticity.ClayPlasticity

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.CrushableFoam.CrushableFoam.CrushableFoam

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.CrushableFoam.CrushableFoamHardening.CrushableFoamHardening

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.CrushStress.CrushStress.CrushStress

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.CrushStress.CrushStressVelocityFactor.CrushStressVelocityFactor

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPrager.DruckerPrager

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPragerCreep.DruckerPragerCreep

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPragerHardening.DruckerPragerHardening

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.TriaxialTestData.TriaxialTestData

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapCreepCohesion.CapCreepCohesion

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapCreepConsolidation.CapCreepConsolidation

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapHardening.CapHardening

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapPlasticity.CapPlasticity

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.Annealing.AnnealTemperature.AnnealTemperature

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronCompressionHardening.CastIronCompressionHardening

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronPlasticity.CastIronPlasticity

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronTensionHardening.CastIronTensionHardening

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.Cyclic.CycledPlastic.CycledPlastic

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.Cyclic.CyclicHardening.CyclicHardening

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.Deformation.DeformationPlasticity.DeformationPlasticity

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.ORNL.Ornl.Ornl

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.Porous.PorousFailureCriteria.PorousFailureCriteria

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.Porous.PorousMetalPlasticity.PorousMetalPlasticity

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.Porous.VoidNucleation.VoidNucleation

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.RateDependent.RateDependent.RateDependent

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Metal.TwoLayerViscoPlasticity.Viscous.Viscous

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.MohrCoulomb.MohrCoulombHardening.MohrCoulombHardening

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.MohrCoulomb.MohrCoulombPlasticity.MohrCoulombPlasticity

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.MohrCoulomb.TensionCutOff.TensionCutOff

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Plastic.Plastic

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Potential.Potential

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.SuperElastic.SuperElasticHardening.SuperElasticHardening

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.SuperElastic.SuperElasticHardeningModifications.SuperElasticHardeningModifications

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.Swelling.Swelling.Swelling

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Plastic.TensileFailure.TensileFailure

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageEvolution.DamageEvolution

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageStabilization.DamageStabilization

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageStabilizationCohesive.DamageStabilizationCohesive

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Ratios.Ratios

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Regularization.Regularization

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.TestData.BiaxialTestData.BiaxialTestData

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.TestData.BiaxialTestDataArray.BiaxialTestDataArray

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.TestData.MullinsEffect.MullinsEffect

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.TestData.PlanarTestData.PlanarTestData

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.TestData.PlanarTestDataArray.PlanarTestDataArray

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.TestData.ShearTestData.ShearTestData

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.TestData.SimpleShearTestData.SimpleShearTestData

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.TestData.UniaxialTestData.UniaxialTestData

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.TestData.UniaxialTestDataArray.UniaxialTestDataArray

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.TestData.VolumetricTestData.VolumetricTestData

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Multiscale.MeanFieldHomogenization.MeanFieldHomogenization

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Multiscale.MeanFieldInclusion.MeanFieldInclusion

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Multiscale.MeanFieldMatrix.MeanFieldMatrix

        .. autoclasstoc::

    .. autoclass:: abaqus.Material.Multiscale.MeanFieldVoid.MeanFieldVoid

        .. autoclasstoc::
```
