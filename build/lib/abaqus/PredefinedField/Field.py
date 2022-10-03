from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .PredefinedField import PredefinedField
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import (CONSTANT_THROUGH_THICKNESS, OFF, SymbolicConstant,
                                              UNIFORM, UNSET)


@abaqus_class_doc
class Field(PredefinedField):
    """The Field object stores the data for field predefined fields.
    The Field object is derived from the PredefinedField object.
    **distributionType=FROM_FILE** or FROM_FILE_AND_USER_DEFINED.

    .. note::
        This object can be accessed by::

            import load
            mdb.models[name].predefinedFields[name]

        The corresponding analysis keywords are:

        - INITIAL CONDITIONS
        - FIELD

    .. versionadded:: 2018
        The `Field` class was added.
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

    #: A Region object specifying the region to which the predefined field is applied. *Region*
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
        outputVariable: str = "",
        fieldVariableNum: Optional[int] = None,
        distributionType: SymbolicConstant = UNIFORM,
        crossSectionDistribution: SymbolicConstant = CONSTANT_THROUGH_THICKNESS,
        field: str = "",
        amplitude: str = UNSET,
        fileName: str = "",
        beginStep: Optional[SymbolicConstant] = None,
        beginIncrement: Optional[SymbolicConstant] = None,
        endStep: Optional[SymbolicConstant] = None,
        endIncrement: Optional[SymbolicConstant] = None,
        interpolate: SymbolicConstant = OFF,
        magnitudes: str = "",
    ):
        """This method creates a Field object.

        .. note::
            This function can be accessed by::

                mdb.models[name].Field

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the predefined field is created.
        region
            A Region object specifying the region to which the predefined field is applied. *Region*
            is ignored if the predefined field has a **distributionType** member available, and
            **distributionType** = FROM_FILE.
        outputVariable
            A String specifying the scalar nodal output variable that will be read from an output
            database and used to initialize a specified predefined field. This argument is a
            required argument if **distributionType** = FROM_FILE or
            **distributionType** = FROM_FILE_AND_USER_DEFINED.
        fieldVariableNum
            An Int specifying the field variable number.
        distributionType
            A SymbolicConstant specifying how the predefined field varies spatially. Possible values
            are UNIFORM, USER_DEFINED, FROM_FILE, FIELD, FROM_FILE_AND_USER_DEFINED, and
            DISCRETE_FIELD. The default value is UNIFORM.
        crossSectionDistribution
            A SymbolicConstant specifying how the predefined field is distributed over the
            cross-section of the region. Possible values are
            
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
            value is UNSET. 
            
            .. note::
                **amplitude** should be given only if it is valid for the specified
            step.
        fileName
            A String specifying the name of the file from which the Field values are to be read when
            **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED.
        beginStep
            An Int specifying the first step from which Field values are to be read or the
            SymbolicConstant FIRST_STEP or LAST_STEP. This argument is valid only when
            **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        beginIncrement
            An Int specifying the first increment of the step set in **beginStep** or the
            SymbolicConstants STEP_START or STEP_END. This argument is valid only when
            **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        endStep
            An Int specifying the last step from which Field values are to be read or the
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
            database or results file. Possible values are OFF, ON, or MIDSIDE_ONLY. The default
            value is OFF.
        magnitudes
            A Sequence of Doubles specifying the Field values when **distributionType** = UNIFORM or
            FIELD. The value of the **magnitudes** argument is a function of the
            **crossSectionDistribution** argument, as shown in the following list:
            
            - If **crossSectionDistribution** = CONSTANT_THROUGH_THICKNESS, **magnitudes** is a Double
              specifying the Field.
            - If **crossSectionDistribution** = GRADIENTS_THROUGH_SHELL_CS, **magnitudes** is a sequence
              of Doubles specifying the mean value and the gradient in the thickness direction.
            - If **crossSectionDistribution** = GRADIENTS_THROUGH_BEAM_CS, **magnitudes** is a sequence of
              Doubles specifying the mean value, the gradient in the N1 direction, and the gradient in
              the N2 direction.
            - If **crossSectionDistribution** = POINTS_THROUGH_SECTION, **magnitudes** is a sequence of
              Doubles specifying the Field at each point.

        Returns
        -------
            A Field object.
        """
        super().__init__()

    @abaqus_method_doc
    def move(self, fromStepName: str, toStepName: str):
        """This method moves the FieldState object from one step to a different step.

        Parameters
        ----------
        fromStepName
            A String specifying the name of the step from which the PredefinedFieldState is moved.
        toStepName
            A String specifying the name of the step to which the PredefinedFieldState is moved.

        Raises
        ------
            TextError.
        """
        ...

    @abaqus_method_doc
    def setValues(
        self,
        outputVariable: str = "",
        fieldVariableNum: Optional[int] = None,
        distributionType: SymbolicConstant = UNIFORM,
        crossSectionDistribution: SymbolicConstant = CONSTANT_THROUGH_THICKNESS,
        field: str = "",
        amplitude: str = UNSET,
        fileName: str = "",
        beginStep: Optional[SymbolicConstant] = None,
        beginIncrement: Optional[SymbolicConstant] = None,
        endStep: Optional[SymbolicConstant] = None,
        endIncrement: Optional[SymbolicConstant] = None,
        interpolate: SymbolicConstant = OFF,
        magnitudes: str = "",
    ):
        """This method modifies the data for an existing Field object in the step where it is
        created.

        Parameters
        ----------
        outputVariable
            A String specifying the scalar nodal output variable that will be read from an output
            database and used to initialize a specified predefined field. This argument is a
            required argument if **distributionType** = FROM_FILE or
            **distributionType** = FROM_FILE_AND_USER_DEFINED.
        fieldVariableNum
            An Int specifying the field variable number.
        distributionType
            A SymbolicConstant specifying how the predefined field varies spatially. Possible values
            are UNIFORM, USER_DEFINED, FROM_FILE, FIELD, FROM_FILE_AND_USER_DEFINED, and
            DISCRETE_FIELD. The default value is UNIFORM.
        crossSectionDistribution
            A SymbolicConstant specifying how the predefined field is distributed over the
            cross-section of the region. Possible values are
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
            A String specifying the name of the file from which the Field values are to be read when
            **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED.
        beginStep
            An Int specifying the first step from which Field values are to be read or the
            SymbolicConstant FIRST_STEP or LAST_STEP. This argument is valid only when
            **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        beginIncrement
            An Int specifying the first increment of the step set in **beginStep** or the
            SymbolicConstants STEP_START or STEP_END. This argument is valid only when
            **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        endStep
            An Int specifying the last step from which Field values are to be read or the
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
            database or results file. Possible values are OFF, ON, or MIDSIDE_ONLY. The default
            value is OFF.
        magnitudes
            A Sequence of Doubles specifying the Field values when **distributionType** = UNIFORM or
            FIELD. The value of the **magnitudes** argument is a function of the
            **crossSectionDistribution** argument, as shown in the following list:
            - If **crossSectionDistribution** = CONSTANT_THROUGH_THICKNESS, **magnitudes** is a Double
            specifying the Field.
            - If **crossSectionDistribution** = GRADIENTS_THROUGH_SHELL_CS, **magnitudes** is a sequence
            of Doubles specifying the mean value and the gradient in the thickness direction.
            - If **crossSectionDistribution** = GRADIENTS_THROUGH_BEAM_CS, **magnitudes** is a sequence of
            Doubles specifying the mean value, the gradient in the N1 direction, and the gradient in
            the N2 direction.
            - If **crossSectionDistribution** = POINTS_THROUGH_SECTION, **magnitudes** is a sequence of
            Doubles specifying the Field at each point.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        outputVariable: str = "",
        fieldVariableNum: Optional[int] = None,
        field: str = "",
        amplitude: str = UNSET,
        fileName: str = "",
        beginStep: Optional[SymbolicConstant] = None,
        beginIncrement: Optional[SymbolicConstant] = None,
        endStep: Optional[SymbolicConstant] = None,
        endIncrement: Optional[SymbolicConstant] = None,
        interpolate: SymbolicConstant = OFF,
        magnitudes: str = "",
    ):
        """This method modifies the propagating data for an existing Field object in the specified
        step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the predefined field is modified.
        outputVariable
            A String specifying the scalar nodal output variable that will be read from an output
            database and used to initialize a specified predefined field. This argument is a
            required argument if **distributionType** = FROM_FILE or
            **distributionType** = FROM_FILE_AND_USER_DEFINED.
        fieldVariableNum
            An Int specifying the field variable number.
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
            A String specifying the name of the file from which the Field values are to be read when
            **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED.
        beginStep
            An Int specifying the first step from which Field values are to be read or the
            SymbolicConstant FIRST_STEP or LAST_STEP. This argument is valid only when
            **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        beginIncrement
            An Int specifying the first increment of the step set in **beginStep** or the
            SymbolicConstants STEP_START or STEP_END. This argument is valid only when
            **distributionType** = FROM_FILE or **distributionType** = FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        endStep
            An Int specifying the last step from which Field values are to be read or the
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
            database or results file. Possible values are OFF, ON, or MIDSIDE_ONLY. The default
            value is OFF.
        magnitudes
            A Sequence of Doubles specifying the Field values when **distributionType** = UNIFORM or
            FIELD. The value of the **magnitudes** argument is a function of the
            **crossSectionDistribution** argument, as shown in the following list:
            - If **crossSectionDistribution** = CONSTANT_THROUGH_THICKNESS, **magnitudes** is a Double
            specifying the Field.
            - If **crossSectionDistribution** = GRADIENTS_THROUGH_SHELL_CS, **magnitudes** is a sequence
            of Doubles specifying the mean value and the gradient in the thickness direction.
            - If **crossSectionDistribution** = GRADIENTS_THROUGH_BEAM_CS, **magnitudes** is a sequence of
            Doubles specifying the mean value, the gradient in the N1 direction, and the gradient in
            the N2 direction.
            - If **crossSectionDistribution** = POINTS_THROUGH_SECTION, **magnitudes** is a sequence of
            Doubles specifying the Field at each point.
        """
        ...
