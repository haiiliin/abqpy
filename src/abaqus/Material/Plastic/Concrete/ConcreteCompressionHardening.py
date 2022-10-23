from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ....UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class ConcreteCompressionHardening:
    r"""The ConcreteCompressionHardening object specifies hardening for the concrete damaged
    plasticity model.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].concreteDamagedPlasticity.concreteCompressionHardening
            import odbMaterial
            session.odbs[name].materials[name].concreteDamagedPlasticity.concreteCompressionHardening

        The table data for this object are:

        - Yield stress in compression, :math:`\sigma_{c}`.
        - Inelastic (crushing) strain, :math:`\epsilon_{c}^{i n}`.
        - Inelastic (crushing) strain rate, :math:`\dot{\epsilon}_{c}^{i n}`.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - CONCRETE COMPRESSION HARDENING
    """

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        rate: Boolean = OFF,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a ConcreteCompressionHardening object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].concreteDamagedPlasticity.ConcreteCompressionHardening
                session.odbs[name].materials[name].concreteDamagedPlasticity.ConcreteCompressionHardening

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        rate
            A Boolean specifying whether the data depend on rate. The default value is OFF.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        ConcreteCompressionHardening
            A :py:class:`~abaqus.Material.Plastic.Concrete.ConcreteCompressionHardening.ConcreteCompressionHardening` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the ConcreteCompressionHardening object.

        Raises
        ------
        RangeError
        """
        ...
