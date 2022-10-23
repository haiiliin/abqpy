from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class Constraint:
    """The ConstrainedSketchConstraint object is the abstract base type for other ConstrainedSketchConstraint objects. The
    ConstrainedSketchConstraint object has no explicit constructor. The members of the ConstrainedSketchConstraint object are
    common to all objects derived from the ConstrainedSketchConstraint.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].constraints[name]
    """

    #: A String specifying the constraint repository key.
    name: str = ""

    #: A Boolean specifying whether the constraint is suppressed or not. The default value is
    #: OFF.
    suppressed: Boolean = OFF

    @abaqus_method_doc
    def resume(self):
        """This method resumes the constraint that was previously suppressed."""
        ...

    @abaqus_method_doc
    def suppress(self):
        """This method suppresses the constraint."""
        ...

    @abaqus_method_doc
    def delete(self, indices: tuple):
        """This method allows you to delete existing constraints.

        Parameters
        ----------
        indices
            A sequence of Ints specifying the index of each constraint to delete.
        """
        ...
