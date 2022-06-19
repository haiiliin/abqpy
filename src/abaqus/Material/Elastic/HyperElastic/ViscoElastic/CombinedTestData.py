class CombinedTestData:
    """The CombinedTestData object specifies simultaneously the normalized shear and bulk
    compliances or relaxation moduli as functions of time.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].viscoelastic.combinedTestData
        import odbMaterial
        session.odbs[name].materials[name].viscoelastic.combinedTestData

    The table data for this object are:

    If **time**=RELAXATION_TEST_DATA, the table data specify the following:
        - Normalized shear modulus, gR⁢(t) (0≤gR(t)≤1).
        - Normalized volumetric (bulk) modulus, kR⁢(t) (0≤kR(t)≤1).
        - Time t (t>0).
    If **time**=CREEP_TEST_DATA, the table data specify the following:
        - Normalized shear compliance, jS(t)(jS(t)≥1).
        - Normalized volumetric (bulk) compliance, jK⁢(t) (jK(t)≥1)
        - Time t (t>0)

    The corresponding analysis keywords are:

    - COMBINED TEST DATA
    """

    def __init__(self, table: tuple, volinf: float = None, shrinf: float = None):
        """This method creates a CombinedTestData object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].materials[name].viscoelastic.CombinedTestData
            session.odbs[name].materials[name].viscoelastic.CombinedTestData

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. The values of
            the table data depend on the value of the **time** member of the Viscoelastic object.
        volinf
            None or a Float specifying a normalized volume. The value of **volinf** depends on the
            value of the **time** member of the Viscoelastic object. The default value is None.
            If **time**=RELAXATION_TEST_DATA, **volinf** specifies the value of the long-term normalized
            volumetric modulus, kR(∞).
            If **time**=CREEP_TEST_DATA, **volinf** specifies the value of the long-term normalized
            volumetric compliance, jK⁢(∞).
        shrinf
            None or a Float specifying a normalized shear. The value of **shrinf** depends on the
            value of the **time** member of the Viscoelastic object. The default value is None.
            If **time**=RELAXATION_TEST_DATA, **shrinf** specifies the value of the long-term normalized
            shear modulus, gR(∞)
            If **time**=CREEP_TEST_DATA, **shrinf** specifies the value of the long-term normalized
            shear compliance, jS(∞).

        Returns
        -------
            A CombinedTestData object.
        """
        pass

    def setValues(self):
        """This method modifies the CombinedTestData object."""
        pass
