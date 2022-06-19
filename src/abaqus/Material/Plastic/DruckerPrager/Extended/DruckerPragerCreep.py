from abaqusConstants import *


class DruckerPragerCreep:
    """The DruckerPragerCreep object specifies creep for Drucker-Prager plasticity models.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].druckerPrager.druckerPragerCreep
        import odbMaterial
        session.odbs[name].materials[name].druckerPrager.druckerPragerCreep

    The table data for this object are:

    - If **law**=TIME or **law**=STRAIN, the table data specify the following:
        - AA. (Units of F-nL2nT−1−m.)
        - n.
        - m.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    - If **law**=SINGHM, the table data specify the following:
        - A. (Units of T−1.)
        - α. (Units of F−1L2.)
        - m.
        - t1. (Units of T.)
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    The corresponding analysis keywords are:

    - DRUCKER PRAGER CREEP

    """

    def __init__(
        self,
        table: tuple,
        law: SymbolicConstant = STRAIN,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a DruckerPragerCreep object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].materials[name].druckerPrager.DruckerPragerCreep
            session.odbs[name].materials[name].druckerPrager.DruckerPragerCreep

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        law
            A SymbolicConstant specifying the type of data defining the creep law. Possible values
            are:STRAIN, specifying a strain-hardening power law.TIME, specifying a time-hardening
            power law.SINGHM, specifying a Singh-Mitchell type law.USER, specifying the creep law is
            input from user subroutine CREEP.The default value is STRAIN.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
            A DruckerPragerCreep object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self):
        """This method modifies the DruckerPragerCreep object.

        Raises
        ------
        RangeError
        """
        pass
