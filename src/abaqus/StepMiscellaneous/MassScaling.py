from typing import Optional

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import (
    BELOW_MIN,
    GLOBAL_X,
    MODEL,
    SEMI_AUTOMATIC,
    SymbolicConstant,
)


@abaqus_class_doc
class MassScaling:
    """A MassScaling object defines the region and controls that govern mass scaling.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].massScaling[i]
    """

    #: A SymbolicConstant specifying the objective of the mass scaling definition. Possible
    #: values are SEMI_AUTOMATIC, AUTOMATIC, and REINITIALIZE. The default value is
    #: SEMI_AUTOMATIC.
    objective: SymbolicConstant = SEMI_AUTOMATIC

    #: A SymbolicConstant specifying whether mass scaling should be performed at the beginning
    #: of the step or throughout the step. Possible values are AT_BEGINNING and
    #: THROUGHOUT_STEP.
    occurs: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the type of scaling. Possible values are UNIFORM,
    #: BELOW_MIN, SET_EQUAL_DT, and ROLLING. The default value is BELOW_MIN.
    type: SymbolicConstant = BELOW_MIN

    #: A Float specifying a scaling factor.
    factor: Optional[float] = None

    #: A Float specifying a target time increment.
    dt: Optional[float] = None

    #: An Int specifying the frequency at which mass scaling calculations are performed.
    frequency: Optional[int] = None

    #: An Int specifying the number of intervals at which mass scaling calculations are
    #: performed.
    numberInterval: Optional[int] = None

    #: A Float specifying the estimated average velocity of the workpiece in the rolling
    #: direction at steady-state conditions.
    feedRate: Optional[float] = None

    #: A Float specifying the average element length in the extruded direction.
    extrudedLength: Optional[float] = None

    #: An Int specifying the number of nodes in the cross-section of the workpiece.
    crossSection: Optional[int] = None

    #: A SymbolicConstant specifying the rolling direction. Possible values are GLOBAL_X,
    #: GLOBAL_Y, GLOBAL_Z, and GLOBAL_NONE. The default value is GLOBAL_X.
    direction: SymbolicConstant = GLOBAL_X

    #: The SymbolicConstant MODEL or a Region object specifying where the mass scaling is
    #: applied. The default value is MODEL.
    region: SymbolicConstant = MODEL
