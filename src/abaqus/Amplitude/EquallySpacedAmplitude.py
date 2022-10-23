from typing import Union

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Amplitude import Amplitude
from .BaselineCorrection import BaselineCorrection
from ..UtilityAndView.abaqusConstants import SOLVER_DEFAULT, STEP, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class EquallySpacedAmplitude(Amplitude):
    """The EquallySpacedAmplitude object defines a list of amplitude values at fixed time
    intervals beginning at a specified value of time.
    The EquallySpacedAmplitude object is derived from the Amplitude object.

    .. note:: 
        This object can be accessed by::

            import amplitude
            mdb.models[name].amplitudes[name]
            import odbAmplitude
            session.odbs[name].amplitudes[name]

        The corresponding analysis keywords are:

        - AMPLITUDE
    """

    #: A :py:class:`~abaqus.Amplitude.BaselineCorrection.BaselineCorrection` object.
    baselineCorrection: BaselineCorrection = BaselineCorrection()

    #: A String specifying the repository key.
    name: str

    #: A Float specifying the fixed time interval at which the amplitude data are given.
    #: Possible values are positive numbers.
    fixedInterval: float

    #: A sequence of Floats specifying the amplitude values.
    data: tuple

    #: A Float specifying the time at which the first amplitude data are given. Possible values
    #: are non-negative numbers. The default value is 0.0.
    begin: float = 0

    #: The SymbolicConstant SOLVER_DEFAULT or a Float specifying the degree of smoothing.
    #: Possible float values are 0 ≤ **smoothing** ≤ 0.5. If **smooth** = SOLVER_DEFAULT, the
    #: default degree of smoothing will be determined by the solver. The default value is
    #: SOLVER_DEFAULT.
    smooth: Union[SymbolicConstant, float] = SOLVER_DEFAULT

    #: A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
    #: and TOTAL. The default value is STEP.
    timeSpan: SymbolicConstant = STEP

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        fixedInterval: float,
        data: tuple,
        begin: float = 0,
        smooth: Union[Literal[C.SOLVER_DEFAULT], float] = SOLVER_DEFAULT,
        timeSpan: Literal[C.STEP, C.TOTAL] = STEP,
    ):
        """This method creates an EquallySpacedAmplitude object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].EquallySpacedAmplitude
                session.odbs[name].EquallySpacedAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key.
        fixedInterval
            A Float specifying the fixed time interval at which the amplitude data are given.
            Possible values are positive numbers.
        data
            A sequence of Floats specifying the amplitude values.
        begin
            A Float specifying the time at which the first amplitude data are given. Possible values
            are non-negative numbers. The default value is 0.0.
        smooth
            The SymbolicConstant SOLVER_DEFAULT or a Float specifying the degree of smoothing.
            Possible float values are 0 ≤ **smoothing** ≤ 0.5. If **smooth** = SOLVER_DEFAULT, the
            default degree of smoothing will be determined by the solver. The default value is
            SOLVER_DEFAULT.
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
            and TOTAL. The default value is STEP.

        Returns
        -------
        EquallySpacedAmplitude
            An :py:class:`~abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        begin: float = 0,
        smooth: Union[Literal[C.SOLVER_DEFAULT], float] = SOLVER_DEFAULT,
        timeSpan: Literal[C.STEP, C.TOTAL] = STEP,
    ):
        """This method modifies the EquallySpacedAmplitude object.

        Parameters
        ----------
        begin
            A Float specifying the time at which the first amplitude data are given. Possible values
            are non-negative numbers. The default value is 0.0.
        smooth
            The SymbolicConstant SOLVER_DEFAULT or a Float specifying the degree of smoothing.
            Possible float values are 0 ≤ **smoothing** ≤ 0.5. If **smooth** = SOLVER_DEFAULT, the
            default degree of smoothing will be determined by the solver. The default value is
            SOLVER_DEFAULT.
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
            and TOTAL. The default value is STEP.

        Raises
        ------
        RangeError
        """
        ...
