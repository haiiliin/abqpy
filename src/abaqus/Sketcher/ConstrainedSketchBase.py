from __future__ import annotations

from abqpy.decorators import abaqus_class_doc

from .ConstrainedSketchConstraint.ConstrainedSketchConstraint import (
    ConstrainedSketchConstraint,
)
from .ConstrainedSketchDimension.ConstrainedSketchDimension import (
    ConstrainedSketchDimension,
)
from .ConstrainedSketchGeometry.ConstrainedSketchGeometryArray import (
    ConstrainedSketchGeometryArray,
)
from .ConstrainedSketchOptions.ConstrainedSketchImageOptions import (
    ConstrainedSketchImageOptions,
)
from .ConstrainedSketchOptions.ConstrainedSketchOptions import ConstrainedSketchOptions
from .ConstrainedSketchParameter.ConstrainedSketchParameter import (
    ConstrainedSketchParameter,
)
from .ConstrainedSketchVertex.ConstrainedSketchVertexArray import (
    ConstrainedSketchVertexArray,
)


@abaqus_class_doc
class ConstrainedSketchBase:
    """A ConstrainedSketch object contains the entities that are used to create a sketch. The objects include
    ConstrainedSketchGeometry objects contained in the ConstrainedSketchGeometry Repository, such as Line, Arc,
    and Spline. ConstrainedSketchVertex, ConstrainedSketchDimension, ConstrainedSketchConstraint, and
    ConstrainedSketchParameter objects are contained in their respective repositories.

    .. note::
        This object can be accessed by::

            import sketch
            mdb.models[name].sketches[name]
    """

    #: A repository of ConstrainedSketchConstraint objects.
    constraints: dict[str, ConstrainedSketchConstraint] = {}

    #: A repository of ConstrainedSketchDimension objects.
    dimensions: dict[str, ConstrainedSketchDimension] = {}

    #: A ConstrainedSketchGeometryArray object specifying the sketch geometry, such as lines,
    #: arcs, circles, and splines.
    geometry: ConstrainedSketchGeometryArray = ConstrainedSketchGeometryArray()

    #: A repository of ConstrainedSketchParameter objects specifying sketch parameters, which
    #: may be associated with dimensions.
    parameters: dict[str, ConstrainedSketchParameter] = {}

    #: A ConstrainedSketchOptions object specifying the sketch option settings.
    sketchOptions: ConstrainedSketchOptions = ConstrainedSketchOptions()

    #: A ConstrainedSketchVertexArray object.
    vertices: ConstrainedSketchVertexArray = ConstrainedSketchVertexArray()

    #: A ConstrainedSketchImageOptions object.
    imageOptions: ConstrainedSketchImageOptions = ConstrainedSketchImageOptions()
