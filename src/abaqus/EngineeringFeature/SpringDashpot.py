from abaqusConstants import *


class SpringDashpot:
    """The SpringDashpot object is the abstract base type for the SpringDashpotToGround and
    TwoPointSpringDashpot objects.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import part
            mdb.models[name].parts[name].engineeringFeatures.springDashpots[name]
            import assembly
            mdb.models[name].rootAssembly.engineeringFeatures.springDashpots[name]
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A Boolean specifying whether the spring/dashpot is suppressed or not. The default value
    #: is OFF.
    suppressed: Boolean = OFF

    def resume(self):
        """This method resumes the spring/dashpot that was previously suppressed."""
        pass

    def suppress(self):
        """This method suppresses the spring/dashpot."""
        pass
