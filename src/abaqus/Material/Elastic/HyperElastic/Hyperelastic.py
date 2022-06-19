import typing

from abaqusConstants import *
from .ViscoElastic.Hysteresis import Hysteresis
from ...TestData.BiaxialTestData import BiaxialTestData
from ...TestData.PlanarTestData import PlanarTestData
from ...TestData.UniaxialTestData import UniaxialTestData
from ...TestData.VolumetricTestData import VolumetricTestData


class Hyperelastic:
    """The Hyperelastic object specifies elastic properties for approximately incompressible
    elastomers.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].hyperelastic
        import odbMaterial
        session.odbs[name].materials[name].hyperelastic

    The table data for this object are:

    - If **type**=ARRUDA_BOYCE, the table data specify the following:
    
        - μ.
        - λm.
        - D.
        - Temperature, if the data depend on temperature.
    - If **type**=MOONEY_RIVLIN, the table data specify the following:
    
        - C10.
        - C01.
        - D1.
        - Temperature, if the data depend on temperature.
    - If **type**=NEO_HOOKE, the table data specify the following:
    
        - C10.
        - D1.
        - Temperature, if the data depend on temperature.
    - If **type**=OGDEN, the table data specify the following for values of nn:
    
        - μi and αi for ii from 1 to n.
        - nn coefficients Di.
        - Temperature, if the data depend on temperature. Temperature dependence is not allowed for 4 ≤n≤ 6 in an
          Abaqus/Explicit analysis.
    - If **type**=POLYNOMIAL, the table data specify the following for values of nn:
    
        - CijCi⁢j for each value of (i+j) from 11 to n with ii decreasing from (i+j) to zero and j 
          increasing from zero to (i+j).
        - n coefficients Di.
        - Temperature, if the data depend on temperature. Temperature dependence is not allowed for 3 ≤n≤ 6 in an
          Abaqus/Explicit analysis.
    - If **type**=REDUCED_POLYNOMIAL, the table data specify the following for values of nn:
        - Ci⁢0 for ii from 1 to n.
        - n coefficients Di.
        - Temperature, if the data depend on temperature. Temperature dependence is not allowed for 4 ≤n≤ 6 in an
          Abaqus/Explicit analysis.
    - If **type**=VAN_DER_WAALS, the table data specify the following:
    
        - μ.
        - λm.
        - a.
        - β.
        - D.
        - Temperature, if the data depend on temperature.
    - If **type**=YEOH, the table data specify the following:
    
        - C10.
        - C20.
        - C30.
        - D1.
        - D2.
        - D3.
        - Temperature, if the data depend on temperature. Temperature dependence is not allowed in an Abaqus/Explicit analysis.
    The None object is the default value if **testData**=ON.

    The corresponding analysis keywords are:

    - HYPERELASTIC
    """

    # A BiaxialTestData object.
    biaxialTestData: BiaxialTestData = BiaxialTestData(((),))

    # A PlanarTestData object.
    planarTestData: PlanarTestData = PlanarTestData(((),))

    # A UniaxialTestData object.
    uniaxialTestData: UniaxialTestData = UniaxialTestData(((),))

    # A VolumetricTestData object.
    volumetricTestData: VolumetricTestData = VolumetricTestData(((),))

    # A Hysteresis object.
    hysteresis: Hysteresis = Hysteresis(((),))

    def __init__(
        self,
        table: tuple,
        type: SymbolicConstant = UNKNOWN,
        moduliTimeScale: SymbolicConstant = LONG_TERM,
        temperatureDependency: Boolean = OFF,
        n: int = 1,
        beta: typing.Union[SymbolicConstant, float] = FITTED_VALUE,
        testData: Boolean = ON,
        compressible: Boolean = OFF,
        properties: int = 0,
        deviatoricResponse: SymbolicConstant = UNIAXIAL,
        volumetricResponse: SymbolicConstant = DEFAULT,
        poissonRatio: float = 0,
        materialType: SymbolicConstant = ISOTROPIC,
        anisotropicType: SymbolicConstant = FUNG_ANISOTROPIC,
        formulation: SymbolicConstant = STRAIN,
        behaviorType: SymbolicConstant = INCOMPRESSIBLE,
        dependencies: int = 0,
        localDirections: int = 0,
    ):
        """This method creates a Hyperelastic object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].materials[name].Hyperelastic
            session.odbs[name].materials[name].Hyperelastic

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. This argument is
            valid only if **testData**=OFF.
        type
            A SymbolicConstant specifying the type of strain energy potential. Possible values
            are:

            - ARRUDA_BOYCE
            - MARLOW
            - MOONEY_RIVLIN
            - NEO_HOOKE
            - OGDEN
            - POLYNOMIAL
            - REDUCED_POLYNOMIAL
            - USER
            - VAN_DER_WAALS
            - YEOH
            - UNKNOWN

            The default value is UNKNOWN.
        moduliTimeScale
            A SymbolicConstant specifying the nature of the time response. Possible values are
            INSTANTANEOUS and LONG_TERM. The default value is LONG_TERM.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        n
            An Int specifying the order of the strain energy potential. The default value is 1.If
            **testData**=ON and **type**=POLYNOMIAL, **n** can take only the values 1 or 2.If
            **testData**=ON and **type**=OGDEN or if **testData**=OFF for either type, 1 ≤n≤≤n≤ 6.If
            **type**=USER, this argument cannot be used.
        beta
            The SymbolicConstant FITTED_VALUE or a Float specifying the invariant mixture parameter.
            This argument is valid only if **testData**=ON and **type**=VAN_DER_WAALS. The default value
            is FITTED_VALUE.
        testData
            A Boolean specifying whether test data are supplied. The default value is ON.
        compressible
            A Boolean specifying whether the hyperelastic material is compressible. This parameter
            is applicable only to user-defined hyperelastic materials. The default value is OFF.
        properties
            An Int specifying the number of property values needed as data for the user-defined
            hyperelastic material. The default value is 0.
        deviatoricResponse
            A SymbolicConstant specifying which test data to use. Possible values are UNIAXIAL,
            BIAXIAL, and PLANAR. The default value is UNIAXIAL.
        volumetricResponse
            A SymbolicConstant specifying the volumetric response. Possible values are DEFAULT,
            VOLUMETRIC_DATA, POISSON_RATIO, and LATERAL_NOMINAL_STRAIN. The default value is
            DEFAULT.
        poissonRatio
            A Float specifying the poisson ratio. This argument is valid only if
            **volumetricResponse**=POISSON_RATIO. The default value is 0.0.
        materialType
            A SymbolicConstant specifying the type of material. Possible values are ISOTROPIC and
            ANISOTROPIC. The default value is ISOTROPIC.
        anisotropicType
            A SymbolicConstant specifying the type of strain energy potential. Possible values are
            FUNG_ANISOTROPIC, FUNG_ORTHOTROPIC, HOLZAPFEL, and USER_DEFINED. The default value is
            FUNG_ANISOTROPIC.
        formulation
            A SymbolicConstant specifying the type of formulation. Possible values are STRAIN and
            INVARIANT. The default value is STRAIN.
        behaviorType
            A SymbolicConstant specifying the type of anisotropic hyperelastic material behavior.
            Possible values are INCOMPRESSIBLE and COMPRESSIBLE. The default value is
            INCOMPRESSIBLE.
        dependencies
            An Int specifying the number of field variable dependencies for the data
            in*volumetricTable* . The default value is 0.
        localDirections
            An Int specifying the number of local directions for the data in*volumetricTable* . The
            default value is 0.

        Returns
        -------
            A Hyperelastic object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        pass

    def setValues(self):
        """This method modifies the Hyperelastic object.

        Raises
        ------
        RangeError
        """
        pass
