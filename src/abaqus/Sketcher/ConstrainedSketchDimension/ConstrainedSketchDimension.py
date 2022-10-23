from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class ConstrainedSketchDimension:
    """The ConstrainedSketchDimension object stores the dimensions associated with a sketch.

    .. note::
        This object can be accessed by::

            import sketch
            mdb.models[name].sketches[name].dimensions[i]
    """

    ...
