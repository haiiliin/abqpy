from __future__ import annotations

from typing import overload, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .AreaStyle import AreaStyle
from .LineStyle import LineStyle
from .QuantityType import QuantityType
from .SymbolStyle import SymbolStyle
from .TextStyle import TextStyle
from .XYData import XYData
from .XYPlotBase import XYPlotBase
from ..UtilityAndView.abaqusConstants import Boolean, FILLED_CIRCLE, ON, SOLID, SymbolicConstant


@abaqus_class_doc
class XYPlot(XYPlotBase):
    
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
        style: SymbolicConstant = SOLID,
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
    def QuantityType(type: SymbolicConstant, label: str = "") -> QuantityType:
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
        marker: SymbolicConstant = FILLED_CIRCLE,
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
        axis1QuantityType: Optional[QuantityType] = None,
        axis2QuantityType: Optional[QuantityType] = None,
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
    def XYData(*args, **kwargs) -> XYData:
        return XYData(())
