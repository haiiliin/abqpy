from __future__ import annotations

from typing_extensions import List

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .FluidInflator import FluidInflator
from .Interaction import Interaction


@abaqus_class_doc
class FluidInflatorActivation(Interaction):
    """The FluidInflatorActivation object is used to define the activation of fluid inflators to model the deployment of
    an airbag.

    The FluidInflatorActivation object is derived from the Interaction object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name]

        The corresponding analysis keywords are:

        - FLUID INFLATOR ACTIVATION

    .. versionadded:: 2025
        The ``FluidInflatorActivation`` class was added.
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the step in which the FluidInflator object is created.
    createStepName: str

    #: A List specifying fluid inflators to be activated.
    inflators: List[FluidInflator]

    #: A String specifying the name of the amplitude curve defining a mapping between the inflation time and the actual
    #: time.
    inflationTimeAmplitude: str

    #: A String specifying the name of the amplitude curve by which to modify the mass flow rate.
    massFlowAmplitude: str

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        inflators: List[FluidInflator],
        inflationTimeAmplitude: str = "",
        massFlowAmplitude: str = "",
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
            A String specifying the name of the step in which the FluidInflator object is created.
        inflators
            A list specifying fluid inflators to be activated.
        inflationTimeAmplitude
            A string specifying the name of the amplitude curve defining a mapping between the inflation time
            and the actual time.
        massFlowAmplitude
            A string specifying the name of the amplitude curve by which to modify the mass flow rate.

        Returns
        -------
        FluidInflatorActivation
            A FluidInflatorActivation object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        exchanges: List,
        amplitude: str,
        inflators: List[FluidInflator],
        inflationTimeAmplitude: str = "",
        massFlowAmplitude: str = "",
    ):
        """This method modifies the FluidInflatorActivation object.

        Parameters
        ----------

        Parameters
        ----------
        inflators
            A list specifying fluid inflators to be activated.
        inflationTimeAmplitude
            A string specifying the name of the amplitude curve defining a mapping between the inflation time
            and the actual time.
        massFlowAmplitude
            A string specifying the name of the amplitude curve by which to modify the mass flow rate.
        """
        ...
