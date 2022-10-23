from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Interaction import Interaction
from ..UtilityAndView.abaqusConstants import SymbolicConstant, TO_ENVIRONMENT
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class FluidExchange(Interaction):
    """The FluidExchange object is used to define fluid exchange between two fluid cavities or
    between a fluid cavity and its environment.
    The FluidExchange object is derived from the Interaction object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name]

        The corresponding analysis keywords are:

        - FLUID EXCHANGE
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the step in which the FluidExchange object is created.
    createStepName: str

    #: A String specifying the first FluidCavity object associated with this interaction. This
    #: will be the only cavity specified if **definition** = TO_ENVIRONMENT.
    firstCavity: str

    #: A String specifying the FluidExchangeProperty object associated with this interaction.
    interactionProperty: str

    #: A SymbolicConstant specifying the type of fluid exchange to be defined. Possible values
    #: are TO_ENVIRONMENT and BETWEEN_CAVITIES. The default value is TO_ENVIRONMENT.
    definition: SymbolicConstant = TO_ENVIRONMENT

    #: A String specifying the second FluidCavity object associated with this interaction. This
    #: argument is applicable only when **definition** = BETWEEN_CAVITIES.
    secondCavity: str = ""

    #: A Float specifying the effective exchange area. The default value is 1.0.
    exchangeArea: float = 1

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        firstCavity: str,
        interactionProperty: str,
        definition: Literal[C.BETWEEN_CAVITIES, C.TO_ENVIRONMENT] = TO_ENVIRONMENT,
        secondCavity: str = "",
        exchangeArea: float = 1,
    ):
        """This method creates an FluidExchange object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].FluidExchange

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the FluidExchange object is created.
        firstCavity
            A String specifying the first FluidCavity object associated with this interaction. This
            will be the only cavity specified if **definition** = TO_ENVIRONMENT.
        interactionProperty
            A String specifying the FluidExchangeProperty object associated with this interaction.
        definition
            A SymbolicConstant specifying the type of fluid exchange to be defined. Possible values
            are TO_ENVIRONMENT and BETWEEN_CAVITIES. The default value is TO_ENVIRONMENT.
        secondCavity
            A String specifying the second FluidCavity object associated with this interaction. This
            argument is applicable only when **definition** = BETWEEN_CAVITIES.
        exchangeArea
            A Float specifying the effective exchange area. The default value is 1.0.

        Returns
        -------
        FluidExchange
            A :py:class:`~abaqus.Interaction.FluidExchange.FluidExchange` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        definition: Literal[C.BETWEEN_CAVITIES, C.TO_ENVIRONMENT] = TO_ENVIRONMENT,
        secondCavity: str = "",
        exchangeArea: float = 1,
    ):
        """This method modifies the FluidExchange object.

        Parameters
        ----------
        definition
            A SymbolicConstant specifying the type of fluid exchange to be defined. Possible values
            are TO_ENVIRONMENT and BETWEEN_CAVITIES. The default value is TO_ENVIRONMENT.
        secondCavity
            A String specifying the second FluidCavity object associated with this interaction. This
            argument is applicable only when **definition** = BETWEEN_CAVITIES.
        exchangeArea
            A Float specifying the effective exchange area. The default value is 1.0.
        """
        ...
