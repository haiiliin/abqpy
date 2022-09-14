from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

@abaqus_class_doc
class SaturationDependence:
    r"""The SaturationDependence object specifies the dependence of the permeability of a
    material on the saturation of the wetting liquid.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].permeability.saturationDependence
            import odbMaterial
            session.odbs[name].materials[name].permeability.saturationDependence

        The table data for this object are:

        - :math:`k_{s}`. (Dimensionless.)
        - Saturation, :math:`\boldsymbol{S}`. (Dimensionless.)

        The corresponding analysis keywords are:

        - PERMEABILITY
    """

    @abaqus_method_doc
    def __init__(self, table: tuple):
        """This method creates a SaturationDependence object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].permeability.SaturationDependence
                session.odbs[name].materials[name].permeability.SaturationDependence

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.

        Returns
        -------
        SaturationDependence
            A :py:class:`~abaqus.Material.Others.PoreFluidFlow.Permeability.SaturationDependence.SaturationDependence` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the SaturationDependence object.

        Raises
        ------
        RangeError
        """
        ...
