import typing

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..Session.SessionBase import SessionBase
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class XYSessionBase(SessionBase):
    """The following commands operate on Session objects. For more information about the
    Session object, see Session object.

    .. note:: 
        This object can be accessed by::

            import visualization
    """

    @abaqus_method_doc
    def linearizeStress(
        self,
        name: str,
        path: str,
        startPoint: str,
        endPoint: str,
        modelShape: SymbolicConstant,
        components: tuple,
        xyMembraneComps: tuple,
        xyBendingComps: tuple,
        invariantBendingComps: tuple = (),
        intervals: int = 40,
        radiusOfCurvature: float = None,
        oopRadiusOfCurvature: float = None,
        curvatureCorrection: Boolean = OFF,
        curvatureCsys: str = "",
        useCurvatureCsysForOrient: Boolean = OFF,
        saveXy: Boolean = OFF,
        writeReport: Boolean = OFF,
        reportFile: str = "",
        appendToFile: Boolean = OFF,
        saveToPath: Boolean = OFF,
    ):
        """This method is used to perform stress linearization along a defined stress line.

        Parameters
        ----------
        name
            A String specifying the name of the stress line.
        path
            APath object specifying the end points of the stress line.Note:You must provide either
            the **path** argument or the **startPoint** and **endPoint** arguments.
        startPoint
            A String specifying a part instance and a node belonging to that part instance, or a
            sequence of three Floats specifying the coordinates of a point.
        endPoint
            A String specifying a part instance and a node belonging to that part instance, or a
            sequence of three Floats specifying the coordinates of a point.
        modelShape
            A SymbolicConstant specifying the model shape to be used for obtaining coordinates of
            the intermediate points along the stress line. Possible values are UNDEFORMED and
            DEFORMED. When DEFORMED is selected, the deformation scale factor is always set to a
            uniform value of 1.0.
        components
            A sequence of Strings specifying the linearized stress components to be displayed in the
            xyPlot object. Possible values are "S11", "S22", "S33", "S12", "S23", and "S13".Note:You
            must provide at least one of the **components** , **xyMembraneComps** , and **xyBendingComps**
            arguments.
        xyMembraneComps
            A sequence of Strings specifying the linearized stress membrane components to be
            displayed in the xyPlot object. Possible values are "S11", "S22", "S33", "S12", "S23",
            and "S13".
        xyBendingComps
            A sequence of Strings specifying the linearized stress bending components to be
            displayed in the xyPlot object. Possible values are "S11", "S22", "S33", "S12", "S23",
            and "S13".
        invariantBendingComps
            A sequence of Strings specifying the linearized stress bending components to be included
            in the computation of the linearized stress invariants. Possible values are "S11",
            "S22", "S33", "S12", "S23", and "S13". The default value of the sequence includes all
            the possible values.
        intervals
            An Int specifying the number of equally-spaced intervals into which the stress line is
            to be divided. The default value is 40.
        radiusOfCurvature
            A Float specifying the in-plane radius of curvature of the center section along the
            stress line for axi-symmetric models. The default value is ∞∞.
        oopRadiusOfCurvature
            A Float specifying the out-of-plane radius of curvature of the center section along the
            Stress Line for axi-symmetric models. The default value forces Abaqus to compute the
            radius of curvature.
        curvatureCorrection
            A Boolean specifying whether the out-of-plane curvature correction should be applied for
            non-axisymmetric models when performing linearized stress computations. Curvature
            correction is always applied for axisymmetric models. The default value is OFF.
        curvatureCsys
            A String specifying the name of the user-defined local coordinate system to be used for
            computing the out-of-plane radius of curvature for non-axisymmetric models when
            **curvatureCorrection** =ON . The default value uses the global coordinate system to
            compute the out-of-plane radius of curvature.
        useCurvatureCsysForOrient
            A Boolean specifying whether to use the user-defined local coordinate system to compute
            the local stress line orientation for non-axisymmetric models when **curvatureCorrection**
            =ON and **curvatureCsys** is specified. The default value is OFF.
        saveXy
            A Boolean specifying whether to save the xyData objects created during the stress
            linearization operation to the session. The default value is OFF .
        writeReport
            A Boolean specifying whether to write the output from the stress linearization operation
            to a text file. The default value is ON .
        reportFile
            A String specifying the report file name. The default value is “linearStress.rpt”.
        appendToFile
            A Boolean specifying whether to append output from the stress linearization to the text
            file specified by the **reportFile** argument. The default value is ON .
        saveToPath
            A Boolean specifying whether to create a Path object containing all the points used when
            performing the linearized stress computation. The default value is OFF . When this
            argument is set to ON , a Path object is created with the same name as that of the
            stress line and placed in the Path repository.

        Returns
        -------
        typing.List[XYData]
            A list of xyData objects.

        Raises
        ------
        TextError
            The stress line passes through incompatible part instances. Results cannot be
            extracted.
        TextError
            Specified variables cannot be used for extracting results along the stress line.
        TextError
            Results for all the points along the stress line were not found. Selected end points
            and all intermediate sample points must lie within the current display group, and within
            solid continuum elements. Due to tolerance limitations, intermediate points lying on
            display group boundaries may fail to meet this criterion. Choose new end points, adjust
            the number of intervals along the line, or modify the current display group to obtain
            the stress linearization plot.
        """
        ...

    @abaqus_method_doc
    def setPathTolerance(self, tolerance: str = 0):
        """This method is used to set the **tolerance** to be used when creating XYData objects by
        extracting results along Path objects. This command should be exercised with caution
        since setting a value too low or too high may result in getting no results or
        unpredictable results.

        Parameters
        ----------
        tolerance
            A Double specifying the tolerance. The default value is 0.00001.

        Returns
        -------
        None .
        """
        ...

    @abaqus_method_doc
    def getPathTolerance(self):
        """This method is used to get the **tolerance** used when creating XYData objects by
        extracting results along Path objects.

        Returns
        -------
        float
            A Double specifying the tolerance.
        """
        ...

    @abaqus_method_doc
    def setLimitForXYDataPlots(self, limit: int = None):
        """This method is used to set the **limit** for number of XY data objects while creating
        XYData from field output.

        Parameters
        ----------
        limit
            None or an Int specifying the limit for number of XY data objects. The default value is
            no limit

        Returns
        -------
        None .
        """
        ...

    @abaqus_method_doc
    def getLimitForXYDataPlots(self):
        """This method is used to get the **limit** for number of XY data objects while creating
        XYData from field output.

        Returns
        -------
        int 
            Int specifying the limit for number of XY data objects.
        """
        ...
