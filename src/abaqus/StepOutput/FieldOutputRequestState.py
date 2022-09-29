from typing import Union, Optional

from abqpy.decorators import abaqus_class_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class FieldOutputRequestState:
    """The FieldOutputRequestState object stores the propagating data of a field output request
    current in a step. One instance of this object is created internally by the
    FieldOutputRequest object for each step. The instance is also deleted internally by the
    FieldOutputRequest object.
    The FieldOutputRequestState object has no constructor or methods.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].fieldOutputRequestState[name]
    """

    #: A SymbolicConstant specifying the propagation state of the field output request
    #: variables. Possible values are UNSET, SET, and UNCHANGED.
    variablesState: Optional[SymbolicConstant] = None

    #: The SymbolicConstant LAST_INCREMENT or an Int specifying the output frequency in
    #: increments. The default value is 1.
    frequency: SymbolicConstant = 1

    #: A SymbolicConstant specifying the propagation state of the field output request
    #: frequency. Possible values are UNSET, SET, and UNCHANGED.
    frequencyState: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the field output request modes.
    #: Possible values are UNSET, SET, and UNCHANGED.
    modesState: Optional[SymbolicConstant] = None

    #: The SymbolicConstant EVERY_TIME_INCREMENT or a Float specifying the time interval at
    #: which the output states are to be written. The default value is EVERY_TIME_INCREMENT.
    timeInterval: Union[SymbolicConstant, float] = EVERY_TIME_INCREMENT

    #: A SymbolicConstant specifying the propagation state of the field output request time
    #: interval. Possible values are UNSET, SET, and UNCHANGED.
    timeIntervalState: Optional[SymbolicConstant] = None

    #: An Int specifying the number of intervals during the step at which output database
    #: states are to be written. The default value is 20.
    numIntervals: int = 20

    #: A SymbolicConstant specifying the propagation state of the field output request.
    #: Possible values are UNSET, SET, and UNCHANGED.
    numIntervalsState: Optional[SymbolicConstant] = None

    #: A Boolean specifying when to write results to the output database. The default value is
    #: OFF.
    timeMarks: Boolean = OFF

    #: A SymbolicConstant specifying the propagation state of the field output request.
    #: Possible values are UNSET, SET, and UNCHANGED.
    timeMarksState: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the field output request.
    #: Possible values are UNSET, SET, and UNCHANGED.
    timePointState: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the FieldOutputRequestState
    #: object. Possible values are NOT_YET_ACTIVE, CREATED, PROPAGATED, MODIFIED, DEACTIVATED,
    #: NO_LONGER_ACTIVE, TYPE_NOT_APPLICABLE, and INSTANCE_NOT_APPLICABLE.
    status: Optional[SymbolicConstant] = None

    #: A tuple of Strings specifying output request variable or component names, or the
    #: SymbolicConstant PRESELECT or ALL. PRESELECT represents all default output variables for
    #: the given step. ALL represents all valid output variables.
    variables: Optional[SymbolicConstant] = None

    #: The SymbolicConstant ALL or a tuple of Ints specifying a list of eigenmodes for which
    #: output is desired. The default value is ALL.
    modes: SymbolicConstant = ALL

    #: A String specifying the name of a time point object used to determine which output
    #: database states are to be written. The default value is an empty string.
    timePoint: str = ""

    #: A String specifying a read-only SymbolicConstant describing which type of frequency of
    #: output is used. Possible values areFREQUENCY, NUMBER_INTERVALS, TIME_INTERVAL,
    #: TIME_POINT and MODES. The default value depends on the procedure. The default value is
    #: an empty string.
    frequencyType: str = ""
