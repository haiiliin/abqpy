from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ....UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class MohrCoulombHardening:
    """The MohrCoulombHardening object specifies hardening for the Mohr-Coulomb plasticity
    model.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].mohrCoulombPlasticity.mohrCoulombHardening
            import odbMaterial
            session.odbs[name].materials[name].mohrCoulombPlasticity.mohrCoulombHardening

        The table data for this object are:

        - Cohesion yield stress.
        - The absolute value of the corresponding Plastic strain.(The first tabular value entered must always be zero.)
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - MOHR COULOMB HARDENING
    """

    @abaqus_method_doc
    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a MohrCoulombHardening object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].mohrCoulombPlasticity.MohrCoulombHardening.MohrCoulombHardeningmaterials[name].mohrCoulombPlasticity.MohrCoulombHardening

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
        MohrCoulombHardening
            A :py:class:`~abaqus.Material.Plastic.MohrCoulomb.MohrCoulombHardening.MohrCoulombHardening` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the MohrCoulombHardening object.

        Raises
        ------
        RangeError
        """
        ...
