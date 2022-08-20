from .._decorators import abaqus_class_doc


@abaqus_class_doc
class ContactStabilization:
    """The ContactStabilization object is the abstract base type for other ContactStabilization
    objects. The ContactStabilization object has no explicit constructor, members, or
    methods.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import interaction
            mdb.models[name].contactStabilizations[name]
    """

    ...
