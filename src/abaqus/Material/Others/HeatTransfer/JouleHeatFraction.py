from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class JouleHeatFraction:
    """The JouleHeatFraction object defines the fraction of electric energy released as heat.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].jouleHeatFraction
            import odbMaterial
            session.odbs[name].materials[name].jouleHeatFraction

        The corresponding analysis keywords are:

        - JOULE HEAT FRACTION
    """

    @abaqus_method_doc
    def __init__(self, fraction: float = 1):
        """This method creates a JouleHeatFraction object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].JouleHeatFraction
                session.odbs[name].materials[name].JouleHeatFraction

        Parameters
        ----------
        fraction
            A Float specifying the fraction of electrical energy released as heat, including any
            unit conversion factor. The default value is 1.0.

        Returns
        -------
        JouleHeatFraction
            A :py:class:`~abaqus.Material.Others.HeatTransfer.JouleHeatFraction.JouleHeatFraction` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the JouleHeatFraction object.

        Raises
        ------
        RangeError
        """
        ...
