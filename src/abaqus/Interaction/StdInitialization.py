from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .ContactInitialization import ContactInitialization
from ..UtilityAndView.abaqusConstants import ADJUST, SymbolicConstant


@abaqus_class_doc
class StdInitialization(ContactInitialization):
    """The StdInitialization object is used in conjunction with ContactStd in Abaqus/Standard
    analyses to specify contact initialization data.
    The StdInitialization object is derived from the ContactInitialization object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].contactInitializations[name]

        The corresponding analysis keywords are:

        - CONTACT INITIALIZATION DATA
    """

    #: A String specifying the contact initialization repository key.
    name: str

    #: A SymbolicConstant specifying the type of overclosure to be defined. Possible values are
    #: ADJUST, INTERFERENCE, and CLEARANCE. The default value is ADJUST.
    overclosureType: SymbolicConstant = ADJUST

    #: None or a Float specifying the interference distance. This argument is valid only when
    #: **overclosureType** = INTERFERENCE. The default value is None.
    interferenceDistance: Optional[float] = None

    #: None or a Float specifying the initial clearance distance. This argument is valid only
    #: when **overclosureType** = CLEARANCE, and must be specified in that case. The default value
    #: is None.
    clearanceDistance: Optional[float] = None

    #: None or a Float specifying the distance tolerance within which initial openings will
    #: undergo strain-free adjustments. This argument is not valid when
    #: **overclosureType** = INTERFERENCE unless a value has been specified for
    #: **interferenceDistance**. The default value is None.
    openingTolerance: Optional[float] = None

    #: None or a Float specifying the distance tolerance within which initial overclosures will
    #: undergo strain-free adjustments.. The default value is None.
    overclosureTolerance: Optional[float] = None

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        overclosureType: SymbolicConstant = ADJUST,
        interferenceDistance: Optional[float] = None,
        clearanceDistance: Optional[float] = None,
        openingTolerance: Optional[float] = None,
        overclosureTolerance: Optional[float] = None,
    ):
        """This method creates a StdInitialization object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].StdInitialization

        Parameters
        ----------
        name
            A String specifying the contact initialization repository key.
        overclosureType
            A SymbolicConstant specifying the type of overclosure to be defined. Possible values are
            ADJUST, INTERFERENCE, and CLEARANCE. The default value is ADJUST.
        interferenceDistance
            None or a Float specifying the interference distance. This argument is valid only when
            **overclosureType** = INTERFERENCE. The default value is None.
        clearanceDistance
            None or a Float specifying the initial clearance distance. This argument is valid only
            when **overclosureType** = CLEARANCE, and must be specified in that case. The default value
            is None.
        openingTolerance
            None or a Float specifying the distance tolerance within which initial openings will
            undergo strain-free adjustments. This argument is not valid when
            **overclosureType** = INTERFERENCE unless a value has been specified for
            **interferenceDistance**. The default value is None.
        overclosureTolerance
            None or a Float specifying the distance tolerance within which initial overclosures will
            undergo strain-free adjustments.. The default value is None.

        Returns
        -------
        StdInitialization
            A :py:class:`~abaqus.Interaction.StdInitialization.StdInitialization` object.

        Raises
        ------
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        overclosureType: SymbolicConstant = ADJUST,
        interferenceDistance: Optional[float] = None,
        clearanceDistance: Optional[float] = None,
        openingTolerance: Optional[float] = None,
        overclosureTolerance: Optional[float] = None,
    ):
        """This method modifies the StdInitialization object.

        Parameters
        ----------
        overclosureType
            A SymbolicConstant specifying the type of overclosure to be defined. Possible values are
            ADJUST, INTERFERENCE, and CLEARANCE. The default value is ADJUST.
        interferenceDistance
            None or a Float specifying the interference distance. This argument is valid only when
            **overclosureType** = INTERFERENCE. The default value is None.
        clearanceDistance
            None or a Float specifying the initial clearance distance. This argument is valid only
            when **overclosureType** = CLEARANCE, and must be specified in that case. The default value
            is None.
        openingTolerance
            None or a Float specifying the distance tolerance within which initial openings will
            undergo strain-free adjustments. This argument is not valid when
            **overclosureType** = INTERFERENCE unless a value has been specified for
            **interferenceDistance**. The default value is None.
        overclosureTolerance
            None or a Float specifying the distance tolerance within which initial overclosures will
            undergo strain-free adjustments.. The default value is None.

        Raises
        ------
        RangeError
        """
        ...
