from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class DetonationPoint:
    """A DetonationPoint object specifies a suboption of the Eos object. The DetonationPoint object defines
    either isotropic linear elastic shear or linear viscous shear behavior for a hydrodynamic material.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].eos.detonationPoint
            import odbMaterial
            session.odbs[name].materials[name].eos.detonationPoint

        The table data for this object are:

        - X value for coordinate of detonation point.
        - Y value for coordinate of detonation point.
        - Z value for coordinate of detonation point.
        - Detonation delay time.

        The corresponding analysis keywords are:

        - DETONATION POINT
    """

    @abaqus_method_doc
    def __init__(self, table: tuple):
        """This method creates a DetonationPoint object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].eos.DetonationPoint
                session.odbs[name].materials[name].eos.DetonationPoint

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.

        Returns
        -------
        DetonationPoint
            A DetonationPoint object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the DetonationPoint object."""
        ...
