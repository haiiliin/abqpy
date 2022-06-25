class OdbFieldVarList(list[str]):
    """The read-only OdbFieldVarList object is a sequence listing all variables available for
    the current step and frame. Each item in the sequence is itself a sequence fully
    describing the given variable.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import visualization
            session.viewports[name].layers[name].odbDisplay.fieldVariables
            session.viewports[name].odbDisplay.fieldVariables
    """

    pass
