from abaqusConstants import *
from .Interaction import Interaction
from ..Region.Region import Region


class RadiationToAmbient(Interaction):
    """The RadiationToAmbient object defines radiant heat transfer between a surface and its
    environment.
    The RadiationToAmbient object is derived from the Interaction object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].interactions[name]
    """

    def __init__(
        self,
        name: str,
        createStepName: str,
        surface: Region,
        emissivity: float,
        field: str = "",
        distributionType: SymbolicConstant = UNIFORM,
        radiationType: SymbolicConstant = AMBIENT,
        ambientTemperature: float = 0,
        ambientTemperatureAmp: str = "",
    ):
        """This method creates a RadiationToAmbient object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].RadiationToAmbient

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the RadiationToAmbient object is
            created.
        surface
            A Region object specifying the surface to which the radiation interaction is applied.
        emissivity
            A Float specifying the emissivity, ϵϵ.
        field
            A String specifying the name of the AnalyticalField object associated with this
            interaction. The **field** argument applies only when **distributionType**=ANALYTICAL_FIELD.
            The default value is an empty string.
        distributionType
            A SymbolicConstant specifying how the radiation is distributed. This argument applies
            only when **radiationType**=AMBIENT. Possible values are UNIFORM and ANALYTICAL_FIELD. The
            default value is UNIFORM.
        radiationType
            A SymbolicConstant specifying whether to use the default surface radiation behavior, or
            the cavity radiation approximation. Possible values are AMBIENT and CAVITY. The default
            value is AMBIENT.
        ambientTemperature
            A Float specifying the reference ambient temperature, θ0θ0. This argument applies only
            when **radiationType**=AMBIENT. The default value is 0.0.
        ambientTemperatureAmp
            A String specifying the name of the Amplitude object that gives the variation of the
            ambient temperature with time.Note:Use None in an Abaqus/Standard analysis to specify
            that the reference ambient temperature is applied immediately at the beginning of the
            step or linearly over the step. Use None in an Abaqus/Explicit analysis to specify that
            the reference ambient temperature is applied throughout the step. This argument applies
            only when **radiationType**=AMBIENT.

        Returns
        -------
            A RadiationToAmbient object.
        """
        super().__init__()
        pass

    def setValues(
        self,
        field: str = "",
        distributionType: SymbolicConstant = UNIFORM,
        radiationType: SymbolicConstant = AMBIENT,
        ambientTemperature: float = 0,
        ambientTemperatureAmp: str = "",
    ):
        """This method modifies the data for an existing RadiationToAmbient object in the step
        where it is created.

        Parameters
        ----------
        field
            A String specifying the name of the AnalyticalField object associated with this
            interaction. The **field** argument applies only when **distributionType**=ANALYTICAL_FIELD.
            The default value is an empty string.
        distributionType
            A SymbolicConstant specifying how the radiation is distributed. This argument applies
            only when **radiationType**=AMBIENT. Possible values are UNIFORM and ANALYTICAL_FIELD. The
            default value is UNIFORM.
        radiationType
            A SymbolicConstant specifying whether to use the default surface radiation behavior, or
            the cavity radiation approximation. Possible values are AMBIENT and CAVITY. The default
            value is AMBIENT.
        ambientTemperature
            A Float specifying the reference ambient temperature, θ0θ0. This argument applies only
            when **radiationType**=AMBIENT. The default value is 0.0.
        ambientTemperatureAmp
            A String specifying the name of the Amplitude object that gives the variation of the
            ambient temperature with time.Note:Use None in an Abaqus/Standard analysis to specify
            that the reference ambient temperature is applied immediately at the beginning of the
            step or linearly over the step. Use None in an Abaqus/Explicit analysis to specify that
            the reference ambient temperature is applied throughout the step. This argument applies
            only when **radiationType**=AMBIENT.
        """
        pass

    def setValuesInStep(self, stepName: str):
        """This method modifies the propagating data of an existing RadiationToAmbient object in
        the specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified.
        """
        pass
