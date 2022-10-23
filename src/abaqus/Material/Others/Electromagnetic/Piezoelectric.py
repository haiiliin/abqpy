from typing_extensions import Literal
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ....UtilityAndView.abaqusConstants import abaqusConstants as C
from ....UtilityAndView.abaqusConstants import Boolean, OFF, STRESS


@abaqus_class_doc
class Piezoelectric:
    r"""The Piezoelectric object specifies piezoelectric material properties.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].piezoelectric
            import odbMaterial
            session.odbs[name].materials[name].piezoelectric

        The table data for this object are:

        - If **type** = STRESS, the table data specify the following:
        
            - :math:`e_{111}^{\varphi}`.
            - :math:`e_{122}^{\varphi}`.
            - :math:`e_{133}^{\varphi}`.
            - :math:`e_{112}^{\varphi}`.
            - :math:`e_{113}^{\varphi}`.
            - :math:`e_{123}^{\varphi}`.
            - :math:`e_{211}^{\varphi}`.
            - :math:`e_{222}^{\varphi}`.
            - :math:`e_{233}^{\varphi}`.
            - :math:`e_{212}^{\varphi}`.
            - :math:`e_{213}^{\varphi}`.
            - :math:`e_{223}^{\varphi}`.
            - :math:`e_{311}^{\varphi}`.
            - :math:`e_{322}^{\varphi}`.
            - :math:`e_{333}^{\varphi}`.
            - :math:`e_{312}^{\varphi}`.
            - :math:`e_{313}^{\varphi}`.
            - :math:`e_{323}^{\varphi}`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = STRAIN, the table data specify the following:
        
            - :math:`d_{111}^{\varphi}`.
            - :math:`d_{122}^{\varphi}`.
            - :math:`d_{133}^{\varphi}`.
            - :math:`d_{112}^{\varphi}`.
            - :math:`d_{113}^{\varphi}`.
            - :math:`d_{123}^{\varphi}`.
            - :math:`d_{211}^{\varphi}`.
            - :math:`d_{222}^{\varphi}`.
            - :math:`d_{233}^{\varphi}`.
            - :math:`d_{212}^{\varphi}`.
            - :math:`d_{213}^{\varphi}`.
            - :math:`d_{223}^{\varphi}`.
            - :math:`d_{311}^{\varphi}`.
            - :math:`d_{322}^{\varphi}`.
            - :math:`d_{333}^{\varphi}`.
            - :math:`d_{313}^{\varphi}`.
            - :math:`d_{323}^{\varphi}`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - PIEZOELECTRIC
    """

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        type: Literal[C.STRESS, C.STRAIN] = STRESS,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a Piezoelectric object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].Piezoelectric
                session.odbs[name].materials[name].Piezoelectric

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        type
            A SymbolicConstant specifying the type of material coefficients for the piezoelectric
            property. Possible values are STRAIN and STRESS. The default value is STRESS.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        Piezoelectric
            A :py:class:`~abaqus.Material.Others.Electromagnetic.Piezoelectric.Piezoelectric` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Piezoelectric object."""
        ...
