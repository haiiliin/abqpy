from __future__ import annotations

from typing_extensions import List

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import OFF, Boolean
from .FluidExchange import FluidExchange
from .Interaction import Interaction


@abaqus_class_doc
class FluidExchangeActivation(Interaction):
    """The FluidExchnageActivation object is used to define the activation of fluid exchanges within the fluid cavity.

    The FluidExchangeActivation object is derived from the Interaction object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name]

        The corresponding analysis keywords are:

        - FLUID EXCHANGE ACTIVATION

    .. versionadded:: 2025
        The ``FluidExchangeActivation`` class was added.
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the step in which the FluidExchange object is created.
    createStepName: str

    #: A List specifying fluid exchanges to be activated.
    exchanges: List[FluidExchange]

    #: A String specifying the name of the amplitude curve defining a mapping between the inflation time and the actual
    #: time.
    amplitude: str

    #: A Boolean specifying the vent and leakage area obstruction by contacted surfaces.
    isBlockage: Boolean

    #: A Boolean specifying if the flow of fluid is only from the first fluid cavity to the second fluid cavity defined
    #: in the FluidExchange object.
    isOnlyOutflow: Boolean

    #: A Float specifying the ratio of the actual surface area over the initial surface area at which you want the fluid
    #: to leak.
    deltaLeakageArea: float

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        exchanges: List[FluidExchange],
        amplitude: str,
        isBlockage: Boolean = OFF,
        isOnlyOutflow: Boolean = OFF,
        deltaLeakageArea: float = 0.0,
    ):
        """This method creates an FluidExchangeActivation object.

        .. note::
            This function can be accessed by::

                mdb.models[name].FluidExchangeActivation

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the FluidExchangeActivation object is created.
        exchanges
            A List specifying fluid exchanges to be activated.
        amplitude
            A String specifying the name of the amplitude curve defining a mapping between the inflation time and the actual
            time.
        isBlockage
            A Boolean specifying the vent and leakage area obstruction by contacted surfaces.
        isOnlyOutflow
            A Boolean specifying if the flow of fluid is only from the first fluid cavity to the second fluid cavity defined
            in the FluidExchange object.
        deltaLeakageArea
            A Float specifying the ratio of the actual surface area over the initial surface area at which you want the fluid
            to leak.

        Returns
        -------
        FluidExchangeActivation
            A FluidExchangeActivation object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        exchanges: List[FluidExchange],
        amplitude: str,
        isBlockage: Boolean = OFF,
        isOnlyOutflow: Boolean = OFF,
        deltaLeakageArea: float = 0.0,
    ):
        """This method modifies the FluidExchangeActivation object.

        Parameters
        ----------

        Parameters
        ----------
        exchanges
            A List specifying fluid exchanges to be activated.
        amplitude
            A String specifying the name of the amplitude curve defining a mapping between the inflation time and the actual time.
        isBlockage
            A Boolean specifying the vent and leakage area obstruction by contacted surfaces.
        isOnlyOutflow
            A Boolean specifying if the flow of fluid is only from the first fluid cavity to the second fluid cavity defined in the FluidExchange object.
        deltaLeakageArea
            A Float specifying the ratio of the actual surface area over the initial surface area at which you want the fluid to leak.
        """
        ...
