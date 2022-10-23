from typing import Optional, Union

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .FluidCavityPressure import FluidCavityPressure
from .InitialState import InitialState
from .KinematicHardening import KinematicHardening
from .MaterialAssignment import MaterialAssignment
from .PorePressure import PorePressure
from .Saturation import Saturation
from .Stress import Stress
from .Temperature import Temperature
from .Velocity import Velocity
from .VoidsRatio import VoidsRatio
from ..Assembly.PartInstanceArray import PartInstanceArray
from ..Model.ModelBase import ModelBase
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import (Boolean, CONSTANT_THROUGH_THICKNESS, CONSTANT_RATIO,
                                              KINEMATIC_HARDENING, LAST_STEP, MAGNITUDE, OFF,
                                              STEP_END, UNIFORM, UNSET)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class PredefinedFieldModel(ModelBase):
    """Abaqus creates a Model object named `Model-1` when a session is started.

    .. note:: 
        This object can be accessed by::

            mdb.models[name]
    """

    @abaqus_method_doc
    def FluidCavityPressure(
        self, name: str, fluidCavity: str, fluidPressure: float
    ) -> FluidCavityPressure:
        """This method creates a FluidCavityPressure object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].FluidCavityPressure

        Parameters
        ----------
        name
            A String specifying the repository key.
        fluidCavity
            A String specifying the name of a Fluid Cavity Interaction.
        fluidPressure
            A Float specifying the initial fluid pressure.

        Returns
        -------
        FluidCavityPressure
            A :py:class:`~abaqus.PredefinedField.FluidCavityPressure.FluidCavityPressure` object.
        """
        self.predefinedFields[name] = predefinedField = FluidCavityPressure(
            name, fluidCavity, fluidPressure
        )
        return predefinedField

    @abaqus_method_doc
    def InitialState(
        self,
        name: str,
        instances: PartInstanceArray,
        fileName: str,
        endStep: Literal[C.LAST_STEP] = LAST_STEP,
        endIncrement: Literal[C.STEP_END] = STEP_END,
        updateReferenceConfiguration: Boolean = OFF,
    ) -> InitialState:
        """This method creates an InitialState predefined field object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].InitialState

        Parameters
        ----------
        name
            A String specifying the repository key.
        instances
            A :py:class:`~abaqus.Assembly.PartInstanceArray.PartInstanceArray` object specifying the instances to which the predefined field is
            applied.
        fileName
            A String specifying the name of the job that generated the initial state data.
        endStep
            The SymbolicConstant LAST_STEP or an Int specifying the step from which the initial
            state values are to be read or the SymbolicConstant LAST_STEP. The default value is
            LAST_STEP.
        endIncrement
            The SymbolicConstant STEP_END or an Int specifying the increment, interval or iteration
            of the step set in **endStep** or the SymbolicConstant STEP_END. The default value is
            STEP_END.
        updateReferenceConfiguration
            A Boolean specifying whether to update the reference configuration based on the import
            data. The default value is OFF.

        Returns
        -------
        InitialState
            An :py:class:`~abaqus.PredefinedField.InitialState.InitialState` object.
        """
        self.predefinedFields[name] = predefinedField = InitialState(
            name,
            instances,
            fileName,
            endStep,
            endIncrement,
            updateReferenceConfiguration,
        )
        return predefinedField

    @abaqus_method_doc
    def KinematicHardening(
        self,
        name: str,
        region: Region,
        numBackStress: int = 1,
        equivPlasticStrain: tuple = (),
        backStress: tuple = (),
        sectPtNum: tuple = (),
        definition: Literal[C.CRUSHABLE_FOAM, C.KINEMATIC_HARDENING, C.REBAR, C.USER_DEFINED, C.SECTION_PTS] = KINEMATIC_HARDENING,
        rebarLayerNames: tuple = (),
        distributionType: Literal[C.MAGNITUDE, C.ANALYTICAL_FIELD] = MAGNITUDE,
    ) -> KinematicHardening:
        """This method creates a KinematicHardening object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].KinematicHardening

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the predefined field is applied.
        numBackStress
            An Int specifying the number of backstresses. The default value is 1.
        equivPlasticStrain
            A sequence of Floats specifying the initial equivalent Plastic strain.
        backStress
            A sequence of sequences of Floats specifying the initial backstress tensor for kinematic
            hardening models. The default value is an empty sequence.
        sectPtNum
            A sequence of Ints specifying section point numbers. This argument is valid only when
            **definition** = SECTION_PTS.
        definition
            A SymbolicConstant specifying different types of kinematic hardening. Possible values
            are KINEMATIC_HARDENING, CRUSHABLE_FOAM, REBAR, SECTION_PTS, and USER_DEFINED. The
            default value is KINEMATIC_HARDENING.
        rebarLayerNames
            A sequence of Strings specifying rebar layer names. This argument is valid only when
            **definition** = REBAR.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are MAGNITUDE
            and ANALYTICAL_FIELD. The default value is MAGNITUDE.

        Returns
        -------
        KinematicHardening
            A :py:class:`~abaqus.PredefinedField.KinematicHardening.KinematicHardening` object.
        """
        self.predefinedFields[name] = predefinedField = KinematicHardening(
            name,
            region,
            numBackStress,
            equivPlasticStrain,
            backStress,
            sectPtNum,
            definition,
            rebarLayerNames,
            distributionType,
        )
        return predefinedField

    @abaqus_method_doc
    def MaterialAssignment(
        self,
        name: str,
        instanceList: PartInstanceArray,
        useFields: Boolean = OFF,
        assignmentList: tuple = (),
        fieldList: tuple = (),
        colorList: tuple = (),
    ) -> MaterialAssignment:
        """This method creates a MaterialAssignment predefined field object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].MaterialAssignment

        Parameters
        ----------
        name
            A String specifying the repository key.
        instanceList
            A :py:class:`~abaqus.Assembly.PartInstanceArray.PartInstanceArray` object specifying the part instances to which the predefined field
            is applied. All instances must be assigned the same Eulerian section.
        useFields
            A Boolean specifying whether the volume fraction data will be uniform or defined by
            discrete fields. The default value is OFF.
        assignmentList
            A sequence of tuples specifying the uniform volume fractions to be assigned. This
            argument is valid only when **useFields** = FALSE. Each tuple contains two entries:A Region
            object.A tuple of Floats specifying the uniform volume fraction values. The length of
            the tuple must match the number of material instance names specified in the Eulerain
            section assigned to part instances specified by **instanceList**.
        fieldList
            A sequence of tuples specifying the discrete volume fractions to be assigned. This
            argument is valid only when **useFields** = TRUE. Each tuple contains two entries:A Region
            object.A tuple of Strings specifying Discrete Field names. The length of the tuple must
            match the number of material instance names specified in the Eulerain section assigned
            to part instances specified by **instanceList**.
        colorList
            A sequence of three Ints specifying colors used to display the material instance
            assignments. This is a sequence of R,G,B colors, where the values are represented by
            integers between 0 and 255. The default value is an empty sequence.

        Returns
        -------
        MaterialAssignment
            A :py:class:`~abaqus.PredefinedField.MaterialAssignment.MaterialAssignment` object.
        """
        self.predefinedFields[name] = predefinedField = MaterialAssignment(
            name, instanceList, useFields, assignmentList, fieldList, colorList
        )
        return predefinedField

    @abaqus_method_doc
    def PorePressure(
        self,
        name: str,
        region: Region,
        distributionType: Literal[C.UNIFORM, C.FROM_FILE, C.USER_DEFINED] = UNIFORM,
        porePressure1: float = ...,
        porePressure2: float = ...,
        coord1: float = ...,
        coord2: float = ...,
        pressure2Distribution: Literal[C.MAGNITUDE, C.ANALYTICAL_FIELD] = MAGNITUDE,
        pressure2Field: str = ...,
        variation: Literal[C.CONSTANT_RATIO, C.VARIABLE_RATIO] = CONSTANT_RATIO,
        fileName: str = ...,
        increment: Union[int, Literal[C.LAST_INCREMENT]] = ...,
        step: Union[int, Literal[C.LAST_STEP]] = ...,
        interpolate: Boolean = ...,
    ) -> PorePressure:
        """This method creates a PorePressure predefined field object.

        .. note::
        
            This function can be accessed by::

                mdb.models[name].PorePressure

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A Region object specifying the region to which the predefined field is applied. Region
            is ignored if the predefined field has **distributionType** = FROM_FILE.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM,
            FROM_FILE and USER_DEFINED. The default value is UNIFORM.
        porePressure1
            The initial pore pressure in the first region in your model.
        porePressure2
            The pore pressure of the second location in your model
        coord1
            Vertical position of the first location in your model for which you are specifying initial pore pressure.
        coord2
            The vertical position of the second location in your model.
        pressure2Distribution
            A SymbolicConstant specifying either the magnitude of a uniform distribution for pore pressure at the
            second elevation or an analytical field to define a spatially varying initial pore pressure at the second elevation.
            Possible values are MAGNITUDE and ANALYTICAL_FIELD.
        pressure2Field
            A String specifying the name of the AnalyticalField object associated with this predefined field.
            The `pressure2Field` argument applies only when `distributionType` = ANALYTICAL_FIELD.
        variation
            A SymbolicConstant selecting the elevation distribution options, either Linear or Constant.
            Possible values are CONSTANT_RATIO and VARIABLE_RATIO.
        fileName
            A String specifying the name of the file from which the Field values are to be read when 
            `distributionType` = FROM_FILE.
        increment
            The SymbolicConstant LAST_INCREMENT or an Int specifying the increment, interval or iteration
            of the step when `distributionType` = FROM_FILE.
        step
            The SymbolicConstant LAST_STEP or an Int specifying the increment, interval or iteration
            of the step when `distributionType` = FROM_FILE.
        interpolate
            A Boolean specifying whether to interpolate a field read from an output database or results file.

        Returns
        -------
            A PorePressure object.
        """
        self.predefinedFields[name] = predefinedField = PorePressure(
            name,
            region,
            distributionType,
            porePressure1,
            porePressure2,
            coord1,
            coord2,
            pressure2Distribution,
            pressure2Field,
            variation,
            fileName,
            increment,
            step,
            interpolate,
        )
        return predefinedField

    @abaqus_method_doc
    def Temperature(
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
    ) -> Temperature:
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
        self.predefinedFields[name] = predefinedField = Temperature(
            name,
            createStepName,
            region,
            distributionType,
            crossSectionDistribution,
            field,
            amplitude,
            fileName,
            beginStep,
            beginIncrement,
            endStep,
            endIncrement,
            interpolate,
            magnitudes,
            absoluteExteriorTolerance,
            exteriorTolerance,
        )
        return predefinedField

    @abaqus_method_doc
    def Velocity(
        self,
        name: str,
        region: Region,
        velocity1: float,
        velocity2: float,
        velocity3: float,
        omega: float,
        axisBegin: tuple,
        axisEnd: tuple,
        field: str = "",
        distributionType: Literal[C.MAGNITUDE, C.FIELD_ANALYTICAL] = MAGNITUDE,
    ) -> Velocity:
        """This method creates a Velocity predefined field object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].Velocity

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the predefined field is applied.
        velocity1
            A Float specifying the first component of the velocity.
        velocity2
            A Float specifying the second component of the velocity.
        velocity3
            A Float specifying the third component of the velocity.
        omega
            A Float specifying the angular velocity.
        axisBegin
            A sequence of Floats specifying the *X-*, *Y-*, and **Z**- coordinates of the starting
            point of the axis about which **omega** is defined.
        axisEnd
            A sequence of Floats specifying the *X-*, *Y-*, and **Z**- coordinates of the end point of
            the axis about which **omega** is defined.
        field
            A String specifying the name of the AnalyticalField object associated with this
            predefined field. The **field** argument applies only when
            **distributionType** = FIELD_ANALYTICAL. The default value is an empty string.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are MAGNITUDE
            and FIELD_ANALYTICAL. The default value is MAGNITUDE.

        Returns
        -------
        Velocity
            A :py:class:`~abaqus.PredefinedField.Velocity.Velocity` object.
        """
        self.predefinedFields[name] = predefinedField = Velocity(
            name,
            region,
            velocity1,
            velocity2,
            velocity3,
            omega,
            axisBegin,
            axisEnd,
            field,
            distributionType,
        )
        return predefinedField

    @abaqus_method_doc
    def Saturation(
        self,
        name: str,
        region: Region,
        distributionType: Literal[C.UNIFORM, C.FIELD] = UNIFORM,
        field: str = '',
        value: float = ...
    ) -> Saturation:
        """This method creates a Saturation predefined field object.

        .. note::

            This function can be accessed by::

                mdb.models[name].Saturation

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A Region object specifying the region to which the predefined field is applied.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM,
            and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated
            with this predefined field. The **field** argument applies only when
            **distributionType** = FIELD. The default value is an empty string.
        value
            A float specifying an initial saturation value for the region between 0.0 (for no
            saturation) and 1.0 (for full saturation).

        Returns
        -------
            A Saturation object.
        """
        self.predefinedFields[name] = predefinedField = Saturation(
            name,
            region,
            distributionType,
            field,
            value,
        )
        return predefinedField

    @abaqus_method_doc
    def Stress(
        self,
        name: str,
        region: Region,
        distributionType: Literal[C.UNIFORM, C.FROM_FILE] = UNIFORM,
        sigma11: float = ...,
        sigma22: float = ...,
        sigma33: float = ...,
        sigma12: float = ...,
        sigma13: float = ...,
        sigma23: float = ...,
    ) -> Stress:
        """This method creates a Stress predefined field object.

        .. note::
            This function can be accessed by::

                mdb.models[name].Stress

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A Region object specifying the region to which the predefined field is applied. Region
            is ignored if the predefined field has **distributionType** = FROM_FILE.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM
            and FROM_FILE. The default value is UNIFORM.
        sigma11
            A Float specifying the first principal component of the stress.
        sigma22
            A Float specifying the second principal component of the stress.
        sigma33
            A Float specifying the third principal component of the stress.
        sigma12
            A Float specifying the first shear component of the stress.
        sigma13
            A Float specifying the second shear component of the stress.
        sigma23
            A Float specifying the third shear component of the stress.

        Returns
        -------
            A Stress object.
        """
        self.predefinedFields[name] = predefinedField = Stress(
            name,
            region,
            distributionType,
            sigma11,
            sigma22,
            sigma33,
            sigma12,
            sigma13,
            sigma23,
        )
        return predefinedField
<<<<<<< HEAD
=======
    
    @abaqus_method_doc
    def Field(
        self,
        name: str,
        createStepName: str,
        region: Region,
        outputVariable: str = "",
        fieldVariableNum: Optional[int] = None,
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
    ):
        """This method creates a Field object.

        .. note::
            This function can be accessed by::

                mdb.models[name].Field

        .. versionadded:: 2018
            The `Field` method was added.

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
                **amplitude** should be given only if it is valid for the specified step.
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
        self.predefinedFields[name] = predefinedField = Field(
            name,
            createStepName,
            region,
            outputVariable,
            fieldVariableNum,
            distributionType,
            crossSectionDistribution,
            field,
            amplitude,
            fileName,
            beginStep,
            beginIncrement,
            endStep,
            endIncrement,
            interpolate,
            magnitudes,
        )
        return predefinedField
>>>>>>> 9cc45e87 ([typing]: Including remaining `Literal` in all modules (#3004))

    @abaqus_method_doc
    def VoidsRatio(
        self,
        name: str,
        region: Region,
        distributionType: Literal[C.UNIFORM, C.FROM_FILE, C.USER_DEFINED] = UNIFORM,
        voidsRatio1: float = ...,
        voidsRatio2: float = ...,
        coord1: float = ...,
        coord2: float = ...,
        ratio2Distribution: Literal[C.MAGNITUDE, C.ANALYTICAL_FIELD] = MAGNITUDE,
        ratio2Field: str = ...,
        variation: Literal[C.CONSTANT_RATIO, C.VARIABLE_RATIO] = CONSTANT_RATIO,
        fileName: str = ...,
        increment: Union[int, Literal[C.LAST_INCREMENT]] = ...,
        step: Union[int, Literal[C.LAST_STEP]] = ...,
        interpolate: Boolean = ...,
    ) -> VoidsRatio:
        """This method creates a PorePressure predefined field object.

        .. note::
        This function can be accessed by::

            mdb.models[name].PorePressure

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A Region object specifying the region to which the predefined field is applied. Region
            is ignored if the predefined field has **distributionType** = FROM_FILE.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM,
            FROM_FILE and USER_DEFINED. The default value is UNIFORM.
        voidsRatio1
            The initial void ratio in the first region in your model.
        voidsRatio2
            The void ratio of the second location in your model
        coord1
            Vertical position of the first location in your model for which you are specifying initial void ratio.
        coord2
            The vertical position of the second location in your model
        ratio2Distribution
            A SymbolicConstant specifying either the magnitude of a uniform distribution for void ratio at the
            second elevation or an analytical field to define a spatially varying initial void ratio at the second elevation.
            Possible values are MAGNITUDE and ANALYTICAL_FIELD.
        ratio2Field
            A String specifying the name of the AnalyticalField object associated with this predefined field.
            The `ratio2Field` argument applies only when `distributionType` = ANALYTICAL_FIELD.
        variation
            A SymbolicConstant selecting the elevation distribution options, either Linear or Constant.
            Possible values are CONSTANT_RATIO and VARIABLE_RATIO.
        fileName
            A String specifying the name of the file from which the Field values are to be read when 
            `distributionType` = FROM_FILE.
        increment
            The SymbolicConstant LAST_INCREMENT or an Int specifying the increment, interval or iteration
            of the step when `distributionType` = FROM_FILE.
        step
            The SymbolicConstant LAST_STEP or an Int specifying the increment, interval or iteration
            of the step when `distributionType` = FROM_FILE.
        interpolate
            A Boolean specifying whether to interpolate a field read from an output database or results file.

        Returns
        -------
            A VoidsRatio object.
        """
        self.predefinedFields[name] = predefinedField = VoidsRatio(
            name,
            region,
            distributionType,
            voidsRatio1,
            voidsRatio2,
            coord1,
            coord2,
            ratio2Distribution,
            ratio2Field,
            variation,
            fileName,
            increment,
            step,
            interpolate,
        )
        return predefinedField
