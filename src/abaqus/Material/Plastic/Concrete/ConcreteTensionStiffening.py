from abaqusConstants import *


class ConcreteTensionStiffening:
    """The ConcreteTensionStiffening object specifies hardening for the concrete damaged
    plasticity model.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].concreteDamagedPlasticity.concreteTensionStiffening
        import odbMaterial
        session.odbs[name].materials[name].concreteDamagedPlasticity.concreteTensionStiffening

    The table data for this object are:

    - If **type**=STRAIN, the table data specify the following:
        - Remaining direct stress after cracking, σt.
        - Direct cracking strain, ϵckt.
        - Direct cracking strain rate, ˙ϵckt.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    - If **type**=DISPLACEMENT, the table data specify the following:
        - Remaining direct stress after cracking, σt.
        - Direct cracking displacement, uckt.
        - Direct cracking displacement rate, ˙uckt
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    - If **type**=GFI, the table data specify the following:
        - Failure stress, σt0σt⁢0.
        - Fracture energy, Gf.
        - Direct cracking displacement rate, ˙uckt.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    The corresponding analysis keywords are:

    - CONCRETE TENSION STIFFENING
    """

    def __init__(
        self,
        table: tuple,
        rate: Boolean = OFF,
        type: SymbolicConstant = STRAIN,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a ConcreteTensionStiffening object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].materials[name].concreteDamagedPlasticity\
            - .ConcreteTensionStiffening
                session.odbs[name].materials[name].concreteDamagedPlasticity\
            - .ConcreteTensionStiffening
        
        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        rate
            A Boolean specifying whether the data depend on rate. The default value is OFF. 
        type
            A SymbolicConstant specifying the type of postcracking behavior data. Possible values 
            are: 
            - STRAIN, specifying postfailure stress as a function of cracking strain. 
            - DISPLACEMENT, specifying postfailure stress as a function of cracking displacement. 
            - GFI, specifying failure stress as a function of the fracture energy. 
            The default value is STRAIN. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A ConcreteTensionStiffening object. 

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self):
        """This method modifies the ConcreteTensionStiffening object.

        Raises
        ------
        RangeError
        """
        pass
