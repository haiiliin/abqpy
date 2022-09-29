from typing import Optional
from abqpy.decorators import abaqus_class_doc
from .InteractionState import InteractionState
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class CyclicSymmetryState(InteractionState):
    """The CyclicSymmetryState object stores the propagating data for a CyclicSymmetry object.
    One instance of this object is created internally by the CyclicSymmetry object for each
    step. The instance is also deleted internally by the CyclicSymmetry object.
    The CyclicSymmetryState object has no constructor or methods.
    The CyclicSymmetryState object is derived from the InteractionState object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].steps[name].interactionStates[name]

        The corresponding analysis keywords are:

        - CLOAD
        - DLOAD
        - DSLOAD
        - SELECT CYCLIC SYMMETRY MODES
    """

    #: A SymbolicConstant specifying whether Abaqus should extract all possible nodal diameters
    #: or the nodal diameters between the user-specified values for **lowestNodalDiameter** and
    #: **highestNodalDiameter**. Possible values are ALL_NODAL_DIAMETER and
    #: SPECIFIED_NODAL_DIAMETER. The default value is ALL_NODAL_DIAMETER.
    extractedNodalDiameter: SymbolicConstant = ALL_NODAL_DIAMETER

    #: A SymbolicConstant specifying the propagation state of the **extractedNodalDiameter**
    #: member. Possible values are UNSET, SET, UNCHANGED, and FREED.
    extractedNodalDiameterState: Optional[SymbolicConstant] = None

    #: An Int specifying the lowest nodal diameter to be used in the eigenfrequency analysis.
    #: The default value is 0.
    lowestNodalDiameter: int = 0

    #: A SymbolicConstant specifying the propagation state of the **lowestNodalDiameter** member.
    #: Possible values are UNSET, SET, UNCHANGED, and FREED.
    lowestNodalDiameterState: Optional[SymbolicConstant] = None

    #: An Int specifying the highest nodal diameter to be used in the eigenfrequency analysis.
    #: This argument value should be less than or equal to the half of the total number of
    #: sectors. The default value is 0.
    highestNodalDiameter: int = 0

    #: A SymbolicConstant specifying the propagation state of the **highestNodalDiameter**
    #: member. Possible values are UNSET, SET, UNCHANGED, and FREED.
    highestNodalDiameterState: Optional[SymbolicConstant] = None

    #: An Int specifying the nodal diameter for which the modal-based steady-state dynamic
    #: analysis will be performed. This value should be greater than or equal to the lowest
    #: nodal diameter (specified in the **lowestNodalDiameter** parameter), and less than or
    #: equal to the highest nodal diameter (specified in the **highestNodalDiameter** parameter).
    #: The default value is 0.
    excitiationNodalDiameter: int = 0

    #: A SymbolicConstant specifying the propagation state of the **excitiationNodalDiameter**
    #: member. Possible values are UNSET, SET, UNCHANGED, and FREED.
    excitiationNodalDiameterState: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the InteractionState object.
    #: Possible values are:
    #: 
    #: - NOT_YET_ACTIVE
    #: - CREATED
    #: - PROPAGATED
    #: - MODIFIED
    #: - DEACTIVATED
    #: - NO_LONGER_ACTIVE
    #: - TYPE_NOT_APPLICABLE
    #: - INSTANCE_NOT_APPLICABLE
    #: - BUILT_INTO_BASE_STATE
    status: Optional[SymbolicConstant] = None
