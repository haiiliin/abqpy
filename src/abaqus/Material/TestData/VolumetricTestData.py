from abaqusConstants import *


class VolumetricTestData:
    """The VolumetricTestData object provides volumetric test data.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].hyperelastic.volumetricTestData
        mdb.models[name].materials[name].hyperfoam.volumetricTestData
        mdb.models[name].materials[name].viscoelastic.volumetricTestData
        import odbMaterial
        session.odbs[name].materials[name].hyperelastic.volumetricTestData
        session.odbs[name].materials[name].hyperfoam.volumetricTestData
        session.odbs[name].materials[name].viscoelastic.volumetricTestData

    The table data for this object are:

    - For a hyperelastic or hyperfoam material model, the table data specify the following:
    
        - Pressure, p.
        - Volume ratio, J (current volume/original volume).
    - For a viscoelastic material model, the values depend on the value of the **time** member of the [Viscoelastic](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viscoelasticpyc.htm?ContextScope=all) object.
        - If **time**=RELAXATION_TEST_DATA, the table data specify the following:
        
            - Normalized volumetric (bulk) modulus kR(t),(0≤kR(t)≤1).
            - Time t (t>0).
        - If **time**=CREEP_TEST_DATA, the table data specify the following:
        
            - Normalized volumetric (bulk) compliance jK(t),(jK(t)≥1).
            - Time t (t>0).

    The corresponding analysis keywords are:

    - VOLUMETRIC TEST DATA
    """

    def __init__(
        self,
        table: tuple,
        volinf: float = None,
        smoothing: int = None,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a VolumetricTestData object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].materials[name].hyperelastic.VolumetricTestData
            mdb.models[name].materials[name].hyperfoam.VolumetricTestData
            mdb.models[name].materials[name].viscoelastic.VolumetricTestData
            session.odbs[name].materials[name].hyperelastic.VolumetricTestData
            session.odbs[name].materials[name].hyperfoam.VolumetricTestData
            session.odbs[name].materials[name].viscoelastic.VolumetricTestData

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        volinf
            None or a Float specifying a normalized volumetric value that depends on the value of
            the **time** member of the Viscoelastic object. The default value is None.If
            **time**=RELAXATION_TEST_DATA, **volinf** specifies the value of the long-term, normalized
            volumetric modulus, kR⁢(∞). If **time**=CREEP_TEST_DATA, **volinf** specifies the value of
            the long-term, normalized volumetric compliance, K⁢(∞).This argument is valid only for a
            viscoelastic material model.
        smoothing
            None or an Int specifying the value for smoothing. If **smoothing**=None, no smoothing is
            employed. The default value is None.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
            A VolumetricTestData object.
        """
        pass

    def setValues(self):
        """This method modifies the VolumetricTestData object."""
        pass
