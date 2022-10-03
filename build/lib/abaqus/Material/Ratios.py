from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class Ratios:
    """The Ratios object specifies ratios that define anisotropic swelling.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].moistureSwelling.ratios
            mdb.models[name].materials[name].swelling.ratios
            import odbMaterial
            session.odbs[name].materials[name].moistureSwelling.ratios
            session.odbs[name].materials[name].swelling.ratios

        The table data for this object are:
            
        - r11.
        - r22.
        - r33.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - RATIOS
    """

    #: A sequence of sequences of Floats specifying the items described below.
    table: tuple

    #: A Boolean specifying whether the data depend on temperature. The default value is OFF.
    temperatureDependency: Boolean = OFF

    #: An Int specifying the number of field variable dependencies. The default value is 0.
    dependencies: int = 0

    @abaqus_method_doc
    def __init__(
        self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0
    ):
        """This method creates a Ratios object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].moistureSwelling.Ratios
                mdb.models[name].materials[name].swelling.Ratios
                session.odbs[name].materials[name].moistureSwelling.Ratios
                session.odbs[name].materials[name].swelling.Ratios

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        Ratios
            A :py:class:`~abaqus.Material.Ratios.Ratios` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Ratios object.

        Raises
        ------
        RangeError
        """
        ...
