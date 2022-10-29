# Sketcher

Sketcher commands are used to define the entities, such as the geometry, constraints, and dimensions, to create a sketch and to store the values and attributes associated with a particular sketch.

## Create constrained sketches

```{eval-rst}
.. autoclass:: abaqus.Sketcher.SketchModel.SketchModel

    .. autoclasstoc::

```

## Classes

```{eval-rst}

.. collapse:: Click here to Expand

    .. autoclass:: abaqus.Sketcher.ConstrainedSketch.ConstrainedSketch

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchVertexModel

        .. autoclasstoc::


    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.CoincidentConstraint.CoincidentConstraint

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.ConcentricConstraint.ConcentricConstraint

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.EqualDistanceConstraint.EqualDistanceConstraint

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.EqualLengthConstraint.EqualLengthConstraint

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.EqualRadiusConstraint.EqualRadiusConstraint

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.FixedConstraint.FixedConstraint

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.HorizontalConstraint.HorizontalConstraint

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.ParallelConstraint.ParallelConstraint

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.PerpendicularConstraint.PerpendicularConstraint

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.TangentConstraint.TangentConstraint

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.VerticalConstraint.VerticalConstraint

        .. autoclasstoc::


    .. autoclass:: abaqus.Sketcher.ConstrainedSketchDimension.AngularDimension.AngularDimension

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchDimension.DistanceDimension.DistanceDimension

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchDimension.HorizontalDimension.HorizontalDimension

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchDimension.ObliqueDimension.ObliqueDimension

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchDimension.RadialDimension.RadialDimension

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchDimension.VerticalDimension.VerticalDimension

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryArray.ConstrainedSketchGeometryArray

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.Arc3Points.Arc3Points

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.ArcByCenterEnds.ArcByCenterEnds

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.ArcByStartEndTangent.ArcByStartEndTangent

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.CircleByCenterPerimeter.CircleByCenterPerimeter

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.ConstructionCircleByCenterPerimeter.ConstructionCircleByCenterPerimeter

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.ConstructionLine.ConstructionLine

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.EllipseByCenterPerimeter.EllipseByCenterPerimeter

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.FilletByRadius.FilletByRadius

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.getPointAtDistance

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.Line.Line

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.Spline.Spline

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.Spot.Spot

        .. autoclasstoc::


    .. autoclass:: abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchParameter.Parameter.Parameter

        .. autoclasstoc::


    .. autoclass:: abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertex.ConstrainedSketchVertex

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexArray.ConstrainedSketchVertexArray

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchVertex.Spot.Spot

        .. autoclasstoc::
```
