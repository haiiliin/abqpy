from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .ContactInitialization import ContactInitialization
from ..UtilityAndView.abaqusConstants import ADJUST, Boolean, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class ExpInitialization(ContactInitialization):
    """The ExpInitialization object is used in conjunction with ContactExp in Abaqus/Explicit
    analyses to specify contact initialization data.
    The ExpInitialization object is derived from the ContactInitialization object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].contactInitializations[name]

        The corresponding analysis keywords are:

        - CONTACT INITIALIZATION DATA

    .. versionadded:: 2020
        The `ExpInitialization` class was added.
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
    #: when **overclosureType** = CLEARANCE and must be specified in that case. The default value
    #: is None.
    clearanceDistance: Optional[float] = None

    #: None or a Float specifying the distance tolerance within which initial openings will
    #: undergo strain-free adjustments. This argument is not valid when
    #: **overclosureType** = INTERFERENCE unless a value has been specified for
    #: **interferenceDistance**. The default value is None.
    openingTolerance: Optional[float] = None

    #: None or a Float specifying the distance tolerance within which initial overclosures will
    #: undergo strain-free adjustments. The default value is None.
    overclosureTolerance: Optional[float] = None

    #: A Boolean specifying whether to resolve clearances/overclosures by adjusting the nodal
    #: coordinates without creating strain in the model. **adjustNodalCoords** = True can be used
    #: only for clearances/overclosures defined in the first step of an analysis. The default
    #: value is True.
    adjustNodalCoords: Boolean = True

    #: A String specifying the name of the node set containing the secondary nodes to be
    #: included in the initial clearance specification. This argument is not valid when
    #: **overclosureType** = INTERFERENCE and if **openingTolerance** or **overclosureTolerance** is
    #: specified. The default value is None.
    #:
    #: .. versionchanged:: 2022
    #:     The attribute `slaveNodesetName` was renamed to `secondaryNodesetName`.
    secondaryNodesetName: Optional[str] = None

    #: A Float specifying the fraction of the step time (between 0.0 and 1.0) in which the
    #: interference fit has to be solved. The default value is 1.0. This argument is valid only
    #: when **overclosureType** = INTERFERENCE.
    stepFraction: float = 1

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        overclosureType: Literal[C.INTERFERENCE, C.ADJUST, C.CLEARANCE] = ADJUST,
        interferenceDistance: Optional[float] = None,
        clearanceDistance: Optional[float] = None,
        openingTolerance: Optional[float] = None,
        overclosureTolerance: Optional[float] = None,
        adjustNodalCoords: Boolean = True,
        secondaryNodesetName: Optional[str] = None,
        stepFraction: float = 1,
    ):
        """This method creates an ExpInitialization object.

        .. note::
            This function can be accessed by::

                mdb.models[name].ExpInitialization

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
            when **overclosureType** = CLEARANCE and must be specified in that case. The default value
            is None.
        openingTolerance
            None or a Float specifying the distance tolerance within which initial openings will
            undergo strain-free adjustments. This argument is not valid when
            **overclosureType** = INTERFERENCE unless a value has been specified for
            **interferenceDistance**. The default value is None.
        overclosureTolerance
            None or a Float specifying the distance tolerance within which initial overclosures will
            undergo strain-free adjustments. The default value is None.
        adjustNodalCoords
            A Boolean specifying whether to resolve clearances/overclosures by adjusting the nodal
            coordinates without creating strain in the model. **adjustNodalCoords** = True can be used
            only for clearances/overclosures defined in the first step of an analysis. The default
            value is True.
        secondaryNodesetName
            A String specifying the name of the node set containing the secondary nodes to be
            included in the initial clearance specification. This argument is not valid when
            **overclosureType** = INTERFERENCE and if **openingTolerance** or **overclosureTolerance** is
            specified. The default value is None.

            .. versionchanged:: 2022
                The argument `slaveNodesetName` was renamed to `secondaryNodesetName`.
        stepFraction
            A Float specifying the fraction of the step time (between 0.0 and 1.0) in which the
            interference fit has to be solved. The default value is 1.0. This argument is valid only
            when **overclosureType** = INTERFERENCE.

        Returns
        -------
        ExpInitialization
            An :py:class:`~abaqus.Interaction.ExpInitialization.ExpInitialization` object.

        Raises
        ------
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        overclosureType: Literal[C.INTERFERENCE, C.ADJUST, C.CLEARANCE] = ADJUST,
        interferenceDistance: Optional[float] = None,
        clearanceDistance: Optional[float] = None,
        openingTolerance: Optional[float] = None,
        overclosureTolerance: Optional[float] = None,
        adjustNodalCoords: Boolean = True,
        secondaryNodesetName: Optional[str] = None,
        stepFraction: float = 1,
    ):
        """This method modifies the ExpInitialization object.

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
            when **overclosureType** = CLEARANCE and must be specified in that case. The default value
            is None.
        openingTolerance
            None or a Float specifying the distance tolerance within which initial openings will
            undergo strain-free adjustments. This argument is not valid when
            **overclosureType** = INTERFERENCE unless a value has been specified for
            **interferenceDistance**. The default value is None.
        overclosureTolerance
            None or a Float specifying the distance tolerance within which initial overclosures will
            undergo strain-free adjustments. The default value is None.
        adjustNodalCoords
            A Boolean specifying whether to resolve clearances/overclosures by adjusting the nodal
            coordinates without creating strain in the model. **adjustNodalCoords** = True can be used
            only for clearances/overclosures defined in the first step of an analysis. The default
            value is True.
        secondaryNodesetName
            A String specifying the name of the node set containing the secondary nodes to be
            included in the initial clearance specification. This argument is not valid when
            **overclosureType** = INTERFERENCE and if **openingTolerance** or **overclosureTolerance** is
            specified. The default value is None.

            .. versionchanged:: 2022
                The argument `slaveNodesetName` was renamed to `secondaryNodesetName`.
        stepFraction
            A Float specifying the fraction of the step time (between 0.0 and 1.0) in which the
            interference fit has to be solved. The default value is 1.0. This argument is valid only
            when **overclosureType** = INTERFERENCE.

        Raises
        ------
        RangeError
        """
        ...
