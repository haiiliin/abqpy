from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import ON, Boolean


@abaqus_class_doc
class BCDisplayOptions:
    """The BCDisplayOptions object stores settings that specify how assemblies are to be displayed in a
    particular viewport when session.viewports[name].assemblyDisplay.bcs=ON The BCDisplayOptions object has no
    constructor. When you create a new viewport, the settings are copied from the current viewport.

    .. note::
        This object can be accessed by::

            session.viewports[name].assemblyDisplay.bcOptions
            session.viewports[name].layers[name].assemblyDisplay.bcOptions
    """

    @abaqus_method_doc
    def setValues(
        self,
        displacement: Boolean = ON,
        velocity: Boolean = ON,
        acceleration: Boolean = ON,
        symmetry: Boolean = ON,
        antiSymmetry: Boolean = ON,
        temperature: Boolean = ON,
        porePressure: Boolean = ON,
        fluidCavityPressure: Boolean = ON,
        acousticPressure: Boolean = ON,
        electricPotential: Boolean = ON,
        concentration: Boolean = ON,
        encastre: Boolean = ON,
        pinned: Boolean = ON,
    ):
        """This method modifies the BCDisplayOptions object.

        Parameters
        ----------
        displacement
            A Boolean specifying whether displacement symbols are shown. The default value is ON.
        velocity
            A Boolean specifying whether velocity symbols are shown. The default value is ON.
        acceleration
            A Boolean specifying whether acceleration symbols are shown. The default value is ON.
        symmetry
            A Boolean specifying whether symmetry symbols are shown. The default value is ON.
        antiSymmetry
            A Boolean specifying whether anti- symmetry symbols are shown. The default value is ON.
        temperature
            A Boolean specifying whether temperature symbols are shown. The default value is ON.
        porePressure
            A Boolean specifying whether pore pressure symbols are shown. The default value is ON.
        fluidCavityPressure
            A Boolean specifying whether fluid cavity pressure symbols are shown. The default value
            is ON.
        acousticPressure
            A Boolean specifying whether acoustic pressure symbols are shown. The default value is
            ON.
        electricPotential
            A Boolean specifying whether electric potential symbols are shown. The default value is
            ON.
        concentration
            A Boolean specifying whether concentration mass diffusion symbols are shown. The default
            value is ON.
        encastre
            A Boolean specifying whether encastre symbols are shown. The default value is ON.
        pinned
            A Boolean specifying whether pinned symbols are shown. The default value is ON.
        """
        ...
