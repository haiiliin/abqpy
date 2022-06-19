class NodeQuery:
    """The NodeQuery object specifies nodes and their coordinates in a path. The NodeQuery
    object has no constructor or methods. Abaqus creates the **nodeQuery** member when you
    import the visualization module.

    Attributes
    ----------
    nodeId: int
        An Int specifying the ID of the most recently queried node. If the last query was
        unsuccessful, **nodeID**=−1.
    nodePos: float
        A tuple of Floats specifying the **X**-, **Y**-, and **Z**-coordinates of the most recently
        queried node.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import visualization
        session.nodeQuery
    """

    # An Int specifying the ID of the most recently queried node. If the last query was
    # unsuccessful, **nodeID**=−1.
    nodeId: int = None

    # A tuple of Floats specifying the **X**-, **Y**-, and **Z**-coordinates of the most recently
    # queried node.
    nodePos: float = None
