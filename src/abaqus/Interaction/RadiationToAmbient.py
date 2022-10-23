from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Interaction import Interaction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import AMBIENT, SymbolicConstant, UNIFORM
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class RadiationToAmbient(Interaction):
    """The RadiationToAmbient object defines radiant heat transfer between a surface and its
    environment.
    The RadiationToAmbient object is derived from the Interaction object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name]
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the step in which the RadiationToAmbient object is
    #: created.
    createStepName: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the surface to which the radiation interaction is applied.
    surface: Region

    #: A Float specifying the emissivity, ϵϵ.
    emissivity: float

    #: A String specifying the name of the AnalyticalField object associated with this
    #: interaction. The **field** argument applies only when **distributionType** = ANALYTICAL_FIELD.
    #: The default value is an empty string.
    field: str = ""

    #: A SymbolicConstant specifying how the radiation is distributed. This argument applies
    #: only when **radiationType** = AMBIENT. Possible values are UNIFORM and ANALYTICAL_FIELD. The
    #: default value is UNIFORM.
    distributionType: SymbolicConstant = UNIFORM

    #: A SymbolicConstant specifying whether to use the default surface radiation behavior, or
    #: the cavity radiation approximation. Possible values are AMBIENT and CAVITY. The default
    #: value is AMBIENT.
    radiationType: SymbolicConstant = AMBIENT

    #: A Float specifying the reference ambient temperature, θ0θ0. This argument applies only
    #: when **radiationType** = AMBIENT. The default value is 0.0.
    ambientTemperature: float = 0

    #: A String specifying the name of the Amplitude object that gives the variation of the
    #: ambient temperature with time.Note:Use None in an Abaqus/Standard analysis to specify
    #: that the reference ambient temperature is applied immediately at the beginning of the
    #: step or linearly over the step. Use None in an Abaqus/Explicit analysis to specify that
    #: the reference ambient temperature is applied throughout the step. This argument applies
    #: only when **radiationType** = AMBIENT.
    ambientTemperatureAmp: str = ""

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        surface: Region,
        emissivity: float,
        field: str = "",
        distributionType: Literal[C.AMBIENT, C.UNIFORM, C.ANALYTICAL_FIELD] = UNIFORM,
        radiationType: Literal[C.AMBIENT, C.CAVITY] = AMBIENT,
        ambientTemperature: float = 0,
        ambientTemperatureAmp: str = "",
    ):
        """This method creates a RadiationToAmbient object.

        .. note::
            This function can be accessed by::

                mdb.models[name].RadiationToAmbient

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the RadiationToAmbient object is
            created.
        surface
            A :py:class:`~abaqus.Region.Region.Region` object specifying the surface to which the radiation interaction is applied.
        emissivity
            A Float specifying the emissivity, ϵϵ.
        field
            A String specifying the name of the AnalyticalField object associated with this
            interaction. The **field** argument applies only when **distributionType** = ANALYTICAL_FIELD.
            The default value is an empty string.
        distributionType
            A SymbolicConstant specifying how the radiation is distributed. This argument applies
            only when **radiationType** = AMBIENT. Possible values are UNIFORM and ANALYTICAL_FIELD. The
            default value is UNIFORM.
        radiationType
            A SymbolicConstant specifying whether to use the default surface radiation behavior, or
            the cavity radiation approximation. Possible values are AMBIENT and CAVITY. The default
            value is AMBIENT.
        ambientTemperature
            A Float specifying the reference ambient temperature, θ0θ0. This argument applies only
            when **radiationType** = AMBIENT. The default value is 0.0.
        ambientTemperatureAmp
            A String specifying the name of the Amplitude object that gives the variation of the
            ambient temperature with time.Note:Use None in an Abaqus/Standard analysis to specify
            that the reference ambient temperature is applied immediately at the beginning of the
            step or linearly over the step. Use None in an Abaqus/Explicit analysis to specify that
            the reference ambient temperature is applied throughout the step. This argument applies
            only when **radiationType** = AMBIENT.

        Returns
        -------
        RadiationToAmbient
            A :py:class:`~abaqus.Interaction.RadiationToAmbient.RadiationToAmbient` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        field: str = "",
        distributionType: Literal[C.AMBIENT, C.UNIFORM, C.ANALYTICAL_FIELD] = UNIFORM,
        radiationType: Literal[C.AMBIENT, C.CAVITY] = AMBIENT,
        ambientTemperature: float = 0,
        ambientTemperatureAmp: str = "",
    ):
        """This method modifies the data for an existing RadiationToAmbient object in the step
        where it is created.

        Parameters
        ----------
        field
            A String specifying the name of the AnalyticalField object associated with this
            interaction. The **field** argument applies only when **distributionType** = ANALYTICAL_FIELD.
            The default value is an empty string.
        distributionType
            A SymbolicConstant specifying how the radiation is distributed. This argument applies
            only when **radiationType** = AMBIENT. Possible values are UNIFORM and ANALYTICAL_FIELD. The
            default value is UNIFORM.
        radiationType
            A SymbolicConstant specifying whether to use the default surface radiation behavior, or
            the cavity radiation approximation. Possible values are AMBIENT and CAVITY. The default
            value is AMBIENT.
        ambientTemperature
            A Float specifying the reference ambient temperature, θ0θ0. This argument applies only
            when **radiationType** = AMBIENT. The default value is 0.0.
        ambientTemperatureAmp
            A String specifying the name of the Amplitude object that gives the variation of the
            ambient temperature with time.Note:Use None in an Abaqus/Standard analysis to specify
            that the reference ambient temperature is applied immediately at the beginning of the
            step or linearly over the step. Use None in an Abaqus/Explicit analysis to specify that
            the reference ambient temperature is applied throughout the step. This argument applies
            only when **radiationType** = AMBIENT.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(self, stepName: str):
        """This method modifies the propagating data of an existing RadiationToAmbient object in
        the specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified.
        """
        ...
