from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class DesignResponse:
    """The DesignResponse object is the abstract base type for other DesignResponse objects.
    The DesponseResponse object has no explicit constructor. The methods and members of the
    DesignResponse object are common to all objects derived from DesignResponse.

    .. note::
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].designResponses[name]
    """

    #: A String specifying the design response repository key.
    name: str = ""
