from abaqusConstants import *
from .Interaction import Interaction
from ..Region.Region import Region


class StdXplCosimulation(Interaction):
    """The StdXplCosimulation object defines co-simulation behavior between Abaqus/Standard and
    Abaqus/Explicit.
    The StdXplCosimulation object is derived from the Interaction object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].interactions[name]
    """

    def __init__(
        self,
        name: str,
        createStepName: str,
        region: Region,
        incrementation: SymbolicConstant = ALLOW_SUBCYCLING,
        stepSize: float = 0,
        stepSizeDefinition: SymbolicConstant = DEFAULT,
    ):
        """This method creates a StdXplCosimulation object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].StdXplCosimulation

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the StdXplCosimulation object is
            created.
        region
            A Region object specifying the import and export region upon which the co-simulation
            exchanges data with the coupled analysis program.
        incrementation
            A SymbolicConstant specifying whether the analysis programs use the same time increments
            or one is allowed to use more time increments than the other before exchanging data.
            Possible values are ALLOW_SUBCYCLING and LOCKSTEP. The default value is
            ALLOW_SUBCYCLING.
        stepSize
            A Float specifying the size of the increments to be used by Abaqus/Standard and
            Abaqus/Explicit. The default value is 0.0.
        stepSizeDefinition
            A SymbolicConstant specifying whether the increment size is the analysis default or a
            supplied variable. Possible values are DEFAULT and SPECIFIED. The default value is
            DEFAULT.

        Returns
        -------
        A StdXplCosimulation object.
        """
        super().__init__()
        pass

    def setValues(
        self,
        incrementation: SymbolicConstant = ALLOW_SUBCYCLING,
        stepSize: float = 0,
        stepSizeDefinition: SymbolicConstant = DEFAULT,
    ):
        """This method modifies the StdXplCosimulation object.

        Parameters
        ----------
        incrementation
            A SymbolicConstant specifying whether the analysis programs use the same time increments
            or one is allowed to use more time increments than the other before exchanging data.
            Possible values are ALLOW_SUBCYCLING and LOCKSTEP. The default value is
            ALLOW_SUBCYCLING.
        stepSize
            A Float specifying the size of the increments to be used by Abaqus/Standard and
            Abaqus/Explicit. The default value is 0.0.
        stepSizeDefinition
            A SymbolicConstant specifying whether the increment size is the analysis default or a
            supplied variable. Possible values are DEFAULT and SPECIFIED. The default value is
            DEFAULT.
        """
        pass
