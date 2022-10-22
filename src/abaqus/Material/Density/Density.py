from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ...UtilityAndView.abaqusConstants import Boolean, OFF, UNIFORM
from ...UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class Density:
    """The Density object specifies the material density.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].density
            import odbMaterial
            session.odbs[name].materials[name].density

        The table data for this object are:

        - The mass density.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - DENSITY
    """

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        distributionType: Literal[
            C.UNIFORM, C.ANALYTICAL_FIELD, C.DISCRETE_FIELD
        ] = UNIFORM,
        fieldName: str = "",
    ):
        """This method creates a Density object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].Density
                session.odbs[name].materials[name].Density

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        distributionType
            A SymbolicConstant specifying how the density is distributed spatially. Possible values
            are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM.
        fieldName
            A String specifying the name of the AnalyticalField or DiscreteField object associated
            with this material option. The **fieldName** argument applies only when
            **distributionType** = ANALYTICAL_FIELD or **distributionType** = DISCRETE_FIELD. The default
            value is an empty string.

        Returns
        -------
        Density
            A :py:class:`~abaqus.Material.Density.Density.Density` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Density object.

        Raises
        ------
        RangeError
        """
        ...
