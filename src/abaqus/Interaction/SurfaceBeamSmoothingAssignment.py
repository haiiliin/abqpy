from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class SurfaceBeamSmoothingAssignment:
    """The SurfaceBeamSmoothingAssignment object stores the surface beam smoothing assignment definition for
    surfaces in ContactStd objects. The SurfaceBeamSmoothingAssignment object has no constructor or members.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name].surfaceBeamSmoothingAssignments

        The corresponding analysis keywords are:

        - SURFACE PROPERTY ASSIGNMENT

    .. versionadded:: 2021
        The ``SurfaceBeamSmoothingAssignment`` class was added.
    """

    @abaqus_method_doc
    def changeValuesInStep(self, stepName: str, index: int, value: float):
        """This method allows modification of surface beam smoothing assignments already defined on surfaces in
        a given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the surface beam smoothing assignments
            are to be modified.
        index
            An Int specifying the position of the surface beam smoothing assignment whose value is
            to be modified.
        value
            A tuple specifying the value of the surface beam smoothing assignments for the surface
            whose index is referenced. Each tuple contains one entry:A Float specifying the surface
            beam smoothing value to be used for the surface.
        """
        ...

    @abaqus_method_doc
    def appendInStep(self, stepName: str, assignments: tuple):
        """This method allows addition of surface beam smoothing assignments to new surfaces in a given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which new surface beam smoothing assignments
            are to be defined.
        assignments
            A sequence of tuples specifying the surface beam smoothing assignments. Each tuple
            contains two entries:A region object specifying the surface to which the smoothing is
            assigned.A Float specifying the surface smoothing value to be used for the surface.
        """
        ...

    @abaqus_method_doc
    def delete(self, indices: tuple):
        """The delete method allows you to delete existing surface beam smoothing assignments from ContactStd
        objects.

        Parameters
        ----------
        indices
            A sequence of Ints specifying the index of each surface beam smoothing assignment to
            delete.
        """
        ...
