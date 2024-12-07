from __future__ import annotations

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Interaction import Interaction


@abaqus_class_doc
class FluidInflator(Interaction):
    """The FluidInflator object is used to define a fluid inflator to model deployment of an airbag. The
    FluidInflator object is derived from the Interaction object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name]

        The corresponding analysis keywords are:

        - FLUID INFLATOR

    .. versionadded:: 2019
        The ``FluidInflator`` class was added.
    """

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        cavity: str,
        interactionProperty: str,
    ):
        """This method creates a FluidInflator object.

        .. note::
            This function can be accessed by::

                mdb.models[name].FluidInflator

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the FluidInflator object is created.
        cavity
            A String specifying the first FluidCavity object associated with this interaction.
        interactionProperty
            A String specifying the FluidInflatorProperty object associated with this interaction.

        Returns
        -------
            A FluidInflator object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self):
        """This method modifies the FluidInflator object."""
        ...
