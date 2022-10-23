from typing import Optional, Union

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .PredefinedField import PredefinedField
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import (CONSTANT_THROUGH_THICKNESS, OFF, SymbolicConstant,
                                              UNIFORM, UNSET, Boolean)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class Temperature(PredefinedField):
    """The Temperature object stores the data for temperature predefined fields.
    The Temperature object is derived from the PredefinedField object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].predefinedFields[name]

        The corresponding analysis keywords are:

        - INITIAL CONDITIONS
        - TEMPERATURE
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A SymbolicConstant specifying how the predefined field varies spatially. Possible values
    #: are UNIFORM, USER_DEFINED, FROM_FILE, FIELD, FROM_FILE_AND_USER_DEFINED, and
    #: DISCRETE_FIELD. The default value is UNIFORM.
    distributionType: SymbolicConstant = UNIFORM

    #: A String specifying the name of the AnalyticalField or DiscreteField object associated
    #: with this predefined field. The **field** argument applies only when
    #: **distributionType** = FIELD or **distributionType** = DISCRETE_FIELD. The default value is an
    #: empty string.
    field: str = ""

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the predefined field is applied. **Region**
    #: is ignored if the predefined field has an **instances** member available. **Region** is also
    #: ignored if the predefined field has a **distributionType** member available, and
    #: **distributionType** = FROM_FILE or FROM_FILE_AND_USER_DEFINED.
    region: Region = Region()

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        region: Region,
        distributionType: Literal[C.FIELD, C.FROM_FILE, C.DISCRETE_FIELD, C.FROM_FILE_AND_USER_DEFINED, C.UNIFORM, C.USER_DEFINED] = UNIFORM,
        crossSectionDistribution: Literal[C.GRADIENTS_THROUGH_BEAM_CS, C.POINTS_THROUGH_SECTION, C.GRADIENTS_THROUGH_SHELL_CS, C.CONSTANT_THROUGH_THICKNESS] = CONSTANT_THROUGH_THICKNESS,
        field: str = "",
        amplitude: str = UNSET,
        fileName: str = "",
        beginStep: Optional[Literal[C.FROM_FILE, C.LAST_STEP, C.FROM_FILE_AND_USER_DEFINED, C.FIRST_STEP]] = None,
        beginIncrement: Optional[Literal[C.FROM_FILE, C.FROM_FILE_AND_USER_DEFINED, C.STEP_END, C.STEP_START]] = None,
        endStep: Optional[Literal[C.FROM_FILE, C.LAST_STEP, C.FROM_FILE_AND_USER_DEFINED, C.FIRST_STEP]] = None,
        endIncrement: Optional[Literal[C.FROM_FILE, C.FROM_FILE_AND_USER_DEFINED, C.STEP_END, C.STEP_START]] = None,
        interpolate: Union[Literal[C.MIDSIDE_ONLY], Boolean] = OFF,
        magnitudes: str = "",
        absoluteExteriorTolerance: float = 0,
        exteriorTolerance: float = 0,
    ):
        """This method creates a Temperature object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].Temperature

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the predefined field is created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the predefined field is applied. **Region**
            is ignored if the predefined field has a **distributionType** member available, and
            **distributionType** = FROM_FILE .
        distributionType
            A SymbolicConstant specifying how the predefined field varies spatially. Possible values
            are UNIFORM, USER_DEFINED, FROM_FILE, FIELD, FROM_FILE_AND_USER_DEFINED, and
            DISCRETE_FIELD. The default value is UNIFORM.
        crossSectionDistribution
            A SymbolicConstant specifying how the predefined field is distributed over the cross
            section of the region. Possible values are
            
            - CONSTANT_THROUGH_THICKNESS
            - GRADIENTS_THROUGH_SHELL_CS
            - GRADIENTS_THROUGH_BEAM_CS
            - POINTS_THROUGH_SECTION
            
            The default value is CONSTANT_THROUGH_THICKNESS.
        field
            A String specifying the name of the AnalyticalField or DiscreteField object associated
            with this predefined field. The **field** argument applies only when
            **distributionType** = FIELD or **distributionType** = DISCRETE_FIELD. The default value is an
            empty string.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the predefined field has no amplitude reference. The default
            value is UNSET.Note:*amplitude* should be given only if it is valid for the specified
            step.
        fileName
            A String specifying the name of the file from which the temperature values are to be
            read when **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED.
        beginStep
            An Int specifying the first step from which temperature values are to be read or the
            SymbolicConstant FIRST_STEP or LAST_STEP. This argument is valid only when
            **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        beginIncrement
            An Int specifying the first increment of the step set in **beginStep** or the
            SymbolicConstants STEP_START or STEP_END. This argument is valid only when
            **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        endStep
            An Int specifying the last step from which temperature values are to be read or the
            SymbolicConstants FIRST_STEP and LAST_STEP. This argument is valid only when
            **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        endIncrement
            An Int specifying the last increment of the step set in **endStep** or the
            SymbolicConstants STEP_START and STEP_END. This argument is valid only when
            **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        interpolate
            A SymbolicConstant specifying whether to interpolate a field read from an output
            database or results file. Possible values are OFF, ON or MIDSIDE_ONLY. The default value
            is OFF.
        magnitudes
            A Sequence of Doubles specifying the temperature values when **distributionType** = UNIFORM
            or FIELD. The value of the **magnitudes** argument is a function of the
            **crossSectionDistribution** argument, as shown in the following list:
            
            - If **crossSectionDistribution** = CONSTANT_THROUGH_THICKNESS then **magnitudes** is a Double
              specifying the temperature.
            - If **crossSectionDistribution** = GRADIENTS_THROUGH_SHELL_CS then **magnitudes** is a
              sequence of Doubles specifying the mean value and the gradient in the thickness
            direction.
            - If **crossSectionDistribution** = GRADIENTS_THROUGH_BEAM_CS then **magnitudes** is a
              sequence of Doubles specifying the mean value, the gradient in the N1 direction, and the
              gradient in the N2 direction.
            - If **crossSectionDistribution** = POINTS_THROUGH_SECTION then **magnitudes** is a sequence
              of Doubles specifying the temperature at each point.
        absoluteExteriorTolerance
            A Float specifying the absolute value by which a driven node of the field can lie
            outside the region of the elements of the global model. The default value is 0.0. This
            argument cannot be used with **midside**.
        exteriorTolerance
            A Float specifying the fraction of the average element size in the global model by which
            a driven node of the field can lie outside the region of the elements of the global
            model. The default value is 0.0. This argument cannot be used with **midside**.

        Returns
        -------
        Temperature
            A :py:class:`~abaqus.PredefinedField.Temperature.Temperature` object.
        """
        super().__init__()

    @abaqus_method_doc
    def move(self, fromStepName: str, toStepName: str):
        """This method moves the TemperatureState object from one step to a different step.

        Parameters
        ----------
        fromStepName
            A String specifying the name of the step from which the PredefinedFieldState is moved.
        toStepName
            A String specifying the name of the step to which the PredefinedFieldState is moved.

        Raises
        ------
        TextError
        """
        ...

    @abaqus_method_doc
    def setValues(
        self,
        distributionType: Literal[C.FIELD, C.FROM_FILE, C.DISCRETE_FIELD, C.FROM_FILE_AND_USER_DEFINED, C.UNIFORM, C.USER_DEFINED] = UNIFORM,
        crossSectionDistribution: Literal[C.GRADIENTS_THROUGH_BEAM_CS, C.POINTS_THROUGH_SECTION, C.GRADIENTS_THROUGH_SHELL_CS, C.CONSTANT_THROUGH_THICKNESS] = CONSTANT_THROUGH_THICKNESS,
        field: str = "",
        amplitude: str = UNSET,
        fileName: str = "",
        beginStep: Optional[Literal[C.FROM_FILE, C.LAST_STEP, C.FROM_FILE_AND_USER_DEFINED, C.FIRST_STEP]] = None,
        beginIncrement: Optional[Literal[C.FROM_FILE, C.FROM_FILE_AND_USER_DEFINED, C.STEP_END, C.STEP_START]] = None,
        endStep: Optional[Literal[C.FROM_FILE, C.LAST_STEP, C.FROM_FILE_AND_USER_DEFINED, C.FIRST_STEP]] = None,
        endIncrement: Optional[Literal[C.FROM_FILE, C.FROM_FILE_AND_USER_DEFINED, C.STEP_END, C.STEP_START]] = None,
        interpolate: Union[Literal[C.MIDSIDE_ONLY], Boolean] = OFF,
        magnitudes: str = "",
        absoluteExteriorTolerance: float = 0,
        exteriorTolerance: float = 0,
    ):
        """This method modifies the data for an existing Temperature object in the step where it is
        created.

        Parameters
        ----------
        distributionType
            A SymbolicConstant specifying how the predefined field varies spatially. Possible values
            are UNIFORM, USER_DEFINED, FROM_FILE, FIELD, FROM_FILE_AND_USER_DEFINED, and
            DISCRETE_FIELD. The default value is UNIFORM.
        crossSectionDistribution
            A SymbolicConstant specifying how the predefined field is distributed over the cross
            section of the region. Possible values are
            
            - CONSTANT_THROUGH_THICKNESS
            - GRADIENTS_THROUGH_SHELL_CS
            - GRADIENTS_THROUGH_BEAM_CS
            - POINTS_THROUGH_SECTION
            
            The default value is CONSTANT_THROUGH_THICKNESS.
        field
            A String specifying the name of the AnalyticalField or DiscreteField object associated
            with this predefined field. The **field** argument applies only when
            **distributionType** = FIELD or **distributionType** = DISCRETE_FIELD. The default value is an
            empty string.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the predefined field has no amplitude reference. The default
            value is UNSET.Note:*amplitude* should be given only if it is valid for the specified
            step.
        fileName
            A String specifying the name of the file from which the temperature values are to be
            read when **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED.
        beginStep
            An Int specifying the first step from which temperature values are to be read or the
            SymbolicConstant FIRST_STEP or LAST_STEP. This argument is valid only when
            **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        beginIncrement
            An Int specifying the first increment of the step set in **beginStep** or the
            SymbolicConstants STEP_START or STEP_END. This argument is valid only when
            **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        endStep
            An Int specifying the last step from which temperature values are to be read or the
            SymbolicConstants FIRST_STEP and LAST_STEP. This argument is valid only when
            **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        endIncrement
            An Int specifying the last increment of the step set in **endStep** or the
            SymbolicConstants STEP_START and STEP_END. This argument is valid only when
            **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        interpolate
            A SymbolicConstant specifying whether to interpolate a field read from an output
            database or results file. Possible values are OFF, ON or MIDSIDE_ONLY. The default value
            is OFF.
        magnitudes
            A Sequence of Doubles specifying the temperature values when **distributionType** = UNIFORM
            or FIELD. The value of the **magnitudes** argument is a function of the
            **crossSectionDistribution** argument, as shown in the following list:
            
            - If **crossSectionDistribution** = CONSTANT_THROUGH_THICKNESS then **magnitudes** is a Double
              specifying the temperature.
            - If **crossSectionDistribution** = GRADIENTS_THROUGH_SHELL_CS then **magnitudes** is a
              sequence of Doubles specifying the mean value and the gradient in the thickness
              direction.
            - If **crossSectionDistribution** = GRADIENTS_THROUGH_BEAM_CS then **magnitudes** is a
              sequence of Doubles specifying the mean value, the gradient in the N1 direction, and the
              gradient in the N2 direction.
            - If **crossSectionDistribution** = POINTS_THROUGH_SECTION then **magnitudes** is a sequence
              of Doubles specifying the temperature at each point.
        absoluteExteriorTolerance
            A Float specifying the absolute value by which a driven node of the field can lie
            outside the region of the elements of the global model. The default value is 0.0. This
            argument cannot be used with **midside**.
        exteriorTolerance
            A Float specifying the fraction of the average element size in the global model by which
            a driven node of the field can lie outside the region of the elements of the global
            model. The default value is 0.0. This argument cannot be used with **midside**.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        field: str = "",
        amplitude: str = UNSET,
        fileName: str = "",
        beginStep: Optional[Literal[C.FROM_FILE, C.LAST_STEP, C.FROM_FILE_AND_USER_DEFINED, C.FIRST_STEP]] = None,
        beginIncrement: Optional[Literal[C.FROM_FILE, C.FROM_FILE_AND_USER_DEFINED, C.STEP_END, C.STEP_START]] = None,
        endStep: Optional[Literal[C.FROM_FILE, C.LAST_STEP, C.FROM_FILE_AND_USER_DEFINED, C.FIRST_STEP]] = None,
        endIncrement: Optional[Literal[C.FROM_FILE, C.FROM_FILE_AND_USER_DEFINED, C.STEP_END, C.STEP_START]] = None,
        interpolate: Union[Literal[C.MIDSIDE_ONLY], Boolean] = OFF,
        magnitudes: str = "",
        absoluteExteriorTolerance: float = 0,
        exteriorTolerance: float = 0,
    ):
        """This method modifies the propagating data for an existing Temperature object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the predefined field is modified.
        field
            A String specifying the name of the AnalyticalField or DiscreteField object associated
            with this predefined field. The **field** argument applies only when
            **distributionType** = FIELD or **distributionType** = DISCRETE_FIELD. The default value is an
            empty string.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the predefined field has no amplitude reference. The default
            value is UNSET.Note:*amplitude* should be given only if it is valid for the specified
            step.
        fileName
            A String specifying the name of the file from which the temperature values are to be
            read when **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED.
        beginStep
            An Int specifying the first step from which temperature values are to be read or the
            SymbolicConstant FIRST_STEP or LAST_STEP. This argument is valid only when
            **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        beginIncrement
            An Int specifying the first increment of the step set in **beginStep** or the
            SymbolicConstants STEP_START or STEP_END. This argument is valid only when
            **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        endStep
            An Int specifying the last step from which temperature values are to be read or the
            SymbolicConstants FIRST_STEP and LAST_STEP. This argument is valid only when
            **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        endIncrement
            An Int specifying the last increment of the step set in **endStep** or the
            SymbolicConstants STEP_START and STEP_END. This argument is valid only when
            **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        interpolate
            A SymbolicConstant specifying whether to interpolate a field read from an output
            database or results file. Possible values are OFF, ON or MIDSIDE_ONLY. The default value
            is OFF.
        magnitudes
            A Sequence of Doubles specifying the temperature values when **distributionType** = UNIFORM
            or FIELD. The value of the **magnitudes** argument is a function of the
            **crossSectionDistribution** argument, as shown in the following list:
            
            - If **crossSectionDistribution** = CONSTANT_THROUGH_THICKNESS then **magnitudes** is a Double
              specifying the temperature.
            - If **crossSectionDistribution** = GRADIENTS_THROUGH_SHELL_CS then **magnitudes** is a
              sequence of Doubles specifying the mean value and the gradient in the thickness
              direction.
            - If **crossSectionDistribution** = GRADIENTS_THROUGH_BEAM_CS then **magnitudes** is a
              sequence of Doubles specifying the mean value, the gradient in the N1 direction, and the
              gradient in the N2 direction.
            - If **crossSectionDistribution** = POINTS_THROUGH_SECTION then **magnitudes** is a sequence
              of Doubles specifying the temperature at each point.
        absoluteExteriorTolerance
            A Float specifying the absolute value by which a driven node of the field can lie
            outside the region of the elements of the global model. The default value is 0.0. This
            argument cannot be used with **midside**.
        exteriorTolerance
            A Float specifying the fraction of the average element size in the global model by which
            a driven node of the field can lie outside the region of the elements of the global
            model. The default value is 0.0. This argument cannot be used with **midside**.
        """
        ...
