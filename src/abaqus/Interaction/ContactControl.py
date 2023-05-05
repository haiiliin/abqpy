from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class ContactControl:
    """The ContactControl object is the abstract base type for other ContactControl objects. The ContactControl
    object has no explicit constructor, members, or methods.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].contactControls[name]
    """

    ...
