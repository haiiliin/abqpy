from typing_extensions import Literal
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .PredefinedField import PredefinedField
from ..Assembly.PartInstanceArray import PartInstanceArray
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import Boolean, LAST_STEP, OFF, STEP_END, SymbolicConstant


@abaqus_class_doc
class InitialState(PredefinedField):
    """The InitialState object stores the data for an initial state predefined field.
    The InitialState object is derived from the PredefinedField object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].predefinedFields[name]

        The corresponding analysis keywords are:

        - INSTANCE
    """

    #: A String specifying the repository key.
    name: str

    #: A :py:class:`~abaqus.Assembly.PartInstanceArray.PartInstanceArray` object specifying the instances to which the predefined field is
    #: applied.
    instances: PartInstanceArray

    #: A String specifying the name of the job that generated the initial state data.
    fileName: str

    #: The SymbolicConstant LAST_STEP or an Int specifying the step from which the initial
    #: state values are to be read or the SymbolicConstant LAST_STEP. The default value is
    #: LAST_STEP.
    endStep: SymbolicConstant = LAST_STEP

    #: The SymbolicConstant STEP_END or an Int specifying the increment, interval or iteration
    #: of the step set in **endStep** or the SymbolicConstant STEP_END. The default value is
    #: STEP_END.
    endIncrement: SymbolicConstant = STEP_END

    #: A Boolean specifying whether to update the reference configuration based on the import
    #: data. The default value is OFF.
    updateReferenceConfiguration: Boolean = OFF

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        instances: PartInstanceArray,
        fileName: str,
        endStep: Literal[C.LAST_STEP] = LAST_STEP,
        endIncrement: Literal[C.STEP_END] = STEP_END,
        updateReferenceConfiguration: Boolean = OFF,
    ):
        """This method creates an InitialState predefined field object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].InitialState

        Parameters
        ----------
        name
            A String specifying the repository key.
        instances
            A :py:class:`~abaqus.Assembly.PartInstanceArray.PartInstanceArray` object specifying the instances to which the predefined field is
            applied.
        fileName
            A String specifying the name of the job that generated the initial state data.
        endStep
            The SymbolicConstant LAST_STEP or an Int specifying the step from which the initial
            state values are to be read or the SymbolicConstant LAST_STEP. The default value is
            LAST_STEP.
        endIncrement
            The SymbolicConstant STEP_END or an Int specifying the increment, interval or iteration
            of the step set in **endStep** or the SymbolicConstant STEP_END. The default value is
            STEP_END.
        updateReferenceConfiguration
            A Boolean specifying whether to update the reference configuration based on the import
            data. The default value is OFF.

        Returns
        -------
        InitialState
            An :py:class:`~abaqus.PredefinedField.InitialState.InitialState` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        endStep: Literal[C.LAST_STEP] = LAST_STEP,
        endIncrement: Literal[C.STEP_END] = STEP_END,
        updateReferenceConfiguration: Boolean = OFF,
    ):
        """This method modifies the InitialState object.

        Parameters
        ----------
        endStep
            The SymbolicConstant LAST_STEP or an Int specifying the step from which the initial
            state values are to be read or the SymbolicConstant LAST_STEP. The default value is
            LAST_STEP.
        endIncrement
            The SymbolicConstant STEP_END or an Int specifying the increment, interval or iteration
            of the step set in **endStep** or the SymbolicConstant STEP_END. The default value is
            STEP_END.
        updateReferenceConfiguration
            A Boolean specifying whether to update the reference configuration based on the import
            data. The default value is OFF.
        """
        ...
