from typing import Optional, overload

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class HistoryOutput:
    """The HistoryOutput object contains the history output at a point for the specified
    variable.

    .. note:: 
        This object can be accessed by::

            import odbAccess
            session.odbs[name].steps[name].historyRegions[name].historyOutputs[name]
    """

    #: A tuple of pairs of Floats specifying the pairs (*frameValue*, **value**) where
    #: **frameValue** is either time, frequency, or mode and **value** is the value of the
    #: specified variable at **frameValue**. (This value depends on the type of the variable.)
    data: Optional[float] = None

    #: A tuple of pairs of Floats specifying the imaginary portion of a specified complex
    #: variable at each frame value (time, frequency, or mode). The pairs have the form
    #: (*frameValue*, **value**).
    conjugateData: Optional[float] = None

    #: A String specifying the output variable name.
    name: str

    #: A String specifying the output variable.
    description: str

    #: A SymbolicConstant specifying the output type. Only SCALAR is currently supported.
    type: SymbolicConstant

    #: A sequence of SymbolicConstants specifying which invariants should be calculated for
    #: this field. Possible values are MAGNITUDE, MISES, TRESCA, PRESS, INV3, MAX_PRINCIPAL,
    #: MID_PRINCIPAL, and MIN_PRINCIPAL. The default value is an empty sequence.
    validInvariants: Optional[SymbolicConstant] = None

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        description: str,
        type: Literal[SCALAR],
        validInvariants: Optional[SymbolicConstant] = None,
    ) -> None:
        """This method creates a HistoryOutput object.

        .. note:: 
            This function can be accessed by::

                session.odbs[name].steps[name].historyRegions[name].HistoryOutput

        Parameters
        ----------
        name
            A String specifying the output variable name.
        description
            A String specifying the output variable.
        type
            A SymbolicConstant specifying the output type. Only SCALAR is currently supported.
        validInvariants
            A sequence of SymbolicConstants specifying which invariants should be calculated for
            this field. Possible values are MAGNITUDE, MISES, TRESCA, PRESS, INV3, MAX_PRINCIPAL,
            MID_PRINCIPAL, and MIN_PRINCIPAL. The default value is an empty sequence.

        Returns
        -------
        HistoryOutput
            A :py:class:`~abaqus.Odb.HistoryOutput.HistoryOutput` object.
        """
        ...

    @overload
    @abaqus_method_doc
    def addData(self, frame: str, value: str) -> None:
        """This method adds data to the **data** member of the HistoryOutput object.

        Parameters
        ----------
        frame
            A Double specifying the frame value. **frame** can be specified in step time, frequency,
            or mode number.
        value
            A Double specifying the value of the variable at the frame value specified in **frame**.
        """
        ...

    @overload
    @abaqus_method_doc
    def addData(self, frame: tuple, value: tuple) -> None:
        """This method adds data to the **data** member of the HistoryOutput object.

        Parameters
        ----------
        frame
            A sequence of Floats specifying the frame values. **frame** can be specified in step time,
            frequency, or mode number.
        value
            A sequence of Floats specifying the value of the variable at the frame values specified
            in **frame**.

        Raises
        ------
        ValueError
            If the length of **frame** is not the same as the length of **value**.
        """
        ...

    @overload
    @abaqus_method_doc
    def addData(self, data: tuple) -> None:
        """This method adds data to the **data** member of the HistoryOutput object.

        Parameters
        ----------
        data
            A sequence of pairs of Floats specifying the pairs (*frameValue*, **value**) where
            **frameValue** is either time, frequency, or mode and **value** is the value of the
            specified variable at **frameValue**. (This value depends on the type of the variable.)
        """
        ...

    def addData(self, *args, **kwargs) -> None:
        ...
