class InelasticHeatFraction:
    """The InelasticHeatFraction object defines the fraction of the rate of inelastic
    dissipation that appears as a heat source.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import material
            mdb.models[name].materials[name].inelasticHeatFraction
            import odbMaterial
            session.odbs[name].materials[name].inelasticHeatFraction

        The corresponding analysis keywords are:

        - INELASTIC HEAT FRACTION
    """

    def __init__(self, fraction: float = 0):
        """This method creates an InelasticHeatFraction object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].materials[name].InelasticHeatFraction
                session.odbs[name].materials[name].InelasticHeatFraction

        Parameters
        ----------
        fraction
            A Float specifying the fraction of inelastic dissipation rate that appears as a heat
            flux per unit volume. The fraction may include a unit conversion factor if required.
            Possible values are 0.0 ≤ **fraction** ≤ 1.0. The default value is 0.9.

        Returns
        -------
        InelasticHeatFraction
            An :py:class:`~abaqus.Material.Others.HeatTransfer.InelasticHeatFraction.InelasticHeatFraction` object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the InelasticHeatFraction object.

        Raises
        ------
        RangeError
        """
        pass
