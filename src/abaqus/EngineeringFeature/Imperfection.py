from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import OFF, Boolean


@abaqus_class_doc
class Imperfection:
    """The Imperfection object is the abstract base type for FileImperfection, InputImperfection, and
    DataImperfection.

    .. note::
        This object can be accessed by::

            import assembly
            mdb.models[name].rootAssembly.engineeringFeatures.imperfections[name]

    .. versionadded:: 2023
        The ``Imperfection`` class was added.
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A Boolean specifying whether the fastener is suppressed or not. The default value is
    #: OFF.
    suppressed: Boolean = OFF

    @abaqus_method_doc
    def resume(self):
        """This method resumes the imperfection that was previously suppressed."""
        ...

    @abaqus_method_doc
    def suppress(self):
        """This method suppresses the imperfection."""
        ...
