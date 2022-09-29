from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..Session.NumberFormat import NumberFormat
from ..UtilityAndView.abaqusConstants import (ASCENDING, Boolean, ENGINEERING, NO_LIMIT, OFF, ON,
                                              SINGLE_TABLE, SymbolicConstant)


@abaqus_class_doc
class FieldReportOptions:
    """The FieldReportOptions object stores settings used by the writeFieldReport method when
    you write a FieldOutput object to an ASCII file. The FieldReportOptions object has no
    constructor. Abaqus creates the **fieldReportOptions** member when you import the
    Visualization module.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.defaultFieldReportOptions
            session.fieldReportOptions
    """

    #: Format of the number
    numberFormat: NumberFormat = NumberFormat()

    @abaqus_method_doc
    def setValues(
        self,
        numColumns: int,
        numberFormat: NumberFormat,
        printXYData: Boolean = ON,
        printTotal: Boolean = ON,
        printMinMax: Boolean = ON,
        pageWidth: SymbolicConstant = NO_LIMIT,
        columnLayout: SymbolicConstant = SINGLE_TABLE,
        sort: SymbolicConstant = ASCENDING,
    ):
        """This method modifies the FieldReportOptions object.

        Parameters
        ----------
        numColumns
            An Int specifying the number of columns to display for the tabular report. The default
            value is 80.
        numberFormat
            A :py:class:`~abaqus.Session.NumberFormat.NumberFormat` object specifying the format type, number of digits and precision used to
            print the numeric output.
        printXYData
            A Boolean specifying whether to include **X - Y** data values in the tabular report. The
            default value is ON.
        printTotal
            A Boolean specifying whether to include column totals in the tabular report. The default
            value is ON.
        printMinMax
            A Boolean specifying whether to include column summary minimum and maximum values in the
            tabular report. The default value is ON.
        pageWidth
            A SymbolicConstant specifying how the width of the tabular report is to be determined.
            Possible values are NO_LIMIT and SPECIFY. The default value is NO_LIMIT.
        columnLayout
            A SymbolicConstant specifying how values are to be presented in the tabular report.
            Possible values are SINGLE_TABLE and SEPARATE_TABLES. The default value is SINGLE_TABLE.
        sort
            A SymbolicConstant specifying the order in which values are to be sorted within a
            tabular report. Possible values are ASCENDING and DESCENDING. The default value is
            ASCENDING.

        Returns
        -------
        FieldReportOptions
            A :py:class:`~abaqus.FieldReport.FieldReportOptions.FieldReportOptions` object.
        """
        ...

    @abaqus_method_doc
    def NumberFormat(
        self,
        blankPad: Boolean = ON,
        format: SymbolicConstant = ENGINEERING,
        numDigits: int = 6,
        precision: int = 0,
    ) -> NumberFormat:
        """This method creates a NumberFormat object.

        .. note:: 
            This function can be accessed by::

                session.defaultFieldReportOptions.NumberFormat
                session.fieldReportOptions.NumberFormat
                session.journalOptions.NumberFormat

        Parameters
        ----------
        blankPad
            A Boolean specifying whether the printed digits should be padded with blank characters
            to ensure equal sized fields. The **blankPad** argument is useful when your printed output
            includes columns. The default value is ON.
        format
            A SymbolicConstant specifying the formatting type. Possible values are ENGINEERING,
            SCIENTIFIC, and AUTOMATIC. The default value is ENGINEERING.
        numDigits
            An Int specifying the number of digits to be displayed in the result. **numDigits** >0>0.
            The default value is 6.
        precision
            An Int specifying the number of decimal places to which the number is to be truncated
            for display. **precision** ≤0≤0. If **precision** =0, no truncation is applied. The default
            value is 0.

        Returns
        -------
        NumberFormat
            A :py:class:`~abaqus.Session.NumberFormat.NumberFormat` object.
        """
        self.numberFormat = numberFormat = NumberFormat(
            blankPad, format, numDigits, precision
        )
        return numberFormat
