from abaqusConstants import *
from ..Metal.ORNL.Ornl import Ornl
from ..Potential import Potential


class Creep:
    """The Creep object defines a creep law.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].creep
        import odbMaterial
        session.odbs[name].materials[name].creep

    The table data for this object are:

    - If **law**=STRAIN or **law**=TIME, the table data specify the following:
    
        - A.
        - n.
        - m.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    - If **law**=HYPERBOLIC_SINE, the table data specify the following:
    
        - A.
        - B.
        - n.
        - △⁢H, if the data depend on temperature.
        - R.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    - If **law**=ANAND, the table data specify the following:
    
        - s1.
        - QR.
        - A.
        - ξ.
        - m.
        - A0.
        - ˆS.
        - n.
        - a.
        - S2.
        - S3.
        - A1.
        - A2.
        - A3.
        - A4.
    - If **law**=DARVEAUX, the table data specify the following:
    
        - Css.
        - QR.
        - α.
        - n.
        - ϵT.
        - B.
    - If **law**=DOUBLE_POWER, the table data specify the following:
    
        - A1.
        - B1.
        - C1.
        - A2.
        - B2.
        - C2.
        - σ0.
    - If **law**=POWER_LAW or **law**=TIME_POWER_LAW, the table data specify the following:
    
        - q0.
        - n.
        - m.
        - ∙ε0•.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    The corresponding analysis keywords are:

    - CREEP
    """

    # An Ornl object.
    ornl: Ornl = Ornl()

    # A Potential object.
    potential: Potential = Potential(((),))

    def __init__(
        self,
        table: tuple,
        law: SymbolicConstant = STRAIN,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        time: SymbolicConstant = TOTAL,
    ):
        """This method creates a Creep object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].materials[name].Creep
            session.odbs[name].materials[name].Creep

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        law
            A SymbolicConstant specifying the strain-hardening law. Possible values are STRAIN,
            TIME, HYPERBOLIC_SINE, USER, ANAND, DARVEAUX,DOUBLE_POWER, POWER_LAW, and
            TIME_POWER_LAW. The default value is STRAIN.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        time
            A SymbolicConstant specifying the time interval for relevant laws. Possible values are
            CREEP and TOTAL. The default value is TOTAL.

        Returns
        -------
            A Creep object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self):
        """This method modifies the Creep object.

        Raises
        ------
        RangeError
        """
        pass
