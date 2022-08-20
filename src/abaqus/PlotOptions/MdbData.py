import typing

from .MdbDataInstance import MdbDataInstance
from .MdbDataStep import MdbDataStep
from .._decorators import abaqus_class_doc


@abaqus_class_doc
class MdbData:
    """The MdbData object has no constructor. Abaqus creates an MdbData object when a cae file
    is opened or a new model is created. There is one MdbData for each model in session.
    MdbData is updated when it is displayed in a viewport.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import visualization
            session.mdbData[name]
    """

    #: A tuple of (String, Float) tuples specifying the stepName and the stepPeriod.
    stepPeriods: float = None

    #: A repository of MdbDataStep objects specifying the list of steps. The repository is
    #: read-only.
    steps: typing.Dict[str, MdbDataStep] = {}

    #: A repository of MdbDataInstance objects specifying the list of instances. The repository
    #: is read-only.
    instances: typing.Dict[str, MdbDataInstance] = {}
