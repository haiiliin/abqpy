from __future__ import annotations

from typing import Union, Tuple, Sequence, List, Dict, overload

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .AreaStyle import AreaStyle
from .LineStyle import LineStyle
from .QuantityType import QuantityType
from .SymbolStyle import SymbolStyle
from .TextStyle import TextStyle
from .XYData import XYData
from .XYSessionBase import XYSessionBase
from ..Odb.Odb import Odb
from ..PathAndProbe.Path import Path
from ..UtilityAndView.SymbolicConstant import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import (Boolean, COMPLEX_VAL_AT_ANGLE, FILLED_CIRCLE, IMAGINARY, NONE, OFF, ON,
                                              REAL, SOLID, SymbolicConstant)


@abaqus_class_doc
class XYSession(XYSessionBase):
    @staticmethod
    @abaqus_method_doc
    def AreaStyle(
        color: str = "", fill: Boolean = ON, style: SymbolicConstant = SOLID
    ) -> AreaStyle:
        """This method creates an AreaStyle.

        .. note:: 
            This function can be accessed by::

                session.AreaStyle
                xyPlot.AreaStyle

        Parameters
        ----------
        color
            A String specifying the color to be used when filling an area with this AreaStyle
            object. The default value is "White".
        fill
            A Boolean specifying whether to fill the area when using this AreaStyle. The default
            value is ON.
        style
            A SymbolicConstant specifying the area pattern style to be used when filling an area
            using this AreaStyle. The default value is SOLID.

        Returns
        -------
        AreaStyle
            An :py:class:`~abaqus.XY.AreaStyle.AreaStyle` object.

        Raises
        ------
        ColorError
        """
        areaStyle = AreaStyle(color, fill, style)
        return areaStyle

    @staticmethod
    @abaqus_method_doc
    def LineStyle(
        color: str = "",
        show: Boolean = ON,
        style: Literal[C.SOLID, C.DASHED, C.DOTTED, C.DOT_DASH] = SOLID,
        thickness: float = 0,
    ) -> LineStyle:
        """This method creates a LineStyle.

        .. note:: 
            This function can be accessed by::

                session.LineStyle
                xyPlot.LineStyle

        Parameters
        ----------
        color
            A String specifying the color to be used when drawing a line with this LineStyle object.
            The default value is "White".
        show
            A Boolean specifying whether to draw the line when using this LineStyle. The default
            value is ON.
        style
            A SymbolicConstant specifying the line style to be used when drawing lines using this
            LineStyle. Possible values are SOLID, DASHED, DOTTED, and DOT_DASH. The default value is
            SOLID.
        thickness
            A Float specifying the line thickness in mm to be used when drawing lines using this
            LineStyle. The default value is 0.2.

        Returns
        -------
        LineStyle
            A :py:class:`~abaqus.XY.LineStyle.LineStyle` object.

        Raises
        ------
        ColorError
        """
        lineStyle = LineStyle(color, show, style, thickness)
        return lineStyle

    @staticmethod
    @abaqus_method_doc
    def QuantityType(
        type: Literal[
            C.NONE,
            C.ACCELERATION,
            C.ACOUSTIC_INTENSITY,
            C.ANGLE,
            C.ANGULAR_MOMENTUM,
            C.ARC_LENGTH,
            C.AREA,
            C.AREA_VELOCITY_SQUARED,
            C.BIMOMENT,
            C.CURVATURE,
            C.CORIOLIS_LOAD,
            C.DAMAGE,
            C.DAMAGE_CRITERION,
            C.DENSITY,
            C.DENSITY_ROTATIONAL_ACCELERATION,
            C.DISPLACEMENT,
            C.ECURRENT_AREA_TIME,
            C.ELECTRIC_CHARGE,
            C.ELECTRIC_CURRENT,
            C.ELECTRIC_CURRENT_AREA,
            C.ELECTRIC_POTENTIAL,
            C.ENERGY,
            C.ENERGY_DENSITY,
            C.ENERGY_RELEASE_RATE,
            C.EPOTENTIAL_GRADIENT,
            C.FREQUENCY,
            C.FORCE,
            C.FORCE_VOLUME,
            C.HEAT_FLUX,
            C.HEAT_FLUX_AREA,
            C.HEAT_FLUX_RATE,
            C.HEAT_FLUX_VOLUME,
            C.LENGTH,
            C.LINEAR_PRESSURE,
            C.LUMIN,
            C.MASS,
            C.MASS_FLOW_AREA,
            C.MASS_FLOW_AREA_RATE,
            C.MASS_FLOW_RATE,
            C.MODE_NUMBER,
            C.MOMENT,
            C.NUMBER,
            C.PATH,
            C.PHASE,
            C.POSITION,
            C.PRESSURE,
            C.PRESSURE_GRADIENT,
            C.RATE,
            C.ROTARY_INERTIA,
            C.ROTATIONAL_ACCELERATION,
            C.ROTATIONAL_VELOCITY,
            C.STATUS,
            C.STRAIN,
            C.STRAIN_RATE,
            C.STRESS,
            C.STRESS_INTENS_FACTOR,
            C.SUBSTANCE,
            C.TEMPERATURE,
            C.THICKNESS,
            C.TIME,
            C.TIME_INCREMENT,
            C.TIME_HEAT_FLUX,
            C.TIME_HEAT_FLUX_AREA,
            C.TIME_VOLUME,
            C.TIME_VOLUME_FLUX,
            C.TWIST,
            C.VELOCITY,
            C.VELOCITY_SQUARED,
            C.VOLUME,
            C.VOLUME_FLUX,
            C.VOLUME_FLUX_AREA,
            C.VOLUME_FRACTION,
        ],
        label: str = "",
    ) -> QuantityType:
        """This method creates a QuantityType object.

        .. note:: 
            This function can be accessed by::

                session.QuantityType
                xyPlot.QuantityType

        Parameters
        ----------
        type
            A SymbolicConstant specifying the physical dimension of the axis. Possible values are:

            - NONE.
            - ACCELERATION.
            - ACOUSTIC_INTENSITY.
            - ANGLE.
            - ANGULAR_MOMENTUM.
            - ARC_LENGTH.
            - AREA.
            - AREA_VELOCITY_SQUARED, specifying "Velocity squared per area".
            - BIMOMENT.
            - CURVATURE.
            - CORIOLIS_LOAD.
            - DAMAGE.
            - DAMAGE_CRITERION.
            - DENSITY.
            - DENSITY_ROTATIONAL_ACCELERATION, specifying "Density * Angular acceleration".
            - DISPLACEMENT.
            - ECURRENT_AREA_TIME, specifying "Time integrated electric current per area".
            - ELECTRIC_CHARGE.
            - ELECTRIC_CURRENT.
            - ELECTRIC_CURRENT_AREA, specifying "Electric current per unit area".
            - ELECTRIC_POTENTIAL.
            - ENERGY.
            - ENERGY_DENSITY.
            - ENERGY_RELEASE_RATE.
            - EPOTENTIAL_GRADIENT, specifying "Electric potential gradient".
            - FREQUENCY.
            - FORCE.
            - FORCE_VOLUME, specifying "Force per volume".
            - HEAT_FLUX.
            - HEAT_FLUX_AREA, specifying "Heat flux per area".
            - HEAT_FLUX_RATE.
            - HEAT_FLUX_VOLUME, specifying "Heat flux per volume".
            - LENGTH.
            - LINEAR_PRESSURE.
            - LUMIN, specifying "Luminous intensity".
            - MASS.
            - MASS_FLOW_AREA, specifying "Mass flow per area".
            - MASS_FLOW_AREA_RATE, specifying "Mass flow rate per area".
            - MASS_FLOW_RATE.
            - MODE_NUMBER.
            - MOMENT.
            - NUMBER.
            - PATH.
            - PHASE.
            - POSITION.
            - PRESSURE.
            - PRESSURE_GRADIENT.
            - RATE.
            - ROTARY_INERTIA.
            - ROTATIONAL_ACCELERATION.
            - ROTATIONAL_VELOCITY.
            - STATUS.
            - STRAIN.
            - STRAIN_RATE.
            - STRESS.
            - STRESS_INTENS_FACTOR, specifying "Stress intensity factor".
            - SUBSTANCE, specifying "Amount of substance".
            - TEMPERATURE.
            - THICKNESS.
            - TIME.
            - TIME_INCREMENT.
            - TIME_HEAT_FLUX, specifying "Time integrated heat flux".
            - TIME_HEAT_FLUX_AREA, specifying "Time integrated heat flux per area".
            - TIME_VOLUME, specifying "Time integrated volume".
            - TIME_VOLUME_FLUX, specifying "Time integrated volume flux per area".
            - TWIST.
            - VELOCITY.
            - VELOCITY_SQUARED.
            - VOLUME.
            - VOLUME_FLUX.
            - VOLUME_FLUX_AREA, specifying "Volume flux per area".
            - VOLUME_FRACTION.
        label
            A String specifying the label for this quantity type.

        Returns
        -------
        QuantityType
            A :py:class:`~abaqus.XY.QuantityType.QuantityType` object.
        """
        quantityType = QuantityType(type, label)
        return quantityType

    @staticmethod
    @abaqus_method_doc
    def SymbolStyle(
        color: str = "",
        show: Boolean = ON,
        marker: Literal[
            C.FILLED_CIRCLE,
            C.FILLED_SQUARE,
            C.FILLED_DIAMOND,
            C.FILLED_TRI,
            C.HOLLOW_CIRCLE,
            C.HOLLOW_SQUARE,
            C.HOLLOW_DIAMOND,
            C.HOLLOW_TRI,
            C.CROSS,
            C.XMARKER,
            C.POINT,
        ] = FILLED_CIRCLE,
        size: float = 2,
    ) -> SymbolStyle:
        """This method creates a SymbolStyle object.

        .. note:: 
            This function can be accessed by::

                session.SymbolStyle
                xyPlot.SymbolStyle

        Parameters
        ----------
        color
            A String specifying the color to be used when drawing a marker with this SymbolStyle
            object. The default value is "White".
        show
            A Boolean specifying whether to draw the marker when using this SymbolStyle object. The
            default value is ON.
        marker
            A SymbolicConstant specifying the marker type be used when drawing symbols using this
            SymbolStyle object. Possible values are:
            
            - FILLED_CIRCLE
            - FILLED_SQUARE
            - FILLED_DIAMOND
            - FILLED_TRI
            - HOLLOW_CIRCLE
            - HOLLOW_SQUARE
            - HOLLOW_DIAMOND
            - HOLLOW_TRI
            - CROSS
            - XMARKER
            - POINT
            
            The default value is FILLED_CIRCLE.
        size
            A Float specifying the marker size to be used when drawing markers using this
            SymbolStyle object. The default value is 2.0.

        Returns
        -------
        SymbolStyle
            A :py:class:`~abaqus.XY.SymbolStyle.SymbolStyle` object.

        Raises
        ------
        ColorError
        """
        symbolStyle = SymbolStyle(color, show, marker, size)
        return symbolStyle

    @staticmethod
    @abaqus_method_doc
    def TextStyle(
        color: str = "", show: Boolean = ON, font: str = "", rotationAngle: float = 0
    ) -> TextStyle:
        """This method creates a TextStyle.

        .. note:: 
            This function can be accessed by::

                session.TextStyle
                xyPlot.TextStyle

        Parameters
        ----------
        color
            A String specifying the color to be used when drawing text with this TextStyle object.
            The default value is "White".
        show
            A Boolean specifying whether to draw the text when using this TextStyle object. The
            default value is ON.
        font
            A String specifying the name of the font to be used when drawing text with this
            TextStyle object. The default value is "-*-verdana-medium-r-normal-*-*-120-*-*-p-*-*-*".
        rotationAngle
            A Float specifying the angle in degrees used for displaying the text. The default value
            is 0.0.

        Returns
        -------
        TextStyle
            A :py:class:`~abaqus.XY.TextStyle.TextStyle` object.

        Raises
        ------
        ColorError
        """
        textStyle = TextStyle(color, show, font, rotationAngle)
        return textStyle

    @staticmethod
    @overload
    @abaqus_method_doc
    def XYData(
        data: tuple,
        name: str = "",
        sourceDescription: str = "",
        contentDescription: str = "",
        positionDescription: str = "",
        legendLabel: str = "",
        xValuesLabel: str = "",
        yValuesLabel: str = "",
        axis1QuantityType: QuantityType = ...,
        axis2QuantityType: QuantityType = ...,
    ) -> XYData:
        """This method creates an XYData object from a sequence of **X - Y** data pairs.

        .. note:: 
            This function can be accessed by::

                session.XYData
                xyPlot.XYData

        Parameters
        ----------
        data
            A sequence of pairs of Floats specifying the **X - Y** data pairs.
        name
            The repository key. If the name is not supplied while creating the XYData object using
            xyPlot.XYData, a default name in the form _temp#_ is generated and the XYData object is
            temporary. (This argument is required if the method is accessed from the session
            object.)
        sourceDescription
            A String specifying the source of the **X - Y** data (e.g., “Entered from keyboard”, “Taken
            from ASCII file”, “Read from an ODB”, etc.). The default value is an empty string.
        contentDescription
            A String specifying the content of the **X - Y** data (e.g., “field 1 vs. field 2”). The
            default value is an empty string.
        positionDescription
            A String specifying additional information about the **X - Y** data (e.g., “for whole
            model”). The default value is an empty string.
        legendLabel
            A String specifying the label to be used in the legend. The default value is the name of
            the XYData object.
        xValuesLabel
            A String specifying the label for the X-values. This value may be overridden if the
            **X - Y** data are combined with other **X - Y** data. The default value is an empty string.
        yValuesLabel
            A String specifying the label for the Y-values. This value may be overridden if the
            **X - Y** data are combined with other **X - Y** data. The default value is an empty string.
        axis1QuantityType
            A :py:class:`~abaqus.XY.QuantityType.QuantityType` object specifying the QuantityType object associated to the X -axis1-
            values.
        axis2QuantityType
            A :py:class:`~abaqus.XY.QuantityType.QuantityType` object specifying the QuantityType object associated to the Y -axis2-
            values.

        Returns
        -------
        XYData
            An :py:class:`~abaqus.XY.XYData.XYData` object.
        """
        ...

    @staticmethod
    @overload
    @abaqus_method_doc
    def XYData(objectToCopy: XYData) -> XYData:
        """This method creates an XYData object by copying an existing XYData object.

        .. note:: 
            This function can be accessed by::

                session.odbs[name].userData.XYData
                session.XYData
                xyPlot.XYData

        Parameters
        ----------
        objectToCopy
            An :py:class:`~abaqus.XY.XYData.XYData` object to be copied.

        Returns
        -------
        XYData
            An :py:class:`~abaqus.XY.XYData.XYData` object.
        """
        ...

    @staticmethod
    @abaqus_method_doc
    def XYData(*args, **kwargs) -> XYData:
        return XYData(())

    def XYDataFromFile(
        self,
        fileName: str,
        name: str = "",
        sourceDescription: str = "",
        contentDescription: str = "",
        positionDescription: str = "",
        legendLabel: str = "",
        xValuesLabel: str = "",
        yValuesLabel: str = "",
        axis1QuantityType: QuantityType = ...,
        axis2QuantityType: QuantityType = ...,
        xField: int = 1,
        yField: int = 2,
        skipFrequency: int = 0,
    ) -> XYData:
        """This method creates an XYData object from data in an ASCII file.

        .. note:: 
            This function can be accessed by::

                session.XYDataFromFile
                xyPlot.XYDataFromFile

        Parameters
        ----------
        fileName
            A String specifying the name of the file from which the **X - Y** data will be read.
        name
            The repository key. If the name is not supplied, a default name in the form _temp#_ is
            generated and the XYData object is temporary.
        sourceDescription
            A String specifying the source of the **X - Y** data (e.g., “Entered from keyboard”, “Taken
            from ASCII file”, “Read from an ODB”, etc.). The default value is an empty string.
        contentDescription
            A String specifying the content of the **X - Y** data (e.g., “field 1 vs. field 2”). The
            default value is an empty string.
        positionDescription
            A String specifying additional information about the **X - Y** data (e.g., “for whole
            model”). The default value is an empty string.
        legendLabel
            A String specifying the label to be used in the legend. The default value is the name of
            the XYData object.
        xValuesLabel
            A String specifying the label for the X-values. This value may be overridden if the
            **X - Y** data are combined with other **X - Y** data. The default value is an empty string.
        yValuesLabel
            A String specifying the label for the Y-values. This value may be overridden if the
            **X - Y** data are combined with other **X - Y** data. The default value is an empty string.
        axis1QuantityType
            A :py:class:`~abaqus.XY.QuantityType.QuantityType` object specifying the QuantityType object associated to
            the X -axis1- values.
        axis2QuantityType
            A :py:class:`~abaqus.XY.QuantityType.QuantityType` object specifying the QuantityType object associated to
            the Y -axis2- values.
        xField
            An Int specifying the field from which the **X**-data will be read. Fields are delimited
            by spaces, tabs, or commas. The default value is 1.
        yField
            An Int specifying the field from which the **Y**-data will be read. Fields are delimited
            by spaces, tabs, or commas. The default value is 2.
        skipFrequency
            An Int specifying how often data rows will be skipped. A **skipFrequency** of 1 means skip
            every other row. The first row is always read. Possible values are **skipFrequency** ≥ 0.
            The default value is 0 (data are read from every row).

        Returns
        -------
        XYData
            An :py:class:`~abaqus.XY.XYData.XYData` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.xyDataObjects[name] = xyData = XYData(())
        return xyData

    @abaqus_method_doc
    def XYDataFromHistory(
        self,
        odb: Odb,
        outputVariableName: str,
        steps: tuple,
        name: str = "",
        sourceDescription: str = "",
        contentDescription: str = "",
        positionDescription: str = "",
        legendLabel: str = "",
        skipFrequency: int = 0,
        numericForm: Literal[
            C.COMPLEX_MAGNITUDE, C.COMPLEX_PHASE, C.REAL, C.IMAGINARY, C.COMPLEX_VAL_AT_ANGLE
        ] = REAL,
        complexAngle: float = 0,
        stepTuple: Sequence[int] = ...,
    ) -> XYData:
        """This method creates an XYData object by reading history data from an Odb object.

        .. note:: 
            This function can be accessed by::

                session.XYDataFromHistory
                xyPlot.XYDataFromHistory

        Parameters
        ----------
        odb
            An :py:class:`~abaqus.Odb.Odb.Odb` object specifying the output database from which data will be read.
        outputVariableName
            A String specifying the output variable from which the **X - Y** data will be read.
        steps
            A sequence of Strings specifying the names of the steps from which data will be
            extracted.
        name
            The repository key. If the name is not supplied, a default name in the form _temp#_ is
            generated and the XYData object is temporary (this argument is required if the method is
            accessed from the session object).
        sourceDescription
            A String specifying the source of the **X - Y** data (for example, “Entered from keyboard”,
            “Taken from ASCII file”, “Read from an ODB”, etc.). The default value is an empty
            string.
        contentDescription
            A String specifying the content of the **X - Y** data (for example, “field 1 vs. field 2”).
            The default value is an empty string.
        positionDescription
            A String specifying additional information about the **X - Y** data (for example, “for whole
            model”). The default value is an empty string.
        legendLabel
            A String specifying the label to be used in the legend. The default value is the name of
            the XYData object.
        skipFrequency
            An Int specifying how often data frames will be skipped. If **skipFrequency** = 1, Abaqus
            will skip every other frame. The first frame is always read. Possible values are
            **skipFrequency** ≥ 0. The default value is 0 (data are read from every frame).
        numericForm
            A SymbolicConstant specifying the numeric form in which to display results that contain
            complex numbers. Possible values are COMPLEX_MAGNITUDE, COMPLEX_PHASE, REAL, IMAGINARY,
            and COMPLEX_VAL_AT_ANGLE. The default value is REAL.
        complexAngle
            A Float specifying the angle (in degrees) at which to display results that contain
            complex numbers when **numericForm** = COMPLEX_VAL_AT_ANGLE. The default value is 0.
        stepTuple
            A tuple of Integers specifying the steps to include when extracting data.

        Returns
        -------
        XYData
            An :py:class:`~abaqus.XY.XYData.XYData` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.xyDataObjects[name] = xyData = XYData(())
        return xyData

    @abaqus_method_doc
    def xyDataListFromField(
        self,
        odb: Odb,
        outputPosition: Literal[
            C.ELEMENT_CENTROID, C.ELEMENT_NODAL, C.INTEGRATION_POINT, C.NODAL
        ],
        variable: Tuple[
            Tuple[
                str,
                Literal[
                    C.ELEMENT_CENTROID,
                    C.ELEMENT_FACE,
                    C.ELEMENT_NODAL,
                    C.GENERAL_PARTICLE,
                    C.INTEGRATION_POINT,
                    C.NODAL,
                    C.WHOLE_ELEMENT,
                    C.WHOLE_MODEL,
                    C.WHOLE_PART_INSTANCE,
                    C.WHOLE_REGION,
                ],
                Tuple[Tuple[Literal[C.INVARIANT, C.COMPONENT], str], ...],
            ]
        ],
        elementSets: Union[Sequence[str], str] = ...,
        elementLabels: Sequence[Tuple[str, Union[int, str]]] = ...,
        nodeSets: Union[str, Sequence[str]] = ...,
        nodeLabels: Sequence[Tuple[str, Union[int, str]]] = ...,
        numericForm: Literal[
            C.COMPLEX_MAGNITUDE, C.COMPLEX_PHASE, C.REAL, C.IMAGINARY, C.COMPLEX_VAL_AT_ANGLE
        ] = REAL,
        complexAngle: float = 0,
        operator: Literal[
            C.ADD,
            C.SUBTRACT,
            C.MULTIPLY,
            C.DIVIDE,
            C.POWER,
            C.MINIMUM,
            C.MAXIMUM,
            C.AVERAGE,
            C.RANGE,
            C.SRSS,
            C.ABSOLUTE,
            C.UNARY_NEGATIVE,
            C.COSINE,
            C.HYPERBOLIC_COSINE,
            C.INVERSE_COSINE,
            C.SINE,
            C.HYPERBOLIC_SINE,
            C.INVERSE_SINE,
            C.TANGENT,
            C.HYPERBOLIC_TANGENT,
            C.INVERSE_TANGENT,
            C.EXPONENTIAL,
            C.NATURAL_LOG,
            C.LOG,
            C.SQUARE_ROOT,
            C.NORMALIZE,
            C.DEG2RAD,
            C.RAD2DEG,
            C.SMOOTH,
            C.SWAP,
            C.AVERAGE_ALL,
            C.MAXIMUM_ENVELOPE,
            C.MINIMUM_ENVELOPE,
            C.RANGE_ALL,
        ] = ...,
    ) -> List[XYData]:
        """This method creates a list of XYData objects by reading field data from an Odb object.

        .. note:: 
            This function can be accessed by::

                session.xyDataListFromField
                xyPlot.xyDataListFromField

        Parameters
        ----------
        odb
            An :py:class:`~abaqus.Odb.Odb.Odb` object specifying the output database from which data will be read.
        outputPosition
            A SymbolicConstant specifying the position from which output will be read. Possible
            values are ELEMENT_CENTROID, ELEMENT_NODAL, INTEGRATION_POINT, and NODAL.
        variable
            A tuple of tuples containing the descriptions of variables for which to extract data
            from the field. Each tuple specifies the following: 
            
            * Variable label: A String specifying the variable; for example, 'U'.
            * Variable output position: A SymbolicConstant specifying the output position. Possible values are
              ELEMENT_CENTROID, ELEMENT_FACE, ELEMENT_NODAL, GENERAL_PARTICLE, INTEGRATION_POINT, NODAL,
              WHOLE_ELEMENT,  WHOLE_MODEL, WHOLE_PART_INSTANCE, and WHOLE_REGION.
            * Refinement: A tuple specifying the refinement. If the refinement tuple is omitted, data are
              written  for all components and invariants (if applicable). This element is required if the
              location dictionary (the following element in the tuple) is included. The refinement tuple
              contains the following: 
              
              * Type: A SymbolicConstant specifying the type of refinement. Possible values are INVARIANT and
                COMPONENT.
              * Label: A String specifying the invariant or the component; for example, 'Mises' or 'S22'.
              
            * Location: An optional Dictionary specifying the location. The dictionary contains pairs of the
              following:
              
              * A String specifying the category selection label.
              * A String specifying the section point label.
              
            For example::

                variable = ('S', INTEGRATION_POINT, ((COMPONENT, 'S22'), ), )
                variable = (('S', INTEGRATION_POINT, ((COMPONENT, 'S11'), ), ),
                            ('U', NODAL,((COMPONENT, 'U1'), )), )
                variable = (('S', INTEGRATION_POINT, ((INVARIANT, 'Mises'), ),
                             {'shell < STEEL > < 3 section points >': 'SNEG, (fraction = -1.0)', }), )

        elementSets
            A sequence of Strings specifying element sets or a String specifying a single element
            set.
        elementLabels
            A sequence of expressions specifying element labels per part instance in the model. Each
            part instance element expression is a sequence of a String specifying the part instance
            name and a sequence of element expressions; for example,
            `(('partInstance1',(1,'7','3:15;3'),), ('partInstance2','8'),))`. The element
            expressions can be any of the following:
            
            * An Int specifying a single element label; for example, `1`.
            * A String specifying a single element label; for example, `'7'`.
            * A String specifying a sequence of element labels; for example, `'3:5'` and `'3:15:3'`.
            
        nodeSets
            A sequence of Strings specifying node sets or a String specifying a single node set.
        nodeLabels
            A sequence of expressions specifying node labels per part instance in the model. Each
            part instance node expression is a sequence of a String specifying the part instance
            name and a sequence of node expressions; for example,
            `(('partInstance1',(1,'7','3:15;3'),), ('partInstance2','8'),))`. The node expressions
            can be any of the following:
            
            * An Int specifying a single node label; for example, `1`.A
            * String specifying a single node label; for example, `'7'`.
            * A String specifying a sequence of node labels; for example, `'3:5'` and `'3:15:3'`.
            
        numericForm
            A SymbolicConstant specifying the numeric form in which to display results that contain
            complex numbers. Possible values are COMPLEX_MAGNITUDE, COMPLEX_PHASE, REAL, IMAGINARY,
            and COMPLEX_VAL_AT_ANGLE. The default value is REAL.
        complexAngle
            A Float specifying the angle (in degrees) at which to display results that contain
            complex numbers when **numericForm** = COMPLEX_VAL_AT_ANGLE. The default value is 0.
        operator
            A SymbolicConstant specifying the mathematical, trigonometric, logarithmic, exponential,
            or other operations. Possible values are ADD, SUBTRACT, MULTIPLY, DIVIDE, POWER,
            MINIMUM, MAXIMUM, AVERAGE, RANGE, SRSS, ABSOLUTE, UNARY_NEGATIVE, COSINE,
            HYPERBOLIC_COSINE, INVERSE_COSINE, SINE, HYPERBOLIC_SINE, INVERSE_SINE, TANGENT,
            HYPERBOLIC_TANGENT, INVERSE_TANGENT, EXPONENTIAL, NATURAL_LOG, LOG, SQUARE_ROOT,
            NORMALIZE, DEG2RAD, RAD2DEG, SMOOTH, SWAP, AVERAGE_ALL, MAXIMUM_ENVELOPE,
            MINIMUM_ENVELOPE, and RANGE_ALL. If no value is defined, no operation will be performed
            on the data, and the data will be saved as is.

        Returns
        -------
        List[XYData]
            A list of XYData objects.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.xyDataObjects["name"] = xyData = XYData(())
        return [xyData]

    @abaqus_method_doc
    def XYDataFromFreeBody(
        self,
        odb: Odb,
        force: Boolean = ON,
        moment: Boolean = OFF,
        heatFlowRate: Boolean = OFF,
        resultant: Boolean = ON,
        comp1: Boolean = OFF,
        comp2: Boolean = OFF,
        comp3: Boolean = OFF,
    ) -> List[XYData]:
        """This method creates a list of XYData objects by computing free body data from an Odb
        object.

        .. note:: 
            This function can be accessed by::

                session.XYDataFromFreeBody
                xyPlot.XYDataFromFreeBody

        Parameters
        ----------
        odb
            An :py:class:`~abaqus.Odb.Odb.Odb` object specifying the output database from which data will be read.
        force
            A boolean indicating whether to compute the force. The default is ON.
        moment
            A boolean indicating whether to compute the moment. The default is OFF.
        heatFlowRate
            A boolean indicating whether to compute the heat flow rate resultant magnitude. It is
            extracted only for viewcut based freebodies. The default is OFF.
        resultant
            A boolean indicating whether to compute the resultant. It applies only to **force** and
            **moment**. The default is ON.
        comp1
            A boolean indicating whether to compute the first component. It applies only to **force**
            and **moment**. The default is OFF.
        comp2
            A boolean indicating whether to compute the second component. It applies only to **force**
            and **moment**. The default is OFF.
        comp3
            A boolean indicating whether to compute the third component. It applies only to **force**
            and **moment**. The default is OFF.

        Returns
        -------
        List[XYData]
            A list of XYData objects.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.xyDataObjects["name"] = xyData = XYData(())
        return [xyData]

    @abaqus_method_doc
    def XYDataFromShellThickness(
        self,
        odb: Odb,
        outputPosition: Literal[
            C.ELEMENT_CENTROID, C.ELEMENT_NODAL, C.INTEGRATION_POINT, C.NODAL
        ],
        variable: Tuple[
            Tuple[
                C.str,
                Literal[
                    C.ELEMENT_CENTROID,
                    C.ELEMENT_FACE,
                    C.ELEMENT_NODAL,
                    C.GENERAL_PARTICLE,
                    C.INTEGRATION_POINT,
                    C.NODAL,
                    C.WHOLE_ELEMENT,
                    C.WHOLE_MODEL,
                    C.WHOLE_PART_INSTANCE,
                    C.WHOLE_REGION,
                ],
                Tuple[Literal[C.INVARIANT, C.COMPONENT], str],
                Dict[str, str],
            ],
            ...,
        ],
        elementSets: Union[str, Sequence[str]] = ...,
        elementLabels: Sequence[Tuple[str, Union[int, str]]] = (),
        nodeSets: Union[str, Sequence[str]] = (),
        nodeLabels: Sequence[Tuple[str, Union[int, str]]] = (),
        numericForm: Literal[
            C.COMPLEX_MAGNITUDE, C.COMPLEX_PHASE, C.REAL, C.IMAGINARY, C.COMPLEX_VAL_AT_ANGLE
        ] = REAL,
        complexAngle: float = 0,
    ) -> List[XYData]:
        """This method creates a list of XYData objects by reading through the thickness field data
        from an Odb object.

        .. note:: 
            This function can be accessed by::

                session.XYDataFromShellThickness
                xyPlot.XYDataFromShellThickness

        Parameters
        ----------
        odb
            An :py:class:`~abaqus.Odb.Odb.Odb` object specifying the output database from which data will be read.
        outputPosition
            A SymbolicConstant specifying the position from which output will be read. Possible
            values are ELEMENT_CENTROID, ELEMENT_NODAL, INTEGRATION_POINT, and NODAL.
        variable
            A tuple of tuples containing the descriptions of variables for which to extract data from the
            field. Each tuple specifies the following:
            
            * Variable label: A String specifying the variable; for example, 'U'.
            * Variable output position: A SymbolicConstant specifying
              the output position. Possible values are ELEMENT_CENTROID, ELEMENT_FACE, ELEMENT_NODAL,
              GENERAL_PARTICLE, INTEGRATION_POINT, NODAL, WHOLE_ELEMENT, WHOLE_MODEL, WHOLE_PART_INSTANCE, and
              WHOLE_REGION.
            * Refinement: A tuple specifying the refinement. If
              the refinement tuple is omitted, data are written for all components and invariants (if
              applicable). This element is required if the location dictionary (the following element in the
              tuple) is included. The refinement tuple contains the following:
              
              * Type: A SymbolicConstant specifying the type of refinement. Possible values are INVARIANT and COMPONENT.
              * Label: A String specifying the invariant or the component; for example, 'Mises' or 'S22'.
              
            * Location: An optional Dictionary specifying the location. The
              dictionary contains pairs of the following:
              
              * A String specifying the category selection label.
              * A String specifying the section point label.
              
            For example::

                variable = ('S', INTEGRATION_POINT, ((COMPONENT, 'S22'), ), )
                variable = (('S', INTEGRATION_POINT, ((COMPONENT, 'S11'), ), ),
                            ('U', NODAL,((COMPONENT, 'U1'), )), )
                variable = (('S', INTEGRATION_POINT, ((INVARIANT, 'Mises'), ),
                             {'shell < STEEL > < 3 section points >': 'SNEG, (fraction = -1.0)', }), )
        elementSets
            A sequence of Strings specifying element sets or a String specifying a single element
            set.
        elementLabels
            A sequence of expressions specifying element labels per part instance in the model. Each
            part instance element expression is a sequence of a String specifying the part instance
            name and a sequence of element expressions; for example,
            `(('partInstance1',(1,'7','3:15;3'),), ('partInstance2','8'),))`. The element
            expressions can be any of the following:

            * An Int specifying a single element label; for example, `1`.
            * A String specifying a single element label; for example, `'7'`.
            * A String specifying a sequence of element labels; for example, `'3:5'` and `'3:15:3'`.

        nodeSets
            A sequence of Strings specifying node sets or a String specifying a single node set.
        nodeLabels
            A sequence of expressions specifying node labels per part instance in the model. Each
            part instance node expression is a sequence of a String specifying the part instance
            name and a sequence of node expressions; for example,
            `(('partInstance1',(1,'7','3:15;3'),), ('partInstance2','8'),))`. The node expressions
            can be any of the following:
            
            * An Int specifying a single node label; for example, `1`.
            * A String specifying a single node label; for example, `'7'`.
            * A String specifying a sequence of node labels; for example, `'3:5'` and `'3:15:3'`.
            
        numericForm
            A SymbolicConstant specifying the numeric form in which to display results that contain
            complex numbers. Possible values are COMPLEX_MAGNITUDE, COMPLEX_PHASE, REAL, IMAGINARY,
            and COMPLEX_VAL_AT_ANGLE. The default value is REAL.
        complexAngle
            A Float specifying the angle (in degrees) at which to display results that contain
            complex numbers when **numericForm** = COMPLEX_VAL_AT_ANGLE. The default value is 0.

        Returns
        -------
        List[XYData]
            A list of XYData objects.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.xyDataObjects["name"] = xyData = XYData(())
        return [xyData]

    @abaqus_method_doc
    def XYDataFromPath(
        self,
        path: Path,
        name: str,
        includeIntersections: Boolean = False,
        shape: Literal[C.UNDEFORMED, C.DEFORMED] = ...,
        pathStyle: Literal[C.PATH_POINTS, C.UNIFORM_SPACING] = ...,
        numIntervals: int = 10,
        labelType: Literal[
            C.NORM_DISTANCE,
            C.SEQ_ID,
            C.TRUE_DISTANCE,
            C.TRUE_DISTANCE_X,
            C.TRUE_DISTANCE_Y,
            C.TRUE_DISTANCE_Z,
            C.X_COORDINATE,
            C.Y_COORDINATE,
            C.Z_COORDINATE,
        ] = ...,
        viewport: str = ...,
        removeDuplicateXYPairs: Boolean = True,
        includeAllElements: Boolean = False,
        step: int = ...,
        frame: int = ...,
        variable: Tuple[
            Tuple[
                str,
                Literal[
                    C.ELEMENT_CENTROID,
                    C.ELEMENT_FACE,
                    C.ELEMENT_NODAL,
                    C.GENERAL_PARTICLE,
                    C.INTEGRATION_POINT,
                    C.NODAL,
                    C.WHOLE_ELEMENT,
                    C.WHOLE_MODEL,
                    C.WHOLE_PART_INSTANCE,
                    C.WHOLE_REGION,
                ],
                Tuple[Literal[C.INVARIANT, C.COMPONENT], str],
                Dict[str, str],
            ],
            ...,
        ] = ...,
        deformedMag: Tuple[float, float, float] = (1, 1, 1),
        numericForm: Literal[
            C.COMPLEX_MAGNITUDE, C.COMPLEX_PHASE, C.REAL, IMAGINARY, COMPLEX_VAL_AT_ANGLE
        ] = REAL,
        complexAngle: float = 0,
        projectOntoMesh: Boolean = False,
        projectionTolerance: float = 0,
    ) -> XYData:
        """This method creates an XYData object from path information.

        .. note:: 
            This function can be accessed by::

                session.XYDataFromPath
                xyPlot.XYDataFromPath

        Parameters
        ----------
        path
            A :py:class:`~abaqus.PathAndProbe.Path.Path` object to use in **X - Y** data generation.
        name
            A String specifying the repository key:for **session** 'name' is required argument and for
            **xyPlot** 'name' is optional argument.
        includeIntersections
            A Boolean specifying whether to include **X - Y** data for the intersections between the
            path and element faces or edges. The default value is False.
        shape
            A SymbolicConstant specifying the model shape to use. Possible values are UNDEFORMED and
            DEFORMED.
        pathStyle
            A SymbolicConstant specifying the path style. Possible values are PATH_POINTS and
            UNIFORM_SPACING.
        numIntervals
            An Int specifying the number of uniform-spacing intervals. The default value is 10.
        labelType
            A SymbolicConstant specifying the **X** label type to use. Possible values are
            NORM_DISTANCE, SEQ_ID, TRUE_DISTANCE, TRUE_DISTANCE_X, TRUE_DISTANCE_Y, TRUE_DISTANCE_Z,
            X_COORDINATE, Y_COORDINATE and Z_COORDINATE.
        viewport
            A String specifying the viewport name or an Int specifying the viewport id from which to
            obtain values. The default is the current viewport.
        step
            An Int identifying the step from which to obtain values. The default value is the
            current step.
        frame
            An Int identifying the frame from which to obtain values. The default value is the
            current frame.
        variable
            A tuple of tuples containing the descriptions of variables for which to extract data
            along the path. The default value is the current variable. Each tuple specifies the
            following:
            
            * Variable label: A String specifying the variable; for example, 'U'.
            * Variable output position: A SymbolicConstant specifying the output position. Possible values are
              ELEMENT_CENTROID, ELEMENT_FACE, ELEMENT_NODAL, GENERAL_PARTICLE, INTEGRATION_POINT,
              NODAL, WHOLE_ELEMENT, WHOLE_MODEL, WHOLE_PART_INSTANCE, and WHOLE_REGION.
            * Refinement: A tuple specifying the refinement. If the refinement tuple is omitted, data are written
              for all components and invariants (if applicable). This element is required if the
              location dictionary (the following element in the tuple) is included. The refinement
              tuple contains the following:
                
              * Type: A SymbolicConstant specifying the type of refinement. Possible values are INVARIANT
                and COMPONENT.
              * Label: A String specifying the invariant or the component; for example, 'Mises' or 'S22'.
            
            * Location: An optional Dictionary specifying the location. The dictionary contains pairs of the
              following:
              
              * A String specifying the category selection label.
              * A String specifying the section point label.
            
            For example::

                variable = ('S', INTEGRATION_POINT, ((COMPONENT, 'S22'), ), )
                variable = (('S', INTEGRATION_POINT, ((COMPONENT, 'S11'), ), ),
                            ('U', NODAL,((COMPONENT, 'U1'), )), )
                variable = (('S', INTEGRATION_POINT, ((INVARIANT, 'Mises'), ),
                             {'shell < STEEL > < 3 section points >': 'SNEG, (fraction = -1.0)', }), )
        deformedMag
            A tuple of three Floats specifying the deformation magnitude in the *X-*, *Y-*, and
            *Z-* planes. The default value is (1, 1, 1).
        numericForm
            A SymbolicConstant specifying the numeric form in which to display results that contain
            complex numbers. Possible values are COMPLEX_MAGNITUDE, COMPLEX_PHASE, REAL, IMAGINARY,
            and COMPLEX_VAL_AT_ANGLE. The default value is REAL.
        complexAngle
            A Float specifying the angle (in degrees) at which to display results that contain
            complex numbers when **numericForm** = COMPLEX_VAL_AT_ANGLE. The default value is 0.
        projectOntoMesh
            A Boolean to specify whether to consider the data points that do not lie on or inside
            the mesh. The default value is False.
        projectionTolerance
            A Float specifying the tolerance value for the projected distance considered for the
            data extraction when **projectOntoMesh** =  True. The default value is 0.

        Returns
        -------
        If **variable** specified has one fieldoutput: Returns an XYData object.
        If **variable** specified has more than one fieldoutputs: Returns list of XYData objects.

        Raises
        ------
        ErrorPathNotFound: Path not found
            If **path** is invalid.
        ErrorCurrentVPNotFound: Current viewport not found
            If **viewport** is invalid.
        ErrorInvalidUserStepAndFrame: The user step and frame specified have not been defined
            If **step** and/or **frame** are invalid.
        ErrorNoVarInPathExtract: No variable selection for XY data extraction from path
            If the **variable** argument is empty.
        ErrorUnavailableSelectedVariable: The selected variable is not available for the current frame
            If the specified output variable is not available in the output database.
        ErrorUnusableVarInPathExtract: Specified variable cannot be used in XY data extraction
            If the specified output variable cannot be used to obtain **X - Y** data from path.
        ErrorUnsupportedRefinementType: Unsupported refinement type
            If the SymbolicConstant specifying the refinement type is invalid.
        ErrorInvalidRefinementSpecification: Invalid refinement specification
            If the label specifying the refinement invariant or component is invalid.
        ErrorDeformedMagTupleInPathExtract: Deformed magnification tuple must contain X, Y and Z values
            If **deformedMag** does not contain three Floats.
        """
        self.xyDataObjects[name] = xyData = XYData(())
        return xyData
