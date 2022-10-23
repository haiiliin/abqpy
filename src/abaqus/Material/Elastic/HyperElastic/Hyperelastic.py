from typing import Union

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .ViscoElastic.Hysteresis import Hysteresis
from ...TestData.BiaxialTestData import BiaxialTestData
from ...TestData.PlanarTestData import PlanarTestData
from ...TestData.UniaxialTestData import UniaxialTestData
from ...TestData.VolumetricTestData import VolumetricTestData
from ....UtilityAndView.abaqusConstants import (
    Boolean,
    DEFAULT,
    FITTED_VALUE,
    FUNG_ANISOTROPIC,
    INCOMPRESSIBLE,
    ISOTROPIC,
    LONG_TERM,
    OFF,
    ON,
    STRAIN,
    UNIAXIAL,
    UNKNOWN,
)
from ....UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class Hyperelastic:
    r"""The Hyperelastic object specifies elastic properties for approximately incompressible
    elastomers.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].hyperelastic
            import odbMaterial
            session.odbs[name].materials[name].hyperelastic

        The table data for this object are:

        - If **type** = ARRUDA_BOYCE, the table data specify the following:

            - :math:`\mu`.
            - :math:`\lambda_{m}`.
            - :math:`D`.
            - Temperature, if the data depend on temperature.

        - If **type** = MOONEY_RIVLIN, the table data specify the following:

            - :math:`C_{10}`
            - :math:`C_{01}`.
            - :math:`D_{1}`.
            - Temperature, if the data depend on temperature.

        - If **type** = NEO_HOOKE, the table data specify the following:

            - :math:`C_{10}`
            - :math:`D_{1}`.
            - Temperature, if the data depend on temperature.

        - If **type** = OGDEN, the table data specify the following for values of nn:

            - :math:`\mu_{i}` and :math:`\alpha_{i}` for :math:`i` from 1 to :math:`n`.
            - :math:`n` coefficients :math:`D_{i}`.
            - Temperature, if the data depend on temperature. Temperature dependence is not
              allowed for :math:`4 \leq n \leq 6` in an Abaqus/Explicit analysis.

        - If **type** = POLYNOMIAL, the table data specify the following for values of nn:

            - :math:`C_{i j}` for each value of :math:`(i+j)` from 1 to :math:`n` with
              :math:`i` decreasing from :math:`(i+j)` to zero and :math:`j` increasing
              from zero to :math:`(i+j)`.
            - :math:`n` coefficients :math:`D_{i}`
            - Temperature, if the data depend on temperature. Temperature dependence is
              not allowed for :math:`3 \leq n \leq 6` in an Abaqus/Explicit analysis.

        - If **type** = REDUCED_POLYNOMIAL, the table data specify the following for values of nn:

            - :math:`C_{i 0}` for :math:`i` from 1 to :math:`n`.
            - :math:`n` coefficients :math:`D_{i}`
            - Temperature, if the data depend on temperature. Temperature dependence
              is not allowed for :math:`4 \leq n \leq 6` in an Abaqus/Explicit analysis.

        - If **type** = VAN_DER_WAALS, the table data specify the following:

            - :math:`\mu`.
            - :math:`\lambda_{m}`.
            - :math:`a`.
            - :math:`\beta`.
            - :math:`D`.
            - Temperature, if the data depend on temperature.

        - If **type** = YEOH, the table data specify the following:

            - :math:`C_{10}`
            - :math:`C_{20}`
            - :math:`C_{30}`
            - :math:`D_{1}`.
            - :math:`D_{2}`
            - :math:`D_{3}`.
            - Temperature, if the data depend on temperature. Temperature dependence
              is not allowed in an Abaqus/Explicit analysis.

        The None object is the default value if **testData** = ON.

        The corresponding analysis keywords are:

        - HYPERELASTIC
    """

    #: A :py:class:`~abaqus.Material.TestData.BiaxialTestData.BiaxialTestData` object.
    biaxialTestData: BiaxialTestData = BiaxialTestData(((),))

    #: A :py:class:`~abaqus.Material.TestData.PlanarTestData.PlanarTestData` object.
    planarTestData: PlanarTestData = PlanarTestData(((),))

    #: A :py:class:`~abaqus.Material.TestData.UniaxialTestData.UniaxialTestData` object.
    uniaxialTestData: UniaxialTestData = UniaxialTestData(((),))

    #: A :py:class:`~abaqus.Material.TestData.VolumetricTestData.VolumetricTestData` object.
    volumetricTestData: VolumetricTestData = VolumetricTestData(((),))

    #: A :py:class:`~abaqus.Material.Elastic.HyperElastic.ViscoElastic.Hysteresis.Hysteresis` object.
    hysteresis: Hysteresis = Hysteresis(((),))

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        type: Literal[
            C.MARLOW,
            C.MOONEY_RIVLIN,
            C.POLYNOMIAL,
            C.YEOH,
            C.ARRUDA_BOYCE,
            C.REDUCED_POLYNOMIAL,
            C.UNKNOWN,
            C.VALANIS_LANDEL,
            C.USER,
            C.OGDEN,
            C.VAN_DER_WAALS,
            C.NEO_HOOKE,
        ] = UNKNOWN,
        moduliTimeScale: Literal[C.INSTANTANEOUS, C.LONG_TERM] = LONG_TERM,
        temperatureDependency: Boolean = OFF,
        n: int = 1,
        beta: Union[Literal[C.FITTED_VALUE, C.VAN_DER_WAALS], float] = FITTED_VALUE,
        testData: Boolean = ON,
        compressible: Boolean = OFF,
        properties: int = 0,
        deviatoricResponse: Literal[C.PLANAR, C.UNIAXIAL, C.BIAXIAL] = UNIAXIAL,
        volumetricResponse: Literal[C.LATERAL_NOMINAL_STRAIN, C.VOLUMETRIC_DATA, C.DEFAULT, C.POISSON_RATIO] = DEFAULT,
        poissonRatio: float = 0,
        materialType: Literal[C.ANISOTROPIC, C.ISOTROPIC] = ISOTROPIC,
        anisotropicType: Literal[
            C.USER_DEFINED, C.FUNG_ANISOTROPIC, C.HOLZAPFEL, C.FUNG_ORTHOTROPIC
        ] = FUNG_ANISOTROPIC,
        formulation: Literal[C.STRAIN, C.INVARIANT] = STRAIN,
        behaviorType: Literal[C.COMPRESSIBLE, C.INCOMPRESSIBLE] = INCOMPRESSIBLE,
        dependencies: int = 0,
        localDirections: int = 0,
    ):
        """This method creates a Hyperelastic object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].Hyperelastic
                session.odbs[name].materials[name].Hyperelastic

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. This argument is
            valid only if **testData** = OFF.
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
            - VALANIS_LANDEL

            The default value is UNKNOWN.

            .. versionchanged:: 2022
                Add available value: VALANIS_LANDEL.
        moduliTimeScale
            A SymbolicConstant specifying the nature of the time response. Possible values are
            INSTANTANEOUS and LONG_TERM. The default value is LONG_TERM.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        n
            An Int specifying the order of the strain energy potential. The default value is 1.If
            **testData** = ON and **type** = POLYNOMIAL, **n** can take only the values 1 or 2.If
            **testData** = ON and **type** = OGDEN or if **testData** = OFF for either type, 1 ≤n≤n≤ 6.If
            **type** = USER, this argument cannot be used.
        beta
            The SymbolicConstant FITTED_VALUE or a Float specifying the invariant mixture parameter.
            This argument is valid only if **testData** = ON and **type** = VAN_DER_WAALS. The default value
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
            **volumetricResponse** = POISSON_RATIO. The default value is 0.0.
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
        Hyperelastic
            A :py:class:`~abaqus.Material.Elastic.HyperElastic.Hyperelastic.Hyperelastic` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Hyperelastic object.

        Raises
        ------
        RangeError
        """
        ...
