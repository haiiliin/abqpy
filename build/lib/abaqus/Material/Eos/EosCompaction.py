from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

@abaqus_class_doc
class EosCompaction:
    """The EosCompaction object specifies material eos compaction.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].eos.eosCompaction
            import odbMaterial
            session.odbs[name].materials[name].eos.eosCompaction

        The corresponding analysis keywords are:

        - EOS COMPACTION
    """

    @abaqus_method_doc
    def __init__(
        self,
        soundSpeed: float,
        porosity: float,
        pressure: float,
        compactionPressure: float,
    ):
        """This method creates an EosCompaction object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].eos.EosCompaction
                session.odbs[name].materials[name].eos.EosCompaction

        Parameters
        ----------
        soundSpeed
            A Float specifying reference sound speed in the porous material.
        porosity
            A Float specifying value of the porosity of the unloaded material.
        pressure
            A Float specifying pressure required to initialize Plastic behavior.
        compactionPressure
            A Float specifying compaction pressure at which all pores are crushed.

        Returns
        -------
        EosCompaction
            An :py:class:`~abaqus.Material.Eos.EosCompaction.EosCompaction` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the EosCompaction object.

        Raises
        ------
        RangeError
        """
        ...
