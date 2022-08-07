class MeanFieldMatrix:
    """The MeanFieldMatrix object specifies the matrix property.

    .. note::
        This object can be accessed by:

        .. code-block:: python

            import material
            mdb.models[name].materials[name].constituents[name]
            import odbMaterial
            session.odbs[name].materials[name].constituents[name]

    The corresponding analysis keywords are:

    - CONSTITUENT

    """

    def __init__(
        self, name: str, material: str = "", isotropizationCoefficient: float = None
    ):
        """This method creates a MeanFieldMatrix object.

        .. note::
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].materials[name].meanFieldHomogenization.MeanFieldMatrix
                session.odbs[name].materials[name].meanFieldHomogenization.MeanFieldMatrix

        Parameters
        ----------
        name
            A String specifying the constituent repository key.
        material
            A String specifying the name of the material.
        isotropizationCoefficient
            A Float specifying the factor used for scaling the Plastic strain of the constituent
            when calculating the isotropic part of the tangent.

        Returns
        -------
            A MeanFieldMatrix object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self):
        """This method modifies the MeanFieldMatrix object.

        Raises
        ------
        RangeError
        """
        pass
