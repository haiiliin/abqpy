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

<<<<<<< HEAD
    #: A Float specifying the emissivity of the master surface.
    masterEmissivity: float

    #: A Float specifying the emissivity of the slave surface.
    slaveEmissivity: float
=======
    #: A Float specifying the emissivity of the main surface.
    #:
    #: .. versionchanged:: 2022
    #:     The attribute ``masterEmissivity`` was renamed to ``mainEmissivity``.
    mainEmissivity: float

    #: A Float specifying the emissivity of the secondary surface.
    #:
    #: .. versionchanged:: 2022
    #:     The attribute ``slaveEmissivity`` was renamed to ``secondaryEmissivity``.
    secondaryEmissivity: float
>>>>>>> 0ca8d932 ([bugfix] Fix backquotes for code and add autoapi class template (#4221))

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
<<<<<<< HEAD
        masterEmissivity
            A Float specifying the emissivity of the master surface.
        slaveEmissivity
            A Float specifying the emissivity of the slave surface.
=======
        mainEmissivity
            A Float specifying the emissivity of the main surface.

            .. versionchanged:: 2022
                The argument ``masterEmissivity`` was renamed to ``mainEmissivity``.
        secondaryEmissivity
            A Float specifying the emissivity of the secondary surface.

            .. versionchanged:: 2022
                The argument ``slaveEmissivity`` was renamed to ``secondaryEmissivity``.
>>>>>>> 0ca8d932 ([bugfix] Fix backquotes for code and add autoapi class template (#4221))
        table
            A sequence of sequences of Floats specifying the following:Effective viewfactor, FF.Gap
            clearance, dd.

        Returns
        -------
        Radiation
            A Radiation object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Radiation object."""
        ...
