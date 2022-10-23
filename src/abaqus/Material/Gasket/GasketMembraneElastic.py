from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ...UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class GasketMembraneElastic:
    r"""The GasketMembraneElastic object defines the elastic parameters for the membrane shear
    behavior of a gasket.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].gasketMembraneElastic
            import odbMaterial
            session.odbs[name].materials[name].gasketMembraneElastic

        The table data for this object are:

        - Young's modulus, :math:`E`.
        - Poisson's ratio, :math:`\nu`.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - GASKET ELASTICITY
    """

    @abaqus_method_doc
    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a GasketMembraneElastic object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].GasketMembraneElastic
                session.odbs[name].materials[name].GasketMembraneElastic

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        GasketMembraneElastic
            A :py:class:`~abaqus.Material.Gasket.GasketMembraneElastic.GasketMembraneElastic` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the GasketMembraneElastic object.

        Raises
        ------
        RangeError
        """
        ...
