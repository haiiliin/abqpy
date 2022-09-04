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

    .. autoclasstoc::


Assign properties to the material
---------------------------------

.. autoclass:: abaqus.Material.Material.Material
    :members:

    .. autoclasstoc::


Object features
---------------

Density
~~~~~~~


Density
*******

.. autoclass:: abaqus.Material.Density.Density.Density
    :members:

    .. autoclasstoc::

Elastic
~~~~~~~


HyperElastic
************


Hyperelastic
''''''''''''

.. autoclass:: abaqus.Material.Elastic.HyperElastic.Hyperelastic.Hyperelastic
    :members:

    .. autoclasstoc::

HyperFoam
'''''''''


Hyperfoam
`````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.HyperFoam.Hyperfoam.Hyperfoam
    :members:

    .. autoclasstoc::

ViscoElastic
''''''''''''


CombinedTestData
````````````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.CombinedTestData.CombinedTestData
    :members:

    .. autoclasstoc::

Hysteresis
``````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.Hysteresis.Hysteresis
    :members:

    .. autoclasstoc::

Viscoelastic
````````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.Viscoelastic.Viscoelastic
    :members:

    .. autoclasstoc::

HypoElastic
***********


Hypoelastic
'''''''''''

.. autoclass:: abaqus.Material.Elastic.HypoElastic.Hypoelastic.Hypoelastic
    :members:

    .. autoclasstoc::

Linear
******


Elastic
'''''''

.. autoclass:: abaqus.Material.Elastic.Linear.Elastic.Elastic
    :members:

    .. autoclasstoc::

FailStrain
''''''''''

.. autoclass:: abaqus.Material.Elastic.Linear.FailStrain.FailStrain
    :members:

    .. autoclasstoc::

FailStress
''''''''''

.. autoclass:: abaqus.Material.Elastic.Linear.FailStress.FailStress
    :members:

    .. autoclasstoc::

LowDensityFoam
**************


LowDensityFoam
''''''''''''''

.. autoclass:: abaqus.Material.Elastic.LowDensityFoam.LowDensityFoam.LowDensityFoam
    :members:

    .. autoclasstoc::

Porous
******


PorousElastic
'''''''''''''

.. autoclass:: abaqus.Material.Elastic.Porous.PorousElastic.PorousElastic
    :members:

    .. autoclasstoc::

SuperElastic
************


SuperElasticity
'''''''''''''''

.. autoclass:: abaqus.Material.Elastic.SuperElastic.SuperElasticity.SuperElasticity
    :members:

    .. autoclasstoc::

Eos
~~~


DetonationPoint
***************

.. autoclass:: abaqus.Material.Eos.DetonationPoint.DetonationPoint
    :members:

    .. autoclasstoc::

Eos
***

.. autoclass:: abaqus.Material.Eos.Eos.Eos
    :members:

    .. autoclasstoc::

EosCompaction
*************

.. autoclass:: abaqus.Material.Eos.EosCompaction.EosCompaction
    :members:

    .. autoclasstoc::

evaluateMaterial
~~~~~~~~~~~~~~~~

.. automodule:: abaqus.Material.evaluateMaterial
    :members:

Gap
~~~




GapFlow
*******

.. autoclass:: abaqus.Material.Gap.GapFlow.GapFlow
    :members:

    .. autoclasstoc::

Gasket
~~~~~~


ContactArea
***********

.. autoclass:: abaqus.Material.Gasket.ContactArea.ContactArea
    :members:

    .. autoclasstoc::

GasketMembraneElastic
*********************

.. autoclass:: abaqus.Material.Gasket.GasketMembraneElastic.GasketMembraneElastic
    :members:

    .. autoclasstoc::

GasketThicknessBehavior
***********************

.. autoclass:: abaqus.Material.Gasket.GasketThicknessBehavior.GasketThicknessBehavior
    :members:

    .. autoclasstoc::

GasketTransverseShearElastic
****************************

.. autoclass:: abaqus.Material.Gasket.GasketTransverseShearElastic.GasketTransverseShearElastic
    :members:

    .. autoclasstoc::

Others
~~~~~~


Acoustic
********


AcousticMedium
''''''''''''''

.. autoclass:: abaqus.Material.Others.Acoustic.AcousticMedium.AcousticMedium
    :members:

    .. autoclasstoc::

Electromagnetic
***************


Dielectric
''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.Dielectric.Dielectric
    :members:

    .. autoclasstoc::

ElectricalConductivity
''''''''''''''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.ElectricalConductivity.ElectricalConductivity
    :members:

    .. autoclasstoc::

MagneticPermeability
''''''''''''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.MagneticPermeability.MagneticPermeability
    :members:

    .. autoclasstoc::

Piezoelectric
'''''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.Piezoelectric.Piezoelectric
    :members:

    .. autoclasstoc::

HeatTransfer
************


Conductivity
''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.Conductivity.Conductivity
    :members:

    .. autoclasstoc::

HeatGeneration
''''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.HeatGeneration.HeatGeneration
    :members:

    .. autoclasstoc::

InelasticHeatFraction
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.InelasticHeatFraction.InelasticHeatFraction
    :members:

    .. autoclasstoc::

JouleHeatFraction
'''''''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.JouleHeatFraction.JouleHeatFraction
    :members:

    .. autoclasstoc::

LatentHeat
''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.LatentHeat.LatentHeat
    :members:

    .. autoclasstoc::

SpecificHeat
''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.SpecificHeat.SpecificHeat
    :members:

    .. autoclasstoc::

Hydrodynamic
************


MassDiffusion
*************


Diffusivity
'''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.Diffusivity.Diffusivity
    :members:

    .. autoclasstoc::

PressureEffect
''''''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.PressureEffect.PressureEffect
    :members:

    .. autoclasstoc::

Solubility
''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.Solubility.Solubility
    :members:

    .. autoclasstoc::

SoretEffect
'''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.SoretEffect.SoretEffect
    :members:

    .. autoclasstoc::

Mechanical
**********


Damping
'''''''

.. autoclass:: abaqus.Material.Others.Mechanical.Damping.Damping
    :members:

    .. autoclasstoc::

Expansion
'''''''''

.. autoclass:: abaqus.Material.Others.Mechanical.Expansion.Expansion
    :members:

    .. autoclasstoc::

PoreFluidExpansion
''''''''''''''''''

.. autoclass:: abaqus.Material.Others.Mechanical.PoreFluidExpansion.PoreFluidExpansion
    :members:

    .. autoclasstoc::

Viscosity
'''''''''


Trs
```

.. autoclass:: abaqus.Material.Others.Mechanical.Viscosity.Trs.Trs
    :members:

    .. autoclasstoc::

Viscosity
`````````

.. autoclass:: abaqus.Material.Others.Mechanical.Viscosity.Viscosity.Viscosity
    :members:

    .. autoclasstoc::

PoreFluidFlow
*************


FluidLeakoff
''''''''''''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.FluidLeakoff.FluidLeakoff
    :members:

    .. autoclasstoc::

Gel
'''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Gel.Gel
    :members:

    .. autoclasstoc::

MoistureSwelling
''''''''''''''''


MoistureSwelling
````````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.MoistureSwelling.MoistureSwelling.MoistureSwelling
    :members:

    .. autoclasstoc::

Permeability
''''''''''''


Permeability
````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.Permeability.Permeability
    :members:

    .. autoclasstoc::

SaturationDependence
````````````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.SaturationDependence.SaturationDependence
    :members:

    .. autoclasstoc::

VelocityDependence
``````````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.VelocityDependence.VelocityDependence
    :members:

    .. autoclasstoc::

PorousBulkModuli
''''''''''''''''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.PorousBulkModuli.PorousBulkModuli
    :members:

    .. autoclasstoc::

Sorption
''''''''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Sorption.Sorption
    :members:

    .. autoclasstoc::

User
****


Depvar
''''''

.. autoclass:: abaqus.Material.Others.User.Depvar.Depvar
    :members:

    .. autoclasstoc::

UserDefinedField
''''''''''''''''

.. autoclass:: abaqus.Material.Others.User.UserDefinedField.UserDefinedField
    :members:

    .. autoclasstoc::

UserMaterial
''''''''''''

.. autoclass:: abaqus.Material.Others.User.UserMaterial.UserMaterial
    :members:

    .. autoclasstoc::

UserOutputVariables
'''''''''''''''''''

.. autoclass:: abaqus.Material.Others.User.UserOutputVariables.UserOutputVariables
    :members:

    .. autoclasstoc::

Plastic
~~~~~~~


Concrete
********


BrittleCracking
'''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.BrittleCracking.BrittleCracking
    :members:

    .. autoclasstoc::

BrittleFailure
''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.BrittleFailure.BrittleFailure
    :members:

    .. autoclasstoc::

BrittleShear
''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.BrittleShear.BrittleShear
    :members:

    .. autoclasstoc::

Concrete
''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.Concrete.Concrete
    :members:

    .. autoclasstoc::

ConcreteCompressionDamage
'''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteCompressionDamage.ConcreteCompressionDamage
    :members:

    .. autoclasstoc::

ConcreteCompressionHardening
''''''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteCompressionHardening.ConcreteCompressionHardening
    :members:

    .. autoclasstoc::

ConcreteDamagedPlasticity
'''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteDamagedPlasticity.ConcreteDamagedPlasticity
    :members:

    .. autoclasstoc::

ConcreteTensionDamage
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteTensionDamage.ConcreteTensionDamage
    :members:

    .. autoclasstoc::

ConcreteTensionStiffening
'''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteTensionStiffening.ConcreteTensionStiffening
    :members:

    .. autoclasstoc::

FailureRatios
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.FailureRatios.FailureRatios
    :members:

    .. autoclasstoc::

ShearRetention
''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ShearRetention.ShearRetention
    :members:

    .. autoclasstoc::

TensionStiffening
'''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.TensionStiffening.TensionStiffening
    :members:

    .. autoclasstoc::

Creep
*****


Creep
'''''

.. autoclass:: abaqus.Material.Plastic.Creep.Creep.Creep
    :members:

    .. autoclasstoc::

CriticalStateClay
*****************


ClayHardening
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.CriticalStateClay.ClayHardening.ClayHardening
    :members:

    .. autoclasstoc::

ClayPlasticity
''''''''''''''

.. autoclass:: abaqus.Material.Plastic.CriticalStateClay.ClayPlasticity.ClayPlasticity
    :members:

    .. autoclasstoc::

CrushableFoam
*************


CrushableFoam
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.CrushableFoam.CrushableFoam.CrushableFoam
    :members:

    .. autoclasstoc::

CrushableFoamHardening
''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.CrushableFoam.CrushableFoamHardening.CrushableFoamHardening
    :members:

    .. autoclasstoc::

DruckerPrager
*************


Extended
''''''''


DruckerPrager
`````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPrager.DruckerPrager
    :members:

    .. autoclasstoc::

DruckerPragerCreep
``````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPragerCreep.DruckerPragerCreep
    :members:

    .. autoclasstoc::

DruckerPragerHardening
``````````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPragerHardening.DruckerPragerHardening
    :members:

    .. autoclasstoc::

TriaxialTestData
````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.TriaxialTestData.TriaxialTestData
    :members:

    .. autoclasstoc::

ModifiedCap
'''''''''''


CapCreepCohesion
````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapCreepCohesion.CapCreepCohesion
    :members:

    .. autoclasstoc::

CapCreepConsolidation
`````````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapCreepConsolidation.CapCreepConsolidation
    :members:

    .. autoclasstoc::

CapHardening
````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapHardening.CapHardening
    :members:

    .. autoclasstoc::

CapPlasticity
`````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapPlasticity.CapPlasticity
    :members:

    .. autoclasstoc::

Metal
*****


Annealing
'''''''''


AnnealTemperature
`````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Annealing.AnnealTemperature.AnnealTemperature
    :members:

    .. autoclasstoc::

CastIron
''''''''


CastIronCompressionHardening
````````````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronCompressionHardening.CastIronCompressionHardening
    :members:

    .. autoclasstoc::

CastIronPlasticity
``````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronPlasticity.CastIronPlasticity
    :members:

    .. autoclasstoc::

CastIronTensionHardening
````````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronTensionHardening.CastIronTensionHardening
    :members:

    .. autoclasstoc::

Cyclic
''''''


CycledPlastic
`````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Cyclic.CycledPlastic.CycledPlastic
    :members:

    .. autoclasstoc::

CyclicHardening
```````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Cyclic.CyclicHardening.CyclicHardening
    :members:

    .. autoclasstoc::

Deformation
'''''''''''


DeformationPlasticity
`````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Deformation.DeformationPlasticity.DeformationPlasticity
    :members:

    .. autoclasstoc::

ORNL
''''


Ornl
````

.. autoclass:: abaqus.Material.Plastic.Metal.ORNL.Ornl.Ornl
    :members:

    .. autoclasstoc::

Porous
''''''


PorousFailureCriteria
`````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Porous.PorousFailureCriteria.PorousFailureCriteria
    :members:

    .. autoclasstoc::

PorousMetalPlasticity
`````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Porous.PorousMetalPlasticity.PorousMetalPlasticity
    :members:

    .. autoclasstoc::

VoidNucleation
``````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Porous.VoidNucleation.VoidNucleation
    :members:

    .. autoclasstoc::

RateDependent
'''''''''''''


RateDependent
`````````````

.. autoclass:: abaqus.Material.Plastic.Metal.RateDependent.RateDependent.RateDependent
    :members:

    .. autoclasstoc::

TwoLayerViscoPlasticity
'''''''''''''''''''''''


Viscous
```````

.. autoclass:: abaqus.Material.Plastic.Metal.TwoLayerViscoPlasticity.Viscous.Viscous
    :members:

    .. autoclasstoc::

MohrCoulomb
***********


MohrCoulombHardening
''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.MohrCoulomb.MohrCoulombHardening.MohrCoulombHardening
    :members:

    .. autoclasstoc::

MohrCoulombPlasticity
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.MohrCoulomb.MohrCoulombPlasticity.MohrCoulombPlasticity
    :members:

    .. autoclasstoc::

TensionCutOff
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.MohrCoulomb.TensionCutOff.TensionCutOff
    :members:

    .. autoclasstoc::

Plastic
*******

.. autoclass:: abaqus.Material.Plastic.Plastic.Plastic
    :members:

    .. autoclasstoc::

Potential
*********

.. autoclass:: abaqus.Material.Plastic.Potential.Potential
    :members:

    .. autoclasstoc::

SuperElastic
************


SuperElasticHardening
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.SuperElastic.SuperElasticHardening.SuperElasticHardening
    :members:

    .. autoclasstoc::

SuperElasticHardeningModifications
''''''''''''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.SuperElastic.SuperElasticHardeningModifications.SuperElasticHardeningModifications
    :members:

    .. autoclasstoc::

Swelling
********


Swelling
''''''''

.. autoclass:: abaqus.Material.Plastic.Swelling.Swelling.Swelling
    :members:

    .. autoclasstoc::

ProgressiveDamageFailure
~~~~~~~~~~~~~~~~~~~~~~~~


DamageEvolution
***************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageEvolution.DamageEvolution
    :members:

    .. autoclasstoc::

DamageInitiation
****************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation
    :members:

    .. autoclasstoc::

DamageStabilization
*******************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageStabilization.DamageStabilization
    :members:

    .. autoclasstoc::

DamageStabilizationCohesive
***************************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageStabilizationCohesive.DamageStabilizationCohesive
    :members:

    .. autoclasstoc::

Ratios
~~~~~~

.. autoclass:: abaqus.Material.Ratios.Ratios
    :members:

    .. autoclasstoc::

Regularization
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Material.Regularization.Regularization
    :members:

    .. autoclasstoc::

TestData
~~~~~~~~


BiaxialTestData
***************

.. autoclass:: abaqus.Material.TestData.BiaxialTestData.BiaxialTestData
    :members:

    .. autoclasstoc::

BiaxialTestDataArray
********************

.. autoclass:: abaqus.Material.TestData.BiaxialTestDataArray.BiaxialTestDataArray
    :members:

    .. autoclasstoc::

MullinsEffect
*************

.. autoclass:: abaqus.Material.TestData.MullinsEffect.MullinsEffect
    :members:

    .. autoclasstoc::

PlanarTestData
**************

.. autoclass:: abaqus.Material.TestData.PlanarTestData.PlanarTestData
    :members:

    .. autoclasstoc::

PlanarTestDataArray
*******************

.. autoclass:: abaqus.Material.TestData.PlanarTestDataArray.PlanarTestDataArray
    :members:

    .. autoclasstoc::

ShearTestData
*************

.. autoclass:: abaqus.Material.TestData.ShearTestData.ShearTestData
    :members:

    .. autoclasstoc::

SimpleShearTestData
*******************

.. autoclass:: abaqus.Material.TestData.SimpleShearTestData.SimpleShearTestData
    :members:

    .. autoclasstoc::

UniaxialTestData
****************

.. autoclass:: abaqus.Material.TestData.UniaxialTestData.UniaxialTestData
    :members:

    .. autoclasstoc::

UniaxialTestDataArray
*********************

.. autoclass:: abaqus.Material.TestData.UniaxialTestDataArray.UniaxialTestDataArray
    :members:

    .. autoclasstoc::

VolumetricTestData
******************

.. autoclass:: abaqus.Material.TestData.VolumetricTestData.VolumetricTestData
    :members:

    .. autoclasstoc::

MultiScale
~~~~~~~~~~

.. autoclass:: abaqus.Material.Multiscale.MeanFieldHomogenization.MeanFieldHomogenization
    :members:

    .. autoclasstoc::

.. autoclass:: abaqus.Material.Multiscale.MeanFieldInclusion.MeanFieldInclusion
    :members:

    .. autoclasstoc::

.. autoclass:: abaqus.Material.Multiscale.MeanFieldMatrix.MeanFieldMatrix
    :members:

    .. autoclasstoc::

.. autoclass:: abaqus.Material.Multiscale.MeanFieldVoid.MeanFieldVoid
    :members:

    .. autoclasstoc::
