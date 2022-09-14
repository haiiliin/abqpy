from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class SubstructureGenerateFrequency:
    """A :py:class:`~abaqus.StepMiscellaneous.SubstructureGenerateFrequency.SubstructureGenerateFrequency` object is used to define the modes to be used in a modal
    dynamic analysis. These modes are selected from the specified frequency range including
    the frequency boundary.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].frequencyRange[i]
    """

    #: A Float specifying the lower limit of the frequency range, in cycles/time.
    lower: float = None

    #: A Float specifying the upper limit of the frequency range, in cycles/time.
    upper: float = None
