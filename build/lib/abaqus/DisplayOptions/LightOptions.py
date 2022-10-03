from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .LightArray import LightArray
from ..UtilityAndView.abaqusConstants import GOURAUD, INFINITE, SymbolicConstant


@abaqus_class_doc
class LightOptions:
    """The LightOptions object stores settings that control how objects are lit when the
    **renderStyle** is set to SHADED. LightOptions objects are accessed in one of two ways:
    - The default light options. These settings are used as defaults when you start a
    session and by the Defaults button on the Light ConstrainedSketchOptions dialog box.
    - The light options associated with a particular viewport.
    The LightOptions object has no constructor; Abaqus creates the **defaultLightOptions**
    member when a session is started. When a new viewport is created, the **lightOptions**
    member is copied from the current viewport.

    .. note::
        This object can be accessed by::

            session.defaultLightOptions
            session.viewports[name].lightOptions
    """

    #: A SymbolicConstant specifying the shading technique that should be used to fill facets
    #: for geometric bodies when **renderStyle** =SHADED. The lighting of facets for meshed
    #: geometry is not affected by this setting. Possible values are:GOURAUD, specifying that
    #: lighting values should be computed for each corner of a facet and interpolated to fill
    #: the remainder of the facet.PHONG, specifying that lighting values should be computed for
    #: each pixel of a facet.The default value is GOURAUD.When set to **shading** =GOURAUD,
    #: lighting values are computed for each corner of a facet and the lighting for the
    #: remainder of the facet is interpolated from the corner values. When **shading** =PHONG,
    #: lighting values are computed for each pixel of a facet.Note:The shading technique can
    #: only be set to PHONG when the **shadersAvailable** member of GraphicsOptions is
    #: True.Printed output will only contain Phong shading if the output format is raster and
    #: the **accelerateOffScreen** member of GraphicsOptions is ON.The **renderStyle** setting is
    #: part of AssemblyDisplayOptions, PartDisplayOptions, and various other options objects
    #: not listed here since they are generally used for meshed geometry.
    shading: SymbolicConstant = GOURAUD

    #: A SymbolicConstant specifying how specular highlights should be calculated. Possible
    #: values are:INFINITE, specifying that a constant vector should be used for the direction
    #: from the camera to a vertex when computing specular highlights.LOCAL, specifying that
    #: the vector from the camera to each vertex should be calculated when computing specular
    #: highlights.The default value is INFINITE.When set to **viewpoint** =INFINITE, a constant
    #: vector is used for the direction from the camera (viewpoint) to a vertex. When
    #: **viewpoint** =LOCAL, the result is more realistic because the actual vector from the
    #: camera to each vertex is calculated. However, overall performance is decreased.
    viewpoint: SymbolicConstant = INFINITE

    #: A Float specifying the degree to which specular reflection is focused. The higher the
    #: **materialShininess** argument, the more focused the specular highlight. Possible values
    #: are 0.0 ≤ **polygonOffsetConstant** ≤ 128.0. The default value is 105.0.
    materialShininess: float = 105

    #: A :py:class:`~abaqus.DisplayOptions.LightArray.LightArray` object of length 8.
    lights: LightArray = []

    #: A String specifying the light applied evenly to the entire scene independent of any
    #: individual light. The initial value is 20% gray. A list of valid color strings is in the
    #: **colors** map in the **session** object.
    ambientColor: str = ""

    @abaqus_method_doc
    def setValues(
        self,
        shading: SymbolicConstant = GOURAUD,
        viewpoint: SymbolicConstant = INFINITE,
        ambientColor: str = "",
        materialShininess: float = 105,
    ):
        """This method modifies the LightOptions object.

        Parameters
        ----------
        shading
            A SymbolicConstant specifying the shading technique that should be used to fill facets
            for geometric bodies when **renderStyle** =SHADED. The lighting of facets for meshed
            geometry is not affected by this setting. Possible values are:GOURAUD, specifying that
            lighting values should be computed for each corner of a facet and interpolated to fill
            the remainder of the facet.PHONG, specifying that lighting values should be computed for
            each pixel of a facet.The default value is GOURAUD.When set to **shading** =GOURAUD,
            lighting values are computed for each corner of a facet and the lighting for the
            remainder of the facet is interpolated from the corner values. When **shading** =PHONG,
            lighting values are computed for each pixel of a facet.Note:The shading technique can
            only be set to PHONG when the **shadersAvailable** member of GraphicsOptions is
            True.Printed output will only contain Phong shading if the output format is raster and
            the **accelerateOffScreen** member of GraphicsOptions is ON.The **renderStyle** setting is
            part of AssemblyDisplayOptions, PartDisplayOptions, and various other options objects
            not listed here since they are generally used for meshed geometry.
        viewpoint
            A SymbolicConstant specifying how specular highlights should be calculated. Possible
            values are:INFINITE, specifying that a constant vector should be used for the direction
            from the camera to a vertex when computing specular highlights.LOCAL, specifying that
            the vector from the camera to each vertex should be calculated when computing specular
            highlights.The default value is INFINITE.When set to **viewpoint** =INFINITE, a constant
            vector is used for the direction from the camera (viewpoint) to a vertex. When
            **viewpoint** =LOCAL, the result is more realistic because the actual vector from the
            camera to each vertex is calculated. However, overall performance is decreased.
        ambientColor
            A String specifying the light applied evenly to the entire scene independent of any
            individual light. The initial value is 20% gray. A list of valid color strings is in the
            **colors** map in the **session** object.
        materialShininess
            A Float specifying the degree to which specular reflection is focused. The higher the
            **materialShininess** argument, the more focused the specular highlight. Possible values
            are 0.0 ≤ **polygonOffsetConstant** ≤ 128.0. The default value is 105.0.

        Raises
        ------
        RangeError
        """
        ...
