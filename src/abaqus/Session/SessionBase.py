import typing

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .AutoColors import AutoColors
from .Color import Color
from .Drawing import Drawing
from .Image import Image
from .JournalOptions import JournalOptions
from .MemoryReductionOptions import MemoryReductionOptions
from .NetworkDatabaseConnector import NetworkDatabaseConnector
from ..Animation.AVIOptions import AVIOptions
from ..Animation.AnimationOptions import AnimationOptions
from ..Animation.ImageAnimation import ImageAnimation
from ..Animation.ImageAnimationOptions import ImageAnimationOptions
from ..Animation.Movie import Movie
from ..Animation.QuickTimeOptions import QuickTimeOptions
from ..Canvas.Canvas import Canvas
from ..Canvas.DrawingArea import DrawingArea
from ..Canvas.Viewport import Viewport
from ..CustomKernel.RepositorySupport import RepositorySupport
from ..DisplayGroup.DisplayGroup import DisplayGroup
from ..DisplayOptions.GraphicsInfo import GraphicsInfo
from ..DisplayOptions.GraphicsOptions import GraphicsOptions
from ..DisplayOptions.LightOptions import LightOptions
from ..DisplayOptions.ViewportAnnotationOptions import ViewportAnnotationOptions
from ..FieldReport.FieldReportOptions import FieldReportOptions
from ..FieldReport.FreeBodyReportOptions import FreeBodyReportOptions
from ..Job.Queue import Queue
from ..Mesh.MesherOptions import MesherOptions
from ..Odb.Odb import Odb
from ..Odb.ScratchOdb import ScratchOdb
from ..OdbDisplay.DefaultOdbDisplay import DefaultOdbDisplay
from ..OdbDisplay.ViewerOptions import ViewerOptions
from ..PathAndProbe.CurrentProbeValues import CurrentProbeValues
from ..PathAndProbe.FreeBody import FreeBody
from ..PathAndProbe.NodeQuery import NodeQuery
from ..PathAndProbe.Path import Path
from ..PathAndProbe.ProbeOptions import ProbeOptions
from ..PathAndProbe.ProbeReport import ProbeReport
from ..PathAndProbe.SelectedProbeValues import SelectedProbeValues
from ..PathAndProbe.Spectrum import Spectrum
from ..PathAndProbe.Stream import Stream
from ..PlotOptions.MdbData import MdbData
from ..PlotOptions.OdbData import OdbData
from ..PredefinedField.TiffOptions import TiffOptions
from ..Print.EpsOptions import EpsOptions
from ..Print.PageSetupOptions import PageSetupOptions
from ..Print.PngOptions import PngOptions
from ..Print.PrintOptions import PrintOptions
from ..Print.PsOptions import PsOptions
from ..Print.SvgOptions import SvgOptions
from ..Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions import (
    ConstrainedSketcherOptions,
)
from ..UtilityAndView.View import View
from ..UtilityAndView.abaqusConstants import *
from ..XY.Chart import Chart
from ..XY.DefaultChartOptions import DefaultChartOptions
from ..XY.DefaultPlot import DefaultPlot
from ..XY.XYCurve import XYCurve
from ..XY.XYData import XYData
from ..XY.XYPlot import XYPlot
from ..XY.XYReportOptions import XYReportOptions


@abaqus_class_doc
class SessionBase:
    """The Session object has no constructor. Abaqus creates the **session** member when a
    session is started.

    .. note:: 
        This object can be accessed by::

            session
    """

    #: A Boolean specifying whether an Abaqus interactive session is running.
    attachedToGui: Boolean = OFF

    #: A Boolean specifying whether Abaqus is executing a replay file.
    replayInProgress: Boolean = OFF

    #: A Float specifying the memory usage value for the Abaqus/CAE kernel process in
    #: megabytes.
    kernelMemoryFootprint: float = None

    #: A Float specifying the maximum value for the memory usage for the Abaqus/CAE kernel
    #: process in megabytes.
    kernelMemoryMaxFootprint: float = None

    #: A Float specifying the limit for the memory use for the Abaqus/CAE kernel process in
    #: megabytes.
    kernelMemoryLimit: float = None

    #: A repository of Color objects.
    colors: typing.Dict[str, Color] = {}

    #: A :py:class:`~abaqus.Session.JournalOptions.JournalOptions` object specifying how to record selection of geometry in the journal
    #: and replay files.
    journalOptions: JournalOptions = JournalOptions()

    #: A :py:class:`~abaqus.Session.MemoryReductionOptions.MemoryReductionOptions` object specifying options for running in reduced memory mode.
    memoryReductionOptions: MemoryReductionOptions = MemoryReductionOptions()

    #: A :py:class:`~abaqus.PathAndProbe.NodeQuery.NodeQuery` object specifying nodes and their coordinates in a path.
    nodeQuery: NodeQuery = NodeQuery()

    #: A :py:class:`~abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions` object specifying common options for all sketches.
    sketcherOptions: ConstrainedSketcherOptions = ConstrainedSketcherOptions()

    #: A :py:class:`~abaqus.OdbDisplay.ViewerOptions.ViewerOptions` object.
    viewerOptions: ViewerOptions = ViewerOptions()

    #: An :py:class:`~abaqus.Animation.AnimationOptions.AnimationOptions` object.
    animationOptions: AnimationOptions = AnimationOptions()

    #: An :py:class:`~abaqus.Animation.AVIOptions.AVIOptions` object.
    aviOptions: AVIOptions = AVIOptions()

    #: An :py:class:`~abaqus.Animation.ImageAnimationOptions.ImageAnimationOptions` object.
    imageAnimationOptions: ImageAnimationOptions = ImageAnimationOptions()

    #: An :py:class:`~abaqus.Animation.ImageAnimation.ImageAnimation` object.
    imageAnimation: ImageAnimation = ImageAnimation("img", AVI)

    #: A :py:class:`~abaqus.Animation.QuickTimeOptions.QuickTimeOptions` object.
    quickTimeOptions: QuickTimeOptions = QuickTimeOptions()

    #: A repository of Viewport objects.
    viewports: typing.Dict[str, Viewport] = {}

    #: A :py:class:`~abaqus.CustomKernel.RepositorySupport.RepositorySupport` object.
    customData: RepositorySupport = RepositorySupport()

    #: A :py:class:`~abaqus.FieldReport.FieldReportOptions.FieldReportOptions` object.
    defaultFieldReportOptions: FieldReportOptions = FieldReportOptions()

    #: A :py:class:`~abaqus.FieldReport.FreeBodyReportOptions.FreeBodyReportOptions` object.
    defaultFreeBodyReportOptions: FreeBodyReportOptions = FreeBodyReportOptions()

    #: A :py:class:`~abaqus.FieldReport.FieldReportOptions.FieldReportOptions` object.
    fieldReportOptions: FieldReportOptions = FieldReportOptions()

    #: A :py:class:`~abaqus.FieldReport.FreeBodyReportOptions.FreeBodyReportOptions` object.
    freeBodyReportOptions: FreeBodyReportOptions = FreeBodyReportOptions()

    #: A repository of Odb objects.
    odbs: typing.Dict[str, Odb] = {}

    #: A repository of ScratchOdb objects.
    scratchOdbs: typing.Dict[str, ScratchOdb] = {}

    #: A :py:class:`~abaqus.OdbDisplay.DefaultOdbDisplay.DefaultOdbDisplay` object.
    defaultOdbDisplay: DefaultOdbDisplay = DefaultOdbDisplay()

    #: A :py:class:`~abaqus.XY.DefaultPlot.DefaultPlot` object.
    defaultPlot: DefaultPlot = DefaultPlot()

    #: A :py:class:`~abaqus.XY.DefaultChartOptions.DefaultChartOptions` object.
    defaultChartOptions: DefaultChartOptions = DefaultChartOptions()

    #: A repository of OdbData objects.
    odbData: typing.Dict[str, OdbData] = {}

    #: A repository of MdbData objects.
    mdbData: typing.Dict[str, MdbData] = {}

    #: A repository of Path objects.
    paths: typing.Dict[str, Path] = {}

    #: A repository of FreeBody objects.
    freeBodies: typing.Dict[str, FreeBody] = {}

    #: A repository of Stream objects.
    streams: typing.Dict[str, Stream] = {}

    #: A repository of Spectrum objects.
    spectrums: typing.Dict[str, Spectrum] = {}

    #: A :py:class:`~abaqus.PathAndProbe.CurrentProbeValues.CurrentProbeValues` object.
    currentProbeValues: CurrentProbeValues = CurrentProbeValues()

    #: A :py:class:`~abaqus.PathAndProbe.ProbeOptions.ProbeOptions` object.
    defaultProbeOptions: ProbeOptions = ProbeOptions()

    #: A :py:class:`~abaqus.PathAndProbe.ProbeOptions.ProbeOptions` object.
    probeOptions: ProbeOptions = ProbeOptions()

    #: A :py:class:`~abaqus.PathAndProbe.ProbeReport.ProbeReport` object.
    probeReport: ProbeReport = ProbeReport()

    #: A :py:class:`~abaqus.PathAndProbe.ProbeReport.ProbeReport` object.
    defaultProbeReport: ProbeReport = ProbeReport()

    #: A :py:class:`~abaqus.PathAndProbe.SelectedProbeValues.SelectedProbeValues` object.
    selectedProbeValues: SelectedProbeValues = SelectedProbeValues()

    #: A :py:class:`~abaqus.Print.PrintOptions.PrintOptions` object.
    printOptions: PrintOptions = PrintOptions()

    #: An :py:class:`~abaqus.Print.EpsOptions.EpsOptions` object.
    epsOptions: EpsOptions = EpsOptions()

    #: A :py:class:`~abaqus.Print.PageSetupOptions.PageSetupOptions` object.
    pageSetupOptions: PageSetupOptions = PageSetupOptions()

    #: A :py:class:`~abaqus.Print.PngOptions.PngOptions` object.
    pngOptions: PngOptions = PngOptions()

    #: A :py:class:`~abaqus.Print.PsOptions.PsOptions` object.
    psOptions: PsOptions = PsOptions()

    #: A :py:class:`~abaqus.Print.SvgOptions.SvgOptions` object.
    svgOptions: SvgOptions = SvgOptions()

    #: A :py:class:`~abaqus.PredefinedField.TiffOptions.TiffOptions` object.
    tiffOptions: TiffOptions = TiffOptions()

    #: An :py:class:`~abaqus.Session.AutoColors.AutoColors` object specifying the color palette to be used for color coding.
    autoColors: AutoColors = AutoColors()

    #: An :py:class:`~abaqus.Session.AutoColors.AutoColors` object specifying the color palette to be used forXYCurve objects.
    xyColors: AutoColors = AutoColors()

    #: A repository of XYData objects.
    xyDataObjects: typing.Dict[str, XYData] = {}

    #: A repository of XYCurve objects.
    curves: typing.Dict[str, XYCurve] = {}

    #: A repository of XYPlot objects.
    xyPlots: typing.Dict[str, XYPlot] = {}

    #: A repository of Chart objects.
    charts: typing.Dict[str, Chart] = {}

    #: An :py:class:`~abaqus.XY.XYReportOptions.XYReportOptions` object.
    defaultXYReportOptions: XYReportOptions = XYReportOptions()

    #: An :py:class:`~abaqus.XY.XYReportOptions.XYReportOptions` object.
    xyReportOptions: XYReportOptions = XYReportOptions()

    #: A repository of View objects.
    views: typing.Dict[str, View] = {}

    #: A repository of NetworkDatabaseConnector objects.
    networkDatabaseConnectors: typing.Dict[str, NetworkDatabaseConnector] = {}

    #: A repository of DisplayGroup objects.
    displayGroups: typing.Dict[str, DisplayGroup] = {}

    #: A :py:class:`~abaqus.DisplayOptions.GraphicsInfo.GraphicsInfo` object.
    graphicsInfo: GraphicsInfo = GraphicsInfo()

    #: A :py:class:`~abaqus.DisplayOptions.GraphicsOptions.GraphicsOptions` object.
    defaultGraphicsOptions: GraphicsOptions = GraphicsOptions()

    #: A :py:class:`~abaqus.DisplayOptions.GraphicsOptions.GraphicsOptions` object.
    graphicsOptions: GraphicsOptions = GraphicsOptions()

    #: A :py:class:`~abaqus.DisplayOptions.ViewportAnnotationOptions.ViewportAnnotationOptions` object.
    defaultViewportAnnotationOptions: ViewportAnnotationOptions = (
        ViewportAnnotationOptions()
    )

    #: A repository of Queue objects.
    queues: typing.Dict[str, Queue] = {}

    #: A String specifying the name of the current viewport.
    currentViewportName: str = ""

    #: A Dictionary object specifying the viewports and their associated models. The Dictionary
    #: key specifies the viewport name. The Dictionary value is a Dictionary specifying the
    #: model name.
    sessionState: dict = None

    #: A repository of Image objects.
    images: typing.Dict[str, Image] = {}

    #: A repository of Movie objects.
    movies: typing.Dict[str, Movie] = {}

    #: A :py:class:`~abaqus.DisplayOptions.LightOptions.LightOptions` object.
    defaultLightOptions: LightOptions = LightOptions()

    #: A :py:class:`~abaqus.Canvas.DrawingArea.DrawingArea` object.
    drawingArea: DrawingArea = DrawingArea()

    #: A :py:class:`~abaqus.Mesh.MesherOptions.MesherOptions` object specifying how to control default settings in the Mesh module.
    defaultMesherOptions: MesherOptions = MesherOptions()

    #: A repository of Drawing objects.
    drawings: typing.Dict[str, Drawing] = {}

    @abaqus_method_doc
    def setValues(self, kernelMemoryLimit: float = None):
        """This method modifies the Session object.

        Parameters
        ----------
        kernelMemoryLimit
            A Float specifying the memory limit value for the Abaqus/CAE kernel process in
            megabytes. If the limit is exceeded, Abaqus/CAE displays an error message.The default
            memory limit value for Windows 32-bit systems if not set is 1800 MB. Increasing the
            memory limit is not recommended unless you are using a Windows 32-bit system with the
            boot option `/3GB /userva = SizeInMBytes` to extend the amount of memory available for
            Abaqus/CAE. In this case the limit can be changed to 2800 MB.If the kernel memory size
            reaches the **abq_ker_memory** value or the virtual memory limit of the machine, the
            following message will be displayed: 
            
            `Operation did not complete due to a memory allocation failure.` 
            
            For optimal performance, the memory limit should be set to a value
            less than the physical amount of memory on the machine.The minimum setting allowed is
            256 MB.
        """
        ...

    @abaqus_method_doc
    def enableCADConnection(self, CADName: str, portNum: int = None):
        """This method enables the Abaqus/CAE listening port for the specified **CAD** system.

        Parameters
        ----------
        CADName
            A String specifying the CAD system. Available options are Pro/ENGINEER, CATIA V5, CATIA
            V6, NX and SolidWorks.
        portNum
            An Integer specifying the port number to be used by the CAD system to communicate with
            Abaqus/CAE. If unspecified, attempts will be made to identify an open port. The default
            ports used are as follow: Pro/E : 49178CATIA V5 : 49179SolidWorks : 49180NX : 49181CATIA
            V6 : 49182

        Returns
        -------
        int 
            The connection port number used for the CAD connection.
        """
        ...

    @abaqus_method_doc
    def isCADConnectionEnabled(self):
        """This method checks the status of CAD Connection.

        Returns
        -------
        Boolean
            A Boolean value of True if the CAD connection enabled and False if the CAD connection
            disabled.
        """
        ...

    @abaqus_method_doc
    def disableCADConnection(self, CADName: str):
        """This method disables an associative import CAD connection that was enabled.

        Parameters
        ----------
        CADName
            A String specifying the CAD system for which associative import will be disabled.
            Available options are Pro/ENGINEER, CATIA V5, and CATIA V6, NX and SolidWorks.
        """
        ...

    @abaqus_method_doc
    def enableParameterUpdate(self, CADName: str, CADVersion: str, CADPort: int = None):
        """This method enables parameter updates for ProE and NX by establishing a connection with
        the listening port previously setup by the CAD application.

        Parameters
        ----------
        CADName
            A String specifying the CAD system for which parameter update will be enabled. Available
            options are Pro/ENGINEER and NX.
        CADVersion
            A String specifying the CAD system version. Allowable options take the form of the
            specific CAD system plus a version string. Examples for Pro/ENGINEER are "Wildfire5" and
            "Creo4." An NX example is "NX11."
        CADPort
            An Integer specifying the port number to be used by Abaqus/CAE to communicate with the
            CAD system. If unspecified, attempts will be made to identify an open port. This port
            number is not the same as the **portNum** used by the associative import interface. The
            default CAD listening ports are as follow:ProE : 3344NX : 3344
        """
        ...

    @abaqus_method_doc
    def setCADPortNumber(self, CADName: str, Port: str):
        """This method enables parameter updates for CATIA V5 and CATIA V6 by establishing a
        connection with the listening port previously setup by the CAD application. This port
        number is used to send the parameter information to the CAD system.

        Parameters
        ----------
        CADName
            A String specifying the CAD system for which the port number will be saved. The
            available options are 'CATIA V5' and ' CATIA V6'.
        Port
            An integer specifying the port number to be used by Abaqus/CAE to send the modified
            parameters to the CAD system.
        """
        ...

    @abaqus_method_doc
    def updateCADParameters(
        self,
        modelName: str,
        CADName: str,
        parameterFile: str,
        CADPartFile: str,
        CADPartName: str = "",
    ):
        """This method updates the parameters for the specified model using the specified parameter
        file.

        Parameters
        ----------
        modelName
            A String specifying the model name to update.
        CADName
            A String specifying the CAD system for which Abaqus updates the parameters. The
            available options are 'Pro/ENGINEER', 'CATIA V5' and 'CATIA V6'.
        parameterFile
            A parameter file containing the parameters that were exposed in the CAD system using the
            `ABQ_` prefix.
        CADPartFile
            A file name specifying the CAD part file for which parameter update is triggered.For
            **CADName** = 'CATIA V5' or 'CATIA V6', you can specify either products or parts using this
            argument. If you specify a product, Abaqus updates all of the parts associated with that
            product.For **CADName** = 'Pro/ENGINEER', this argument is optional, and you can specify
            update for parts only. However, a single file can be associated with multiple parts in
            the case of family tables. In this case, Abaqus updates all listed parts.
        CADPartName
            An String specifying the part name to update. This part name should match the part name
            in the originating CAD system.If you specify neither **CADPartFile** nor **CADPartName**
            during an update in which you specified **CADName** = 'Pro/ENGINEER', Abaqus updates all of
            the parts in the specified file.
        """
        ...

    @abaqus_method_doc
    def disableParameterUpdate(self, CADName: str):
        """This method disables an associative CAD connection using parameters.

        Parameters
        ----------
        CADName
            A String specifying the CAD system for which the parameter update will be disabled.
            Available option is Pro/ENGINEER.
        """
        ...

    @abaqus_method_doc
    def printToFile(
        self,
        fileName: str,
        format: SymbolicConstant = PNG,
        canvasObjects: typing.Tuple[Canvas, ...] = (),
        compression: Boolean = OFF,
    ):
        """This method prints canvas objects to a file using the attributes stored in the
        PrintOptions object and the appropriate format options object.

        Parameters
        ----------
        fileName
            A String specifying the file to which the image is to be written. If no file extension
            is supplied, an extension is added based on the selected image format (.ps, .eps, .png,
            .tif, .svg, or .svgz).
        format
            A SymbolicConstant specifying the image format. Possible values are PNG, SVG, TIFF, PS,
            and EPS. The default value is PNG.
        canvasObjects
            A sequence of canvas objects (viewports, text strings, or arrows) to print. The default
            is to print all canvas objects.
        compression
            A Boolean specifying the format for an SVG file. It is only valid to use this argument
            when **format** is SVG. Possible values are False (Uncompressed) and True (Compressed).
        """
        ...

    @abaqus_method_doc
    def printToPrinter(
        self,
        printCommand: str = "",
        numCopies: int = 1,
        canvasObjects: typing.Tuple[Canvas, ...] = (),
    ):
        """This method prints canvas objects to a Windows printer or to a PostScript printer. The
        attributes used for printing to a Windows printer are stored in the PrintOptions object
        and the PageSetupOptions object; the attributes used for printing to a PostScript
        printer are stored in the PrintOptions object and the PsOptions object.

        Parameters
        ----------
        printCommand
            A String specifying the operating system command or printer name to issue for printing
            to the printer. The default value is “lpr” or the value specified by the printOptions
            method. If you create a script to print directly to a Windows printer, the
            **printCommand** must take the following
            form::
            
                session.printToPrinter.setValues(
                    printCommand='PRINTER[number of characters in name]:printername PROPERTIES[number of characters in properties]:document properties'
                )
                
            The `PROPERTIES` is a list of characters that represents the
            printing preferences for the selected Windows printer. The properties are not required
            in a script; the printed output will use the current settings for the selected printer.
            You can use `'PRINTER[7]: DEFAULT'` to specify the default Windows printer.
        numCopies
            An Int specifying the number of copies to print. Possible values are 1 ≤ **numCopies** ≤
            100. The default value is 1.
        canvasObjects
            A sequence of canvas objects (viewports, text strings, or arrows) to print. The default
            is to print all canvas objects.

        Raises
        ------
        SystemError: invalid print command
            If **printCommand** is invalid.
        SystemError: print command failed
            If the print command fails.
        RangeError: numCopies must be in the range 1 <= value <= 100
            If **numCopies** is out of range.
        TypeError: keyword error on compression
            If **compression** is specified when **format** is not SVG.
        """
        ...

    @abaqus_method_doc
    def saveOptions(self, directory: SymbolicConstant):
        """This method saves your customized display settings.

        Parameters
        ----------
        directory
            A SymbolicConstant specifying the directory in which Abaqus saves the file that will be
            used to restore your customized settings (abaqus_2021.gpr). Possible values are HOME and
            CURRENT.
        """
        ...

    @abaqus_method_doc
    def writeVrmlFile(
        self, fileName: str, format: Boolean = OFF, canvasObjects: typing.Tuple[Canvas, ...] = ()
    ):
        """This method exports the current viewport objects to a file.

        Parameters
        ----------
        fileName
            A String specifying the file to which the graphics data is to be written. If no file
            extension is supplied, an extension is added based on the selected format (.wrl, .wrz).
        format
            A Boolean specifying the format. Possible values are False (Uncompressed) and True
            (Compressed).
        canvasObjects
            A sequence of canvas objects (viewports, text strings, or arrows) to export.
        """
        ...

    @abaqus_method_doc
    def write3DXMLFile(
        self, fileName: str, format: Boolean = OFF, canvasObjects: typing.Tuple[Canvas, ...] = ()
    ):
        """This method exports the current viewport objects to a file.

        Parameters
        ----------
        fileName
            A String specifying the file to which the graphics data is to be written. If no file
            extension is supplied, (.3dxml) will be added.
        format
            A Boolean specifying the format. Possible values are False (Uncompressed) and True
            (Compressed).
        canvasObjects
            A sequence of canvas objects to export.
        """
        ...

    @abaqus_method_doc
    def writeOBJFile(self, fileName: str, canvasObjects: typing.Tuple[Canvas, ...] = ()):
        """This method exports the current viewport objects to a file.

        Parameters
        ----------
        fileName
            A String specifying the file to which the graphics data is to be written. If no file
            extension is supplied, (.obj) will be added.
        canvasObjects
            A sequence of canvas objects to export.
        """
        ...
    
    # The following method was originally in the `OdbCommands` page documentation
    # But it accessed only by `session` object.
    @abaqus_method_doc
    def openOdb(self, name: str, path: str = "", readOnly: Boolean = OFF) -> Odb:
        """This method opens an existing output database (`.odb`) file and creates a new Odb object.
        This method is accessed only via the session object inside Abaqus/CAE and adds the new
        Odb object to the session.odbs repository. This method allows you to open multiple
        output databases at the same time and to use the repository key to specify a particular
        output database. For example::

            import visualization
            session.openOdb(name='myOdb', path='stress.odb', readOnly=True)

        Parameters
        ----------
        name
            A String specifying the repository key. If the `name` is not the same as the `path` to the
            output database (`.odb`) file, the `path` must be specified as well. Additionally, to
            support backwards compatibility of the interface, if the `name` parameter is omitted,
            the `path` and `name` will be presumed to be the same.
        path
            A String specifying the path to an existing output database (`.odb`) file.
        readOnly
            A Boolean specifying whether the file will permit only read access or both read and
            write access. The initial value is TRUE when the output database file is opened from
            Abaqus/CAE, indicating that only read access will be permitted.

        Returns
        -------
        Odb
            An :py:class:`~abaqus.Odb.Odb.Odb` object.

        Raises
        ------
        OdbError: The database is from a previous release of Abaqus
            If the output database was generated by a previous release of Abaqus and needs
            upgrading, Run  `abaqus upgrade -job <newFilename> -odb <oldFileName>` to upgrade it.
        OdbError: Abaqus installation must be upgraded before this output database can be opened
            If the output database was generated by a newer release of Abaqus, and the
            installation of Abaqus needs upgrading.
        AbaqusError: Cannot open file <filename>
            If the file is not a valid database.
        """
        self.odbs[name] = odb = Odb(name)
        return odb
