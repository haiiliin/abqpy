from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

@abaqus_class_doc
class Gel:
    r"""The Gel object defines a swelling gel.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].gel
            import odbMaterial
            session.odbs[name].materials[name].gel

        The table data for this object are:

        - Radius of gel particles when completely dry, :math:`r_{a}^{\mathrm{dry}}`.
        - Fully swollen radius of gel particles, :math:`r_{a}^{f}`.
        - Number of gel particles per unit volume, :math:`k_{a}`.
        - Relaxation time constant for long-term swelling of gel particles, :math:`\tau_{1}`.

        The corresponding analysis keywords are:

        - GEL
    """

    @abaqus_method_doc
    def __init__(self, table: tuple):
        """This method creates a Gel object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].Gel
                session.odbs[name].materials[name].Gel

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.

        Returns
        -------
        Gel
            A :py:class:`~abaqus.Material.Others.PoreFluidFlow.Gel.Gel` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Gel object."""
        ...
