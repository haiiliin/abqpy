class SaturationDependence:
    """The SaturationDependence object specifies the dependence of the permeability of a
    material on the saturation of the wetting liquid.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].permeability.saturationDependence
        import odbMaterial
        session.odbs[name].materials[name].permeability.saturationDependence

    The table data for this object are:

    - ks. (Dimensionless.)
    - Saturation, s. (Dimensionless.)

    The corresponding analysis keywords are:

    - PERMEABILITY
    """

    def __init__(self, table: tuple):
        """This method creates a SaturationDependence object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].materials[name].permeability.SaturationDependence
            session.odbs[name].materials[name].permeability.SaturationDependence

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.

        Returns
        -------
            A SaturationDependence object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self):
        """This method modifies the SaturationDependence object.

        Raises
        ------
        RangeError
        """
        pass
