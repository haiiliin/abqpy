from typing import Union

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class Control:
    """The Control object is used to provide additional optional general solution controls.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].control
    """

    @abaqus_method_doc
    def setValues(
        self,
        allowPropagation: Boolean = ON,
        resetDefaultValues: Boolean = OFF,
        discontinuous: Boolean = OFF,
        constraints: Union[SymbolicConstant, float] = DEFAULT,
        lineSearch: Union[SymbolicConstant, float] = DEFAULT,
        timeIncrementation: Union[SymbolicConstant, float] = DEFAULT,
        directCyclic: Union[SymbolicConstant, float] = DEFAULT,
        concentrationField: Union[SymbolicConstant, float] = DEFAULT,
        displacementField: Union[SymbolicConstant, float] = DEFAULT,
        electricalPotentialField: Union[SymbolicConstant, float] = DEFAULT,
        globalField: Union[SymbolicConstant, float] = DEFAULT,
        hydrostaticFluidPressureField: Union[SymbolicConstant, float] = DEFAULT,
        poreFluidPressureField: Union[SymbolicConstant, float] = DEFAULT,
        rotationField: Union[SymbolicConstant, float] = DEFAULT,
        temperatureField: Union[SymbolicConstant, float] = DEFAULT,
        vcctLinearScaling: Union[SymbolicConstant, float] = DEFAULT,
    ):
        """This method modifies the Control object.

        Parameters
        ----------
        allowPropagation
            A Boolean specifying whether to allow all control values to propagate from a previous
            step. Setting this argument to ON automatically sets **resetDefaultValues** to OFF. The
            default value is ON.
        resetDefaultValues
            A Boolean specifying whether to use all default control values. Setting this argument to
            ON automatically sets **allowPropagation** to OFF. The default value is OFF.
        discontinuous
            A Boolean specifying whether to set **timeIncrementation** values that will usually
            improve efficiency for analyses with severely discontinuous behavior. The default value
            is OFF.
        constraints
            The SymbolicConstant DEFAULT or a sequence of Floats specifying tolerances on constraint
            equations. If a specified sequence contains a value of 0, that item in the sequence will
            be set to its system-defined value. The value can also be the SymbolicConstant DEFAULT.
            The default value is DEFAULT.
        lineSearch
            The SymbolicConstant DEFAULT or a sequence of Floats specifying line search control
            parameters. If a specified sequence contains a value of 0, that item in the sequence
            will be set to its system-defined value. The value can also be the SymbolicConstant
            DEFAULT. The default value is DEFAULT.
        timeIncrementation
            The SymbolicConstant DEFAULT or a sequence of Floats specifying time incrementation
            control parameters. If a specified sequence contains a value of 0, that item in the
            sequence will be set to its system-defined value. The value can also be the
            SymbolicConstant DEFAULT. The default value is DEFAULT.
        directCyclic
            The SymbolicConstant DEFAULT or a sequence of Floats specifying direct cyclic control
            parameters. If a specified sequence contains a value of 0, that item in the sequence
            will be set to its system-defined value. The value can also be the SymbolicConstant
            DEFAULT. The default value is DEFAULT.
        concentrationField
            The SymbolicConstant DEFAULT or a sequence of Floats specifying mass concentration field
            equilibrium equation parameters. If a specified sequence contains a value of 0, that
            item in the sequence will be set to its system-defined value. The value can also be the
            SymbolicConstant DEFAULT. The default value is DEFAULT.
        displacementField
            The SymbolicConstant DEFAULT or a sequence of Floats specifying displacement field and
            warping degree of freedom field equilibrium equation parameters. If a specified sequence
            contains a value of 0, that item in the sequence will be set to its system-defined
            value. The value can also be the SymbolicConstant DEFAULT. The default value is DEFAULT.
        electricalPotentialField
            The SymbolicConstant DEFAULT or a sequence of Floats specifying electrical potential
            field equilibrium equation parameters. If a specified sequence contains a value of 0,
            that item in the sequence will be set to its system-defined value. The value can also be
            the SymbolicConstant DEFAULT. The default value is DEFAULT.
        globalField
            The SymbolicConstant DEFAULT or a sequence of Floats specifying parameters for all
            applicable field equilibrium equations. This argument overwrites all other field
            equilibrium equation control values. If a specified sequence contains a value of 0, that
            item in the sequence will be set to its system-defined value. The value can also be the
            SymbolicConstant DEFAULT. The default value is DEFAULT.
        hydrostaticFluidPressureField
            The SymbolicConstant DEFAULT or a sequence of Floats specifying hydrostatic fluid
            element volume constraint parameters. If a specified sequence contains a value of 0,
            that item in the sequence will be set to its system-defined value. The value can also be
            the SymbolicConstant DEFAULT. The default value is DEFAULT.
        poreFluidPressureField
            The SymbolicConstant DEFAULT or a sequence of Floats specifying pore liquid volumetric
            continuity equilibrium equation parameters. If a specified sequence contains a value of
            0, that item in the sequence will be set to its system-defined value. The value can also
            be the SymbolicConstant DEFAULT. The default value is DEFAULT.
        rotationField
            The SymbolicConstant DEFAULT or a sequence of Floats specifying rotation field
            equilibrium equation parameters. If a specified sequence contains a value of 0, that
            item in the sequence will be set to its system-defined value. The value can also be the
            SymbolicConstant DEFAULT. The default value is DEFAULT.
        temperatureField
            The SymbolicConstant DEFAULT or a sequence of Floats specifying temperature field
            equilibrium equation parameters. If a specified sequence contains a value of 0, that
            item in the sequence will be set to its system-defined value. The value can also be the
            SymbolicConstant DEFAULT. The default value is DEFAULT.
        vcctLinearScaling
            The SymbolicConstant DEFAULT or a Float specifying linear scaling parameter for a VCCT
            debonding analysis. If a specified value is 0, it will be set to its system-defined
            value. The value can also be the SymbolicConstant DEFAULT. The default value is DEFAULT.

        Raises
        ------
        RangeError
        """
        ...
