from typing import Optional
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .BoundaryCondition import BoundaryCondition
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class EulerianMotionBC(BoundaryCondition):
    """The EulerianMotionBC object stores the data for an Eulerian mesh motion boundary
    condition.
    The EulerianMotionBC object is derived from the BoundaryCondition object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].boundaryConditions[name]
    """

    #: A String specifying the boundary condition repository key.
    name: str = ""

    #: A Boolean specifying whether the mesh will follow a regular surface region or an
    #: Eulerian surface. The default value is ON.
    followRegion: Boolean = ON

    #: A SymbolicConstant specifying the 1-direction translational constraint on the center of
    #: the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.
    ctrPosition1: SymbolicConstant = FREE

    #: A SymbolicConstant specifying the 2-direction translational constraint on the center of
    #: the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.
    ctrPosition2: SymbolicConstant = FREE

    #: A SymbolicConstant specifying the 3-direction translational constraint on the center of
    #: the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.
    ctrPosition3: SymbolicConstant = FREE

    #: A SymbolicConstant specifying the translational constraint on the positive (maximum)
    #: bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
    #: value is FREE.
    posPosition1: SymbolicConstant = FREE

    #: A SymbolicConstant specifying the translational constraint on the positive (maximum)
    #: bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
    #: value is FREE.
    posPosition2: SymbolicConstant = FREE

    #: A SymbolicConstant specifying the translational constraint on the positive (maximum)
    #: bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
    #: value is FREE.
    posPosition3: SymbolicConstant = FREE

    #: A SymbolicConstant specifying the translational constraint on the negative (minimum)
    #: bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
    #: value is FREE.
    negPosition1: SymbolicConstant = FREE

    #: A SymbolicConstant specifying the translational constraint on the negative (minimum)
    #: bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
    #: value is FREE.
    negPosition2: SymbolicConstant = FREE

    #: A SymbolicConstant specifying the translational constraint on the negative (minimum)
    #: bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
    #: value is FREE.
    negPosition3: SymbolicConstant = FREE

    #: None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
    #: 1 direction. If **expansionRatio1** = None, then there is no upper limit. The default value
    #: is None.
    expansionRatio1: Optional[float] = None

    #: None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
    #: 2 direction. If **expansionRatio2** = None, then there is no upper limit. The default value
    #: is None.
    expansionRatio2: Optional[float] = None

    #: None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
    #: 3 direction. If **expansionRatio3** = None, then there is no upper limit. The default value
    #: is None.
    expansionRatio3: Optional[float] = None

    #: A Float specifying the lower bounds on the allowable scaling of the mesh in the 1
    #: direction. The default value is 0.0.
    contractRatio1: float = 0

    #: A Float specifying the lower bounds on the allowable scaling of the mesh in the 2
    #: direction. The default value is 0.0.
    contractRatio2: float = 0

    #: A Float specifying the lower bounds on the allowable scaling of the mesh in the 3
    #: direction. The default value is 0.0.
    contractRatio3: float = 0

    #: A Boolean specifying whether the mesh is allowed to contract . The default value is ON.
    allowContraction: Boolean = ON

    #: A Float specifying the maximum change in allowed aspect ratio (for any of the three mesh
    #: aspects, 1-2, 2-3, 3-1). The default value is 10.0.
    aspectLimit: float = 10

    #: A Float specifying the multiplier for the mesh nodal velocity limit. The default value
    #: is 1.01.
    vmaxFactor: float = 1

    #: A Float specifying the lower bounds on the volume fraction when determining which nodes
    #: to include in the surface bounding box calculation for an Eulerian material surface.
    #: This argument applies only when **followRegion** = False. The default value is 0.5.
    volThreshold: float = 0

    #: None or a Float specifying the buffer between the surface box and the Eulerian section
    #: mesh bounding box. The default value is 2.0.
    bufferSize: float = 2

    #: A String specifying the name of the Eulerian part instance.
    instanceName: str = ""

    #: A String specifying the name of the Eulerian surface to follow. This argument applies
    #: only when **followRegion** = False.
    materialName: str = ""

    #: A SymbolicConstant specifying the category of the boundary condition. Possible values
    #: are MECHANICAL and THERMAL.
    category: Optional[SymbolicConstant] = None

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
    region: Region = Region()

    #: None or a DatumCsys object specifying the local coordinate system of the boundary
    #: condition's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
    #: in the global coordinate system. The default value is None.
    localCsys: Optional[str] = None

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        instanceName: str,
        followRegion: Boolean = ON,
        region: Optional[Region] = None,
        materialName: str = "",
        ctrPosition1: SymbolicConstant = FREE,
        posPosition1: SymbolicConstant = FREE,
        negPosition1: SymbolicConstant = FREE,
        expansionRatio1: Optional[float] = None,
        contractRatio1: float = 0,
        ctrPosition2: SymbolicConstant = FREE,
        posPosition2: SymbolicConstant = FREE,
        negPosition2: SymbolicConstant = FREE,
        expansionRatio2: Optional[float] = None,
        contractRatio2: float = 0,
        ctrPosition3: SymbolicConstant = FREE,
        posPosition3: SymbolicConstant = FREE,
        negPosition3: SymbolicConstant = FREE,
        expansionRatio3: Optional[float] = None,
        contractRatio3: float = 0,
        allowContraction: Boolean = ON,
        aspectLimit: float = 10,
        vmaxFactor: float = 1,
        volThreshold: float = 0,
        bufferSize: float = 2,
    ):
        """This method creates an EulerianMotionBC object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].EulerianMotionBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key.
        createStepName
            A String specifying the name of the step in which the boundary condition is created.
        instanceName
            A String specifying the name of the Eulerian part instance.
        followRegion
            A Boolean specifying whether the mesh will follow a regular surface region or an
            Eulerian surface. The default value is ON.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        materialName
            A String specifying the name of the Eulerian surface to follow. This argument applies
            only when **followRegion** = False.
        ctrPosition1
            A SymbolicConstant specifying the 1-direction translational constraint on the center of
            the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.
        posPosition1
            A SymbolicConstant specifying the translational constraint on the positive (maximum)
            bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        negPosition1
            A SymbolicConstant specifying the translational constraint on the negative (minimum)
            bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        expansionRatio1
            None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
            1 direction. If **expansionRatio1** = None, then there is no upper limit. The default value
            is None.
        contractRatio1
            A Float specifying the lower bounds on the allowable scaling of the mesh in the 1
            direction. The default value is 0.0.
        ctrPosition2
            A SymbolicConstant specifying the 2-direction translational constraint on the center of
            the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.
        posPosition2
            A SymbolicConstant specifying the translational constraint on the positive (maximum)
            bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        negPosition2
            A SymbolicConstant specifying the translational constraint on the negative (minimum)
            bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        expansionRatio2
            None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
            2 direction. If **expansionRatio2** = None, then there is no upper limit. The default value
            is None.
        contractRatio2
            A Float specifying the lower bounds on the allowable scaling of the mesh in the 2
            direction. The default value is 0.0.
        ctrPosition3
            A SymbolicConstant specifying the 3-direction translational constraint on the center of
            the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.
        posPosition3
            A SymbolicConstant specifying the translational constraint on the positive (maximum)
            bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        negPosition3
            A SymbolicConstant specifying the translational constraint on the negative (minimum)
            bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        expansionRatio3
            None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
            3 direction. If **expansionRatio3** = None, then there is no upper limit. The default value
            is None.
        contractRatio3
            A Float specifying the lower bounds on the allowable scaling of the mesh in the 3
            direction. The default value is 0.0.
        allowContraction
            A Boolean specifying whether the mesh is allowed to contract . The default value is ON.
        aspectLimit
            A Float specifying the maximum change in allowed aspect ratio (for any of the three mesh
            aspects, 1-2, 2-3, 3-1). The default value is 10.0.
        vmaxFactor
            A Float specifying the multiplier for the mesh nodal velocity limit. The default value
            is 1.01.
        volThreshold
            A Float specifying the lower bounds on the volume fraction when determining which nodes
            to include in the surface bounding box calculation for an Eulerian material surface.
            This argument applies only when **followRegion** = False. The default value is 0.5.
        bufferSize
            None or a Float specifying the buffer between the surface box and the Eulerian section
            mesh bounding box. The default value is 2.0.

        Returns
        -------
        EulerianMotionBC
            An :py:class:`~abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        instanceName: str,
        followRegion: Boolean = ON,
        region: Optional[Region] = None,
        materialName: str = "",
        ctrPosition1: SymbolicConstant = FREE,
        posPosition1: SymbolicConstant = FREE,
        negPosition1: SymbolicConstant = FREE,
        expansionRatio1: Optional[float] = None,
        contractRatio1: float = 0,
        ctrPosition2: SymbolicConstant = FREE,
        posPosition2: SymbolicConstant = FREE,
        negPosition2: SymbolicConstant = FREE,
        expansionRatio2: Optional[float] = None,
        contractRatio2: float = 0,
        ctrPosition3: SymbolicConstant = FREE,
        posPosition3: SymbolicConstant = FREE,
        negPosition3: SymbolicConstant = FREE,
        expansionRatio3: Optional[float] = None,
        contractRatio3: float = 0,
        allowContraction: Boolean = ON,
        aspectLimit: float = 10,
        vmaxFactor: float = 1,
        volThreshold: float = 0,
        bufferSize: float = 2,
    ):
        """This method modifies the data for an existing EulerianMotionBC object in the step where
        it is created.

        Parameters
        ----------
        instanceName
            A String specifying the name of the Eulerian part instance.
        followRegion
            A Boolean specifying whether the mesh will follow a regular surface region or an
            Eulerian surface. The default value is ON.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
        materialName
            A String specifying the name of the Eulerian surface to follow. This argument applies
            only when **followRegion** = False.
        ctrPosition1
            A SymbolicConstant specifying the 1-direction translational constraint on the center of
            the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.
        posPosition1
            A SymbolicConstant specifying the translational constraint on the positive (maximum)
            bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        negPosition1
            A SymbolicConstant specifying the translational constraint on the negative (minimum)
            bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        expansionRatio1
            None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
            1 direction. If **expansionRatio1** = None, then there is no upper limit. The default value
            is None.
        contractRatio1
            A Float specifying the lower bounds on the allowable scaling of the mesh in the 1
            direction. The default value is 0.0.
        ctrPosition2
            A SymbolicConstant specifying the 2-direction translational constraint on the center of
            the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.
        posPosition2
            A SymbolicConstant specifying the translational constraint on the positive (maximum)
            bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        negPosition2
            A SymbolicConstant specifying the translational constraint on the negative (minimum)
            bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        expansionRatio2
            None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
            2 direction. If **expansionRatio2** = None, then there is no upper limit. The default value
            is None.
        contractRatio2
            A Float specifying the lower bounds on the allowable scaling of the mesh in the 2
            direction. The default value is 0.0.
        ctrPosition3
            A SymbolicConstant specifying the 3-direction translational constraint on the center of
            the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.
        posPosition3
            A SymbolicConstant specifying the translational constraint on the positive (maximum)
            bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        negPosition3
            A SymbolicConstant specifying the translational constraint on the negative (minimum)
            bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        expansionRatio3
            None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
            3 direction. If **expansionRatio3** = None, then there is no upper limit. The default value
            is None.
        contractRatio3
            A Float specifying the lower bounds on the allowable scaling of the mesh in the 3
            direction. The default value is 0.0.
        allowContraction
            A Boolean specifying whether the mesh is allowed to contract . The default value is ON.
        aspectLimit
            A Float specifying the maximum change in allowed aspect ratio (for any of the three mesh
            aspects, 1-2, 2-3, 3-1). The default value is 10.0.
        vmaxFactor
            A Float specifying the multiplier for the mesh nodal velocity limit. The default value
            is 1.01.
        volThreshold
            A Float specifying the lower bounds on the volume fraction when determining which nodes
            to include in the surface bounding box calculation for an Eulerian material surface.
            This argument applies only when **followRegion** = False. The default value is 0.5.
        bufferSize
            None or a Float specifying the buffer between the surface box and the Eulerian section
            mesh bounding box. The default value is 2.0.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        ctrPosition1: SymbolicConstant = FREE,
        posPosition1: SymbolicConstant = FREE,
        negPosition1: SymbolicConstant = FREE,
        expansionRatio1: Optional[float] = None,
        contractRatio1: float = 0,
        ctrPosition2: SymbolicConstant = FREE,
        posPosition2: SymbolicConstant = FREE,
        negPosition2: SymbolicConstant = FREE,
        expansionRatio2: Optional[float] = None,
        contractRatio2: float = 0,
        ctrPosition3: SymbolicConstant = FREE,
        posPosition3: SymbolicConstant = FREE,
        negPosition3: SymbolicConstant = FREE,
        expansionRatio3: Optional[float] = None,
        contractRatio3: float = 0,
        allowContraction: Boolean = ON,
        aspectLimit: float = 10,
        vmaxFactor: float = 1,
        volThreshold: float = 0,
        bufferSize: float = 2,
    ):
        """This method modifies the propagating data for an existing EulerianMotionBC object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the boundary condition is modified.
        ctrPosition1
            A SymbolicConstant specifying the 1-direction translational constraint on the center of
            the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.
        posPosition1
            A SymbolicConstant specifying the translational constraint on the positive (maximum)
            bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        negPosition1
            A SymbolicConstant specifying the translational constraint on the negative (minimum)
            bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        expansionRatio1
            None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
            1 direction. If **expansionRatio1** = None, then there is no upper limit. The default value
            is None.
        contractRatio1
            A Float specifying the lower bounds on the allowable scaling of the mesh in the 1
            direction. The default value is 0.0.
        ctrPosition2
            A SymbolicConstant specifying the 2-direction translational constraint on the center of
            the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.
        posPosition2
            A SymbolicConstant specifying the translational constraint on the positive (maximum)
            bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        negPosition2
            A SymbolicConstant specifying the translational constraint on the negative (minimum)
            bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        expansionRatio2
            None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
            2 direction. If **expansionRatio2** = None, then there is no upper limit. The default value
            is None.
        contractRatio2
            A Float specifying the lower bounds on the allowable scaling of the mesh in the 2
            direction. The default value is 0.0.
        ctrPosition3
            A SymbolicConstant specifying the 3-direction translational constraint on the center of
            the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.
        posPosition3
            A SymbolicConstant specifying the translational constraint on the positive (maximum)
            bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        negPosition3
            A SymbolicConstant specifying the translational constraint on the negative (minimum)
            bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
            value is FREE.
        expansionRatio3
            None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
            3 direction. If **expansionRatio3** = None, then there is no upper limit. The default value
            is None.
        contractRatio3
            A Float specifying the lower bounds on the allowable scaling of the mesh in the 3
            direction. The default value is 0.0.
        allowContraction
            A Boolean specifying whether the mesh is allowed to contract . The default value is ON.
        aspectLimit
            A Float specifying the maximum change in allowed aspect ratio (for any of the three mesh
            aspects, 1-2, 2-3, 3-1). The default value is 10.0.
        vmaxFactor
            A Float specifying the multiplier for the mesh nodal velocity limit. The default value
            is 1.01.
        volThreshold
            A Float specifying the lower bounds on the volume fraction when determining which nodes
            to include in the surface bounding box calculation for an Eulerian material surface.
            This argument applies only when **followRegion** = False. The default value is 0.5.
        bufferSize
            None or a Float specifying the buffer between the surface box and the Eulerian section
            mesh bounding box. The default value is 2.0.
        """
        ...
