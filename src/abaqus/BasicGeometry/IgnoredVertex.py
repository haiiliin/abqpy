from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class IgnoredVertex:
    """An :py:class:`~abaqus.BasicGeometry.IgnoredVertex.IgnoredVertex` object is a point region of the geometry that was abstracted away by a
    virtual topology feature.

    .. note:: 
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].ignoredVertices[i]
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].ignoredVertices[i]
            mdb.models[name].rootAssembly.instances[name].ignoredVertices[i]
    """

    #: An Int specifying the index of the IgnoredVertex in the IgnoredVertexArray.
    index: int = None

    #: A tuple of Floats specifying the **X**-, **Y**-, and **Z**-coordinates of the vertex.
    pointOn: float = None
