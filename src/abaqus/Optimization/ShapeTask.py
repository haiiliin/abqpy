from typing import Dict, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .DesignResponse import DesignResponse
from .GeometricRestriction import GeometricRestriction
from .ObjectiveFunction import ObjectiveFunction
from .OptimizationConstraint import OptimizationConstraint
from .OptimizationTask import OptimizationTask
from .StopCondition import StopCondition
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class ShapeTask(OptimizationTask):
    """The ShapeTask object defines a shape task.
    The ShapeTask object is derived from the OptimizationTask object.

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

    #: A SymbolicConstant specifying whether to control the permitted absolute step size by the
    #: average optimization displacement or minimum optimization displacement. Possible values
    #: are MINIMUM and AVERAGE. The default value is MINIMUM.
    absoluteStepSizeControl: SymbolicConstant = MINIMUM

    #: A boolean specifying whether or not the durability approach of optimization is turned
    #: on. The default value is ON.
    activateDurability: Boolean = ON

    #: A String specifying the path of additional files pertaining to durability optimization.
    #: Only valid if the **activateDurability** argument is ON.
    additionalDurabilityFiles: str = ""

    #: A SymbolicConstant specifying the constrained Laplacian convergence level. Possible
    #: values are NORMAL, CONSERVATIVE, and AGGRESSIVE. The default value is NORMAL.
    constrainedLaplacianConvergenceLevel: SymbolicConstant = NORMAL

    #: A Float specifying the edge length for the movement vector. The default value is 5.0.
    curvatureSmoothingEdgeLength: float = 5

    #: A string specifying the path of the input file. Only valid if the **activateDurability**
    #: argument is ON and is a required argument in that case.
    durabilityInputfile: str = ""

    #: A String specifying the type of solver for durability optimization. Possible values are:
    #: FE_SAFE, FEMFAT, FALANCS, MSC_FATIGUE, FE_FATIGUE, DESIGN_LIFE, CUSTOM, FEMSITE. The
    #: default value is FE_SAFE. Only valid if the **activateDurability** argument is ON.
    durabilitySolver: str = FE_SAFE

    #: A Float specifying the equality constraint tolerance. The default value is 10-3.
    equalityConstraintTolerance: Optional[float] = None

    #: A Float specifying the mesh smoothing feature recognition angle for edges and corners.
    #: The default value is 30.0.
    featureRecognitionAngle: float = 30

    #: A Float specifying the weight depending on the radius, used when **filterMaxRadius** is
    #: specified. The default value is 1.0.
    filterExponent: float = 1

    #: None or a Float specifying the maximum influence radius for equivalent stress. The
    #: default value is None.
    filterMaxRadius: Optional[float] = None

    #: None or a Float specifying the reduction of the radius depending on surface bending,
    #: used when **filterMaxRadius** is specified. The default value is None.
    filterRadiusReduction: Optional[float] = None

    #: A SymbolicConstant specifying the method of specifying volume that can be removed
    #: immediately in the first design cycle. Possible values are OFF, PERCENTAGE, and
    #: ABSOLUTE. The default value is OFF.
    firstCycleDeletedVolumeTechnique: SymbolicConstant = OFF

    #: A Boolean specifying whether to exclude nodes with boundary conditions from the
    #: optimization. The default value is OFF.
    freezeBoundaryConditionRegions: Boolean = OFF

    #: The SymbolicConstant MODEL or a Region object specifying the region in which to freeze
    #: boundary condition regions, or the SymbolicConstant MODEL, used with
    #: **freezeBoundaryConditionRegions**. The default value is MODEL.
    frozenBoundaryConditionRegion: SymbolicConstant = MODEL

    #: A SymbolicConstant specifying the frequency of evaluating geometric restrictions during
    #: mesh smoothing. Possible values are LOW, MEDIUM, and HIGH. The default value is LOW.
    geometricRestrictionEvaluationFrequency: SymbolicConstant = LOW

    #: A Float specifying the scale factor to apply to optimization displacements for nodes
    #: with growth. The default value is 1.0.
    growthScaleFactor: float = 1

    #: A Boolean specifying whether to halt the optimization if quality criteria are not
    #: satisified. The default value is OFF.
    haltUponViolation: Boolean = OFF

    #: None or a Region object specifying the region specifying the first node layer for mesh
    #: smoothing, used when **meshSmoothingRegionMethod** is TASK_REGION_LAYERS. The default
    #: value is None.
    layerReferenceRegion: Optional[str] = None

    #: A SymbolicConstant specifying the method used to determine the mesh smoothing region.
    #: The REGION value uses the **smoothingRegion**. The NUMBER_OF_LAYERS value uses the
    #: **layerReferenceRegion**. The TASK_REGION_LAYERS value will smooth six layers using the
    #: task region. Possible values are TASK_REGION_LAYERS, REGION, and NUMBER_OF_LAYERS. The
    #: default value is TASK_REGION_LAYERS.
    meshSmoothingRegionMethod: SymbolicConstant = TASK_REGION_LAYERS

    #: A SymbolicConstant specifying the method smoothing strategy. Possible values are
    #: CONSTRAINED_LAPLACIAN and LOCAL_GRADIENT. The default value is CONSTRAINED_LAPLACIAN.
    meshSmoothingStrategy: SymbolicConstant = CONSTRAINED_LAPLACIAN

    #: A SymbolicConstant specifying the approach used when treating midside node positions
    #: during optimization. POSITIONS indicates midside node positions are interpolated
    #: linearly by position. OPTIMIZATION_DISPLACEMENT indicates they are interpolated by
    #: optimization displacement of corner nodes. Possible values are POSITIONS and
    #: OPTIMIZATION_DISPLACEMENT. The default value is POSITIONS.
    midsideInterpolation: SymbolicConstant = POSITIONS

    #: The SymbolicConstant FIX_NONE or an Int specifying the number of node layers adjoining
    #: the task region to remain free during mesh smoothing. A value of 0 indicates that no
    #: layers are free and all layers are fixed. The default value is 0.
    numFreeNodeLayers: SymbolicConstant = 0

    #: None or an Int specifying the number of layers for mesh smoothing when
    #: **meshSmoothingRegionMethod** is NUMBER_OF_LAYERS. The default value is None.
    numSmoothedElementLayers: Optional[int] = None

    #: A Boolean specifying whether to ignore automatically frozen boundary condition regions
    #: in the first design cycle. This is used with **freezeBoundaryConditionRegions**. The
    #: default value is ON.
    presumeFeasibleBCRegionAtStart: Boolean = ON

    #: A Float specifying the maximum angle for quad elements during mesh smoothing. The
    #: default value is 160.0.
    quadMaxAngle: float = 160

    #: A Float specifying the minimum angle for quad elements during mesh smoothing. The
    #: default value is 20.0.
    quadMinAngle: float = 20

    #: A Float specifying the skew angle for quad elements during mesh smoothing, used with
    #: **reportQualityViolation**. The default value is 30.0.
    quadSkew: float = 30

    #: A Float specifying the taper for quad elements during mesh smoothing, used with
    #: **reportQualityViolation**. The default value is 0.5.
    quadTaper: float = 0

    #: The SymbolicConstant MODEL or a Region object specifying the region to which the
    #: optimization task is applied. The default value is MODEL.
    region: SymbolicConstant = MODEL

    #: A Boolean specifying whether to report poor quality elements during mesh smoothing. The
    #: default value is OFF.
    reportPoorQualityElements: Boolean = OFF

    #: A Boolean specifying whether to report a quality criteria violation during mesh
    #: smoothing. The default value is OFF.
    reportQualityViolation: Boolean = OFF

    #: A Float specifying the scale factor to apply to optimization displacements for nodes
    #: with shrinkage. The default value is 1.0.
    shrinkScaleFactor: float = 1

    #: None or a Region object specifying the mesh smoothing region, used when
    #: **meshSmoothingRegionMethod** is REGION. The default value is None.
    smoothingRegion: Optional[str] = None

    #: A SymbolicConstant specifying the target mesh quality for mesh smoothing. Possible
    #: values are NONE, LOW, MEDIUM, and HIGH. The default value is LOW.
    targetMeshQuality: SymbolicConstant = LOW

    #: A Float specifying the tet element aspect ratio during mesh smoothing. The default value
    #: is 100.0.
    tetAspectRatio: float = 100

    #: A Float specifying the maximum tet element aspect ratio during mesh smoothing. The
    #: default value is 8.0.
    tetMaxAspect: float = 8

    #: A Float specifying the minimum tet element aspect ratio during mesh smoothing. The
    #: default value is 0.222.
    tetMinAspect: float = 0

    #: A Float specifying the tet element skew value during mesh smoothing. The default value
    #: is 100.0.
    tetSkew: float = 100

    #: A Float specifying the tri element maximum angle during mesh smoothing. The default
    #: value is 140.0.
    triMaxAngle: float = 140

    #: A Float specifying the tri element maximum angle during mesh smoothing. The default
    #: value is 20.0.
    triMinAngle: float = 20

    #: A SymbolicConstant specifying whether to update shape basis vectors in the first design
    #: cycle or every design cycle. Possible values are EVERY_CYCLE and FIRST_CYCLE. The
    #: default value is EVERY_CYCLE.
    updateShapeBasisVectors: SymbolicConstant = EVERY_CYCLE

    #: A Boolean specifying whether the group in the design response will be evaluated using
    #: the existing algorithm or a new algorithm based on Abaqus sensitivities. The default
    #: value of False means that the existing algorithm will be used.
    #:
    #: .. versionadded:: 2022
    #:     The `groupSensitivities` attribute was added.
    groupOperator: Boolean = OFF

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        abaqusSensitivities: Boolean = True,
        absoluteStepSizeControl: SymbolicConstant = MINIMUM,
        activateDurability: Boolean = ON,
        additionalDurabilityFiles: str = "",
        constrainedLaplacianConvergenceLevel: SymbolicConstant = NORMAL,
        curvatureSmoothingEdgeLength: float = 5,
        durabilityInputfile: str = "",
        durabilitySolver: str = FE_SAFE,
        equalityConstraintTolerance: Optional[float] = None,
        featureRecognitionAngle: float = 30,
        filterExponent: float = 1,
        filterMaxRadius: Optional[float] = None,
        filterRadiusReduction: Optional[float] = None,
        firstCycleDeletedVolumeTechnique: SymbolicConstant = OFF,
        freezeBoundaryConditionRegions: Boolean = OFF,
        frozenBoundaryConditionRegion: SymbolicConstant = MODEL,
        geometricRestrictionEvaluationFrequency: SymbolicConstant = LOW,
        growthScaleFactor: float = 1,
        haltUponViolation: Boolean = OFF,
        layerReferenceRegion: Optional[str] = None,
        meshSmoothingRegionMethod: SymbolicConstant = TASK_REGION_LAYERS,
        meshSmoothingStrategy: SymbolicConstant = CONSTRAINED_LAPLACIAN,
        midsideInterpolation: SymbolicConstant = POSITIONS,
        numFreeNodeLayers: SymbolicConstant = 0,
        numSmoothedElementLayers: Optional[int] = None,
        presumeFeasibleBCRegionAtStart: Boolean = ON,
        quadMaxAngle: float = 160,
        quadMinAngle: float = 20,
        quadSkew: float = 30,
        quadTaper: float = 0,
        region: SymbolicConstant = MODEL,
        reportPoorQualityElements: Boolean = OFF,
        reportQualityViolation: Boolean = OFF,
        shrinkScaleFactor: float = 1,
        smoothingRegion: Optional[str] = None,
        targetMeshQuality: SymbolicConstant = LOW,
        tetAspectRatio: float = 100,
        tetMaxAspect: float = 8,
        tetMinAspect: float = 0,
        tetSkew: float = 100,
        triMaxAngle: float = 140,
        triMinAngle: float = 20,
        updateShapeBasisVectors: SymbolicConstant = EVERY_CYCLE,
        groupOperator: Boolean = OFF,
    ):
        """This method creates a ShapeTask object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ShapeTask

        Parameters
        ----------
        name
            A String specifying the optimization task repository key.
        abaqusSensitivities
            A Boolean specifying whether to use Abaqus to compute the design responses and their
            sensitivities. The default value is True.

            .. versionadded:: 2019
                The `abaqusSensitivities` argument was added.
        absoluteStepSizeControl
            A SymbolicConstant specifying whether to control the permitted absolute step size by the
            average optimization displacement or minimum optimization displacement. Possible values
            are MINIMUM and AVERAGE. The default value is MINIMUM.
        activateDurability
            A boolean specifying whether or not the durability approach of optimization is turned
            on. The default value is ON.
        additionalDurabilityFiles
            A String specifying the path of additional files pertaining to durability optimization.
            Only valid if the **activateDurability** argument is ON.
        constrainedLaplacianConvergenceLevel
            A SymbolicConstant specifying the constrained Laplacian convergence level. Possible
            values are NORMAL, CONSERVATIVE, and AGGRESSIVE. The default value is NORMAL.
        curvatureSmoothingEdgeLength
            A Float specifying the edge length for the movement vector. The default value is 5.0.
        durabilityInputfile
            A string specifying the path of the input file. Only valid if the **activateDurability**
            argument is ON and is a required argument in that case.
        durabilitySolver
            A String specifying the type of solver for durability optimization. Possible values are:
            FE_SAFE, FEMFAT, FALANCS, MSC_FATIGUE, FE_FATIGUE, DESIGN_LIFE, CUSTOM, FEMSITE. The
            default value is FE_SAFE. Only valid if the **activateDurability** argument is ON.
        equalityConstraintTolerance
            A Float specifying the equality constraint tolerance. The default value is 10-3.
        featureRecognitionAngle
            A Float specifying the mesh smoothing feature recognition angle for edges and corners.
            The default value is 30.0.
        filterExponent
            A Float specifying the weight depending on the radius, used when **filterMaxRadius** is
            specified. The default value is 1.0.
        filterMaxRadius
            None or a Float specifying the maximum influence radius for equivalent stress. The
            default value is None.
        filterRadiusReduction
            None or a Float specifying the reduction of the radius depending on surface bending,
            used when **filterMaxRadius** is specified. The default value is None.
        firstCycleDeletedVolumeTechnique
            A SymbolicConstant specifying the method of specifying volume that can be removed
            immediately in the first design cycle. Possible values are OFF, PERCENTAGE, and
            ABSOLUTE. The default value is OFF.
        freezeBoundaryConditionRegions
            A Boolean specifying whether to exclude nodes with boundary conditions from the
            optimization. The default value is OFF.
        frozenBoundaryConditionRegion
            The SymbolicConstant MODEL or a Region object specifying the region in which to freeze
            boundary condition regions, or the SymbolicConstant MODEL, used with
            **freezeBoundaryConditionRegions**. The default value is MODEL.
        geometricRestrictionEvaluationFrequency
            A SymbolicConstant specifying the frequency of evaluating geometric restrictions during
            mesh smoothing. Possible values are LOW, MEDIUM, and HIGH. The default value is LOW.
        growthScaleFactor
            A Float specifying the scale factor to apply to optimization displacements for nodes
            with growth. The default value is 1.0.
        haltUponViolation
            A Boolean specifying whether to halt the optimization if quality criteria are not
            satisified. The default value is OFF.
        layerReferenceRegion
            None or a Region object specifying the region specifying the first node layer for mesh
            smoothing, used when **meshSmoothingRegionMethod** is TASK_REGION_LAYERS. The default
            value is None.
        meshSmoothingRegionMethod
            A SymbolicConstant specifying the method used to determine the mesh smoothing region.
            The REGION value uses the **smoothingRegion**. The NUMBER_OF_LAYERS value uses the
            **layerReferenceRegion**. The TASK_REGION_LAYERS value will smooth six layers using the
            task region. Possible values are TASK_REGION_LAYERS, REGION, and NUMBER_OF_LAYERS. The
            default value is TASK_REGION_LAYERS.
        meshSmoothingStrategy
            A SymbolicConstant specifying the method smoothing strategy. Possible values are
            CONSTRAINED_LAPLACIAN and LOCAL_GRADIENT. The default value is CONSTRAINED_LAPLACIAN.
        midsideInterpolation
            A SymbolicConstant specifying the approach used when treating midside node positions
            during optimization. POSITIONS indicates midside node positions are interpolated
            linearly by position. OPTIMIZATION_DISPLACEMENT indicates they are interpolated by
            optimization displacement of corner nodes. Possible values are POSITIONS and
            OPTIMIZATION_DISPLACEMENT. The default value is POSITIONS.
        numFreeNodeLayers
            The SymbolicConstant FIX_NONE or an Int specifying the number of node layers adjoining
            the task region to remain free during mesh smoothing. A value of 0 indicates that no
            layers are free and all layers are fixed. The default value is 0.
        numSmoothedElementLayers
            None or an Int specifying the number of layers for mesh smoothing when
            **meshSmoothingRegionMethod** is NUMBER_OF_LAYERS. The default value is None.
        presumeFeasibleBCRegionAtStart
            A Boolean specifying whether to ignore automatically frozen boundary condition regions
            in the first design cycle. This is used with **freezeBoundaryConditionRegions**. The
            default value is ON.
        quadMaxAngle
            A Float specifying the maximum angle for quad elements during mesh smoothing. The
            default value is 160.0.
        quadMinAngle
            A Float specifying the minimum angle for quad elements during mesh smoothing. The
            default value is 20.0.
        quadSkew
            A Float specifying the skew angle for quad elements during mesh smoothing, used with
            **reportQualityViolation**. The default value is 30.0.
        quadTaper
            A Float specifying the taper for quad elements during mesh smoothing, used with
            **reportQualityViolation**. The default value is 0.5.
        region
            The SymbolicConstant MODEL or a Region object specifying the region to which the
            optimization task is applied. The default value is MODEL.
        reportPoorQualityElements
            A Boolean specifying whether to report poor quality elements during mesh smoothing. The
            default value is OFF.
        reportQualityViolation
            A Boolean specifying whether to report a quality criteria violation during mesh
            smoothing. The default value is OFF.
        shrinkScaleFactor
            A Float specifying the scale factor to apply to optimization displacements for nodes
            with shrinkage. The default value is 1.0.
        smoothingRegion
            None or a Region object specifying the mesh smoothing region, used when
            **meshSmoothingRegionMethod** is REGION. The default value is None.
        targetMeshQuality
            A SymbolicConstant specifying the target mesh quality for mesh smoothing. Possible
            values are NONE, LOW, MEDIUM, and HIGH. The default value is LOW.
        tetAspectRatio
            A Float specifying the tet element aspect ratio during mesh smoothing. The default value
            is 100.0.
        tetMaxAspect
            A Float specifying the maximum tet element aspect ratio during mesh smoothing. The
            default value is 8.0.
        tetMinAspect
            A Float specifying the minimum tet element aspect ratio during mesh smoothing. The
            default value is 0.222.
        tetSkew
            A Float specifying the tet element skew value during mesh smoothing. The default value
            is 100.0.
        triMaxAngle
            A Float specifying the tri element maximum angle during mesh smoothing. The default
            value is 140.0.
        triMinAngle
            A Float specifying the tri element maximum angle during mesh smoothing. The default
            value is 20.0.
        updateShapeBasisVectors
            A SymbolicConstant specifying whether to update shape basis vectors in the first design
            cycle or every design cycle. Possible values are EVERY_CYCLE and FIRST_CYCLE. The
            default value is EVERY_CYCLE.
        groupOperator
            A Boolean specifying whether the group in the design response will be evaluated using
            the existing algorithm or a new algorithm based on Abaqus sensitivities. The default
            value of False means that the existing algorithm will be used.

            .. versionadded:: 2022
                The `groupOperator` argument was added.

        Returns
        -------
        ShapeTask
            A :py:class:`~abaqus.Optimization.ShapeTask.ShapeTask` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        abaqusSensitivities: Boolean = True,
        absoluteStepSizeControl: SymbolicConstant = MINIMUM,
        activateDurability: Boolean = ON,
        additionalDurabilityFiles: str = "",
        algorithm: SymbolicConstant = CONDITION_BASED_OPTIMIZATION,
        constrainedLaplacianConvergenceLevel: SymbolicConstant = NORMAL,
        curvatureSmoothingEdgeLength: float = 5,
        durabilityInputfile: str = "",
        durabilitySolver: str = FE_SAFE,
        equalityConstraintTolerance: Optional[float] = None,
        featureRecognitionAngle: float = 30,
        filterExponent: float = 1,
        filterMaxRadius: Optional[float] = None,
        filterRadiusReduction: Optional[float] = None,
        firstCycleDeletedVolumeTechnique: SymbolicConstant = OFF,
        freezeBoundaryConditionRegions: Boolean = OFF,
        frozenBoundaryConditionRegion: SymbolicConstant = MODEL,
        geometricRestrictionEvaluationFrequency: SymbolicConstant = LOW,
        growthScaleFactor: float = 1,
        haltUponViolation: Boolean = OFF,
        layerReferenceRegion: Optional[str] = None,
        meshSmoothingRegionMethod: SymbolicConstant = TASK_REGION_LAYERS,
        meshSmoothingStrategy: SymbolicConstant = CONSTRAINED_LAPLACIAN,
        midsideInterpolation: SymbolicConstant = POSITIONS,
        numFreeNodeLayers: SymbolicConstant = 0,
        numSmoothedElementLayers: Optional[int] = None,
        presumeFeasibleBCRegionAtStart: Boolean = ON,
        quadMaxAngle: float = 160,
        quadMinAngle: float = 20,
        quadSkew: float = 30,
        quadTaper: float = 0,
        region: SymbolicConstant = MODEL,
        reportPoorQualityElements: Boolean = OFF,
        reportQualityViolation: Boolean = OFF,
        shrinkScaleFactor: float = 1,
        smoothingRegion: Optional[str] = None,
        targetMeshQuality: SymbolicConstant = LOW,
        tetAspectRatio: float = 100,
        tetMaxAspect: float = 8,
        tetMinAspect: float = 0,
        tetSkew: float = 100,
        triMaxAngle: float = 140,
        triMinAngle: float = 20,
        updateShapeBasisVectors: SymbolicConstant = EVERY_CYCLE,
        groupOperator: Boolean = OFF,
    ):
        """This method modifies the ShapeTask object.

        Parameters
        ----------
        abaqusSensitivities
            A Boolean specifying whether to use Abaqus to compute the design responses and their
            sensitivities. The default value is True.

            .. versionadded:: 2019
                The `abaqusSensitivities` argument was added.
        absoluteStepSizeControl
            A SymbolicConstant specifying whether to control the permitted absolute step size by the
            average optimization displacement or minimum optimization displacement. Possible values
            are MINIMUM and AVERAGE. The default value is MINIMUM.
        activateDurability
            A boolean specifying whether or not the durability approach of optimization is turned
            on. The default value is ON.
        additionalDurabilityFiles
            A String specifying the path of additional files pertaining to durability optimization.
            Only valid if the **activateDurability** argument is ON.
        algorithm
            A SymbolicConstant specifying the optimization task algorithm. Possible values are
            GENERAL_OPTIMIZATION and CONDITION_BASED_OPTIMIZATION. The default value is
            CONDITION_BASED_OPTIMIZATION.
        constrainedLaplacianConvergenceLevel
            A SymbolicConstant specifying the constrained Laplacian convergence level. Possible
            values are NORMAL, CONSERVATIVE, and AGGRESSIVE. The default value is NORMAL.
        curvatureSmoothingEdgeLength
            A Float specifying the edge length for the movement vector. The default value is 5.0.
        durabilityInputfile
            A string specifying the path of the input file. Only valid if the **activateDurability**
            argument is ON and is a required argument in that case.
        durabilitySolver
            A String specifying the type of solver for durability optimization. Possible values are:
            FE_SAFE, FEMFAT, FALANCS, MSC_FATIGUE, FE_FATIGUE, DESIGN_LIFE, CUSTOM, FEMSITE. The
            default value is FE_SAFE. Only valid if the **activateDurability** argument is ON.
        equalityConstraintTolerance
            A Float specifying the equality constraint tolerance. The default value is 10-3.
        featureRecognitionAngle
            A Float specifying the mesh smoothing feature recognition angle for edges and corners.
            The default value is 30.0.
        filterExponent
            A Float specifying the weight depending on the radius, used when **filterMaxRadius** is
            specified. The default value is 1.0.
        filterMaxRadius
            None or a Float specifying the maximum influence radius for equivalent stress. The
            default value is None.
        filterRadiusReduction
            None or a Float specifying the reduction of the radius depending on surface bending,
            used when **filterMaxRadius** is specified. The default value is None.
        firstCycleDeletedVolumeTechnique
            A SymbolicConstant specifying the method of specifying volume that can be removed
            immediately in the first design cycle. Possible values are OFF, PERCENTAGE, and
            ABSOLUTE. The default value is OFF.
        freezeBoundaryConditionRegions
            A Boolean specifying whether to exclude nodes with boundary conditions from the
            optimization. The default value is OFF.
        frozenBoundaryConditionRegion
            The SymbolicConstant MODEL or a Region object specifying the region in which to freeze
            boundary condition regions, or the SymbolicConstant MODEL, used with
            **freezeBoundaryConditionRegions**. The default value is MODEL.
        geometricRestrictionEvaluationFrequency
            A SymbolicConstant specifying the frequency of evaluating geometric restrictions during
            mesh smoothing. Possible values are LOW, MEDIUM, and HIGH. The default value is LOW.
        growthScaleFactor
            A Float specifying the scale factor to apply to optimization displacements for nodes
            with growth. The default value is 1.0.
        haltUponViolation
            A Boolean specifying whether to halt the optimization if quality criteria are not
            satisified. The default value is OFF.
        layerReferenceRegion
            None or a Region object specifying the region specifying the first node layer for mesh
            smoothing, used when **meshSmoothingRegionMethod** is TASK_REGION_LAYERS. The default
            value is None.
        meshSmoothingRegionMethod
            A SymbolicConstant specifying the method used to determine the mesh smoothing region.
            The REGION value uses the **smoothingRegion**. The NUMBER_OF_LAYERS value uses the
            **layerReferenceRegion**. The TASK_REGION_LAYERS value will smooth six layers using the
            task region. Possible values are TASK_REGION_LAYERS, REGION, and NUMBER_OF_LAYERS. The
            default value is TASK_REGION_LAYERS.
        meshSmoothingStrategy
            A SymbolicConstant specifying the method smoothing strategy. Possible values are
            CONSTRAINED_LAPLACIAN and LOCAL_GRADIENT. The default value is CONSTRAINED_LAPLACIAN.
        midsideInterpolation
            A SymbolicConstant specifying the approach used when treating midside node positions
            during optimization. POSITIONS indicates midside node positions are interpolated
            linearly by position. OPTIMIZATION_DISPLACEMENT indicates they are interpolated by
            optimization displacement of corner nodes. Possible values are POSITIONS and
            OPTIMIZATION_DISPLACEMENT. The default value is POSITIONS.
        numFreeNodeLayers
            The SymbolicConstant FIX_NONE or an Int specifying the number of node layers adjoining
            the task region to remain free during mesh smoothing. A value of 0 indicates that no
            layers are free and all layers are fixed. The default value is 0.
        numSmoothedElementLayers
            None or an Int specifying the number of layers for mesh smoothing when
            **meshSmoothingRegionMethod** is NUMBER_OF_LAYERS. The default value is None.
        presumeFeasibleBCRegionAtStart
            A Boolean specifying whether to ignore automatically frozen boundary condition regions
            in the first design cycle. This is used with **freezeBoundaryConditionRegions**. The
            default value is ON.
        quadMaxAngle
            A Float specifying the maximum angle for quad elements during mesh smoothing. The
            default value is 160.0.
        quadMinAngle
            A Float specifying the minimum angle for quad elements during mesh smoothing. The
            default value is 20.0.
        quadSkew
            A Float specifying the skew angle for quad elements during mesh smoothing, used with
            **reportQualityViolation**. The default value is 30.0.
        quadTaper
            A Float specifying the taper for quad elements during mesh smoothing, used with
            **reportQualityViolation**. The default value is 0.5.
        region
            The SymbolicConstant MODEL or a Region object specifying the region to which the
            optimization task is applied. The default value is MODEL.
        reportPoorQualityElements
            A Boolean specifying whether to report poor quality elements during mesh smoothing. The
            default value is OFF.
        reportQualityViolation
            A Boolean specifying whether to report a quality criteria violation during mesh
            smoothing. The default value is OFF.
        shrinkScaleFactor
            A Float specifying the scale factor to apply to optimization displacements for nodes
            with shrinkage. The default value is 1.0.
        smoothingRegion
            None or a Region object specifying the mesh smoothing region, used when
            **meshSmoothingRegionMethod** is REGION. The default value is None.
        targetMeshQuality
            A SymbolicConstant specifying the target mesh quality for mesh smoothing. Possible
            values are NONE, LOW, MEDIUM, and HIGH. The default value is LOW.
        tetAspectRatio
            A Float specifying the tet element aspect ratio during mesh smoothing. The default value
            is 100.0.
        tetMaxAspect
            A Float specifying the maximum tet element aspect ratio during mesh smoothing. The
            default value is 8.0.
        tetMinAspect
            A Float specifying the minimum tet element aspect ratio during mesh smoothing. The
            default value is 0.222.
        tetSkew
            A Float specifying the tet element skew value during mesh smoothing. The default value
            is 100.0.
        triMaxAngle
            A Float specifying the tri element maximum angle during mesh smoothing. The default
            value is 140.0.
        triMinAngle
            A Float specifying the tri element maximum angle during mesh smoothing. The default
            value is 20.0.
        updateShapeBasisVectors
            A SymbolicConstant specifying whether to update shape basis vectors in the first design
            cycle or every design cycle. Possible values are EVERY_CYCLE and FIRST_CYCLE. The
            default value is EVERY_CYCLE.
        groupOperator
            A Boolean specifying whether the group in the design response will be evaluated using
            the existing algorithm or a new algorithm based on Abaqus sensitivities. The default
            value of False means that the existing algorithm will be used.

            .. versionadded:: 2022
                The `groupOperator` argument was added.
        """
        ...
