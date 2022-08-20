from .._decorators import abaqus_class_doc


@abaqus_class_doc
class OdbDataInstance:
    """The OdbDataInstance object instance data.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import visualization
            session.odbData[name].instances[i]
    """

    #: A String specifying the instance name. This attribute is read-only.
    name: str = ""
