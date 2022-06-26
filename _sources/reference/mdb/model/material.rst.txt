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

    .. autoclassdoc::


Object features
---------------

Density
~~~~~~~


Density
*******

.. autoclass:: abaqus.Material.Density.Density.Density
    :members:

    .. autoclassdoc::

Elastic
~~~~~~~


HyperElastic
************


Hyperelastic
''''''''''''

.. autoclass:: abaqus.Material.Elastic.HyperElastic.Hyperelastic.Hyperelastic
    :members:

    .. autoclassdoc::

HyperFoam
'''''''''


Hyperfoam
`````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.HyperFoam.Hyperfoam.Hyperfoam
    :members:

    .. autoclassdoc::

ViscoElastic
''''''''''''


CombinedTestData
````````````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.CombinedTestData.CombinedTestData
    :members:

    .. autoclassdoc::

Hysteresis
``````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.Hysteresis.Hysteresis
    :members:

    .. autoclassdoc::

Viscoelastic
````````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.Viscoelastic.Viscoelastic
    :members:

    .. autoclassdoc::

HypoElastic
***********


Hypoelastic
'''''''''''

.. autoclass:: abaqus.Material.Elastic.HypoElastic.Hypoelastic.Hypoelastic
    :members:

    .. autoclassdoc::

Linear
******


Elastic
'''''''

.. autoclass:: abaqus.Material.Elastic.Linear.Elastic.Elastic
    :members:

    .. autoclassdoc::

FailStrain
''''''''''

.. autoclass:: abaqus.Material.Elastic.Linear.FailStrain.FailStrain
    :members:

    .. autoclassdoc::

FailStress
''''''''''

.. autoclass:: abaqus.Material.Elastic.Linear.FailStress.FailStress
    :members:

    .. autoclassdoc::

LowDensityFoam
**************


LowDensityFoam
''''''''''''''

.. autoclass:: abaqus.Material.Elastic.LowDensityFoam.LowDensityFoam.LowDensityFoam
    :members:

    .. autoclassdoc::

Porous
******


PorousElastic
'''''''''''''

.. autoclass:: abaqus.Material.Elastic.Porous.PorousElastic.PorousElastic
    :members:

    .. autoclassdoc::

SuperElastic
************


SuperElasticity
'''''''''''''''

.. autoclass:: abaqus.Material.Elastic.SuperElastic.SuperElasticity.SuperElasticity
    :members:

    .. autoclassdoc::

Eos
~~~


DetonationPoint
***************

.. autoclass:: abaqus.Material.Eos.DetonationPoint.DetonationPoint
    :members:

    .. autoclassdoc::

Eos
***

.. autoclass:: abaqus.Material.Eos.Eos.Eos
    :members:

    .. autoclassdoc::

EosCompaction
*************

.. autoclass:: abaqus.Material.Eos.EosCompaction.EosCompaction
    :members:

    .. autoclassdoc::

evaluateMaterial
~~~~~~~~~~~~~~~~

.. automodule:: abaqus.Material.evaluateMaterial
    :members:

    .. autoclassdoc::

Gap
~~~




GapFlow
*******

.. autoclass:: abaqus.Material.Gap.GapFlow.GapFlow
    :members:

    .. autoclassdoc::

Gasket
~~~~~~


ContactArea
***********

.. autoclass:: abaqus.Material.Gasket.ContactArea.ContactArea
    :members:

    .. autoclassdoc::

GasketMembraneElastic
*********************

.. autoclass:: abaqus.Material.Gasket.GasketMembraneElastic.GasketMembraneElastic
    :members:

    .. autoclassdoc::

GasketThicknessBehavior
***********************

.. autoclass:: abaqus.Material.Gasket.GasketThicknessBehavior.GasketThicknessBehavior
    :members:

    .. autoclassdoc::

GasketTransverseShearElastic
****************************

.. autoclass:: abaqus.Material.Gasket.GasketTransverseShearElastic.GasketTransverseShearElastic
    :members:

    .. autoclassdoc::

Others
~~~~~~


Acoustic
********


AcousticMedium
''''''''''''''

.. autoclass:: abaqus.Material.Others.Acoustic.AcousticMedium.AcousticMedium
    :members:

    .. autoclassdoc::

Electromagnetic
***************


Dielectric
''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.Dielectric.Dielectric
    :members:

    .. autoclassdoc::

ElectricalConductivity
''''''''''''''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.ElectricalConductivity.ElectricalConductivity
    :members:

    .. autoclassdoc::

MagneticPermeability
''''''''''''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.MagneticPermeability.MagneticPermeability
    :members:

    .. autoclassdoc::

Piezoelectric
'''''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.Piezoelectric.Piezoelectric
    :members:

    .. autoclassdoc::

HeatTransfer
************


Conductivity
''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.Conductivity.Conductivity
    :members:

    .. autoclassdoc::

HeatGeneration
''''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.HeatGeneration.HeatGeneration
    :members:

    .. autoclassdoc::

InelasticHeatFraction
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.InelasticHeatFraction.InelasticHeatFraction
    :members:

    .. autoclassdoc::

JouleHeatFraction
'''''''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.JouleHeatFraction.JouleHeatFraction
    :members:

    .. autoclassdoc::

LatentHeat
''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.LatentHeat.LatentHeat
    :members:

    .. autoclassdoc::

SpecificHeat
''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.SpecificHeat.SpecificHeat
    :members:

    .. autoclassdoc::

Hydrodynamic
************


MassDiffusion
*************


Diffusivity
'''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.Diffusivity.Diffusivity
    :members:

    .. autoclassdoc::

PressureEffect
''''''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.PressureEffect.PressureEffect
    :members:

    .. autoclassdoc::

Solubility
''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.Solubility.Solubility
    :members:

    .. autoclassdoc::

SoretEffect
'''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.SoretEffect.SoretEffect
    :members:

    .. autoclassdoc::

Mechanical
**********


Damping
'''''''

.. autoclass:: abaqus.Material.Others.Mechanical.Damping.Damping
    :members:

    .. autoclassdoc::

Expansion
'''''''''

.. autoclass:: abaqus.Material.Others.Mechanical.Expansion.Expansion
    :members:

    .. autoclassdoc::

PoreFluidExpansion
''''''''''''''''''

.. autoclass:: abaqus.Material.Others.Mechanical.PoreFluidExpansion.PoreFluidExpansion
    :members:

    .. autoclassdoc::

Viscosity
'''''''''


Trs
```

.. autoclass:: abaqus.Material.Others.Mechanical.Viscosity.Trs.Trs
    :members:

    .. autoclassdoc::

Viscosity
`````````

.. autoclass:: abaqus.Material.Others.Mechanical.Viscosity.Viscosity.Viscosity
    :members:

    .. autoclassdoc::

PoreFluidFlow
*************


FluidLeakoff
''''''''''''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.FluidLeakoff.FluidLeakoff
    :members:

    .. autoclassdoc::

Gel
'''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Gel.Gel
    :members:

    .. autoclassdoc::

MoistureSwelling
''''''''''''''''


MoistureSwelling
````````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.MoistureSwelling.MoistureSwelling.MoistureSwelling
    :members:

    .. autoclassdoc::

Permeability
''''''''''''


Permeability
````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.Permeability.Permeability
    :members:

    .. autoclassdoc::

SaturationDependence
````````````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.SaturationDependence.SaturationDependence
    :members:

    .. autoclassdoc::

VelocityDependence
``````````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.VelocityDependence.VelocityDependence
    :members:

    .. autoclassdoc::

PorousBulkModuli
''''''''''''''''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.PorousBulkModuli.PorousBulkModuli
    :members:

    .. autoclassdoc::

Sorption
''''''''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Sorption.Sorption
    :members:

    .. autoclassdoc::

User
****


Depvar
''''''

.. autoclass:: abaqus.Material.Others.User.Depvar.Depvar
    :members:

    .. autoclassdoc::

UserDefinedField
''''''''''''''''

.. autoclass:: abaqus.Material.Others.User.UserDefinedField.UserDefinedField
    :members:

    .. autoclassdoc::

UserMaterial
''''''''''''

.. autoclass:: abaqus.Material.Others.User.UserMaterial.UserMaterial
    :members:

    .. autoclassdoc::

UserOutputVariables
'''''''''''''''''''

.. autoclass:: abaqus.Material.Others.User.UserOutputVariables.UserOutputVariables
    :members:

    .. autoclassdoc::

Plastic
~~~~~~~


Concrete
********


BrittleCracking
'''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.BrittleCracking.BrittleCracking
    :members:

    .. autoclassdoc::

BrittleFailure
''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.BrittleFailure.BrittleFailure
    :members:

    .. autoclassdoc::

BrittleShear
''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.BrittleShear.BrittleShear
    :members:

    .. autoclassdoc::

Concrete
''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.Concrete.Concrete
    :members:

    .. autoclassdoc::

ConcreteCompressionDamage
'''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteCompressionDamage.ConcreteCompressionDamage
    :members:

    .. autoclassdoc::

ConcreteCompressionHardening
''''''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteCompressionHardening.ConcreteCompressionHardening
    :members:

    .. autoclassdoc::

ConcreteDamagedPlasticity
'''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteDamagedPlasticity.ConcreteDamagedPlasticity
    :members:

    .. autoclassdoc::

ConcreteTensionDamage
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteTensionDamage.ConcreteTensionDamage
    :members:

    .. autoclassdoc::

ConcreteTensionStiffening
'''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteTensionStiffening.ConcreteTensionStiffening
    :members:

    .. autoclassdoc::

FailureRatios
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.FailureRatios.FailureRatios
    :members:

    .. autoclassdoc::

ShearRetention
''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ShearRetention.ShearRetention
    :members:

    .. autoclassdoc::

TensionStiffening
'''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.TensionStiffening.TensionStiffening
    :members:

    .. autoclassdoc::

Creep
*****


Creep
'''''

.. autoclass:: abaqus.Material.Plastic.Creep.Creep.Creep
    :members:

    .. autoclassdoc::

CriticalStateClay
*****************


ClayHardening
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.CriticalStateClay.ClayHardening.ClayHardening
    :members:

    .. autoclassdoc::

ClayPlasticity
''''''''''''''

.. autoclass:: abaqus.Material.Plastic.CriticalStateClay.ClayPlasticity.ClayPlasticity
    :members:

    .. autoclassdoc::

CrushableFoam
*************


CrushableFoam
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.CrushableFoam.CrushableFoam.CrushableFoam
    :members:

    .. autoclassdoc::

CrushableFoamHardening
''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.CrushableFoam.CrushableFoamHardening.CrushableFoamHardening
    :members:

    .. autoclassdoc::

DruckerPrager
*************


Extended
''''''''


DruckerPrager
`````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPrager.DruckerPrager
    :members:

    .. autoclassdoc::

DruckerPragerCreep
``````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPragerCreep.DruckerPragerCreep
    :members:

    .. autoclassdoc::

DruckerPragerHardening
``````````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPragerHardening.DruckerPragerHardening
    :members:

    .. autoclassdoc::

TriaxialTestData
````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.TriaxialTestData.TriaxialTestData
    :members:

    .. autoclassdoc::

ModifiedCap
'''''''''''


CapCreepCohesion
````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapCreepCohesion.CapCreepCohesion
    :members:

    .. autoclassdoc::

CapCreepConsolidation
`````````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapCreepConsolidation.CapCreepConsolidation
    :members:

    .. autoclassdoc::

CapHardening
````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapHardening.CapHardening
    :members:

    .. autoclassdoc::

CapPlasticity
`````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapPlasticity.CapPlasticity
    :members:

    .. autoclassdoc::

Metal
*****


Annealing
'''''''''


AnnealTemperature
`````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Annealing.AnnealTemperature.AnnealTemperature
    :members:

    .. autoclassdoc::

CastIron
''''''''


CastIronCompressionHardening
````````````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronCompressionHardening.CastIronCompressionHardening
    :members:

    .. autoclassdoc::

CastIronPlasticity
``````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronPlasticity.CastIronPlasticity
    :members:

    .. autoclassdoc::

CastIronTensionHardening
````````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronTensionHardening.CastIronTensionHardening
    :members:

    .. autoclassdoc::

Cyclic
''''''


CycledPlastic
`````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Cyclic.CycledPlastic.CycledPlastic
    :members:

    .. autoclassdoc::

CyclicHardening
```````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Cyclic.CyclicHardening.CyclicHardening
    :members:

    .. autoclassdoc::

Deformation
'''''''''''


DeformationPlasticity
`````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Deformation.DeformationPlasticity.DeformationPlasticity
    :members:

    .. autoclassdoc::

ORNL
''''


Ornl
````

.. autoclass:: abaqus.Material.Plastic.Metal.ORNL.Ornl.Ornl
    :members:

    .. autoclassdoc::

Porous
''''''


PorousFailureCriteria
`````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Porous.PorousFailureCriteria.PorousFailureCriteria
    :members:

    .. autoclassdoc::

PorousMetalPlasticity
`````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Porous.PorousMetalPlasticity.PorousMetalPlasticity
    :members:

    .. autoclassdoc::

VoidNucleation
``````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Porous.VoidNucleation.VoidNucleation
    :members:

    .. autoclassdoc::

RateDependent
'''''''''''''


RateDependent
`````````````

.. autoclass:: abaqus.Material.Plastic.Metal.RateDependent.RateDependent.RateDependent
    :members:

    .. autoclassdoc::

TwoLayerViscoPlasticity
'''''''''''''''''''''''


Viscous
```````

.. autoclass:: abaqus.Material.Plastic.Metal.TwoLayerViscoPlasticity.Viscous.Viscous
    :members:

    .. autoclassdoc::

MohrCoulomb
***********


MohrCoulombHardening
''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.MohrCoulomb.MohrCoulombHardening.MohrCoulombHardening
    :members:

    .. autoclassdoc::

MohrCoulombPlasticity
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.MohrCoulomb.MohrCoulombPlasticity.MohrCoulombPlasticity
    :members:

    .. autoclassdoc::

TensionCutOff
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.MohrCoulomb.TensionCutOff.TensionCutOff
    :members:

    .. autoclassdoc::

Plastic
*******

.. autoclass:: abaqus.Material.Plastic.Plastic.Plastic
    :members:

    .. autoclassdoc::

Potential
*********

.. autoclass:: abaqus.Material.Plastic.Potential.Potential
    :members:

    .. autoclassdoc::

SuperElastic
************


SuperElasticHardening
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.SuperElastic.SuperElasticHardening.SuperElasticHardening
    :members:

    .. autoclassdoc::

SuperElasticHardeningModifications
''''''''''''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.SuperElastic.SuperElasticHardeningModifications.SuperElasticHardeningModifications
    :members:

    .. autoclassdoc::

Swelling
********


Swelling
''''''''

.. autoclass:: abaqus.Material.Plastic.Swelling.Swelling.Swelling
    :members:

    .. autoclassdoc::

ProgressiveDamageFailure
~~~~~~~~~~~~~~~~~~~~~~~~


DamageEvolution
***************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageEvolution.DamageEvolution
    :members:

    .. autoclassdoc::

DamageInitiation
****************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation
    :members:

    .. autoclassdoc::

DamageStabilization
*******************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageStabilization.DamageStabilization
    :members:

    .. autoclassdoc::

DamageStabilizationCohesive
***************************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageStabilizationCohesive.DamageStabilizationCohesive
    :members:

    .. autoclassdoc::

Ratios
~~~~~~

.. autoclass:: abaqus.Material.Ratios.Ratios
    :members:

    .. autoclassdoc::

Regularization
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Material.Regularization.Regularization
    :members:

    .. autoclassdoc::

TestData
~~~~~~~~


BiaxialTestData
***************

.. autoclass:: abaqus.Material.TestData.BiaxialTestData.BiaxialTestData
    :members:

    .. autoclassdoc::

BiaxialTestDataArray
********************

.. autoclass:: abaqus.Material.TestData.BiaxialTestDataArray.BiaxialTestDataArray
    :members:

    .. autoclassdoc::

MullinsEffect
*************

.. autoclass:: abaqus.Material.TestData.MullinsEffect.MullinsEffect
    :members:

    .. autoclassdoc::

PlanarTestData
**************

.. autoclass:: abaqus.Material.TestData.PlanarTestData.PlanarTestData
    :members:

    .. autoclassdoc::

PlanarTestDataArray
*******************

.. autoclass:: abaqus.Material.TestData.PlanarTestDataArray.PlanarTestDataArray
    :members:

    .. autoclassdoc::

ShearTestData
*************

.. autoclass:: abaqus.Material.TestData.ShearTestData.ShearTestData
    :members:

    .. autoclassdoc::

SimpleShearTestData
*******************

.. autoclass:: abaqus.Material.TestData.SimpleShearTestData.SimpleShearTestData
    :members:

    .. autoclassdoc::

UniaxialTestData
****************

.. autoclass:: abaqus.Material.TestData.UniaxialTestData.UniaxialTestData
    :members:

    .. autoclassdoc::

UniaxialTestDataArray
*********************

.. autoclass:: abaqus.Material.TestData.UniaxialTestDataArray.UniaxialTestDataArray
    :members:

    .. autoclassdoc::

VolumetricTestData
******************

.. autoclass:: abaqus.Material.TestData.VolumetricTestData.VolumetricTestData
    :members:

    .. autoclassdoc::
