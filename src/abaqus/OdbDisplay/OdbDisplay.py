from typing import overload, Dict, Optional, Tuple, Union

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .CommonOptions import CommonOptions
from .ContourOptions import ContourOptions
from .DisplayBodyOptions import DisplayBodyOptions
from .OrientationOptions import OrientationOptions
from .SuperimposeOptions import SuperimposeOptions
from .SymbolOptions import SymbolOptions
from .ViewCut import ViewCut
from ..DisplayGroup.DisplayGroup import DisplayGroup
from ..DisplayGroup.DisplayGroupInstanceRepository import DisplayGroupInstanceRepository
from ..DisplayGroup.Leaf import Leaf
from ..FieldReport.OdbFieldVarList import OdbFieldVarList
from ..FieldReport.OdbModelFieldVarList import OdbModelFieldVarList
from ..Odb.OdbFrame import OdbFrame
from ..Odb.OdbSet import OdbSet
from ..PlotOptions.BasicOptions import BasicOptions
from ..PlotOptions.DisplayOptions import DisplayOptions
from ..PlotOptions.FreeBodyOptions import FreeBodyOptions
from ..PlotOptions.StreamOptions import StreamOptions
from ..PlotOptions.ViewCutOptions import ViewCutOptions
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class OdbDisplay:
    """The OdbDisplay object stores the context of an output database for a viewport. The
    OdbDisplay object has no constructor. Abaqus creates the **defaultOdbDisplay** member when
    you import the Visualization module. Abaqus creates the **odbDisplay** member when a
    viewport is created, using the attributes from the previous active viewport. The
    previous active viewport contains the attributes from the **defaultOdbDisplay** object for
    the session. The attributes from the **defaultOdbDisplay** object are copied from the
    previous active viewport to create the new viewport.
    OdbDisplay objects are accessed in one of two ways:
    - The default output database display options. These settings are used as defaults when
    other **odbDisplay** members are created and can be set to customize user preferences.
    - The output database display options associated with a particular viewport.

    .. note:: 
        This object can be accessed by::

            session.viewports[name].layers[name].odbDisplay
            import visualization
            session.viewports[name].odbDisplay
    """

    #: A String specifying the name of the output database associated with the OdbDisplay
    #: object.
    name: str = ""

    #: A tuple of Strings specifying field steps.
    #: Each item in the sequence consists of a tuple that contains the following step
    #: information:
    #: 
    #: - **element0**: A String specifying the step name.
    #: - **element1**: A String specifying the step description.
    #: - **element2**: A Float specifying the time value at the start of the step.
    #: - **element3**: A Float specifying the time period of the step.
    #: - **element4**: A Float specifying the user modified time period of the step.
    #: - **element5**: An Int specifying the domain type of the step. Possible values are:
    #: 
    #:   - 0: Time domain
    #:   - 1: Frequency domain
    #:   - 2: Modal domain
    #:   - 3: Arc Length (Riks) domain
    #: 
    #: - **element6**: A String specifying the default frame label.
    #: - **element7**: A sequence of strings specifying the frame labels for all available frames
    #:   in the step.
    #: - **element8**: A sequence of floats specifying the frame values for all available frames
    #:   in the step.
    #: - **element9**: A Int specifying whether the step is user defined. Possible values are 0
    #:   indicating the step is defined in the analysis and 1 indicating the step is user
    #:   defined.
    #: - **element10**: A sequence of machine readable strings encoding the currently active
    #:   frame numbers.
    fieldSteps: tuple = ()

    #: An :py:class:`~abaqus.FieldReport.OdbFieldVarList.OdbFieldVarList` object.
    fieldVariables: OdbFieldVarList = OdbFieldVarList()

    #: An :py:class:`~abaqus.FieldReport.OdbModelFieldVarList.OdbModelFieldVarList` object.
    modelVariableList: OdbModelFieldVarList = OdbModelFieldVarList()

    #: A repository of OdbSet objects specifying the set label. The repository is read-only.
    nodeSet: Dict[str, OdbSet] = {}

    #: A repository of OdbSet objects specifying the set label. The repository is read-only.
    elementSet: Dict[str, OdbSet] = {}

    #: A repository of OdbSet objects specifying the set label. The repository is read-only.
    surfaceSet: Dict[str, OdbSet] = {}

    #: A :py:class:`~abaqus.PlotOptions.DisplayOptions.DisplayOptions` object.
    display: DisplayOptions = DisplayOptions()

    #: A :py:class:`~abaqus.OdbDisplay.ContourOptions.ContourOptions` object.
    contourOptions: ContourOptions = ContourOptions()

    #: A :py:class:`~abaqus.OdbDisplay.CommonOptions.CommonOptions` object.
    commonOptions: CommonOptions = CommonOptions()

    #: A :py:class:`~abaqus.OdbDisplay.SymbolOptions.SymbolOptions` object.
    symbolOptions: SymbolOptions = SymbolOptions()

    #: A :py:class:`~abaqus.OdbDisplay.SuperimposeOptions.SuperimposeOptions` object.
    superimposeOptions: SuperimposeOptions = SuperimposeOptions()

    #: A :py:class:`~abaqus.OdbDisplay.DisplayBodyOptions.DisplayBodyOptions` object.
    displayBodyOptions: DisplayBodyOptions = DisplayBodyOptions()

    #: A :py:class:`~abaqus.PlotOptions.FreeBodyOptions.FreeBodyOptions` object.
    freeBodyOptions: FreeBodyOptions = FreeBodyOptions()

    #: A :py:class:`~abaqus.PlotOptions.StreamOptions.StreamOptions` object.
    streamOptions: StreamOptions = StreamOptions()

    #: A :py:class:`~abaqus.PlotOptions.ViewCutOptions.ViewCutOptions` object.
    viewCutOptions: ViewCutOptions = ViewCutOptions()

    #: A repository of ViewCut objects.
    viewCuts: Dict[str, ViewCut] = {}

    #: A :py:class:`~abaqus.DisplayGroup.DisplayGroup.DisplayGroup` object specifying the current display group and referring to an object in
    #: the **displayGroups** member of Session.
    displayGroup: DisplayGroup = DisplayGroup("dg", Leaf(EMPTY_LEAF))

    #: A :py:class:`~abaqus.DisplayGroup.DisplayGroupInstanceRepository.DisplayGroupInstanceRepository` object.
    displayGroupInstances: DisplayGroupInstanceRepository = (
        DisplayGroupInstanceRepository()
    )

    #: A :py:class:`~abaqus.PlotOptions.BasicOptions.BasicOptions` object.
    basicOptions: BasicOptions = BasicOptions()

    #: An :py:class:`~abaqus.OdbDisplay.OrientationOptions.OrientationOptions` object.
    materialOrientationOptions: OrientationOptions = OrientationOptions()

    #: A tuple of Strings specifying the step label and the frame label when the current step
    #: is user defined. Alternatively, **fieldFrame** maybe specified as a pair of Ints with the
    #: step index and the frame index, when the current step is defined in the analysis.
    fieldFrame: Tuple[str, ...] = ()

    #: A tuple specifying variables.
    #: Each item in the sequence consists of a tuple containing the following elements:
    #: 
    #: - Element 0: A String specifying the variable label.
    #: - Element 1: An Int specifying the output position. Possible integer values are:
    #: 
    #:   - 0: UNDEFINED_POSITION
    #:   - 1: NODAL
    #:   - 2: INTEGRATION_POINT
    #:   - 3: ELEMENT_FACE
    #:   - 4: ELEMENT_NODAL
    #:   - 5: WHOLE_ELEMENT
    #:   - 6: ELEMENT_CENTROID
    #:   - 7: WHOLE_REGION
    #:   - 8: WHOLE_PART_INSTANCE
    #:   - 9: WHOLE_MODEL
    #:   - 10: GENERAL_PARTICLE
    #: 
    #: - Element 2: An Int specifying the data type. Possible values are:
    #: 
    #:   - 0: ENUMERATION
    #:   - 1: BOOLEAN
    #:   - 2: INTEGER
    #:   - 3: SCALAR
    #:   - 4: VECTOR
    #:   - 5: QUATERNION_2D
    #:   - 6: QUATERNION_3D
    #:   - 7: TENSOR
    #:   - 8: TENSOR_3D_FULL
    #:   - 9: TENSOR_3D_PLANAR
    #:   - 10: TENSOR_3D_SURFACE
    #:   - 11: TENSOR_2D_PLANAR
    #:   - 12: TENSOR_2D_SURFACE
    #: 
    #: - Element 3: An Int specifying the storage type. Possible values are:
    #: 
    #:   - 0: FLOAT
    #:   - 1: DOUBLE
    #:   - 2: INTEGER
    #:   - 3: BOOLEAN
    #: 
    #: - Element 4: An Int specifying the refinement type. Possible values are:
    #: 
    #:   - 0: NO_REFINEMENT
    #:   - 1: INVARIANT
    #:   - 2: COMPONENT
    #: 
    #: - Element 5: A String specifying the refinement label.
    #: - Element 6: An Int specifying the refinement index.
    #: - Element 7: An Int specifying whether section point information is available. Possible
    #:   values are 1 when section point information is available; 0, when this information is
    #:   unavailable.
    #: - Element 8: A sequence of a String specifying the name of the ply and category
    #:   selection tuples (see below) specifying the section point information.
    #: 
    #:   A category selection tuple consists of the following elements:
    #: 
    #: - Element 0: A String specifying the category label.
    #: - Element 1: An Int specifying whether to use both top and bottom section points to
    #:   obtain results. Possible values are 1 to use both section points and 0 to use only the
    #:   top section point.
    #: - Element 2: An Int specifying the top section point index.
    #: - Element 3: A String specifying the top section label.
    #: - Element 4: An Int specifying the bottom section point index.
    #: - Element 5: A String specifying the bottom section label.
    #: - Element 6: An Int specifying the category id.
    #: - Element 9: An Int specifying whether the data are complex. Possible values are 1 when
    #:   the data are complex; 0, when the data is not complex.
    #: - Element 10: A Float specifying the minimum possible value for the data.
    #: - Element 11: A Float specifying the maximum possible value for the data.
    #: - Element 12: An Int specifying whether the data is derived. Possible values are 1 when
    #:   the data is derived; 0, when the data is not derived.
    primaryVariable: tuple = ()

    #: A tuple specifying variables.For information on the sequence, see the member
    #: **primaryVariable**.
    deformedVariable: tuple = ()

    #: A tuple of SymbolicConstants specifying variables.For information on the sequence, see
    #: the member **primaryVariable**.
    statusVariable: Optional[SymbolicConstant] = None

    #: A tuple of SymbolicConstants specifying variables.For information on the sequence, see
    #: the member **primaryVariable**.
    symbolVariable: Optional[SymbolicConstant] = None

    #: A tuple of SymbolicConstants specifying a Boolean to specify if elements are to be
    #: removed in undeformed states based on an active status variable
    applyStatusToUndeformed: Optional[SymbolicConstant] = None

    #: A tuple of SymbolicConstants specifying a Boolean to specify if the status range should
    #: be inside a specified minimum and maximum. The range will be outside when false.
    statusInsideRange: Optional[SymbolicConstant] = None

    #: A tuple of Floats specifying a Float value for the minimum status range value.
    statusMinimum: Optional[float] = None

    #: A tuple of Floats specifying a Float value for the maximum status range value.
    statusMaximum: Optional[float] = None

    #: A tuple of SymbolicConstants specifying a Boolean to specify if elements are to be
    #: removed based on the status variable
    useStatus: Optional[SymbolicConstant] = None

    #: A pair of Ints specifying the step index and the frame index of the first available
    #: frame. This sequence is read-only.
    firstFrame: str = ""

    #: A pair of Ints specifying the step index and the frame index of the frame previous to
    #: the current frame. This sequence is read-only.
    prevFrame: str = ""

    #: A pair of Ints specifying the step index and the frame index of the frame following the
    #: current frame. This sequence is read-only.
    nextFrame: str = ""

    #: A pair of Ints specifying the step index and the frame index of the last available
    #: frame. This sequence is read-only.
    lastFrame: str = ""

    @abaqus_method_doc
    def moveCameraToCsys(self):
        """This method specifies a new position for the camera. It is available only when
        **movieMode** = ON (in the View object). The new camera position is the origin of the
        coordinate system specified by the **cameraCsysName** member of the BasicOptions object.
        """
        ...

    @abaqus_method_doc
    def setDeformedVariable(self, variableLabel: str, field: str):
        """This method specifies the field output variable or FieldOutput object to be used when
        displaying the deformed shape of the model.

        Parameters
        ----------
        variableLabel
            A String specifying the field output variable.
        field
            A String specifying the FieldOutput object.

        Raises
        ------
        Exception
            If the viewport is not associated with any Odb object. The current viewport 
            is not associated with an ODB file. Requested operation cancelled.
        """
        ...

    @overload
    @abaqus_method_doc
    def setFrame(self, step: int, frame: int):
        """This method specifies the step and frame for the OdbDisplay object.

        Parameters
        ----------
        step
            An Int specifying the step index. Possible values are 0 ≤ **step** ≤ (*numSteps* − 1).
        frame
            An Int specifying the frame in the specified step. Valid values are 0 ≤ **frame** ≤
            (*numFramesInStep* − 1). If **frame** ≥ (*numFramesInStep* − 1) the last frame will be
            displayed.

        Raises
        ------
        - If the viewport is not associated with any Odb object:
          The current viewport is not associated with an ODB file. Requested operation
          cancelled.
        - If the Odb object does not contain valid step data:
          There are no valid step data on the odb. Requested operation cancelled.
        - If an invalid step index is passed in as argument:
          Invalid step index:step. Available step indices: 0 - n.
        """
        ...

    @overload
    @abaqus_method_doc
    def setFrame(self, frame: OdbFrame):
        """This method specifies the frame for the OdbDisplay object.

        Parameters
        ----------
        frame
            An :py:class:`~abaqus.Odb.OdbFrame.OdbFrame` object.
        """
        ...

    @abaqus_method_doc
    def setFrame(self, *args, **kwargs):
        ...

    def setPrimaryVariable(
        self,
        variableLabel: str,
        field: str,
        outputPosition: SymbolicConstant,
        refinement: Optional[SymbolicConstant] = None,
        sectionPoint: Optional[dict] = None,
    ):
        """This method specifies the field output variable for which to obtain results.

        Parameters
        ----------
        variableLabel
            A String specifying the field output variable. The **variableLabel** and **field** arguments
            are mutually exclusive.
        field
            A String specifying the FieldOutput object. The **variableLabel** and **field** arguments
            are mutually exclusive.
        outputPosition
            A SymbolicConstant specifying the position from which to obtain data. Possible values
            are NODAL, INTEGRATION_POINT, ELEMENT_FACE, ELEMENT_NODAL, ELEMENT_CENTROID,
            WHOLE_ELEMENT, WHOLE_REGION, WHOLE_PART_INSTANCE, WHOLE_MODEL, and GENERAL_PARTICLE.
            Data can be obtained only from the position at which they were written to the output
            database during the analysis.
        refinement
            A sequence of a SymbolicConstant and a String. Possible values for the SymbolicConstant
            are INVARIANT and COMPONENT. The String specifies an available component or invariant
            for the specified **variableLabel**. This argument is required only if a refinement is
            available for the specified **variableLabel**.
        sectionPoint
            A Dictionary with String keys and String values. Each key specifies a region in the
            model; the corresponding value specifies a section point within that region. For
            example::
            
                sectionPoint={
                    'shell < MAT > < 7 section points >': 'SPOS, (fraction = 1.0)',
                    'shell < MAT > < 5 section points >': 'SPOS, (fraction = 1.0)', 
                }

        Raises
        ------
        If the viewport is not associated with any Odb object
            The current viewport is not associated with an ODB file. Requested operation
            cancelled.
        """
        ...

    @abaqus_method_doc
    def setPrimarySectionPoint(self, sectionPoint: dict, activePly: str):
        """This method specifies the section point for the current primary, symbol and status
        variables.

        Parameters
        ----------
        sectionPoint
            A Dictionary with String keys and String values. Each key specifies a region in the
            model; the corresponding value specifies a section point within that region. For
            example:`sectionPoint={'shell < MAT > < 7 section points >':'SPOS,    (fraction = 1.0)',
            'shell < MAT > < 5 section points >':    'SPOS, (fraction = 1.0)', }`
        activePly
            A String specifying the active ply name.

        Raises
        ------
        - If the viewport is not associated with any Odb object:
          The current viewport is not associated with an ODB file. Requested operation
          cancelled.
        """
        ...

    @abaqus_method_doc
    def setStatusVariable(
        self,
        variableLabel: str,
        field: str,
        outputPosition: SymbolicConstant,
        refinement: Optional[SymbolicConstant] = None,
        sectionPoint: Optional[dict] = None,
        statusMinimum: Optional[float] = None,
        statusMaximum: Optional[float] = None,
        statusInsideRange: Boolean = OFF,
        useStatus: Boolean = OFF,
        applyStatusToUndeformed: Boolean = False,
    ):
        """This method specifies the field output variable for filtering element display based on a
        status criteria.

        Parameters
        ----------
        variableLabel
            A String specifying the field output variable. The **variableLabel** and **field** arguments
            are mutually exclusive.
        field
            A String specifying the FieldOutput object. The **variableLabel** and **field** arguments
            are mutually exclusive.
        outputPosition
            A SymbolicConstant specifying the position from which to obtain data. Possible values
            are NODAL, INTEGRATION_POINT, ELEMENT_FACE, ELEMENT_NODAL, ELEMENT_CENTROID,
            WHOLE_ELEMENT, WHOLE_REGION, WHOLE_PART_INSTANCE, WHOLE_MODEL, and GENERAL_PARTICLE.
            Data can be obtained only from the position at which they were written to the output
            database during the analysis.
        refinement
            A sequence of a SymbolicConstant and a String. Possible values for the SymbolicConstant
            are INVARIANT and COMPONENT. The String specifies an available component or invariant
            for the specified **variableLabel**. This argument is required only if a refinement is
            available for the specified **variableLabel**.
        sectionPoint
            A Dictionary with String keys and String values. Each key specifies a region in the
            model; the corresponding value specifies a section point within that region. For
            example:`sectionPoint={'shell < MAT > < 7 section points >':'SPOS,    (fraction = 1.0)',
            'shell < MAT > < 5 section points >':    'SPOS, (fraction = 1.0)', }`
        statusMinimum
            A Float specifying the minimum result value to be considered for element removal.
        statusMaximum
            A Float specifying the maximum result value to be considered for element removal.
        statusInsideRange
            A Boolean utilized when both **statusMinimum** and **statusMaximum** are given. Elements
            will be removed when they contain values between the minimum and maximum, inclusive,
            when true. Elements will be removed when they contain values outside of the minimum and
            maximum, exclusive, when false.
        useStatus
            A Boolean to specify if the status variable is to be active.
        applyStatusToUndeformed
            A Boolean to specify if the active status variable is to remove elements from undeformed
            plots. The default value is False.

        Raises
        ------
        - If the viewport is not associated with any Odb object:
          The current viewport is not associated with an ODB file. Requested operation
          cancelled.
        """
        ...

    @abaqus_method_doc
    def setSymbolVariable(
        self,
        variableLabel: str,
        field: str,
        outputPosition: SymbolicConstant,
        refinement: Optional[SymbolicConstant] = None,
        sectionPoint: Optional[dict] = None,
        tensorQuantity: Optional[SymbolicConstant] = None,
        vectorQuantity: Optional[SymbolicConstant] = None,
    ):
        """This method specifies the field output variable for which to obtain results used for
        symbol plots. This variable must be in the form of vector or tensor data. The output
        quantity can also be specified with this command to control the display of resultants,
        or components.

        Parameters
        ----------
        variableLabel
            A String specifying the field output variable. The **variableLabel** and **field** arguments
            are mutually exclusive.
        field
            A String specifying the FieldOutput object. The **variableLabel** and **field** arguments
            are mutually exclusive.
        outputPosition
            A SymbolicConstant specifying the position from which to obtain data. Possible values
            are NODAL, INTEGRATION_POINT, ELEMENT_FACE, ELEMENT_NODAL, ELEMENT_CENTROID,
            WHOLE_ELEMENT, WHOLE_REGION, WHOLE_PART_INSTANCE, WHOLE_MODEL, and GENERAL_PARTICLE.
            Data can be obtained only from the position at which they were written to the output
            database during the analysis.
        refinement
            A sequence of a SymbolicConstant and a String. Possible values for the SymbolicConstant
            are INVARIANT and COMPONENT. The String specifies an available component or invariant
            for the specified **variableLabel**. This argument is required only if a refinement is
            available for the specified **variableLabel**.
        sectionPoint
            A Dictionary with String keys and String values. Each key specifies a region in the
            model; the corresponding value specifies a section point within that region. For
            example:`sectionPoint={'shell < MAT > < 7 section points >':'SPOS,    (fraction = 1.0)',
            'shell < MAT > < 5 section points >':    'SPOS, (fraction = 1.0)', }`
        tensorQuantity
            A SymbolicConstant specifying the tensor quantity to be displayed with the symbol. This
            value is set in the SymbolOptions object.
        vectorQuantity
            A SymbolicConstant specifying the vector quantity to be displayed with the symbol. This
            value is set in the SymbolOptions object.

        Raises
        ------
        - If the viewport is not associated with any Odb object:
          The current viewport is not associated with an ODB file. Requested operation
          cancelled.
        """
        ...

    @abaqus_method_doc
    def setStreamVariable(self, variableLabel: str):
        """This method specifies the field output variable for which to obtain results used for
        stream plots. This variable must be in the form of nodal vector data.

        Parameters
        ----------
        variableLabel
            A String specifying the field output variable.

        Raises
        ------
        - If the viewport is not associated with any Odb object:
          The current viewport is not associated with an ODB file. Requested operation
          cancelled.
        """
        ...

    @abaqus_method_doc
    def setValues(
        self,
        visibleDisplayGroups: str = "",
        viewCut: Boolean = OFF,
        viewCutNames: str = "",
    ):
        """This method specifies member values for the OdbDisplay object.

        Parameters
        ----------
        visibleDisplayGroups
            A List of DisplayGroup objects.
        viewCut
            A Boolean specifying whether to display the cut. The default value is OFF.
        viewCutNames
            A List of ViewCut objects.
        """
        ...

    @abaqus_method_doc
    def ViewCut(
        self,
        name: str,
        shape: SymbolicConstant,
        origin: tuple,
        normal: Union[SymbolicConstant, float],
        axis2: Union[SymbolicConstant, float],
        csysName: str,
        cylinderAxis: Union[SymbolicConstant, float],
        followDeformation: Boolean = OFF,
        overrideAveraging: Boolean = ON,
        referenceFrame: SymbolicConstant = FIRST_FRAME,
    ) -> ViewCut:
        """This method creates a ViewCut object.

        .. note:: 
            This function can be accessed by::

                session.viewports[name].layers[name].odbDisplay.ViewCut
                session.viewports[name].odbDisplay.ViewCut

        Parameters
        ----------
        name
            A String specifying the repository key.
        shape
            A SymbolicConstant specifying the shape of the ViewCut object. Possible values are
            PLANE, CYLINDER, SPHERE, and ISOSURFACE.
        origin
            A sequence of three Floats specifying the X-, Y-, and Z-coordinates of the origin of the
            plane, cylinder or sphere cut. This origin is not required if the cut shape is
            ISOSURFACE or if the cut is defined by the **csysName** argument.
        normal
            A sequence of Floats specifying the X-, Y-, and Z-coordinates of the normal axis to the
            plane defining the cut, when the plane is defined using the **origin** argument or a
            SymbolicConstant defining this normal axis, when the cut is defined by the **csysName**
            argument. Possible values are AXIS_1, AXIS_2, AXIS_3. This axis is not required if the
            cut **shape** is CYLINDER, SPHERE or ISOSURFACE.
        axis2
            A sequence of three Floats specifying the X-, Y-, and Z-coordinates of the second axis
            of the plane defining the cut, when the plane is defined using the **origin** argument or
            a SymbolicConstant defining this second axis, when the cut is defined by the **csysName**
            argument. Possible values are AXIS_1, AXIS_2, AXIS_3. This axis is used to rotate the
            plane cut. It is not required if the cut **shape** is CYLINDER, SPHERE or ISOSURFACE.
        csysName
            A String specifying the name of the DatumCsys object to be used to define the cut. This
            name is not required if the cut **shape** is ISOSURFACE or if the cut is defined by the
            **origin** argument.
        cylinderAxis
            A sequence of Floats specifying the X-, Y-, and Z-coordinates of the cylinder axis
            defining the cut, when the cut is defined using the **origin** argument or a
            SymbolicConstant defining this cylinder axis, when the cut is defined by the **csysName**
            argument. Possible values are AXIS_1, AXIS_2, AXIS_3. This axis is not required if the
            cut **shape** is PLANE, SPHERE, or ISOSURFACE.
        followDeformation
            A Boolean specifying whether the cut will follow the deformation or be static. The
            default value is OFF.
        overrideAveraging
            A Boolean specifying averaging for element based fields associated with isosurface cuts
            will be set to compute-average with a threshold of 100% when true. The current field
            options will be used when false. The default value is ON.
        referenceFrame
            A SymbolicConstant specifying which reference frame will be used when the cut follows
            the deformation. Possible values are FIRST_FRAME, LAST_FRAME, and CURRENT_FRAME. The
            default value is FIRST_FRAME.

        Returns
        -------
        ViewCut
            A :py:class:`~abaqus.OdbDisplay.ViewCut.ViewCut` object.
        """
        self.viewCuts[name] = viewCut = ViewCut(
            name,
            shape,
            origin,
            normal,
            axis2,
            csysName,
            cylinderAxis,
            followDeformation,
            overrideAveraging,
            referenceFrame,
        )
        return viewCut
