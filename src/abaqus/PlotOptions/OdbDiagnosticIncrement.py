import typing

from .OdbDiagnosticAttempt import OdbDiagnosticAttempt
from ..UtilityAndView.abaqusConstants import *
from .._decorators import abaqus_class_doc


@abaqus_class_doc
class OdbDiagnosticIncrement:
    """The OdbDiagnosticIncrement object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import visualization
            session.odbData[name].diagnosticData.steps[i].increments[i]
    """

    #: A repository of OdbDiagnosticAttempt objects.
    attempts: typing.Dict[str, OdbDiagnosticAttempt] = {}

    #: A float specifying the size of the initial increment. This attribute is read-only.
    initialSize: str = ""

    #: A boolean specifying whether the solution converged for the particular increment. This
    #: attribute is read-only.
    isConverged: Boolean = OFF

    #: An int specifying the number of attempts for the particular increment. This attribute is
    #: read-only.
    numberOfAttempts: str = ""

    #: An int specifying the number of element diagnostics encountered for the particular
    #: increment. This attribute is read-only.
    numberOfElementDiagnostics: str = ""

    #: A float specifying the size of the particular increment. This attribute is read-only.
    size: str = ""

    #: A float specifying the amount of step time completed in the particular increment. This
    #: attribute is read-only.
    stepTimeCompleted: str = ""
