from .Layer import Layer
from ..Annotation.AnnotationViewport import AnnotationViewport
from .._decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class Viewport(AnnotationViewport):

    @abaqus_method_doc
    def Layer(self, name: str, copyViewName: str = "") -> Layer:
        """This method creates a Layer object in the Layer repository.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                session.viewports[name].Layer

        Parameters
        ----------
        name
            A String specifying the repository key.
        copyViewName
            A String specifying the name of the layer to copy.

        Returns
        -------
        Layer
            A :py:class:`~abaqus.Canvas.Layer.Layer` object.
        """
        self.layers[name] = layer = Layer(name, copyViewName)
        return layer
