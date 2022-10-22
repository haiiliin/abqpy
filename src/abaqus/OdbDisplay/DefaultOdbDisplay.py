from abqpy.decorators import abaqus_class_doc

from .CommonOptions import CommonOptions
from .ContourOptions import ContourOptions
from .DisplayBodyOptions import DisplayBodyOptions
from .OrientationOptions import OrientationOptions
from .SuperimposeOptions import SuperimposeOptions
from .SymbolOptions import SymbolOptions
from ..PlotOptions.BasicOptions import BasicOptions
from ..PlotOptions.FreeBodyOptions import FreeBodyOptions
from ..PlotOptions.StreamOptions import StreamOptions
from ..PlotOptions.ViewCutOptions import ViewCutOptions


@abaqus_class_doc
class DefaultOdbDisplay:
    """The DefaultOdbDisplay object is a limited-functionality version of the OdbDisplay
    object.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.defaultOdbDisplay
    """

    #: A :py:class:`~abaqus.PlotOptions.BasicOptions.BasicOptions` object.
    basicOptions: BasicOptions = BasicOptions()

    #: A :py:class:`~abaqus.OdbDisplay.CommonOptions.CommonOptions` object.
    commonOptions: CommonOptions = CommonOptions()

    #: A :py:class:`~abaqus.OdbDisplay.ContourOptions.ContourOptions` object.
    contourOptions: ContourOptions = ContourOptions()

    #: A :py:class:`~abaqus.OdbDisplay.DisplayBodyOptions.DisplayBodyOptions` object.
    displayBodyOptions: DisplayBodyOptions = DisplayBodyOptions()

    #: A :py:class:`~abaqus.PlotOptions.FreeBodyOptions.FreeBodyOptions` object.
    freeBodyOptions: FreeBodyOptions = FreeBodyOptions()

    #: A :py:class:`~abaqus.PlotOptions.StreamOptions.StreamOptions` object.
    streamOptions: StreamOptions = StreamOptions()

    #: An :py:class:`~abaqus.OdbDisplay.OrientationOptions.OrientationOptions` object.
    materialOrientationOptions: OrientationOptions = OrientationOptions()

    #: A :py:class:`~abaqus.OdbDisplay.SuperimposeOptions.SuperimposeOptions` object.
    superimposeOptions: SuperimposeOptions = SuperimposeOptions()

    #: A :py:class:`~abaqus.OdbDisplay.SymbolOptions.SymbolOptions` object.
    symbolOptions: SymbolOptions = SymbolOptions()

    #: A :py:class:`~abaqus.PlotOptions.ViewCutOptions.ViewCutOptions` object.
    viewCutOptions: ViewCutOptions = ViewCutOptions()
