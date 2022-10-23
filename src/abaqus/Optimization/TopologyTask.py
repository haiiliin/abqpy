from typing import Union, Dict, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .DesignResponse import DesignResponse
from .GeometricRestriction import GeometricRestriction
from .ObjectiveFunction import ObjectiveFunction
from .OptimizationConstraint import OptimizationConstraint
from .OptimizationTask import OptimizationTask
from .StopCondition import StopCondition
from ..UtilityAndView.abaqusConstants import (AVERAGE_EDGE_LENGTH, Boolean, DEFAULT,
                                              GENERAL_OPTIMIZATION, MEDIUM, MODEL, NORMAL, OFF, ON,
                                              STANDARD, SymbolicConstant)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class TopologyTask(OptimizationTask):
    """The TopologyTask object defines a topology task.
    The TopologyTask object is derived from the OptimizationTask object.

    .. note:: 
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name]
    """

    #: A repository of DesignResponse objects.
    designResponses: Dict[str, DesignResponse] = {}

    #: A repository of ObjectiveFunction objects.
    objectiveFunctions: Dict[str, ObjectiveFunction] = {}

    #: A repository of OptimizationConstraint objects.
    optimizationConstraints: Dict[str, OptimizationConstraint] = {}

    #: A repository of GeometricRestriction objects.
    geometricRestrictions: Dict[str, GeometricRestriction] = {}

    #: A repository of StopCondition objects.
    stopConditions: Dict[str, StopCondition] = {}

    #: A String specifying the optimization task repository key.
    name: str

    #: A Boolean specifying whether to use Abaqus to compute the design responses and their
    #: sensitivities. The default value is False.
    #:
    #: .. versionadded:: 2019
    #:     The `abaqusSensitivities` attribute was added.
    abaqusSensitivities: Boolean = False

    #: A SymbolicConstant specifying the optimization task algorithm. Possible values are
    #: GENERAL_OPTIMIZATION and CONDITION_BASED_OPTIMIZATION. The default value is
    #: GENERAL_OPTIMIZATION.
    algorithm: SymbolicConstant = GENERAL_OPTIMIZATION

    #: A Float specifying the maximum density change per design cycle. The default value is
    #: 0.25.
    densityMoveLimit: float = 0

    #: A SymbolicConstant specifying the strategy for how the densities are updated in the
    #: method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and AGGRESSIVE.
    #: The default value is NORMAL.
    densityUpdateStrategy: SymbolicConstant = NORMAL

    #: A Float specifying the stop criteria based upon the change in element densities. The
    #: default value is 0.5×10-2.
    elementDensityDeltaStopCriteria: float = 0

    #: None or a Float specifying the mesh filter radius for mesh independence and minimum
    #: size. The default value is None.
    filterRadius: Optional[float] = None

    #: A Float specifying the volume that can be removed immediately in the first design cycle.
    #: The default value is 5.0.
    firstCycleDeletedVolume: float = 5

    #: A SymbolicConstant specifying the method of quantifying volume that can be removed
    #: immediately in the first design cycle. Possible values are OFF, PERCENTAGE, and
    #: ABSOLUTE. The default value is OFF.
    firstCycleDeletedVolumeTechnique: Union[SymbolicConstant, Boolean] = OFF

    #: A Boolean specifying whether to exclude elements with boundary conditions from the
    #: optimization. The default value is OFF.
    freezeBoundaryConditionRegions: Boolean = OFF

    #: A Boolean specifying whether to exclude elements with loads and elements with loaded
    #: nodes from the optimization. The default value is ON.
    freezeLoadRegions: Boolean = ON

    #: A Float specifying the weighting factor for frequency spectrum peaks. The default value
    #: is 6.0.
    frequencySpectrumWeight: float = 6

    #: A SymbolicConstant specifying the Optimization product default or a float specifying the
    #: initial density. The default value is DEFAULT.
    initialDensity: SymbolicConstant = DEFAULT

    #: A Float specifying the penalty factor for the material interpolation technique. The
    #: default value is 3.0.
    materialInterpolationPenalty: float = 3

    #: A SymbolicConstant specifying the material interpolation technique: optimization product
    #: default, solid isotropic material with penalization, or rational approximation of
    #: material properties. Possible values are DEFAULT, SIMP, and RAMP. The default value is
    #: DEFAULT.
    materialInterpolationTechnique: SymbolicConstant = DEFAULT

    #: A Float specifying the maximum density in the density update. The default value is 1.0.
    maxDensity: float = 1

    #: A Float specifying the minimum density in the density update. The default value is 10-3.
    minDensity: Optional[float] = None

    #: The SymbolicConstant MODEL or a Region object specifying the region to use for mode
    #: tracking. The default value is MODEL.
    modeTrackingRegion: SymbolicConstant = MODEL

    #: An Int specifying the number of design cycles permitted when **stepSize** is DYNAMIC. The
    #: default value is 15.
    numDesignCycles: int = 15

    #: An Int specifying the number of stop criteria. The default value is 2.
    numFulfilledStopCriteria: int = 2

    #: An Int specifying the number of modes included in mode tracking. The default value is 5.
    numTrackedModes: int = 5

    #: A Float specifying the stop criteria based on the change in objective function. The
    #: default value is 10-3.
    objectiveFunctionDeltaStopCriteria: Optional[float] = None

    #: The SymbolicConstant MODEL or a Region object specifying the region to which the
    #: optimization task is applied. The default value is MODEL.
    region: SymbolicConstant = MODEL

    #: A SymbolicConstant specifying the method used when **softDeletionRegion** is specified.
    #: The STANDARD method avoids creating disconnected regions. The AGGRESSIVE method only
    #: considers the **softDeletionThreshold**. The MAX_SHEAR_STRAIN, MAX_ELASTOPLASTIC_STRAIN
    #: and VOLUME_COMPRESSION methods do not need the **softDeletionRadius**. Possible values are
    #: STANDARD, AGGRESSIVE, MAX_SHEAR_STRAIN, MIN_PRINCIPAL_STRAIN, MAX_ELASTOPLASTIC_STRAIN
    #: and VOLUME_COMPRESSION. The default value is STANDARD.
    softDeletionMethod: SymbolicConstant = STANDARD

    #: A Float specifying the radius to use when considering neighboring soft elements to
    #: delete. The default value is 0.0.
    softDeletionRadius: float = 0

    #: None or a Region object specifying the region in which the soft elements should be
    #: deleted during optimization. The default value is None.
    softDeletionRegion: Optional[str] = None

    #: A Float specifying the relative material density value used to identify soft elements.
    #: Those with values below the threshold are considered for removal. For STANDARD and
    #: AGGRESSIVE methods positive values are accepted and the default value is 0.05. For
    #: MAX_SHEAR_STRAIN and MAX_ELASTOPLASTIC_STRAIN methods positive values are accepted
    #: whereas for MIN_PRINCIPAL_STRAIN and VOLUME_COMPRESSION methods negative values are
    #: accepted.
    softDeletionThreshold: Optional[float] = None

    #: A SymbolicConstant specifying the size of the increment for volume modification.
    #: Possible values are DYNAMIC, VERY_SMALL, SMALL, MODERATE, MEDIUM, and LARGE. The default
    #: value is MEDIUM.
    stepSize: SymbolicConstant = MEDIUM

    #: The SymbolicConstant AVERAGE_EDGE_LENGTH or a Float specifying the stiffness mass
    #: damping for the task region. The default value is AVERAGE_EDGE_LENGTH.
    stiffnessMassDamping: Union[SymbolicConstant, float] = AVERAGE_EDGE_LENGTH

    #: An Int specifying the first design cycle used to evaluate convergence criteria. The
    #: default value is 4.
    stopCriteriaDesignCycle: int = 4

    #: None or a Float specifying the structural mass damping for the task region. The default
    #: value is None.
    structuralMassDamping: Optional[float] = None

    #: None or a Float specifying the viscous mass damping for the task region. The default
    #: value is None.
    viscousMassDamping: Optional[float] = None

    #: None or a Float specifying the viscous stiffness damping for the task region. The
    #: default value is None.
    viscousStiffnessDamping: Optional[float] = None

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        abaqusSensitivities: Boolean = False,
        algorithm: Literal[C.CONDITION_BASED_OPTIMIZATION, C.GENERAL_OPTIMIZATION] = GENERAL_OPTIMIZATION,
        densityMoveLimit: float = 0,
        densityUpdateStrategy: Literal[C.AGGRESSIVE, C.NORMAL, C.CONSERVATIVE] = NORMAL,
        elementDensityDeltaStopCriteria: float = 0,
        filterRadius: Optional[float] = None,
        firstCycleDeletedVolume: float = 5,
        firstCycleDeletedVolumeTechnique: Union[Literal[C.PERCENTAGE, C.ABSOLUTE], Boolean] = OFF,
        freezeBoundaryConditionRegions: Boolean = OFF,
        freezeLoadRegions: Boolean = ON,
        frequencySpectrumWeight: float = 6,
        initialDensity: Literal[C.DEFAULT] = DEFAULT,
        materialInterpolationPenalty: float = 3,
        materialInterpolationTechnique: Literal[C.SIMP, C.DEFAULT, C.RAMP] = DEFAULT,
        maxDensity: float = 1,
        minDensity: Optional[float] = None,
        modeTrackingRegion: Literal[C.MODEL] = MODEL,
        numDesignCycles: int = 15,
        numFulfilledStopCriteria: int = 2,
        numTrackedModes: int = 5,
        objectiveFunctionDeltaStopCriteria: Optional[float] = None,
        region: Literal[C.MODEL] = MODEL,
        softDeletionMethod: Literal[C.STANDARD, C.VOLUME_COMPRESSION, C.MAX_SHEAR_STRAIN, C.AGGRESSIVE, C.MIN_PRINCIPAL_STRAIN, C.MAX_ELASTOPLASTIC_STRAIN] = STANDARD,
        softDeletionRadius: float = 0,
        softDeletionRegion: Optional[str] = None,
        softDeletionThreshold: Optional[float] = None,
        stepSize: Literal[C.SMALL, C.LARGE, C.MODERATE, C.VERY_SMALL, C.DYNAMIC, C.MEDIUM] = MEDIUM,
        stiffnessMassDamping: Union[
            Literal[C.AVERAGE_EDGE_LENGTH], float
        ] = AVERAGE_EDGE_LENGTH,
        stopCriteriaDesignCycle: int = 4,
        structuralMassDamping: Optional[float] = None,
        viscousMassDamping: Optional[float] = None,
        viscousStiffnessDamping: Optional[float] = None,
    ):
        """This method creates a TopologyTask object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].TopologyTask

        Parameters
        ----------
        name
            A String specifying the optimization task repository key.
        abaqusSensitivities
            A Boolean specifying whether to use Abaqus to compute the design responses and their
            sensitivities. The default value is False.

            .. versionadded:: 2019
                The `abaqusSensitivities` argument was added.
        algorithm
            A SymbolicConstant specifying the optimization task algorithm. Possible values are
            GENERAL_OPTIMIZATION and CONDITION_BASED_OPTIMIZATION. The default value is
            GENERAL_OPTIMIZATION.
        densityMoveLimit
            A Float specifying the maximum density change per design cycle. The default value is
            0.25.
        densityUpdateStrategy
            A SymbolicConstant specifying the strategy for how the densities are updated in the
            method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and AGGRESSIVE.
            The default value is NORMAL.
        elementDensityDeltaStopCriteria
            A Float specifying the stop criteria based upon the change in element densities. The
            default value is 0.5×10-2.
        filterRadius
            None or a Float specifying the mesh filter radius for mesh independence and minimum
            size. The default value is None.
        firstCycleDeletedVolume
            A Float specifying the volume that can be removed immediately in the first design cycle.
            The default value is 5.0.
        firstCycleDeletedVolumeTechnique
            A SymbolicConstant specifying the method of quantifying volume that can be removed
            immediately in the first design cycle. Possible values are OFF, PERCENTAGE, and
            ABSOLUTE. The default value is OFF.
        freezeBoundaryConditionRegions
            A Boolean specifying whether to exclude elements with boundary conditions from the
            optimization. The default value is OFF.
        freezeLoadRegions
            A Boolean specifying whether to exclude elements with loads and elements with loaded
            nodes from the optimization. The default value is ON.
        frequencySpectrumWeight
            A Float specifying the weighting factor for frequency spectrum peaks. The default value
            is 6.0.
        initialDensity
            A SymbolicConstant specifying the Optimization product default or a float specifying the
            initial density. The default value is DEFAULT.
        materialInterpolationPenalty
            A Float specifying the penalty factor for the material interpolation technique. The
            default value is 3.0.
        materialInterpolationTechnique
            A SymbolicConstant specifying the material interpolation technique: optimization product
            default, solid isotropic material with penalization, or rational approximation of
            material properties. Possible values are DEFAULT, SIMP, and RAMP. The default value is
            DEFAULT.
        maxDensity
            A Float specifying the maximum density in the density update. The default value is 1.0.
        minDensity
            A Float specifying the minimum density in the density update. The default value is 10-3.
        modeTrackingRegion
            The SymbolicConstant MODEL or a Region object specifying the region to use for mode
            tracking. The default value is MODEL.
        numDesignCycles
            An Int specifying the number of design cycles permitted when **stepSize** is DYNAMIC. The
            default value is 15.
        numFulfilledStopCriteria
            An Int specifying the number of stop criteria. The default value is 2.
        numTrackedModes
            An Int specifying the number of modes included in mode tracking. The default value is 5.
        objectiveFunctionDeltaStopCriteria
            A Float specifying the stop criteria based on the change in objective function. The
            default value is 10-3.
        region
            The SymbolicConstant MODEL or a Region object specifying the region to which the
            optimization task is applied. The default value is MODEL.
        softDeletionMethod
            A SymbolicConstant specifying the method used when **softDeletionRegion** is specified.
            The STANDARD method avoids creating disconnected regions. The AGGRESSIVE method only
            considers the **softDeletionThreshold**. The MAX_SHEAR_STRAIN, MAX_ELASTOPLASTIC_STRAIN
            and VOLUME_COMPRESSION methods do not need the **softDeletionRadius**. Possible values are
            STANDARD, AGGRESSIVE, MAX_SHEAR_STRAIN, MIN_PRINCIPAL_STRAIN, MAX_ELASTOPLASTIC_STRAIN
            and VOLUME_COMPRESSION. The default value is STANDARD.
        softDeletionRadius
            A Float specifying the radius to use when considering neighboring soft elements to
            delete. The default value is 0.0.
        softDeletionRegion
            None or a Region object specifying the region in which the soft elements should be
            deleted during optimization. The default value is None.
        softDeletionThreshold
            A Float specifying the relative material density value used to identify soft elements.
            Those with values below the threshold are considered for removal. For STANDARD and
            AGGRESSIVE methods positive values are accepted and the default value is 0.05. For
            MAX_SHEAR_STRAIN and MAX_ELASTOPLASTIC_STRAIN methods positive values are accepted
            whereas for MIN_PRINCIPAL_STRAIN and VOLUME_COMPRESSION methods negative values are
            accepted.
        stepSize
            A SymbolicConstant specifying the size of the increment for volume modification.
            Possible values are DYNAMIC, VERY_SMALL, SMALL, MODERATE, MEDIUM, and LARGE. The default
            value is MEDIUM.
        stiffnessMassDamping
            The SymbolicConstant AVERAGE_EDGE_LENGTH or a Float specifying the stiffness mass
            damping for the task region. The default value is AVERAGE_EDGE_LENGTH.
        stopCriteriaDesignCycle
            An Int specifying the first design cycle used to evaluate convergence criteria. The
            default value is 4.
        structuralMassDamping
            None or a Float specifying the structural mass damping for the task region. The default
            value is None.
        viscousMassDamping
            None or a Float specifying the viscous mass damping for the task region. The default
            value is None.
        viscousStiffnessDamping
            None or a Float specifying the viscous stiffness damping for the task region. The
            default value is None.

        Returns
        -------
        TopologyTask
            A :py:class:`~abaqus.Optimization.TopologyTask.TopologyTask` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        abaqusSensitivities: Boolean = True,
        algorithm: Literal[C.CONDITION_BASED_OPTIMIZATION, C.GENERAL_OPTIMIZATION] = GENERAL_OPTIMIZATION,
        densityMoveLimit: float = 0,
        densityUpdateStrategy: Literal[C.AGGRESSIVE, C.NORMAL, C.CONSERVATIVE] = NORMAL,
        elementDensityDeltaStopCriteria: float = 0,
        filterRadius: Optional[float] = None,
        firstCycleDeletedVolume: float = 5,
        firstCycleDeletedVolumeTechnique: Union[Literal[C.PERCENTAGE, C.ABSOLUTE], Boolean] = OFF,
        freezeBoundaryConditionRegions: Boolean = OFF,
        freezeLoadRegions: Boolean = ON,
        frequencySpectrumWeight: float = 6,
        initialDensity: Literal[C.DEFAULT] = DEFAULT,
        materialInterpolationPenalty: float = 3,
        materialInterpolationTechnique: Literal[C.SIMP, C.DEFAULT, C.RAMP] = DEFAULT,
        maxDensity: float = 1,
        minDensity: Optional[float] = None,
        modeTrackingRegion: Literal[C.MODEL] = MODEL,
        numDesignCycles: int = 15,
        numFulfilledStopCriteria: int = 2,
        numTrackedModes: int = 5,
        objectiveFunctionDeltaStopCriteria: Optional[float] = None,
        region: Literal[C.MODEL] = MODEL,
        softDeletionMethod: Literal[C.STANDARD, C.VOLUME_COMPRESSION, C.MAX_SHEAR_STRAIN, C.AGGRESSIVE, C.MIN_PRINCIPAL_STRAIN, C.MAX_ELASTOPLASTIC_STRAIN] = STANDARD,
        softDeletionRadius: float = 0,
        softDeletionRegion: Optional[str] = None,
        softDeletionThreshold: Optional[float] = None,
        stepSize: Literal[C.SMALL, C.LARGE, C.MODERATE, C.VERY_SMALL, C.DYNAMIC, C.MEDIUM] = MEDIUM,
        stiffnessMassDamping: Union[
            Literal[C.AVERAGE_EDGE_LENGTH], float
        ] = AVERAGE_EDGE_LENGTH,
        stopCriteriaDesignCycle: int = 4,
        structuralMassDamping: Optional[float] = None,
        viscousMassDamping: Optional[float] = None,
        viscousStiffnessDamping: Optional[float] = None,
    ):
        """This method modifies the TopologyTask object.

        Parameters
        ----------
        abaqusSensitivities
            A Boolean specifying whether to use Abaqus to compute the design responses and their
            sensitivities. The default value is True.

            .. versionadded:: 2019
                The `abaqusSensitivities` argument was added.
        algorithm
            A SymbolicConstant specifying the optimization task algorithm. Possible values are
            GENERAL_OPTIMIZATION and CONDITION_BASED_OPTIMIZATION. The default value is
            GENERAL_OPTIMIZATION.
        densityMoveLimit
            A Float specifying the maximum density change per design cycle. The default value is
            0.25.
        densityUpdateStrategy
            A SymbolicConstant specifying the strategy for how the densities are updated in the
            method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and AGGRESSIVE.
            The default value is NORMAL.
        elementDensityDeltaStopCriteria
            A Float specifying the stop criteria based upon the change in element densities. The
            default value is 0.5×10-2.
        filterRadius
            None or a Float specifying the mesh filter radius for mesh independence and minimum
            size. The default value is None.
        firstCycleDeletedVolume
            A Float specifying the volume that can be removed immediately in the first design cycle.
            The default value is 5.0.
        firstCycleDeletedVolumeTechnique
            A SymbolicConstant specifying the method of quantifying volume that can be removed
            immediately in the first design cycle. Possible values are OFF, PERCENTAGE, and
            ABSOLUTE. The default value is OFF.
        freezeBoundaryConditionRegions
            A Boolean specifying whether to exclude elements with boundary conditions from the
            optimization. The default value is OFF.
        freezeLoadRegions
            A Boolean specifying whether to exclude elements with loads and elements with loaded
            nodes from the optimization. The default value is ON.
        frequencySpectrumWeight
            A Float specifying the weighting factor for frequency spectrum peaks. The default value
            is 6.0.
        initialDensity
            A SymbolicConstant specifying the Optimization product default or a float specifying the
            initial density. The default value is DEFAULT.
        materialInterpolationPenalty
            A Float specifying the penalty factor for the material interpolation technique. The
            default value is 3.0.
        materialInterpolationTechnique
            A SymbolicConstant specifying the material interpolation technique: optimization product
            default, solid isotropic material with penalization, or rational approximation of
            material properties. Possible values are DEFAULT, SIMP, and RAMP. The default value is
            DEFAULT.
        maxDensity
            A Float specifying the maximum density in the density update. The default value is 1.0.
        minDensity
            A Float specifying the minimum density in the density update. The default value is 10-3.
        modeTrackingRegion
            The SymbolicConstant MODEL or a Region object specifying the region to use for mode
            tracking. The default value is MODEL.
        numDesignCycles
            An Int specifying the number of design cycles permitted when **stepSize** is DYNAMIC. The
            default value is 15.
        numFulfilledStopCriteria
            An Int specifying the number of stop criteria. The default value is 2.
        numTrackedModes
            An Int specifying the number of modes included in mode tracking. The default value is 5.
        objectiveFunctionDeltaStopCriteria
            A Float specifying the stop criteria based on the change in objective function. The
            default value is 10-3.
        region
            The SymbolicConstant MODEL or a Region object specifying the region to which the
            optimization task is applied. The default value is MODEL.
        softDeletionMethod
            A SymbolicConstant specifying the method used when **softDeletionRegion** is specified.
            The STANDARD method avoids creating disconnected regions. The AGGRESSIVE method only
            considers the **softDeletionThreshold**. The MAX_SHEAR_STRAIN, MAX_ELASTOPLASTIC_STRAIN
            and VOLUME_COMPRESSION methods do not need the **softDeletionRadius**. Possible values are
            STANDARD, AGGRESSIVE, MAX_SHEAR_STRAIN, MIN_PRINCIPAL_STRAIN, MAX_ELASTOPLASTIC_STRAIN
            and VOLUME_COMPRESSION. The default value is STANDARD.
        softDeletionRadius
            A Float specifying the radius to use when considering neighboring soft elements to
            delete. The default value is 0.0.
        softDeletionRegion
            None or a Region object specifying the region in which the soft elements should be
            deleted during optimization. The default value is None.
        softDeletionThreshold
            A Float specifying the relative material density value used to identify soft elements.
            Those with values below the threshold are considered for removal. For STANDARD and
            AGGRESSIVE methods positive values are accepted and the default value is 0.05. For
            MAX_SHEAR_STRAIN and MAX_ELASTOPLASTIC_STRAIN methods positive values are accepted
            whereas for MIN_PRINCIPAL_STRAIN and VOLUME_COMPRESSION methods negative values are
            accepted.
        stepSize
            A SymbolicConstant specifying the size of the increment for volume modification.
            Possible values are DYNAMIC, VERY_SMALL, SMALL, MODERATE, MEDIUM, and LARGE. The default
            value is MEDIUM.
        stiffnessMassDamping
            The SymbolicConstant AVERAGE_EDGE_LENGTH or a Float specifying the stiffness mass
            damping for the task region. The default value is AVERAGE_EDGE_LENGTH.
        stopCriteriaDesignCycle
            An Int specifying the first design cycle used to evaluate convergence criteria. The
            default value is 4.
        structuralMassDamping
            None or a Float specifying the structural mass damping for the task region. The default
            value is None.
        viscousMassDamping
            None or a Float specifying the viscous mass damping for the task region. The default
            value is None.
        viscousStiffnessDamping
            None or a Float specifying the viscous stiffness damping for the task region. The
            default value is None.
        """
        ...
