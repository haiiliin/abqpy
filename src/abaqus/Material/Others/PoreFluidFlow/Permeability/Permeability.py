from typing_extensions import Literal
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .SaturationDependence import SaturationDependence
from .VelocityDependence import VelocityDependence
from .....UtilityAndView.abaqusConstants import abaqusConstants as C
from .....UtilityAndView.abaqusConstants import Boolean, ISOTROPIC, OFF


@abaqus_class_doc
class Permeability:
    """The Permeability object defines permeability for pore fluid flow.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].permeability
            import odbMaterial
            session.odbs[name].materials[name].permeability

        The table data for this object are:

        - If **type** = ISOTROPIC, the table data specify the following:
        
            - :math:`k`.
            - Void ratio, :math:`e`.
            - Temperature, if the data depend on temperature.
        - If **type** = ORTHOTROPIC, the table data specify the following:
        
            - :math:`k_{11}`.
            - :math:`k_{22}`.
            - :math:`k_{33}`.
            - Void ratio, :math:`e`.
            - Temperature, if the data depend on temperature.
        - If **type** = ANISOTROPIC, the table data specify the following:
        
            - :math:`k_{11}`.
            - :math:`k_{12}`.
            - :math:`k_{22}`.
            - :math:`k_{13}`.
            - :math:`k_{23}`.
            - :math:`k_{33}`.
            - Void ratio, :math:`e`.
            - Temperature, if the data depend on temperature.

        The corresponding analysis keywords are:

        - PERMEABILITY
    """

    #: A :py:class:`~abaqus.Material.Others.PoreFluidFlow.Permeability.SaturationDependence.SaturationDependence` object specifying the dependence of the permeability of a
    #: material on the saturation of the wetting liquid.
    saturationDependence: SaturationDependence = SaturationDependence(((),))

    #: A :py:class:`~abaqus.Material.Others.PoreFluidFlow.Permeability.VelocityDependence.VelocityDependence` object specifying the dependence of the permeability of a material
    #: on the velocity of fluid flow.
    velocityDependence: VelocityDependence = VelocityDependence(((),))

    @abaqus_method_doc
    def __init__(
        self,
        specificWeight: float,
        inertialDragCoefficient: float,
        table: tuple,
        type: Literal[C.ANISOTROPIC, C.ISOTROPIC, C.ORTHOTROPIC] = ISOTROPIC,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        r"""This method creates a Permeability object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].Permeability
                session.odbs[name].materials[name].Permeability

        Parameters
        ----------
        specificWeight
            A Float specifying the specific weight of the wetting liquid, :math:`\gamma_w`.
        inertialDragCoefficient
            A Float specifying The inertial drag coefficient of the wetting liquid, :math:`\gamma_w`.
        table
            A sequence of sequences of Floats specifying the items described below.
        type
            A SymbolicConstant specifying the type of permeability. Possible values are ISOTROPIC,
            ORTHOTROPIC, and ANISOTROPIC. The default value is ISOTROPIC.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        Permeability
            A :py:class:`~abaqus.Material.Others.PoreFluidFlow.Permeability.Permeability.Permeability` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Permeability object.

        Raises
        ------
        RangeError
        """
        ...
