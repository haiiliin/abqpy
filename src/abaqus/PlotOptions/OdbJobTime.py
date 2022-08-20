from .._decorators import abaqus_class_doc


@abaqus_class_doc
class OdbJobTime:
    """The OdbJobTime object stores the analysis time of a job.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import visualization
            session.odbData[name].diagnosticData.jobTime
    """

    #: A float specifying the systemtime for the analysis. This attribute is read-only.
    systemTime: str = ""

    #: A float specifying the usertime for the analysis. This attribute is read-only.
    userTime: str = ""

    #: A float specifying the wallclocktime for the analysis. This attribute is read-only.
    wallclockTime: str = ""
