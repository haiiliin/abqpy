from abqpy.decorators import abaqus_class_doc

from .OdbAuxiliaryData import OdbAuxiliaryData


@abaqus_class_doc
class OdbAnalysisError:
    """The OdbAnalysisError object stores the description of different errors encountered
    during the analysis.

    .. note::
        This object can be accessed by::

            import visualization
            session.odbData[name].diagnosticData.analysisErrors[i]
    """

    #: An int specifying the increment number where the analysis was aborted. This attribute is
    #: read-only.
    incrementNumber: str = ""

    #: An int specifying the iteration number where the analysis was aborted. This attribute is
    #: read-only.
    iterationNumber: str = ""

    #: An int specifying the attempt number on which the analysis was aborted. This attribute
    #: is read-only.
    attemptNumber: str = ""

    #: String specifying the category of error. This attribute is read-only.
    category: str = ""

    #: An :py:class:`~abaqus.PlotOptions.OdbAuxiliaryData.OdbAuxiliaryData` object.
    data: OdbAuxiliaryData = OdbAuxiliaryData()

    #: String specifying the cause of the error. This attribute is read-only.
    description: str = ""

    #: String specifying the exact nature of the problem. This attribute is read-only.
    detailStrings: str = ""

    #: String specifying the exact reason for the error encountered. This attribute is
    #: read-only.
    knowledgeItem: str = ""

    #: An int specifying the number of variations. This attribute is read-only.
    numberOfVariations: str = ""

    #: An int specifying the step number on which the error was encountered. This attribute is
    #: read-only.
    stepNumber: str = ""
