from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class ConstrainedSketchConstraint:
    """The ConstrainedSketchConstraint object stores the constraints associated with a sketch.

    .. note:: 
        This object can be accessed by::

            import sketch
            mdb.models[name].sketches[name].constraints[i]
    """

    ...
