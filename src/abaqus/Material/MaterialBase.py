from abaqusConstants import *
from .Density.Density import Density
from .Elastic.HyperElastic.HyperFoam.Hyperfoam import Hyperfoam
from .Elastic.HyperElastic.Hyperelastic import Hyperelastic
from .Elastic.HyperElastic.ViscoElastic.Viscoelastic import Viscoelastic
from .Elastic.HypoElastic.Hypoelastic import Hypoelastic
from .Elastic.Linear.Elastic import Elastic
from .Elastic.LowDensityFoam.LowDensityFoam import LowDensityFoam
from .Elastic.Porous.PorousElastic import PorousElastic
from .Eos.Eos import Eos
from .Gap.GapFlow import GapFlow
from .Gasket.GasketMembraneElastic import GasketMembraneElastic
from .Gasket.GasketThicknessBehavior import GasketThicknessBehavior
from .Gasket.GasketTransverseShearElastic import GasketTransverseShearElastic
from .Others.Acoustic.AcousticMedium import AcousticMedium
from .Others.Electromagnetic.Dielectric import Dielectric
from .Others.Electromagnetic.ElectricalConductivity import ElectricalConductivity
from .Others.Electromagnetic.MagneticPermeability import MagneticPermeability
from .Others.Electromagnetic.Piezoelectric import Piezoelectric
from .Others.HeatTransfer.Conductivity import Conductivity
from .Others.HeatTransfer.HeatGeneration import HeatGeneration
from .Others.HeatTransfer.InelasticHeatFraction import InelasticHeatFraction
from .Others.HeatTransfer.JouleHeatFraction import JouleHeatFraction
from .Others.HeatTransfer.LatentHeat import LatentHeat
from .Others.HeatTransfer.SpecificHeat import SpecificHeat
from .Others.MassDiffusion.Diffusivity import Diffusivity
from .Others.MassDiffusion.Solubility import Solubility
from .Others.Mechanical.Damping import Damping
from .Others.Mechanical.Expansion import Expansion
from .Others.Mechanical.PoreFluidExpansion import PoreFluidExpansion
from .Others.Mechanical.Viscosity.Viscosity import Viscosity
from .Others.PoreFluidFlow.FluidLeakoff import FluidLeakoff
from .Others.PoreFluidFlow.Gel import Gel
from .Others.PoreFluidFlow.MoistureSwelling.MoistureSwelling import MoistureSwelling
from .Others.PoreFluidFlow.Permeability.Permeability import Permeability
from .Others.PoreFluidFlow.PorousBulkModuli import PorousBulkModuli
from .Others.PoreFluidFlow.Sorption import Sorption
from .Others.User.Depvar import Depvar
from .Others.User.UserDefinedField import UserDefinedField
from .Others.User.UserMaterial import UserMaterial
from .Others.User.UserOutputVariables import UserOutputVariables
from .Plastic.Concrete.BrittleCracking import BrittleCracking
from .Plastic.Concrete.Concrete import Concrete
from .Plastic.Concrete.ConcreteDamagedPlasticity import ConcreteDamagedPlasticity
from .Plastic.Creep.Creep import Creep
from .Plastic.CriticalStateClay.ClayPlasticity import ClayPlasticity
from .Plastic.CrushableFoam.CrushableFoam import CrushableFoam
from .Plastic.DruckerPrager.Extended.DruckerPrager import DruckerPrager
from .Plastic.DruckerPrager.ModifiedCap.CapPlasticity import CapPlasticity
from .Plastic.Metal.CastIron.CastIronPlasticity import CastIronPlasticity
from .Plastic.Metal.Deformation.DeformationPlasticity import DeformationPlasticity
from .Plastic.Metal.Porous.PorousMetalPlasticity import PorousMetalPlasticity
from .Plastic.Metal.TwoLayerViscoPlasticity.Viscous import Viscous
from .Plastic.MohrCoulomb.MohrCoulombPlasticity import MohrCoulombPlasticity
from .Plastic.Plastic import Plastic
from .Plastic.Swelling.Swelling import Swelling
from .ProgressiveDamageFailure.DamageInitiation import DamageInitiation
from .Regularization import Regularization
from .TestData.MullinsEffect import MullinsEffect


class MaterialBase:
    """A Material object is the object used to specify a material. The Material object stores
    the various settings that determine how a material behaves.
    A material is created by combining one or more individual material options and sub
    options. A particular material option is associated with the Material object through a
    member. For example: the **acousticMedium** member may contain an AcousticMedium object.
    The alternative of having a MaterialOption abstract base class and a container of
    MaterialOptions was rejected because it would make it more difficult to enforce the fact
    that one Material object cannot contain two AcousticMedium objects, for example.

    Attributes
    ----------
    acousticMedium: AcousticMedium
        An :py:class:`~abaqus.Material.Others.Acoustic.AcousticMedium.AcousticMedium` object.
    brittleCracking: BrittleCracking
        A :py:class:`~abaqus.Material.Plastic.Concrete.BrittleCracking.BrittleCracking` object.
    capPlasticity: CapPlasticity
        A :py:class:`~abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapPlasticity.CapPlasticity` object.
    castIronPlasticity: CastIronPlasticity
        A :py:class:`~abaqus.Material.Plastic.Metal.CastIron.CastIronPlasticity.CastIronPlasticity` object.
    clayPlasticity: ClayPlasticity
        A :py:class:`~abaqus.Material.Plastic.CriticalStateClay.ClayPlasticity.ClayPlasticity` object.
    concrete: Concrete
        A :py:class:`~abaqus.Material.Plastic.Concrete.Concrete.Concrete` object.
    concreteDamagedPlasticity: ConcreteDamagedPlasticity
        A :py:class:`~abaqus.Material.Plastic.Concrete.ConcreteDamagedPlasticity.ConcreteDamagedPlasticity` object.
    conductivity: Conductivity
        A :py:class:`~abaqus.Material.Others.HeatTransfer.Conductivity.Conductivity` object.
    creep: Creep
        A :py:class:`~abaqus.Material.Plastic.Creep.Creep.Creep` object.
    crushableFoam: CrushableFoam
        A :py:class:`~abaqus.Material.Plastic.CrushableFoam.CrushableFoam.CrushableFoam` object.
    ductileDamageInitiation: DamageInitiation
        A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    fldDamageInitiation: DamageInitiation
        A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    flsdDamageInitiation: DamageInitiation
        A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    johnsonCookDamageInitiation: DamageInitiation
        A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    maxeDamageInitiation: DamageInitiation
        A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    maxsDamageInitiation: DamageInitiation
        A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    maxpeDamageInitiation: DamageInitiation
        A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    maxpsDamageInitiation: DamageInitiation
        A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    mkDamageInitiation: DamageInitiation
        A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    msfldDamageInitiation: DamageInitiation
        A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    quadeDamageInitiation: DamageInitiation
        A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    quadsDamageInitiation: DamageInitiation
        A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    shearDamageInitiation: DamageInitiation
        A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    hashinDamageInitiation: DamageInitiation
        A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    damping: Damping
        A :py:class:`~abaqus.Material.Others.Mechanical.Damping.Damping` object.
    deformationPlasticity: DeformationPlasticity
        A :py:class:`~abaqus.Material.Plastic.Metal.Deformation.DeformationPlasticity.DeformationPlasticity` object.
    density: Density
        A :py:class:`~abaqus.Material.Density.Density.Density` object.
    depvar: Depvar
        A :py:class:`~abaqus.Material.Others.User.Depvar.Depvar` object.
    dielectric: Dielectric
        A :py:class:`~abaqus.Material.Others.Electromagnetic.Dielectric.Dielectric` object.
    diffusivity: Diffusivity
        A :py:class:`~abaqus.Material.Others.MassDiffusion.Diffusivity.Diffusivity` object.
    druckerPrager: DruckerPrager
        A :py:class:`~abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPrager.DruckerPrager` object.
    elastic: Elastic
        An :py:class:`~abaqus.Material.Elastic.Linear.Elastic.Elastic` object.
    electricalConductivity: ElectricalConductivity
        An :py:class:`~abaqus.Material.Others.Electromagnetic.ElectricalConductivity.ElectricalConductivity` object.
    eos: Eos
        An :py:class:`~abaqus.Material.Eos.Eos.Eos` object.
    expansion: Expansion
        An :py:class:`~abaqus.Material.Others.Mechanical.Expansion.Expansion` object.
    fluidLeakoff: FluidLeakoff
        A :py:class:`~abaqus.Material.Others.PoreFluidFlow.FluidLeakoff.FluidLeakoff` object.
    gapFlow: GapFlow
        A :py:class:`~abaqus.Material.Gap.GapFlow.GapFlow` object.
    gasketThicknessBehavior: GasketThicknessBehavior
        A :py:class:`~abaqus.Material.Gasket.GasketThicknessBehavior.GasketThicknessBehavior` object.
    gasketTransverseShearElastic: GasketTransverseShearElastic
        A :py:class:`~abaqus.Material.Gasket.GasketTransverseShearElastic.GasketTransverseShearElastic` object.
    gasketMembraneElastic: GasketMembraneElastic
        A :py:class:`~abaqus.Material.Gasket.GasketMembraneElastic.GasketMembraneElastic` object.
    gel: Gel
        A :py:class:`~abaqus.Material.Others.PoreFluidFlow.Gel.Gel` object.
    heatGeneration: HeatGeneration
        A :py:class:`~abaqus.Material.Others.HeatTransfer.HeatGeneration.HeatGeneration` object.
    hyperelastic: Hyperelastic
        A :py:class:`~abaqus.Material.Elastic.HyperElastic.Hyperelastic.Hyperelastic` object.
    hyperfoam: Hyperfoam
        A :py:class:`~abaqus.Material.Elastic.HyperElastic.HyperFoam.Hyperfoam.Hyperfoam` object.
    hypoelastic: Hypoelastic
        A :py:class:`~abaqus.Material.Elastic.HypoElastic.Hypoelastic.Hypoelastic` object.
    inelasticHeatFraction: InelasticHeatFraction
        An :py:class:`~abaqus.Material.Others.HeatTransfer.InelasticHeatFraction.InelasticHeatFraction` object.
    jouleHeatFraction: JouleHeatFraction
        A :py:class:`~abaqus.Material.Others.HeatTransfer.JouleHeatFraction.JouleHeatFraction` object.
    latentHeat: LatentHeat
        A :py:class:`~abaqus.Material.Others.HeatTransfer.LatentHeat.LatentHeat` object.
    lowDensityFoam: LowDensityFoam
        A :py:class:`~abaqus.Material.Elastic.LowDensityFoam.LowDensityFoam.LowDensityFoam` object.
    magneticPermeability: MagneticPermeability
        A :py:class:`~abaqus.Material.Others.Electromagnetic.MagneticPermeability.MagneticPermeability` object.
    mohrCoulombPlasticity: MohrCoulombPlasticity
        A :py:class:`~abaqus.Material.Plastic.MohrCoulomb.MohrCoulombPlasticity.MohrCoulombPlasticity` object.
    moistureSwelling: MoistureSwelling
        A :py:class:`~abaqus.Material.Others.PoreFluidFlow.MoistureSwelling.MoistureSwelling.MoistureSwelling` object.
    mullinsEffect: MullinsEffect
        A :py:class:`~abaqus.Material.TestData.MullinsEffect.MullinsEffect` object.
    permeability: Permeability
        A :py:class:`~abaqus.Material.Others.PoreFluidFlow.Permeability.Permeability.Permeability` object.
    piezoelectric: Piezoelectric
        A :py:class:`~abaqus.Material.Others.Electromagnetic.Piezoelectric.Piezoelectric` object.
    plastic: Plastic
        A :py:class:`~abaqus.Material.Plastic.Plastic.Plastic` object.
    poreFluidExpansion: PoreFluidExpansion
        A :py:class:`~abaqus.Material.Others.Mechanical.PoreFluidExpansion.PoreFluidExpansion` object.
    porousBulkModuli: PorousBulkModuli
        A :py:class:`~abaqus.Material.Others.PoreFluidFlow.PorousBulkModuli.PorousBulkModuli` object.
    porousElastic: PorousElastic
        A :py:class:`~abaqus.Material.Elastic.Porous.PorousElastic.PorousElastic` object.
    porousMetalPlasticity: PorousMetalPlasticity
        A :py:class:`~abaqus.Material.Plastic.Metal.Porous.PorousMetalPlasticity.PorousMetalPlasticity` object.
    regularization: Regularization
        A :py:class:`~abaqus.Material.Regularization.Regularization` object.
    solubility: Solubility
        A :py:class:`~abaqus.Material.Others.MassDiffusion.Solubility.Solubility` object.
    sorption: Sorption
        A :py:class:`~abaqus.Material.Others.PoreFluidFlow.Sorption.Sorption` object.
    specificHeat: SpecificHeat
        A :py:class:`~abaqus.Material.Others.HeatTransfer.SpecificHeat.SpecificHeat` object.
    swelling: Swelling
        A :py:class:`~abaqus.Material.Plastic.Swelling.Swelling.Swelling` object.
    userDefinedField: UserDefinedField
        A :py:class:`~abaqus.Material.Others.User.UserDefinedField.UserDefinedField` object.
    userMaterial: UserMaterial
        A :py:class:`~abaqus.Material.Others.User.UserMaterial.UserMaterial` object.
    userOutputVariables: UserOutputVariables
        A :py:class:`~abaqus.Material.Others.User.UserOutputVariables.UserOutputVariables` object.
    viscoelastic: Viscoelastic
        A :py:class:`~abaqus.Material.Elastic.HyperElastic.ViscoElastic.Viscoelastic.Viscoelastic` object.
    viscosity: Viscosity
        A :py:class:`~abaqus.Material.Others.Mechanical.Viscosity.Viscosity.Viscosity` object.
    viscous: Viscous
        A :py:class:`~abaqus.Material.Plastic.Metal.TwoLayerViscoPlasticity.Viscous.Viscous` object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name]
        import odbMaterial
        session.odbs[name].materials[name]

    The corresponding analysis keywords are:

    - MATERIAL
    """

    # An AcousticMedium object.
    acousticMedium: AcousticMedium = AcousticMedium()

    # A BrittleCracking object.
    brittleCracking: BrittleCracking = BrittleCracking(((),))

    # A CapPlasticity object.
    capPlasticity: CapPlasticity = CapPlasticity(((),))

    # A CastIronPlasticity object.
    castIronPlasticity: CastIronPlasticity = CastIronPlasticity(((),))

    # A ClayPlasticity object.
    clayPlasticity: ClayPlasticity = ClayPlasticity(((),))

    # A Concrete object.
    concrete: Concrete = Concrete(((),))

    # A ConcreteDamagedPlasticity object.
    concreteDamagedPlasticity: ConcreteDamagedPlasticity = ConcreteDamagedPlasticity(
        ((),)
    )

    # A Conductivity object.
    conductivity: Conductivity = Conductivity(((),))

    # A Creep object.
    creep: Creep = Creep(((),))

    # A CrushableFoam object.
    crushableFoam: CrushableFoam = CrushableFoam(((),))

    # A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    ductileDamageInitiation: DamageInitiation = DamageInitiation()

    # A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    fldDamageInitiation: DamageInitiation = DamageInitiation()

    # A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    flsdDamageInitiation: DamageInitiation = DamageInitiation()

    # A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    johnsonCookDamageInitiation: DamageInitiation = DamageInitiation()

    # A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    maxeDamageInitiation: DamageInitiation = DamageInitiation()

    # A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    maxsDamageInitiation: DamageInitiation = DamageInitiation()

    # A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    maxpeDamageInitiation: DamageInitiation = DamageInitiation()

    # A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    maxpsDamageInitiation: DamageInitiation = DamageInitiation()

    # A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    mkDamageInitiation: DamageInitiation = DamageInitiation()

    # A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    msfldDamageInitiation: DamageInitiation = DamageInitiation()

    # A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    quadeDamageInitiation: DamageInitiation = DamageInitiation()

    # A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    quadsDamageInitiation: DamageInitiation = DamageInitiation()

    # A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    shearDamageInitiation: DamageInitiation = DamageInitiation()

    # A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
    hashinDamageInitiation: DamageInitiation = DamageInitiation()

    # A Damping object.
    damping: Damping = Damping()

    # A DeformationPlasticity object.
    deformationPlasticity: DeformationPlasticity = DeformationPlasticity(((),))

    # A Density object.
    density: Density = Density(((),))

    # A Depvar object.
    depvar: Depvar = Depvar()

    # A Dielectric object.
    dielectric: Dielectric = Dielectric(((),))

    # A Diffusivity object.
    diffusivity: Diffusivity = Diffusivity(((),))

    # A DruckerPrager object.
    druckerPrager: DruckerPrager = DruckerPrager(((),))

    # An Elastic object.
    elastic: Elastic = Elastic(((),))

    # An ElectricalConductivity object.
    electricalConductivity: ElectricalConductivity = ElectricalConductivity(((),))

    # An Eos object.
    eos: Eos = Eos()

    # An Expansion object.
    expansion: Expansion = Expansion()

    # A FluidLeakoff object.
    fluidLeakoff: FluidLeakoff = FluidLeakoff()

    # A GapFlow object.
    gapFlow: GapFlow = GapFlow(((),))

    # A GasketThicknessBehavior object.
    gasketThicknessBehavior: GasketThicknessBehavior = GasketThicknessBehavior(((),))

    # A GasketTransverseShearElastic object.
    gasketTransverseShearElastic: GasketTransverseShearElastic = (
        GasketTransverseShearElastic(((),))
    )

    # A GasketMembraneElastic object.
    gasketMembraneElastic: GasketMembraneElastic = GasketMembraneElastic(((),))

    # A Gel object.
    gel: Gel = Gel(((),))

    # A HeatGeneration object.
    heatGeneration: HeatGeneration = HeatGeneration()

    # A Hyperelastic object.
    hyperelastic: Hyperelastic = Hyperelastic(((),))

    # A Hyperfoam object.
    hyperfoam: Hyperfoam = Hyperfoam()

    # A Hypoelastic object.
    hypoelastic: Hypoelastic = Hypoelastic(((),))

    # An InelasticHeatFraction object.
    inelasticHeatFraction: InelasticHeatFraction = InelasticHeatFraction()

    # A JouleHeatFraction object.
    jouleHeatFraction: JouleHeatFraction = JouleHeatFraction()

    # A LatentHeat object.
    latentHeat: LatentHeat = LatentHeat(((),))

    # A LowDensityFoam object.
    lowDensityFoam: LowDensityFoam = LowDensityFoam()

    # A MagneticPermeability object.
    magneticPermeability: MagneticPermeability = MagneticPermeability(
        ((),), ((),), ((),)
    )

    # A MohrCoulombPlasticity object.
    mohrCoulombPlasticity: MohrCoulombPlasticity = MohrCoulombPlasticity(((),))

    # A MoistureSwelling object.
    moistureSwelling: MoistureSwelling = MoistureSwelling(((),))

    # A MullinsEffect object.
    mullinsEffect: MullinsEffect = MullinsEffect()

    # A Permeability object.
    permeability: Permeability = Permeability(0, 0, ((),))

    # A Piezoelectric object.
    piezoelectric: Piezoelectric = Piezoelectric(((),))

    # A Plastic object.
    plastic: Plastic = Plastic(((),))

    # A PoreFluidExpansion object.
    poreFluidExpansion: PoreFluidExpansion = PoreFluidExpansion(((),))

    # A PorousBulkModuli object.
    porousBulkModuli: PorousBulkModuli = PorousBulkModuli(((),))

    # A PorousElastic object.
    porousElastic: PorousElastic = PorousElastic(((),))

    # A PorousMetalPlasticity object.
    porousMetalPlasticity: PorousMetalPlasticity = PorousMetalPlasticity(((),))

    # A Regularization object.
    regularization: Regularization = Regularization()

    # A Solubility object.
    solubility: Solubility = Solubility(((),))

    # A Sorption object.
    sorption: Sorption = Sorption(((),))

    # A SpecificHeat object.
    specificHeat: SpecificHeat = SpecificHeat(((),))

    # A Swelling object.
    swelling: Swelling = Swelling(((),))

    # A UserDefinedField object.
    userDefinedField: UserDefinedField = UserDefinedField()

    # A UserMaterial object.
    userMaterial: UserMaterial = UserMaterial()

    # A UserOutputVariables object.
    userOutputVariables: UserOutputVariables = UserOutputVariables()

    # A Viscoelastic object.
    viscoelastic: Viscoelastic = Viscoelastic(FREQUENCY, ((),))

    # A Viscosity object.
    viscosity: Viscosity = Viscosity(((),))

    # A Viscous object.
    viscous: Viscous = Viscous(((),))

    def __init__(self, name: str, description: str = "", materialIdentifier: str = ""):
        """This method creates a Material object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Material
            session.odbs[name].Material

        Parameters
        ----------
        name
            A String specifying the name of the new material.
        description
            A String specifying user description of the material. The default value is an empty
            string.
        materialIdentifier
            A String specifying material identifier for customer use. The default value is an empty
            string.

        Returns
        -------
            A Material object.
        """
        self.name, self.description, self.materialIdentifier = (
            name,
            description,
            materialIdentifier,
        )

    def materialsFromOdb(self, fileName: str):
        """This methods creates Material objects by reading an output database. The new materials
        are placed in the materials repository.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Material
            session.odbs[name].Material

        Parameters
        ----------
        fileName
            A String specifying the name of the output database file (including the .odb extension)
            to be read. This String can also be the full path to the output database file if it is
            located in another directory.

        Returns
        -------
            A list of Material objects.
        """
        pass
