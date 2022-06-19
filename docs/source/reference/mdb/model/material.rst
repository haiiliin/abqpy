========
Material
========

The Material commands are used to define the materials in a model.

Create materials
-----------------

In Mdb
~~~~~~

.. autoclass:: abaqus.Material.MaterialModel.MaterialModel
    :members:

In Odb
~~~~~~

.. autoclass:: abaqus.Material.MaterialOdb.MaterialOdb
    :members:


Assign properties to the material
---------------------------------

.. autoclass:: abaqus.Material.Material.Material
    :members:


Object features
---------------

Material
~~~~~~~~

.. autoclass:: abaqus.Material.Material.Material
    :members:
    :inherited-members:

Density
~~~~~~~


Density
*******

.. autoclass:: abaqus.Material.Density.Density.Density

Elastic
~~~~~~~


HyperElastic
************


Hyperelastic
''''''''''''

.. autoclass:: abaqus.Material.Elastic.HyperElastic.Hyperelastic.Hyperelastic

HyperFoam
'''''''''


Hyperfoam
`````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.HyperFoam.Hyperfoam.Hyperfoam

ViscoElastic
''''''''''''


CombinedTestData
````````````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.CombinedTestData.CombinedTestData

Hysteresis
``````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.Hysteresis.Hysteresis

Viscoelastic
````````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.Viscoelastic.Viscoelastic

HypoElastic
***********


Hypoelastic
'''''''''''

.. autoclass:: abaqus.Material.Elastic.HypoElastic.Hypoelastic.Hypoelastic

Linear
******


Elastic
'''''''

.. autoclass:: abaqus.Material.Elastic.Linear.Elastic.Elastic

FailStrain
''''''''''

.. autoclass:: abaqus.Material.Elastic.Linear.FailStrain.FailStrain

FailStress
''''''''''

.. autoclass:: abaqus.Material.Elastic.Linear.FailStress.FailStress

LowDensityFoam
**************


LowDensityFoam
''''''''''''''

.. autoclass:: abaqus.Material.Elastic.LowDensityFoam.LowDensityFoam.LowDensityFoam

Porous
******


PorousElastic
'''''''''''''

.. autoclass:: abaqus.Material.Elastic.Porous.PorousElastic.PorousElastic

SuperElastic
************


SuperElasticity
'''''''''''''''

.. autoclass:: abaqus.Material.Elastic.SuperElastic.SuperElasticity.SuperElasticity

Eos
~~~


DetonationPoint
***************

.. autoclass:: abaqus.Material.Eos.DetonationPoint.DetonationPoint

Eos
***

.. autoclass:: abaqus.Material.Eos.Eos.Eos

EosCompaction
*************

.. autoclass:: abaqus.Material.Eos.EosCompaction.EosCompaction

evaluateMaterial
~~~~~~~~~~~~~~~~

.. automodule:: abaqus.Material.evaluateMaterial
    :members:

Gap
~~~




GapFlow
*******

.. autoclass:: abaqus.Material.Gap.GapFlow.GapFlow

Gasket
~~~~~~


ContactArea
***********

.. autoclass:: abaqus.Material.Gasket.ContactArea.ContactArea

GasketMembraneElastic
*********************

.. autoclass:: abaqus.Material.Gasket.GasketMembraneElastic.GasketMembraneElastic

GasketThicknessBehavior
***********************

.. autoclass:: abaqus.Material.Gasket.GasketThicknessBehavior.GasketThicknessBehavior

GasketTransverseShearElastic
****************************

.. autoclass:: abaqus.Material.Gasket.GasketTransverseShearElastic.GasketTransverseShearElastic

Others
~~~~~~


Acoustic
********


AcousticMedium
''''''''''''''

.. autoclass:: abaqus.Material.Others.Acoustic.AcousticMedium.AcousticMedium

Electromagnetic
***************


Dielectric
''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.Dielectric.Dielectric

ElectricalConductivity
''''''''''''''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.ElectricalConductivity.ElectricalConductivity

MagneticPermeability
''''''''''''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.MagneticPermeability.MagneticPermeability

Piezoelectric
'''''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.Piezoelectric.Piezoelectric

HeatTransfer
************


Conductivity
''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.Conductivity.Conductivity

HeatGeneration
''''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.HeatGeneration.HeatGeneration

InelasticHeatFraction
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.InelasticHeatFraction.InelasticHeatFraction

JouleHeatFraction
'''''''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.JouleHeatFraction.JouleHeatFraction

LatentHeat
''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.LatentHeat.LatentHeat

SpecificHeat
''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.SpecificHeat.SpecificHeat

Hydrodynamic
************


MassDiffusion
*************


Diffusivity
'''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.Diffusivity.Diffusivity

PressureEffect
''''''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.PressureEffect.PressureEffect

Solubility
''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.Solubility.Solubility

SoretEffect
'''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.SoretEffect.SoretEffect

Mechanical
**********


Damping
'''''''

.. autoclass:: abaqus.Material.Others.Mechanical.Damping.Damping

Expansion
'''''''''

.. autoclass:: abaqus.Material.Others.Mechanical.Expansion.Expansion

PoreFluidExpansion
''''''''''''''''''

.. autoclass:: abaqus.Material.Others.Mechanical.PoreFluidExpansion.PoreFluidExpansion

Viscosity
'''''''''


Trs
```

.. autoclass:: abaqus.Material.Others.Mechanical.Viscosity.Trs.Trs

Viscosity
`````````

.. autoclass:: abaqus.Material.Others.Mechanical.Viscosity.Viscosity.Viscosity

PoreFluidFlow
*************


FluidLeakoff
''''''''''''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.FluidLeakoff.FluidLeakoff

Gel
'''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Gel.Gel

MoistureSwelling
''''''''''''''''


MoistureSwelling
````````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.MoistureSwelling.MoistureSwelling.MoistureSwelling

Permeability
''''''''''''


Permeability
````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.Permeability.Permeability

SaturationDependence
````````````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.SaturationDependence.SaturationDependence

VelocityDependence
``````````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.VelocityDependence.VelocityDependence

PorousBulkModuli
''''''''''''''''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.PorousBulkModuli.PorousBulkModuli

Sorption
''''''''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Sorption.Sorption

User
****


Depvar
''''''

.. autoclass:: abaqus.Material.Others.User.Depvar.Depvar

UserDefinedField
''''''''''''''''

.. autoclass:: abaqus.Material.Others.User.UserDefinedField.UserDefinedField

UserMaterial
''''''''''''

.. autoclass:: abaqus.Material.Others.User.UserMaterial.UserMaterial

UserOutputVariables
'''''''''''''''''''

.. autoclass:: abaqus.Material.Others.User.UserOutputVariables.UserOutputVariables

Plastic
~~~~~~~


Concrete
********


BrittleCracking
'''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.BrittleCracking.BrittleCracking

BrittleFailure
''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.BrittleFailure.BrittleFailure

BrittleShear
''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.BrittleShear.BrittleShear

Concrete
''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.Concrete.Concrete

ConcreteCompressionDamage
'''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteCompressionDamage.ConcreteCompressionDamage

ConcreteCompressionHardening
''''''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteCompressionHardening.ConcreteCompressionHardening

ConcreteDamagedPlasticity
'''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteDamagedPlasticity.ConcreteDamagedPlasticity

ConcreteTensionDamage
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteTensionDamage.ConcreteTensionDamage

ConcreteTensionStiffening
'''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteTensionStiffening.ConcreteTensionStiffening

FailureRatios
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.FailureRatios.FailureRatios

ShearRetention
''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ShearRetention.ShearRetention

TensionStiffening
'''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.TensionStiffening.TensionStiffening

Creep
*****


Creep
'''''

.. autoclass:: abaqus.Material.Plastic.Creep.Creep.Creep

CriticalStateClay
*****************


ClayHardening
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.CriticalStateClay.ClayHardening.ClayHardening

ClayPlasticity
''''''''''''''

.. autoclass:: abaqus.Material.Plastic.CriticalStateClay.ClayPlasticity.ClayPlasticity

CrushableFoam
*************


CrushableFoam
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.CrushableFoam.CrushableFoam.CrushableFoam

CrushableFoamHardening
''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.CrushableFoam.CrushableFoamHardening.CrushableFoamHardening

DruckerPrager
*************


Extended
''''''''


DruckerPrager
`````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPrager.DruckerPrager

DruckerPragerCreep
``````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPragerCreep.DruckerPragerCreep

DruckerPragerHardening
``````````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPragerHardening.DruckerPragerHardening

TriaxialTestData
````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.TriaxialTestData.TriaxialTestData

ModifiedCap
'''''''''''


CapCreepCohesion
````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapCreepCohesion.CapCreepCohesion

CapCreepConsolidation
`````````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapCreepConsolidation.CapCreepConsolidation

CapHardening
````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapHardening.CapHardening

CapPlasticity
`````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapPlasticity.CapPlasticity

Metal
*****


Annealing
'''''''''


AnnealTemperature
`````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Annealing.AnnealTemperature.AnnealTemperature

CastIron
''''''''


CastIronCompressionHardening
````````````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronCompressionHardening.CastIronCompressionHardening

CastIronPlasticity
``````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronPlasticity.CastIronPlasticity

CastIronTensionHardening
````````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronTensionHardening.CastIronTensionHardening

Cyclic
''''''


CycledPlastic
`````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Cyclic.CycledPlastic.CycledPlastic

CyclicHardening
```````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Cyclic.CyclicHardening.CyclicHardening

Deformation
'''''''''''


DeformationPlasticity
`````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Deformation.DeformationPlasticity.DeformationPlasticity

ORNL
''''


Ornl
````

.. autoclass:: abaqus.Material.Plastic.Metal.ORNL.Ornl.Ornl

Porous
''''''


PorousFailureCriteria
`````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Porous.PorousFailureCriteria.PorousFailureCriteria

PorousMetalPlasticity
`````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Porous.PorousMetalPlasticity.PorousMetalPlasticity

VoidNucleation
``````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Porous.VoidNucleation.VoidNucleation

RateDependent
'''''''''''''


RateDependent
`````````````

.. autoclass:: abaqus.Material.Plastic.Metal.RateDependent.RateDependent.RateDependent

TwoLayerViscoPlasticity
'''''''''''''''''''''''


Viscous
```````

.. autoclass:: abaqus.Material.Plastic.Metal.TwoLayerViscoPlasticity.Viscous.Viscous

MohrCoulomb
***********


MohrCoulombHardening
''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.MohrCoulomb.MohrCoulombHardening.MohrCoulombHardening

MohrCoulombPlasticity
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.MohrCoulomb.MohrCoulombPlasticity.MohrCoulombPlasticity

TensionCutOff
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.MohrCoulomb.TensionCutOff.TensionCutOff

Plastic
*******

.. autoclass:: abaqus.Material.Plastic.Plastic.Plastic

Potential
*********

.. autoclass:: abaqus.Material.Plastic.Potential.Potential

SuperElastic
************


SuperElasticHardening
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.SuperElastic.SuperElasticHardening.SuperElasticHardening

SuperElasticHardeningModifications
''''''''''''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.SuperElastic.SuperElasticHardeningModifications.SuperElasticHardeningModifications

Swelling
********


Swelling
''''''''

.. autoclass:: abaqus.Material.Plastic.Swelling.Swelling.Swelling

ProgressiveDamageFailure
~~~~~~~~~~~~~~~~~~~~~~~~


DamageEvolution
***************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageEvolution.DamageEvolution

DamageInitiation
****************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation

DamageStabilization
*******************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageStabilization.DamageStabilization

DamageStabilizationCohesive
***************************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageStabilizationCohesive.DamageStabilizationCohesive

Ratios
~~~~~~

.. autoclass:: abaqus.Material.Ratios.Ratios

Regularization
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Material.Regularization.Regularization

TestData
~~~~~~~~


BiaxialTestData
***************

.. autoclass:: abaqus.Material.TestData.BiaxialTestData.BiaxialTestData

BiaxialTestDataArray
********************

.. autoclass:: abaqus.Material.TestData.BiaxialTestDataArray.BiaxialTestDataArray

MullinsEffect
*************

.. autoclass:: abaqus.Material.TestData.MullinsEffect.MullinsEffect

PlanarTestData
**************

.. autoclass:: abaqus.Material.TestData.PlanarTestData.PlanarTestData

PlanarTestDataArray
*******************

.. autoclass:: abaqus.Material.TestData.PlanarTestDataArray.PlanarTestDataArray

ShearTestData
*************

.. autoclass:: abaqus.Material.TestData.ShearTestData.ShearTestData

SimpleShearTestData
*******************

.. autoclass:: abaqus.Material.TestData.SimpleShearTestData.SimpleShearTestData

UniaxialTestData
****************

.. autoclass:: abaqus.Material.TestData.UniaxialTestData.UniaxialTestData

UniaxialTestDataArray
*********************

.. autoclass:: abaqus.Material.TestData.UniaxialTestDataArray.UniaxialTestDataArray

VolumetricTestData
******************

.. autoclass:: abaqus.Material.TestData.VolumetricTestData.VolumetricTestData
