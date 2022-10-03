from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import AS_IS, Boolean, OFF, ON, SOLID, SymbolicConstant


@abaqus_class_doc
class GraphicsOptions:
    """The GraphicsOptions object stores settings that control how objects are rendered in all
    viewports. GraphicsOptions objects are accessed in one of two ways:
    - The default graphics options. These settings are used as defaults when you start a
    session and by the Defaults button on the Graphics ConstrainedSketchOptions dialog box.
    - The current graphics options.
    The GraphicsOptions object has no constructor; Abaqus creates both the
    **defaultGraphicsOptions** and the **graphicsOptions** members when a session is started.
    When you start a session, Abaqus detects the graphics hardware installed on your system
    and uses the setValues method in the environment file (abaqus_v6.env ) to modify the
    members of the GraphicsOptions object. If your graphics hardware is not supported by
    Abaqus/CAE, or if you wish to override the default graphics options, you can modify
    settings in the environment file. For more information, see Tuning graphics cards.

    .. note::
        This object can be accessed by::

            session.defaultGraphicsOptions
            session.graphicsOptions
    """

    #: A Boolean specifying whether a viewport background style of GRADIENT can be overridden
    #: when displaying certain objects, such as sketches or XY plots. When overridden, the
    #: background will be the top color of the gradient background.
    backgroundOverride: Boolean = OFF

    #: A Boolean specifying whether facets that are determined to be facing away from the
    #: viewer will be drawn. The default value is ON. backfaceCulling provides a performance
    #: enhancement when displaying solid elements where the front side of the element occludes
    #: the back side of the element. Set **backfaceCulling** = OFF if it appears that you are
    #: seeing the back side of an element and the front side is missing. You should also set
    #: **backfaceCulling** = OFF if you believe the display is not complete.
    backfaceCulling: Boolean = ON

    #: A SymbolicConstant specifying the graphics driver to use. Abaqus/CAE currently uses
    #: OpenGL exclusively so the only possible value is OPEN_GL. OPEN_GL takes advantage of
    #: graphics adapter hardware acceleration.
    graphicsDriver: Optional[SymbolicConstant] = None

    #: A Boolean specifying whether double buffering is used. The default value is ON.Double
    #: buffering controls where Abaqus/CAE draws its graphics. When **doubleBuffering** = OFF,
    #: everything is drawn directly to the screen and on many systems you can see the progress
    #: of the drawing operations. Most users find this distracting, especially in dynamic
    #: situations such as view manipulation or animation of results. When **doubleBuffering** = ON,
    #: the drawing occurs in a separate graphics buffer that is displayed when all the drawing
    #: operations are complete. This results in a much smoother display during view changes or
    #: animation. It is recommended that you set double buffering to ON.
    doubleBuffering: Boolean = ON

    #: A Boolean specifying whether a display list will be used to accelerate graphics
    #: performance. The default value is ON.When **displayLists** = ON, drawing operations are
    #: recorded in a list that can be quickly replayed. This results in faster drawing on most
    #: systems but requires extra memory to record the drawing operations. In the Visualization
    #: module, display lists are only used during view manipulations and then their use is
    #: subject to the setting of **viewManipDisplayListThreshold**.
    displayLists: Boolean = ON

    #: A SymbolicConstant specifying which rendering is used during dynamic rotations of the
    #: view. Possible values are:FAST, specifying a rendering mode where the image is rendered
    #: in wireframe.AS_IS, specifying a rendering mode where the image is rendered as is.The
    #: default value is AS_IS.When set to **dragMode** = FAST, a wireframe outline is drawn during
    #: view changes by rotation, pan, or zoom. When **dragMode** = AS_IS, everything displayed in
    #: the window will be drawn during view changes; however, the display may lag behind the
    #: mouse movement when the model is complex especially if you are using an older or slower
    #: system. For newer systems with graphics hardware acceleration the AS_IS setting can be
    #: accommodated without significant loss of performance.
    dragMode: SymbolicConstant = AS_IS

    #: A Boolean specifying whether lines will be smoothed to reduce the jagged effect of
    #: rasterization. The default value is ON.
    antiAlias: Boolean = ON

    #: A Boolean specifying whether the model is automatically resized to fit the viewport
    #: after each view rotation. The default value is OFF.
    autoFitAfterRotate: Boolean = OFF

    #: A Float specifying the offset added when drawing the faces of a polygon. The
    #: **polygonOffsetConstant** argument affects the behavior of only the OpenGL driver.
    #: Possible values are 0.0 ≤ **polygonOffsetConstant** ≤ 100.0. The default value is
    #: platform dependent and is typically between 0.0 and 2.0.
    polygonOffsetConstant: Optional[float] = None

    #: A Float specifying the factor that multiplies the slope of each line before the line is
    #: added to the vertexes of a polygon face. The **polygonOffsetSlope** argument affects the
    #: behavior of only the OpenGL driver. Possible values are 0.0 ≤ **polygonOffsetSlope** ≤
    #: 100.0. The default value is platform dependent and is typically between 0.0 and 2.0.
    polygonOffsetSlope: Optional[float] = None

    #: A Float specifying the offset added when drawing the faces of a polygon.
    #: **printPolygonOffsetConstant** is similar to **polygonOffsetConstant**; however,
    #: **printPolygonOffsetConstant** is used when printing and **polygonOffsetConstant** is used
    #: for display. Some systems, especially Windows, use different OpenGL drivers for printing
    #: and display, and you may have to use different offset values for each driver.
    printPolygonOffsetConstant: Optional[float] = None

    #: A Float specifying the factor that multiplies the slope of each line before the line is
    #: added to the vertexes of a polygon face. **printPolygonOffsetSlope** is similar to
    #: **polygonOffsetSlope**; however, **printPolygonOffsetSlope** is used when printing and
    #: **polygonOffsetSlope** is used for display. Some systems, especially Windows, use
    #: different OpenGL drivers for printing and display, and you may have to use different
    #: offset values for each driver.
    printPolygonOffsetSlope: Optional[float] = None

    #: A Boolean specifying how the three-dimensional vertices of the model are processed. When
    #: **vertexArrays** = OFF, each vertex of the model is processed separately. When
    #: **vertexArrays** = ON, the vertices are processed in large blocks resulting in faster
    #: display. Not all graphics adapters support this capability correctly. An indicator that
    #: the graphics adapters is not processing three-dimensional vertices correctly is the
    #: absence of graphics during rubber banding operations. For example, when dynamically
    #: dragging the radius of a circle in the Sketcher, the circle should be visible. The
    #: default value is ON.
    vertexArrays: Boolean = ON

    #: A Boolean specifying whether the **vertexArrays** setting should temporarily be set to OFF
    #: when building a display list. The default value is ON.Some graphics adapters do not
    #: properly support using vertex arrays inside a display list. Setting
    #: **vertexArraysInDisplayLists** to OFF has a smaller impact on graphics performance than
    #: setting **vertexArrays** or **displayLists** to OFF.
    vertexArraysInDisplayLists: Boolean = ON

    #: An Int specifying how large a display list may be created in order to accelerate view
    #: manipulation operations. Increasing this value when viewing large models will increase
    #: the delay before a view manipulation operation begins in order to obtain improved
    #: graphics performance during the view manipulation. If set high with a large model, the
    #: delay can be many seconds. In excessive cases, graphics memory can be exceeded and the
    #: result may be an empty display list (no visible model) for the view manipulation. This
    #: setting is treated as 0 if **displayLists** = OFF. Possible values are 0 ≤
    #: **viewManipDisplayListThreshold** ≤ 20000. The default value is 40.
    viewManipDisplayListThreshold: int = 40

    #: A Boolean specifying how Abaqus renders X11 graphics operations. When
    #: **directRendering** = OFF, the graphics are rendered through the X Server. When
    #: **directRendering** = ON, the graphics operations are sent directly to the graphics adapter
    #: producing faster displays. For maximum performance, the initial value is ON. This
    #: argument is used only when you first start Abaqus/CAE; you cannot configure
    #: **directRendering** during a session.
    directRendering: Boolean = OFF

    #: A Boolean specifying whether a hardware accelerated OpenGL graphics driver will be used
    #: on Windows platforms. The default value is ON.When **hardwareAcceleration** = OFF, the
    #: graphics driver uses a software implementation of OpenGL that is included with the
    #: operating system. This results in slower drawing on most systems; however, you may have
    #: to use the software implementation of OpenGL if the hardware graphics driver is
    #: incompatible with Abaqus/CAE. **hardwareAcceleration** is used only when you first start
    #: Abaqus/CAE on a Windows platform; you cannot configure **hardwareAcceleration** during a
    #: session. **hardwareAcceleration** is not used when you start Abaqus/CAE on an X-Windows
    #: platform and display to a Windows platform running Exceed or any other X-Windows server.
    hardwareAcceleration: Boolean = ON

    #: A Boolean specifying whether hardware overlay planes will be used if available. The
    #: default value is the same value as the **hardwareOverlayAvailable** member.When
    #: **hardwareOverlayAvailable** = OFF, it will not be possible to set **hardwareOverlay** to ON
    #: and the HARDWARE_OVERLAY highlight method will not be available. If viewports display a
    #: solid color and will not display the model, it will be necessary to inhibit hardware
    #: overlay completely by setting the ABAQUS_EMULATE_OVERLAYS environment variable (to any
    #: value) before starting Abaqus/CAE. **hardwareOverlay** is used only when you first start
    #: Abaqus/CAE; you cannot configure **hardwareOverlay** during a session.
    hardwareOverlay: Boolean = OFF

    #: A Boolean specifying whether textures will be used to display contour plots. The default
    #: value is ON.Turning off texture mapping is necessary only if viewports will not
    #: correctly display a contour plot of your model.
    textureMapping: Boolean = ON

    #: A Boolean specifying whether textures will be used to display contour plots. The default
    #: value is ON.Turning off texture mapping for printing is necessary only if printed output
    #: does not correctly display a contour plot of your model. **printTextureMapping** is
    #: similar to **textureMapping**; however, **printTextureMapping** is used when printing and
    #: **textureMapping** is used for display. Some systems, especially Windows, use different
    #: OpenGL drivers for printing and display, and you may have to use different settings for
    #: each driver.
    printTextureMapping: Boolean = ON

    #: A SymbolicConstant specifying the background style to be used for all viewport windows.
    #: Possible values are SOLID and GRADIENT. The default value is SOLID.If
    #: **backgroundStyle** = SOLID, the viewport background will appear as a solid color as
    #: specified by **backgroundColor**. If **backgroundStyle** = GRADIENT, the viewport background
    #: will be drawn as a gradient beginning with the **backgroundColor** at the top of the
    #: viewport and gradually blending to the **backgroundBottomColor** at the bottom of the
    #: viewport.
    backgroundStyle: SymbolicConstant = SOLID

    #: A Boolean specifying whether the hardware accelerated graphics driver will be used for
    #: off-screen rendering. The default value is ON if graphics hardware acceleration is
    #: available and has not been disabled via the hardwareAcceleration option, and the
    #: graphics driver supports the underlying technology. When set to OFF, an alternate
    #: (slower) technique will be used to create off-screen images. Off-screen rendering is
    #: used for Printing, Probe, and backing store (viewport refresh). Setting this value to
    #: OFF will force printed images to be rendered without hardware acceleration. This is
    #: useful when writing automated tests to produce raster images that you will want to
    #: compare across multiple machines that may have different graphics environments.
    accelerateOffScreen: Boolean = OFF

    #: A Boolean specifying whether a backing store will be used to refresh a viewport after a
    #: window occluding the viewport is moved or dismissed. The default value is ON.
    backingStore: Boolean = ON

    #: A SymbolicConstant specifying the highlight method. For the GraphicsOptions object,
    #: possible values of the member are HARDWARE_OVERLAY, XOR, SOFTWARE_OVERLAY, and BLEND.
    highlightMethod: Optional[SymbolicConstant] = None

    #: A Boolean specifying if the graphics hardware supports hardware overlay.
    hardwareOverlayAvailable: Boolean = OFF

    #: A Boolean specifying if the graphics hardware supports the OpenGL Shading Language
    #: (GLSL).
    shadersAvailable: Boolean = OFF

    #: An Int specifying whether speed or accuracy is more important when drawing translucent
    #: objects. Lower values optimize for speed while higher values optimize for accuracy. The
    #: actual meaning of each setting will depend on the setting of **shadersAvailable** and the
    #: capabilities of the graphics hardware and driver. Possible values are 1 ≤
    #: **translucencyMode** ≤ 6. The default value is 4.
    translucencyMode: int = 4

    #: A Float specifying a tolerance used when computing the appropriate scale for
    #: transforming result (contour) values to texture values. When set too low the 'out of
    #: range' colors may be incorrectly shown for values near the range limits. The default
    #: value is 0.5×10-5.
    contourRangeTexturePrecision: float = 0

    #: None or a GraphicsOptions object specifying the object from which values are to be
    #: copied. If other arguments are also supplied to setValues, they will override the values
    #: in the **options** member. The default value is None.
    options: Optional[str] = None

    #: A tuple of SymbolicConstants specifying a hint used to modify the highlight method.
    #: Possible values are:HARDWARE_OVERLAY, specifying a hint of hardware overlay. The best
    #: graphics performance is achieved using hardware overlay, but not all systems and
    #: graphics adapters support hardware overlay.XOR, specifying a hint of XOR technique. The
    #: XOR technique uses a boolean pixel operation to simulate the drawing operations but can
    #: produce different colors depending on the color of the underlying
    #: pixels.SOFTWARE_OVERLAY, specifying a hint of software overlay. The software overlay
    #: method simulates the effect of hardware overlay.BLEND, specifying a hint of blend
    #: method. The blend method combines the color of the underlying pixel with the desired
    #: color producing an approximation of the transient graphics.The default value is
    #: (HARDWARE_OVERLAY, XOR, SOFTWARE_OVERLAY, BLEND).The values of this sequence are applied
    #: by Abaqus when you start a session in first to last order. The first successful value
    #: becomes the default highlight method. Not all graphics adapters support the
    #: HARDWARE_OVERLAY value and you must use the **highlightMethodHint** argument to provide an
    #: alternative.You can use a single value to set the first element of the list, or you can
    #: use a tuple with one to four unique values. Abaqus sets any remaining elements of the
    #: tuple to unique values based on the default order.
    highlightMethodHint: Optional[SymbolicConstant] = None

    #: A String specifying one of the two background colors for all viewport windows. The
    #: initial color is black. A list of valid color strings is in the **colors** map in the
    #: Session object.
    backgroundColor: str = ""

    #: A String specifying one of the two background colors for all viewport windows. This
    #: color is used only if **backgroundStyle** =GRADIENT. The initial color is black. A list of
    #: valid color strings is in the **colors** map in the Session object.
    backgroundBottomColor: str = ""

    @abaqus_method_doc
    def setValues(
        self,
        graphicsDriver: Optional[SymbolicConstant] = None,
        doubleBuffering: Boolean = ON,
        displayLists: Boolean = ON,
        highlightMethodHint: Optional[SymbolicConstant] = None,
        dragMode: SymbolicConstant = AS_IS,
        antiAlias: Boolean = ON,
        autoFitAfterRotate: Boolean = OFF,
        polygonOffsetConstant: Optional[float] = None,
        polygonOffsetSlope: Optional[float] = None,
        printPolygonOffsetConstant: Optional[float] = None,
        printPolygonOffsetSlope: Optional[float] = None,
        vertexArrays: Boolean = ON,
        vertexArraysInDisplayLists: Boolean = ON,
        viewManipDisplayListThreshold: int = 40,
        directRendering: Boolean = OFF,
        hardwareAcceleration: Boolean = ON,
        hardwareOverlay: Boolean = OFF,
        textureMapping: Boolean = ON,
        printTextureMapping: Boolean = ON,
        backgroundStyle: SymbolicConstant = SOLID,
        backgroundColor: str = "",
        backgroundBottomColor: str = "",
        backgroundOverride: Boolean = OFF,
        backfaceCulling: Boolean = ON,
        accelerateOffScreen: Boolean = OFF,
        backingStore: Boolean = ON,
        shadersAvailable: Boolean = OFF,
        translucencyMode: int = 4,
        options: Optional[str] = None,
        contourRangeTexturePrecision: float = 0,
    ):
        """This method modifies the GraphicsOptions object.

        Parameters
        ----------
        graphicsDriver
            A SymbolicConstant specifying the graphics driver to use. Abaqus/CAE currently uses
            OpenGL exclusively so the only possible value is OPEN_GL. OPEN_GL takes advantage of
            graphics adapter hardware acceleration.
        doubleBuffering
            A Boolean specifying whether double buffering is used. The default value is ON.Double
            buffering controls where Abaqus/CAE draws its graphics. When **doubleBuffering** = OFF,
            everything is drawn directly to the screen and on many systems you can see the progress
            of the drawing operations. Most users find this distracting, especially in dynamic
            situations such as view manipulation or animation of results. When **doubleBuffering** = ON,
            the drawing occurs in a separate graphics buffer that is displayed when all the drawing
            operations are complete. This results in a much smoother display during view changes or
            animation. It is recommended that you set double buffering to ON.
        displayLists
            A Boolean specifying whether a display list will be used to accelerate graphics
            performance. The default value is ON.When **displayLists** = ON, drawing operations are
            recorded in a list that can be quickly replayed. This results in faster drawing on most
            systems but requires extra memory to record the drawing operations. In the Visualization
            module, display lists are only used during view manipulations and then their use is
            subject to the setting of **viewManipDisplayListThreshold**.
        highlightMethodHint
            A sequence of SymbolicConstants specifying a hint used to modify the highlight method.
            Possible values are:HARDWARE_OVERLAY, specifying a hint of hardware overlay. The best
            graphics performance is achieved using hardware overlay, but not all systems and
            graphics adapters support hardware overlay.XOR, specifying a hint of XOR technique. The
            XOR technique uses a boolean pixel operation to simulate the drawing operations but can
            produce different colors depending on the color of the underlying
            pixels.SOFTWARE_OVERLAY, specifying a hint of software overlay. The software overlay
            method simulates the effect of hardware overlay.BLEND, specifying a hint of blend
            method. The blend method combines the color of the underlying pixel with the desired
            color producing an approximation of the transient graphics.The default value is
            (HARDWARE_OVERLAY, XOR, SOFTWARE_OVERLAY, BLEND).The values of this sequence are applied
            by Abaqus when you start a session in first to last order. The first successful value
            becomes the default highlight method. Not all graphics adapters support the
            HARDWARE_OVERLAY value and you must use the **highlightMethodHint** argument to provide an
            alternative.You can use a single value to set the first element of the list, or you can
            use a tuple with one to four unique values. Abaqus sets any remaining elements of the
            tuple to unique values based on the default order.
        dragMode
            A SymbolicConstant specifying which rendering is used during dynamic rotations of the
            view. Possible values are:FAST, specifying a rendering mode where the image is rendered
            in wireframe.AS_IS, specifying a rendering mode where the image is rendered as is.The
            default value is AS_IS.When set to **dragMode** = FAST, a wireframe outline is drawn during
            view changes by rotation, pan, or zoom. When **dragMode** = AS_IS, everything displayed in
            the window will be drawn during view changes; however, the display may lag behind the
            mouse movement when the model is complex especially if you are using an older or slower
            system. For newer systems with graphics hardware acceleration the AS_IS setting can be
            accommodated without significant loss of performance.
        antiAlias
            A Boolean specifying whether lines will be smoothed to reduce the jagged effect of
            rasterization. The default value is ON.
        autoFitAfterRotate
            A Boolean specifying whether the model is automatically resized to fit the viewport
            after each view rotation. The default value is OFF.
        polygonOffsetConstant
            A Float specifying the offset added when drawing the faces of a polygon. The
            **polygonOffsetConstant** argument affects the behavior of only the OpenGL driver.
            Possible values are 0.0 ≤ **polygonOffsetConstant** ≤ 100.0. The default value is
            platform dependent and is typically between 0.0 and 2.0.
        polygonOffsetSlope
            A Float specifying the factor that multiplies the slope of each line before the line is
            added to the vertexes of a polygon face. The **polygonOffsetSlope** argument affects the
            behavior of only the OpenGL driver. Possible values are 0.0 ≤ **polygonOffsetSlope** ≤
            100.0. The default value is platform dependent and is typically between 0.0 and 2.0.
        printPolygonOffsetConstant
            A Float specifying the offset added when drawing the faces of a polygon.
            **printPolygonOffsetConstant** is similar to **polygonOffsetConstant**; however,
            **printPolygonOffsetConstant** is used when printing and **polygonOffsetConstant** is used
            for display. Some systems, especially Windows, use different OpenGL drivers for printing
            and display, and you may have to use different offset values for each driver.
        printPolygonOffsetSlope
            A Float specifying the factor that multiplies the slope of each line before the line is
            added to the vertexes of a polygon face. **printPolygonOffsetSlope** is similar to
            **polygonOffsetSlope**; however, **printPolygonOffsetSlope** is used when printing and
            **polygonOffsetSlope** is used for display. Some systems, especially Windows, use
            different OpenGL drivers for printing and display, and you may have to use different
            offset values for each driver.
        vertexArrays
            A Boolean specifying how the three-dimensional vertices of the model are processed. When
            **vertexArrays** = OFF, each vertex of the model is processed separately. When
            **vertexArrays** = ON, the vertices are processed in large blocks resulting in faster
            display. Not all graphics adapters support this capability correctly. An indicator that
            the graphics adapters is not processing three-dimensional vertices correctly is the
            absence of graphics during rubber banding operations. For example, when dynamically
            dragging the radius of a circle in the Sketcher, the circle should be visible. The
            default value is ON.
        vertexArraysInDisplayLists
            A Boolean specifying whether the **vertexArrays** setting should temporarily be set to OFF
            when building a display list. The default value is ON.Some graphics adapters do not
            properly support using vertex arrays inside a display list. Setting
            **vertexArraysInDisplayLists** to OFF has a smaller impact on graphics performance than
            setting **vertexArrays** or **displayLists** to OFF.
        viewManipDisplayListThreshold
            An Int specifying how large a display list may be created in order to accelerate view
            manipulation operations. Increasing this value when viewing large models will increase
            the delay before a view manipulation operation begins in order to obtain improved
            graphics performance during the view manipulation. If set high with a large model, the
            delay can be many seconds. In excessive cases, graphics memory can be exceeded and the
            result may be an empty display list (no visible model) for the view manipulation. This
            setting is treated as 0 if **displayLists** = OFF. Possible values are 0 ≤
            **viewManipDisplayListThreshold** ≤ 20000. The default value is 40.
        directRendering
            A Boolean specifying how Abaqus renders X11 graphics operations. When
            **directRendering** = OFF, the graphics are rendered through the X Server. When
            **directRendering** = ON, the graphics operations are sent directly to the graphics adapter
            producing faster displays. For maximum performance, the initial value is ON. This
            argument is used only when you first start Abaqus/CAE; you cannot configure
            **directRendering** during a session.
        hardwareAcceleration
            A Boolean specifying whether a hardware accelerated OpenGL graphics driver will be used
            on Windows platforms. The default value is ON.When **hardwareAcceleration** = OFF, the
            graphics driver uses a software implementation of OpenGL that is included with the
            operating system. This results in slower drawing on most systems; however, you may have
            to use the software implementation of OpenGL if the hardware graphics driver is
            incompatible with Abaqus/CAE. **hardwareAcceleration** is used only when you first start
            Abaqus/CAE on a Windows platform; you cannot configure **hardwareAcceleration** during a
            session. **hardwareAcceleration** is not used when you start Abaqus/CAE on an X-Windows
            platform and display to a Windows platform running Exceed or any other X-Windows server.
        hardwareOverlay
            A Boolean specifying whether hardware overlay planes will be used if available. The
            default value is the same value as the **hardwareOverlayAvailable** member.When
            **hardwareOverlayAvailable** = OFF, it will not be possible to set **hardwareOverlay** to ON
            and the HARDWARE_OVERLAY highlight method will not be available. If viewports display a
            solid color and will not display the model, it will be necessary to inhibit hardware
            overlay completely by setting the ABAQUS_EMULATE_OVERLAYS environment variable (to any
            value) before starting Abaqus/CAE. **hardwareOverlay** is used only when you first start
            Abaqus/CAE; you cannot configure **hardwareOverlay** during a session.
        textureMapping
            A Boolean specifying whether textures will be used to display contour plots. The default
            value is ON.Turning off texture mapping is necessary only if viewports will not
            correctly display a contour plot of your model.
        printTextureMapping
            A Boolean specifying whether textures will be used to display contour plots. The default
            value is ON.Turning off texture mapping for printing is necessary only if printed output
            does not correctly display a contour plot of your model. **printTextureMapping** is
            similar to **textureMapping**; however, **printTextureMapping** is used when printing and
            **textureMapping** is used for display. Some systems, especially Windows, use different
            OpenGL drivers for printing and display, and you may have to use different settings for
            each driver.
        backgroundStyle
            A SymbolicConstant specifying the background style to be used for all viewport windows.
            Possible values are SOLID and GRADIENT. The default value is SOLID.If
            **backgroundStyle** = SOLID, the viewport background will appear as a solid color as
            specified by **backgroundColor**. If **backgroundStyle** = GRADIENT, the viewport background
            will be drawn as a gradient beginning with the **backgroundColor** at the top of the
            viewport and gradually blending to the **backgroundBottomColor** at the bottom of the
            viewport.
        backgroundColor
            A String specifying one of the two background colors for all viewport windows. The
            initial color is black. A list of valid color strings is in the **colors** map in the
            Session object.
        backgroundBottomColor
            A String specifying one of the two background colors for all viewport windows. This
            color is used only if **backgroundStyle** =GRADIENT. The initial color is black. A list of
            valid color strings is in the **colors** map in the Session object.
        backgroundOverride
            A Boolean specifying whether a viewport background style of GRADIENT can be overridden
            when displaying certain objects, such as sketches or XY plots. When overridden, the
            background will be the top color of the gradient background.
        backfaceCulling
            A Boolean specifying whether facets that are determined to be facing away from the
            viewer will be drawn. The default value is ON. backfaceCulling provides a performance
            enhancement when displaying solid elements where the front side of the element occludes
            the back side of the element. Set **backfaceCulling** = OFF if it appears that you are
            seeing the back side of an element and the front side is missing. You should also set
            **backfaceCulling** = OFF if you believe the display is not complete.
        accelerateOffScreen
            A Boolean specifying whether the hardware accelerated graphics driver will be used for
            off-screen rendering. The default value is ON if graphics hardware acceleration is
            available and has not been disabled via the hardwareAcceleration option, and the
            graphics driver supports the underlying technology. When set to OFF, an alternate
            (slower) technique will be used to create off-screen images. Off-screen rendering is
            used for Printing, Probe, and backing store (viewport refresh). Setting this value to
            OFF will force printed images to be rendered without hardware acceleration. This is
            useful when writing automated tests to produce raster images that you will want to
            compare across multiple machines that may have different graphics environments.
        backingStore
            A Boolean specifying whether a backing store will be used to refresh a viewport after a
            window occluding the viewport is moved or dismissed. The default value is ON.
        shadersAvailable
            A Boolean specifying if the graphics hardware supports the OpenGL Shading Language
            (GLSL).
        translucencyMode
            An Int specifying whether speed or accuracy is more important when drawing translucent
            objects. Lower values optimize for speed while higher values optimize for accuracy. The
            actual meaning of each setting will depend on the setting of **shadersAvailable** and the
            capabilities of the graphics hardware and driver. Possible values are 1 ≤
            **translucencyMode** ≤ 6. The default value is 4.
        options
            None or a GraphicsOptions object specifying the object from which values are to be
            copied. If other arguments are also supplied to setValues, they will override the values
            in the **options** member. The default value is None.
        contourRangeTexturePrecision
            A Float specifying a tolerance used when computing the appropriate scale for
            transforming result (contour) values to texture values. When set too low the 'out of
            range' colors may be incorrectly shown for values near the range limits. The default
            value is 0.5×10-5.

        Raises
        ------
        RangeError
        """
        ...
