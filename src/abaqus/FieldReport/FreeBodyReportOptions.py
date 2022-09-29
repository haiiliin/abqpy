from typing import Optional
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class FreeBodyReportOptions:
    """The FreeBodyReportOptions object stores settings used by the writeFreeBodyReport method
    when you write free body computational results to an ASCII file. The
    FreeBodyReportOptions object has no constructor. Abaqus creates the
    **freeBodyReportOptions** member when you import the Visualization module.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.defaultFreeBodyReportOptions
            session.freeBodyReportOptions
    """

    @abaqus_method_doc
    def setValues(
        self,
        numDigits: int = 3,
        forceThreshold: Optional[float] = None,
        momentThreshold: Optional[float] = None,
        numberFormat: SymbolicConstant = SCIENTIFIC,
        reportFormat: SymbolicConstant = NORMAL_ANNOTATED,
        csysType: SymbolicConstant = GLOBAL,
    ):
        """This method modifies the FreeBodyReportOptions object.

        Parameters
        ----------
        numDigits
            An Int specifying the number of decimal places. The default value is 3.
        forceThreshold
            A Float specifying the threshold value for force. The default value is 10-6.
        momentThreshold
            A Float specifying the threshold value for moment. The default value is 10-6.
        numberFormat
            A SymbolicConstant specifying the number format. Possible values are SCIENTIFIC, FIXED,
            and ENGINEERING. The default value is SCIENTIFIC.
        reportFormat
            A SymbolicConstant specifying the report format. Possible values are NORMAL_ANNOTATED
            and COMMA_SEPARATED_VALUES. The default value is NORMAL_ANNOTATED.
        csysType
            A SymbolicConstant specifying the coordinate system type. Possible values are GLOBAL and
            LOCAL. The default value is GLOBAL.

        Returns
        -------
        FreeBodyReportOptions
            A :py:class:`~abaqus.FieldReport.FreeBodyReportOptions.FreeBodyReportOptions` object.
        """
        ...
