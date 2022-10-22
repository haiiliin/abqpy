from typing_extensions import Literal
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ....UtilityAndView.abaqusConstants import abaqusConstants as C
from ....UtilityAndView.abaqusConstants import Boolean, ISOTROPIC, OFF, SymbolicConstant


@abaqus_class_doc
class Dielectric:
    r"""The Dielectric object specifies dielectric material properties.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].dielectric
            import odbMaterial
            session.odbs[name].materials[name].dielectric

        The table data for this object are:

        - If **type** = ISOTROPIC, the table data specify the following:
        
            - Dielectric constant.
            - Frequency, if the data depend on frequency.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = ORTHOTROPIC, the table data specify the following:
        
            - :math:`D_{11}^{\varphi}`
            - :math:`D_{22}^{\varphi}`.
            - :math:`D_{33}^{\varphi}`
            - Frequency, if the data depend on frequency.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = ANISOTROPIC, the table data specify the following:
        
            - :math:`D_{11}^{\varphi}`
            - :math:`D_{12}^{\varphi}`
            - :math:`D_{22}^{\varphi}`
            - :math:`D_{13}^{\varphi}`
            - :math:`D_{23}^{\varphi}`
            - :math:`D_{33}^{\varphi}`
            - Frequency, if the data depend on frequency.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - DIELECTRIC
    """

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        type: Literal[C.ANISOTROPIC, C.ISOTROPIC, C.ORTHOTROPIC] = ISOTROPIC,
        frequencyDependency: Boolean = OFF,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a Dielectric object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].Dielectric
                session.odbs[name].materials[name].Dielectric

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        type
            A SymbolicConstant specifying the dielectric behavior. Possible values are ISOTROPIC,
            ORTHOTROPIC, and ANISOTROPIC. The default value is ISOTROPIC.
        frequencyDependency
            A Boolean specifying whether the data depend on frequency. The default value is OFF.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        Dielectric
            A :py:class:`~abaqus.Material.Others.Electromagnetic.Dielectric.Dielectric` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Dielectric object."""
        ...
