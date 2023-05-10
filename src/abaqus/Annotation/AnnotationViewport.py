from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Canvas.ViewportBase import ViewportBase
from .Annotation import Annotation


@abaqus_class_doc
class AnnotationViewport(ViewportBase):
    """The following commands operate on Viewport objects. For more information about the Viewport object, see
    Viewport object.

    .. note::
        This object can be accessed by::

            import annotationToolset
    """

    @abaqus_method_doc
    def plotAnnotation(self, annotation: Annotation, index: int = 0):
        """This method plots an Annotation object in aViewport.

        Parameters
        ----------
        annotation
            An Annotation object to plot.
        index
            An Int specifying the index of the Annotation object in the sequence of annotations to
            plot. The default value is zero.
        """
        # TODO: implement this method
        ...
