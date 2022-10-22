from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Interaction import Interaction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import KINEMATIC, SymbolicConstant


@abaqus_class_doc
class SelfContactExp(Interaction):
    """The SelfContactExp object defines self-contact during an Abaqus/Explicit analysis.
    The SelfContactExp object is derived from the Interaction object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name]
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the step in which the SelfContactExp object is created.
    createStepName: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the surface where self-contact is defined.
    surface: Region

    #: A String specifying the name of the ContactProperty object associated with this
    #: interaction.
    interactionProperty: str

    #: A SymbolicConstant specifying the mechanical constraint formulation. Possible values are
    #: KINEMATIC and PENALTY. The default value is KINEMATIC.
    mechanicalConstraint: SymbolicConstant = KINEMATIC

    #: A String specifying the name of the ContactControl object associated with this
    #: interaction. An empty string indicates that the default contact controls will be used.
    #: The default value is an empty string.
    contactControls: str = ""

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        surface: Region,
        interactionProperty: str,
        mechanicalConstraint: SymbolicConstant = KINEMATIC,
        contactControls: str = "",
    ):
        """This method creates a SelfContactExp object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].SelfContactExp

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the SelfContactExp object is created.
        surface
            A :py:class:`~abaqus.Region.Region.Region` object specifying the surface where self-contact is defined.
        interactionProperty
            A String specifying the name of the ContactProperty object associated with this
            interaction.
        mechanicalConstraint
            A SymbolicConstant specifying the mechanical constraint formulation. Possible values are
            KINEMATIC and PENALTY. The default value is KINEMATIC.
        contactControls
            A String specifying the name of the ContactControl object associated with this
            interaction. An empty string indicates that the default contact controls will be used.
            The default value is an empty string.

        Returns
        -------
        SelfContactExp
            A :py:class:`~abaqus.Interaction.SelfContactExp.SelfContactExp` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        mechanicalConstraint: SymbolicConstant = KINEMATIC,
        contactControls: str = "",
    ):
        """This method modifies the data for an existing SelfContactExp object in the step where it
        is created.

        Parameters
        ----------
        mechanicalConstraint
            A SymbolicConstant specifying the mechanical constraint formulation. Possible values are
            KINEMATIC and PENALTY. The default value is KINEMATIC.
        contactControls
            A String specifying the name of the ContactControl object associated with this
            interaction. An empty string indicates that the default contact controls will be used.
            The default value is an empty string.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self, stepName: str, interactionProperty: str = "", contactControls: str = ""
    ):
        """This method modifies the propagating data for an existing SelfContactExp object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified.
        interactionProperty
            A String specifying the name of the ContactProperty object associated with this
            interaction.
        contactControls
            A String specifying the name of the ContactControl object associated with this
            interaction. An empty string indicates that the default contact controls will be used.
            The default value is an empty string.
        """
        ...
