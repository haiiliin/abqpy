from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class InteractionProperty:
    """The InteractionProperty object is the abstract base type for other InteractionProperty
    objects. The InteractionProperty object has no explicit constructor, members, or
    methods.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactionProperties[name]
    """

    ...
