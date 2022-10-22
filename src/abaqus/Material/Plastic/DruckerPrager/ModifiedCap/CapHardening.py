from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .....UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class CapHardening:
    """The CapHardening object specifies Drucker-Prager/Cap plasticity hardening.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].capPlasticity.capHardening
            import odbMaterial
            session.odbs[name].materials[name].capPlasticity.capHardening

        The table data for this object are:

        - Hydrostatic pressure yield stress.
        - Absolute value of the corresponding volumetric inelastic strain.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - CAP HARDENING
    """

    @abaqus_method_doc
    def __init__(
        self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0
    ):
        """This method creates a CapHardening object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].capPlasticity.CapHardening
                session.odbs[name].materials[name].capPlasticity.CapHardening

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
        CapHardening
            A :py:class:`~abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapHardening.CapHardening` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the CapHardening object.

        Raises
        ------
        RangeError
        """
        ...
