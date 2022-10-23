from typing_extensions import Literal
from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .NumberFormat import NumberFormat
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import (Boolean, COMPRESSEDINDEX, ENGINEERING, ON)


@abaqus_class_doc
class JournalOptions:
    """A :py:class:`~abaqus.Session.JournalOptions.JournalOptions` object specifies how to record selection of geometry in the journal and
    replay files. **journalOptions** can also be used to set the numeric formatting options
    for field report output, geometry commands output, and a default format for other
    numeric output. The JournalOptions object has no constructor. Abaqus creates the
    **journalOptions** member when a session is started.

    .. note:: 
        This object can be accessed by::

            session.journalOptions
    """

    #: Format of the number
    numberFormat: NumberFormat = NumberFormat()

    @abaqus_method_doc
    def setValues(
        self,
        replayGeometry: Literal[C.COORDINATE, C.COMPRESSEDINDEX, C.INDEX] = COMPRESSEDINDEX,
        recoverGeometry: Literal[C.COORDINATE, C.COMPRESSEDINDEX, C.INDEX] = COMPRESSEDINDEX,
        defaultFormat: Optional[NumberFormat] = None, 
        fieldReportFormat: Optional[NumberFormat] = None, 
        geometryFormat: Optional[NumberFormat] = None, 
    ):
        """This method modifies the JournalOptions object.

        Parameters
        ----------
        replayGeometry
            A SymbolicConstant specifying the format of the geometry in the replay file. Possible
            values are COORDINATE, INDEX, and COMPRESSEDINDEX. The default value is COMPRESSEDINDEX.
        recoverGeometry
            A SymbolicConstant specifying the format of the geometry in the recovery file. Possible
            values are COORDINATE, INDEX, and COMPRESSEDINDEX. The default value is COMPRESSEDINDEX.
        defaultFormat
            A :py:class:`~abaqus.Session.NumberFormat.NumberFormat` object specifying the default format for numeric output. The default
            values are the same as the default values for the NumberFormat object.
        fieldReportFormat
            A :py:class:`~abaqus.Session.NumberFormat.NumberFormat` object specifying the default format for numbers in a field report
            output. The default values are the same as the default values for the NumberFormat
            object.
        geometryFormat
            A :py:class:`~abaqus.Session.NumberFormat.NumberFormat` object specifying the default format for numbers in geometry commands
            output. The default values are the same as the default values for the NumberFormat
            object.
        """
        ...

    @abaqus_method_doc
    def NumberFormat(
        self,
        blankPad: Boolean = ON,
        format: Literal[C.AUTOMATIC, C.ENGINEERING, C.SCIENTIFIC] = ENGINEERING,
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
