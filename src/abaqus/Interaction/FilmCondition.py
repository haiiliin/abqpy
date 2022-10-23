from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Interaction import Interaction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import SymbolicConstant, UNIFORM
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class FilmCondition(Interaction):
    """The FilmCondition object defines film coefficients and associated sink temperatures for
    coupled temperature-displacement analyses.
    The FilmCondition object is derived from the Interaction object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name]
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the step in which the FilmCondition object is created.
    createStepName: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the name of the surface to which the film condition
    #: interaction is applied.
    surface: Region

    #: A SymbolicConstant specifying how the film condition is defined. Possible values are
    #: EMBEDDED_COEFF, PROPERTY_REF, USER_SUB, and FIELD.
    definition: SymbolicConstant

    #: A String specifying the name of the FilmConditionProp object associated with this
    #: interaction. The **interactionProperty** argument applies only when
    #: **definition** = PROPERTY_REF. The default value is an empty string.
    interactionProperty: str = ""

    #: A Float specifying the reference sink temperature, θ0θ0. The default value is 0.0.
    sinkTemperature: float = 0

    #: A String specifying the name of the Amplitude object that gives the variation of the
    #: sink temperature, θ0θ0, with time. The default value is an empty string.Note:Use empty
    #: string in an Abaqus/Standard analysis to specify that the reference sink temperature is
    #: applied immediately at the beginning of the step or linearly over the step. Use empty
    #: string in an Abaqus/Explicit analysis to specify that the reference sink temperature is
    #: applied throughout the step.
    sinkAmplitude: str = ""

    #: A Float specifying the reference film coefficient value, hh. The **filmCoeff** argument
    #: applies when **definition** = EMBEDDED_COEFF, **definition** = USER_SUB, or **definition** = FIELD.
    #: The default value is 0.0.
    filmCoeff: float = 0

    #: A String specifying the name of the Amplitude object that gives the variation of the
    #: film coefficient, hh, with time. The default value is an empty string. Note: Use empty
    #: string in an Abaqus/Standard analysis to specify that the reference film coefficient is
    #: applied immediately at the beginning of the step or linearly over the step. Use empty
    #: string in an Abaqus/Explicit analysis to specify that the reference film coefficient is
    #: applied throughout the step.
    filmCoeffAmplitude: str = ""

    #: A String specifying the name of the AnalyticalField object associated with this
    #: interaction. The **field** argument applies only when **definition** = FIELD. The default
    #: value is an empty string.
    field: str = ""

    #: A String specifying the name of the AnalyticalField or DiscreteField object associated
    #: with the sink temperature. The **sinkFieldName** argument applies only when
    #: **sinkDistributionType** = ANALYTICAL_FIELD or **sinkDistributionType** = DISCRETE_FIELD. The
    #: default value is an empty string.
    sinkFieldName: str = ""

    #: A SymbolicConstant specifying how the sink temperature is distributed. Possible values
    #: are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM.
    sinkDistributionType: SymbolicConstant = UNIFORM

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        surface: Region,
        definition: Literal[C.EMBEDDED_COEFF, C.FIELD, C.USER_SUB, C.PROPERTY_REF],
        interactionProperty: str = "",
        sinkTemperature: float = 0,
        sinkAmplitude: str = "",
        filmCoeff: float = 0,
        filmCoeffAmplitude: str = "",
        field: str = "",
        sinkFieldName: str = "",
        sinkDistributionType: Literal[C.DISCRETE_FIELD, C.UNIFORM, C.ANALYTICAL_FIELD] = UNIFORM,
    ):
        """This method creates a FilmCondition object.

        .. note::
            This function can be accessed by::

                mdb.models[name].FilmCondition

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the FilmCondition object is created.
        surface
            A :py:class:`~abaqus.Region.Region.Region` object specifying the name of the surface to which the film condition
            interaction is applied.
        definition
            A SymbolicConstant specifying how the film condition is defined. Possible values are
            EMBEDDED_COEFF, PROPERTY_REF, USER_SUB, and FIELD.
        interactionProperty
            A String specifying the name of the FilmConditionProp object associated with this
            interaction. The **interactionProperty** argument applies only when
            **definition** = PROPERTY_REF. The default value is an empty string.
        sinkTemperature
            A Float specifying the reference sink temperature, θ0θ0. The default value is 0.0.
        sinkAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the
            sink temperature, θ0θ0, with time. The default value is an empty string.Note:Use empty
            string in an Abaqus/Standard analysis to specify that the reference sink temperature is
            applied immediately at the beginning of the step or linearly over the step. Use empty
            string in an Abaqus/Explicit analysis to specify that the reference sink temperature is
            applied throughout the step.
        filmCoeff
            A Float specifying the reference film coefficient value, hh. The **filmCoeff** argument
            applies when **definition** = EMBEDDED_COEFF, **definition** = USER_SUB, or **definition** = FIELD.
            The default value is 0.0.
        filmCoeffAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the
            film coefficient, hh, with time. The default value is an empty string. Note: Use empty
            string in an Abaqus/Standard analysis to specify that the reference film coefficient is
            applied immediately at the beginning of the step or linearly over the step. Use empty
            string in an Abaqus/Explicit analysis to specify that the reference film coefficient is
            applied throughout the step.
        field
            A String specifying the name of the AnalyticalField object associated with this
            interaction. The **field** argument applies only when **definition** = FIELD. The default
            value is an empty string.
        sinkFieldName
            A String specifying the name of the AnalyticalField or DiscreteField object associated
            with the sink temperature. The **sinkFieldName** argument applies only when
            **sinkDistributionType** = ANALYTICAL_FIELD or **sinkDistributionType** = DISCRETE_FIELD. The
            default value is an empty string.
        sinkDistributionType
            A SymbolicConstant specifying how the sink temperature is distributed. Possible values
            are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM.

        Returns
        -------
        FilmCondition
            A :py:class:`~abaqus.Interaction.FilmCondition.FilmCondition` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        interactionProperty: str = "",
        sinkTemperature: float = 0,
        sinkAmplitude: str = "",
        filmCoeff: float = 0,
        filmCoeffAmplitude: str = "",
        field: str = "",
        sinkFieldName: str = "",
        sinkDistributionType: Literal[C.DISCRETE_FIELD, C.UNIFORM, C.ANALYTICAL_FIELD] = UNIFORM,
    ):
        """This method modifies the data for an existing FilmCondition object in the step where it
        is created.

        Parameters
        ----------
        interactionProperty
            A String specifying the name of the FilmConditionProp object associated with this
            interaction. The **interactionProperty** argument applies only when
            **definition** = PROPERTY_REF. The default value is an empty string.
        sinkTemperature
            A Float specifying the reference sink temperature, θ0θ0. The default value is 0.0.
        sinkAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the
            sink temperature, θ0θ0, with time. The default value is an empty string.Note:Use empty
            string in an Abaqus/Standard analysis to specify that the reference sink temperature is
            applied immediately at the beginning of the step or linearly over the step. Use empty
            string in an Abaqus/Explicit analysis to specify that the reference sink temperature is
            applied throughout the step.
        filmCoeff
            A Float specifying the reference film coefficient value, hh. The **filmCoeff** argument
            applies when **definition** = EMBEDDED_COEFF, **definition** = USER_SUB, or **definition** = FIELD.
            The default value is 0.0.
        filmCoeffAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the
            film coefficient, hh, with time. The default value is an empty string. Note: Use empty
            string in an Abaqus/Standard analysis to specify that the reference film coefficient is
            applied immediately at the beginning of the step or linearly over the step. Use empty
            string in an Abaqus/Explicit analysis to specify that the reference film coefficient is
            applied throughout the step.
        field
            A String specifying the name of the AnalyticalField object associated with this
            interaction. The **field** argument applies only when **definition** = FIELD. The default
            value is an empty string.
        sinkFieldName
            A String specifying the name of the AnalyticalField or DiscreteField object associated
            with the sink temperature. The **sinkFieldName** argument applies only when
            **sinkDistributionType** = ANALYTICAL_FIELD or **sinkDistributionType** = DISCRETE_FIELD. The
            default value is an empty string.
        sinkDistributionType
            A SymbolicConstant specifying how the sink temperature is distributed. Possible values
            are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(self, stepName: str):
        """This method modifies the propagating data of an existing FilmCondition object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified.
        """
        ...
