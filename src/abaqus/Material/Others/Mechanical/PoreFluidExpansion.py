from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ....UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class PoreFluidExpansion:
    r"""The PoreFluidExpansion object specifies the thermal expansion coefficient for a
    hydraulic fluid.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].poreFluidExpansion
            import odbMaterial
            session.odbs[name].materials[name].poreFluidExpansion

        The table data for this object are:

        - Mean coefficient of thermal expansion, :math:`\theta_0`.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - EXPANSION
    """

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        zero: float = 0,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a PoreFluidExpansion object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].PoreFluidExpansion
                session.odbs[name].materials[name].PoreFluidExpansion

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        zero
            A Float specifying the value of θ0. The default value is 0.0.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        PoreFluidExpansion
            A :py:class:`~abaqus.Material.Others.Mechanical.PoreFluidExpansion.PoreFluidExpansion` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the PoreFluidExpansion object.

        Raises
        ------
        RangeError
        """
        ...
