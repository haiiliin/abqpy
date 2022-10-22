from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .....UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class CyclicHardening:
    r"""The CyclicHardening object defines the evolution of the elastic domain for the nonlinear
    isotropic/kinematic hardening model.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].Plastic.cyclicHardening
            import odbMaterial
            session.odbs[name].materials[name].Plastic.cyclicHardening

        The table data for this object are:

        - Equivalent stress.
        - :math:`Q_{\infty}` (only if **parameters** = ON).
        - Hardening parameter (only if **parameters** = ON).
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - CYCLIC HARDENING
    """

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        parameters: Boolean = OFF,
    ):
        """This method creates a CyclicHardening object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].Plastic.CyclicHardening
                session.odbs[name].materials[name].Plastic.CyclicHardening

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        parameters
            A Boolean specifying whether material parameters are to be input directly. The default
            value is OFF.

        Returns
        -------
        CyclicHardening
            A :py:class:`~abaqus.Material.Plastic.Metal.Cyclic.CyclicHardening.CyclicHardening` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the CyclicHardening object."""
        ...
