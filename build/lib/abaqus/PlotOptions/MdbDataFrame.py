from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class MdbDataFrame:
    """The MdbDataFrame object. There is one and only MdbDataFrame in a MdbDataStep.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.mdbData[name].steps[i].frames[i]
    """

    ...
