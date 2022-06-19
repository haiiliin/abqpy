class ShearTestData:
    """The ShearTestData object specifies the normalized shear creep compliance or relaxation
    modulus as a function of time.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].viscoelastic.shearTestData
        import odbMaterial
        session.odbs[name].materials[name].viscoelastic.shearTestData

    The corresponding analysis keywords are:

    - SHEAR TEST DATA
    """

    def __init__(self, table: tuple, shrinf: float = None):
        """This method creates a ShearTestData object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].materials[name].viscoelastic.ShearTestData
            session.odbs[name].materials[name].viscoelastic.ShearTestData

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying values that depend on the **time** member of
            the Viscoelastic object.
            
            - If **time**=RELAXATION_TEST_DATA, the table data specify the following:
            
                - Normalized shear relaxation modulus gR⁢(t) (0≤gR⁢(t)≤1).
                - Time t. (t>0).
                
            - If **time**=CREEP_TEST_DATA, the table data specify the following:
            
                - Normalized shear compliance jS⁢(t). (jS⁢(t)≥1).
                - Time t. (t>0).
        shrinf
            None or a Float specifying a normalized shear. The value of **shrinf** depends on the
            value of the **time** member of the Viscoelastic object. The default value is None.If
            **time**=RELAXATION_TEST_DATA, **shrinf** specifies the value of the long-term, normalized
            shear modulus gR(∞).If **time**=CREEP_TEST_DATA, **shrinf** specifies the value of the
            long-term, normalized shear compliance jS(∞).

        Returns
        -------
            A ShearTestData object.
        """
        pass

    def setValues(self):
        """This method modifies the ShearTestData object."""
        pass
