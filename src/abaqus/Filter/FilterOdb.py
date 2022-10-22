from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .ButterworthFilter import ButterworthFilter
from .Chebyshev1Filter import Chebyshev1Filter
from .Chebyshev2Filter import Chebyshev2Filter
from .OperatorFilter import OperatorFilter
from ..Odb.OdbBase import OdbBase
from ..UtilityAndView.abaqusConstants import Boolean, NONE, OFF, SymbolicConstant


@abaqus_class_doc
class FilterOdb(OdbBase):
    """The Odb object is the in-memory representation of an output database (ODB) file.

    .. note:: 
        This object can be accessed by::

            import odbAccess
            session.odbs[name]
    """

    @abaqus_method_doc
    def ButterworthFilter(
        self,
        name: str,
        cutoffFrequency: float,
        order: int = 2,
        operation: SymbolicConstant = NONE,
        halt: Boolean = OFF,
        limit: Optional[float] = None,
        invariant: SymbolicConstant = NONE,
    ) -> ButterworthFilter:
        """This method creates a ButterworthFilter object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ButterworthFilter
                session.odbs[name].ButterworthFilter

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
        ButterworthFilter
            A :py:class:`~abaqus.Filter.ButterworthFilter.ButterworthFilter` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.filters[name] = butterworthFilter = ButterworthFilter(
            name, cutoffFrequency, order, operation, halt, limit, invariant
        )
        return butterworthFilter

    @abaqus_method_doc
    def Chebyshev1Filter(
        self,
        name: str,
        cutoffFrequency: float,
        rippleFactor: float = 0,
        order: int = 2,
        operation: SymbolicConstant = NONE,
        halt: Boolean = OFF,
        limit: Optional[float] = None,
        invariant: SymbolicConstant = NONE,
    ) -> Chebyshev1Filter:
        """This method creates a Chebyshev1Filter object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].Chebyshev1Filter
                session.odbs[name].Chebyshev1Filter

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
            non-negative numbers. The default value is 0.225.
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
        Chebyshev1Filter
            A :py:class:`~abaqus.Filter.Chebyshev1Filter.Chebyshev1Filter` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.filters[name] = chebyshev1Filter = Chebyshev1Filter(
            name,
            cutoffFrequency,
            rippleFactor,
            order,
            operation,
            halt,
            limit,
            invariant,
        )
        return chebyshev1Filter

    @abaqus_method_doc
    def Chebyshev2Filter(
        self,
        name: str,
        cutoffFrequency: float,
        rippleFactor: float = 0,
        order: int = 2,
        operation: SymbolicConstant = NONE,
        halt: Boolean = OFF,
        limit: Optional[float] = None,
        invariant: SymbolicConstant = NONE,
    ) -> Chebyshev2Filter:
        """This method creates a Chebyshev2Filter object.

        .. note:: 
            This function can be accessed by::

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
        Chebyshev2Filter
            A :py:class:`~abaqus.Filter.Chebyshev2Filter.Chebyshev2Filter` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.filters[name] = chebyshev2Filter = Chebyshev2Filter(
            name,
            cutoffFrequency,
            rippleFactor,
            order,
            operation,
            halt,
            limit,
            invariant,
        )
        return chebyshev2Filter

    @abaqus_method_doc
    def OperatorFilter(
        self,
        name: str,
        cutoffFrequency: float,
        order: int = 2,
        operation: SymbolicConstant = NONE,
        halt: Boolean = OFF,
        limit: Optional[float] = None,
        invariant: SymbolicConstant = NONE,
    ) -> OperatorFilter:
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
        self.filters[name] = operatorFilter = OperatorFilter(
            name, cutoffFrequency, order, operation, halt, limit, invariant
        )
        return operatorFilter
