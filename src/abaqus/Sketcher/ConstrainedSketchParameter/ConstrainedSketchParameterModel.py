from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..ConstrainedSketchBase import ConstrainedSketchBase


@abaqus_class_doc
class ConstrainedSketchParameterModel(ConstrainedSketchBase):
    """A :py:class:`~abaqus.Sketcher.ConstrainedSketch.ConstrainedSketch` object contains the entities that are used to create a sketch. The
    objects include ConstrainedSketchGeometry objects contained in the ConstrainedSketchGeometry Repository,
    such as Line, Arc, and Spline. ConstrainedSketchVertex, ConstrainedSketchDimension, ConstrainedSketchConstraint, and ConstrainedSketchParameter objects are
    contained in their respective repositories.

    .. note:: 
        This object can be accessed by::

            import sketch
            mdb.models[name].sketches[name]
    """

    @abaqus_method_doc
    def ConstrainedSketchParameter(
        self,
        name: str,
        path: str = "",
        expression: str = "",
        previousParameter: str = "",
    ):
        """This method creates a parameter and optionally associates a dimension with this
        parameter.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].ConstrainedSketchParameter

        Parameters
        ----------
        name
            A String specifying the name of the ConstrainedSketchParameter object. No two parameters
            in the same ConstrainedSketch can have the same name.
        path
            A String specifying the ConstrainedSketchDimension object with which this parameter is
            associated.
        expression
            A String specifying the expression or value associated with the
            ConstrainedSketchParameter.
        previousParameter
            A String specifying the name of the previous ConstrainedSketchParameter, if it exists.
            The **previousParameter** argument implies an order among the parameters. No two
            parameters can reference the same parameter as the previous parameter.

        Returns
        -------
        obj: ConstrainedSketchParameter
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameter.ConstrainedSketchParameter` object
        """
        ...
