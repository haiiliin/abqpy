from typing import Optional

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ...UtilityAndView.abaqusConstants import Boolean, ENERGY, LINEAR, MAXIMUM, MODE_INDEPENDENT, OFF
from ...UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class DamageEvolution:
    """The DamageEvolution object specifies material properties to define the evolution of
    damage.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].ductileDamageInitiation.damageEvolution
            mdb.models[name].materials[name].fldDamageInitiation.damageEvolution
            mdb.models[name].materials[name].flsdDamageInitiation.damageEvolution
            mdb.models[name].materials[name].hashinDamageInitiation.damageEvolution
            mdb.models[name].materials[name].johnsonCookDamageInitiation.damageEvolution
            mdb.models[name].materials[name].maxeDamageInitiation.damageEvolution
            mdb.models[name].materials[name].maxpeDamageInitiation.damageEvolution
            mdb.models[name].materials[name].maxpsDamageInitiation.damageEvolution
            mdb.models[name].materials[name].maxsDamageInitiation.damageEvolution
            mdb.models[name].materials[name].mkDamageInitiation.damageEvolution
            mdb.models[name].materials[name].msfldDamageInitiation.damageEvolution
            mdb.models[name].materials[name].quadeDamageInitiation.damageEvolution
            mdb.models[name].materials[name].quadsDamageInitiation.damageEvolution
            mdb.models[name].materials[name].shearDamageInitiation.damageEvolution
            import odbMaterial
            session.odbs[name].materials[name].ductileDamageInitiation.damageEvolution
            session.odbs[name].materials[name].fldDamageInitiation.damageEvolution
            session.odbs[name].materials[name].flsdDamageInitiation.damageEvolution
            session.odbs[name].materials[name].hashinDamageInitiation.damageEvolution
            session.odbs[name].materials[name].johnsonCookDamageInitiation.damageEvolution
            session.odbs[name].materials[name].maxeDamageInitiation.damageEvolution
            session.odbs[name].materials[name].maxpeDamageInitiation.damageEvolution
            session.odbs[name].materials[name].maxpsDamageInitiation.damageEvolution
            session.odbs[name].materials[name].maxsDamageInitiation.damageEvolution
            session.odbs[name].materials[name].mkDamageInitiation.damageEvolution
            session.odbs[name].materials[name].msfldDamageInitiation.damageEvolution
            session.odbs[name].materials[name].quadeDamageInitiation.damageEvolution
            session.odbs[name].materials[name].quadsDamageInitiation.damageEvolution
            session.odbs[name].materials[name].shearDamageInitiation.damageEvolution

        The table data for this object are:

        - If **type** = DISPLACEMENT, and **softening** = LINEAR, and **mixedModeBehavior** = MODE_INDEPENDENT, the table data specify the following:
        
            - Equivalent total or Plastic displacement at failure, measured from the time of damage initiation.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = ENERGY, and **softening** = LINEAR, and **mixedModeBehavior** = MODE_INDEPENDENT, the table data specify the following:
        
            - Fracture energy.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = DISPLACEMENT, and **softening** = LINEAR, and **mixedModeBehavior** = TABULAR, the table data specify the following:
        
            - Total displacement at failure, measured from the time of damage initiation.
            - Appropriate mode mix ratio.
            - Appropriate mode mix ratio (if relevant, for three-dimensional problems with anisotropic shear behavior).
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = ENERGY, and **softening** = LINEAR, and **mixedModeBehavior** = TABULAR, the table data specify the following:
        
            - Fracture energy.
            - Appropriate mode mix ratio.
            - Appropriate mode mix ratio (if relevant, for three-dimensional problems with anisotropic shear behavior).
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = DISPLACEMENT, and **softening** = EXPONENTIAL, and **mixedModeBehavior** = MODE_INDEPENDENT, the table data specify the following:
        
            - Equivalent total or Plastic displacement at failure, measured from the time of damage initiation.
            - Exponential law parameter.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = ENERGY, and **softening** = EXPONENTIAL, and **mixedModeBehavior** = MODE_INDEPENDENT, the table data specify the following:
        
            - Fracture energy.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = DISPLACEMENT, and **softening** = EXPONENTIAL, and **mixedModeBehavior** = TABULAR, the table data specify the following:
        
            - Total displacement at failure, measured from the time of damage initiation.
            - Exponential law parameter.
            - Appropriate mode mix ratio.
            - Appropriate mode mix ratio (if relevant, for three-dimensional problems with anisotropic shear behavior).
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = ENERGY, and **softening** = EXPONENTIAL, and **mixedModeBehavior** = TABULAR, the table data specify the following:
        
            - Fracture energy.
            - Appropriate mode mix ratio.
            - Appropriate mode mix ratio (if relevant, for three-dimensional problems with anisotropic shear behavior).
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = DISPLACEMENT, and **softening** = TABULAR, and **mixedModeBehavior** = MODE_INDEPENDENT, the table data specify the following:
        
            - Damage variable.
            - Equivalent total or Plastic displacement, measured from the time of damage initiation.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = DISPLACEMENT, and **softening** = TABULAR, and **mixedModeBehavior** = TABULAR, the table data specify the following:
        
            - Damage variable.
            - Equivalent total or Plastic displacement, measured from the time of damage initiation.
            - Appropriate mode mix ratio.
            - Appropriate mode mix ratio (if relevant, for three-dimensional problems with anisotropic shear behavior).
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = ENERGY, and **softening** = LINEAR or EXPONENTIAL, and **mixedModeBehavior** = POWER_LAW or BK, the table data specify the following:
        
            - Normal mode fracture energy.
            - Shear mode fracture energy for failure in the first shear direction.
            - Shear mode fracture energy for failure in the second shear direction.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = ENERGY, **softening** = LINEAR and constructor for :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` = HashinDamageInitiation, the table data specify the following:
        
            - Fiber tensile fracture energy.
            - Fiber compressive fracture energy.
            - Matrix tensile fracture energy.
            - Matrix compressive fracture energy.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - DAMAGE EVOLUTION
    """

    @abaqus_method_doc
    def __init__(
        self,
        type: Literal[C.DISPLACEMENT, C.ENERGY],
        table: tuple,
        degradation: Literal[C.MAXIMUM, C.MULTIPLICATIVE] = MAXIMUM,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        mixedModeBehavior: Literal[
            C.MODE_INDEPENDENT, C.TABULAR, C.POWER_LAW, C.BK
        ] = MODE_INDEPENDENT,
        modeMixRatio: Literal[C.TRACTION, C.ENERGY] = ENERGY,
        power: Optional[float] = None,
        softening: Literal[C.LINEAR, C.EXPONENTIAL, C.TABULAR] = LINEAR,
    ) -> None:
        """This method creates a DamageEvolution object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].ductileDamageInitiation.DamageEvolution
                mdb.models[name].materials[name].fldDamageInitiation.DamageEvolution
                mdb.models[name].materials[name].flsdDamageInitiation.DamageEvolution
                mdb.models[name].materials[name].hashinDamageInitiation.DamageEvolution.DamageEvolutione].materials[name].johnsonCookDamageInitiation.DamageEvolution
                mdb.models[name].materials[name].maxeDamageInitiation.DamageEvolution
                mdb.models[name].materials[name].maxpeDamageInitiation.DamageEvolution
                mdb.models[name].materials[name].maxpsDamageInitiation.DamageEvolution
                mdb.models[name].materials[name].maxsDamageInitiation.DamageEvolution
                mdb.models[name].materials[name].mkDamageInitiation.DamageEvolution
                mdb.models[name].materials[name].msfldDamageInitiation.DamageEvolution
                mdb.models[name].materials[name].quadeDamageInitiation.DamageEvolution
                mdb.models[name].materials[name].quadsDamageInitiation.DamageEvolution
                mdb.models[name].materials[name].shearDamageInitiation.DamageEvolution
                session.odbs[name].materials[name].ductileDamageInitiation.DamageEvolution
                session.odbs[name].materials[name].fldDamageInitiation.DamageEvolution
                session.odbs[name].materials[name].flsdDamageInitiation.DamageEvolution.DamageEvolutioname].materials[name].hashinDamageInitiation.DamageEvolution.DamageEvolutioname].materials[name].johnsonCookDamageInitiation.DamageEvolution.DamageEvolutioname].materials[name].maxeDamageInitiation.DamageEvolution
                session.odbs[name].materials[name].maxpeDamageInitiation.DamageEvolution
                session.odbs[name].materials[name].maxpsDamageInitiation.DamageEvolution
                session.odbs[name].materials[name].maxsDamageInitiation.DamageEvolution
                session.odbs[name].materials[name].mkDamageInitiation.DamageEvolution
                session.odbs[name].materials[name].msfldDamageInitiation.DamageEvolution.DamageEvolutioname].materials[name].quadeDamageInitiation.DamageEvolution.DamageEvolutioname].materials[name].quadsDamageInitiation.DamageEvolution
                session.odbs[name].materials[name].shearDamageInitiation.DamageEvolution
            
        Parameters
        ----------
        type
            A SymbolicConstant specifying the type of damage evolution. Possible values are 
            DISPLACEMENT and ENERGY. 
        table
            A sequence of sequences of Floats specifying the items described below. 
        degradation
            A SymbolicConstant specifying the degradation. Possible values are MAXIMUM and 
            MULTIPLICATIVE. The default value is MAXIMUM. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 
        mixedModeBehavior
            A SymbolicConstant specifying the mixed mode behavior. Possible values are 
            MODE_INDEPENDENT, TABULAR, POWER_LAW, and BK. The default value is MODE_INDEPENDENT. 
        modeMixRatio
            A SymbolicConstant specifying the mode mix ratio. Possible values are ENERGY and 
            TRACTION. The default value is ENERGY. 
        power
            None or a Float specifying the exponent in the power law or the Benzeggagh-Kenane 
            criterion that defines the variation of fracture energy with mode mix for cohesive 
            elements. The default value is None. 
        softening
            A SymbolicConstant specifying the softening. Possible values are LINEAR, EXPONENTIAL, 
            and TABULAR. The default value is LINEAR. 

        Returns
        -------
        DamageEvolution
            A :py:class:`~abaqus.Material.ProgressiveDamageFailure.DamageEvolution.DamageEvolution` object. 

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the DamageEvolution object.

        Raises
        ------
        RangeError
        """
        ...
