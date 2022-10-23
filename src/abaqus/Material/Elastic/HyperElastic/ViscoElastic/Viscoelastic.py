from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .CombinedTestData import CombinedTestData
from ....Others.Mechanical.Viscosity.Trs import Trs
from ....TestData.ShearTestData import ShearTestData
from ....TestData.VolumetricTestData import VolumetricTestData
from .....UtilityAndView.abaqusConstants import FORMULA, ISOTROPIC, NONE, PRONY
from .....UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class Viscoelastic:
    r"""The Viscoelastic object specifies dissipative behavior for use with elasticity.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].viscoelastic
            import odbMaterial
            session.odbs[name].materials[name].viscoelastic

        The table data for this object are:

        - If **frequency** = FORMULA, the table data for **table** specify the following:

            - Real part of :math:`g_{1}^{*}\left(g^{*}(\omega)=g_{1}^{*} f^{-a}\right)`
            - Imaginary part of :math:`g_{1}^{*}`.
            - Value of :math:`a`.
            - Real part of :math:`k_{1}^{*}\left(k^{*}(\omega)=k_{1}^{*} f^{-b}\right)`. If
              the material is incompressible, this value is ignored.
            - Imaginary part of :math:`k_{1}^{*}`. If the material is incompressible, this
              value is ignored.
            - Value of :math:`b`. If the material is incompressible, this value is ignored.

        - If **frequency** = TABULAR and **type** = ISOTROPIC and **preload** = NONE, or **time** = FREQUENCY_DATA
          the table data for **table** specify the following:

            - Real part of :math:`\omega g^{*}\left(\omega \Re\left(g^{*}\right)=G_{\ell} / G_{\infty}\right)`.
            - Imaginary part of :math:`\omega g^{*}\left(\omega \mathfrak{J}\left(g^{*}\right)=1-G_{s} / G_{\infty}\right)`
            - Real part of :math:`\omega k^{*}\left(\omega \mathfrak{R}\left(k^{*}\right)=\mathrm{K}_{\ell} / \mathrm{K}_{\infty}\right)`. If the material is incompressible, this value is ignored.
            - Imaginary part of :math:`\omega k^{*}\left(\omega \mathfrak{I}\left(k^{*}\right)=1-\mathrm{K}_{s} / \mathrm{K}_{\infty}\right)`. If the material is incompressible, this value is ignored.
            - Frequency :math:`f` in cycles per time.

        - If **frequency** = TABULAR and **type** = ISOTROPIC and **preload** = UNIAXIAL the table data for **table**
          specify the following:

            - Loss modulus.
            - Storage modulus.
            - Frequency.
            - Uniaxial strain.

        - If **frequency** = TABULAR and **type** = TRACTION and **preload** = NONE the table data for **table**
          specify the following:

            - Normalized loss modulus.
            - Normalized shear modulus.
            - Frequency.

        - If **frequency** = TABULAR and **type** = TRACTION and **preload** = UNIAXIAL or
          **preload** = UNIAXIAL_VOLUMETRIC the table data for **table** specify the following:

            - Loss modulus.
            - Storage modulus.
            - Frequency.
            - Closure.

        - If **time** = PRONY or **frequency** = PRONY, the table data for **table** specify the following:

            - :math:`\bar{g}_{1}^{P}`, the modulus ratio in the first term in the Prony series
              expansion of the shear relaxation modulus.
            - :math:`\bar{k}_{1}^{P}`, the modulus ratio in the first term in the Prony series
              expansion of the bulk relaxation modulus.
            - :math:`\tau_{1}`, the relaxation time for the first term in the Prony series expansion.

        - If **frequency** = TABULAR and **type** = ISOTROPIC and **preload** = VOLUMETRIC or
          **preload** = UNIAXIAL_VOLUMETRIC the table data for **volumetricTable** specify the following:

            - Loss modulus.
            - Storage modulus.
            - Frequency.
            - Volume ratio.

        The corresponding analysis keywords are:

        - VISCOELASTIC
    """

    #: A :py:class:`~abaqus.Material.Elastic.HyperElastic.ViscoElastic.CombinedTestData.CombinedTestData` object.
    combinedTestData: CombinedTestData = CombinedTestData(((),))

    #: A :py:class:`~abaqus.Material.TestData.ShearTestData.ShearTestData` object.
    shearTestData: ShearTestData = ShearTestData(((),))

    #: A :py:class:`~abaqus.Material.Others.Mechanical.Viscosity.Trs.Trs` object.
    trs: Trs = Trs()

    #: A :py:class:`~abaqus.Material.TestData.VolumetricTestData.VolumetricTestData` object.
    volumetricTestData: VolumetricTestData = VolumetricTestData(((),))

    @abaqus_method_doc
    def __init__(
        self,
        domain: Literal[C.FREQUENCY, C.TIME],
        table: tuple,
        frequency: Literal[
            C.PRONY, C.CREEP_TEST_DATA, C.TABULAR, C.FREQUENCY, C.RELAXATION_TEST_DATA, C.FORMULA
        ] = FORMULA,
        type: Literal[C.FREQUENCY, C.TRACTION, C.ISOTROPIC, C.TABULAR] = ISOTROPIC,
        preload: Literal[C.VOLUMETRIC, C.UNIAXIAL, C.TABULAR, C.FREQUENCY, C.UNIAXIAL_VOLUMETRIC, C.NONE] = NONE,
        time: Literal[C.PRONY, C.CREEP_TEST_DATA, C.FREQUENCY_DATA, C.TIME, C.RELAXATION_TEST_DATA] = PRONY,
        errtol: float = 0,
        nmax: int = 13,
        volumetricTable: tuple = (),
    ):
        """This method creates a Viscoelastic object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].Viscoelastic
                session.odbs[name].materials[name].Viscoelastic

        Parameters
        ----------
        domain
            A SymbolicConstant specifying the domain definition. Possible values are:
            - FREQUENCY, specifying a frequency domain. This domain is only available for an Abaqus/Standard analysis.
            - TIME, specifying a time domain.
        table
            A sequence of sequences of Floats specifying the items described below.
        frequency
            A SymbolicConstant specifying the frequency domain definition. This argument is required
            only when **domain** = FREQUENCY. Possible values are FORMULA, TABULAR, PRONY,
            CREEP_TEST_DATA, and RELAXATION_TEST_DATA. The default value is FORMULA.
        type
            A SymbolicConstant specifying the type. This argument is required only when
            **domain** = FREQUENCY and **frequency** = TABULAR. Possible values are ISOTROPIC and TRACTION.
            The default value is ISOTROPIC.
        preload
            A SymbolicConstant specifying the preload. This argument is required only when
            **domain** = FREQUENCY and **frequency** = TABULAR. Possible values are NONE, UNIAXIAL,
            VOLUMETRIC, and UNIAXIAL_VOLUMETRIC. The default value is NONE.
        time
            A SymbolicConstant specifying the time domain definition. This argument is required only
            when **domain** = TIME. Possible values are PRONY, CREEP_TEST_DATA, RELAXATION_TEST_DATA,
            and FREQUENCY_DATA. The default value is PRONY.
        errtol
            A Float specifying the allowable average root-mean-square error of the data points in
            the least-squares fit. The Float values correspond to percentages; for example, 0.01 is
            1%. The default value is 0.01.This argument is valid only when **time** = CREEP_TEST_DATA,
            RELAXATION_TEST_DATA or FREQUENCY_DATA; or only when **frequency** = CREEP_TEST_DATA or
            RELAXATION_TEST_DATA.
        nmax
            An Int specifying the maximum number of terms NN in the Prony series. The maximum value
            is 13. The default value is 13.This argument is valid only when **time** = CREEP_TEST_DATA,
            RELAXATION_TEST_DATA or FREQUENCY_DATA; or only when **frequency** = CREEP_TEST_DATA or
            RELAXATION_TEST_DATA.
        volumetricTable
            A sequence of sequences of Floats specifying the items described below. The default
            value is an empty sequence.

        Returns
        -------
        Viscoelastic
            A :py:class:`~abaqus.Material.Elastic.HyperElastic.ViscoElastic.Viscoelastic.Viscoelastic` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Viscoelastic object.

        Raises
        ------
        RangeError
        """
        ...
