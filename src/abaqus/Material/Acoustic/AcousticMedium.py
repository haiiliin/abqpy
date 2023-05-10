from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ...UtilityAndView.abaqusConstants import OFF, Boolean


@abaqus_class_doc
class AcousticMedium:
    """The AcousticMedium object specifies the acoustic properties of a material.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].acousticMedium
            import odbMaterial
            session.odbs[name].materials[name].acousticMedium

        The corresponding analysis keywords are:

        - ACOUSTIC MEDIUM
    """

    @abaqus_method_doc
    def __init__(
        self,
        acousticVolumetricDrag: Boolean = OFF,
        temperatureDependencyB: Boolean = OFF,
        temperatureDependencyV: Boolean = OFF,
        dependenciesB: int = 0,
        dependenciesV: int = 0,
        bulkTable: tuple = (),
        volumetricTable: tuple = (),
    ):
        """This method creates an AcousticMedium object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].AcousticMedium
                session.odbs[name].materials[name].AcousticMedium

        Parameters
        ----------
        acousticVolumetricDrag
            A Boolean specifying whether the volumetricTable data is specified. The default value is
            OFF.
        temperatureDependencyB
            A Boolean specifying whether the data in **bulkTable** depend on temperature. The default
            value is OFF.
        temperatureDependencyV
            A Boolean specifying whether the data in **volumetricTable** depend on temperature. The
            default value is OFF.
        dependenciesB
            An Int specifying the number of field variable dependencies for the data in **bulkTable**.
            The default value is 0.
        dependenciesV
            An Int specifying the number of field variable dependencies for the data in
            **volumetricTable**. The default value is 0.
        bulkTable
            A sequence of sequences of Floats specifying the following:

            - Bulk modulus.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        volumetricTable
            A sequence of sequences of Floats specifying the following:

            - Volumetric drag.
            - Frequency.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

            The default value is an empty sequence.

        Returns
        -------
        AcousticMedium
            An AcousticMedium object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the AcousticMedium object.

        Raises
        ------
        RangeError
        """
        ...
