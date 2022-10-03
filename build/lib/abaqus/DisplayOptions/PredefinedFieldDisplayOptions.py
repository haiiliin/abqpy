from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import Boolean, ON


@abaqus_class_doc
class PredefinedFieldDisplayOptions:
    """The PredefinedFieldDisplayOptions object stores settings that specify how assemblies are
    to be displayed in a particular viewport when
    session.viewports[name].assemblyDisplay.predefinedFields=ON
    The PredefinedFieldDisplayOptions object has no constructor. When you create a new
    viewport, the settings are copied from the current viewport.

    .. note::
        This object can be accessed by::

            session.viewports[name].assemblyDisplay.predefinedFieldOptions
            session.viewports[name].layers[name].assemblyDisplay.predefinedFieldOptions
    """

    @abaqus_method_doc
    def setValues(
        self,
        temperatureField: Boolean = ON,
        velocityField: Boolean = ON,
        generalField: Boolean = ON,
        stressField: Boolean = ON,
        hardeningField: Boolean = ON,
    ):
        """This method modifies the PredefinedFieldDisplayOptions object.

        Parameters
        ----------
        temperatureField
            A Boolean specifying whether temperature field symbols are shown. The default value is
            ON.
        velocityField
            A Boolean specifying whether translational velocity symbols are shown. The default value
            is ON.
        generalField
            A Boolean specifying whether general field symbols are shown. The default value is ON.
        stressField
            A Boolean specifying whether stress field symbols are shown. The default value is ON.
        hardeningField
            A Boolean specifying whether hardening field symbols are shown. The default value is ON.

        Raises
        ------
        RangeError
        """
        ...
