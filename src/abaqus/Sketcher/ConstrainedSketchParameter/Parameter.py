from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ConstrainedSketchParameter import ConstrainedSketchParameter


@abaqus_class_doc
class Parameter(ConstrainedSketchParameter):
    @abaqus_method_doc
    def __init__(
        self, name: str, path: str = "", expression: str = "", previous: str = ""
    ):
        """This method creates a parameter and optionally associates a dimension with this
        parameter.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].Parameter

        ----------

        Parameters
        ----------
        name
            A String specifying the name of the ConstrainedSketch object. No two parameters
            in the same ConstrainedSketch can have the same name.
        path
            A String specifying the ConstrainedSketchDimension object with which this parameter is
            associated.
        expression
            A String specifying the expression or value associated with the
            ConstrainedSketch.
        previous
            A String specifying the name of the previous ConstrainedSketch, if it exists.
            The **previous** argument implies an order among the parameters. No two
            parameters can reference the same parameter as the previous parameter.

        Returns
        -------
        sketch: ConstrainedSketch
            A :py:class:`~abaqus.Sketcher.ConstrainedSketch.ConstrainedSketch` object.

        """
        ...
