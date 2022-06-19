from abaqusConstants import *


class DeformationPlasticity:
    """The DeformationPlasticity object specifies the deformation plasticity model.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].deformationPlasticity
        import odbMaterial
        session.odbs[name].materials[name].deformationPlasticity

    The table data for this object are:

    - Young's modulus, E.
    - Poisson's ratio, ν.
    - Yield stress, σ0.
    - Exponent, n.
    - Yield offset, α.
    - Temperature, if the data depend on temperature.

    The corresponding analysis keywords are:

    - DEFORMATION PLASTICITY

    """

    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF):
        """This method creates a DeformationPlasticity object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].materials[name].DeformationPlasticity
            session.odbs[name].materials[name].DeformationPlasticity

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.

        Returns
        -------
            A DeformationPlasticity object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self):
        """This method modifies the DeformationPlasticity object.

        Raises
        ------
        RangeError
        """
        pass
