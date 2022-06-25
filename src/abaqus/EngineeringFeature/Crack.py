from abaqusConstants import *


class Crack:
    """The Crack object is the abstract base type for ContourIntegral and future crack objects.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import part
            mdb.models[name].parts[name].engineeringFeatures.cracks[name]
            import assembly
            mdb.models[name].rootAssembly.engineeringFeatures.cracks[name]
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A Boolean specifying whether the crack is suppressed or not. The default value is OFF.
    suppressed: Boolean = OFF

    def resume(self):
        """This method resumes the crack that was previously suppressed."""
        pass

    def suppress(self):
        """This method suppresses the crack."""
        pass
