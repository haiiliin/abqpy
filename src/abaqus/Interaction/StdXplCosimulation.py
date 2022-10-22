from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Interaction import Interaction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import ALLOW_SUBCYCLING, DEFAULT, SymbolicConstant


@abaqus_class_doc
class StdXplCosimulation(Interaction):
    """The StdXplCosimulation object defines co-simulation behavior between Abaqus/Standard and
    Abaqus/Explicit.
    The StdXplCosimulation object is derived from the Interaction object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name]
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the step in which the StdXplCosimulation object is
    #: created.
    createStepName: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the import and export region upon which the co-simulation
    #: exchanges data with the coupled analysis program.
    region: Region

    #: A SymbolicConstant specifying whether the analysis programs use the same time increments
    #: or one is allowed to use more time increments than the other before exchanging data.
    #: Possible values are ALLOW_SUBCYCLING and LOCKSTEP. The default value is
    #: ALLOW_SUBCYCLING.
    incrementation: SymbolicConstant = ALLOW_SUBCYCLING

    #: A Float specifying the size of the increments to be used by Abaqus/Standard and
    #: Abaqus/Explicit. The default value is 0.0.
    stepSize: float = 0

    #: A SymbolicConstant specifying whether the increment size is the analysis default or a
    #: supplied variable. Possible values are DEFAULT and SPECIFIED. The default value is
    #: DEFAULT.
    stepSizeDefinition: SymbolicConstant = DEFAULT

    @abaqus_method_doc
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

        .. note:: 
            This function can be accessed by::

                mdb.models[name].StdXplCosimulation

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the StdXplCosimulation object is
            created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the import and export region upon which the co-simulation
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
        StdXplCosimulation
            A :py:class:`~abaqus.Interaction.StdXplCosimulation.StdXplCosimulation` object.
        """
        super().__init__()

    @abaqus_method_doc
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
        ...
