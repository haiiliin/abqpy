from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Filter import Filter
from ..UtilityAndView.abaqusConstants import Boolean, NONE, OFF, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class OperatorFilter(Filter):
    """The OperatorFilter object defines an operator filter.
    The OperatorFilter object is derived from the Filter object.

    .. note::
        This object can be accessed by::

            import filter
            mdb.models[name].filters[name]
            import odbFilter
            session.odbs[name].filters[name]

        The corresponding analysis keywords are:

        - FILTER
    """

    #: A String specifying the repository key. This name ANTIALIASING is reserved for filters
    #: generated internally by the program.
    name: str

    #: A Float specifying the attenuation point of the filter. Possible values are non-negative
    #: numbers. Order is not available for OperatorFilter.
    cutoffFrequency: float

    #: An Int specifying the highest power of the filter transfer function. Possible values are
    #: non-negative numbers less than or equal to 20. Order is not available for
    #: OperatorFilter. The default value is 2.
    order: int = 2

    #: A SymbolicConstant specifying the filter operator. Possible values are NONE, MIN, MAX,
    #: and ABS. The default value is NONE.
    operation: SymbolicConstant = NONE

    #: A Boolean specifying whether to stop the analysis if the specified limit is reached. The
    #: default value is OFF.
    halt: Boolean = OFF

    #: None or a Float specifying the threshold limit, an upper or lower bound for output
    #: values depending on the operation, or a bound for stopping the analysis when Halt is
    #: used. The default value is None.
    limit: Optional[float] = None

    #: A SymbolicConstant specifying the invariant to which filtering is applied. Possible
    #: values are NONE, FIRST, and SECOND. The default value is NONE.
    invariant: SymbolicConstant = NONE

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        cutoffFrequency: float,
        order: int = 2,
        operation: Literal[C.MIN, C.MAX, C.NONE, C.ABS] = NONE,
        halt: Boolean = OFF,
        limit: Optional[float] = None,
        invariant: Literal[C.FIRST, C.SECOND, C.NONE] = NONE,
    ):
        """This method creates an OperatorFilter object.

        .. note::
            This function can be accessed by::

                mdb.models[name].OperatorFilter
                session.odbs[name].OperatorFilter

        Parameters
        ----------
        name
            A String specifying the repository key. This name ANTIALIASING is reserved for filters
            generated internally by the program.
        cutoffFrequency
            A Float specifying the attenuation point of the filter. Possible values are non-negative
            numbers. Order is not available for OperatorFilter.
        order
            An Int specifying the highest power of the filter transfer function. Possible values are
            non-negative numbers less than or equal to 20. Order is not available for
            OperatorFilter. The default value is 2.
        operation
            A SymbolicConstant specifying the filter operator. Possible values are NONE, MIN, MAX,
            and ABS. The default value is NONE.
        halt
            A Boolean specifying whether to stop the analysis if the specified limit is reached. The
            default value is OFF.
        limit
            None or a Float specifying the threshold limit, an upper or lower bound for output
            values depending on the operation, or a bound for stopping the analysis when Halt is
            used. The default value is None.
        invariant
            A SymbolicConstant specifying the invariant to which filtering is applied. Possible
            values are NONE, FIRST, and SECOND. The default value is NONE.

        Returns
        -------
        OperatorFilter
            An :py:class:`~abaqus.Filter.OperatorFilter.OperatorFilter` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        order: int = 2,
        operation: Literal[C.MIN, C.MAX, C.NONE, C.ABS] = NONE,
        halt: Boolean = OFF,
        limit: Optional[float] = None,
        invariant: Literal[C.FIRST, C.SECOND, C.NONE] = NONE,
    ):
        """This method modifies the OperatorFilter object.

        Parameters
        ----------
        order
            An Int specifying the highest power of the filter transfer function. Possible values are
            non-negative numbers less than or equal to 20. Order is not available for
            OperatorFilter. The default value is 2.
        operation
            A SymbolicConstant specifying the filter operator. Possible values are NONE, MIN, MAX,
            and ABS. The default value is NONE.
        halt
            A Boolean specifying whether to stop the analysis if the specified limit is reached. The
            default value is OFF.
        limit
            None or a Float specifying the threshold limit, an upper or lower bound for output
            values depending on the operation, or a bound for stopping the analysis when Halt is
            used. The default value is None.
        invariant
            A SymbolicConstant specifying the invariant to which filtering is applied. Possible
            values are NONE, FIRST, and SECOND. The default value is NONE.

        Raises
        ------
        RangeError
        """
        ...
