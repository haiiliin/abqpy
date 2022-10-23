from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class VelocityDependence:
    r"""The VelocityDependence object specifies the dependence of the permeability of a material
    on the velocity of fluid flow.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].permeability.velocityDependence
            import odbMaterial
            session.odbs[name].materials[name].permeability.velocityDependence

        The table data for this object are:

        - :math:`\beta`. Only :math:`\beta>0.0` is allowed.
        - Void ratio, :math:`e`.

        The corresponding analysis keywords are:

        - PERMEABILITY
    """

    @abaqus_method_doc
    def __init__(self, table: tuple):
        """This method creates a VelocityDependence object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].permeability.VelocityDependence
                session.odbs[name].materials[name].permeability.VelocityDependence

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.

        Returns
        -------
        VelocityDependence
            A :py:class:`~abaqus.Material.Others.PoreFluidFlow.Permeability.VelocityDependence.VelocityDependence` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the VelocityDependence object.

        Raises
        ------
        RangeError
        """
        ...
