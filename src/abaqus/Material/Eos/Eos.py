from abaqusConstants import *


class Eos:
    """The Eos object specifies an equation of state model.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].eos
        import odbMaterial
        session.odbs[name].materials[name].eos

    The table data for this object are:

    - If **type**=IDEALGAS, the table data represents the following:
        - Gas constant, R.
        - The ambient pressure, pA. If this field is left blank, a default of 0.0 is used.
    - If **type**=JWL, the table data represents the following:
        - Detonation wave speed, Cd.
        - A.
        - B.
        - ω. (Dimensionless.)
        - R1. (Dimensionless.)
        - R2. (Dimensionless.)
        - Pre-detonation bulk modulus, Kp⁢d.
        - Detonation energy density, E0.
    - If **type**=USUP, the table data represents the following:
        - c0.
        - s. (Dimensionless.)
        - Γ0. (Dimensionless.)
    - If **type**=TABULAR, the table data represents the following:
        - F1.
        - F2.
        - εcvol. (Dimensionless.)

    """

    def __init__(
        self,
        type: SymbolicConstant = IDEALGAS,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        detonationEnergy: float = 0,
        solidTable: tuple = (),
        gasTable: tuple = (),
        reactionTable: tuple = (),
        gasSpecificTable: tuple = (),
        table: tuple = (),
    ):
        """This method creates an Eos object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].materials[name].Eos
            session.odbs[name].materials[name].Eos

        Parameters
        ----------
        type
            A SymbolicConstant specifying the equation of state. Possible values are USUP, JWL,
            IDEALGAS, TABULAR, and IGNITIONANDGROWTH. The default value is IDEALGAS.
        temperatureDependency
            A Boolean specifying whether the data in **gasSpecificTable** depend on temperature. The
            default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies for the data in
            **gasSpecificTable**. The default value is 0.
        detonationEnergy
            A Float specifying the detonation energy text field. The default value is 0.0.
        solidTable
            A sequence of sequences of Floats specifying the following:
            - $A_{s}$.
            - $B_{s}$.
            - ${\omega}_{s}$.
            - $R_{1s}$.
            - $R_{2s}$.
            The default value is an empty sequence.
        gasTable
            A sequence of sequences of Floats specifying the following:
            - $A_{g}$.
            - $B_{g}$.
            - ${\omega}_{g}$.
            - $R_{1g}$.
            - $R_{2g}$.
            The default value is an empty sequence.
        reactionTable
            A sequence of sequences of Floats specifying the following:
            - Initial Pressure, $I$.
            - Product co-volume, $a$.
            - Exponent on the unreacted fraction (ignition term), $x$.
            - First burn rate coefficient, $G_{1}$
            - Exponent on the unreacted fraction (growth term), $c$.
            - Exponent on the reacted fraction (growth term), $d$.
            - Pressure exponent (growth term), $y$.
            - Second burn rate coefficient, $G_{2}$.
            - Exponent on the unreacted fraction (completion term), $e$.
            - Exponent on the reacted fraction (completion term), $g$.
            - Pressure exponent (completion term), $z$.
            - Initial reacted fraction, ${F^{max}}_{ig}$.
            - Maximum reacted fraction for the growth term, ${F^{max}}_{G1}$.
            - Minimum reacted fraction, ${F^{min}}_{G2}$.
            The default value is an empty sequence.
        gasSpecificTable
            A sequence of sequences of Floats specifying the following:
            - Specific Heat per unit mass.
            - Temperature dependent data.
            - Value of first field variable.
            - Value of second field variable.
            - Etc.
            The default value is an empty sequence.
        table
            A sequence of sequences of Floats specifying the items described below. The default
            value is an empty sequence.

        Returns
        -------

        Raises
        ------
        """
        pass
