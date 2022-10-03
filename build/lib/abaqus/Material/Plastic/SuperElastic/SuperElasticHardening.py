from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

@abaqus_class_doc
class SuperElasticHardening:
    """The SuperElasticHardening object specifies the dependence of the yield stress on the
    total strain to define the piecewise linear hardening of a martensite material model.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].superElasticity.SuperElasticHardening
            import odbMaterial
            session.odbs[name].materials[name].superElasticity.SuperElasticHardening

        The table data for this object are:

        - Yield Stress.
        - Total Strain.

        The corresponding analysis keywords are:

        - SUPERELASTIC HARDENING
    """

    @abaqus_method_doc
    def __init__(self, table: tuple):
        """This method creates a SuperElasticHardening object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].superElasticity.SuperElasticHardening
                session.odbs[name].materials[name].superElasticity.SuperElasticHardening

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.

        Returns
        -------
        SuperElasticHardening
            A :py:class:`~abaqus.Material.Plastic.SuperElastic.SuperElasticHardening.SuperElasticHardening` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the SuperElasticHardening object.

        Raises
        ------
        RangeError
        """
        ...
