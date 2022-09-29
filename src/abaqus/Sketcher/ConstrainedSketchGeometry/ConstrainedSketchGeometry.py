from typing import Optional

from abqpy.decorators import abaqus_class_doc
from ...UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class ConstrainedSketchGeometry:
    """The ConstrainedSketchGeometry object stores the geometry of a sketch, such as lines,
    circles, arcs, and construction lines.

    .. note:: 
        This object can be accessed by::

            import sketch
            mdb.models[name].sketches[name].geometry[i]
            mdb.models[name].sketches[name].geometry[i][i]
    """

    #: An Int specifying the index of the sketch entity in the ConstrainedSketchGeometryArray.
    id: Optional[int] = None

    #: A SymbolicConstant specifying the geometry of the sketch entity. Possible values are
    #: ARC, CIRCLE, ELLIPSE, LINE, and SPLINE.
    curveType: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the type of sketch entity. Possible values are REGULAR,
    #: REFERENCE, and CONSTRUCTION.
    type: Optional[SymbolicConstant] = None

    #: A tuple of Floats specifying the **X**- and*Y*-coordinates of a point located on the
    #: geometry.
    pointOn: Optional[float] = None
