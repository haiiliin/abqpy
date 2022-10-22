from typing_extensions import Literal
from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .ContactControl import ContactControl
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import Boolean, DEFAULT, ON, SymbolicConstant


@abaqus_class_doc
class ExpContactControl(ContactControl):
    """The ExpContactControl object is used in Abaqus/Explicit analyses to specify optional
    solution controls for problems involving contact between bodies.
    The ExpContactControl object is derived from the ContactControl object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].contactControls[name]

        The corresponding analysis keywords are:

        - CONTACT CONTROLS
    """

    #: A String specifying the contact controls repository key.
    name: str

    #: A SymbolicConstant specifying whether or not the default value will be used for the
    #: maximum number of increments between global contact searches. Possible values are
    #: DEFAULT and SPECIFY. The default value is DEFAULT.
    globTrkChoice: SymbolicConstant = DEFAULT

    #: An Int specifying the maximum number of increments between global contact searches. The
    #: **globTrkInc** argument applies only when **globTrkChoice** = SPECIFY. The default value is
    #: 100 for surface-to-surface contact and 4 for self-contact.
    globTrkInc: Optional[int] = None

    #: A Boolean specifying whether to use the more computationally efficient local tracking
    #: method. The default value is ON.
    fastLocalTrk: Boolean = ON

    #: A Float specifying the factor by which Abaqus/Explicit will scale the default penalty
    #: stiffness to obtain the stiffnesses used for the penalty contact pairs. The default
    #: value is 1.0.
    scalePenalty: float = 1

    #: An Int specifying the number of increments between checks for highly warped facets on
    #: main surfaces. The default value is 20.
    warpCheckPeriod: int = 20

    #: A Float specifying the out-of-plane warping angle (in degrees), at which a facet will be
    #: considered to be highly warped. The default value is 20.0.
    warpCutoff: float = 20

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        globTrkChoice: Literal[C.SPECIFY, C.DEFAULT] = DEFAULT,
        globTrkInc: Optional[int] = None,
        fastLocalTrk: Boolean = ON,
        scalePenalty: float = 1,
        warpCheckPeriod: int = 20,
        warpCutoff: float = 20,
    ):
        """This method creates an ExpContactControl object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ExpContactControl

        Parameters
        ----------
        name
            A String specifying the contact controls repository key.
        globTrkChoice
            A SymbolicConstant specifying whether or not the default value will be used for the
            maximum number of increments between global contact searches. Possible values are
            DEFAULT and SPECIFY. The default value is DEFAULT.
        globTrkInc
            An Int specifying the maximum number of increments between global contact searches. The
            **globTrkInc** argument applies only when **globTrkChoice** = SPECIFY. The default value is
            100 for surface-to-surface contact and 4 for self-contact.
        fastLocalTrk
            A Boolean specifying whether to use the more computationally efficient local tracking
            method. The default value is ON.
        scalePenalty
            A Float specifying the factor by which Abaqus/Explicit will scale the default penalty
            stiffness to obtain the stiffnesses used for the penalty contact pairs. The default
            value is 1.0.
        warpCheckPeriod
            An Int specifying the number of increments between checks for highly warped facets on
            main surfaces. The default value is 20.
        warpCutoff
            A Float specifying the out-of-plane warping angle (in degrees), at which a facet will be
            considered to be highly warped. The default value is 20.0.

        Returns
        -------
        ExpContactControl
            An :py:class:`~abaqus.Interaction.ExpContactControl.ExpContactControl` object.

        Raises
        ------
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        globTrkChoice: Literal[C.SPECIFY, C.DEFAULT] = DEFAULT,
        globTrkInc: Optional[int] = None,
        fastLocalTrk: Boolean = ON,
        scalePenalty: float = 1,
        warpCheckPeriod: int = 20,
        warpCutoff: float = 20,
    ):
        """This method modifies the ExpContactControl object.

        Parameters
        ----------
        globTrkChoice
            A SymbolicConstant specifying whether or not the default value will be used for the
            maximum number of increments between global contact searches. Possible values are
            DEFAULT and SPECIFY. The default value is DEFAULT.
        globTrkInc
            An Int specifying the maximum number of increments between global contact searches. The
            **globTrkInc** argument applies only when **globTrkChoice** = SPECIFY. The default value is
            100 for surface-to-surface contact and 4 for self-contact.
        fastLocalTrk
            A Boolean specifying whether to use the more computationally efficient local tracking
            method. The default value is ON.
        scalePenalty
            A Float specifying the factor by which Abaqus/Explicit will scale the default penalty
            stiffness to obtain the stiffnesses used for the penalty contact pairs. The default
            value is 1.0.
        warpCheckPeriod
            An Int specifying the number of increments between checks for highly warped facets on
            main surfaces. The default value is 20.
        warpCutoff
            A Float specifying the out-of-plane warping angle (in degrees), at which a facet will be
            considered to be highly warped. The default value is 20.0.

        Raises
        ------
        RangeError
        """
        ...
