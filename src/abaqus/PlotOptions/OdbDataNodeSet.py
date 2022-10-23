from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class OdbDataNodeSet:
    """The OdbDataNodeSet object stores node set data.

    .. note::
        This object can be accessed by::

            import visualization
            session.odbData[name].nodeSets[i]
    """

    #: A String specifying the set name. This attribute is read-only.
    name: str = ""

    #: A String-to-tuple-of-Ints Dictionary specifying the nodes in the set. This attribute is
    #: read-only.
    nodes: str = ""
