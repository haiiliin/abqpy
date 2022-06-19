from abaqusConstants import *


class Piezoelectric:
    """The Piezoelectric object specifies piezoelectric material properties.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].piezoelectric
        import odbMaterial
        session.odbs[name].materials[name].piezoelectric

    The table data for this object are:

    - If **type**=STRESS, the table data specify the following:
        - e1 11φ.
        - e1 22φ.
        - e1 33φ.
        - e1 12φ.
        - e1 13φ.
        - e1 23φ.
        - e2 11φ.
        - e2 22φ.
        - e2 33φ.
        - e2 12φ.
        - e2 13φ.
        - e2 23φ.
        - e3 11φ.
        - e3 22φ.
        - e3 33φ.
        - e3 12φ.
        - e3 13φ.
        - e3 23φ.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    - If **type**=STRAIN, the table data specify the following:
        - d1 11φ.
        - d1 22φ.
        - d1 33φ.
        - d1 12φ.
        - d1 13φ.
        - d1 23φ.
        - d2 11φ.
        - d2 22φ.
        - d2 33φ.
        - d2 12φ.
        - d2 13φ.
        - d2 23φ.
        - d3 11φ.
        - d3 22φ.
        - d3 33φ.
        - d3 13φ.
        - d3 23φ.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    The corresponding analysis keywords are:

    - PIEZOELECTRIC

    """

    def __init__(
        self,
        table: tuple,
        type: SymbolicConstant = STRESS,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a Piezoelectric object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].materials[name].Piezoelectric
            session.odbs[name].materials[name].Piezoelectric

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        type
            A SymbolicConstant specifying the type of material coefficients for the piezoelectric
            property. Possible values are STRAIN and STRESS. The default value is STRESS.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
            A Piezoelectric object.
        """
        pass

    def setValues(self):
        """This method modifies the Piezoelectric object."""
        pass
