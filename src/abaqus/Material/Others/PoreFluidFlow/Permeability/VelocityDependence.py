class VelocityDependence:
    """The VelocityDependence object specifies the dependence of the permeability of a material
    on the velocity of fluid flow.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].permeability.velocityDependence
        import odbMaterial
        session.odbs[name].materials[name].permeability.velocityDependence

    The table data for this object are:

    - β. Only β> 0.0 is allowed.
    - Void ratio, ee.

    The corresponding analysis keywords are:

    - PERMEABILITY

    """

    def __init__(self, table: tuple):
        """This method creates a VelocityDependence object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].materials[name].permeability.VelocityDependence
            session.odbs[name].materials[name].permeability.VelocityDependence

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.

        Returns
        -------
            A VelocityDependence object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self):
        """This method modifies the VelocityDependence object.

        Raises
        ------
        RangeError
        """
        pass
