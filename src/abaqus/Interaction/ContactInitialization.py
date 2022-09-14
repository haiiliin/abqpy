from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class ContactInitialization:
    """The ContactInitialization object is the abstract base type for other
    ContactInitialization objects. The ContactInitialization object has no explicit
    constructor, members, or methods.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].contactInitializations[name]
    """

    ...
