from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Step.StepBase import StepBase
from ..TableCollection.ActivateElements import ActivateElements


@abaqus_class_doc
class TableCollectionStep(StepBase):
    """The Step object stores the parameters that determine the context of the step. The Step object is the
    abstract base type for other Step objects. The Step object has no explicit constructor. The methods and
    members of the Step object are common to all objects derived from the Step.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name]

    .. versionadded:: 2020
        The ``TableCollectionStep`` class was added.
    """

    @abaqus_method_doc
    def ActivateElements(
        self,
        tableCollection: str,
        activation: str,
        eigenTimeConst: str = "",
        expansionTimeConstant: str = "",
    ) -> ActivateElements:
        """This method creates an ActivateElements object.

        .. note::
            This function can be accessed by::

                mdb.models[name].ActivateElements

        Parameters
        ----------
        tableCollection
            A String specifying the name of the tableCollection object.
        activation
            A string specifying the name of progressive element activation.
        eigenTimeConst
            A Double specifying the time constant used to ramp up the eigenstrains at element
            activation.
        expansionTimeConstant
            A Double specifying the time constant used to ramp up the thermal strains at element
            activation.

        Returns
        -------
        elements: ActivateElements
            An ActivateElements object.
        """
        self.activateElements["activation"] = activateElements = ActivateElements(
            tableCollection, activation, eigenTimeConst, expansionTimeConstant
        )
        return activateElements
