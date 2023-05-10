from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import ON, Boolean
from .Interaction import Interaction


@abaqus_class_doc
class XFEMCrackGrowth(Interaction):
    """The XFEMCrackGrowth object defines the enrichment activation state for an XFEMCrack. The XFEMCrackGrowth
    object is derived from the Interaction object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name]

        The corresponding analysis keywords are:

        - ENRICHMENT ACTIVATION
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the step in which the XFEMCrackGrowth object is created.
    createStepName: str

    #: A String specifying the XFEMCrack object associated with this interaction.
    crackName: str

    #: A Boolean specifying whether the crack is allowed to grow (propagate) during this
    #: analysis step. The default value is ON.
    allowGrowth: Boolean = ON

    @abaqus_method_doc
    def __init__(self, name: str, createStepName: str, crackName: str, allowGrowth: Boolean = ON):
        """This method creates an XFEMCrackGrowth object.

        .. note::
            This function can be accessed by::

                mdb.models[name].XFEMCrackGrowth

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the XFEMCrackGrowth object is created.
        crackName
            A String specifying the XFEMCrack object associated with this interaction.
        allowGrowth
            A Boolean specifying whether the crack is allowed to grow (propagate) during this
            analysis step. The default value is ON.

        Returns
        -------
        XFEMCrackGrowth
            A XFEMCrackGrowth object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, allowGrowth: Boolean = ON):
        """This method modifies the data for an existing XFEMCrackGrowth object in the step where it is created.

        Parameters
        ----------
        allowGrowth
            A Boolean specifying whether the crack is allowed to grow (propagate) during this
            analysis step. The default value is ON.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(self, stepName: str, allowGrowth: Boolean = ON):
        """This method modifies the propagating data for an existing XFEMCrackGrowth object in the specified
        step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified.
        allowGrowth
            A Boolean specifying whether the crack is allowed to grow (propagate) during this
            analysis step. The default value is ON.
        """
        ...
