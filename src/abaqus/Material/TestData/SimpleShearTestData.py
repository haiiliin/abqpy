class SimpleShearTestData:
    r"""The SimpleShearTestData object provides simple shear test data.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import material
            mdb.models[name].materials[name].hyperfoam.simpleShearTestData
            import odbMaterial
            session.odbs[name].materials[name].hyperfoam.simpleShearTestData

        The table data for this object are:

        - Nominal shear stress, :math:`T_{S}`.
        - Nominal shear strain, :math:`\gamma`
        - Nominal transverse stress, :math:`T_{T}` (normal to edge with shear stress). This stress value is optional.

        The corresponding analysis keywords are:

        - SIMPLE SHEAR TEST DATA
    """

    def __init__(self, table: tuple):
        """This method creates a SimpleShearTestData object.

        .. note:: 
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
        SimpleShearTestData
            A :py:class:`~abaqus.Material.TestData.SimpleShearTestData.SimpleShearTestData` object.
        """
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the SimpleShearTestData object."""
        pass
