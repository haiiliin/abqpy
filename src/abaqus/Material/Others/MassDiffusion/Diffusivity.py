from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .PressureEffect import PressureEffect
from .SoretEffect import SoretEffect
from ....UtilityAndView.abaqusConstants import Boolean, GENERAL, ISOTROPIC, OFF, SymbolicConstant


@abaqus_class_doc
class Diffusivity:
    r"""The Diffusivity object specifies mass diffusivity.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].diffusivity
            import odbMaterial
            session.odbs[name].materials[name].diffusivity

        The table data for this object are:

        - If **type** = ISOTROPIC, the table data specify the following:
        
            - Diffusivity, :math:`D`.
            - Concentration, :math:`c`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = ORTHOTROPIC, the table data specify the following:
        
            - :math:`D_{11}`.
            - :math:`D_{22}`.
            - :math:`D_{33}`.
            - Concentration, :math:`c`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = ANISOTROPIC, the table data specify the following:
        
            - :math:`D_{11}`.
            - :math:`D_{12}`.
            - :math:`D_{22}`.
            - :math:`D_{13}`.
            - :math:`D_{23}`.
            - :math:`D_{33}`.
            - Concentration, :math:`c`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - DIFFUSIVITY
    """

    #: A :py:class:`~abaqus.Material.Others.MassDiffusion.PressureEffect.PressureEffect` object.
    pressureEffect: PressureEffect = PressureEffect(((),))

    #: A :py:class:`~abaqus.Material.Others.MassDiffusion.SoretEffect.SoretEffect` object.
    soretEffect: SoretEffect = SoretEffect(((),))

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        type: SymbolicConstant = ISOTROPIC,
        law: SymbolicConstant = GENERAL,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a Diffusivity object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].Diffusivity
                session.odbs[name].materials[name].Diffusivity

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        type
            A SymbolicConstant specifying the type of diffusivity. Possible values are ISOTROPIC,
            ORTHOTROPIC, and ANISOTROPIC. The default value is ISOTROPIC.
        law
            A SymbolicConstant specifying the diffusion behavior. Possible values are GENERAL and
            FICK. The default value is GENERAL.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        Diffusivity
            A :py:class:`~abaqus.Material.Others.MassDiffusion.Diffusivity.Diffusivity` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Diffusivity object.

        Raises
        ------
        RangeError
        """
        ...
