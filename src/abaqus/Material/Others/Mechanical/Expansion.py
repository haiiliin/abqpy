from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ....UtilityAndView.abaqusConstants import Boolean, ISOTROPIC, OFF
from ....UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class Expansion:
    r"""The Expansion object specifies thermal expansion.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].expansion
            import odbMaterial
            session.odbs[name].materials[name].expansion

        The table data for this object are:

        - If **type** = ISOTROPIC, the table data specify the following:

            - :math:`\alpha` in Abaqus/Standard or Abaqus/Explicit analysis.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = ORTHOTROPIC, the table data specify the following:

            - :math:`\alpha_{11}`.
            - :math:`\alpha_{22}`.
            - :math:`\alpha_{33}`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = ANISOTROPIC, the table data specify the following:

            - :math:`\alpha_{11}`.
            - :math:`\alpha_{22}`.
            - :math:`\alpha_{33}`. (Not used for plane stress case.)
            - :math:`\alpha_{12}`.
            - :math:`\alpha_{13}`.
            - :math:`\alpha_{23}`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = SHORT_FIBER, there is no table data.

        The corresponding analysis keywords are:

        - EXPANSION
    """

    @abaqus_method_doc
    def __init__(
        self,
        type: Literal[C.ANISOTROPIC, C.ISOTROPIC, C.SHORT_FIBER, C.ORTHOTROPIC] = ISOTROPIC,
        userSubroutine: Boolean = OFF,
        zero: float = 0,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        table: tuple = (),
    ):
        r"""This method creates an Expansion object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].Expansion
                session.odbs[name].materials[name].Expansion

        Parameters
        ----------
        type
            A SymbolicConstant specifying the type of expansion. Possible values are ISOTROPIC,
            ORTHOTROPIC, ANISOTROPIC, and SHORT_FIBER. The default value is ISOTROPIC.
        userSubroutine
            A Boolean specifying whether a user subroutine is used to define the increments of
            thermal strain. The default value is OFF.
        zero
            A Float specifying the value of :math:`\theta_0` if the thermal expansion is temperature-dependent or
            field-variable-dependent. The default value is 0.0.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        table
            A sequence of sequences of Floats specifying the items described below. The default
            value is an empty sequence.This argument is required only if **type** is not USER.

        Returns
        -------
        Expansion
            An :py:class:`~abaqus.Material.Others.Mechanical.Expansion.Expansion` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Expansion object.

        Raises
        ------
        RangeError
        """
        ...
