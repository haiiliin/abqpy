class ShearTestData:
    r"""The ShearTestData object specifies the normalized shear creep compliance or relaxation
    modulus as a function of time.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import material
            mdb.models[name].materials[name].viscoelastic.shearTestData
            import odbMaterial
            session.odbs[name].materials[name].viscoelastic.shearTestData
            
        The table data for this object are:
                
        - If **time** = RELAXATION_TEST_DATA, the table data specify the following:
        
            - Normalized shear relaxation modulus :math:`g_{R}(t)`. :math:`\left(0 \leq g_{R}(t) \leq 1\right)`
            - Time :math:`t (t>0)`.
            
        - If **time** = CREEP_TEST_DATA, the table data specify the following:
        
            - Normalized shear compliance :math:`j_{S}(t)`. :math:`\left(j_{S}(t) \geq 1\right)`.
            - Time :math:`t (t>0)`.

        The corresponding analysis keywords are:

        - SHEAR TEST DATA
    """

    def __init__(self, table: tuple, shrinf: float = None):
        r"""This method creates a ShearTestData object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].materials[name].viscoelastic.ShearTestData
                session.odbs[name].materials[name].viscoelastic.ShearTestData

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying values that depend on the **time** member of
            the Viscoelastic object.
        shrinf
            None or a Float specifying a normalized shear. The value of **shrinf** depends on the
            value of the **time** member of the Viscoelastic object. The default value is None.If
            **time** = RELAXATION_TEST_DATA, **shrinf** specifies the value of the long-term, normalized
            shear modulus :math:`g_R(\infty)`.If **time** = CREEP_TEST_DATA, **shrinf** specifies the value of the
            long-term, normalized shear compliance :math:`j_S(\infty)`.

        Returns
        -------
        ShearTestData
            A :py:class:`~abaqus.Material.TestData.ShearTestData.ShearTestData` object.
        """
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the ShearTestData object."""
        pass
