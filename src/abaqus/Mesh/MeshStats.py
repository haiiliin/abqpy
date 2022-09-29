from typing import Optional

from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class MeshStats:
    """The MeshStats object is a query object for holding mesh statistics and is returned by
    the getMeshStats command. The object does not have any methods.

    .. note:: 
        This object can be accessed by::

            import mesh
    """

    #: An Int specifying the number of point elements.
    numPointElems: Optional[int] = None

    #: An Int specifying the number of line elements.
    numLineElems: Optional[int] = None

    #: An Int specifying the number of quadrilateral elements.
    numQuadElems: Optional[int] = None

    #: An Int specifying the number of triangular elements.
    numTriElems: Optional[int] = None

    #: An Int specifying the number of hexahedral elements.
    numHexElems: Optional[int] = None

    #: An Int specifying the number of wedge elements.
    numWedgeElems: Optional[int] = None

    #: An Int specifying the number of tetrahedral elements.
    numTetElems: Optional[int] = None

    #: An Int specifying the number of pyramid elements.
    numPyramidElems: Optional[int] = None

    #: An Int specifying the number of nodes.
    numNodes: Optional[int] = None

    #: An Int specifying the number of regions that contain a mesh.
    numMeshedRegions: Optional[int] = None
