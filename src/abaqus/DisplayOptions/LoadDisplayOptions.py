from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import ON


@abaqus_class_doc
class LoadDisplayOptions:
    """The LoadDisplayOptions object stores settings that specify how assemblies are to be
    displayed in a particular viewport when
    session.viewports[name].assemblyDisplay.loads=ON
    The LoadDisplayOptions object has no constructor. When you create a new viewport, the
    settings are copied from the current viewport.

    .. note::
        This object can be accessed by::

            session.viewports[name].assemblyDisplay.loadOptions
            session.viewports[name].layers[name].assemblyDisplay.loadOptions
    """

    @abaqus_method_doc
    def setValues(
        self,
        concentratedForce: str = ON,
        moment: str = ON,
        pressure: str = ON,
        pipePressure: str = ON,
        bodyForce: str = ON,
        lineLoad: str = ON,
        gravity: str = ON,
        boltLoad: str = ON,
        pegLoad: str = ON,
        connectorForce: str = ON,
        connectorMoment: str = ON,
        inertiaRelief: str = ON,
        rotationalIntertiaLoad: str = ON,
        coriolisForce: str = ON,
        bodyHeatFlux: str = ON,
        surfaceHeatFlux: str = ON,
        concentratedHeatFlux: str = ON,
        concentratedPoreFluid: str = ON,
        surfacePoreFluid: str = ON,
        hydroFluidFlow: str = ON,
        concentratedCharge: str = ON,
        concentratedCurrent: str = ON,
        surfaceCharge: str = ON,
        surfaceCurrent: str = ON,
        bodyCharge: str = ON,
        bodyCurrent: str = ON,
        inwardVolAccel: str = ON,
        bodyConcentrationFlux: str = ON,
        surfaceConcentrationFlux: str = ON,
        concentratedConcentrationFlux: str = ON,
    ):
        """This method modifies the LoadDisplayOptions object.
        
        Parameters
        ----------
        concentratedForce
            A Boolean specifying whether concentrated force symbols are shown. The default value
            is ON.
        moment
            A Boolean specifying whether moment symbols are shown. The default value is ON.
        pressure
            A Boolean specifying whether pressure symbols are shown. The default value is ON.
        pipePressure
            A Boolean specifying whether pipe pressure symbols are shown. The default value is
            ON.
        bodyForce
            A Boolean specifying whether body force symbols are shown. The default value is ON.
        lineLoad
            A Boolean specifying whether line load symbols are shown. The default value is ON.
        gravity
            A Boolean specifying whether gravity symbols are shown. The default value is ON.
        boltLoad
            A Boolean specifying whether bolt load symbols are shown. The default value is ON.
        pegLoad
            A Boolean specifying whether PEG load symbols are shown. The default value is ON.
        connectorForce
            A Boolean specifying whether connector force symbols are shown. The default value is
            ON.
        connectorMoment
            A Boolean specifying whether connector moment symbols are shown. The default value is
            ON.
        inertiaRelief
            A Boolean specifying whether inertia relief symbols are shown. The default value is
            ON.
        rotationalIntertiaLoad
            A Boolean specifying whether rotational inertia load symbols are shown. The default
            value is ON.
        coriolisForce
            A Boolean specifying whether coriolis force symbols are shown. The default value is
            ON.
        bodyHeatFlux
            A Boolean specifying whether body heat flux symbols are shown. The default value is
            ON.
        surfaceHeatFlux
            A Boolean specifying whether surface heat flux symbols are shown. The default value
            is ON.
        concentratedHeatFlux
            A Boolean specifying whether concentrated heat flux symbols are shown. The default
            value is ON.
        concentratedPoreFluid
            A Boolean specifying whether concentrated pore fluid symbols are shown. The default
            value is ON.
        surfacePoreFluid
            A Boolean specifying whether surface pore fluid symbols are shown. The default value
            is ON.
        hydroFluidFlow
            A Boolean specifying whether hydro fluid flow symbols are shown. The default value is
            ON.
        concentratedCharge
            A Boolean specifying whether concentrated charge symbols are shown. The default value
            is ON.
        concentratedCurrent
            A Boolean specifying whether concentrated current symbols are shown. The default
            value is ON.
        surfaceCharge
            A Boolean specifying whether surface charge symbols are shown. The default value is
            ON.
        surfaceCurrent
            A Boolean specifying whether surface current symbols are shown. The default value is
            ON.
        bodyCharge
            A Boolean specifying whether body charge symbols are shown. The default value is ON.
        bodyCurrent
            A Boolean specifying whether body current symbols are shown. The default value is ON.
        inwardVolAccel
            A Boolean specifying whether inward volume acceleration symbols are shown. The
            default value is ON.
        bodyConcentrationFlux
            A Boolean specifying whether body concentration flux symbols are shown. The default
            value is ON.
        surfaceConcentrationFlux
            A Boolean specifying whether surface concentration flux symbols are shown. The
            default value is ON.
        concentratedConcentrationFlux
            A Boolean specifying whether concentrated concentration flux symbols are shown. The
            default value is ON.

        Raises
        ------
        RangeError
        """
        ...
