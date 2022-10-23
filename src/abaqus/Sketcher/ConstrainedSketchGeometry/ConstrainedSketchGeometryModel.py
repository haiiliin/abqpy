from typing_extensions import Literal
from typing import Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..ConstrainedSketchBase import ConstrainedSketchBase
from ...UtilityAndView.abaqusConstants import abaqusConstants as C
from ...UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class ConstrainedSketchGeometryModel(ConstrainedSketchBase):
    """A :py:class:`~abaqus.Sketcher.ConstrainedSketch.ConstrainedSketch` object contains the entities that are used to create a sketch. The
    objects include ConstrainedSketchGeometry objects contained in the ConstrainedSketchGeometry Repository,
    such as Line, Arc, and Spline. ConstrainedSketchVertex, ConstrainedSketchDimension, ConstrainedSketchConstraint, and ConstrainedSketchParameter objects are
    contained in their respective repositories.

    .. note:: 
        This object can be accessed by::

            import sketch
            mdb.models[name].sketches[name]
    """

    @abaqus_method_doc
    def Arc3Points(
        self, point1: Sequence[float], point2: Sequence[float], point3: Sequence[float]
    ):
        """This method constructs an arc using a two endpoints and an intermediate third point on
        the arc.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].Arc3Points

        Parameters
        ----------
        point1
            A pair of Floats specifying the first endpoint of the arc.
        point2
            A pair of Floats specifying the second endpoint of the arc.
        point3
            A pair of Floats specifying the third point on the arc.

        Returns
        -------
        geometry: ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object
        """
        ...

    @abaqus_method_doc
    def ArcByCenterEnds(
        self,
        center: Sequence[float],
        point1: Sequence[float],
        point2: Sequence[float],
        direction: Literal[C.COUNTERCLOCKWISE, C.CLOCKWISE],
    ):
        """This method constructs an arc using a center point and two vertices. The Arc object is
        added to the geometry repository of the ConstrainedSketch object. The arc is created in
        a clockwise fashion from **point1** to **point2**.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].ArcByCenterEnds

        Parameters
        ----------
        center
            A pair of Floats specifying the center point of the arc.
        point1
            A pair of Floats specifying the first endpoint of the arc.
        point2
            A pair of Floats specifying the second endpoint of the arc.
        direction
            A SymbolicConstant specifying the direction of the arc. Possible values are CLOCKWISE
            and COUNTERCLOCKWISE.

        Returns
        -------
        geometry: ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object

        Raises
        ------
        If incompatible data are given, the second endpoint is ignored
        """
        ...

    @abaqus_method_doc
    def ArcByStartEndTangent(
        self, point1: Sequence[float], point2: Sequence[float], vector: tuple
    ):
        """This method constructs an arc using two vertices. The Arc object is added to the
        geometry repository of the ConstrainedSketch object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].ArcByStartEndTangent

        Parameters
        ----------
        point1
            A pair of Floats specifying the first endpoint of the arc.
        point2
            A pair of Floats specifying the second endpoint of the arc.
        vector
            A sequence of two Floats specifying the start direction for constructing the arc.

        Returns
        -------
        geometry: ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object
        """
        ...

    @abaqus_method_doc
    def CircleByCenterPerimeter(self, center: Sequence[float], point1: Sequence[float]):
        """This method constructs a circle using a center point and a point on the perimeter. The
        circle is added to the geometry repository of the ConstrainedSketch object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].CircleByCenterPerimeter

        Parameters
        ----------
        center
            A pair of Floats specifying the center point of the circle.
        point1
            A pair of Floats specifying a point on the perimeter of the circle.

        Returns
        -------
        geometry: ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object
        """
        ...

    @abaqus_method_doc
    def ConstructionCircleByCenterPerimeter(
        self, center: Sequence[float], point1: Sequence[float]
    ):
        """This method constructs a construction circle using a center point and a point on the
        perimeter. The circle is added to the geometry repository of the ConstrainedSketch
        object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].ConstructionCircleByCenterPerimeter

        Parameters
        ----------
        center
            A pair of Floats specifying the center point of the construction circle.
        point1
            A pair of Floats specifying a point on the perimeter of the construction circle.

        Returns
        -------
        geometry: ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object
        """
        ...

    @abaqus_method_doc
    def EllipseByCenterPerimeter(
        self, center: Sequence[float], axisPoint1: Sequence[float], axisPoint2: Sequence[float]
    ):
        """This method constructs an ellipse using a center point, a major axis point, and a minor
        axis point. The ellipse is added to the geometry repository of the ConstrainedSketch
        object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].EllipseByCenterPerimeter

        Parameters
        ----------
        center
            A pair of Floats specifying the center point of the ellipse.
        axisPoint1
            A pair of Floats specifying the major or minor axis point of the ellipse.
        axisPoint2
            A pair of Floats specifying the minor or major axis point of the ellipse.

        Returns
        -------
        geometry: ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object
        """
        ...

    @abaqus_method_doc
    def FilletByRadius(
        self,
        radius: float,
        curve1: "ConstrainedSketchGeometryModel",
        nearPoint1: Sequence[float],
        curve2: "ConstrainedSketchGeometryModel",
        nearPoint2: Sequence[float],
    ):
        """This method constructs a fillet arc of a given radius between two curves. The fillet is
        added to the geometry repository of the ConstrainedSketch object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].FilletByRadius

        Parameters
        ----------
        radius
            A Float specifying the radius of the fillet arc. Possible values are Floats > 0.
        curve1
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object specifying the first curve.
        nearPoint1
            A pair of Floats specifying a point on the sketch near where the user wishes the fillet
            to intersect with **curve1**. This point does not need to be on*curve1*; it is used as a
            hint to draw the fillet.
        curve2
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object specifying the second curve.
        nearPoint2
            A pair of Floats specifying a point on the sketch near where the user wishes the fillet
            to intersect with **curve2**. This point does not need to be on **curve2**; it is used as a
            hint to draw the fillet.

        Returns
        -------
        geometry: ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object

        Raises
        ------
        Range Error: cannot construct the Fillet specified
            If the radius given cannot be used to create a fillet between the two curves given.
        """
        ...

    @abaqus_method_doc
    def Line(self, point1: Sequence[float], point2: Sequence[float]):
        """This method creates a line between two given points.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].Line

        Parameters
        ----------
        point1
            A pair of Floats specifying the first endpoint.
        point2
            A pair of Floats specifying the second endpoint.

        Returns
        -------
        geometry: ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object
        """
        ...

    @abaqus_method_doc
    def ConstructionLine(self, point1: Sequence[float], point2: Sequence[float]):
        """This method creates an oblique construction line that runs between two given points.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].ConstructionLine

        Parameters
        ----------
        point1
            A pair of Floats specifying the first endpoint.
        point2
            A pair of Floats specifying the second endpoint.

        Returns
        -------
        geometry: ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object
        """
        ...

    @abaqus_method_doc
    def Spline(self, points: tuple, constrainPoints: Boolean = True):
        """This method creates a spline curve running through a sequence of points.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].Spline

        Parameters
        ----------
        points
            A sequence of pairs of Floats specifying the points through which the spline passes.
        constrainPoints
            A Boolean that determines whether the points given are to constrained to always remain
            on the Spline. The default is True. For a large sequence of **points**, significant
            performance gains may be achieved by setting the value to False.

        Returns
        -------
        geometry: ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object
        """
        ...

    @abaqus_method_doc
    def Spot(self, point: Sequence[float]):
        """This method creates a spot construction point located at the specified coordinates. The
        spot is added to the vertex repository of the ConstrainedSketch object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].Spot

        Parameters
        ----------
        point
            A pair of Floats specifying the coordinates of the spot construction point.

        Returns
        -------
        geometry: ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object
        """
        ...

    @abaqus_method_doc
    def getVertices(self):
        """This method returns an list of ConstrainedSketchVertex objects which are a part of the
        given ConstrainedSketchGeometry object.

        Returns
        -------
        vertices: List[ConstrainedSketchVertex]
            A list of ConstrainedSketchVertex objects
        """
        ...

    @abaqus_method_doc
    def getSize(self):
        """This method returns the length of the given ConstrainedSketchGeometry object.

        Returns
        -------
        length: int
            The length of the given ConstrainedSketchGeometry
        """
        ...

    @abaqus_method_doc
    def getPointAtDistance(
        self, point: Sequence[float], distance: str, percentage: Boolean = OFF
    ):
        """This method returns a point offset along the given ConstrainedSketchGeometry from the
        given end by a specified arc length distance or a percentage of the total length of the
        ConstrainedSketchGeometry object.

        Parameters
        ----------
        point
            A pair of Floats specifying the point from which the distance is to be measured.
        distance
            A float specifying the arc length distance along the ConstrainedSketchGeometry from the
            **point** at which the required point is situated.
        percentage
            A Boolean that specifies if the **distance** is an absolute distance or is a fraction
            relative to the length of the ConstrainedSketchGeometry object.

        Returns
        -------
        points: Sequence[float]
            A pair of floats representing the point along the edge
        """
        ...
