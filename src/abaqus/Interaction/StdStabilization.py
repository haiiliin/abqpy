from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .ContactStabilization import ContactStabilization
from ..UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class StdStabilization(ContactStabilization):
    """The StdStabilization object is used in conjunction with ContactStd in Abaqus/Standard
    analyses to specify contact stabilization.
    The StdStabilization object is derived from the ContactStabilization object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].contactStabilizations[name]

        The corresponding analysis keywords are:

        - CONTACT STABILIZATION
    """

    #: A String specifying the contact stabilization repository key.
    name: str

    #: None or a Float specifying the clearance distance at which the stabilization becomes
    #: zero. The default value is None.
    zeroDistance: Optional[float] = None

    #: A Float specifying the factor by which the analysis will reduce the contact
    #: stabilization coefficient per increment. The default value is 0.1.
    reductionFactor: float = 0

    #: A Float specifying the factor by which the analysis will scale the contact stabilization
    #: coefficient. The default value is 1.0.
    scaleFactor: float = 1

    #: A Float specifying the factor that scales the contact stabilization coefficient in the
    #: tangential direction. The default value is 0.0.
    tangentialFactor: float = 0

    #: A String specifying the name of the Amplitude object that defines a time-dependent scale
    #: factor for contact stabilization over the step. The default value is an empty string.
    amplitude: str = ""

    #: A Boolean specifying whether to cancel carryover effects from contact stabilization
    #: specifications involving nondefault amplitudes that appeared in previous steps. The
    #: default value is OFF.
    reset: Boolean = OFF

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        zeroDistance: Optional[float] = None,
        reductionFactor: float = 0,
        scaleFactor: float = 1,
        tangentialFactor: float = 0,
        amplitude: str = "",
        reset: Boolean = OFF,
    ):
        """This method creates a StdStabilization object.

        .. note::
            This function can be accessed by::

                mdb.models[name].StdStabilization

        Parameters
        ----------
        name
            A String specifying the contact stabilization repository key.
        zeroDistance
            None or a Float specifying the clearance distance at which the stabilization becomes
            zero. The default value is None.
        reductionFactor
            A Float specifying the factor by which the analysis will reduce the contact
            stabilization coefficient per increment. The default value is 0.1.
        scaleFactor
            A Float specifying the factor by which the analysis will scale the contact stabilization
            coefficient. The default value is 1.0.
        tangentialFactor
            A Float specifying the factor that scales the contact stabilization coefficient in the
            tangential direction. The default value is 0.0.
        amplitude
            A String specifying the name of the Amplitude object that defines a time-dependent scale
            factor for contact stabilization over the step. The default value is an empty string.
        reset
            A Boolean specifying whether to cancel carryover effects from contact stabilization
            specifications involving nondefault amplitudes that appeared in previous steps. The
            default value is OFF.

        Returns
        -------
        StdStabilization
            A :py:class:`~abaqus.Interaction.StdStabilization.StdStabilization` object.

        Raises
        ------
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        zeroDistance: Optional[float] = None,
        reductionFactor: float = 0,
        scaleFactor: float = 1,
        tangentialFactor: float = 0,
        amplitude: str = "",
        reset: Boolean = OFF,
    ):
        """This method modifies the StdStabilization object.

        Parameters
        ----------
        zeroDistance
            None or a Float specifying the clearance distance at which the stabilization becomes
            zero. The default value is None.
        reductionFactor
            A Float specifying the factor by which the analysis will reduce the contact
            stabilization coefficient per increment. The default value is 0.1.
        scaleFactor
            A Float specifying the factor by which the analysis will scale the contact stabilization
            coefficient. The default value is 1.0.
        tangentialFactor
            A Float specifying the factor that scales the contact stabilization coefficient in the
            tangential direction. The default value is 0.0.
        amplitude
            A String specifying the name of the Amplitude object that defines a time-dependent scale
            factor for contact stabilization over the step. The default value is an empty string.
        reset
            A Boolean specifying whether to cancel carryover effects from contact stabilization
            specifications involving nondefault amplitudes that appeared in previous steps. The
            default value is OFF.

        Raises
        ------
        RangeError
        """
        ...
