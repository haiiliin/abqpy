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
    :special-members: __init__

In Odb
~~~~~~

.. autoclass:: abaqus.Material.MaterialOdb.MaterialOdb
    :members:
    :special-members: __init__

    .. autoclasstoc::


Assign properties to the material
---------------------------------

.. autoclass:: abaqus.Material.Material.Material
    :members:
    :special-members: __init__

    .. autoclasstoc::


Object features
---------------

Density
~~~~~~~


Density
*******

.. autoclass:: abaqus.Material.Density.Density.Density
    :members:
    :special-members: __init__

    .. autoclasstoc::

Elastic
~~~~~~~


HyperElastic
************


Hyperelastic
''''''''''''

.. autoclass:: abaqus.Material.Elastic.HyperElastic.Hyperelastic.Hyperelastic
    :members:
    :special-members: __init__

    .. autoclasstoc::

HyperFoam
'''''''''


Hyperfoam
`````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.HyperFoam.Hyperfoam.Hyperfoam
    :members:
    :special-members: __init__

    .. autoclasstoc::

ViscoElastic
''''''''''''


CombinedTestData
````````````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.CombinedTestData.CombinedTestData
    :members:
    :special-members: __init__

    .. autoclasstoc::

Hysteresis
``````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.Hysteresis.Hysteresis
    :members:
    :special-members: __init__

    .. autoclasstoc::

Viscoelastic
````````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.Viscoelastic.Viscoelastic
    :members:
    :special-members: __init__

    .. autoclasstoc::

HypoElastic
***********


Hypoelastic
'''''''''''

.. autoclass:: abaqus.Material.Elastic.HypoElastic.Hypoelastic.Hypoelastic
    :members:
    :special-members: __init__

    .. autoclasstoc::

Linear
******


Elastic
'''''''

.. autoclass:: abaqus.Material.Elastic.Linear.Elastic.Elastic
    :members:
    :special-members: __init__

    .. autoclasstoc::

FailStrain
''''''''''

.. autoclass:: abaqus.Material.Elastic.Linear.FailStrain.FailStrain
    :members:
    :special-members: __init__

    .. autoclasstoc::

FailStress
''''''''''

.. autoclass:: abaqus.Material.Elastic.Linear.FailStress.FailStress
    :members:
    :special-members: __init__

    .. autoclasstoc::

LowDensityFoam
**************


LowDensityFoam
''''''''''''''

.. autoclass:: abaqus.Material.Elastic.LowDensityFoam.LowDensityFoam.LowDensityFoam
    :members:
    :special-members: __init__

    .. autoclasstoc::

Porous
******


PorousElastic
'''''''''''''

.. autoclass:: abaqus.Material.Elastic.Porous.PorousElastic.PorousElastic
    :members:
    :special-members: __init__

    .. autoclasstoc::

SuperElastic
************


SuperElasticity
'''''''''''''''

.. autoclass:: abaqus.Material.Elastic.SuperElastic.SuperElasticity.SuperElasticity
    :members:
    :special-members: __init__

    .. autoclasstoc::

Eos
~~~


DetonationPoint
***************

.. autoclass:: abaqus.Material.Eos.DetonationPoint.DetonationPoint
    :members:
    :special-members: __init__

    .. autoclasstoc::

Eos
***

.. autoclass:: abaqus.Material.Eos.Eos.Eos
    :members:
    :special-members: __init__

    .. autoclasstoc::

EosCompaction
*************

.. autoclass:: abaqus.Material.Eos.EosCompaction.EosCompaction
    :members:
    :special-members: __init__

    .. autoclasstoc::

evaluateMaterial
~~~~~~~~~~~~~~~~

.. automodule:: abaqus.Material.evaluateMaterial
    :members:
    :special-members: __init__

Gap
~~~


<<<<<<< HEAD

=======
.. autoclass:: abaqus.Material.Gap.GapConductance.GapConductance
    :members:
    :special-members: __init__

    .. autoclasstoc::

GapConvection
*************

.. autoclass:: abaqus.Material.Gap.GapConvection.GapConvection
    :members:
    :special-members: __init__

    .. autoclasstoc::
>>>>>>> bbd46fa6 (Add special members of classes in the documentation (#2640))

GapFlow
*******

.. autoclass:: abaqus.Material.Gap.GapFlow.GapFlow
    :members:
    :special-members: __init__

    .. autoclasstoc::

<<<<<<< HEAD
=======
GapRadiation
************

.. autoclass:: abaqus.Material.Gap.GapRadiation.GapRadiation
    :members:
    :special-members: __init__

    .. autoclasstoc::

>>>>>>> bbd46fa6 (Add special members of classes in the documentation (#2640))
Gasket
~~~~~~


ContactArea
***********

.. autoclass:: abaqus.Material.Gasket.ContactArea.ContactArea
    :members:
    :special-members: __init__

    .. autoclasstoc::

GasketMembraneElastic
*********************

.. autoclass:: abaqus.Material.Gasket.GasketMembraneElastic.GasketMembraneElastic
    :members:
    :special-members: __init__

    .. autoclasstoc::

GasketThicknessBehavior
***********************

.. autoclass:: abaqus.Material.Gasket.GasketThicknessBehavior.GasketThicknessBehavior
    :members:
    :special-members: __init__

    .. autoclasstoc::

GasketTransverseShearElastic
****************************

.. autoclass:: abaqus.Material.Gasket.GasketTransverseShearElastic.GasketTransverseShearElastic
    :members:
    :special-members: __init__

    .. autoclasstoc::

Others
~~~~~~


Acoustic
********


AcousticMedium
''''''''''''''

.. autoclass:: abaqus.Material.Others.Acoustic.AcousticMedium.AcousticMedium
    :members:
    :special-members: __init__

    .. autoclasstoc::

Electromagnetic
***************


Dielectric
''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.Dielectric.Dielectric
    :members:
    :special-members: __init__

    .. autoclasstoc::

ElectricalConductivity
''''''''''''''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.ElectricalConductivity.ElectricalConductivity
    :members:
    :special-members: __init__

    .. autoclasstoc::

MagneticPermeability
''''''''''''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.MagneticPermeability.MagneticPermeability
    :members:
    :special-members: __init__

    .. autoclasstoc::

Piezoelectric
'''''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.Piezoelectric.Piezoelectric
    :members:
    :special-members: __init__

    .. autoclasstoc::

HeatTransfer
************


Conductivity
''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.Conductivity.Conductivity
    :members:
    :special-members: __init__

    .. autoclasstoc::

HeatGeneration
''''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.HeatGeneration.HeatGeneration
    :members:
    :special-members: __init__

    .. autoclasstoc::

InelasticHeatFraction
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.InelasticHeatFraction.InelasticHeatFraction
    :members:
    :special-members: __init__

    .. autoclasstoc::

JouleHeatFraction
'''''''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.JouleHeatFraction.JouleHeatFraction
    :members:
    :special-members: __init__

    .. autoclasstoc::

LatentHeat
''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.LatentHeat.LatentHeat
    :members:
    :special-members: __init__

    .. autoclasstoc::

SpecificHeat
''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.SpecificHeat.SpecificHeat
    :members:
    :special-members: __init__

    .. autoclasstoc::

Hydrodynamic
************


MassDiffusion
*************


Diffusivity
'''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.Diffusivity.Diffusivity
    :members:
    :special-members: __init__

    .. autoclasstoc::

PressureEffect
''''''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.PressureEffect.PressureEffect
    :members:
    :special-members: __init__

    .. autoclasstoc::

Solubility
''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.Solubility.Solubility
    :members:
    :special-members: __init__

    .. autoclasstoc::

SoretEffect
'''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.SoretEffect.SoretEffect
    :members:
    :special-members: __init__

    .. autoclasstoc::

Mechanical
**********


Damping
'''''''

.. autoclass:: abaqus.Material.Others.Mechanical.Damping.Damping
    :members:
    :special-members: __init__

    .. autoclasstoc::

Expansion
'''''''''

.. autoclass:: abaqus.Material.Others.Mechanical.Expansion.Expansion
    :members:
    :special-members: __init__

    .. autoclasstoc::

PoreFluidExpansion
''''''''''''''''''

.. autoclass:: abaqus.Material.Others.Mechanical.PoreFluidExpansion.PoreFluidExpansion
    :members:
    :special-members: __init__

    .. autoclasstoc::

Viscosity
'''''''''


Trs
```

.. autoclass:: abaqus.Material.Others.Mechanical.Viscosity.Trs.Trs
    :members:
    :special-members: __init__

    .. autoclasstoc::

Viscosity
`````````

.. autoclass:: abaqus.Material.Others.Mechanical.Viscosity.Viscosity.Viscosity
    :members:
    :special-members: __init__

    .. autoclasstoc::

PoreFluidFlow
*************


FluidLeakoff
''''''''''''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.FluidLeakoff.FluidLeakoff
    :members:
    :special-members: __init__

    .. autoclasstoc::

Gel
'''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Gel.Gel
    :members:
    :special-members: __init__

    .. autoclasstoc::

MoistureSwelling
''''''''''''''''


MoistureSwelling
````````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.MoistureSwelling.MoistureSwelling.MoistureSwelling
    :members:
    :special-members: __init__

    .. autoclasstoc::

Permeability
''''''''''''


Permeability
````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.Permeability.Permeability
    :members:
    :special-members: __init__

    .. autoclasstoc::

SaturationDependence
````````````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.SaturationDependence.SaturationDependence
    :members:
    :special-members: __init__

    .. autoclasstoc::

VelocityDependence
``````````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.VelocityDependence.VelocityDependence
    :members:
    :special-members: __init__

    .. autoclasstoc::

PorousBulkModuli
''''''''''''''''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.PorousBulkModuli.PorousBulkModuli
    :members:
    :special-members: __init__

    .. autoclasstoc::

Sorption
''''''''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Sorption.Sorption
    :members:
    :special-members: __init__

    .. autoclasstoc::

User
****


Depvar
''''''

.. autoclass:: abaqus.Material.Others.User.Depvar.Depvar
    :members:
    :special-members: __init__

    .. autoclasstoc::

UserDefinedField
''''''''''''''''

.. autoclass:: abaqus.Material.Others.User.UserDefinedField.UserDefinedField
    :members:
    :special-members: __init__

    .. autoclasstoc::

UserMaterial
''''''''''''

.. autoclass:: abaqus.Material.Others.User.UserMaterial.UserMaterial
    :members:
    :special-members: __init__

    .. autoclasstoc::

UserOutputVariables
'''''''''''''''''''

.. autoclass:: abaqus.Material.Others.User.UserOutputVariables.UserOutputVariables
    :members:
    :special-members: __init__

    .. autoclasstoc::

Plastic
~~~~~~~


Concrete
********


BrittleCracking
'''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.BrittleCracking.BrittleCracking
    :members:
    :special-members: __init__

    .. autoclasstoc::

BrittleFailure
''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.BrittleFailure.BrittleFailure
    :members:
    :special-members: __init__

    .. autoclasstoc::

BrittleShear
''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.BrittleShear.BrittleShear
    :members:
    :special-members: __init__

    .. autoclasstoc::

Concrete
''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.Concrete.Concrete
    :members:
    :special-members: __init__

    .. autoclasstoc::

ConcreteCompressionDamage
'''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteCompressionDamage.ConcreteCompressionDamage
    :members:
    :special-members: __init__

    .. autoclasstoc::

ConcreteCompressionHardening
''''''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteCompressionHardening.ConcreteCompressionHardening
    :members:
    :special-members: __init__

    .. autoclasstoc::

ConcreteDamagedPlasticity
'''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteDamagedPlasticity.ConcreteDamagedPlasticity
    :members:
    :special-members: __init__

    .. autoclasstoc::

ConcreteTensionDamage
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteTensionDamage.ConcreteTensionDamage
    :members:
    :special-members: __init__

    .. autoclasstoc::

ConcreteTensionStiffening
'''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteTensionStiffening.ConcreteTensionStiffening
    :members:
    :special-members: __init__

    .. autoclasstoc::

FailureRatios
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.FailureRatios.FailureRatios
    :members:
    :special-members: __init__

    .. autoclasstoc::

ShearRetention
''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ShearRetention.ShearRetention
    :members:
    :special-members: __init__

    .. autoclasstoc::

TensionStiffening
'''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.TensionStiffening.TensionStiffening
    :members:
    :special-members: __init__

    .. autoclasstoc::

Creep
*****


Creep
'''''

.. autoclass:: abaqus.Material.Plastic.Creep.Creep.Creep
    :members:
    :special-members: __init__

    .. autoclasstoc::

CriticalStateClay
*****************


ClayHardening
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.CriticalStateClay.ClayHardening.ClayHardening
    :members:
    :special-members: __init__

    .. autoclasstoc::

ClayPlasticity
''''''''''''''

.. autoclass:: abaqus.Material.Plastic.CriticalStateClay.ClayPlasticity.ClayPlasticity
    :members:
    :special-members: __init__

    .. autoclasstoc::

CrushableFoam
*************


CrushableFoam
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.CrushableFoam.CrushableFoam.CrushableFoam
    :members:
    :special-members: __init__

    .. autoclasstoc::

CrushableFoamHardening
''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.CrushableFoam.CrushableFoamHardening.CrushableFoamHardening
    :members:
    :special-members: __init__

    .. autoclasstoc::

<<<<<<< HEAD
=======
CrushStress
*************

CrushStress
'''''''''''

.. autoclass:: abaqus.Material.Plastic.CrushStress.CrushStress.CrushStress
    :members:
    :special-members: __init__

    .. autoclasstoc::

CrushStressVelocityFactor
'''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.CrushStress.CrushStressVelocityFactor.CrushStressVelocityFactor
    :members:
    :special-members: __init__

    .. autoclasstoc::

>>>>>>> bbd46fa6 (Add special members of classes in the documentation (#2640))
DruckerPrager
*************


Extended
''''''''


DruckerPrager
`````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPrager.DruckerPrager
    :members:
    :special-members: __init__

    .. autoclasstoc::

DruckerPragerCreep
``````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPragerCreep.DruckerPragerCreep
    :members:
    :special-members: __init__

    .. autoclasstoc::

DruckerPragerHardening
``````````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPragerHardening.DruckerPragerHardening
    :members:
    :special-members: __init__

    .. autoclasstoc::

TriaxialTestData
````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.TriaxialTestData.TriaxialTestData
    :members:
    :special-members: __init__

    .. autoclasstoc::

ModifiedCap
'''''''''''


CapCreepCohesion
````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapCreepCohesion.CapCreepCohesion
    :members:
    :special-members: __init__

    .. autoclasstoc::

CapCreepConsolidation
`````````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapCreepConsolidation.CapCreepConsolidation
    :members:
    :special-members: __init__

    .. autoclasstoc::

CapHardening
````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapHardening.CapHardening
    :members:
    :special-members: __init__

    .. autoclasstoc::

CapPlasticity
`````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapPlasticity.CapPlasticity
    :members:
    :special-members: __init__

    .. autoclasstoc::

Metal
*****


Annealing
'''''''''


AnnealTemperature
`````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Annealing.AnnealTemperature.AnnealTemperature
    :members:
    :special-members: __init__

    .. autoclasstoc::

CastIron
''''''''


CastIronCompressionHardening
````````````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronCompressionHardening.CastIronCompressionHardening
    :members:
    :special-members: __init__

    .. autoclasstoc::

CastIronPlasticity
``````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronPlasticity.CastIronPlasticity
    :members:
    :special-members: __init__

    .. autoclasstoc::

CastIronTensionHardening
````````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronTensionHardening.CastIronTensionHardening
    :members:
    :special-members: __init__

    .. autoclasstoc::

Cyclic
''''''


CycledPlastic
`````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Cyclic.CycledPlastic.CycledPlastic
    :members:
    :special-members: __init__

    .. autoclasstoc::

CyclicHardening
```````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Cyclic.CyclicHardening.CyclicHardening
    :members:
    :special-members: __init__

    .. autoclasstoc::

Deformation
'''''''''''


DeformationPlasticity
`````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Deformation.DeformationPlasticity.DeformationPlasticity
    :members:
    :special-members: __init__

    .. autoclasstoc::

ORNL
''''


Ornl
````

.. autoclass:: abaqus.Material.Plastic.Metal.ORNL.Ornl.Ornl
    :members:
    :special-members: __init__

    .. autoclasstoc::

Porous
''''''


PorousFailureCriteria
`````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Porous.PorousFailureCriteria.PorousFailureCriteria
    :members:
    :special-members: __init__

    .. autoclasstoc::

PorousMetalPlasticity
`````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Porous.PorousMetalPlasticity.PorousMetalPlasticity
    :members:
    :special-members: __init__

    .. autoclasstoc::

VoidNucleation
``````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Porous.VoidNucleation.VoidNucleation
    :members:
    :special-members: __init__

    .. autoclasstoc::

RateDependent
'''''''''''''


RateDependent
`````````````

.. autoclass:: abaqus.Material.Plastic.Metal.RateDependent.RateDependent.RateDependent
    :members:
    :special-members: __init__

    .. autoclasstoc::

TwoLayerViscoPlasticity
'''''''''''''''''''''''


Viscous
```````

.. autoclass:: abaqus.Material.Plastic.Metal.TwoLayerViscoPlasticity.Viscous.Viscous
    :members:
    :special-members: __init__

    .. autoclasstoc::

MohrCoulomb
***********


MohrCoulombHardening
''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.MohrCoulomb.MohrCoulombHardening.MohrCoulombHardening
    :members:
    :special-members: __init__

    .. autoclasstoc::

MohrCoulombPlasticity
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.MohrCoulomb.MohrCoulombPlasticity.MohrCoulombPlasticity
    :members:
    :special-members: __init__

    .. autoclasstoc::

TensionCutOff
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.MohrCoulomb.TensionCutOff.TensionCutOff
    :members:
    :special-members: __init__

    .. autoclasstoc::

Plastic
*******

.. autoclass:: abaqus.Material.Plastic.Plastic.Plastic
    :members:
    :special-members: __init__

    .. autoclasstoc::

Potential
*********

.. autoclass:: abaqus.Material.Plastic.Potential.Potential
    :members:
    :special-members: __init__

    .. autoclasstoc::

SuperElastic
************


SuperElasticHardening
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.SuperElastic.SuperElasticHardening.SuperElasticHardening
    :members:
    :special-members: __init__

    .. autoclasstoc::

SuperElasticHardeningModifications
''''''''''''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.SuperElastic.SuperElasticHardeningModifications.SuperElasticHardeningModifications
    :members:
    :special-members: __init__

    .. autoclasstoc::

Swelling
********


Swelling
''''''''

.. autoclass:: abaqus.Material.Plastic.Swelling.Swelling.Swelling
    :members:
    :special-members: __init__

    .. autoclasstoc::

<<<<<<< HEAD
=======
TensileFailure
**************

.. autoclass:: abaqus.Material.Plastic.TensileFailure.TensileFailure
    :members:
    :special-members: __init__

    .. autoclasstoc::

>>>>>>> bbd46fa6 (Add special members of classes in the documentation (#2640))
ProgressiveDamageFailure
~~~~~~~~~~~~~~~~~~~~~~~~


DamageEvolution
***************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageEvolution.DamageEvolution
    :members:
    :special-members: __init__

    .. autoclasstoc::

DamageInitiation
****************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation
    :members:
    :special-members: __init__

    .. autoclasstoc::

DamageStabilization
*******************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageStabilization.DamageStabilization
    :members:
    :special-members: __init__

    .. autoclasstoc::

DamageStabilizationCohesive
***************************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageStabilizationCohesive.DamageStabilizationCohesive
    :members:
    :special-members: __init__

    .. autoclasstoc::

Ratios
~~~~~~

.. autoclass:: abaqus.Material.Ratios.Ratios
    :members:
    :special-members: __init__

    .. autoclasstoc::

Regularization
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Material.Regularization.Regularization
    :members:
    :special-members: __init__

    .. autoclasstoc::

TestData
~~~~~~~~


BiaxialTestData
***************

.. autoclass:: abaqus.Material.TestData.BiaxialTestData.BiaxialTestData
    :members:
    :special-members: __init__

    .. autoclasstoc::

BiaxialTestDataArray
********************

.. autoclass:: abaqus.Material.TestData.BiaxialTestDataArray.BiaxialTestDataArray
    :members:
    :special-members: __init__

    .. autoclasstoc::

MullinsEffect
*************

.. autoclass:: abaqus.Material.TestData.MullinsEffect.MullinsEffect
    :members:
    :special-members: __init__

    .. autoclasstoc::

PlanarTestData
**************

.. autoclass:: abaqus.Material.TestData.PlanarTestData.PlanarTestData
    :members:
    :special-members: __init__

    .. autoclasstoc::

PlanarTestDataArray
*******************

.. autoclass:: abaqus.Material.TestData.PlanarTestDataArray.PlanarTestDataArray
    :members:
    :special-members: __init__

    .. autoclasstoc::

ShearTestData
*************

.. autoclass:: abaqus.Material.TestData.ShearTestData.ShearTestData
    :members:
    :special-members: __init__

    .. autoclasstoc::

SimpleShearTestData
*******************

.. autoclass:: abaqus.Material.TestData.SimpleShearTestData.SimpleShearTestData
    :members:
    :special-members: __init__

    .. autoclasstoc::

UniaxialTestData
****************

.. autoclass:: abaqus.Material.TestData.UniaxialTestData.UniaxialTestData
    :members:
    :special-members: __init__

    .. autoclasstoc::

UniaxialTestDataArray
*********************

.. autoclass:: abaqus.Material.TestData.UniaxialTestDataArray.UniaxialTestDataArray
    :members:
    :special-members: __init__

    .. autoclasstoc::

VolumetricTestData
******************

.. autoclass:: abaqus.Material.TestData.VolumetricTestData.VolumetricTestData
    :members:
    :special-members: __init__

    .. autoclasstoc::

MultiScale
~~~~~~~~~~

.. autoclass:: abaqus.Material.Multiscale.MeanFieldHomogenization.MeanFieldHomogenization
    :members:
    :special-members: __init__

    .. autoclasstoc::

.. autoclass:: abaqus.Material.Multiscale.MeanFieldInclusion.MeanFieldInclusion
    :members:
    :special-members: __init__

    .. autoclasstoc::

.. autoclass:: abaqus.Material.Multiscale.MeanFieldMatrix.MeanFieldMatrix
    :members:
    :special-members: __init__

    .. autoclasstoc::

.. autoclass:: abaqus.Material.Multiscale.MeanFieldVoid.MeanFieldVoid
    :members:
    :special-members: __init__

    .. autoclasstoc::
