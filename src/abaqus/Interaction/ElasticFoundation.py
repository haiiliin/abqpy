from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Interaction import Interaction
from ..Region.Region import Region


@abaqus_class_doc
class ElasticFoundation(Interaction):
    """The ElasticFoundation object defines a mechanical foundation.
    The ElasticFoundation object is derived from the Interaction object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name]

        The corresponding analysis keywords are:

        - FOUNDATION
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the step in which the ElasticFoundation object is
    #: created. **createStepName** must be set to 'Initial'.
    createStepName: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the surface to which the foundation applies.
    surface: Region

    #: A Float specifying the foundation stiffness per area (or per length for beams).
    stiffness: float

    @abaqus_method_doc
    def __init__(
        self, name: str, createStepName: str, surface: Region, stiffness: float
    ):
        """This method creates an ElasticFoundation object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ElasticFoundation

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the ElasticFoundation object is
            created. **createStepName** must be set to 'Initial'.
        surface
            A :py:class:`~abaqus.Region.Region.Region` object specifying the surface to which the foundation applies.
        stiffness
            A Float specifying the foundation stiffness per area (or per length for beams).

        Returns
        -------
        ElasticFoundation
            An :py:class:`~abaqus.Interaction.ElasticFoundation.ElasticFoundation` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the data for an existing ElasticFoundation object in the step where
        it is created.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(self, stepName: str, stiffness: Optional[float] = None):
        """This method modifies the propagating data of an existing ElasticFoundation object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified.
        stiffness
            A Float specifying the foundation stiffness per area (or per length for beams).
        """
        ...
