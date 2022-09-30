from abqpy.decorators import abaqus_class_doc
from ..UtilityAndView.abaqusConstants import STEP, SymbolicConstant


@abaqus_class_doc
class Amplitude:
    """The Amplitude object is the abstract base type for other Amplitude objects. The
    Amplitude object has no explicit constructor. The methods and members of the Amplitude
    object are common to all objects derived from the Amplitude.

    .. note:: 
        This object can be accessed by::

            import amplitude
            mdb.models[name].amplitudes[name]
            import odbAmplitude
            session.odbs[name].amplitudes[name]
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
    #: and TOTAL. The default value is STEP.
    timeSpan: SymbolicConstant = STEP
