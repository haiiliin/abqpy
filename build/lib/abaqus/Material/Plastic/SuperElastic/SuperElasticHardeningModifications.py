from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

@abaqus_class_doc
class SuperElasticHardeningModifications:
    """The SuperElasticHardeningModifications object specifies the variation of the
    transformation stress levels of a material model.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].superElasticity.SuperElasticHardening
            import odbMaterial
            session.odbs[name].materials[name].superElasticity.SuperElasticHardening

        The table data for this object are:

        - Start of Transformation (Loading).
        - End of Transformation (Loading).
        - Start of Transformation (Unloading).
        - End of Transformation (Unloading).
        - Plastic Strain.

        The corresponding analysis keywords are:

        - SUPERELASTIC HARDENING MODIFICATIONS
    """

    @abaqus_method_doc
    def __init__(self, table: tuple):
        """This method creates a SuperElasticHardeningModifications object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].superElasticity.SuperElasticHardeningModifications
                session.odbs[name].materials[name].superElasticity.SuperElasticHardeningModifications

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below or user-defined
            data if the dependence of the transformation stress levels on Plastic strain is
            specified in a user subroutine.

        Returns
        -------
        SuperElasticHardeningModifications
            A :py:class:`~abaqus.Material.Plastic.SuperElastic.SuperElasticHardeningModifications.SuperElasticHardeningModifications` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the SuperElasticHardeningModifications object.

        Raises
        ------
        RangeError
        """
        ...
