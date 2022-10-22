from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import Boolean, ENGINEERING, ON, SymbolicConstant


@abaqus_class_doc
class NumberFormat:
    """The NumberFormat object is a formatting template used to define formatting options for
    certain numeric output.This page
    discusses:Access[NumberFormat(...)](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-numberformatpyc.htm?ContextScope=all#simaker-numberformatnumberformatpyc)Members

    .. note:: 
        This object can be accessed by::

            import visualization
            session.defaultFieldReportOptions.numberFormat
            session.fieldReportOptions.numberFormat
            session.journalOptions.defaultFormat
            session.journalOptions.fieldReportFormat
            session.journalOptions.geometryFormat
    """

    #: A Boolean specifying whether the printed digits should be padded with blank characters
    #: to ensure equal sized fields. The **blankPad** argument is useful when your printed output
    #: includes columns. The default value is ON.
    blankPad: Boolean = ON

    #: A SymbolicConstant specifying the formatting type. Possible values are ENGINEERING,
    #: SCIENTIFIC, and AUTOMATIC. The default value is ENGINEERING.
    format: SymbolicConstant = ENGINEERING

    #: An Int specifying the number of digits to be displayed in the result. **numDigits** >0>0.
    #: The default value is 6.
    numDigits: int = 6

    #: An Int specifying the number of decimal places to which the number is to be truncated
    #: for display. **precision** ≤0≤0. If **precision** =0, no truncation is applied. The default
    #: value is 0.
    precision: int = 0

    @abaqus_method_doc
    def __init__(
        self,
        blankPad: Boolean = ON,
        format: SymbolicConstant = ENGINEERING,
        numDigits: int = 6,
        precision: int = 0,
    ):
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
        ...
