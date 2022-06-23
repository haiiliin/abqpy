from .ConstrainedSketchConstraint.ConstrainedSketchConstraint import (
    ConstrainedSketchConstraint,
)
from .ConstrainedSketchDimension.ConstrainedSketchDimension import (
    ConstrainedSketchDimension,
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
from .ConstrainedSketchGeometry.ConstrainedSketchGeometryArray import (
    ConstrainedSketchGeometryArray
)


class ConstrainedSketchBase:
    """A :py:class:`~abaqus.Sketcher.ConstrainedSketch.ConstrainedSketch` object contains the entities that are used to create a sketch. The
    objects include ConstrainedSketchGeometry objects contained in the ConstrainedSketchGeometry Repository,
    such as Line, Arc, and Spline. ConstrainedSketchVertex, ConstrainedSketchDimension, ConstrainedSketchConstraint, and ConstrainedSketchParameter objects are
    contained in their respective repositories.

    Attributes
    ----------
    constraints: dict[str, ConstrainedSketchConstraint]
        A repository of :py:class:`~abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint` objects.
    dimensions: dict[str, ConstrainedSketchDimension]
        A repository of :py:class:`~abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimension.ConstrainedSketchDimension` objects.
    geometry: ConstrainedSketchGeometryArray
        A :py:class:`~abaqus.Amplitude.ConstrainedSketchGeometryArray.ConstrainedSketchGeometryArray` object specifying the sketch geometry, such as lines,
        arcs, circles, and splines.
    parameters: dict[str, ConstrainedSketchParameter]
        A repository of :py:class:`~abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameter.ConstrainedSketchParameter` objects specifying sketch parameters, which
        may be associated with dimensions.
    sketchOptions: ConstrainedSketchOptions
        A :py:class:`~abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions` object specifying the sketch option settings.
    vertices: ConstrainedSketchVertexArray
        A :py:class:`~abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexArray.ConstrainedSketchVertexArray` object.
    imageOptions: ConstrainedSketchImageOptions
        A :py:class:`~abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions` object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import sketch
        mdb.models[name].sketches[name]
    """

    #: A repository of ConstrainedSketchConstraint objects.
    constraints: dict[str, ConstrainedSketchConstraint] = dict[
        str, ConstrainedSketchConstraint
    ]()

    #: A repository of ConstrainedSketchDimension objects.
    dimensions: dict[str, ConstrainedSketchDimension] = dict[
        str, ConstrainedSketchDimension
    ]()

    #: A :py:class:`~abaqus.Amplitude.ConstrainedSketchGeometryArray.ConstrainedSketchGeometryArray` object specifying the sketch geometry, such as lines,
    #: arcs, circles, and splines.
    geometry: ConstrainedSketchGeometryArray = ConstrainedSketchGeometryArray()

    #: A repository of ConstrainedSketchParameter objects specifying sketch parameters, which
    #: may be associated with dimensions.
    parameters: dict[str, ConstrainedSketchParameter] = dict[
        str, ConstrainedSketchParameter
    ]()

    #: A :py:class:`~abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions` object specifying the sketch option settings.
    sketchOptions: ConstrainedSketchOptions = ConstrainedSketchOptions()

    #: A :py:class:`~abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexArray.ConstrainedSketchVertexArray` object.
    vertices: ConstrainedSketchVertexArray = ConstrainedSketchVertexArray()

    #: A :py:class:`~abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions` object.
    imageOptions: ConstrainedSketchImageOptions = ConstrainedSketchImageOptions()
