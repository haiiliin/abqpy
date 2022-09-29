import typing
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
    numPointElems: typing.Optional[int] = None

    #: An Int specifying the number of line elements.
    numLineElems: typing.Optional[int] = None

    #: An Int specifying the number of quadrilateral elements.
    numQuadElems: typing.Optional[int] = None

    #: An Int specifying the number of triangular elements.
    numTriElems: typing.Optional[int] = None

    #: An Int specifying the number of hexahedral elements.
    numHexElems: typing.Optional[int] = None

    #: An Int specifying the number of wedge elements.
    numWedgeElems: typing.Optional[int] = None

    #: An Int specifying the number of tetrahedral elements.
    numTetElems: typing.Optional[int] = None

    #: An Int specifying the number of pyramid elements.
    numPyramidElems: typing.Optional[int] = None

    #: An Int specifying the number of nodes.
    numNodes: typing.Optional[int] = None

    #: An Int specifying the number of regions that contain a mesh.
    numMeshedRegions: typing.Optional[int] = None
