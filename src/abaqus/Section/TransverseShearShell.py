class TransverseShearShell:
    """The TransverseShearShell object defines the transverse shear stiffness properties of a
    shell section.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import section
        mdb.models[name].sections[name].transverseShear
        import odbSection
        session.odbs[name].sections[name].transverseShear

    The corresponding analysis keywords are:

    - TRANSVERSE SHEAR STIFFNESS

    """

    def __init__(self, k11: float, k22: float, k12: float):
        """This method creates a TransverseShearShell object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].sections[name].TransverseShearShell
            session.odbs[name].sections[name].TransverseShearShell

        Parameters
        ----------
        k11
            A Float specifying the shear stiffness of the section in the first direction.
        k22
            A Float specifying the shear stiffness of the section in the second direction.
        k12
            A Float specifying the coupling term in the shear stiffness of the section.

        Returns
        -------
            A TransverseShearShell object.
        """
        pass

    def setValues(self):
        """This method modifies the TransverseShearShell object."""
        pass
