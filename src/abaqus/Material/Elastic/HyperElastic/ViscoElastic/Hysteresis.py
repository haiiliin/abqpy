from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class Hysteresis:
    """The Hysteresis object specifies the creep part of the material model for the hysteretic
    behavior of elastomers.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].hyperelastic.hysteresis
            import odbMaterial
            session.odbs[name].materials[name].hyperelastic.hysteresis

        The table data for this object are:

        - Stress scaling factor.
        - Creep parameter.
        - Effective stress exponent.
        - Creep strain exponent.

        The corresponding analysis keywords are:

        - HYSTERESIS
    """

    @abaqus_method_doc
    def __init__(self, table: tuple):
        """This method creates a Hysteresis object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].hyperelastic.Hysteresis
                session.odbs[name].materials[name].hyperelastic.Hysteresis

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.

        Returns
        -------
        Hysteresis
            A :py:class:`~abaqus.Material.Elastic.HyperElastic.ViscoElastic.Hysteresis.Hysteresis` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Hysteresis object.

        Raises
        ------
        RangeError
        """
        ...
