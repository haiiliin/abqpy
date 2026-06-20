from __future__ import annotations

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import (
    OFF,
    ON,
    SOLID,
    TABULAR,
    Boolean,
    SymbolicConstant,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class GapElectricalConductance:
    """The GapElectricalConductance object specifies electrical conductance for a contact interaction property.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactionProperties[name].electricalConductance

        The table data for this object are:

        The **clearanceDepTable** data specify the following:

        - Conductivity.
        - Clearance.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The **pressureDepTable** data specify the following:

        - Conductivity.
        - Pressure.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - GAP ELECTRICAL CONDUCTANCE
    """

    #: A SymbolicConstant specifying how the electrical conductance is defined. Possible values
    #: are TABULAR and USER_DEFINED. The default value is TABULAR.
    definition: SymbolicConstant = TABULAR

    #: A Boolean specifying whether to use clearance-dependent data. The default value is ON.
    clearanceDependency: Boolean = ON

    #: A Boolean specifying whether to use pressure-dependent data. The default value is OFF.
    pressureDependency: Boolean = OFF

    #: A Boolean specifying whether to use temperature-dependent data with clearance
    #: dependency. The default value is OFF.
    temperatureDependencyC: Boolean = OFF

    #: An Int specifying the number of field variables to use with clearance dependency. The
    #: default value is 0.
    dependenciesC: int = 0

    #: A sequence of sequences of Floats specifying clearance dependency data. The items in the
    #: table data are described below.
    clearanceDepTable: tuple[tuple[float, ...], ...] = ()

    #: A Boolean specifying whether to use temperature-dependent data with pressure dependency.
    #: The default value is OFF.
    temperatureDependencyP: Boolean = OFF

    #: An Int specifying the number of field variables to use with pressure dependency. The
    #: default value is 0.
    dependenciesP: int = 0

    #: A sequence of sequences of Floats specifying pressure dependency data. The items in the
    #: table data are described below.
    pressureDepTable: tuple[tuple[float, ...], ...] = ()

    @abaqus_method_doc
    def __init__(
        self,
        definition: Literal[C.USER_DEFINED, C.TABULAR] = TABULAR,
        Type: Literal[C.SOLID, C.LIQUID] = SOLID,
        clearanceDependency: Boolean = ON,
        pressureDependency: Boolean = OFF,
        temperatureDependencyC: Boolean = OFF,
        ionConcentrationDependencyC: Boolean = OFF,
        dependenciesC: int = 0,
        clearanceDepTable: tuple = (),
        temperatureDependencyP: Boolean = OFF,
        ionConcentrationDependencyP: Boolean = OFF,
        dependenciesP: int = 0,
        pressureDepTable: tuple = (),
    ):
        """This method creates a GapElectricalConductance object.

        .. note::
            This function can be accessed by::

                mdb.models[name].interactionProperties[name].GapElectricalConductance

        Parameters
        ----------
        definition
            A SymbolicConstant specifying how the electrical conductance is defined. Possible values
            are TABULAR and USER_DEFINED. The default value is TABULAR.
        Type
            A SymbolicConstant specifying the Type of material. Possible values are SOLID and LIQUID. The default value is SOLID.

            .. versionadded:: 2025

                The ``Type`` argument was added.
        clearanceDependency
            A Boolean specifying whether to use clearance-dependent data. The default value is ON.
        pressureDependency
            A Boolean specifying whether to use pressure-dependent data. The default value is OFF.
        temperatureDependencyC
            A Boolean specifying whether to use temperature-dependent data with clearance
            dependency. The default value is OFF.
        ionConcentrationDependencyC
            A Boolean specifying whether to use ion-concentration-dependent data with clearance dependency. The default value is OFF.

            .. versionadded:: 2025

                The ``ionConcentrationDependencyC`` argument was added.
        dependenciesC
            An Int specifying the number of field variables to use with clearance dependency. The
            default value is 0.
        clearanceDepTable
            A sequence of sequences of Floats specifying clearance dependency data. The items in the
            table data are described below.
        temperatureDependencyP
            A Boolean specifying whether to use temperature-dependent data with pressure dependency.
            The default value is OFF.
        ionConcentrationDependencyP
            A Boolean specifying whether to use ion-concentration–dependent data with pressure dependency. The default value is OFF.

            .. versionadded:: 2025

                The ``ionConcentrationDependencyP`` argument was added.
        dependenciesP
            An Int specifying the number of field variables to use with pressure dependency. The
            default value is 0.
        pressureDepTable
            A sequence of sequences of Floats specifying pressure dependency data. The items in the
            table data are described below.

        Returns
        -------
        GapElectricalConductance
            A GapElectricalConductance object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the GapElectricalConductance object."""
        ...
