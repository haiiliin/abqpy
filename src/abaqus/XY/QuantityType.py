from typing import Literal
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class QuantityType:
    """The QuantityType object is used to store attributes defining the physical dimension and
    label of the quantity type to be associated with an XYData or an AxisData object.
    QuantityType objects are automatically created when creating XYData objects from the
    odb.
    QuantityType objects can be created using the methods described below.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.charts[name].axes1[i].axisData.curves[i].data.axis1QuantityType
            session.charts[name].axes1[i].axisData.curves[i].data.axis2QuantityType
            session.charts[name].axes1[i].axisData.quantityType
            session.charts[name].axes2[i].axisData.curves[i].data.axis1QuantityType
            session.charts[name].axes2[i].axisData.curves[i].data.axis2QuantityType
            session.charts[name].axes2[i].axisData.quantityType
            session.charts[name].curves[name].data.axis1QuantityType
            session.charts[name].curves[name].data.axis2QuantityType
            session.curves[name].data.axis1QuantityType
            session.curves[name].data.axis2QuantityType
            session.defaultChartOptions.defaultAxis1Options.axisData.curves[i].data.axis1QuantityType
            session.defaultChartOptions.defaultAxis1Options.axisData.curves[i].data.axis2QuantityType
            session.defaultChartOptions.defaultAxis1Options.axisData.quantityType
            session.defaultChartOptions.defaultAxis2Options.axisData.curves[i].data.axis1QuantityType
            session.defaultChartOptions.defaultAxis2Options.axisData.curves[i].data.axis2QuantityType
            session.defaultChartOptions.defaultAxis2Options.axisData.quantityType
            import odbAccess
            session.odbs[name].userData.axis1QuantityType
            session.odbs[name].userData.axis2QuantityType
            import visualization
            import xyPlot
            session.odbs[name].userData.xyDataObjects[name].axis1QuantityType
            session.odbs[name].userData.xyDataObjects[name].axis2QuantityType
            session.xyDataObjects[name].axis1QuantityType
            session.xyDataObjects[name].axis2QuantityType
            session.xyPlots[name].charts[name].axes1[i].axisData.curves[i].data.axis1QuantityType
            session.xyPlots[name].charts[name].axes1[i].axisData.curves[i].data.axis2QuantityType
            session.xyPlots[name].charts[name].axes1[i].axisData.quantityType
            session.xyPlots[name].charts[name].axes2[i].axisData.curves[i].data.axis1QuantityType
            session.xyPlots[name].charts[name].axes2[i].axisData.curves[i].data.axis2QuantityType
            session.xyPlots[name].charts[name].axes2[i].axisData.quantityType
            session.xyPlots[name].charts[name].curves[name].data.axis1QuantityType
            session.xyPlots[name].charts[name].curves[name].data.axis2QuantityType
            session.xyPlots[name].curves[name].data.axis1QuantityType
            session.xyPlots[name].curves[name].data.axis2QuantityType
    """

    #: A String specifying the label for this quantity type.
    label: str = ""

    #: A SymbolicConstant specifying the physical dimension of the axis. Possible values are:
    #:
    #: - NONE.
    #: - ACCELERATION.
    #: - ACOUSTIC_INTENSITY.
    #: - ANGLE.
    #: - ANGULAR_MOMENTUM.
    #: - ARC_LENGTH.
    #: - AREA.
    #: - AREA_VELOCITY_SQUARED, specifying "Velocity squared per area".
    #: - BIMOMENT.
    #: - CURVATURE.
    #: - CORIOLIS_LOAD.
    #: - DAMAGE.
    #: - DAMAGE_CRITERION.
    #: - DENSITY.
    #: - DENSITY_ROTATIONAL_ACCELERATION, specifying "Density * Angular acceleration".
    #: - DISPLACEMENT.
    #: - ECURRENT_AREA_TIME, specifying "Time integrated electric current per area".
    #: - ELECTRIC_CHARGE.
    #: - ELECTRIC_CURRENT.
    #: - ELECTRIC_CURRENT_AREA, specifying "Electric current per unit area".
    #: - ELECTRIC_POTENTIAL.
    #: - ENERGY.
    #: - ENERGY_DENSITY.
    #: - ENERGY_RELEASE_RATE.
    #: - EPOTENTIAL_GRADIENT, specifying "Electric potential gradient".
    #: - FREQUENCY.
    #: - FORCE.
    #: - FORCE_VOLUME, specifying "Force per volume".
    #: - HEAT_FLUX.
    #: - HEAT_FLUX_AREA, specifying "Heat flux per area".
    #: - HEAT_FLUX_RATE.
    #: - HEAT_FLUX_VOLUME, specifying "Heat flux per volume".
    #: - LENGTH.
    #: - LINEAR_PRESSURE.
    #: - LUMIN, specifying "Luminous intensity".
    #: - MASS.
    #: - MASS_FLOW_AREA, specifying "Mass flow per area".
    #: - MASS_FLOW_AREA_RATE, specifying "Mass flow rate per area".
    #: - MASS_FLOW_RATE.
    #: - MODE_NUMBER.
    #: - MOMENT.
    #: - NUMBER.
    #: - PATH.
    #: - PHASE.
    #: - POSITION.
    #: - PRESSURE.
    #: - PRESSURE_GRADIENT.
    #: - RATE.
    #: - ROTARY_INERTIA.
    #: - ROTATIONAL_ACCELERATION.
    #: - ROTATIONAL_VELOCITY.
    #: - STATUS.
    #: - STRAIN.
    #: - STRAIN_RATE.
    #: - STRESS.
    #: - STRESS_INTENS_FACTOR, specifying "Stress intensity factor".
    #: - SUBSTANCE, specifying "Amount of substance".
    #: - TEMPERATURE.
    #: - THICKNESS.
    #: - TIME.
    #: - TIME_INCREMENT.
    #: - TIME_HEAT_FLUX, specifying "Time integrated heat flux".
    #: - TIME_HEAT_FLUX_AREA, specifying "Time integrated heat flux per area".
    #: - TIME_VOLUME, specifying "Time integrated volume".
    #: - TIME_VOLUME_FLUX, specifying "Time integrated volume flux per area".
    #: - TWIST.
    #: - VELOCITY.
    #: - VELOCITY_SQUARED.
    #: - VOLUME.
    #: - VOLUME_FLUX.
    #: - VOLUME_FLUX_AREA, specifying "Volume flux per area".
    #: - VOLUME_FRACTION.
    #:
    #: The default value is NONE
    type: Literal[
        NONE,
        ACCELERATION,
        ACOUSTIC_INTENSITY,
        ANGLE,
        ANGULAR_MOMENTUM,
        ARC_LENGTH,
        AREA,
        AREA_VELOCITY_SQUARED,
        BIMOMENT,
        CURVATURE,
        CORIOLIS_LOAD,
        DAMAGE,
        DAMAGE_CRITERION,
        DENSITY,
        DENSITY_ROTATIONAL_ACCELERATION,
        DISPLACEMENT,
        ECURRENT_AREA_TIME,
        ELECTRIC_CHARGE,
        ELECTRIC_CURRENT,
        ELECTRIC_CURRENT_AREA,
        ELECTRIC_POTENTIAL,
        ENERGY,
        ENERGY_DENSITY,
        ENERGY_RELEASE_RATE,
        EPOTENTIAL_GRADIENT,
        FREQUENCY,
        FORCE,
        FORCE_VOLUME,
        HEAT_FLUX,
        HEAT_FLUX_AREA,
        HEAT_FLUX_RATE,
        HEAT_FLUX_VOLUME,
        LENGTH,
        LINEAR_PRESSURE,
        LUMIN,
        MASS,
        MASS_FLOW_AREA,
        MASS_FLOW_AREA_RATE,
        MASS_FLOW_RATE,
        MODE_NUMBER,
        MOMENT,
        NUMBER,
        PATH,
        PHASE,
        POSITION,
        PRESSURE,
        PRESSURE_GRADIENT,
        RATE,
        ROTARY_INERTIA,
        ROTATIONAL_ACCELERATION,
        ROTATIONAL_VELOCITY,
        STATUS,
        STRAIN,
        STRAIN_RATE,
        STRESS,
        STRESS_INTENS_FACTOR,
        SUBSTANCE,
        TEMPERATURE,
        THICKNESS,
        TIME,
        TIME_INCREMENT,
        TIME_HEAT_FLUX,
        TIME_HEAT_FLUX_AREA,
        TIME_VOLUME,
        TIME_VOLUME_FLUX,
        TWIST,
        VELOCITY,
        VELOCITY_SQUARED,
        VOLUME,
        VOLUME_FLUX,
        VOLUME_FLUX_AREA,
        VOLUME_FRACTION,
    ] = NONE

    @abaqus_method_doc
    def __init__(
        self,
        label: str = "",
        type: Literal[
            NONE,
            ACCELERATION,
            ACOUSTIC_INTENSITY,
            ANGLE,
            ANGULAR_MOMENTUM,
            ARC_LENGTH,
            AREA,
            AREA_VELOCITY_SQUARED,
            BIMOMENT,
            CURVATURE,
            CORIOLIS_LOAD,
            DAMAGE,
            DAMAGE_CRITERION,
            DENSITY,
            DENSITY_ROTATIONAL_ACCELERATION,
            DISPLACEMENT,
            ECURRENT_AREA_TIME,
            ELECTRIC_CHARGE,
            ELECTRIC_CURRENT,
            ELECTRIC_CURRENT_AREA,
            ELECTRIC_POTENTIAL,
            ENERGY,
            ENERGY_DENSITY,
            ENERGY_RELEASE_RATE,
            EPOTENTIAL_GRADIENT,
            FREQUENCY,
            FORCE,
            FORCE_VOLUME,
            HEAT_FLUX,
            HEAT_FLUX_AREA,
            HEAT_FLUX_RATE,
            HEAT_FLUX_VOLUME,
            LENGTH,
            LINEAR_PRESSURE,
            LUMIN,
            MASS,
            MASS_FLOW_AREA,
            MASS_FLOW_AREA_RATE,
            MASS_FLOW_RATE,
            MODE_NUMBER,
            MOMENT,
            NUMBER,
            PATH,
            PHASE,
            POSITION,
            PRESSURE,
            PRESSURE_GRADIENT,
            RATE,
            ROTARY_INERTIA,
            ROTATIONAL_ACCELERATION,
            ROTATIONAL_VELOCITY,
            STATUS,
            STRAIN,
            STRAIN_RATE,
            STRESS,
            STRESS_INTENS_FACTOR,
            SUBSTANCE,
            TEMPERATURE,
            THICKNESS,
            TIME,
            TIME_INCREMENT,
            TIME_HEAT_FLUX,
            TIME_HEAT_FLUX_AREA,
            TIME_VOLUME,
            TIME_VOLUME_FLUX,
            TWIST,
            VELOCITY,
            VELOCITY_SQUARED,
            VOLUME,
            VOLUME_FLUX,
            VOLUME_FLUX_AREA,
            VOLUME_FRACTION,
        ] = NONE,
    ):
        """This method creates a QuantityType object.

        .. note:: 
            This function can be accessed by::

                session.QuantityType
                xyPlot.QuantityType

        Parameters
        ----------
        label
            A String specifying the label for this quantity type.
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
            
            The default value is NONE

        Returns
        -------
        QuantityType
            A :py:class:`~abaqus.XY.QuantityType.QuantityType` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the QuantityType object."""
        ...
