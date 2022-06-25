class LatentHeat:
    """The LatentHeat object specifies a material's latent heat.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import material
            mdb.models[name].materials[name].latentHeat
            import odbMaterial
            session.odbs[name].materials[name].latentHeat

        The table data for this object are:

        - Latent heat per unit mass.
        - Solidus temperature.
        - Liquidus temperature.

        The corresponding analysis keywords are:

        - LATENT HEAT
    """

    def __init__(self, table: tuple):
        """This method creates a LatentHeat object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].materials[name].LatentHeat
                session.odbs[name].materials[name].LatentHeat

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.

        Returns
        -------
        LatentHeat
            A :py:class:`~abaqus.Material.Others.HeatTransfer.LatentHeat.LatentHeat` object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the LatentHeat object.

        Raises
        ------
        RangeError
        """
        pass
