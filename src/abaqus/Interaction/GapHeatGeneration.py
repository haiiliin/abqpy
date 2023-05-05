from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class GapHeatGeneration:
    """The GapHeatGeneration object specifies heat generation for a contact interaction property.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactionProperties[name].heatGeneration

        The corresponding analysis keywords are:

        - GAP HEAT GENERATION
    """

    #: A Float specifying the fraction of dissipated energy caused by friction or electric
    #: currents that is converted to heat. The default value is 1.0.
    conversionFraction: float = 1

    #: A Float specifying the fraction of converted heat distributed to the secondary surface.
    #: The default value is 0.5.
    #:
    #: .. versionchanged:: 2022
    #:     The attribute ``slaveFraction`` was renamed to ``secondaryFraction``.
    secondaryFraction: float = 0

    @abaqus_method_doc
    def __init__(self, conversionFraction: float = 1, secondaryFraction: float = 0):
        """This method creates a GapHeatGeneration object.

        .. note::
            This function can be accessed by::

                mdb.models[name].interactionProperties[name].HeatGeneration

        Parameters
        ----------
        conversionFraction
            A Float specifying the fraction of dissipated energy caused by friction or electric
            currents that is converted to heat. The default value is 1.0.
        secondaryFraction
            A Float specifying the fraction of converted heat distributed to the secondary surface.
            The default value is 0.5.

            .. versionchanged:: 2022
                The argument ``slaveFraction`` was renamed to ``secondaryFraction``.

        Returns
        -------
        GapHeatGeneration
            A GapHeatGeneration object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the GapHeatGeneration object."""
        ...
