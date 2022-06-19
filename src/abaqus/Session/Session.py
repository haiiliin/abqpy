from ..Animation.AnimationSession import AnimationSession
from ..DisplayGroup.DisplayGroupSession import DisplayGroupSession
from ..FieldReport.FieldReportSession import FieldReportSession
from ..Job.JobSession import JobSession
from ..Odb.OdbSession import OdbSession
from ..PathAndProbe.PathSession import PathSession
from ..XY.XYSession import XYSession


class Session(
    AnimationSession,
    DisplayGroupSession,
    FieldReportSession,
    JobSession,
    OdbSession,
    PathSession,
    XYSession,
):
    """The Session object has no constructor. Abaqus creates the **session** member when a
    session is started.

    Attributes
    ----------
    attachedToGui: Boolean
        A Boolean specifying whether an Abaqus interactive session is running.
    replayInProgress: Boolean
        A Boolean specifying whether Abaqus is executing a replay file.
    kernelMemoryFootprint: float
        A Float specifying the memory usage value for the Abaqus/CAE kernel process in
        megabytes.
    kernelMemoryMaxFootprint: float
        A Float specifying the maximum value for the memory usage for the Abaqus/CAE kernel
        process in megabytes.
    kernelMemoryLimit: float
        A Float specifying the limit for the memory use for the Abaqus/CAE kernel process in
        megabytes.
    colors: dict[str, Color]
        A repository of :py:class:`~abaqus.Session.Color.Color` objects.
    journalOptions: JournalOptions
        A :py:class:`~abaqus.Session.JournalOptions.JournalOptions` object specifying how to record selection of geometry in the journal
        and replay files.
    memoryReductionOptions: MemoryReductionOptions
        A :py:class:`~abaqus.Session.MemoryReductionOptions.MemoryReductionOptions` object specifying options for running in reduced memory mode.
    nodeQuery: NodeQuery
        A :py:class:`~abaqus.PathAndProbe.NodeQuery.NodeQuery` object specifying nodes and their coordinates in a path.
    sketcherOptions: ConstrainedSketcherOptions
        A :py:class:`~abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions` object specifying common options for all sketches.
    viewerOptions: ViewerOptions
        A :py:class:`~abaqus.OdbDisplay.ViewerOptions.ViewerOptions` object.
    animationOptions: AnimationOptions
        An :py:class:`~abaqus.Animation.AnimationOptions.AnimationOptions` object.
    aviOptions: AVIOptions
        An :py:class:`~abaqus.Animation.AVIOptions.AVIOptions` object.
    imageAnimationOptions: ImageAnimationOptions
        An :py:class:`~abaqus.Animation.ImageAnimationOptions.ImageAnimationOptions` object.
    imageAnimation: ImageAnimation
        An :py:class:`~abaqus.Animation.ImageAnimation.ImageAnimation` object.
    quickTimeOptions: QuickTimeOptions
        A :py:class:`~abaqus.Animation.QuickTimeOptions.QuickTimeOptions` object.
    viewports: dict[str, Viewport]
        A repository of :py:class:`~abaqus.Canvas.Viewport.Viewport` objects.
    customData: RepositorySupport
        A :py:class:`~abaqus.CustomKernel.RepositorySupport.RepositorySupport` object.
    defaultFieldReportOptions: FieldReportOptions
        A :py:class:`~abaqus.FieldReport.FieldReportOptions.FieldReportOptions` object.
    defaultFreeBodyReportOptions: FreeBodyReportOptions
        A :py:class:`~abaqus.FieldReport.FreeBodyReportOptions.FreeBodyReportOptions` object.
    fieldReportOptions: FieldReportOptions
        A :py:class:`~abaqus.FieldReport.FieldReportOptions.FieldReportOptions` object.
    freeBodyReportOptions: FreeBodyReportOptions
        A :py:class:`~abaqus.FieldReport.FreeBodyReportOptions.FreeBodyReportOptions` object.
    odbs: dict[str, Odb]
        A repository of :py:class:`~abaqus.Odb.Odb.Odb` objects.
    scratchOdbs: dict[str, ScratchOdb]
        A repository of :py:class:`~abaqus.Odb.ScratchOdb.ScratchOdb` objects.
    defaultOdbDisplay: DefaultOdbDisplay
        A :py:class:`~abaqus.OdbDisplay.DefaultOdbDisplay.DefaultOdbDisplay` object.
    defaultPlot: DefaultPlot
        A :py:class:`~abaqus.XY.DefaultPlot.DefaultPlot` object.
    defaultChartOptions: DefaultChartOptions
        A :py:class:`~abaqus.XY.DefaultChartOptions.DefaultChartOptions` object.
    odbData: dict[str, OdbData]
        A repository of :py:class:`~abaqus.PlotOptions.OdbData.OdbData` objects.
    mdbData: dict[str, MdbData]
        A repository of :py:class:`~abaqus.PlotOptions.MdbData.MdbData` objects.
    paths: dict[str, Path]
        A repository of :py:class:`~abaqus.PathAndProbe.Path.Path` objects.
    freeBodies: dict[str, FreeBody]
        A repository of :py:class:`~abaqus.PathAndProbe.FreeBody.FreeBody` objects.
    streams: dict[str, Stream]
        A repository of :py:class:`~abaqus.PathAndProbe.Stream.Stream` objects.
    spectrums: dict[str, Spectrum]
        A repository of :py:class:`~abaqus.PathAndProbe.Spectrum.Spectrum` objects.
    currentProbeValues: CurrentProbeValues
        A :py:class:`~abaqus.PathAndProbe.CurrentProbeValues.CurrentProbeValues` object.
    defaultProbeOptions: ProbeOptions
        A :py:class:`~abaqus.PathAndProbe.ProbeOptions.ProbeOptions` object.
    probeOptions: ProbeOptions
        A :py:class:`~abaqus.PathAndProbe.ProbeOptions.ProbeOptions` object.
    probeReport: ProbeReport
        A :py:class:`~abaqus.PathAndProbe.ProbeReport.ProbeReport` object.
    defaultProbeReport: ProbeReport
        A :py:class:`~abaqus.PathAndProbe.ProbeReport.ProbeReport` object.
    selectedProbeValues: SelectedProbeValues
        A :py:class:`~abaqus.PathAndProbe.SelectedProbeValues.SelectedProbeValues` object.
    printOptions: PrintOptions
        A :py:class:`~abaqus.Print.PrintOptions.PrintOptions` object.
    epsOptions: EpsOptions
        An :py:class:`~abaqus.Print.EpsOptions.EpsOptions` object.
    pageSetupOptions: PageSetupOptions
        A :py:class:`~abaqus.Print.PageSetupOptions.PageSetupOptions` object.
    pngOptions: PngOptions
        A :py:class:`~abaqus.Print.PngOptions.PngOptions` object.
    psOptions: PsOptions
        A :py:class:`~abaqus.Print.PsOptions.PsOptions` object.
    svgOptions: SvgOptions
        A :py:class:`~abaqus.Print.SvgOptions.SvgOptions` object.
    tiffOptions: TiffOptions
        A :py:class:`~abaqus.PredefinedField.TiffOptions.TiffOptions` object.
    autoColors: AutoColors
        An :py:class:`~abaqus.Session.AutoColors.AutoColors` object specifying the color palette to be used for color coding.
    xyColors: AutoColors
        An :py:class:`~abaqus.Session.AutoColors.AutoColors` object specifying the color palette to be used :py:class:`~.forXYCurve` objects.
    xyDataObjects: dict[str, XYData]
        A repository of :py:class:`~abaqus.XY.XYData.XYData` objects.
    curves: dict[str, XYCurve]
        A repository of :py:class:`~abaqus.XY.XYCurve.XYCurve` objects.
    xyPlots: dict[str, XYPlot]
        A repository of :py:class:`~abaqus.XY.XYPlot.XYPlot` objects.
    charts: dict[str, Chart]
        A repository of :py:class:`~abaqus.XY.Chart.Chart` objects.
    defaultXYReportOptions: XYReportOptions
        An :py:class:`~abaqus.XY.XYReportOptions.XYReportOptions` object.
    xyReportOptions: XYReportOptions
        An :py:class:`~abaqus.XY.XYReportOptions.XYReportOptions` object.
    views: dict[str, View]
        A repository of :py:class:`~abaqus.UtilityAndView.View.View` objects.
    networkDatabaseConnectors: dict[str, NetworkDatabaseConnector]
        A repository of :py:class:`~abaqus.Session.NetworkDatabaseConnector.NetworkDatabaseConnector` objects.
    displayGroups: dict[str, DisplayGroup]
        A repository of :py:class:`~abaqus.DisplayGroup.DisplayGroup.DisplayGroup` objects.
    graphicsInfo: GraphicsInfo
        A :py:class:`~abaqus.DisplayOptions.GraphicsInfo.GraphicsInfo` object.
    defaultGraphicsOptions: GraphicsOptions
        A :py:class:`~abaqus.DisplayOptions.GraphicsOptions.GraphicsOptions` object.
    graphicsOptions: GraphicsOptions
        A :py:class:`~abaqus.DisplayOptions.GraphicsOptions.GraphicsOptions` object.
    defaultViewportAnnotationOptions: ViewportAnnotationOptions
        A :py:class:`~abaqus.DisplayOptions.ViewportAnnotationOptions.ViewportAnnotationOptions` object.
    queues: dict[str, Queue]
        A repository of :py:class:`~abaqus.Job.Queue.Queue` objects.
    currentViewportName: str
        A String specifying the name of the current viewport.
    sessionState: dict
        A :py:class:`~.Dictionary` object specifying the viewports and their associated models. The :py:class:`~.Dictionary`
        key specifies the viewport name. The :py:class:`~.Dictionary` value is a :py:class:`~.Dictionary` specifying the
        model name.
    images: dict[str, Image]
        A repository of :py:class:`~abaqus.Session.Image.Image` objects.
    movies: dict[str, Movie]
        A repository of :py:class:`~abaqus.Animation.Movie.Movie` objects.
    defaultLightOptions: LightOptions
        A :py:class:`~abaqus.DisplayOptions.LightOptions.LightOptions` object.
    drawingArea: DrawingArea
        A :py:class:`~abaqus.Canvas.DrawingArea.DrawingArea` object.
    defaultMesherOptions: MesherOptions
        A :py:class:`~abaqus.Mesh.MesherOptions.MesherOptions` object specifying how to control default settings in the Mesh module.
    drawings: dict[str, Drawing]
        A repository of :py:class:`~abaqus.Session.Drawing.Drawing` objects.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        session
    """

    pass
