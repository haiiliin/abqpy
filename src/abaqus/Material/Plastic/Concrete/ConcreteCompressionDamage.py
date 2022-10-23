from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ....UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class ConcreteCompressionDamage:
    r"""The ConcreteCompressionDamage object specifies hardening for the concrete damaged
    plasticity model.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].concreteDamagedPlasticity.concreteCompressionDamage
            import odbMaterial
            session.odbs[name].materials[name].concreteDamagedPlasticity.concreteCompressionDamage

        The table data for this object are:

        - Compressive damage variable, :math:`d_{c}`.
        - Inelastic (crushing) strain, :math:`\epsilon_{c}^{i n}`.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - CONCRETE COMPRESSION DAMAGE
    """

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        tensionRecovery: float = 0,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a ConcreteCompressionDamage object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].concreteDamagedPlasticity.ConcreteCompressionDamage
                session.odbs[name].materials[name].concreteDamagedPlasticity.ConcreteCompressionDamage

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        tensionRecovery
            A Float specifying the value of the stiffness recovery factor, :math:`w_{t}`, that determines the
            amount of tension stiffness that is recovered as loading changes from compression to
            tension. The default value is 0.0.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        ConcreteCompressionDamage
            A :py:class:`~abaqus.Material.Plastic.Concrete.ConcreteCompressionDamage.ConcreteCompressionDamage` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the ConcreteCompressionDamage object.

        Raises
        ------
        RangeError
        """
        ...
