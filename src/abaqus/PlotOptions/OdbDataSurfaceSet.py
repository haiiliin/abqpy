class OdbDataSurfaceSet:
    """The OdbDataSurfaceSet object stores surface set data.

    Attributes
    ----------
    name: str
        A String specifying the set name. This attribute is read-only.
    elements: str
        A String-to-tuple-of-Ints Dictionary specifying the elements in the set. This attribute
        is read-only.
    facets: str
        A String-to-tuple-of-Ints Dictionary specifying the facets corresponding to the
        **elements**. This attribute is read-only.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

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
