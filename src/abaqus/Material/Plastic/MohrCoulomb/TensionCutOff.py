from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ....UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class TensionCutOff:
    """The TensionCutOff object specifies tension cutoff for different material models for
    example the Mohr-Coulomb plasticity model.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].mohrCoulombPlasticity.tensionCutOff
            import odbMaterial
            session.odbs[name].materials[name].mohrCoulombPlasticity.tensionCutOff

        The table data for this object are:

        - Tension cutoff stress.
        - The value of the corresponding tensile Plastic strain.(The first tabular value
          entered must always be zero.)
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - TENSION CUTOFF
    """

    @abaqus_method_doc
    def __init__(
        self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0
    ):
        """This method creates a TensionCutOff object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].mohrCoulombPlasticity.TensionCutOff
                session.odbs[name].materials[name].mohrCoulombPlasticity.TensionCutOff

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
        TensionCutOff
            A :py:class:`~abaqus.Material.Plastic.MohrCoulomb.TensionCutOff.TensionCutOff` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the TensionCutOff object.

        Raises
        ------
        RangeError
        """
        ...
