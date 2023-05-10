from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Annotation.AnnotationViewport import AnnotationViewport
from .Layer import Layer


@abaqus_class_doc
class Viewport(AnnotationViewport):
    @abaqus_method_doc
    def Layer(self, name: str, copyViewName: str = "") -> Layer:
        """This method creates a Layer object in the Layer repository.

        .. note::
            This function can be accessed by::

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
            A Layer object.
        """
        self.layers[name] = layer = Layer(name, copyViewName)
        return layer
