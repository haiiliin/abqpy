from .PlyStackPlotOptions import PlyStackPlotOptions
from .._decorators import abaqus_class_doc


@abaqus_class_doc
class DetailPlotOptions:
    """The DetailPlotOptions object stores values and attributes associated with a Viewport
    object. The DetailPlotOptions object has no constructor command. Abaqus creates the
    **detailPlotOptions** member whenever a Viewport is created.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            session.viewports[name].detailPlotOptions
    """

    #: A :py:class:`~abaqus.PlotOptions.PlyStackPlotOptions.PlyStackPlotOptions` object.
    plyStackPlotOptions: PlyStackPlotOptions = PlyStackPlotOptions()
