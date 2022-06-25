from abaqusConstants import *


class Fastener:
    """The Fastener object is the abstract base type for PointFastener, DiscreteFastener, and
    AssembledFastener.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import part
            mdb.models[name].parts[name].engineeringFeatures.fasteners[name]
            import assembly
            mdb.models[name].rootAssembly.engineeringFeatures.fasteners[name]
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A Boolean specifying whether the fastener is suppressed or not. The default value is
    #: OFF.
    suppressed: Boolean = OFF

    def resume(self):
        """This method resumes the fastener that was previously suppressed."""
        pass

    def suppress(self):
        """This method suppresses the fastener."""
        pass
