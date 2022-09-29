import typing
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ...TestData.UniaxialTestData import UniaxialTestData
from ....UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class LowDensityFoam:
    """The LowDensityFoam object specifies properties for low-density foam.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].lowDensityFoam
            import odbMaterial
            session.odbs[name].materials[name].lowDensityFoam

        The corresponding analysis keywords are:

        - LOW DENSITY FOAM
    """

    #: A :py:class:`~abaqus.Material.TestData.UniaxialTestData.UniaxialTestData` object.
    uniaxialTensionTestData: UniaxialTestData = UniaxialTestData(((),))

    #: A :py:class:`~abaqus.Material.TestData.UniaxialTestData.UniaxialTestData` object.
    uniaxialCompressionTestData: UniaxialTestData = UniaxialTestData(((),))

    @abaqus_method_doc
    def __init__(
        self,
        elementRemoval: Boolean = OFF,
        maxAllowablePrincipalStress: typing.Optional[float] = None,
        extrapolateStressStrainCurve: Boolean = OFF,
        strainRateType: SymbolicConstant = VOLUMETRIC,
        mu0: typing.Optional[float] = None,
        mu1: float = 0,
        alpha: float = 2,
    ):
        """This method creates a LowDensityFoam object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].LowDensityFoam
                session.odbs[name].materials[name].LowDensityFoam

        Parameters
        ----------
        elementRemoval
            A Boolean specifying whether elements are removed if exceeding maximum principal tensile
            stress. This argument is valid only when **maxAllowablePrincipalStress** is defined. The
            default value is OFF.
        maxAllowablePrincipalStress
            None or a Float specifying the maximum allowable principal tensile stress. The default
            value is None.
        extrapolateStressStrainCurve
            A Boolean specifying whether the stress-strain curve is extrapolated if exceeding
            maximum strain rate. The default value is OFF.
        strainRateType
            A SymbolicConstant specifying strain rate measure used for constitutive calculations.
            Possible values are PRINCIPAL and VOLUMETRIC. The default value is VOLUMETRIC.
        mu0
            A Float specifying the relaxation coefficient μ0. The default value is 10-4.
        mu1
            A Float specifying the relaxation coefficient μ1. The default value is 0.5×10-2.
        alpha
            A Float specifying the relaxation coefficient α. The default value is 2.0.

        Returns
        -------
        LowDensityFoam
            A :py:class:`~abaqus.Material.Elastic.LowDensityFoam.LowDensityFoam.LowDensityFoam` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the LowDensityFoam object.

        Raises
        ------
        RangeError
        """
        ...
