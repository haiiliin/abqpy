from abaqusConstants import *
from .FailStrain import FailStrain
from .FailStress import FailStress


class Elastic:
    """The Elastic object specifies elastic material properties.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].elastic
        import odbMaterial
        session.odbs[name].materials[name].elastic

    The table data for this object are:

    - If **type**=ISOTROPIC, the table data specify the following:
        - The Young's modulus, E.
        - The Poisson's ratio, v.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    - If **type**=SHEAR, the table data specify the following:
        - The shear modulus,G.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    - If **type**=ENGINEERING_CONSTANTS, the table data specify the following:
        - E1.
        - E2.
        - E3.
        - v12.
        - v13.
        - v23.
        - G12.
        - G13.
        - G23.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    - If **type**=LAMINA, the table data specify the following:
        - E1.
        - E2.
        - v12.
        - G12.
        - G13. This shear modulus is needed to define transverse shear behavior in shells.
        - G23. This shear modulus is needed to define transverse shear behavior in shells.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    - If **type**=ORTHOTROPIC, the table data specify the following:
        - D1111.
        - D1122.
        - D2222.
        - D1133.
        - D2233.
        - D3333.
        - D1212.
        - D1313.
        - D2323.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    - If **type**=ANISOTROPIC, the table data specify the following:
        - D1111.
        - D1122.
        - D2222.
        - D1133.
        - D2233.
        - D3333.
        - D1112.
        - D2212.
        - D3312.
        - D1212.
        - D1113.
        - D2213.
        - D3313.
        - D1213.
        - D1313.
        - D1123.
        - D2223.
        - D3323.
        - D1223.
        - D1323.
        - D2323.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    - If **type**=TRACTION, the table data specify the following:
        - EE for warping elements; Enn for cohesive elements.
        - G1 for warping elements; Ess for cohesive elements.
        - G2 for warping elements; Ett for cohesive elements.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    - If **type**=BILAMINA, the table data specify the following:
        - E1+.
        - E2+.
        - v12+.
        - G12.
        - E1-.
        - E2-.
        - v112-.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    - If **type**=SHORT_FIBER, there is no table data.

    The corresponding analysis keywords are:

    - ELASTIC

    """

    # A FailStress object.
    failStress: FailStress = FailStress(((),))

    # A FailStrain object.
    failStrain: FailStrain = FailStrain(((),))

    def __init__(
        self,
        table: tuple,
        type: SymbolicConstant = ISOTROPIC,
        noCompression: Boolean = OFF,
        noTension: Boolean = OFF,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        moduli: SymbolicConstant = LONG_TERM,
    ):
        """This method creates an Elastic object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].materials[name].Elastic
            session.odbs[name].materials[name].Elastic

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        type
            A SymbolicConstant specifying the type of elasticity data provided. Possible values are:

            - ISOTROPIC
            - ORTHOTROPIC
            - ANISOTROPIC
            - ENGINEERING_CONSTANTS
            - LAMINA
            - TRACTION
            - COUPLED_TRACTION
            - SHORT_FIBER
            - SHEAR
            - BILAMINA
            The default value is ISOTROPIC.
        noCompression
            A Boolean specifying whether compressive stress is allowed. The default value is OFF.
        noTension
            A Boolean specifying whether tensile stress is allowed. The default value is OFF.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        moduli
            A SymbolicConstant specifying the time-dependence of the elastic material constants.
            Possible values are INSTANTANEOUS and LONG_TERM. The default value is LONG_TERM.

        Returns
        -------
            An Elastic object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self):
        """This method modifies the Elastic object.

        Raises
        ------
        RangeError
        """
        pass
