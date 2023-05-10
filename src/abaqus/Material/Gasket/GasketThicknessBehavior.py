from typing import Optional

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ...UtilityAndView.abaqusConstants import (
    ELASTIC_PLASTIC,
    OFF,
    RELATIVE_SLOPE_DROP,
    STRESS,
    Boolean,
)
from ...UtilityAndView.abaqusConstants import abaqusConstants as C
from .ContactArea import ContactArea


@abaqus_class_doc
class GasketThicknessBehavior:
    """The GasketThicknessBehavior object defines the behavior in the thickness direction for a gasket.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].gasketThicknessBehavior
            import odbMaterial
            session.odbs[name].materials[name].gasketThicknessBehavior

        The table data for this object are:

        - If **variableUnits** = STRESS, the loading table data specify the following:

            - Pressure; this value must be positive.
            - Closure; this value must be positive.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **variableUnits** = FORCE, the loading table data specify the following:

            - Force or force per unit length; this value must be positive.
            - Closure; this value must be positive.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **variableUnits** = STRESS and **type** = ELASTIC_PLASTIC, the **unloadingTable** data specify the following:

            - Pressure; this value must be positive.
            - Closure; this value must be positive.
            - Plastic closure; this value must be positive.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **variableUnits** = FORCE and **type** = ELASTIC_PLASTIC, the **unloadingTable** data specify the following:

            - Pressure; this value must be positive.
            - Closure; this value must be positive.
            - Plastic closure; this value must be positive.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **variableUnits** = STRESS and **type** = DAMAGE, the **unloadingTable** data specify the following:

            - Pressure; this value must be positive.
            - Closure; this value must be positive.
            - Maximum closure reached while loading the gasket; this value must be positive.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **variableUnits** = FORCE and **type** = DAMAGE, the **unloadingTable** data specify the following:

            - Force or force per unit length; this value must be positive.
            - Closure; this value must be positive.
            - Maximum closure reached while loading the gasket; this value must be positive.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - GASKET THICKNESS BEHAVIOR
    """

    #: A ContactArea object.
    contactArea: ContactArea = ContactArea(((),))

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        tensileStiffnessFactor: Optional[float] = None,
        type: Literal[C.DAMAGE, C.ELASTIC_PLASTIC] = ELASTIC_PLASTIC,
        unloadingDependencies: int = 0,
        unloadingTemperatureDependency: Boolean = OFF,
        variableUnits: Literal[C.STRESS, C.FORCE] = STRESS,
        yieldOnset: float = 0,
        yieldOnsetMethod: Literal[C.RELATIVE_SLOPE_DROP, C.CLOSURE_VALUE] = RELATIVE_SLOPE_DROP,
        unloadingTable: tuple = (),
    ):
        """This method creates a GasketThicknessBehavior object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].GasketThicknessBehavior
                session.odbs[name].materials[name].GasketThicknessBehavior

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying loading data. The first sequence must
            contain only 0. At least two sequences must be specified if **type** = DAMAGE, and at least
            3 sequences must be specified if **type** = ELASTIC_PLASTIC. The items in the table data are
            described below.
        temperatureDependency
            A Boolean specifying whether the loading data depend on temperature. The default value
            is OFF.
        dependencies
            An Int specifying the number of field variable dependencies included in the definition
            of the loading data, in addition to temperature. The default value is 0.
        tensileStiffnessFactor
            A Float specifying the fraction of the initial compressive stiffness that defines the
            stiffness in tension. The default value is 10⁻³.
        type
            A SymbolicConstant specifying a damage elasticity model or an elastic-Plastic model for
            gasket thickness-direction behavior. Possible values are ELASTIC_PLASTIC and DAMAGE. The
            default value is ELASTIC_PLASTIC.
        unloadingDependencies
            An Int specifying the number of field variable dependencies included in the definition
            of the unloading data, in addition to temperature. The default value is 0.
        unloadingTemperatureDependency
            A Boolean specifying whether unloading data depends on temperature. The default value is
            OFF.
        variableUnits
            A SymbolicConstant specifying the behavior in terms of units of force (or force in unit
            length) versus closure or pressure versus closure. Possible values are STRESS and FORCE.
            The default value is STRESS.
        yieldOnset
            A Float specifying the closure value at which the onset of yield occurs or the relative
            drop in slope on the loading curve that defines the onset of Plastic deformation
            (depending on the value of **yieldOnsetMethod**). The default value is 0.1.
        yieldOnsetMethod
            A SymbolicConstant specifying the method used to determine yield onset. Possible values
            are RELATIVE_SLOPE_DROP and CLOSURE_VALUE. The default value is RELATIVE_SLOPE_DROP.
        unloadingTable
            A sequence of sequences of Floats specifying unloading data. The items in the table data
            are described below. The default value is an empty sequence.

        Returns
        -------
        GasketThicknessBehavior
            A GasketThicknessBehavior object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the GasketThicknessBehavior object.

        Raises
        ------
        RangeError
        """
        ...
