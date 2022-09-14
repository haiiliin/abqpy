from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class OdbDataSurfaceSet:
    """The OdbDataSurfaceSet object stores surface set data.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.odbData[name].surfaceSets[i]
    """

    #: A String specifying the set name. This attribute is read-only.
    name: str = ""

    #: A String-to-tuple-of-Ints Dictionary specifying the elements in the set. This attribute
    #: is read-only.
    elements: str = ""

    #: A String-to-tuple-of-Ints Dictionary specifying the facets corresponding to the
    #: **elements**. This attribute is read-only.
    facets: str = ""
