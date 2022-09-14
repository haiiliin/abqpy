from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class OdbAnalysisWarning:
    """The OdbAnalysisWarning object stores the description of different warnings encountered
    during the analysis.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.odbData[name].diagnosticData.analysisWarnings[i]
    """

    ...
