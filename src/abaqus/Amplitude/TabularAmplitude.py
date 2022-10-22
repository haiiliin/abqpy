from typing import Union, Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Amplitude import Amplitude
from .BaselineCorrection import BaselineCorrection
from ..UtilityAndView.abaqusConstants import SOLVER_DEFAULT, STEP, TOTAL


@abaqus_class_doc
class TabularAmplitude(Amplitude):
    """The TabularAmplitude object defines an amplitude curve as a table of values at
    convenient points on the time scale.
    The TabularAmplitude object is derived from the Amplitude object.

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

    #: A sequence of pairs of Floats specifying time/frequency and amplitude pairs. Possible
    #: values for time/frequency are positive numbers.
    data: Sequence[Sequence[float]]

    #: The SymbolicConstant SOLVER_DEFAULT or a Float specifying the degree of smoothing.
    #: Possible float values are between 0 and 0.5. If **smooth** = SOLVER_DEFAULT, the default
    #: degree of smoothing will be determined by the solver. The default value is
    #: SOLVER_DEFAULT.
    smooth: Union[Literal[SOLVER_DEFAULT], float] = SOLVER_DEFAULT

    #: A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
    #: and TOTAL. The default value is STEP.
    timeSpan: Literal[STEP, TOTAL] = STEP

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        data: Sequence[Sequence[float]],
        smooth: Union[Literal[SOLVER_DEFAULT], float] = SOLVER_DEFAULT,
        timeSpan: Literal[STEP, TOTAL] = STEP,
    ):
        """This method creates a TabularAmplitude object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].TabularAmplitude
                session.odbs[name].TabularAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key.
        data
            A sequence of pairs of Floats specifying time/frequency and amplitude pairs. Possible
            values for time/frequency are positive numbers.
        smooth
            The SymbolicConstant SOLVER_DEFAULT or a Float specifying the degree of smoothing.
            Possible float values are between 0 and 0.5. If **smooth** = SOLVER_DEFAULT, the default
            degree of smoothing will be determined by the solver. The default value is
            SOLVER_DEFAULT.
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
            and TOTAL. The default value is STEP.

        Returns
        -------
        TabularAmplitude
            A :py:class:`~abaqus.Amplitude.TabularAmplitude.TabularAmplitude` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        smooth: Union[Literal[SOLVER_DEFAULT], float] = SOLVER_DEFAULT,
        timeSpan: Literal[STEP, TOTAL] = STEP,
    ):
        """This method modifies the TabularAmplitude object.

        Parameters
        ----------
        smooth
            The SymbolicConstant SOLVER_DEFAULT or a Float specifying the degree of smoothing.
            Possible float values are between 0 and 0.5. If **smooth** = SOLVER_DEFAULT, the default
            degree of smoothing will be determined by the solver. The default value is
            SOLVER_DEFAULT.
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
            and TOTAL. The default value is STEP.

        Raises
        ------
        RangeError
        """
        ...
