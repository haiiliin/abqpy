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
    numPointElems: int = None

    #: An Int specifying the number of line elements.
    numLineElems: int = None

    #: An Int specifying the number of quadrilateral elements.
    numQuadElems: int = None

    #: An Int specifying the number of triangular elements.
    numTriElems: int = None

    #: An Int specifying the number of hexahedral elements.
    numHexElems: int = None

    #: An Int specifying the number of wedge elements.
    numWedgeElems: int = None

    #: An Int specifying the number of tetrahedral elements.
    numTetElems: int = None

    #: An Int specifying the number of pyramid elements.
    numPyramidElems: int = None

    #: An Int specifying the number of nodes.
    numNodes: int = None

    #: An Int specifying the number of regions that contain a mesh.
    numMeshedRegions: int = None
