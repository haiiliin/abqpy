from typing import Optional
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Constraint import Constraint
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class EmbeddedRegion(Constraint):
    """The EmbeddedRegion object allows you to embed a region of the model within a “host”
    region of the model or within the whole model.
    The EmbeddedRegion object is derived from the ConstrainedSketchConstraint object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].constraints[name]

        The corresponding analysis keywords are:

        - EMBEDDED ELEMENT
    """

    #: A Boolean specifying whether the constraint is suppressed or not. The default value is
    #: OFF.
    suppressed: Boolean = OFF

    #: A String specifying the constraint repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the body region to be embedded.
    embeddedRegion: Region

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the host region. A value of None indicates that the host
    #: region is the whole model.
    hostRegion: Region

    #: A Float specifying a small value below which the weighting factors will be zeroed out.
    #: The default value is 10-6.
    weightFactorTolerance: Optional[float] = None

    #: A SymbolicConstant specifying the method used to determine the embedded element
    #: tolerance. Possible values are ABSOLUTE, FRACTIONAL, and BOTH. The default value is
    #: BOTH.
    toleranceMethod: SymbolicConstant = BOTH

    #: A Float specifying the absolute value by which a node on the embedded region may lie
    #: outside the host region. If **absoluteTolerance** = 0.0, the **fractionalTolerance** value
    #: will be used. The default value is 0.0.This argument applies only when
    #: **toleranceMethod** = ABSOLUTE or BOTH.
    absoluteTolerance: float = 0

    #: A Float specifying the fractional value by which a node on the embedded region may lie
    #: outside the host region. The fractional value is based on the average element size
    #: within the host region. The default value is 0.05.If both tolerance arguments are
    #: specified, the smaller value will be used.This argument applies only when
    #: **toleranceMethod** = FRACTIONAL or BOTH.
    fractionalTolerance: float = 0

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        embeddedRegion: Region,
        hostRegion: Region,
        weightFactorTolerance: Optional[float] = None,
        toleranceMethod: SymbolicConstant = BOTH,
        absoluteTolerance: float = 0,
        fractionalTolerance: float = 0,
    ):
        """This method creates a EmbeddedRegion object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].EmbeddedRegion

        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        embeddedRegion
            A :py:class:`~abaqus.Region.Region.Region` object specifying the body region to be embedded.
        hostRegion
            A :py:class:`~abaqus.Region.Region.Region` object specifying the host region. A value of None indicates that the host
            region is the whole model.
        weightFactorTolerance
            A Float specifying a small value below which the weighting factors will be zeroed out.
            The default value is 10-6.
        toleranceMethod
            A SymbolicConstant specifying the method used to determine the embedded element
            tolerance. Possible values are ABSOLUTE, FRACTIONAL, and BOTH. The default value is
            BOTH.
        absoluteTolerance
            A Float specifying the absolute value by which a node on the embedded region may lie
            outside the host region. If **absoluteTolerance** = 0.0, the **fractionalTolerance** value
            will be used. The default value is 0.0.This argument applies only when
            **toleranceMethod** = ABSOLUTE or BOTH.
        fractionalTolerance
            A Float specifying the fractional value by which a node on the embedded region may lie
            outside the host region. The fractional value is based on the average element size
            within the host region. The default value is 0.05.If both tolerance arguments are
            specified, the smaller value will be used.This argument applies only when
            **toleranceMethod** = FRACTIONAL or BOTH.

        Returns
        -------
        EmbeddedRegion
            An :py:class:`~abaqus.Constraint.EmbeddedRegion.EmbeddedRegion` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        weightFactorTolerance: Optional[float] = None,
        toleranceMethod: SymbolicConstant = BOTH,
        absoluteTolerance: float = 0,
        fractionalTolerance: float = 0,
    ):
        """This method modifies the EmbeddedRegion object.

        Parameters
        ----------
        weightFactorTolerance
            A Float specifying a small value below which the weighting factors will be zeroed out.
            The default value is 10-6.
        toleranceMethod
            A SymbolicConstant specifying the method used to determine the embedded element
            tolerance. Possible values are ABSOLUTE, FRACTIONAL, and BOTH. The default value is
            BOTH.
        absoluteTolerance
            A Float specifying the absolute value by which a node on the embedded region may lie
            outside the host region. If **absoluteTolerance** = 0.0, the **fractionalTolerance** value
            will be used. The default value is 0.0.This argument applies only when
            **toleranceMethod** = ABSOLUTE or BOTH.
        fractionalTolerance
            A Float specifying the fractional value by which a node on the embedded region may lie
            outside the host region. The fractional value is based on the average element size
            within the host region. The default value is 0.05.If both tolerance arguments are
            specified, the smaller value will be used.This argument applies only when
            **toleranceMethod** = FRACTIONAL or BOTH.
        """
        ...
