class Radiation:
    """The Radiation object specifies radiation for a contact interaction property.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import interaction
            mdb.models[name].interactionProperties[name].radiation

        The corresponding analysis keywords are:

        - GAP RADIATION
    """

    #: A Float specifying the emissivity of the main surface.
    mainEmissivity: float

    #: A Float specifying the emissivity of the secondary surface.
    secondaryEmissivity: float

    #: A sequence of sequences of Floats specifying the following:Effective viewfactor, FF.Gap
    #: clearance, dd.
    table: tuple

    def __init__(self, mainEmissivity: float, secondaryEmissivity: float, table: tuple):
        """This method creates a Radiation object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].interactionProperties[name].Radiation

        Parameters
        ----------
        mainEmissivity
            A Float specifying the emissivity of the main surface.
        secondaryEmissivity
            A Float specifying the emissivity of the secondary surface.
        table
            A sequence of sequences of Floats specifying the following:Effective viewfactor, FF.Gap
            clearance, dd.

        Returns
        -------
        Radiation
            A :py:class:`~abaqus.Interaction.Radiation.Radiation` object.
        """
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the Radiation object."""
        pass
