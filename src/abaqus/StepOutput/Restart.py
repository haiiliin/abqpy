from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class Restart:
    """The Restart object defines a restart request.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].restart

        The corresponding analysis keywords are:

        - RESTART
    """

    #: An Int specifying the number of intervals during the step at which restart information
    #: will be written. The default value is 0. The default value is 1.
    numberIntervals: int = 0

    #: A Boolean specifying whether to use exact time marks for writing during an analysis. The
    #: default value is OFF. The default value is OFF.
    timeMarks: Boolean = OFF

    #: A Boolean specifying that only one increment per step should be retained on the restart
    #: file, thus minimizing the size of the restart file. The default value is OFF. The
    #: default value is ON.
    overlay: Boolean = OFF

    #: An Int specifying the increments at which restart information will be written. The
    #: default value is 0. The default value is 0.This argument applies only to Abaqus/Standard
    #: analyses.
    frequency: int = 0

    @abaqus_method_doc
    def __init__(
        self,
        numberIntervals: int = 0,
        timeMarks: Boolean = OFF,
        overlay: Boolean = OFF,
        frequency: int = 0,
    ):
        """This method creates a restart request.

        .. note::
            This function can be accessed by::

                mdb.models[name].steps[name].Restart

        Parameters
        ----------
        numberIntervals
            An Int specifying the number of intervals during the step at which restart information
            will be written. The default value is 0. The default value is 1.
        timeMarks
            A Boolean specifying whether to use exact time marks for writing during an analysis. The
            default value is OFF. The default value is OFF.
        overlay
            A Boolean specifying that only one increment per step should be retained on the restart
            file, thus minimizing the size of the restart file. The default value is OFF. The
            default value is ON.
        frequency
            An Int specifying the increments at which restart information will be written. The
            default value is 0. The default value is 0.This argument applies only to Abaqus/Standard
            analyses.

        Returns
        -------
        Restart
            A :py:class:`~abaqus.StepOutput.Restart.Restart` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Restart object.

        Raises
        ------
        RangeError
        """
        ...
