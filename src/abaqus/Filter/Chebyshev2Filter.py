from abaqusConstants import *
from .Filter import Filter


class Chebyshev2Filter(Filter):
    """The Chebyshev2Filter object defines a Chebyshev type 2 filter.
    The Chebyshev2Filter object is derived from the Filter object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import filter
        mdb.models[name].filters[name]
        import odbFilter
        session.odbs[name].filters[name]

    The corresponding analysis keywords are:

    - FILTER

    """

    def __init__(
        self,
        name: str,
        cutoffFrequency: float,
        rippleFactor: float = 0,
        order: int = 2,
        operation: SymbolicConstant = NONE,
        halt: Boolean = OFF,
        limit: float = None,
        invariant: SymbolicConstant = NONE,
    ):
        """This method creates a Chebyshev2Filter object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Chebyshev2Filter
            session.odbs[name].Chebyshev2Filter

        Parameters
        ----------
        name
            A String specifying the repository key. This name ANTIALIASING is reserved for filters
            generated internally by the program.
        cutoffFrequency
            A Float specifying the attenuation point of the filter. Possible values are non-negative
            numbers. Order is not available for OperatorFilter.
        rippleFactor
            A Float specifying the amount of allowable ripple in the filter. Possible values are
            non-negative numbers less than 1. The default value is 0.025.
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
            A Chebyshev2Filter object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        super().__init__()
        pass

    def setValues(
        self,
        rippleFactor: float = 0,
        order: int = 2,
        operation: SymbolicConstant = NONE,
        halt: Boolean = OFF,
        limit: float = None,
        invariant: SymbolicConstant = NONE,
    ):
        """This method modifies the Chebyshev2Filter object.

        Parameters
        ----------
        rippleFactor
            A Float specifying the amount of allowable ripple in the filter. Possible values are
            non-negative numbers less than 1. The default value is 0.025.
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
        pass
