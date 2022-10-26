from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ...UtilityAndView.abaqusConstants import Boolean, MINIMUM_MOVE, ON, REGULAR, STANDARD
from ...UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class ConstrainedSketchOptions:
    """The ConstrainedSketchOptions object is used to store values and attributes associated
    with a particular sketch. The ConstrainedSketchOptions object has no constructor.

    .. note::
        This object can be accessed by::

            import sketch
            mdb.models[name].sketches[name].sketchOptions
    """

    @abaqus_method_doc
    def setValues(
        self,
        sheetSize: Optional[float] = None,
        gridSpacing: Optional[float] = None,
        grid: Boolean = ON,
        gridFrequency: int = 1,
        dimensionTextHeight: float = 12,
        decimalPlaces: Optional[int] = None,
        constructionGeometry: Boolean = ON,
        gridSnap: Boolean = ON,
        preselection: Boolean = ON,
        sheetAuto: Boolean = ON,
        gridOrigin: tuple = (),
        gridAngle: float = 0,
        viewStyle: Literal[C.AXISYM, C.REGULAR] = REGULAR,
        addImpliedConstraints: Boolean = ON,
        maxCoplanarEntities: int = 300,
        autoConstrainAngularTolerance: float = 0,
        autoConstrainLinearTolerance: Optional[float] = None,
        autoConstrainOptions: Optional[
            Literal[C.PERPENDICULAR, C.EQUALRADIUS, C.IDENTICAL, C.TANGENT, C.PARALLEL, C.CONCENTRIC]
        ] = None,
        dragMethod: Literal[C.WEIGHTED, C.RELAXATION, C.MINIMUM_MOVE, C.STANDARD] = MINIMUM_MOVE,
        editMethod: Literal[C.WEIGHTED, C.RELAXATION, C.MINIMUM_MOVE, C.STANDARD] = STANDARD,
    ):
        """This method modifies the ConstrainedSketchOptions object.

        Parameters
        ----------
        sheetSize
            A Float specifying the sheet size. Possible values are Floats > 0. The default value is
            the **sheetSize** specified with the Sketch method.
        gridSpacing
            A Float specifying the spacing between gridlines. Possible values are Floats > 0. The
            default value is approximately 2.5% of **sheetSize**.
        grid
            A Boolean specifying whether the grid is shown. The default value is ON.
        gridFrequency
            An Int specifying how often gridlines are shown. Possible values are **gridFrequency** >
            0. The default value is 1.
        dimensionTextHeight
            A Float specifying the height of the dimension text in points. Possible values are
            Floats > 0. The default value is 12.0.
        decimalPlaces
            An Int specifying how many decimal places are shown in dimensions. Possible values are 0
            ≤ **decimalPlaces** ≤ 6. The initial value depends on the value of **sheetSize**.
        constructionGeometry
            A Boolean specifying whether construction geometry is shown. The default value is ON.
        gridSnap
            A Boolean specifying whether the cursor snaps to the grid. The default value is ON.
        preselection
            A Boolean specifying whether geometry will be preselected. The default value is ON.
        sheetAuto
            A Boolean specifying if the sheet size and the grid spacing are automatically computed.
            The default value is ON.
        gridOrigin
            A sequence of Floats specifying the **X - Y** coordinates for the origin of the grid. The
            default value is (0, 0).
        gridAngle
            A Float specifying the angle of the grid relative to the computer screen. The default
            value is 0.0.
        viewStyle
            A SymbolicConstant specifying the type of sketch displayed in the viewport. Possible
            values are REGULAR and AXISYM. The default value is REGULAR.
        addImpliedConstraints
            A Boolean specifying if implied constraints are added during sketching. The default
            value is ON.
        maxCoplanarEntities
            An Int specifying the maximum number of coplanar entities which should be automatically
            projected from the background, when a sketch based feature is created or edited. When
            this value is exceeded no entities are automatically projected and a warning issued.
            Possible values are **maxCoplanarEntities** > 0. The default value is 300.
        autoConstrainAngularTolerance
            A Float specifying the angular tolerance in degrees which is used to determine parallel
            and tangential conditions during the auto-constrain operation. For example any two lines
            which have an angle smaller than the given **autoConstrainAngularTolerance** will be
            assumed to be parallel, and a parallel constrain may be added during the auto-constrain
            operation. The default value is 0.01.
        autoConstrainLinearTolerance
            A Float specifying the linear tolerance which is used to determine when two points or
            geometries are coincident during the auto-constrain operation. The default value is
            10-6.
        autoConstrainOptions
            A sequence of SymbolicConstants specifying which type of constraints may be added by the
            auto-constraint tool. Possible values are PARALLEL, PERPENDICULAR, IDENTICAL, TANGENT,
            CONCENTRIC, and EQUALRADIUS. The default value is (PARALLEL,, PERPENDICULAR,,
            IDENTICAL,, TANGENT,, CONCENTRIC,, EQUALRADIUS).
        dragMethod
            A SymbolicConstant specifying the constraint solving mode used by the sketcher during
            drag operation. Possible values are MINIMUM_MOVE, STANDARD, WEIGHTED, and RELAXATION.
            The default value is MINIMUM_MOVE.
        editMethod
            A SymbolicConstant specifying the constraint solving mode used by the sketcher during
            regular sketch editing and adding new constraints and dimensions. Possible values are
            MINIMUM_MOVE, STANDARD, WEIGHTED, and RELAXATION. The default value is STANDARD.

        Raises
        ------
        RangeError

        """
        ...
