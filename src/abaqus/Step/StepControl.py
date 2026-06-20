from __future__ import annotations

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class StepControl:
    """The StepControl object is used to control the progress of a simulation based on the
    solution state.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].stepControls[name]

    .. versionadded:: 2025
        The ``StepControl`` class was added.
    """

    #: A String specifying the name of the object.
    name: str = ""

    #: A Tuple of tuples specifying the values according to the data lines given in STEP CONTROL.
    data: tuple = ()

    #: A SymbolicConstant defining a value of ACTION. The default value is CONTINUE.
    action: SymbolicConstant = C.CONTINUE

    #: A SymbolicConstant defining a value of DT REFINEMENT. The default value is YES.
    dtRefinement: SymbolicConstant = C.YES

    #: A float defining a value of TOLERANCE. The default value is 0.001.
    tolerance: float = 0.001

    #: A Boolean specifying whether the step control is suppressed or not. The default value is
    #: OFF.
    suppressed: bool = False

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        data: tuple,
        action: SymbolicConstant = C.CONTINUE,
        dtRefinement: SymbolicConstant = C.YES,
        tolerance: float = 0.001,
    ):
        """This method creates a step control in a step.

        .. note::
            This function can be accessed by::

                mdb.models[name].steps[name].StepControl

        Parameters
        ----------
        name
            A String specifying the name of the object.
        data
            A Tuple of tuples specifying the values according to the data lines given in STEP CONTROL.
            Example: If DT REFINEMENT = YES and ACTION = CONTINUE, then data = ((sensor name, Time
            increment value, sensor limit when the time increment refinement starts, Sensor limit
            value when the time increment refinement ends),). You can specify multiple tuples
            according to the number of sensors to be introduced; each inner tuple is considered as a
            new data line.
        action
            A SymbolicConstant defining a value of ACTION. The default value is CONTINUE.
        dtRefinement
            A SymbolicConstant defining a value of DT REFINEMENT. The default value is YES.
        tolerance
            A float defining a value of TOLERANCE. The default value is 0.001.

        Returns
        -------
        StepControl
            A StepControl object.

        Exceptions
        ----------
        RangeError
        """
        ...

    @abaqus_method_doc
    def resume(self):
        """This method resumes the step control that was previously suppressed."""
        ...

    @abaqus_method_doc
    def suppress(self):
        """This method suppresses the step control."""
        ...

    @abaqus_method_doc
    def setValues(
        self,
        data: tuple | None = None,
        action: SymbolicConstant = C.CONTINUE,
        dtRefinement: SymbolicConstant = C.YES,
        tolerance: float = 0.001,
    ):
        """This method modifies the StepControl object.

        Parameters
        ----------
        data
            A Tuple of tuples specifying the values according to the data lines given in STEP CONTROL.
            Example: If DT REFINEMENT = YES and ACTION = CONTINUE, then data = ((sensor name, Time
            increment value, sensor limit when the time increment refinement starts, Sensor limit
            value when the time increment refinement ends),). You can specify multiple tuples
            according to the number of sensors to be introduced; each inner tuple is considered as a
            new data line.
        action
            A SymbolicConstant defining a value of ACTION. The default value is CONTINUE.
        dtRefinement
            A SymbolicConstant defining a value of DT REFINEMENT. The default value is YES.
        tolerance
            A float defining a value of TOLERANCE. The default value is 0.001.

        Exceptions
        ----------
        RangeError
        """
        ...
