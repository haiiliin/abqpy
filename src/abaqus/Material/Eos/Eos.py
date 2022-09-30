from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ...UtilityAndView.abaqusConstants import Boolean, IDEALGAS, OFF, SymbolicConstant


@abaqus_class_doc
class Eos:
    r"""The Eos object specifies an equation of state model.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].eos
            import odbMaterial
            session.odbs[name].materials[name].eos

        The table data for this object are:

        - If **type** = IDEALGAS, the table data represents the following:
        
            - Gas constant, :math:`R`.
            - The ambient pressure, :math:`p_{A}`. If this field is left blank, a default of 0.0 is used.
            
        - If **type** = JWL, the table data represents the following:
        
            - Detonation wave speed, :math:`C_{d}`.
            - :math:`A`.
            - :math:`B`.
            - :math:`\omega`. (Dimensionless.)
            - :math:`R_{1}`. (Dimensionless.)
            - :math:`R_{2}`. (Dimensionless.)
            - Pre-detonation bulk modulus, :math:`K_{p d}`.
            - Detonation energy density, :math:`E_{0}`.
            
        - If **type** = USUP, the table data represents the following:
        
            - :math:`C_{0}`
            - :math:`\boldsymbol{S}`. (Dimensionless.)
            - :math:`\Gamma_{0}`. (Dimensionless.)
            
        - If **type** = TABULAR, the table data represents the following:
        
            - :math:`F_{1}`
            - :math:`F_{2}`
            - :math:`\varepsilon_{v o l}^{c}`. (Dimensionless.)
    """

    @abaqus_method_doc
    def __init__(
        self,
        type: SymbolicConstant = IDEALGAS,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        detonationEnergy: float = 0,
        solidTable: tuple = (),
        gasTable: tuple = (),
        reactionTable: tuple = (),
        gasSpecificTable: tuple = (),
        table: tuple = (),
    ):
        r"""This method creates an Eos object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].Eos
                session.odbs[name].materials[name].Eos

        Parameters
        ----------
        type
            A SymbolicConstant specifying the equation of state. Possible values are USUP, JWL,
            IDEALGAS, TABULAR, and IGNITIONANDGROWTH. The default value is IDEALGAS.
        temperatureDependency
            A Boolean specifying whether the data in **gasSpecificTable** depend on temperature. The
            default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies for the data in
            **gasSpecificTable**. The default value is 0.
        detonationEnergy
            A Float specifying the detonation energy text field. The default value is 0.0.
        solidTable
            A sequence of sequences of Floats specifying the following:
            
            - :math:`A_{s}`.
            - :math:`B_{s}`.
            - :math:`{\omega}_{s}`.
            - :math:`R_{1s}`.
            - :math:`R_{2s}`.
            
            The default value is an empty sequence.
        gasTable
            A sequence of sequences of Floats specifying the following:
            
            - :math:`A_{g}`.
            - :math:`B_{g}`.
            - :math:`{\omega}_{g}`.
            - :math:`R_{1g}`.
            - :math:`R_{2g}`.
            
            The default value is an empty sequence.
        reactionTable
            A sequence of sequences of Floats specifying the following:
            
            - Initial Pressure, :math:`I`.
            - Product co-volume, :math:`a`.
            - Exponent on the unreacted fraction (ignition term), :math:`x`.
            - First burn rate coefficient, :math:`G_{1}`
            - Exponent on the unreacted fraction (growth term), :math:`c`.
            - Exponent on the reacted fraction (growth term), :math:`d`.
            - Pressure exponent (growth term), :math:`y`.
            - Second burn rate coefficient, :math:`G_{2}`.
            - Exponent on the unreacted fraction (completion term), :math:`e`.
            - Exponent on the reacted fraction (completion term), :math:`g`.
            - Pressure exponent (completion term), :math:`z`.
            - Initial reacted fraction, :math:`{F^{max}}_{ig}`.
            - Maximum reacted fraction for the growth term, :math:`{F^{max}}_{G1}`.
            - Minimum reacted fraction, :math:`{F^{min}}_{G2}`.
            
            The default value is an empty sequence.
        gasSpecificTable
            A sequence of sequences of Floats specifying the following:
            
            - Specific Heat per unit mass.
            - Temperature dependent data.
            - Value of first field variable.
            - Value of second field variable.
            - Etc.
            
            The default value is an empty sequence.
        table
            A sequence of sequences of Floats specifying the items described below. The default
            value is an empty sequence.

        Returns
        -------

        Raises
        ------
        """
        ...
