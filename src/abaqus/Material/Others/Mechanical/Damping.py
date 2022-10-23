from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class Damping:
    """The Damping object specifies material damping.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].damping
            import odbMaterial
            session.odbs[name].materials[name].damping

        The corresponding analysis keywords are:

        - DAMPING
    """

    @abaqus_method_doc
    def __init__(
        self,
        alpha: float = 0,
        beta: float = 0,
        composite: float = 0,
        structural: float = 0,
    ):
        """This method creates a Damping object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].Damping
                session.odbs[name].materials[name].Damping

        Parameters
        ----------
        alpha
            A Float specifying the αRαR factor to create mass proportional damping in
            direct-integration and explicit dynamics. The default value is 0.0.
        beta
            A Float specifying the βRβR factor to create stiffness proportional damping in
            direct-integration and explicit dynamics. The default value is 0.0.
        composite
            A Float specifying the fraction of critical damping to be used with this material in
            calculating composite damping factors for the modes (for use in modal dynamics). The
            default value is 0.0.This argument applies only to Abaqus/Standard analyses.
        structural
            A Float specifying the structural factor to create material damping in
            direct-integration and explicit dynamics. The default value is 0.0.

        Returns
        -------
        Damping
            A :py:class:`~abaqus.Material.Others.Mechanical.Damping.Damping` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Damping object.

        Raises
        ------
        RangeError
        """
        ...
