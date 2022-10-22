from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ....UtilityAndView.abaqusConstants import Boolean, OFF, RETENTION_FACTOR, SymbolicConstant


@abaqus_class_doc
class BrittleShear:
    """The BrittleShear object specifies the postcracking shear behavior of a material used in
    a brittle cracking model.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].brittleCracking.brittleShear
            import odbMaterial
            session.odbs[name].materials[name].brittleCracking.brittleShear

        The table data for this object are:

        - If **type** = RETENTION_FACTOR the table data specify the following:
        
            - Shear retention factor.
            - Crack opening strain.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = POWER_LAW the table data specify the following:
        
            - :math:`e`.
            - :math:`p`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - BRITTLE SHEAR
    """

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        type: SymbolicConstant = RETENTION_FACTOR,
    ):
        """This method creates a BrittleShear object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].brittleCracking.BrittleShear
                session.odbs[name].materials[name].brittleCracking.BrittleShear

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        type
            A SymbolicConstant specifying the type of postcracking shear behavior. Possible values
            are RETENTION_FACTOR and POWER_LAW. The default value is RETENTION_FACTOR.

        Returns
        -------
        BrittleShear
            A :py:class:`~abaqus.Material.Plastic.Concrete.BrittleShear.BrittleShear` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the BrittleShear object.

        Raises
        ------
        RangeError
        """
        ...
