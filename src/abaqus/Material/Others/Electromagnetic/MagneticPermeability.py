from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ....UtilityAndView.abaqusConstants import Boolean, ISOTROPIC, OFF
from ....UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class MagneticPermeability:
    r"""The MagneticPermeability object specifies magnetic permeability.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].magneticPermeability
            import odbMaterial
            session.odbs[name].materials[name].magneticPermeability

        The table data for this object are:

        - If **type** = ISOTROPIC, the table data specify the following:

            - Magnetic permeability.
            - Frequency, if the data depend on frequency.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = ISOTROPIC, and **nonlinearBH** = TRUE, the table data specify the following:

            - Magntitude of the magnetic flux density vector.
            - Magnitude of the magnetic field vector.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = ORTHOTROPIC, the table data specify the following:

            - :math:`\mu_{11}^{E}`.
            - :math:`\mu_{22}^{E}`.
            - :math:`\mu_{33}^{E}`.
            - Frequency, if the data depend on frequency.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = ORTHOTROPIC, and **nonlinearBH** = TRUE, the table data specify the following:

            - Magntitude of the magnetic flux density vector in the first direction.
            - Magnitude of the magnetic field vector in the second direction.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = ANISOTROPIC, the table data specify the following:

            - :math:`\mu_{11}^{E}`.
            - :math:`\mu_{12}^{E}`.
            - :math:`\mu_{22}^{E}`.
            - :math:`\mu_{13}^{E}`.
            - :math:`\mu_{23}^{E}`.
            - :math:`\mu_{33}^{E}`.
            - Frequency, if the data depend on frequency.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - MAGNETIC PERMEABILITY
    """

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        table2: tuple,
        table3: tuple,
        type: Literal[C.ANISOTROPIC, C.ISOTROPIC, C.ORTHOTROPIC] = ISOTROPIC,
        frequencyDependency: Boolean = OFF,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        nonlinearBH: Boolean = OFF,
    ):
        """This method creates a MagneticPermeability object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].MagneticPermeability
                session.odbs[name].materials[name].MagneticPermeability

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below in “Table data.”
            If **type** = ORTHOTROPIC and nonlinearBH=ON, the data specified in the **table** is for the
            first direction and **table2** and **table3** must be specified.
        table2
            A sequence of sequences of Floats specifying the items described below in “Table data”
            in the second direction. **table2** must be specified only if **type** = ORTHOTROPIC and
            nonlinearBH=ON.
        table3
            A sequence of sequences of Floats specifying the items described below in “Table data”
            in the third direction. **table3** must be specified only if **type** = ORTHOTROPIC and
            nonlinearBH=ON.
        type
            A SymbolicConstant specifying the type of magnetic permeability. Possible values are
            ISOTROPIC, ORTHOTROPIC, and ANISOTROPIC. The default value is ISOTROPIC.
        frequencyDependency
            A Boolean specifying whether the data depend on frequency. The default value is OFF.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        nonlinearBH
            A Boolean specifying whether the magnetic behavior is nonlinear and available in tabular
            form of magnetic flux density versus magnetic field values. The default value is OFF.

        Returns
        -------
        MagneticPermeability
            A :py:class:`~abaqus.Material.Others.Electromagnetic.MagneticPermeability.MagneticPermeability` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the MagneticPermeability object.

        Raises
        ------
        RangeError
        """
        ...
