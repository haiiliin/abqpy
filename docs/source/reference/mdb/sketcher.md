# Sketcher

Sketcher commands are used to define the entities, such as the geometry, constraints, and dimensions, to create a sketch and to store the values and attributes associated with a particular sketch.

## Create constrained sketches

```{eval-rst}
.. autoclass:: abaqus.Sketcher.SketchModel.SketchModel
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::

```

## Other Classes

```{eval-rst}

.. toggle::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketch.ConstrainedSketch
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchVertexModel
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::


    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.CoincidentConstraint.CoincidentConstraint
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.ConcentricConstraint.ConcentricConstraint
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.EqualDistanceConstraint.EqualDistanceConstraint
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.EqualLengthConstraint.EqualLengthConstraint
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.EqualRadiusConstraint.EqualRadiusConstraint
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.FixedConstraint.FixedConstraint
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.HorizontalConstraint.HorizontalConstraint
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.ParallelConstraint.ParallelConstraint
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.PerpendicularConstraint.PerpendicularConstraint
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.TangentConstraint.TangentConstraint
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.VerticalConstraint.VerticalConstraint
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::


    .. autoclass:: abaqus.Sketcher.ConstrainedSketchDimension.AngularDimension.AngularDimension
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchDimension.DistanceDimension.DistanceDimension
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchDimension.HorizontalDimension.HorizontalDimension
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchDimension.ObliqueDimension.ObliqueDimension
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchDimension.RadialDimension.RadialDimension
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchDimension.VerticalDimension.VerticalDimension
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryArray.ConstrainedSketchGeometryArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.Arc3Points.Arc3Points
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.ArcByCenterEnds.ArcByCenterEnds
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.ArcByStartEndTangent.ArcByStartEndTangent
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.CircleByCenterPerimeter.CircleByCenterPerimeter
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.ConstructionCircleByCenterPerimeter.ConstructionCircleByCenterPerimeter
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.ConstructionLine.ConstructionLine
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.EllipseByCenterPerimeter.EllipseByCenterPerimeter
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.FilletByRadius.FilletByRadius
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.getPointAtDistance
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.Line.Line
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.Spline.Spline
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.Spot.Spot
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::


    .. autoclass:: abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchParameter.Parameter.Parameter
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::


    .. autoclass:: abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertex.ConstrainedSketchVertex
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexArray.ConstrainedSketchVertexArray
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Sketcher.ConstrainedSketchVertex.Spot.Spot
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::
```
