from typing_extensions import Literal
from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Interaction import Interaction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import Boolean, GEOMETRY, OFF, SymbolicConstant


@abaqus_class_doc
class ModelChange(Interaction):
    """The ModelChange object defines model change interactions for element removal and
    reactivation.
    The ModelChange object is derived from the Interaction object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name]

        The corresponding analysis keywords are:

        - MODEL CHANGE
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the step in which the ModelChange object is created.
    createStepName: str

    #: A Boolean specifying whether this interaction is being used solely to indicate that
    #: model change may be required in a subsequent restart analysis (either for elements or
    #: contact pairs). The default value is OFF.
    isRestart: Boolean = OFF

    #: A SymbolicConstant specifying the region selection type. This argument is valid only
    #: when **isRestart** = False. Possible values are GEOMETRY, SKINS, STRINGERS, and ELEMENTS.
    #: The default value is GEOMETRY.
    regionType: SymbolicConstant = GEOMETRY

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the elements to be removed or reactivated. This argument is
    #: valid only when **isRestart** = False.
    region: Optional[Region] = None

    #: A Boolean specifying whether elements are being removed or reactivated. This argument is
    #: valid only when **isRestart** = False. The default value is OFF.
    activeInStep: Boolean = OFF

    #: A Boolean specifying whether stress/displacement elements are reactivated with strain.
    #: This argument is valid only when **isRestart** = False and when **activeInStep** = True. The
    #: default value is OFF.
    includeStrain: Boolean = OFF

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        isRestart: Boolean = OFF,
        regionType: Literal[C.SKINS, C.GEOMETRY, C.ELEMENTS, C.STRINGERS] = GEOMETRY,
        region: Optional[Region] = None,
        activeInStep: Boolean = OFF,
        includeStrain: Boolean = OFF,
    ):
        """This method creates a ModelChange object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ModelChange

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the ModelChange object is created.
        isRestart
            A Boolean specifying whether this interaction is being used solely to indicate that
            model change may be required in a subsequent restart analysis (either for elements or
            contact pairs). The default value is OFF.
        regionType
            A SymbolicConstant specifying the region selection type. This argument is valid only
            when **isRestart** = False. Possible values are GEOMETRY, SKINS, STRINGERS, and ELEMENTS.
            The default value is GEOMETRY.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the elements to be removed or reactivated. This argument is
            valid only when **isRestart** = False.
        activeInStep
            A Boolean specifying whether elements are being removed or reactivated. This argument is
            valid only when **isRestart** = False. The default value is OFF.
        includeStrain
            A Boolean specifying whether stress/displacement elements are reactivated with strain.
            This argument is valid only when **isRestart** = False and when **activeInStep** = True. The
            default value is OFF.

        Returns
        -------
        ModelChange
            A :py:class:`~abaqus.Interaction.ModelChange.ModelChange` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        isRestart: Boolean = OFF,
        regionType: Literal[C.SKINS, C.GEOMETRY, C.ELEMENTS, C.STRINGERS] = GEOMETRY,
        region: Optional[Region] = None,
        activeInStep: Boolean = OFF,
        includeStrain: Boolean = OFF,
    ):
        """This method modifies the data for an existing ModelChange object in the step where it is
        created.

        Parameters
        ----------
        isRestart
            A Boolean specifying whether this interaction is being used solely to indicate that
            model change may be required in a subsequent restart analysis (either for elements or
            contact pairs). The default value is OFF.
        regionType
            A SymbolicConstant specifying the region selection type. This argument is valid only
            when **isRestart** = False. Possible values are GEOMETRY, SKINS, STRINGERS, and ELEMENTS.
            The default value is GEOMETRY.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the elements to be removed or reactivated. This argument is
            valid only when **isRestart** = False.
        activeInStep
            A Boolean specifying whether elements are being removed or reactivated. This argument is
            valid only when **isRestart** = False. The default value is OFF.
        includeStrain
            A Boolean specifying whether stress/displacement elements are reactivated with strain.
            This argument is valid only when **isRestart** = False and when **activeInStep** = True. The
            default value is OFF.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self, stepName: str, activeInStep: Boolean = OFF, includeStrain: Boolean = OFF
    ):
        """This method modifies the propagating data of an existing ModelChange object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified.
        activeInStep
            A Boolean specifying whether elements are being removed or reactivated. This argument is
            valid only when **isRestart** = False. The default value is OFF.
        includeStrain
            A Boolean specifying whether stress/displacement elements are reactivated with strain.
            This argument is valid only when **isRestart** = False and when **activeInStep** = True. The
            default value is OFF.
        """
        ...
