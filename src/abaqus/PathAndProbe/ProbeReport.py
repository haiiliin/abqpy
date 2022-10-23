from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ..UtilityAndView.abaqusConstants import Boolean, ENGINEERING, NO_LIMIT, OFF
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class ProbeReport:
    """The ProbeReport object is used to store settings associated with tabular reports of
    probe data. The ProbeReport object has no constructor. Abaqus creates the
    **defaultProbeReport** and the **probeReport** members when you import the Visualization
    module. When probing is initiated for the first time, the values in the **probeReport**
    member are initialized using the values from the **defaultProbeReport** member.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.defaultProbeReport
            session.probeReport
    """

    @abaqus_method_doc
    def setValues(
        self,
        options: Optional[str] = None,
        numColumns: int = 80,
        numDigits: int = 6,
        numFormat: Literal[C.AUTOMATIC, C.ENGINEERING, C.SCIENTIFIC] = ENGINEERING,
        pageWidth: Literal[C.SPECIFY, C.NO_LIMIT] = NO_LIMIT,
        printTotal: Boolean = OFF,
        printMinMax: Boolean = OFF,
    ):
        """This method modifies the ProbeReport object.

        Parameters
        ----------
        options
            None or a ProbeReport object specifying values to be copied. If other arguments are also
            supplied to setValues, they will override the values in **options**. The default value is
            None.
        numColumns
            An Int specifying the number of columns in the report file. This argument is valid only
            when **pageWidth** = SPECIFY. The default value is 80.
        numDigits
            An Int specifying the number of significant digits to be written for decimal values. The
            default value is 6.
        numFormat
            A SymbolicConstant specifying the number format to be used when formatting decimal
            values. Possible values are AUTOMATIC, ENGINEERING, and SCIENTIFIC. The default value is
            ENGINEERING.
        pageWidth
            A SymbolicConstant specifying the page width format. Possible values are NO_LIMIT and
            SPECIFY. The default value is NO_LIMIT.
        printTotal
            A Boolean specifying whether to print the total value of either the field output result
            (when **probeObject** = ”ODB”) or the **x**- and **y**-coordinates (when **probeObject** = XYPlot).
            The default value is OFF.
        printMinMax
            A Boolean specifying whether to print the minimum and maximum values of either the field
            output result (when **probeObject** = ”ODB”) or the **x**- and **y**-coordinates (when
            **probeObject** = XYPlot). The default value is OFF.
        """
        ...
