from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ....UtilityAndView.abaqusConstants import OFF, Boolean
from .ConcreteCompressionDamage import ConcreteCompressionDamage
from .ConcreteCompressionHardening import ConcreteCompressionHardening
from .ConcreteTensionDamage import ConcreteTensionDamage
from .ConcreteTensionStiffening import ConcreteTensionStiffening


@abaqus_class_doc
class ConcreteDamagedPlasticity:
    r"""The ConcreteDamagedPlasticity object specifies the concrete damaged plasticity model.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].concreteDamagedPlasticity
            import odbMaterial
            session.odbs[name].materials[name].concreteDamagedPlasticity

        The table data for this object are:

        - Dilation angle, :math:`\psi` (in degrees) in the :math:`p - q` plane.
        - Flow potential eccentricity, :math:`\epsilon`. The default value is 0.1.
        - :math:`\sigma_{b 0} / \sigma_{t 0}`, the ratio of initial equibiaxial compressive
          yield stress to initial uniaxial compressive yield stress. The default value
          is 1.16. stress is negative. The default value is 2/3. default value is 0.0.
        - :math:`K_c`, the ratio of the second stress invariant on the tensile meridian, to that on
          the compressive meridian, at initial yield for any given value of the pressure invariant :math:`p`
          such that the maximum principal stress is negative. The default value is 2/3.
        - Viscosity parameter, :math:`\mu`, used for the viscoplastic regularization of the concrete
          constitutive equations in an Abaqus/Standard analysis. This parameter is ignored in an
          Abaqus/Explicit analysis. The default value is 0.0.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - CONCRETE DAMAGED PLASTICITY
    """

    #: A ConcreteCompressionHardening object.
    concreteCompressionHardening: ConcreteCompressionHardening = ConcreteCompressionHardening(((),))

    #: A ConcreteTensionStiffening object.
    concreteTensionStiffening: ConcreteTensionStiffening = ConcreteTensionStiffening(((),))

    #: A ConcreteCompressionDamage object.
    concreteCompressionDamage: ConcreteCompressionDamage = ConcreteCompressionDamage(((),))

    #: A ConcreteTensionDamage object.
    concreteTensionDamage: ConcreteTensionDamage = ConcreteTensionDamage(((),))

    @abaqus_method_doc
    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a ConcreteDamagedPlasticity object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].ConcreteDamagedPlasticity
                session.odbs[name].materials[name].ConcreteDamagedPlasticity

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        ConcreteDamagedPlasticity
            A ConcreteDamagedPlasticity object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the ConcreteDamagedPlasticity object.

        Raises
        ------
        RangeError
        """
        ...
