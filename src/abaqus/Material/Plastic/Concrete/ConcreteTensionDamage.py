from abaqusConstants import *


class ConcreteTensionDamage:
    """The ConcreteTensionDamage object specifies hardening for the concrete damaged plasticity
    model.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].concreteDamagedPlasticity.concreteTensionDamage
        import odbMaterial
        session.odbs[name].materials[name].concreteDamagedPlasticity.concreteTensionDamage

    The table data for this object are:

    - If **type**=STRAIN, the table data specify the following:
    
        - Tensile damage variable, dt.
        - Direct cracking strain, ϵtc⁢k.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    - If **type**=DISPLACEMENT, the table data specify the following:
    
        - Tensile damage variable, dt.
        - Direct cracking displacement, utc⁢k.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    The corresponding analysis keywords are:

    - CONCRETE TENSION DAMAGE
    """

    def __init__(
        self,
        table: tuple,
        compressionRecovery: float = 1,
        type: SymbolicConstant = STRAIN,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a ConcreteTensionDamage object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].materials[name].concreteDamagedPlasticity\
            - .ConcreteTensionDamage
                session.odbs[name].materials[name].concreteDamagedPlasticity\
            - .ConcreteTensionDamage
        
        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        compressionRecovery
            A Float specifying the value of the stiffness recovery factor, wcwc, that determines the 
            amount of compression stiffness that is recovered as loading changes from tension to 
            compression. The default value is 1.0. 
        type
            A SymbolicConstant specifying the type of tensile damage data. Set **type**=STRAIN to 
            specify the tensile damage variable as a function of cracking strain. Set 
            **type**=DISPLACEMENT to specify the tensile damage variable as a function of cracking 
            displacement. Possible values are STRAIN and DISPLACEMENT. The default value is STRAIN. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A ConcreteTensionDamage object. 

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self):
        """This method modifies the ConcreteTensionDamage object.

        Raises
        ------
        RangeError
        """
        pass
