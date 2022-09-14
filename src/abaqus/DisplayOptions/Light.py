from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class Light:
    """The Light object stores settings that control how objects are lit when the **renderStyle**
    is set to SHADED.
    The Light object has no constructor; Abaqus creates them as part of the
    **defaultLightOptions** and the **lightOptions** objects when a session is started.

    .. note::
        This object can be accessed by::

            session.defaultLightOptions.lights[i]
            session.viewports[name].lightOptions.lights[i]
    """

    @abaqus_method_doc
    def setValues(
        self,
        enabled: Boolean = OFF,
        type: SymbolicConstant = DIRECTIONAL,
        latitude: float = 0,
        longitude: float = 0,
        diffuseColor: str = "",
        specularColor: str = "",
    ):
        """This method modifies the Light object.

        Parameters
        ----------
        enabled
            A Boolean specifying whether the light is on or off. The default value is OFF.
        type
            A SymbolicConstant specifying how the effect of the light should be calculated. Possible
            values are:DIRECTIONAL, specifying a constant vector should be used for the direction
            from the light to a vertex.POINT, specifying the vector from the light to each vertex
            should be calculated.The default value is DIRECTIONAL.When set to **type** =DIRECTIONAL, a
            constant vector is used for the direction from the light to a vertex. When **type**
            =POINT, the result is more realistic because the actual vector from the light to each
            vertex is calculated. However, overall performance is decreased.
        latitude
            A Float specifying the altitude of the light above or below the camera. Possible values
            are -90.0 ≤ **latitude** ≤ 90.0. The default value is 0.0.
        longitude
            A Float specifying the east/west position of the light to the left or right of the
            camera. Possible values are -90.0 ≤ **longitude** ≤ 90.0. The default value is 0.0.
        diffuseColor
            A String specifying the color of the light added to the scene by this light source. The
            initial value is 70% gray. A list of valid color strings is in the **colors** map in the
            **session** object.
        specularColor
            A String specifying the color of the specular highlights created by this light source.
            The initial value is 36% gray. A list of valid color strings is in the **colors** map in
            the **session** object.

        Raises
        ------
        RangeError
        """
        ...
