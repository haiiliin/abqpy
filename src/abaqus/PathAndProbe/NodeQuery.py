import typing
from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class NodeQuery:
    """The NodeQuery object specifies nodes and their coordinates in a path. The NodeQuery
    object has no constructor or methods. Abaqus creates the **nodeQuery** member when you
    import the visualization module.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.nodeQuery
    """

    #: An Int specifying the ID of the most recently queried node. If the last query was
    #: unsuccessful, **nodeID** = −1.
    nodeId: typing.Optional[int] = None

    #: A tuple of Floats specifying the **X**-, **Y**-, and **Z**-coordinates of the most recently
    #: queried node.
    nodePos: typing.Optional[float] = None
