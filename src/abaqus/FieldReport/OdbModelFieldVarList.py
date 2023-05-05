from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class OdbModelFieldVarList:
    """The read-only OdbModelFieldVarList object lists all variables available for the model in the current
    OdbDisplay object.

    .. note::
        This object can be accessed by::

            import visualization
            session.viewports[name].layers[name].odbDisplay.modelVariableList
            session.viewports[name].odbDisplay.modelVariableList
    """

    ...
