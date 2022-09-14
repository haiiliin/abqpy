from abqpy.decorators import abaqus_class_doc
from .OdbInstance import OdbInstance
from .OdbPart import OdbPart
from .SectionPoint import SectionPoint
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class FieldBulkData:
    """The FieldBulkData object represents the entire field data for a class of elements or
    nodes. All elements in a class correspond to the same element type and material.

    .. note:: 
        This object can be accessed by::

            import odbAccess
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].bulkDataBlocks[i]
    """

    #: A SymbolicConstant specifying the position of the output in the element. Possible values
    #: are:
    #: 
    #: - NODAL, specifying the values calculated at the nodes.
    #: - INTEGRATION_POINT, specifying the values calculated at the integration points.
    #: - ELEMENT_NODAL, specifying the values obtained by extrapolating results calculated at
    #:   the integration points.
    #: - ELEMENT_FACE.
    #: - CENTROID, specifying the value at the centroid obtained by extrapolating results
    #:   calculated at the integration points.
    position: SymbolicConstant = None

    #: A SymbolicConstant specifying the output type. Possible values are SCALAR, VECTOR,
    #: TENSOR_3D_FULL, TENSOR_3D_PLANAR, TENSOR_3D_SURFACE, TENSOR_2D_PLANAR, and
    #: TENSOR_2D_SURFACE.
    type: SymbolicConstant = None

    #: An :py:class:`~abaqus.Odb.OdbInstance.OdbInstance` object specifying the part to which the labels belong.
    instance: OdbInstance = OdbInstance(
        "instance", OdbPart("part", THREE_D, DEFORMABLE_BODY)
    )

    #: A :py:class:`~abaqus.Odb.SectionPoint.SectionPoint` object specifying the section point number of the current block of data.
    sectionPoint: SectionPoint = None

    #: A sequence of Ints specifying the element labels of the elements in the block.
    #: **elementLabels** is valid only if **position** = INTEGRATION_POINT, CENTROID, ELEMENT_NODAL,
    #: or ELEMENT_FACE.
    elementLabels: tuple = ()

    #: A sequence of Ints specifying the node labels of the nodes in the block. **nodelabels** is
    #: valid only if **position** = ELEMENT_NODAL or NODAL.
    nodeLabels: tuple = ()

    #: A sequence of Strings specifying the component labels.
    componentLabels: tuple = ()

    #: A sequence of Ints specifying the integration points in the elements in the block.
    #: **integrationPoints** is available only if **position** = INTEGRATION_POINT.
    integrationPoints: tuple = ()

    #: A tuple of Floats specifying data in the form described by **type**. If **type** = TENSOR or
    #: VECTOR, **data** is a sequence containing the components for each element or node in the
    #: block. If the underlying data are in double precision, an exception will be thrown.
    data: tuple = ()

    #: A tuple of Floats specifying data in the form described by **type**. If **type** = TENSOR or
    #: VECTOR, **conjugateData** is a sequence containing the imaginary part of the components
    #: for each element or node in the block. If the underlying data are in double precision,
    #: an exception will be thrown.
    conjugateData: tuple = ()

    #: A sequence of Floats specifying the calculated von Mises stress at each output location
    #: in the block of element data, or NULL. The value is valid only when the
    #: **validInvariants** member includes MISES; otherwise, the value is indeterminate.
    #: Conjugate data will be ignored in invariant calculation.
    mises: tuple = ()

    #: A pointer to an array of Floats specifying the quaternion representing the local
    #: coordinate system (the rotation from global to local) at each output location. The
    #: quaternion is returned in the form q=(q,q0), which is the reverse of that shown in
    #: [Rotation
    #: variables](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAETHERefMap/simathe-c-rotationvars.htm?ContextScope=all).
    #: **localCoordSystem** is available for TENSOR data written in a local coordinate system. It
    #: is also available for VECTOR data for connector element outputs. For connector element
    #: outputs the quaternion form is q=(q0,q)q=(q0,q), which represents the rotation from
    #: local to global. If the underlying data are in double precision, an exception will be
    #: thrown.
    localCoordSystem: float = None
