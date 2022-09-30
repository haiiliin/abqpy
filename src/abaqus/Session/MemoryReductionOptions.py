from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import Boolean, ON


@abaqus_class_doc
class MemoryReductionOptions:
    """The MemoryReductionOptions object controls the default settings that Abaqus/CAE uses for
    running in reduced memory mode. The MemoryReductionOptions object has no constructor.
    Abaqus creates the **MemoryReductionOptions** member when a session is started.

    .. note:: 
        This object can be accessed by::

            session.memoryReductionOptions
    """

    @abaqus_method_doc
    def setValues(self, reducedMemoryMode: Boolean = ON, percentThreshold: float = 75):
        """This method modifies the MemoryReductionOptions object.

        Parameters
        ----------
        reducedMemoryMode
            A Boolean specifying whether Abaqus/CAE should run in reduced memory mode. The default
            value is ON.
        percentThreshold
            A Float specifying the percent of **kernelMemoryLimit** at which the reduced memory mode
            starts. The default value is 75.0.
        """
        ...
