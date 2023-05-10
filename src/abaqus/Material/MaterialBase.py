from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import FREQUENCY, RAMBERG_OSGOOD
from .Acoustic.AcousticMedium import AcousticMedium
from .Density.Density import Density
from .Elastic.HyperElastic.Hyperelastic import Hyperelastic
from .Elastic.HyperElastic.HyperFoam.Hyperfoam import Hyperfoam
from .Elastic.HyperElastic.ViscoElastic.Viscoelastic import Viscoelastic
from .Elastic.HypoElastic.Hypoelastic import Hypoelastic
from .Elastic.Linear.Elastic import Elastic
from .Elastic.LowDensityFoam.LowDensityFoam import LowDensityFoam
from .Elastic.Porous.PorousElastic import PorousElastic
from .Electromagnetic.Dielectric import Dielectric
from .Electromagnetic.ElectricalConductivity import ElectricalConductivity
from .Electromagnetic.MagneticPermeability import MagneticPermeability
from .Electromagnetic.Piezoelectric import Piezoelectric
from .Eos.Eos import Eos
from .Gap.GapFlow import GapFlow
from .Gasket.GasketMembraneElastic import GasketMembraneElastic
from .Gasket.GasketThicknessBehavior import GasketThicknessBehavior
from .Gasket.GasketTransverseShearElastic import GasketTransverseShearElastic
from .HeatTransfer.Conductivity import Conductivity
from .HeatTransfer.HeatGeneration import HeatGeneration
from .HeatTransfer.InelasticHeatFraction import InelasticHeatFraction
from .HeatTransfer.JouleHeatFraction import JouleHeatFraction
from .HeatTransfer.LatentHeat import LatentHeat
from .HeatTransfer.SpecificHeat import SpecificHeat
from .MassDiffusion.Diffusivity import Diffusivity
from .MassDiffusion.Solubility import Solubility
from .Mechanical.Damping import Damping
from .Mechanical.Expansion import Expansion
from .Mechanical.PoreFluidExpansion import PoreFluidExpansion
from .Mechanical.Viscosity.Viscosity import Viscosity
from .Multiscale.MeanFieldHomogenization import MeanFieldHomogenization
from .Plastic.Concrete.BrittleCracking import BrittleCracking
from .Plastic.Concrete.Concrete import Concrete
from .Plastic.Concrete.ConcreteDamagedPlasticity import ConcreteDamagedPlasticity
from .Plastic.Creep.Creep import Creep
from .Plastic.CriticalStateClay.ClayPlasticity import ClayPlasticity
from .Plastic.CrushableFoam.CrushableFoam import CrushableFoam
from .Plastic.CrushStress.CrushStress import CrushStress
from .Plastic.DruckerPrager.Extended.DruckerPrager import DruckerPrager
from .Plastic.DruckerPrager.ModifiedCap.CapPlasticity import CapPlasticity
from .Plastic.Metal.CastIron.CastIronPlasticity import CastIronPlasticity
from .Plastic.Metal.Deformation.DeformationPlasticity import DeformationPlasticity
from .Plastic.Metal.Porous.PorousMetalPlasticity import PorousMetalPlasticity
from .Plastic.Metal.TwoLayerViscoPlasticity.Viscous import Viscous
from .Plastic.MohrCoulomb.MohrCoulombPlasticity import MohrCoulombPlasticity
from .Plastic.Plastic import Plastic
from .Plastic.PlasticityCorrection import PlasticityCorrection
from .Plastic.Swelling.Swelling import Swelling
from .PoreFluidFlow.FluidLeakoff import FluidLeakoff
from .PoreFluidFlow.Gel import Gel
from .PoreFluidFlow.MoistureSwelling.MoistureSwelling import MoistureSwelling
from .PoreFluidFlow.Permeability.Permeability import Permeability
from .PoreFluidFlow.PorousBulkModuli import PorousBulkModuli
from .PoreFluidFlow.Sorption import Sorption
from .ProgressiveDamageFailure.DamageInitiation import DamageInitiation
from .Regularization import Regularization
from .TestData.MullinsEffect import MullinsEffect
from .User.Depvar import Depvar
from .User.UserDefinedField import UserDefinedField
from .User.UserMaterial import UserMaterial
from .User.UserOutputVariables import UserOutputVariables


@abaqus_class_doc
class MaterialBase:
    """A Material object is the object used to specify a material. The Material object stores the various
    settings that determine how a material behaves. A material is created by combining one or more individual
    material options and sub options. A particular material option is associated with the Material object
    through a member. For example: the **acousticMedium** member may contain an AcousticMedium object. The
    alternative of having a MaterialOption abstract base class and a container of MaterialOptions was rejected
    because it would make it more difficult to enforce the fact that one Material object cannot contain two
    AcousticMedium objects, for example.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name]
            import odbMaterial
            session.odbs[name].materials[name]

        The corresponding analysis keywords are:

        - MATERIAL
    """

    #: An AcousticMedium object.
    acousticMedium: AcousticMedium = AcousticMedium()

    #: A BrittleCracking object.
    brittleCracking: BrittleCracking = BrittleCracking(((),))

    #: A CapPlasticity object.
    capPlasticity: CapPlasticity = CapPlasticity(((),))

    #: A CastIronPlasticity object.
    castIronPlasticity: CastIronPlasticity = CastIronPlasticity(((),))

    #: A ClayPlasticity object.
    clayPlasticity: ClayPlasticity = ClayPlasticity(((),))

    #: A Concrete object.
    concrete: Concrete = Concrete(((),))

    #: A ConcreteDamagedPlasticity object.
    concreteDamagedPlasticity: ConcreteDamagedPlasticity = ConcreteDamagedPlasticity(((),))

    #: A Conductivity object.
    conductivity: Conductivity = Conductivity(((),))

    #: A Creep object.
    creep: Creep = Creep(((),))

    #: A CrushableFoam object.
    crushableFoam: CrushableFoam = CrushableFoam(((),))

    #: A CrushStress object
    #:
    #: .. versionadded:: 2022
    #:     The ``crushStress`` attribute was added.
    crushStress: CrushStress = CrushStress(((),))

    #: A DamageInitiation object.
    ductileDamageInitiation: DamageInitiation = DamageInitiation()

    #: A DamageInitiation object.
    fldDamageInitiation: DamageInitiation = DamageInitiation()

    #: A DamageInitiation object.
    flsdDamageInitiation: DamageInitiation = DamageInitiation()

    #: A DamageInitiation object.
    johnsonCookDamageInitiation: DamageInitiation = DamageInitiation()

    #: A DamageInitiation object.
    maxeDamageInitiation: DamageInitiation = DamageInitiation()

    #: A DamageInitiation object.
    maxsDamageInitiation: DamageInitiation = DamageInitiation()

    #: A DamageInitiation object.
    maxpeDamageInitiation: DamageInitiation = DamageInitiation()

    #: A DamageInitiation object.
    maxpsDamageInitiation: DamageInitiation = DamageInitiation()

    #: A DamageInitiation object.
    mkDamageInitiation: DamageInitiation = DamageInitiation()

    #: A DamageInitiation object.
    msfldDamageInitiation: DamageInitiation = DamageInitiation()

    #: A DamageInitiation object.
    quadeDamageInitiation: DamageInitiation = DamageInitiation()

    #: A DamageInitiation object.
    quadsDamageInitiation: DamageInitiation = DamageInitiation()

    #: A DamageInitiation object.
    shearDamageInitiation: DamageInitiation = DamageInitiation()

    #: A DamageInitiation object.
    hashinDamageInitiation: DamageInitiation = DamageInitiation()

    #: A Damping object.
    damping: Damping = Damping()

    #: A DeformationPlasticity object.
    deformationPlasticity: DeformationPlasticity = DeformationPlasticity(((),))

    #: A Density object.
    density: Density = Density(((),))

    #: A Depvar object.
    depvar: Depvar = Depvar()

    #: A Dielectric object.
    dielectric: Dielectric = Dielectric(((),))

    #: A Diffusivity object.
    diffusivity: Diffusivity = Diffusivity(((),))

    #: A DruckerPrager object.
    druckerPrager: DruckerPrager = DruckerPrager(((),))

    #: An Elastic object.
    elastic: Elastic = Elastic(((),))

    #: An ElectricalConductivity object.
    electricalConductivity: ElectricalConductivity = ElectricalConductivity(((),))

    #: An Eos object.
    eos: Eos = Eos()

    #: An Expansion object.
    expansion: Expansion = Expansion()

    #: A FluidLeakoff object.
    fluidLeakoff: FluidLeakoff = FluidLeakoff()

    #: A GapFlow object.
    gapFlow: GapFlow = GapFlow(((),))

    #: A GasketThicknessBehavior object.
    gasketThicknessBehavior: GasketThicknessBehavior = GasketThicknessBehavior(((),))

    #: A GasketTransverseShearElastic object.
    gasketTransverseShearElastic: GasketTransverseShearElastic = GasketTransverseShearElastic(((),))

    #: A GasketMembraneElastic object.
    gasketMembraneElastic: GasketMembraneElastic = GasketMembraneElastic(((),))

    #: A Gel object.
    gel: Gel = Gel(((),))

    #: A HeatGeneration object.
    heatGeneration: HeatGeneration = HeatGeneration()

    #: A Hyperelastic object.
    hyperelastic: Hyperelastic = Hyperelastic(((),))

    #: A Hyperfoam object.
    hyperfoam: Hyperfoam = Hyperfoam()

    #: A Hypoelastic object.
    hypoelastic: Hypoelastic = Hypoelastic(((),))

    #: An InelasticHeatFraction object.
    inelasticHeatFraction: InelasticHeatFraction = InelasticHeatFraction()

    #: A JouleHeatFraction object.
    jouleHeatFraction: JouleHeatFraction = JouleHeatFraction()

    #: A LatentHeat object.
    latentHeat: LatentHeat = LatentHeat(((),))

    #: A LowDensityFoam object.
    lowDensityFoam: LowDensityFoam = LowDensityFoam()

    #: A MagneticPermeability object.
    magneticPermeability: MagneticPermeability = MagneticPermeability(((),), ((),), ((),))

    #: A MohrCoulombPlasticity object.
    mohrCoulombPlasticity: MohrCoulombPlasticity = MohrCoulombPlasticity(((),))

    #: A MoistureSwelling object.
    moistureSwelling: MoistureSwelling = MoistureSwelling(((),))

    #: A MullinsEffect object.
    mullinsEffect: MullinsEffect = MullinsEffect()

    #: A Permeability object.
    permeability: Permeability = Permeability(0, 0, ((),))

    #: A Piezoelectric object.
    piezoelectric: Piezoelectric = Piezoelectric(((),))

    #: A Plastic object.
    plastic: Plastic = Plastic(((),))

    #: A PlasticityCorrection object.
    plasticityCorrection: PlasticityCorrection = PlasticityCorrection(RAMBERG_OSGOOD, ((),))

    #: A PoreFluidExpansion object.
    poreFluidExpansion: PoreFluidExpansion = PoreFluidExpansion(((),))

    #: A PorousBulkModuli object.
    porousBulkModuli: PorousBulkModuli = PorousBulkModuli(((),))

    #: A PorousElastic object.
    porousElastic: PorousElastic = PorousElastic(((),))

    #: A PorousMetalPlasticity object.
    porousMetalPlasticity: PorousMetalPlasticity = PorousMetalPlasticity(((),))

    #: A Regularization object.
    regularization: Regularization = Regularization()

    #: A Solubility object.
    solubility: Solubility = Solubility(((),))

    #: A Sorption object.
    sorption: Sorption = Sorption(((),))

    #: A SpecificHeat object.
    specificHeat: SpecificHeat = SpecificHeat(((),))

    #: A Swelling object.
    swelling: Swelling = Swelling(((),))

    #: A UserDefinedField object.
    userDefinedField: UserDefinedField = UserDefinedField()

    #: A UserMaterial object.
    userMaterial: UserMaterial = UserMaterial()

    #: A UserOutputVariables object.
    userOutputVariables: UserOutputVariables = UserOutputVariables()

    #: A Viscoelastic object.
    viscoelastic: Viscoelastic = Viscoelastic(FREQUENCY, ((),))

    #: A Viscosity object.
    viscosity: Viscosity = Viscosity(((),))

    #: A Viscous object.
    viscous: Viscous = Viscous(((),))

    #: A MeanFieldHomogenization object.
    #:
    #: .. versionadded:: 2018
    #:     The ``meanFieldHomogenization`` attribute was added.
    meanFieldHomogenization: MeanFieldHomogenization = MeanFieldHomogenization()

    @abaqus_method_doc
    def __init__(self, name: str, description: str = "", materialIdentifier: str = ""):
        """This method creates a Material object.

        .. note::
            This function can be accessed by::

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
        Material
            A Material object.
        """
        self.name, self.description, self.materialIdentifier = (
            name,
            description,
            materialIdentifier,
        )

    @abaqus_method_doc
    def materialsFromOdb(self, fileName: str):
        """This methods creates Material objects by reading an output database. The new materials are placed in
        the materials repository.

        .. note::
            This function can be accessed by::

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
        List[Material]
            A list of Material objects.
        """
        ...
