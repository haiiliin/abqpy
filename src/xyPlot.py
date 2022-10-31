from typing import Optional, Tuple, Sequence, Union, List, Dict

from typing_extensions import Literal

from abaqus.Odb.Odb import Odb
from abaqus.PathAndProbe.Path import Path
from abaqus.UtilityAndView.SymbolicConstant import SymbolicConstant
from abaqus.UtilityAndView.SymbolicConstant import abaqusConstants as C
from abaqus.UtilityAndView.abaqusConstants import (
    Boolean,
    OFF,
    ON,
    REAL,
)
from abaqus.XY.AreaStyle import AreaStyle  # noqa # pylint: disable=unused-import
from abaqus.XY.LineStyle import LineStyle  # noqa # pylint: disable=unused-import
from abaqus.XY.QuantityType import QuantityType  # noqa # pylint: disable=unused-import
from abaqus.XY.SymbolStyle import SymbolStyle  # noqa # pylint: disable=unused-import
from abaqus.XY.TextStyle import TextStyle  # noqa # pylint: disable=unused-import
from abaqus.XY.XYData import XYData  # noqa # pylint: disable=unused-import
from abaqus.XY.XYSession import XYSession  # noqa # pylint: disable=unused-import


def XYDataFromFile(
    fileName: str,
    name: str = "",
    sourceDescription: str = "",
    contentDescription: str = "",
    positionDescription: str = "",
    legendLabel: str = "",
    xValuesLabel: str = "",
    yValuesLabel: str = "",
    axis1QuantityType: Optional[QuantityType] = None,
    axis2QuantityType: Optional[QuantityType] = None,
    xField: int = 1,
    yField: int = 2,
    skipFrequency: Optional[int] = None,
) -> XYData:
    """This method creates an XYData object from data in an ASCII file.

    .. note:: 
        This function can be accessed by::

            session.XYDataFromFile
            xyPlot.XYDataFromFile

    Parameters
    ----------
    fileName
        A String specifying the name of the file from which the **X - Y** data will be read.
    name
        The repository key. If the name is not supplied, a default name in the form _temp#_ is
        generated and the XYData object is temporary.
    sourceDescription
        A String specifying the source of the **X - Y** data (e.g., “Entered from keyboard”, “Taken
        from ASCII file”, “Read from an ODB”, etc.). The default value is an empty string.
    contentDescription
        A String specifying the content of the **X - Y** data (e.g., “field 1 vs. field 2”). The
        default value is an empty string.
    positionDescription
        A String specifying additional information about the **X - Y** data (e.g., “for whole
        model”). The default value is an empty string.
    legendLabel
        A String specifying the label to be used in the legend. The default value is the name of
        the XYData object.
    xValuesLabel
        A String specifying the label for the X-values. This value may be overridden if the
        **X - Y** data are combined with other **X - Y** data. The default value is an empty string.
    yValuesLabel
        A String specifying the label for the Y-values. This value may be overridden if the
        **X - Y** data are combined with other **X - Y** data. The default value is an empty string.
    axis1QuantityType
        A QuantityType object specifying the QuantityType object associated to
        the X -axis1- values.
    axis2QuantityType
        A QuantityType object specifying the QuantityType object associated to
        the Y -axis2- values.
    xField
        An Int specifying the field from which the **X**-data will be read. Fields are delimited
        by spaces, tabs, or commas. The default value is 1.
    yField
        An Int specifying the field from which the **Y**-data will be read. Fields are delimited
        by spaces, tabs, or commas. The default value is 2.
    skipFrequency
        An Int specifying how often data rows will be skipped. A **skipFrequency** of 1 means skip
        every other row. The first row is always read. Possible values are **skipFrequency** ≥≥ 0.
        The default value is 0 (data are read from every row).

    Returns
    -------
    XYData
        An XYData object.

    Raises
    ------
    InvalidNameError
    RangeError
    """
    return XYData(())


def XYDataFromFreeBody(
    odb: Odb,
    force: Boolean = ON,
    moment: Boolean = OFF,
    heatFlowRate: Boolean = OFF,
    resultant: Boolean = ON,
    comp1: Boolean = OFF,
    comp2: Boolean = OFF,
    comp3: Boolean = OFF,
) -> List[XYData]:
    """This method creates a list of XYData objects by computing free body data from an Odb
    object.

    .. note:: 
        This function can be accessed by::

            session.XYDataFromFreeBody
            xyPlot.XYDataFromFreeBody

    Parameters
    ----------
    odb
        An Odb object specifying the output database from which data will be read.
    force
        A boolean indicating whether to compute the force. The default is ON.
    moment
        A boolean indicating whether to compute the moment. The default is OFF.
    heatFlowRate
        A boolean indicating whether to compute the heat flow rate resultant magnitude. It is
        extracted only for viewcut based freebodies. The default is OFF.
    resultant
        A boolean indicating whether to compute the resultant. It applies only to **force** and
        **moment**. The default is ON.
    comp1
        A boolean indicating whether to compute the first component. It applies only to **force**
        and **moment**. The default is OFF.
    comp2
        A boolean indicating whether to compute the second component. It applies only to **force**
        and **moment**. The default is OFF.
    comp3
        A boolean indicating whether to compute the third component. It applies only to **force**
        and **moment**. The default is OFF.

    Returns
    -------
    List[XYData]
        A list of XYData objects.

    Raises
    ------
    InvalidNameError
    RangeError
    """
    return [XYData(())]


def XYDataFromHistory(
    odb: Odb,
    outputVariableName: str,
    steps: tuple,
    name: str = "",
    sourceDescription: str = "",
    contentDescription: str = "",
    positionDescription: str = "",
    legendLabel: str = "",
    skipFrequency: Optional[int] = None,
    numericForm: Literal[
        C.COMPLEX_MAGNITUDE, C.COMPLEX_PHASE, C.REAL, C.IMAGINARY, C.COMPLEX_VAL_AT_ANGLE
    ] = REAL,
    complexAngle: float = 0,
    stepTuple: Optional[int] = None,
) -> XYData:
    """This method creates an XYData object by reading history data from an Odb object.

    .. note:: 
        This function can be accessed by::

            session.XYDataFromHistory
            xyPlot.XYDataFromHistory

    Parameters
    ----------
    odb
        An Odb object specifying the output database from which data will be read.
    outputVariableName
        A String specifying the output variable from which the **X - Y** data will be read.
    steps
        A sequence of Strings specifying the names of the steps from which data will be
        extracted.
    name
        The repository key. If the name is not supplied, a default name in the form _temp#_ is
        generated and the XYData object is temporary (this argument is required if the method is
        accessed from the session object).
    sourceDescription
        A String specifying the source of the **X - Y** data (for example, “Entered from keyboard”,
        “Taken from ASCII file”, “Read from an ODB”, etc.). The default value is an empty
        string.
    contentDescription
        A String specifying the content of the **X - Y** data (for example, “field 1 vs. field 2”).
        The default value is an empty string.
    positionDescription
        A String specifying additional information about the **X - Y** data (for example, “for whole
        model”). The default value is an empty string.
    legendLabel
        A String specifying the label to be used in the legend. The default value is the name of
        the XYData object.
    skipFrequency
        An Int specifying how often data frames will be skipped. If **skipFrequency** = 1, Abaqus
        will skip every other frame. The first frame is always read. Possible values are
        **skipFrequency** ≥≥ 0. The default value is 0 (data are read from every frame).
    numericForm
        A SymbolicConstant specifying the numeric form in which to display results that contain
        complex numbers. Possible values are COMPLEX_MAGNITUDE, COMPLEX_PHASE, REAL, IMAGINARY,
        and COMPLEX_VAL_AT_ANGLE. The default value is REAL.
    complexAngle
        A Float specifying the angle (in degrees) at which to display results that contain
        complex numbers when **numericForm** = COMPLEX_VAL_AT_ANGLE. The default value is 0.
    stepTuple
        A tuple of Integers specifying the steps to include when extracting data.

    Returns
    -------
    XYData
        An XYData object.

    Raises
    ------
    InvalidNameError
    RangeError
    """
    return XYData(())


def XYDataFromPath(
    path: Path,
    name: str,
    includeIntersections: Boolean,
    shape: Literal[C.UNDEFORMED, C.DEFORMED],
    pathStyle: Literal[C.PATH_POINTS, C.UNIFORM_SPACING],
    numIntervals: int,
    labelType: Literal[
        C.NORM_DISTANCE,
        C.SEQ_ID,
        C.TRUE_DISTANCE,
        C.TRUE_DISTANCE_X,
        C.TRUE_DISTANCE_Y,
        C.TRUE_DISTANCE_Z,
        C.X_COORDINATE,
        C.Y_COORDINATE,
        C.Z_COORDINATE,
    ],
    viewport: str = "",
    removeDuplicateXYPairs: Boolean = True,
    includeAllElements: Boolean = False,
    step: Optional[int] = None,
    frame: Optional[int] = None,
    variable: Optional[SymbolicConstant] = None,
    deformedMag: Optional[float] = None,
    numericForm: Literal[
        C.COMPLEX_MAGNITUDE, C.COMPLEX_PHASE, C.REAL, C.IMAGINARY, C.COMPLEX_VAL_AT_ANGLE
    ] = REAL,
    complexAngle: float = 0,
    projectOntoMesh: Boolean = False,
    projectionTolerance: float = 0,
) -> XYData:
    """This method creates an XYData object from path information.

    .. note:: 
        This function can be accessed by::

            session.XYDataFromPath
            xyPlot.XYDataFromPath

    Parameters
    ----------
    path
        A Path object to use in **X - Y** data generation.
    name
        A String specifying the repository key:for **session** 'name' is required argument and for
        **xyPlot** 'name' is optional argument.
    includeIntersections
        A Boolean specifying whether to include **X - Y** data for the intersections between the
        path and element faces or edges. The default value is False.
    shape
        A SymbolicConstant specifying the model shape to use. Possible values are UNDEFORMED and
        DEFORMED.
    pathStyle
        A SymbolicConstant specifying the path style. Possible values are PATH_POINTS and
        UNIFORM_SPACING.
    numIntervals
        An Int specifying the number of uniform-spacing intervals. The default value is 10.
    labelType
        A SymbolicConstant specifying the **X** label type to use. Possible values are
        NORM_DISTANCE, SEQ_ID, TRUE_DISTANCE, TRUE_DISTANCE_X, TRUE_DISTANCE_Y, TRUE_DISTANCE_Z,
        X_COORDINATE, Y_COORDINATE and Z_COORDINATE.
    viewport
        A String specifying the viewport name or an Int specifying the viewport id from which to
        obtain values. The default is the current viewport.
    removeDuplicateXYPairs
        A Boolean specifying whether to remove duplicate XY values from the final result. The
        default value is True.

        .. versionadded:: 2018
            The `removeDuplicateXYPairs` argument was added.
    includeAllElements
        A Boolean specifying whether to include elements which do not lie in the direction of
        the path. The default value is False.
        
        .. versionadded:: 2018
            The `includeAllElements` argument was added.
    step
        An Int identifying the step from which to obtain values. The default value is the
        current step.
    frame
        An Int identifying the frame from which to obtain values. The default value is the
        current frame.
    variable
        A tuple of tuples containing the descriptions of variables for which to extract data
        along the path. The default value is the current variable. Each tuple specifies the
        following:Variable label: A String specifying the variable; for example, 'U'.Variable
        output position: A SymbolicConstant specifying the output position. Possible values are
        ELEMENT_CENTROID, ELEMENT_FACE, ELEMENT_NODAL, GENERAL_PARTICLE, INTEGRATION_POINT,
        NODAL, WHOLE_ELEMENT, WHOLE_MODEL, WHOLE_PART_INSTANCE, and WHOLE_REGION.Refinement: A
        tuple specifying the refinement. If the refinement tuple is omitted, data are written
        for all components and invariants (if applicable). This element is required if the
        location dictionary (the following element in the tuple) is included. The refinement
        tuple contains the following:Type: A SymbolicConstant specifying the type of refinement.
        Possible values are INVARIANT and COMPONENT.Label: A String specifying the invariant or
        the component; for example, 'Mises' or 'S22'.Location: An optional Dictionary specifying
        the location. The dictionary contains pairs of the following:A String specifying the
        category selection label.A String specifying the section point label. For
        example::
        
            variable = ('S',INTEGRATION_POINT, ((COMPONENT, 'S22' ), ), ) 
            variable = (('S',INTEGRATION_POINT, ((COMPONENT, 'S11' ), ), ),
                        ('U',NODAL,((COMPONENT, 'U1'),)),) 
            variable = (('S', INTEGRATION_POINT, ((INVARIANT, 'Mises' ), ),
                        {'shell < STEEL > < 3 section points >':'SNEG,
                        (fraction = -1.0)', }), )
    deformedMag
        A tuple of three Floats specifying the deformation magnitude in the *X-*, *Y-*, and
        *Z-* planes. The default value is (1, 1, 1).
    numericForm
        A SymbolicConstant specifying the numeric form in which to display results that contain
        complex numbers. Possible values are COMPLEX_MAGNITUDE, COMPLEX_PHASE, REAL, IMAGINARY,
        and COMPLEX_VAL_AT_ANGLE. The default value is REAL.
    complexAngle
        A Float specifying the angle (in degrees) at which to display results that contain
        complex numbers when **numericForm** = COMPLEX_VAL_AT_ANGLE. The default value is 0.
    projectOntoMesh
        A Boolean to specify whether to consider the data points that do not lie on or inside
        the mesh. The default value is False.
    projectionTolerance
        A Float specifying the tolerance value for the projected distance considered for the
        data extraction when **projectOntoMesh** =  True. The default value is 0.

    Returns
    -------
    If **variable** specified has one fieldoutput: Returns an XYData object.
    If **variable** specified has more than one fieldoutputs: Returns list of XYData objects.

    Raises
    ------
    ErrorPathNotFound: Path not found
        If **path** is invalid.
    ErrorCurrentVPNotFound: Current viewport not found
        If **viewport** is invalid.
    ErrorInvalidUserStepAndFrame: The user step and frame specified have not been defined
        If **step** and/or **frame** are invalid.
    ErrorNoVarInPathExtract: No variable selection for XY data extraction from path
        If the **variable** argument is empty.
    ErrorUnavailableSelectedVariable: The selected variable is not available for the current frame
        If the specified output variable is not available in the output database.
    ErrorUnusableVarInPathExtract: Specified variable cannot be used in XY data extraction
        If the specified output variable cannot be used to obtain **X - Y** data from path.
    ErrorUnsupportedRefinementType: Unsupported refinement type
        If the SymbolicConstant specifying the refinement type is invalid.
    ErrorInvalidRefinementSpecification: Invalid refinement specification
        If the label specifying the refinement invariant or component is invalid.
    ErrorDeformedMagTupleInPathExtract: Deformed magnification tuple must contain X, Y and Z values
        If **deformedMag** does not contain three Floats.
    """
    return XYData(())


def XYDataFromShellThickness(
    odb: Odb,
    outputPosition: Literal[C.ELEMENT_CENTROID, C.ELEMENT_NODAL, C.INTEGRATION_POINT, C.NODAL],
    variable: Tuple[
        Tuple[
            str,
            Literal[
                C.ELEMENT_CENTROID,
                C.ELEMENT_FACE,
                C.ELEMENT_NODAL,
                C.GENERAL_PARTICLE,
                C.INTEGRATION_POINT,
                C.NODAL,
                C.WHOLE_ELEMENT,
                C.WHOLE_MODEL,
                C.WHOLE_PART_INSTANCE,
                C.WHOLE_REGION,
            ],
            Tuple[Literal[C.INVARIANT, C.COMPONENT], str],
            Dict[str, str],
        ],
        ...,
    ],
    elementSets: Union[str, Sequence[str]] = ...,
    elementLabels: Sequence[Tuple[str, Union[int, str]]] = ...,
    nodeSets: Union[str, Sequence[str]] = ...,
    nodeLabels: Sequence[Tuple[str, Union[int, str]]] = ...,
    numericForm: Literal[
        C.COMPLEX_MAGNITUDE, C.COMPLEX_PHASE, C.REAL, C.IMAGINARY, C.COMPLEX_VAL_AT_ANGLE
    ] = REAL,
    complexAngle: float = 0,
) -> List[XYData]:
    """This method creates a list of XYData objects by reading through the thickness field data
    from an Odb object.

    .. note:: 
        This function can be accessed by::

            session.XYDataFromShellThickness
            xyPlot.XYDataFromShellThickness

    Parameters
    ----------
    odb
        An Odb object specifying the output database from which data will be read.
    outputPosition
        A SymbolicConstant specifying the position from which output will be read. Possible
        values are ELEMENT_CENTROID, ELEMENT_NODAL, INTEGRATION_POINT, and NODAL.
    variable
        A tuple of tuples containing the descriptions of variables for which to extract data from the
        field. Each tuple specifies the following:

        * Variable label: A String specifying the variable; for example, 'U'.
        * Variable output position: A SymbolicConstant specifying
            the output position. Possible values are ELEMENT_CENTROID, ELEMENT_FACE, ELEMENT_NODAL,
            GENERAL_PARTICLE, INTEGRATION_POINT, NODAL, WHOLE_ELEMENT, WHOLE_MODEL, WHOLE_PART_INSTANCE, and
            WHOLE_REGION.
        * Refinement: A tuple specifying the refinement. If
            the refinement tuple is omitted, data are written for all components and invariants (if
            applicable). This element is required if the location dictionary (the following element in the
            tuple) is included. The refinement tuple contains the following:

            * Type: A SymbolicConstant specifying the type of refinement. Possible values are INVARIANT and COMPONENT.
            * Label: A String specifying the invariant or the component; for example, 'Mises' or 'S22'.

        * Location: An optional Dictionary specifying the location. The
            dictionary contains pairs of the following:
            
            * A String specifying the category selection label.
            * A String specifying the section point label.

        For example::

            variable = ('S', INTEGRATION_POINT, ((COMPONENT, 'S22'), ), )
            variable = (('S', INTEGRATION_POINT, ((COMPONENT, 'S11'), ), ),
                        ('U', NODAL,((COMPONENT, 'U1'), )), )
            variable = (('S', INTEGRATION_POINT, ((INVARIANT, 'Mises'), ),
                            {'shell < STEEL > < 3 section points >': 'SNEG, (fraction = -1.0)', }), )
    elementSets
        A sequence of Strings specifying element sets or a String specifying a single element
        set.
    elementLabels
        A sequence of expressions specifying element labels per part instance in the model. Each
        part instance element expression is a sequence of a String specifying the part instance
        name and a sequence of element expressions; for example, 
        `(('partInstance1',(1,'7','3:15;3'),), ('partInstance2','8'),))`. The element
        expressions can be any of the following:An Int specifying a single element label; for
        example, `1`.A String specifying a single element label; for example, `'7'`.A String
        specifying a sequence of element labels; for example, `'3:5'` and `'3:15:3'`.
    nodeSets
        A sequence of Strings specifying node sets or a String specifying a single node set.
    nodeLabels
        A sequence of expressions specifying node labels per part instance in the model. Each
        part instance node expression is a sequence of a String specifying the part instance
        name and a sequence of node expressions; for example,
        `(('partInstance1',(1,'7','3:15;3'),), ('partInstance2','8'),))`. The node expressions
        can be any of the following:An Int specifying a single node label; for example, `1`.A
        String specifying a single node label; for example, `'7'`.A String specifying a sequence
        of node labels; for example, `'3:5'` and `'3:15:3'`.
    numericForm
        A SymbolicConstant specifying the numeric form in which to display results that contain
        complex numbers. Possible values are COMPLEX_MAGNITUDE, COMPLEX_PHASE, REAL, IMAGINARY,
        and COMPLEX_VAL_AT_ANGLE. The default value is REAL.
    complexAngle
        A Float specifying the angle (in degrees) at which to display results that contain
        complex numbers when **numericForm** = COMPLEX_VAL_AT_ANGLE. The default value is 0.

    Returns
    -------
    List[XYData]
        A list of XYData objects.

    Raises
    ------
    InvalidNameError
    RangeError
    """
    return [XYData(())]


def xyDataListFromField(
    odb: Odb,
    outputPosition: Literal[C.ELEMENT_CENTROID, C.ELEMENT_NODAL, C.INTEGRATION_POINT, C.NODAL],
    variable: Tuple[
        Tuple[
            str,
            Literal[
                C.ELEMENT_CENTROID,
                C.ELEMENT_FACE,
                C.ELEMENT_NODAL,
                C.GENERAL_PARTICLE,
                C.INTEGRATION_POINT,
                C.NODAL,
                C.WHOLE_ELEMENT,
                C.WHOLE_MODEL,
                C.WHOLE_PART_INSTANCE,
                C.WHOLE_REGION,
            ],
            Tuple[Literal[C.INVARIANT, C.COMPONENT], str],
            Dict[str, str],
        ],
        ...,
    ],
    elementSets: Union[Sequence[str], str] = ...,
    elementLabels: Sequence[Tuple[str, Union[int, str]]] = ...,
    nodeSets: Union[str, Sequence[str]] = ...,
    nodeLabels: Sequence[Tuple[str, Union[int, str]]] = ...,
    numericForm: Literal[
        C.COMPLEX_MAGNITUDE, C.COMPLEX_PHASE, C.REAL, C.IMAGINARY, C.COMPLEX_VAL_AT_ANGLE
    ] = REAL,
    complexAngle: float = 0,
    operator: Literal[
        C.ADD,
        C.SUBTRACT,
        C.MULTIPLY,
        C.DIVIDE,
        C.POWER,
        C.MINIMUM,
        C.MAXIMUM,
        C.AVERAGE,
        C.RANGE,
        C.SRSS,
        C.ABSOLUTE,
        C.UNARY_NEGATIVE,
        C.COSINE,
        C.HYPERBOLIC_COSINE,
        C.INVERSE_COSINE,
        C.SINE,
        C.HYPERBOLIC_SINE,
        C.INVERSE_SINE,
        C.TANGENT,
        C.HYPERBOLIC_TANGENT,
        C.INVERSE_TANGENT,
        C.EXPONENTIAL,
        C.NATURAL_LOG,
        C.LOG,
        C.SQUARE_ROOT,
        C.NORMALIZE,
        C.DEG2RAD,
        C.RAD2DEG,
        C.SMOOTH,
        C.SWAP,
        C.AVERAGE_ALL,
        C.MAXIMUM_ENVELOPE,
        C.MINIMUM_ENVELOPE,
        C.RANGE_ALL,
    ] = ...,
) -> List[XYData]:
    """This method creates a list of XYData objects by reading field data from an Odb object.

    .. note:: 
        This function can be accessed by::

            session.xyDataListFromField
            xyPlot.xyDataListFromField

    Parameters
    ----------
    odb
        An Odb object specifying the output database from which data will be read.
    outputPosition
        A SymbolicConstant specifying the position from which output will be read. Possible
        values are ELEMENT_CENTROID, ELEMENT_NODAL, INTEGRATION_POINT, and NODAL.
    variable
        A tuple of tuples containing the descriptions of variables for which to extract data
        from the field. Each tuple specifies the following: 
        
        * Variable label: A String specifying the variable; for example, 'U'.
        * Variable output position: A SymbolicConstant specifying the output position. Possible values are
            ELEMENT_CENTROID, ELEMENT_FACE, ELEMENT_NODAL, GENERAL_PARTICLE, INTEGRATION_POINT, NODAL,
            WHOLE_ELEMENT,  WHOLE_MODEL, WHOLE_PART_INSTANCE, and WHOLE_REGION.
        * Refinement: A tuple specifying the refinement. If the refinement tuple is omitted, data are
            written  for all components and invariants (if applicable). This element is required if the
            location dictionary (the following element in the tuple) is included. The refinement tuple
            contains the following: 
            
            * Type: A SymbolicConstant specifying the type of refinement. Possible values are INVARIANT and
            COMPONENT.
            * Label: A String specifying the invariant or the component; for example, 'Mises' or 'S22'.
            
        * Location: An optional Dictionary specifying the location. The dictionary contains pairs of the
            following:
            
            * A String specifying the category selection label.
            * A String specifying the section point label.
            
        For example::

            variable = ('S', INTEGRATION_POINT, ((COMPONENT, 'S22'), ), )
            variable = (('S', INTEGRATION_POINT, ((COMPONENT, 'S11'), ), ),
                        ('U', NODAL,((COMPONENT, 'U1'), )), )
            variable = (('S', INTEGRATION_POINT, ((INVARIANT, 'Mises'), ),
                            {'shell < STEEL > < 3 section points >': 'SNEG, (fraction = -1.0)', }), )

    elementSets
        A sequence of Strings specifying element sets or a String specifying a single element
        set.
    elementLabels
        A sequence of expressions specifying element labels per part instance in the model. Each
        part instance element expression is a sequence of a String specifying the part instance
        name and a sequence of element expressions; for example,
        `(('partInstance1',(1,'7','3:15;3'),), ('partInstance2','8'),))`. The element
        expressions can be any of the following:

        * An Int specifying a single element label; for example, `1`.
        * A String specifying a single element label; for example, `'7'`.
        * A String specifying a sequence of element labels; for example, `'3:5'` and `'3:15:3'`.

    nodeSets
        A sequence of Strings specifying node sets or a String specifying a single node set.
    nodeLabels
        A sequence of expressions specifying node labels per part instance in the model. Each
        part instance node expression is a sequence of a String specifying the part instance
        name and a sequence of node expressions; for example,
        `(('partInstance1',(1,'7','3:15;3'),), ('partInstance2','8'),))`. The node expressions
        can be any of the following:

        * An Int specifying a single node label; for example, `1`.A
        * String specifying a single node label; for example, `'7'`.
        * A String specifying a sequence of node labels; for example, `'3:5'` and `'3:15:3'`.

    numericForm
        A SymbolicConstant specifying the numeric form in which to display results that contain
        complex numbers. Possible values are COMPLEX_MAGNITUDE, COMPLEX_PHASE, REAL, IMAGINARY,
        and COMPLEX_VAL_AT_ANGLE. The default value is REAL.
    complexAngle
        A Float specifying the angle (in degrees) at which to display results that contain
        complex numbers when **numericForm** = COMPLEX_VAL_AT_ANGLE. The default value is 0.
    operator
        A SymbolicConstant specifying the mathematical, trigonometric, logarithmic, exponential,
        or other operations. Possible values are ADD, SUBTRACT, MULTIPLY, DIVIDE, POWER,
        MINIMUM, MAXIMUM, AVERAGE, RANGE, SRSS, ABSOLUTE, UNARY_NEGATIVE, COSINE,
        HYPERBOLIC_COSINE, INVERSE_COSINE, SINE, HYPERBOLIC_SINE, INVERSE_SINE, TANGENT,
        HYPERBOLIC_TANGENT, INVERSE_TANGENT, EXPONENTIAL, NATURAL_LOG, LOG, SQUARE_ROOT,
        NORMALIZE, DEG2RAD, RAD2DEG, SMOOTH, SWAP, AVERAGE_ALL, MAXIMUM_ENVELOPE,
        MINIMUM_ENVELOPE, and RANGE_ALL. If no value is defined, no operation will be performed
        on the data, and the data will be saved as is.

    Returns
    -------
    List[XYData]
        A list of XYData objects.

    Raises
    ------
    InvalidNameError
    RangeError
    """
    return [XYData(())]
