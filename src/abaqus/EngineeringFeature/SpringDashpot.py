from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import OFF, Boolean


@abaqus_class_doc
class SpringDashpot:
    """The SpringDashpot object is the abstract base type for the SpringDashpotToGround and
    TwoPointSpringDashpot objects.

    .. note::
        This object can be accessed by::

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

    @abaqus_method_doc
    def resume(self):
        """This method resumes the spring/dashpot that was previously suppressed."""
        ...

    @abaqus_method_doc
    def suppress(self):
        """This method suppresses the spring/dashpot."""
        ...
