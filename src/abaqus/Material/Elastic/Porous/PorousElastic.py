from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ....UtilityAndView.abaqusConstants import Boolean, OFF, POISSON, SymbolicConstant


@abaqus_class_doc
class PorousElastic:
    r"""The PorousElastic object specifies elastic material properties for porous materials.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].porousElastic
            import odbMaterial
            session.odbs[name].materials[name].porousElastic

        The table data for this object are:

        - If **shear** = :math:`G`, the table data specify the following:
        
            - The logarithmic bulk modulus, :math:`\kappa`. (Dimensionless.)
            - The shear modulus, :math:`G`.
            - The elastic tensile limit, :math:`p_{t}^{e l}`.
              (This value cannot be negative.)
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
            
        - If **shear** = POISSON, the table data specify the following:
        
            - The logarithmic bulk modulus, :math:`\kappa`. (Dimensionless.)
            - The Poisson's ratio, :math:`\nu`.
            - The elastic tensile limit, :math:`p_{t}^{e l}`. (This value cannot be negative.)
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - POROUS ELASTIC
    """

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        shear: SymbolicConstant = POISSON,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a PorousElastic object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].PorousElastic
                session.odbs[name].materials[name].PorousElastic

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        shear
            A SymbolicConstant specifying the shear definition form. Possible values are G and
            POISSON. The default value is POISSON.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        PorousElastic
            A :py:class:`~abaqus.Material.Elastic.Porous.PorousElastic.PorousElastic` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the PorousElastic object.

        Raises
        ------
        RangeError
        """
        ...
