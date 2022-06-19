from abaqusConstants import *


class Hypoelastic:
    """The Hypoelastic object specifies hypoelastic material properties.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].hypoelastic
        import odbMaterial
        session.odbs[name].materials[name].hypoelastic

    The table data for this object are:

    - Instantaneous Young's modulus, E.
    - Instantaneous Poisson's ratio, ν.
    - First strain invariant, I1.
    - Second strain invariant, I2.
    - Third strain invariant, I3.

    The corresponding analysis keywords are:

    - HYPOELASTIC

    """

    def __init__(self, table: tuple, user: Boolean = OFF):
        """This method creates a Hypoelastic object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].materials[name].Hypoelastic
            session.odbs[name].materials[name].Hypoelastic

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        user
            A Boolean specifying that hypoelasticity is defined by user subroutine UHYPEL. The
            default value is OFF.

        Returns
        -------
            A Hypoelastic object.
        """
        pass

    def setValues(self):
        """This method modifies the Hypoelastic object."""
        pass
