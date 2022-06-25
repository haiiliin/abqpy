from abaqusConstants import *
from .OdbAnalysisError import OdbAnalysisError
from .OdbAnalysisWarning import OdbAnalysisWarning
from .OdbDiagnosticStep import OdbDiagnosticStep
from .OdbJobTime import OdbJobTime
from .OdbNumericalProblemSummary import OdbNumericalProblemSummary


class OdbDiagnosticData:
    """The OdbDiagnosticData object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import visualization
            session.odbData[name].diagnosticData
    """

    #: A repository of OdbAnalysisError objects.
    analysisErrors: dict[str, OdbAnalysisError] = dict[str, OdbAnalysisError]()

    #: A repository of OdbAnalysisWarning objects.
    analysisWarnings: dict[str, OdbAnalysisWarning] = dict[str, OdbAnalysisWarning]()

    #: A repository of OdbDiagnosticStep objects.
    steps: dict[str, OdbDiagnosticStep] = dict[str, OdbDiagnosticStep]()

    #: An :py:class:`~abaqus.PlotOptions.OdbJobTime.OdbJobTime` object.
    jobTime: OdbJobTime = OdbJobTime()

    #: An :py:class:`~abaqus.PlotOptions.OdbNumericalProblemSummary.OdbNumericalProblemSummary` object.
    numericalProblemSummary: OdbNumericalProblemSummary = OdbNumericalProblemSummary()

    #: A boolean specifying whether or not double precision is used for the analysis. This
    #: attribute is read-only.
    isXplDoublePrecision: Boolean = OFF

    #: A String specifying the job status after the analysis. This attribute is read-only.
    jobStatus: str = ""

    #: An int specifying the number of domains. This attribute is read-only.
    numDomains: str = ""

    #: An int specifying the number of analysis errors encountered. This attribute is
    #: read-only.
    numberOfAnalysisErrors: str = ""

    #: An int specifying the number of analysis warnings encountered. This attribute is
    #: read-only.
    numberOfAnalysisWarnings: str = ""

    #: An int specifying the number of steps present in the analysis. This attribute is
    #: read-only.
    numberOfSteps: str = ""
