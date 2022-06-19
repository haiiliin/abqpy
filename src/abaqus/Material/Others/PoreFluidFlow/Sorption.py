from abaqusConstants import *


class Sorption:
    """The Sorption object defines absorption and exsorption behaviors of a partially saturated
    porous medium in the analysis of coupled wetting liquid flow and porous medium stress.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].sorption
        import odbMaterial
        session.odbs[name].materials[name].sorption

    The table data for this object are:

    - If **lawAbsorption**=TABULAR or **lawExsorption**=TABULAR, the **absorptionTable** and **exsorptionTable** data respectively specify the following:

        - Pore pressure, uw.
        - Saturation, s.

    - If **lawAbsorption**=LOG or **lawExsorption**=LOG, the **absorptionTable** and **exsorptionTable** data respectively specify the following:

        - A.
        - B.
        - s0.
        - s1.

    The corresponding analysis keywords are:

    - SORPTION

    """

    def __init__(
        self,
        absorptionTable: tuple,
        lawAbsorption: SymbolicConstant = TABULAR,
        exsorption: Boolean = OFF,
        lawExsorption: SymbolicConstant = TABULAR,
        scanning: float = 0,
        exsorptionTable: tuple = (),
    ):
        """This method creates a Sorption object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].materials[name].Sorption
            session.odbs[name].materials[name].Sorption

        Parameters
        ----------
        absorptionTable
            A sequence of sequences of Floats specifying the items described below.
        lawAbsorption
            A SymbolicConstant specifying absorption behavior. Possible values are LOG and TABULAR.
            The default value is TABULAR.
        exsorption
            A Boolean specifying whether the exsorption data is specified. The default value is OFF.
        lawExsorption
            A SymbolicConstant specifying exsorption behavior. Possible values are LOG and TABULAR.
            The default value is TABULAR.
        scanning
            A Float specifying the slope of the scanning line, (duw/ds)|s. This slope must be
            positive and larger than the slope of the absorption or exsorption behaviors. The
            default value is 0.0.
        exsorptionTable
            A sequence of sequences of Floats specifying the items described below. The default
            value is an empty sequence.

        Returns
        -------
            A Sorption object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self):
        """This method modifies the Sorption object.

        Raises
        ------
        RangeError
        """
        pass
