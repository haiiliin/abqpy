from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ContactProperty import ContactProperty


@abaqus_class_doc
class FluidInflatorProperty(ContactProperty):
    """The FluidInflatorProperty object is an interaction property that defines a fluid
    inflator property to model the deployment of an airbag. The inflator property defines
    the mass flow rate and temperature as a function of inflation time either directly or by
    entering tank test data. It also defines the mixture of gases entering the fluid cavity.
    The FluidInflatorProperty object is derived from the InteractionProperty object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactionProperties[name]

        The table data for this object are:

        - If **definition** = DUAL PRESSURE, the table data specify the following:

            - Inflation time.
            - Inflator pressure.
            - Tank pressure.

        - If **definition** = PRESSURE AND MASS, the table data specify the following:

            - Inflation time.
            - Inflator pressure.
            - Inflator mass flow rate.

        - If **definition** = TANK TEST, the table data specify the following:

            - Inflation time.
            - Inflator gas temperature.
            - Tank pressure.

        - If **definition** = TEMPERATURE AND MASS, the table data specify the following:

            - Inflation time.
            - Inflator gas temperature.
            - Inflator mass flow rate.

        The corresponding analysis keywords are:

        - FLUID INFLATOR PROPERTY

    .. versionadded:: 2019
        The `FluidInflatorProperty` class was added.
    """

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        definition: str,
        effectiveArea: float,
        tankVolume: float,
        dischargeCoefficient: float = None,
        dataTable: tuple = (),
        numFluids: int = None,
        mixtureType: str = "",
        inflationTime: tuple = (),
        fluidbehaviorName: tuple = (),
        massFraction: tuple = (),
    ):
        """This method creates a FluidInflatorProperty object.

        .. note::
            This function can be accessed by::

                mdb.models[name].FluidInflatorProperty

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.
        definition
            A Symbolic constant specifying the method used for modeling the flow characteristics of
            inflators. The default value is **definition** = DUAL PRESSURE. The possible values are DUAL
            PRESSURE, PRESSURE AND MASS, TANK TEST, and TEMPERATURE AND MASS.
        effectiveArea
            A Float specifying the total inflator orifice area. This argument is applicable only if
            **definition** = DUAL PRESSURE or **definition** = PRESSURE AND MASS.
        tankVolume
            A Float specifying the tank volume. This argument is applicable only if
            **definition** = DUAL PRESSURE or **definition** = TANK TEST.
        dischargeCoefficient
            A Float specifying the discharge coefficient. This argument is applicable only if
            **definition** = DUAL PRESSURE or **definition** = PRESSURE AND MASS.
        dataTable
            A sequence of sequences of Floats specifying the items described in the "Table data"
            section below.
        numFluids
            An Int specifying the number of gas species used for this inflator.
        mixtureType
            A Symbolic constant specifying whether to use mass fraction or the molar fraction for a
            mixture of ideal gases. The default value is MASS FRACTION. The possible values are MASS
            FRACTION or MOLAR FRACTION.
        inflationTime
            A sequence of sequences of Floats specifying the inflation time.
        fluidbehaviorName
            A sequence of sequences of Strings specifying fluid behavior names.
        massFraction
            A sequence of sequences of Floats specifying the mass fraction or the molar fraction
            corresponding to entered fluid behavior.

        Returns
        -------
            A FluidInflatorProperty object.
        """
        super().__init__(name)

    @abaqus_method_doc
    def setValues(
        self,
        dischargeCoefficient: float = None,
        dataTable: tuple = (),
        numFluids: int = None,
        mixtureType: str = "",
        inflationTime: tuple = (),
        fluidbehaviorName: tuple = (),
        massFraction: tuple = (),
    ):
        """This method modifies the FluidInflatorProperty object.

        Parameters
        ----------
        dischargeCoefficient
            A Float specifying the discharge coefficient. This argument is applicable only if
            **definition** = DUAL PRESSURE or **definition** = PRESSURE AND MASS.
        dataTable
            A sequence of sequences of Floats specifying the items described in the "Table data"
            section below.
        numFluids
            An Int specifying the number of gas species used for this inflator.
        mixtureType
            A Symbolic constant specifying whether to use mass fraction or the molar fraction for a
            mixture of ideal gases. The default value is MASS FRACTION. The possible values are MASS
            FRACTION or MOLAR FRACTION.
        inflationTime
            A sequence of sequences of Floats specifying the inflation time.
        fluidbehaviorName
            A sequence of sequences of Strings specifying fluid behavior names.
        massFraction
            A sequence of sequences of Floats specifying the mass fraction or the molar fraction
            corresponding to entered fluid behavior.
        """
        ...
