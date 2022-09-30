from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import Boolean, CCW, FILL, OFF, ON, SymbolicConstant


@abaqus_class_doc
class Drawing:
    """A drawing is the container for a geometric object. The Drawing object stores the vertex
    data and various settings that determine how the drawing will be displayed.

    .. note:: 
        This object can be accessed by::

            session.drawings[name]
    """

    #: An Int specifying the number of vertices in the vertex array after a call to the
    #: setVertices method. The default value is 0.
    vertexCount: int = 0

    #: An Int specifying the number of normal vectors in the normal array after a call to the
    #: setNormals method. The default value is 0.
    normalCount: int = 0

    #: An Int specifying the number of colors in the color array after a call to the setColors
    #: method. The default value is 0.
    colorCount: int = 0

    #: A Boolean specifying whether the drawing object will be rendered when referenced. The
    #: default value is OFF.
    show: Boolean = OFF

    #: A Boolean specifying whether polygonal graphics primitives facing away from the viewer
    #: should be culled (not rendered). The default value is OFF.The winding order, and not the
    #: normal, of the graphics primitive is used to determine its facing.
    cullBackfaces: Boolean = OFF

    #: A SymbolicConstant specifying the winding order for polygonal graphics primitives that
    #: face the viewer. Possible values are:CCW, specifying front face winding order is
    #: counter-clockwise.CW, specifying front face winding order is clockwise.The default value
    #: is CCW.
    frontFaceOrder: SymbolicConstant = CCW

    #: A Float specifying the opacity for polygonal graphics primitives. Possible values are
    #: 0.0 ≤ **translucency** ≤ 1.0 with 0.0 being completely transparent (invisible) and 1.0
    #: being opaque. The default value is 1.0.A value greater than 0.3 will cause the
    #: translucent facets to be sorted by depth before being rendered and has the side effect
    #: of disabling two-sided lighting for those facets.
    translucency: float = 1

    #: A Float specifying the width of the line, in millimeters, used to render edges. Possible
    #: values are 0.0 ≤ **lineSize** ≤ 5.0 with 0.0 being interpreted as the thinnest possible
    #: line. The default value is 0.0.A value of 0.0 will be one pixel on the output device.
    #: One pixel on the screen is generally visible but one pixel on a 1200 DPI printer may not
    #: be clear.
    lineSize: float = 0

    #: A Float specifying the width of points, in millimeters, used to render points. Possible
    #: values are 0.0 ≤ **lineSize** ≤ 5.0 with 0.0 being interpreted as the smallest possible
    #: point. The default value is 0.0.A value of 0.0 will be one pixel on the output device.
    #: One pixel on the screen is generally visible but one pixel on a 1200 DPI printer may not
    #: be clear.
    pointSize: float = 0

    #: A Boolean specifying whether the lighting of polygonal graphics primitives is consistent
    #: for each facet or calculated for each displayed pixel. The default value is ON.When
    #: False, only the last normal for each facet will be used in the lighting calculation.
    smoothShade: Boolean = ON

    #: A Boolean specifying whether edge and point drawing commands will be issued in a FILLED
    #: or SHADED display. The default value is ON.If no edge or point drawing commands have
    #: been defined, the polygonal drawing commands will be issued in WIREFRAME and HIDDEN_LINE
    #: displays with the **polygonMode** set to EDGES. If only edge and point drawing commands
    #: have been defined, the Drawing will not be rendered in FILLED or SHADED displays.
    edgesInShaded: Boolean = ON

    #: A tuple of three Floats specifying the **Red**, **Green**, and **Blue** component values for
    #: the edge color. Possible values for each component are between 0.0 and 1.0.
    edgeColor: Optional[float] = None

    #: A tuple of three Floats specifying the **Red**, **Green**, and **Blue** component values for
    #: the point color. Possible values for each component are between 0.0 and 1.0.
    pointColor: Optional[float] = None

    #: A String specifying the repository key.
    name: str

    @abaqus_method_doc
    def __init__(self, name: str):
        """This method creates an empty Drawing object.

        .. note:: 
            This function can be accessed by::

                session.Drawing

        Parameters
        ----------
        name
            A String specifying the repository key.

        Returns
        -------
        Drawing
            A :py:class:`~abaqus.Session.Drawing.Drawing` object.

        Raises
        ------
        ValueError
            - If the user attempts to create a new drawing with the name of an existing drawing:
              ValueError: There is already a drawing with this name
        """
        ...

    @abaqus_method_doc
    def setVertices(self, vertexDimension: float, vertexData: tuple):
        """This method accepts the vertex data that defines the Drawing object. It defines in an
        array of vertices with a length equal to the length of the **vertexData** sequence divided
        by **vertexDimension**.

        Parameters
        ----------
        vertexDimension
            An Integer in the range of 2 to 4 specifying how many Float values are needed to compose
            a single vertex.
        vertexData
            A sequence of Float values that will be used to compose the vertices. There must be
            **vertexDimension** values in the sequence for each vertex.

        Returns
        -------
        int
            The number of vertices described.

        Raises
        ------
        RangeError: **vertexDimension** must be in the range 2 <= value <= 4
            If an invalid **vertexDimension** is specified.
        ValueError: **vertexData** cannot be empty
            If **vertexData** is an empty sequence.
        ValueError: **vertexData** cannot be reduced
            If setVertices has already been called and this call is sending fewer vertices.
        """
        ...

    @abaqus_method_doc
    def setNormals(self, normalData: tuple):
        """This method accepts the normal data for each vertex. It defines in an array of normal
        vectors with a length equal to the length of the **normalData** sequence divided by 3.

        Parameters
        ----------
        normalData
            A sequence of Float values that will be used to compose the normals. There must be 3
            values in the sequence for each normal.If only one normal is specified, all vertices
            will use the normal value.

        Returns
        -------
        int
            The number of normals described.

        Raises
        ------
        RangeError
        ValueError: **normalData** must have at least three values
            If **normalData** is sequence with less than 3 values.
        ValueError: **normalData** cannot be reduced
            If setNormals has already been called and this call is sending fewer values.
        """
        ...

    @abaqus_method_doc
    def setColors(self, colorDimension: float, colorData: tuple):
        """This method accepts the color data for each vertex. It defines in an array of colors
        with a length equal to the length of the **colorData** sequence divided by
        **colorDimension**.

        Parameters
        ----------
        colorDimension
            An Integer in the range of 3 to 4 specifying how many Float values are needed to compose
            a single color.
        colorData
            A sequence of Float values in the range of 0.0 to 1.0 that will be used to compose the
            colors. There must be **colorDimension** values in the sequence for each color. The first
            color will be associated with the fist vertex and so on.The first Float will be the red
            value for the first color. The second Float will be the green value and the third will
            be the blue value. When **colorDimension** is 4 the 4th Float will be the alpha value for
            the first color but is ignored.If only one color is specified, all vertices will use the
            color value.

        Returns
        -------
        int 
            The number of colors described.

        Raises
        ------
        RangeError: **colorDimension** must be in the range 3 <= value <= 4
            If an invalid **colorDimension** is specified.
        ValueError: **colorData** cannot be empty
            If **colorData** is an empty sequence.
        ValueError: **colorData** cannot be reduced
            If setColors has already been called and this call is sending fewer colors.
        """
        ...

    @abaqus_method_doc
    def setEdgeColor(self, edgeColor: tuple):
        """This method allows a separate, single color to be used when rendering the edges of the
        drawing. Once called, edges will be rendered using the specified color but facets will
        continue to use the colors specified in the setColors method. An empty sequence can be
        specified to resume using the colors arrays for edges.

        Parameters
        ----------
        edgeColor
            A sequence of 0 or 3 Float values in the range of 0.0 to 1.0 that will be used to
            compose the edge color.If the initial Float value is -1, the viewport background color
            will be used for the edge color.

        Raises
        ------
        ValueError
            - If **edgeColor** is not a sequence of 0 or 3 Floats:
              ValueError: **edgeColor** must be a tuple with 3 values
        """
        ...

    @abaqus_method_doc
    def setPointColor(self, pointColor: tuple):
        """This method allows a separate, single color to be used when rendering the points of the
        drawing. Once called, points will be rendered using the specified color but facets will
        continue to use the colors specified in the setColors method. An empty sequence can be
        specified to resume using the colors arrays for points.

        Parameters
        ----------
        pointColor
            A sequence of 0 or 3 Float values in the range of 0.0 to 1.0 that will be used to
            compose the point color.If the initial Float value is -1, the viewport background color
            will be used for the edge color.

        Raises
        ------
        ValueError
            - If **pointColor** is a not sequence of 0 or 3 Floats:
              ValueError: **pointColor** must be a tuple with 3 values
        """
        ...

    @abaqus_method_doc
    def addArrayDraw(
        self,
        type: SymbolicConstant,
        startIndex: int,
        numVertices: int,
        polygonMode: SymbolicConstant = FILL,
    ):
        """This method adds a rendering command to the drawing and can be called multiple times to
        add additional rendering commands. When the drawing is referenced by a Viewport, the
        drawing commands are used the render the Drawing.
        The rendering command constructs the specified type of geometric primitive using
        **numVertices** array elements starting at element index **startIndex**.

        Parameters
        ----------
        type
            A SymbolicConstant specifying the type of graphics primitive rendered by this command.
            Possible values are POINTS, LINES, LINE_LOOP, LINE_STRIP, TRIANGLES, TRIANGLE_STRIP,
            TRIANGLE_FAN, QUADS, and QUAD_STRIP.
        startIndex
            An Integer specifying the index of the first vertex to render.
        numVertices
            An Integer specifying the total number of vertices to render.
        polygonMode
            A SymbolicConstant specifying how polygonal graphics primitives will be rendered by this
            command. Possible values are FILL, EDGES, and POINTS. The default value is FILL.

        Returns
        -------
        int
            The total number of rendering commands that have been specified.

        Raises
        ------
        ValueError
            If (**startIndex** + **numVertices** - 1) is larger than the length of the vertex array:
        ValueError: Drawing request extends past array size of vertices
            - If (**startIndex** + **numVertices** - 1) is larger than the length of the normal array
              and normals are required for the graphics primitive:
              Drawing request extends past array size of normals.
            - If (**startIndex** + **numVertices** - 1) is larger than the length of the color array and
              vertex colors are required for the graphics primitive:
              Drawing request extends past array size of colors.
        """
        ...

    @abaqus_method_doc
    def addIndexDraw(
        self,
        type: SymbolicConstant,
        indices: tuple,
        polygonMode: SymbolicConstant = FILL,
    ):
        """This method adds a rendering command to the drawing and can be called multiple times to
        add additional rendering commands. When the drawing is referenced by a Viewport, the
        drawing commands are used the render the Drawing.
        The rendering command constructs the specified type of geometric primitive using
        **numVertices** array elements starting at element index **startIndex**.

        Parameters
        ----------
        type
            A SymbolicConstant specifying the type of graphics primitive rendered by this command.
            Possible values are POINTS, LINES, LINE_LOOP, LINE_STRIP, TRIANGLES, TRIANGLE_STRIP,
            TRIANGLE_FAN, QUADS, and QUAD_STRIP.
        indices
            A sequence of Integer values specifying index of each vertex to render.
        polygonMode
            A SymbolicConstant specifying how polygonal graphics primitives will be rendered by this
            command. Possible values are FILL, EDGES, and POINTS. The default value is FILL.

        Returns
        -------
        int 
            The total number of rendering commands that have been specified.

        Raises
        ------
        ValueError
            - If any value in the **indices** sequence negative:
              ValueError: Index values must be positive.
            - If any value in the **indices** sequence is larger than the length of the vertex array:
        ValueError: Drawing request extends past array size of vertices.
            - If any value in the **indices** sequence is larger than the length of the normal array
              and normals are required for the graphics primitive:
              Drawing request extends past array size of normals.
            - If any value in the **indices** sequence is larger than the length of the color array
              and vertex colors are required for the graphics primitive:
              Drawing request extends past array size of colors.
        """
        ...

    @abaqus_method_doc
    def setValues(
        self,
        show: Boolean = OFF,
        cullBackfaces: Boolean = OFF,
        frontFaceOrder: SymbolicConstant = CCW,
        smoothShade: Boolean = ON,
        edgesInShaded: Boolean = ON,
        translucency: float = 1,
        lineSize: float = 0,
        pointSize: float = 0,
    ):
        """This method modifies the rendering of the Drawing object.

        Parameters
        ----------
        show
            A Boolean specifying whether the drawing object will be rendered when referenced. The
            default value is OFF.
        cullBackfaces
            A Boolean specifying whether polygonal graphics primitives facing away from the viewer
            should be culled (not rendered). The default value is OFF.The winding order, and not the
            normal, of the graphics primitive is used to determine its facing.
        frontFaceOrder
            A SymbolicConstant specifying the winding order for polygonal graphics primitives that
            face the viewer. Possible values are:CCW, specifying front face winding order is
            counter-clockwise.CW, specifying front face winding order is clockwise.The default value
            is CCW.
        smoothShade
            A Boolean specifying whether the lighting of polygonal graphics primitives is consistent
            for each facet or calculated for each displayed pixel. The default value is ON.When
            False, only the last normal for each facet will be used in the lighting calculation.
        edgesInShaded
            A Boolean specifying whether edge and point drawing commands will be issued in a FILLED
            or SHADED display. The default value is ON.If no edge or point drawing commands have
            been defined, the polygonal drawing commands will be issued in WIREFRAME and HIDDEN_LINE
            displays with the **polygonMode** set to EDGES. If only edge and point drawing commands
            have been defined, the Drawing will not be rendered in FILLED or SHADED displays.
        translucency
            A Float specifying the opacity for polygonal graphics primitives. Possible values are
            0.0 ≤ **translucency** ≤ 1.0 with 0.0 being completely transparent (invisible) and 1.0
            being opaque. The default value is 1.0.A value greater than 0.3 will cause the
            translucent facets to be sorted by depth before being rendered and has the side effect
            of disabling two-sided lighting for those facets.
        lineSize
            A Float specifying the width of the line, in millimeters, used to render edges. Possible
            values are 0.0 ≤ **lineSize** ≤ 5.0 with 0.0 being interpreted as the thinnest possible
            line. The default value is 0.0.A value of 0.0 will be one pixel on the output device.
            One pixel on the screen is generally visible but one pixel on a 1200 DPI printer may not
            be clear.
        pointSize
            A Float specifying the width of points, in millimeters, used to render points. Possible
            values are 0.0 ≤ **lineSize** ≤ 5.0 with 0.0 being interpreted as the smallest possible
            point. The default value is 0.0.A value of 0.0 will be one pixel on the output device.
            One pixel on the screen is generally visible but one pixel on a 1200 DPI printer may not
            be clear.

        Raises
        ------
        RangeError
            - If an invalid **translucency** value is specified:
              RangeError: **translucency** must be in the range 0.0 <= value <= 1.0
            - If an invalid **lineSize** value is specified:
              RangeError: **lineSize** must be in the range 0.0 <= value <= 5.0
            - If an invalid **pointSize** value is specified:
              RangeError: **pointSize** must be in the range 0.0 <= value <= 5.0
        """
        ...
