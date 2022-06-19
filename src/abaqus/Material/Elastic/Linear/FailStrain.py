from abaqusConstants import *


class FailStrain:
    """The FailStrain object defines parameters for strain-based failure measures.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].elastic.failStrain
        import odbMaterial
        session.odbs[name].materials[name].elastic.failStrain

    The table data for this object are:
        - Tensile strain limit in fiber direction, Xεt.
        - Compressive strain limit in fiber direction, Xεc.
        - Tensile strain limit in transverse direction, Yεt.
        - Compressive strain limit in transverse direction, Yεc.
        - Shear strain limit in the X–Y plane, Sε.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    The corresponding analysis keywords are:

    - FAIL STRAIN

    """

    def __init__(
        self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0
    ):
        """This method creates a FailStrain object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].materials[name].elastic.FailStrain
            session.odbs[name].materials[name].elastic.FailStrain

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
            A FailStrain object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self):
        """This method modifies the FailStrain object.

        Raises
        ------
        RangeError
        """
        pass
