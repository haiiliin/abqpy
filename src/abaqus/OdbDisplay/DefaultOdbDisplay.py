from abqpy.decorators import abaqus_class_doc

from ..PlotOptions.BasicOptions import BasicOptions
from ..PlotOptions.FreeBodyOptions import FreeBodyOptions
from ..PlotOptions.StreamOptions import StreamOptions
from ..PlotOptions.ViewCutOptions import ViewCutOptions
from .CommonOptions import CommonOptions
from .ContourOptions import ContourOptions
from .DisplayBodyOptions import DisplayBodyOptions
from .OrientationOptions import OrientationOptions
from .SuperimposeOptions import SuperimposeOptions
from .SymbolOptions import SymbolOptions


@abaqus_class_doc
class DefaultOdbDisplay:
    """The DefaultOdbDisplay object is a limited-functionality version of the OdbDisplay object.

    .. note::
        This object can be accessed by::

            import visualization
            session.defaultOdbDisplay
    """

    #: A BasicOptions object.
    basicOptions: BasicOptions = BasicOptions()

    #: A CommonOptions object.
    commonOptions: CommonOptions = CommonOptions()

    #: A ContourOptions object.
    contourOptions: ContourOptions = ContourOptions()

    #: A DisplayBodyOptions object.
    displayBodyOptions: DisplayBodyOptions = DisplayBodyOptions()

    #: A FreeBodyOptions object.
    freeBodyOptions: FreeBodyOptions = FreeBodyOptions()

    #: A StreamOptions object.
    streamOptions: StreamOptions = StreamOptions()

    #: An OrientationOptions object.
    materialOrientationOptions: OrientationOptions = OrientationOptions()

    #: A SuperimposeOptions object.
    superimposeOptions: SuperimposeOptions = SuperimposeOptions()

    #: A SymbolOptions object.
    symbolOptions: SymbolOptions = SymbolOptions()

    #: A ViewCutOptions object.
    viewCutOptions: ViewCutOptions = ViewCutOptions()
