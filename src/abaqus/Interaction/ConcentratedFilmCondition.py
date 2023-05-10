from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import LAGRANGIAN, UNIFORM, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .Interaction import Interaction


@abaqus_class_doc
class ConcentratedFilmCondition(Interaction):
    """The ConcentratedFilmCondition object defines concentrated film coefficients and associated sink
    temperatures. The ConcentratedFilmCondition object is derived from the Interaction object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name]
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the step in which the ConcentratedFilmCondition object
    #: is created.
    createStepName: str

    #: A Region object specifying the region to which the concentrated film condition
    #: interaction is applied. The interaction is applied to each node in the region.
    region: Region

    #: A SymbolicConstant specifying how the concentrated film condition is defined. Possible
    #: values are EMBEDDED_COEFF, PROPERTY_REF, USER_SUB, and FIELD.
    definition: SymbolicConstant

    #: A Float specifying the area associated with the node where the concentrated film
    #: condition is applied. The default value is 1.0.
    nodalArea: float = 1

    #: A SymbolicConstant specifying how the concentrated film condition is applied to the
    #: boundary of an adaptive mesh domain. Possible values are LAGRANGIAN, SLIDING, and
    #: EULERIAN. The default value is LAGRANGIAN. This argument applies only during an
    #: Abaqus/Explicit analysis.
    explicitRegionType: SymbolicConstant = LAGRANGIAN

    #: A String specifying the name of the FilmConditionProp object associated with this
    #: interaction. The **interactionProperty** argument applies only when
    #: **definition** = PROPERTY_REF. The default value is an empty string.
    interactionProperty: str = ""

    #: A String specifying the name of the AnalyticalField object associated with this
    #: interaction. The **field** argument applies only when **definition** = FIELD. The default
    #: value is an empty string.
    field: str = ""

    #: A Float specifying the reference sink temperature, θ0θ0. The default value is 0.0.
    sinkTemperature: float = 0

    #: A String specifying the name of the Amplitude object that gives the variation of the
    #: sink temperature, θ0θ0, with time. The default value is an empty string. Note: Use None in
    #: an Abaqus/Standard analysis to specify that the reference sink temperature is applied
    #: immediately at the beginning of the step or linearly over the step. Use None in an
    #: Abaqus/Explicit analysis to specify that the reference sink temperature is applied
    #: throughout the step.
    sinkAmplitude: str = ""

    #: A Float specifying the reference film coefficient value, hh. The **filmCoeff** argument
    #: applies when **definition** = EMBEDDED_COEFF, **definition** = USER_SUB, or **definition** = FIELD.
    #: The default value is 0.0.
    filmCoeff: float = 0

    #: A String specifying the name of the Amplitude object that gives the variation of the
    #: film coefficient, hh, with time. The default value is an empty string. Note: Use None in
    #: an Abaqus/Standard analysis to specify that the reference film coefficient is applied
    #: immediately at the beginning of the step or linearly over the step. Use None in an
    #: Abaqus/Explicit analysis to specify that the reference film coefficient is applied
    #: throughout the step.
    filmCoeffAmplitude: str = ""

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
        region: Region,
        definition: Literal[C.EMBEDDED_COEFF, C.FIELD, C.USER_SUB, C.PROPERTY_REF],
        nodalArea: float = 1,
        explicitRegionType: Literal[C.LAGRANGIAN, C.SLIDING, C.EULERIAN] = LAGRANGIAN,
        interactionProperty: str = "",
        field: str = "",
        sinkTemperature: float = 0,
        sinkAmplitude: str = "",
        filmCoeff: float = 0,
        filmCoeffAmplitude: str = "",
        sinkFieldName: str = "",
        sinkDistributionType: Literal[C.DISCRETE_FIELD, C.UNIFORM, C.ANALYTICAL_FIELD] = UNIFORM,
    ):
        """This method creates a ConcentratedFilmCondition object.

        .. note::
            This function can be accessed by::

                mdb.models[name].ConcentratedFilmCondition

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the ConcentratedFilmCondition object
            is created.
        region
            A Region object specifying the region to which the concentrated film condition
            interaction is applied. The interaction is applied to each node in the region.
        definition
            A SymbolicConstant specifying how the concentrated film condition is defined. Possible
            values are EMBEDDED_COEFF, PROPERTY_REF, USER_SUB, and FIELD.
        nodalArea
            A Float specifying the area associated with the node where the concentrated film
            condition is applied. The default value is 1.0.
        explicitRegionType
            A SymbolicConstant specifying how the concentrated film condition is applied to the
            boundary of an adaptive mesh domain. Possible values are LAGRANGIAN, SLIDING, and
            EULERIAN. The default value is LAGRANGIAN. This argument applies only during an
            Abaqus/Explicit analysis.
        interactionProperty
            A String specifying the name of the FilmConditionProp object associated with this
            interaction. The **interactionProperty** argument applies only when
            **definition** = PROPERTY_REF. The default value is an empty string.
        field
            A String specifying the name of the AnalyticalField object associated with this
            interaction. The **field** argument applies only when **definition** = FIELD. The default
            value is an empty string.
        sinkTemperature
            A Float specifying the reference sink temperature, θ0θ0. The default value is 0.0.
        sinkAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the
            sink temperature, θ0θ0, with time. The default value is an empty string. Note: Use None in
            an Abaqus/Standard analysis to specify that the reference sink temperature is applied
            immediately at the beginning of the step or linearly over the step. Use None in an
            Abaqus/Explicit analysis to specify that the reference sink temperature is applied
            throughout the step.
        filmCoeff
            A Float specifying the reference film coefficient value, hh. The **filmCoeff** argument
            applies when **definition** = EMBEDDED_COEFF, **definition** = USER_SUB, or **definition** = FIELD.
            The default value is 0.0.
        filmCoeffAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the
            film coefficient, hh, with time. The default value is an empty string. Note: Use None in
            an Abaqus/Standard analysis to specify that the reference film coefficient is applied
            immediately at the beginning of the step or linearly over the step. Use None in an
            Abaqus/Explicit analysis to specify that the reference film coefficient is applied
            throughout the step.
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
        ConcentratedFilmCondition
            A ConcentratedFilmCondition object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        nodalArea: float = 1,
        explicitRegionType: Literal[C.LAGRANGIAN, C.SLIDING, C.EULERIAN] = LAGRANGIAN,
        interactionProperty: str = "",
        field: str = "",
        sinkTemperature: float = 0,
        sinkAmplitude: str = "",
        filmCoeff: float = 0,
        filmCoeffAmplitude: str = "",
        sinkFieldName: str = "",
        sinkDistributionType: Literal[C.DISCRETE_FIELD, C.UNIFORM, C.ANALYTICAL_FIELD] = UNIFORM,
    ):
        """This method modifies the data for an existing ConcentratedFilmCondition object in the step where it
        is created.

        Parameters
        ----------
        nodalArea
            A Float specifying the area associated with the node where the concentrated film
            condition is applied. The default value is 1.0.
        explicitRegionType
            A SymbolicConstant specifying how the concentrated film condition is applied to the
            boundary of an adaptive mesh domain. Possible values are LAGRANGIAN, SLIDING, and
            EULERIAN. The default value is LAGRANGIAN. This argument applies only during an
            Abaqus/Explicit analysis.
        interactionProperty
            A String specifying the name of the FilmConditionProp object associated with this
            interaction. The **interactionProperty** argument applies only when
            **definition** = PROPERTY_REF. The default value is an empty string.
        field
            A String specifying the name of the AnalyticalField object associated with this
            interaction. The **field** argument applies only when **definition** = FIELD. The default
            value is an empty string.
        sinkTemperature
            A Float specifying the reference sink temperature, θ0θ0. The default value is 0.0.
        sinkAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the
            sink temperature, θ0θ0, with time. The default value is an empty string. Note: Use None in
            an Abaqus/Standard analysis to specify that the reference sink temperature is applied
            immediately at the beginning of the step or linearly over the step. Use None in an
            Abaqus/Explicit analysis to specify that the reference sink temperature is applied
            throughout the step.
        filmCoeff
            A Float specifying the reference film coefficient value, hh. The **filmCoeff** argument
            applies when **definition** = EMBEDDED_COEFF, **definition** = USER_SUB, or **definition** = FIELD.
            The default value is 0.0.
        filmCoeffAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the
            film coefficient, hh, with time. The default value is an empty string. Note: Use None in
            an Abaqus/Standard analysis to specify that the reference film coefficient is applied
            immediately at the beginning of the step or linearly over the step. Use None in an
            Abaqus/Explicit analysis to specify that the reference film coefficient is applied
            throughout the step.
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
        """This method modifies the propagating data of an existing ConcentratedFilmCondition object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified.
        """
        ...
