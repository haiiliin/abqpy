from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

@abaqus_class_doc
class Radiation:
    """The Radiation object specifies radiation for a contact interaction property.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactionProperties[name].radiation

        The corresponding analysis keywords are:

        - GAP RADIATION
    """

    #: A Float specifying the emissivity of the master surface.
    masterEmissivity: float

    #: A Float specifying the emissivity of the slave surface.
    slaveEmissivity: float

    #: A sequence of sequences of Floats specifying the following:Effective viewfactor, FF.Gap
    #: clearance, dd.
    table: tuple

    @abaqus_method_doc
    def __init__(self, masterEmissivity: float, slaveEmissivity: float, table: tuple):
        """This method creates a Radiation object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].interactionProperties[name].Radiation

        Parameters
        ----------
        masterEmissivity
            A Float specifying the emissivity of the master surface.
        slaveEmissivity
            A Float specifying the emissivity of the slave surface.
        table
            A sequence of sequences of Floats specifying the following:Effective viewfactor, FF.Gap
            clearance, dd.

        Returns
        -------
        Radiation
            A :py:class:`~abaqus.Interaction.Radiation.Radiation` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Radiation object."""
        ...
