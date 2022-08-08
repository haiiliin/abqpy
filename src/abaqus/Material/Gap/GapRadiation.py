class GapRadiation:
    """The GapRadiation object specifies radiative heat transfer between closely adjacent
    surfaces.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].gapRadiation
        import odbMaterial
        session.odbs[name].materials[name].gapRadiation

    The table data for this object are:

    - Effective view factor.
    - Gap clearance.
    - Repeat this data line as often as necessary to define the dependence of the view factor on gap clearance.

    The corresponding analysis keywords are:

    - GAP RADIATION

    """

    def __init__(
        self,
        mainSurfaceEmissivity: float,
        secondarySurfaceEmissivity: float,
        table: tuple,
    ):
        r"""This method creates a GapRadiation object.

        .. note::
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].materials[name].Gapradiation
                session.odbs[name].materials[name].Gapradiation

        Parameters
        ----------
        mainSurfaceEmissivity
            A Float specifying the Emissivity of master surface :math:`\varepsilon_A`.
        secondarySurfaceEmissivity
            A Float specifying the Emissivity of the slave surface :math:`\varepsilon_B`.
        table
            A sequence of sequences of Floats specifying the items described below.

        Returns
        -------
            A Gapradiation object.
        """
        pass

    def setValues(self):
        """This method modifies the GapRadiation object."""
        pass
