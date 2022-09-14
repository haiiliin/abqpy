from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class ProbeOptions:
    """The ProbeOptions object is used to store settings associated with probing a model or an
    **X - Y** plot. The ProbeOptions object has no constructor. Abaqus creates the
    **defaultProbeOptions** and the **probeOptions** members when you import the Visualization
    module. When probing is initiated for the first time, the values in the **probeOptions**
    member are initialized using the values from the **defaultProbeOptions** member.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.defaultProbeOptions
            session.probeOptions
    """

    #: A SymbolicConstant specifying the entity being probed when **probeObject** = "ODB". Possible
    #: values are NODE and ELEMENT. The default value is ELEMENT.
    probeEntity: SymbolicConstant = ELEMENT

    #: A SymbolicConstant specifying the output position to probe for field output results when
    #: **probeObject** = "ODB". Possible values are NODAL, INTEGRATION_POINT, ELEMENT_FACE,
    #: ELEMENT_NODAL, and ELEMENT_CENTROID.When **probeEntity** = NODE, the only possible value is
    #: NODAL. When **probeEntity** = ELEMENT, the only possible values are INTEGRATION_POINT,
    #: ELEMENT_FACE, ELEMENT_NODAL, and ELEMENT_CENTROID, and the default is INTEGRATION_POINT.
    probeOutputPosition: SymbolicConstant = None

    #: A Boolean specifying whether to display the part instance information. This member is
    #: valid when **probeObject** = ODB. The default value is ON.
    partInstance: Boolean = ON

    #: A Boolean specifying whether to display the element ID information. This member is valid
    #: when **probeObject** = ODB and **probeEntity** = ELEMENT. The default value is ON.
    elementID: Boolean = ON

    #: A Boolean specifying whether to display the element type information. This member is
    #: valid when **probeObject** = ODB and **probeEntity** = ELEMENT. The default value is ON.
    elementType: Boolean = ON

    #: A Boolean specifying whether to display the element connectivity. This member is valid
    #: when **probeObject** = ODB and **probeEntity** = ELEMENT. The default value is ON.
    elementConnectivity: Boolean = ON

    #: A Boolean specifying whether to display the element field output results. This member is
    #: valid when **probeObject** = ODB, **probeEntity** = ELEMENT, and **isFieldOutputAvailable** = ON.
    #: The default value is ON.
    elementFieldResults: Boolean = ON

    #: A Boolean specifying whether to display the node ID when **probeObject** = ODB and
    #: **probeEntity** = NODE. The default value is ON.
    nodeId: Boolean = ON

    #: A Boolean specifying whether to display the base coordinates of a node when
    #: **probeObject** = ODB and **probeEntity** = NODE. The default value is ON.
    baseCoordinates: Boolean = ON

    #: A Boolean specifying whether to display the deformed coordinates of a node when
    #: **probeObject** = ODB and **probeEntity** = NODE. The default value is ON.
    deformedCoordinates: Boolean = ON

    #: A Boolean specifying whether to display the elements attached to a node when
    #: **probeObject** = ODB and **probeEntity** = NODE. The default value is ON.
    attachedElements: Boolean = ON

    #: A Boolean specifying whether to display the node field output results. This member is
    #: valid when **probeObject** = ODB, **probeEntity** = NODE, and **isFieldOutputAvailable** = ON. The
    #: default value is ON.
    nodeFieldResults: Boolean = ON

    #: A Boolean specifying whether to display the legend for a curve being probed. This member
    #: is valid when **probeObject** = XYPlot. The default value is ON.
    legend: Boolean = ON

    #: A Boolean specifying whether to display the **x**-coordinate value of the point on the
    #: curve being probed. This member is valid when **probeObject** = XYPlot. The default value is
    #: ON.
    xValue: Boolean = ON

    #: A Boolean specifying whether to display the **y**-coordinate value of the point on the
    #: curve being probed. This member is valid when **probeObject** = XYPlot. The default value is
    #: ON.
    yValue: Boolean = ON

    #: A Boolean specifying whether to display the sequence ID of the point on the curve being
    #: probed. This member is valid when **probeObject** = XYPlot. The default value is ON.
    sequenceID: Boolean = ON

    #: A Boolean specifying whether to interpolate values within a line segment when
    #: **probeObject** = XYPlot. When **interpolateXy** = OFF, probing returns the nearest **X - Y** data
    #: point on the curve. When **interpolateXy** = ON, probing interpolates data to return a value
    #: at the nearest point on the curve. The default value is OFF.
    interpolateXy: Boolean = OFF

    #: A Boolean specifying whether field output is available for probing when
    #: **probeObject** = XYPlot. This member is read-only.
    isFieldOutputAvailable: Boolean = OFF

    #: A String specifying the type of the displayed object being probed. Possible values are
    #: "ODB" and "XYPlot". This member is read-only.
    probeObject: str = ""

    @abaqus_method_doc
    def setValues(
        self,
        options: "ProbeOptions" = None,
        probeEntity: SymbolicConstant = ELEMENT,
        probeOutputPosition: SymbolicConstant = None,
        partInstance: Boolean = ON,
        elementID: Boolean = ON,
        elementType: Boolean = ON,
        elementConnectivity: Boolean = ON,
        elementFieldResults: Boolean = ON,
        nodeId: Boolean = ON,
        baseCoordinates: Boolean = ON,
        deformedCoordinates: Boolean = ON,
        attachedElements: Boolean = ON,
        nodeFieldResults: Boolean = ON,
        legend: Boolean = ON,
        xValue: Boolean = ON,
        yValue: Boolean = ON,
        sequenceID: Boolean = ON,
        interpolateXy: Boolean = OFF,
    ):
        """This method modifies the settings on the ProbeOptions object.

        Parameters
        ----------
        options
            A :py:class:`~abaqus.PathAndProbe.ProbeOptions.ProbeOptions` object from which values are to be copied. If other arguments are also
            supplied to setValues, they will override the values in **options**. The default value is
            None.
        probeEntity
            A SymbolicConstant specifying the entity being probed when **probeObject** = "ODB". Possible
            values are NODE and ELEMENT. The default value is ELEMENT.
        probeOutputPosition
            A SymbolicConstant specifying the output position to probe for field output results when
            **probeObject** = "ODB". Possible values are NODAL, INTEGRATION_POINT, ELEMENT_FACE,
            ELEMENT_NODAL, and ELEMENT_CENTROID.When **probeEntity** = NODE, the only possible value is
            NODAL. When **probeEntity** = ELEMENT, the only possible values are INTEGRATION_POINT,
            ELEMENT_FACE, ELEMENT_NODAL, and ELEMENT_CENTROID, and the default is INTEGRATION_POINT.
        partInstance
            A Boolean specifying whether to display the part instance information. This member is
            valid when **probeObject** = ODB. The default value is ON.
        elementID
            A Boolean specifying whether to display the element ID information. This member is valid
            when **probeObject** = ODB and **probeEntity** = ELEMENT. The default value is ON.
        elementType
            A Boolean specifying whether to display the element type information. This member is
            valid when **probeObject** = ODB and **probeEntity** = ELEMENT. The default value is ON.
        elementConnectivity
            A Boolean specifying whether to display the element connectivity. This member is valid
            when **probeObject** = ODB and **probeEntity** = ELEMENT. The default value is ON.
        elementFieldResults
            A Boolean specifying whether to display the element field output results. This member is
            valid when **probeObject** = ODB, **probeEntity** = ELEMENT, and **isFieldOutputAvailable** = ON.
            The default value is ON.
        nodeId
            A Boolean specifying whether to display the node ID when **probeObject** = ODB and
            **probeEntity** = NODE. The default value is ON.
        baseCoordinates
            A Boolean specifying whether to display the base coordinates of a node when
            **probeObject** = ODB and **probeEntity** = NODE. The default value is ON.
        deformedCoordinates
            A Boolean specifying whether to display the deformed coordinates of a node when
            **probeObject** = ODB and **probeEntity** = NODE. The default value is ON.
        attachedElements
            A Boolean specifying whether to display the elements attached to a node when
            **probeObject** = ODB and **probeEntity** = NODE. The default value is ON.
        nodeFieldResults
            A Boolean specifying whether to display the node field output results. This member is
            valid when **probeObject** = ODB, **probeEntity** = NODE, and **isFieldOutputAvailable** = ON. The
            default value is ON.
        legend
            A Boolean specifying whether to display the legend for a curve being probed. This member
            is valid when **probeObject** = XYPlot. The default value is ON.
        xValue
            A Boolean specifying whether to display the **x**-coordinate value of the point on the
            curve being probed. This member is valid when **probeObject** = XYPlot. The default value is
            ON.
        yValue
            A Boolean specifying whether to display the **y**-coordinate value of the point on the
            curve being probed. This member is valid when **probeObject** = XYPlot. The default value is
            ON.
        sequenceID
            A Boolean specifying whether to display the sequence ID of the point on the curve being
            probed. This member is valid when **probeObject** = XYPlot. The default value is ON.
        interpolateXy
            A Boolean specifying whether to interpolate values within a line segment when
            **probeObject** = XYPlot. When **interpolateXy** = OFF, probing returns the nearest **X - Y** data
            point on the curve. When **interpolateXy** = ON, probing interpolates data to return a value
            at the nearest point on the curve. The default value is OFF.
        """
        ...
