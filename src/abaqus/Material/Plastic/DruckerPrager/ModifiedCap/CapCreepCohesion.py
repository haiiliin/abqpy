from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .....UtilityAndView.abaqusConstants import Boolean, OFF, STRAIN, SymbolicConstant, TOTAL


@abaqus_class_doc
class CapCreepCohesion:
    r"""The CapCreepCohesion object specifies a cap creep model and material properties.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].capPlasticity.capCreepCohesion
            import odbMaterial
            session.odbs[name].materials[name].capPlasticity.capCreepCohesion

        The table data for this object are:

        - If **law** = STRAIN or **law** = TIME, the table data specify the following:
        
            - :math:`A`.
            - :math:`n`.
            - :math:`m`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **law** = SINGHM, the table data specify the following:
        
            - :math:`A`.
            - :math:`\alpha`.
            - :math:`m`.
            - :math:`t_{1}`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - CAP CREEP
    """

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        law: SymbolicConstant = STRAIN,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        time: SymbolicConstant = TOTAL,
    ):
        """This method creates a CapCreepCohesion object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].capPlasticity.CapCreepCohesion
                session.odbs[name].materials[name].capPlasticity.CapCreepCohesion

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        law
            A SymbolicConstant specifying the cap creep law. Possible values are STRAIN, TIME,
            SINGHM, USER and POWER_LAW. The default value is STRAIN.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        time
            A SymbolicConstant specifying the time increment for the relevant laws. Possible values
            are CREEP and TOTAL. The default value is TOTAL.

        Returns
        -------
        CapCreepCohesion
            A :py:class:`~abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapCreepCohesion.CapCreepCohesion` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the CapCreepCohesion object."""
        ...
