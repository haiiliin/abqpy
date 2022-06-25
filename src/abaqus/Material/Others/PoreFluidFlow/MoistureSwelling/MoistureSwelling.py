from ....Ratios import Ratios


class MoistureSwelling:
    r"""The MoistureSwelling object defines moisture-driven swelling.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import material
            mdb.models[name].materials[name].moistureSwelling
            import odbMaterial
            session.odbs[name].materials[name].moistureSwelling

        The table data for this object are:

        - Volumetric moisture swelling strain, :math:`\varepsilon^{m s}`.
        - Saturation, :math:`s`. This value must lie in the range :math:`0.0 \leq s \leq 1.0`.

        The corresponding analysis keywords are:

        - MOISTURE SWELLING
    """

    #: A :py:class:`~abaqus.Material.Ratios.Ratios` object.
    ratios: Ratios = Ratios(((),))

    def __init__(self, table: tuple):
        """This method creates a MoistureSwelling object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].materials[name].MoistureSwelling
                session.odbs[name].materials[name].MoistureSwelling

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.

        Returns
        -------
        MoistureSwelling
            A :py:class:`~abaqus.Material.Others.PoreFluidFlow.MoistureSwelling.MoistureSwelling.MoistureSwelling` object.
        """
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the MoistureSwelling object."""
        pass
