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


class DefaultOdbDisplay:
    """The DefaultOdbDisplay object is a limited-functionality version of the OdbDisplay
    object.

    Attributes
    ----------
    basicOptions: BasicOptions
        A :py:class:`~abaqus.PlotOptions.BasicOptions.BasicOptions` object.
    commonOptions: CommonOptions
        A :py:class:`~abaqus.OdbDisplay.CommonOptions.CommonOptions` object.
    contourOptions: ContourOptions
        A :py:class:`~abaqus.OdbDisplay.ContourOptions.ContourOptions` object.
    displayBodyOptions: DisplayBodyOptions
        A :py:class:`~abaqus.OdbDisplay.DisplayBodyOptions.DisplayBodyOptions` object.
    freeBodyOptions: FreeBodyOptions
        A :py:class:`~abaqus.PlotOptions.FreeBodyOptions.FreeBodyOptions` object.
    streamOptions: StreamOptions
        A :py:class:`~abaqus.PlotOptions.StreamOptions.StreamOptions` object.
    materialOrientationOptions: OrientationOptions
        An :py:class:`~abaqus.OdbDisplay.OrientationOptions.OrientationOptions` object.
    superimposeOptions: SuperimposeOptions
        A :py:class:`~abaqus.OdbDisplay.SuperimposeOptions.SuperimposeOptions` object.
    symbolOptions: SymbolOptions
        A :py:class:`~abaqus.OdbDisplay.SymbolOptions.SymbolOptions` object.
    viewCutOptions: ViewCutOptions
        A :py:class:`~abaqus.PlotOptions.ViewCutOptions.ViewCutOptions` object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import visualization
        session.defaultOdbDisplay
    """

    # A BasicOptions object.
    basicOptions: BasicOptions = BasicOptions()

    # A CommonOptions object.
    commonOptions: CommonOptions = CommonOptions()

    # A ContourOptions object.
    contourOptions: ContourOptions = ContourOptions()

    # A DisplayBodyOptions object.
    displayBodyOptions: DisplayBodyOptions = DisplayBodyOptions()

    # A FreeBodyOptions object.
    freeBodyOptions: FreeBodyOptions = FreeBodyOptions()

    # A StreamOptions object.
    streamOptions: StreamOptions = StreamOptions()

    # An OrientationOptions object.
    materialOrientationOptions: OrientationOptions = OrientationOptions()

    # A SuperimposeOptions object.
    superimposeOptions: SuperimposeOptions = SuperimposeOptions()

    # A SymbolOptions object.
    symbolOptions: SymbolOptions = SymbolOptions()

    # A ViewCutOptions object.
    viewCutOptions: ViewCutOptions = ViewCutOptions()
