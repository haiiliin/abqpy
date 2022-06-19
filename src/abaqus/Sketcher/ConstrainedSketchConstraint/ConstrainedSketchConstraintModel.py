from ..ConstrainedSketchBase import ConstrainedSketchBase
from ..ConstrainedSketchGeometry.ConstrainedSketchGeometry import (
    ConstrainedSketchGeometry,
)
from ...BasicGeometry.Vertex import Vertex


class ConstrainedSketchConstraintModel(ConstrainedSketchBase):
    """A ConstrainedSketch object contains the entities that are used to create a sketch. The
    objects include ConstrainedSketchGeometry objects contained in the ConstrainedSketchGeometry Repository,
    such as Line, Arc, and Spline. ConstrainedSketchVertex, ConstrainedSketchDimension, ConstrainedSketchConstraint, and ConstrainedSketchParameter objects are
    contained in their respective repositories.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import sketch
        mdb.models[name].sketches[name]

    """

    def CoincidentConstraint(
        self, entity1: ConstrainedSketchGeometry, entity2: ConstrainedSketchGeometry
    ):
        """This method creates a coincident constraint. This constraint applies to two vertices, to
        a vertex and a ConstrainedSketchGeometry object, or to two ConstrainedSketchGeometry
        objects of the same type and constrains them to be coincident.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].sketches[name].CoincidentConstraint

        Parameters
        ----------
        entity1
            A ConstrainedSketchGeometry object or a ConstrainedSketchVertex object specifying the first object.
        entity2
            A ConstrainedSketchGeometry object or a ConstrainedSketchVertex object specifying the second object.

        Returns
        -------
        sketch: ConstrainedSketch
            A ConstrainedSketch object
        """
        pass

    def ConcentricConstraint(
        self, entity1: ConstrainedSketchGeometry, entity2: ConstrainedSketchGeometry
    ):
        """This method creates a concentric constraint. This constraint applies to any combination
        of circles, arcs, ellipses, and points and constrains them to be concentric. A
        concentric constraint implies that the center of ConstrainedSketchGeometry objects
        coincide.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].sketches[name].ConcentricConstraint

        Parameters
        ----------
        entity1
            A ConstrainedSketchGeometry object specifying the first arc, circle, ellipse, or sketch
            vertex.
        entity2
            A ConstrainedSketchGeometry object specifying the second arc, circle, ellipse, or sketch
            vertex.

        Returns
        -------
        sketch: ConstrainedSketch
            A ConstrainedSketch object
        """
        pass

    def EqualLengthConstraint(
        self, entity1: ConstrainedSketchGeometry, entity2: ConstrainedSketchGeometry
    ):
        """This method creates an equal length constraint. This constraint applies to lines and
        constrains them such that their lengths are equal.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].sketches[name].EqualLengthConstraint

        Parameters
        ----------
        entity1
            A ConstrainedSketchGeometry object specifying the first line.
        entity2
            A ConstrainedSketchGeometry object specifying the second line.

        Returns
        -------
        sketch: ConstrainedSketch
            A ConstrainedSketch object
        """
        pass

    def EqualRadiusConstraint(self, entity1: ConstrainedSketchGeometry, entity2: str):
        """This method creates an equal radius constraint. This constraint applies to circles and
        arcs and constrains them such that their radii are equal.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].sketches[name].EqualRadiusConstraint

        Parameters
        ----------
        entity1
            A ConstrainedSketchGeometry object specifying the first arc or circle.
        entity2
            A ConstrainedSketchGeometry specifying the second arc or circle.

        Returns
        -------
        sketch: ConstrainedSketch
            A ConstrainedSketch object
        """
        pass

    def FixedConstraint(self, entity: ConstrainedSketchGeometry):
        """This method creates a fixed constraint. This constraint applies to a
        ConstrainedSketchGeometry object or a ConstrainedSketchVertex object and constrains them to be fixed in
        space. Both the location and the shape of the sketch geometry is fixed.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].sketches[name].FixedConstraint

        Parameters
        ----------
        entity
            A ConstrainedSketchGeometry object or a ConstrainedSketchVertex object specifying the item to fix in
            space.

        Returns
        -------
        sketch: ConstrainedSketch
            A ConstrainedSketch object
        """
        pass

    def HorizontalConstraint(self, entity: ConstrainedSketchGeometry):
        """This method creates a horizontal constraint. This constraint applies to a line and
        constrains it to be horizontal.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].sketches[name].HorizontalConstraint

        Parameters
        ----------
        entity
            A ConstrainedSketchGeometry object specifying the line to constrain.

        Returns
        -------
        sketch: ConstrainedSketch
            A ConstrainedSketch object
        """
        pass

    def VerticalConstraint(self, entity: ConstrainedSketchGeometry):
        """This method creates a vertical constraint. This constraint applies to a line and
        constrains it to be vertical.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].sketches[name].VerticalConstraint

        Parameters
        ----------
        entity
            A ConstrainedSketchGeometry object specifying the line to constrain.

        Returns
        -------
        sketch: ConstrainedSketch
            A ConstrainedSketch object
        """
        pass

    def ParallelConstraint(
        self, entity1: ConstrainedSketchGeometry, entity2: ConstrainedSketchGeometry
    ):
        """This method creates a parallel constraint. This constraint applies to lines and
        constrains them to be parallel.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].sketches[name].ParallelConstraint

        Parameters
        ----------
        entity1
            A ConstrainedSketchGeometry object specifying the first line.
        entity2
            A ConstrainedSketchGeometry object specifying the second line.

        Returns
        -------
        sketch: ConstrainedSketch
            A ConstrainedSketch object
        """
        pass

    def PerpendicularConstraint(
        self, entity1: ConstrainedSketchGeometry, entity2: ConstrainedSketchGeometry
    ):
        """This method creates a perpendicular constraint. This constraint applies to different
        types of ConstrainedSketchGeometry objects and constrains them to be perpendicular to
        each other.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].sketches[name].PerpendicularConstraint

        Parameters
        ----------
        entity1
            A ConstrainedSketchGeometry object specifying the first object.
        entity2
            A ConstrainedSketchGeometry object specifying the second object.

        Returns
        -------
        sketch: ConstrainedSketch
            A ConstrainedSketch object
        """
        pass

    def EqualDistanceConstraint(
        self, entity1: str, entity2: ConstrainedSketchGeometry, midpoint: Vertex
    ):
        """This method creates an equal distance constraint. This constraint can be applied between
        a midpoint ConstrainedSketchVertex object and any other two ConstrainedSketchVertex objects or between a
        midpoint ConstrainedSketchVertex
        object and two ConstrainedSketchGeometry objects that are lines. The equal distance
        constraint forces the midpoint vertex to remain at an equal distance from the two other
        vertices or lines.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].sketches[name].EqualDistanceConstraint

        Parameters
        ----------
        entity1
            AConstrainedSketchGeometry object specifying the first line or ConstrainedSketchVertex object.
        entity2
            A ConstrainedSketchGeometry object specifying the second line or ConstrainedSketchVertex object.
        midpoint
            A ConstrainedSketchVertex object specifying the vertex that will be positioned an equal distance from
            **entity1** and **entity2**.

        Returns
        -------
        sketch: ConstrainedSketch
            A ConstrainedSketch object
        """
        pass

    def TangentConstraint(
        self, entity1: ConstrainedSketchGeometry, entity2: ConstrainedSketchGeometry
    ):
        """This method creates a tangent constraint. This constraint applies to different types of
        ConstrainedSketchGeometry objects and constrains them to remain tangential.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].sketches[name].TangentConstraint

        Parameters
        ----------
        entity1
            A ConstrainedSketchGeometry object specifying the first object.
        entity2
            A ConstrainedSketchGeometry object specifying the second object.

        Returns
        -------
        sketch: ConstrainedSketch
            A ConstrainedSketch object
        """
        pass
