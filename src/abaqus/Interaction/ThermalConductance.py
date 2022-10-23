from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ..UtilityAndView.abaqusConstants import Boolean, OFF, ON, SymbolicConstant, TABULAR
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class ThermalConductance:
    """The ThermalConductance object specifies thermal conductance for a contact interaction
    property.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactionProperties[name].thermalConductance

        The table data for this object are:

        The **clearanceDepTable** data specify the following:

        - Conductivity.
        - Clearance.
        - Temperature, if the data depend on temperature.
        - Mass flow rate, if the data depend on mass flow rate.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The **pressureDepTable** data specify the following:

        - Conductivity.
        - Pressure.
        - Temperature, if the data depend on temperature.
        - Mass flow rate, if the data depend on mass flow rate.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - GAP CONDUCTANCE
    """

    #: A SymbolicConstant specifying how the thermal conductance is defined. Possible values
    #: are TABULAR and USER_DEFINED. The default value is TABULAR.
    definition: SymbolicConstant = TABULAR

    #: A Boolean specifying whether to use clearance-dependent data. The default value is ON.
    clearanceDependency: Boolean = ON

    #: A Boolean specifying whether to use pressure-dependent data. The default value is OFF.
    pressureDependency: Boolean = OFF

    #: A Boolean specifying whether to use temperature-dependent data with clearance
    #: dependency. The default value is OFF.
    temperatureDependencyC: Boolean = OFF

    #: A Boolean specifying whether to use mass-flow-rate-dependent data with clearance
    #: dependency. The default value is OFF.
    massFlowRateDependencyC: Boolean = OFF

    #: An Int specifying the number of field variables to use with clearance dependency. The
    #: default value is 0.
    dependenciesC: int = 0

    #: A sequence of sequences of Floats specifying clearance dependency data. The items in the
    #: table data are described below.
    clearanceDepTable: tuple = ()

    #: A Boolean specifying whether to use temperature-dependent data with pressure dependency.
    #: The default value is OFF.
    temperatureDependencyP: Boolean = OFF

    #: A Boolean specifying whether to use mass-flow-rate-dependent data with pressure
    #: dependency. The default value is OFF.
    massFlowRateDependencyP: Boolean = OFF

    #: An Int specifying the number of field variables to use with pressure dependency. The
    #: default value is 0.
    dependenciesP: int = 0

    #: A sequence of sequences of Floats specifying pressure dependency data. The items in the
    #: table data are described below.
    pressureDepTable: tuple = ()

    @abaqus_method_doc
    def __init__(
        self,
        definition: Literal[C.USER_DEFINED, C.TABULAR] = TABULAR,
        clearanceDependency: Boolean = ON,
        pressureDependency: Boolean = OFF,
        temperatureDependencyC: Boolean = OFF,
        massFlowRateDependencyC: Boolean = OFF,
        dependenciesC: int = 0,
        clearanceDepTable: tuple = (),
        temperatureDependencyP: Boolean = OFF,
        massFlowRateDependencyP: Boolean = OFF,
        dependenciesP: int = 0,
        pressureDepTable: tuple = (),
    ):
        """This method creates a ThermalConductance object.

        .. note::
            This function can be accessed by::

                mdb.models[name].interactionProperties[name].ThermalConductance

        Parameters
        ----------
        definition
            A SymbolicConstant specifying how the thermal conductance is defined. Possible values
            are TABULAR and USER_DEFINED. The default value is TABULAR.
        clearanceDependency
            A Boolean specifying whether to use clearance-dependent data. The default value is ON.
        pressureDependency
            A Boolean specifying whether to use pressure-dependent data. The default value is OFF.
        temperatureDependencyC
            A Boolean specifying whether to use temperature-dependent data with clearance
            dependency. The default value is OFF.
        massFlowRateDependencyC
            A Boolean specifying whether to use mass-flow-rate-dependent data with clearance
            dependency. The default value is OFF.
        dependenciesC
            An Int specifying the number of field variables to use with clearance dependency. The
            default value is 0.
        clearanceDepTable
            A sequence of sequences of Floats specifying clearance dependency data. The items in the
            table data are described below.
        temperatureDependencyP
            A Boolean specifying whether to use temperature-dependent data with pressure dependency.
            The default value is OFF.
        massFlowRateDependencyP
            A Boolean specifying whether to use mass-flow-rate-dependent data with pressure
            dependency. The default value is OFF.
        dependenciesP
            An Int specifying the number of field variables to use with pressure dependency. The
            default value is 0.
        pressureDepTable
            A sequence of sequences of Floats specifying pressure dependency data. The items in the
            table data are described below.

        Returns
        -------
        ThermalConductance
            A :py:class:`~abaqus.Interaction.ThermalConductance.ThermalConductance` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the ThermalConductance object."""
        ...
