class DesignResponse:
    """The DesignResponse object is the abstract base type for other DesignResponse objects.
    The DesponseResponse object has no explicit constructor. The methods and members of the
    DesignResponse object are common to all objects derived from DesignResponse.

    Attributes
    ----------
    name: str
        A String specifying the design response repository key.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import optimization
        mdb.models[name].optimizationTasks[name].designResponses[name]

    """

    # A String specifying the design response repository key.
    name: str = ""
