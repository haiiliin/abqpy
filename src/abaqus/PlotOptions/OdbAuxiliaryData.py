from ..UtilityAndView.abaqusConstants import *
from .._decorators import abaqus_class_doc


@abaqus_class_doc
class OdbAuxiliaryData:
    """The OdbAuxiliaryData object stores auxiliary data related to the steps in the analysis.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import visualization
            session.odbData[name].diagnosticData.analysisErrors[i].data[i]
            session.odbData[name].diagnosticData.analysisWarnings[i].data[i]
            session.odbData[name].diagnosticData.steps[i].contactDiagnostics[i].data[i]
    """

    #: A tuple consisting of element instance names. This attribute is read-only.
    elementInstanceNames: tuple = ()

    #: A tuple consisting of element label names. This attribute is read-only.
    elementLabels: tuple = ()

    #: A boolean specifying whether the OdbAuxiliaryData object has values in it. This
    #: attribute is read-only.
    hasValues: Boolean = OFF

    #: A tuple consisting of node instance names. This attribute is read-only.
    nodeInstanceNames: tuple = ()

    #: A tuple consisting of node label names. This attribute is read-only.
    nodeLables: tuple = ()
