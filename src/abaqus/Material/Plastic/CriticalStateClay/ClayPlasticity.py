from abaqusConstants import *
from .ClayHardening import ClayHardening


class ClayPlasticity:
    """The ClayPlasticity object specifies the extended Cam-clay plasticity model.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].clayPlasticity
        import odbMaterial
        session.odbs[name].materials[name].clayPlasticity

    The table data for this object are:

    - If **hardening**=EXPONENTIAL, the table data specify the following:
    
        - Logarithmic Plastic bulk modulus, λ (dimensionless).
        - Stress ratio at critical state, M.
        - The initial yield surface size, a0.
        - ββ, the parameter defining the size of the yield surface on the “wet” side of critical state.
        - KK, the ratio of the flow stress in triaxial tension to the flow stress in triaxial compression. 0.778≤K≤1.0. If the default value of 0.0 is accepted, a value of 1.0 is assumed.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    - If **hardening**=TABULAR, the table data specify the following:
    
        - Stress ratio at critical state, M.
        - The initial volumetric Plastic strain, ε_vol^pl∣0, corresponding to pc|0according to the [ClayHardening](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-clayhardeningpyc.htm?ContextScope=all) definition.
        - ββ, the parameter defining the size of the yield surface on the “wet” side of critical state.
        - KK, the ratio of the flow stress in triaxial tension to the flow stress in triaxial compression. 0.778≤K≤1.0.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    The corresponding analysis keywords are:

    - CLAY PLASTICITY
    """

    # A ClayHardening object.
    clayHardening: ClayHardening = ClayHardening(((),))

    def __init__(
        self,
        table: tuple,
        intercept: float = None,
        hardening: SymbolicConstant = EXPONENTIAL,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a ClayPlasticity object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].materials[name].ClayPlasticity
            session.odbs[name].materials[name].ClayPlasticity

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        intercept
            None or a Float specifying e1e1, the intercept of the virgin consolidation line with the
            void ratio axis in a plot of void ratio versus the logarithm of pressure stress. The
            default value is None.This argument is valid only if **hardening**=EXPONENTIAL.
        hardening
            A SymbolicConstant specifying the type of hardening/softening definition. Possible
            values are EXPONENTIAL and TABULAR. The default value is EXPONENTIAL.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
            A ClayPlasticity object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self):
        """This method modifies the ClayPlasticity object.

        Raises
        ------
        RangeError
        """
        pass
