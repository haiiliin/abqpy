from typing import Union

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import Boolean, DEFAULT, OFF, ON, SymbolicConstant


@abaqus_class_doc
class SolverControl:
    """The SolverControl object is used to provide additional optional solver controls.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].solverControl
    """

    @abaqus_method_doc
    def setValues(
        self,
        allowPropagation: Boolean = ON,
        resetDefaultValues: Boolean = OFF,
        relativeTolerance: Union[SymbolicConstant, float] = DEFAULT,
        maxIterations: SymbolicConstant = DEFAULT,
        fillInLevel: SymbolicConstant = DEFAULT,
    ):
        """This method modifies the SolverControl object.

        Parameters
        ----------
        allowPropagation
            A Boolean specifying whether to allow all solver control values to propagate from a
            previous step. Setting this argument to ON automatically sets **resetDefaultValues** to
            OFF. The default value is ON.
        resetDefaultValues
            A Boolean specifying whether to use all default solver control values. Setting this
            argument to ON automatically sets **allowPropagation** to OFF. The default value is OFF.
        relativeTolerance
            The SymbolicConstant DEFAULT or a Float specifying the relative tolerance for
            convergence of the domain decomposition iterative solver. The default value is DEFAULT.
        maxIterations
            The SymbolicConstant DEFAULT or an Int specifying the maximum number of linear solver
            iterations. The default value is DEFAULT.
        fillInLevel
            The SymbolicConstant DEFAULT or an Int specifying the incomplete LU factorization
            fill-in level (for geostatic and soil analysis only). The default value is DEFAULT.

        Raises
        ------
        RangeError
        """
        ...
