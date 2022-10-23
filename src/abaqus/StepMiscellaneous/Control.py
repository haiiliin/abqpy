from typing_extensions import Literal
from typing import Union

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import Boolean, DEFAULT, OFF, ON


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
        constraints: Union[Literal[C.DEFAULT], float] = DEFAULT,
        lineSearch: Union[Literal[C.DEFAULT], float] = DEFAULT,
        timeIncrementation: Union[Literal[C.DEFAULT], float] = DEFAULT,
        directCyclic: Union[Literal[C.DEFAULT], float] = DEFAULT,
        concentrationField: Union[Literal[C.DEFAULT], float] = DEFAULT,
        displacementField: Union[Literal[C.DEFAULT], float] = DEFAULT,
        electricalPotentialField: Union[Literal[C.DEFAULT], float] = DEFAULT,
        globalField: Union[Literal[C.DEFAULT], float] = DEFAULT,
        hydrostaticFluidPressureField: Union[Literal[C.DEFAULT], float] = DEFAULT,
        poreFluidPressureField: Union[Literal[C.DEFAULT], float] = DEFAULT,
        rotationField: Union[Literal[C.DEFAULT], float] = DEFAULT,
        temperatureField: Union[Literal[C.DEFAULT], float] = DEFAULT,
        vcctLinearScaling: Union[Literal[C.DEFAULT, C.VCCT], float] = DEFAULT,
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
