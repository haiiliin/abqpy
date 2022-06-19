class SimpleShearTestData:
    """The SimpleShearTestData object provides simple shear test data.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].hyperfoam.simpleShearTestData
        import odbMaterial
        session.odbs[name].materials[name].hyperfoam.simpleShearTestData

    The table data for this object are:

    - Nominal shear stress, TS.
    - Nominal shear strain, γ.
    - Nominal transverse stress, TT (normal to edge with shear stress). This stress value is optional.

    The corresponding analysis keywords are:

    - SIMPLE SHEAR TEST DATA
    """

    def __init__(self, table: tuple):
        """This method creates a SimpleShearTestData object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].materials[name].hyperfoam.SimpleShearTestData
            session.odbs[name].materials[name].hyperfoam.SimpleShearTestData

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.

        Returns
        -------
            A SimpleShearTestData object.
        """
        pass

    def setValues(self):
        """This method modifies the SimpleShearTestData object."""
        pass
