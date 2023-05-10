from typing import Optional, Union

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Model.ModelBase import ModelBase
from ..UtilityAndView.abaqusConstants import (
    AVERAGE_EDGE_LENGTH,
    CONSERVATIVE,
    CONSTRAINED_LAPLACIAN,
    DEFAULT,
    EVERY_CYCLE,
    FE_SAFE,
    GENERAL_OPTIMIZATION,
    LOW,
    MEDIUM,
    MINIMUM,
    MODEL,
    NORMAL,
    OFF,
    ON,
    POSITIONS,
    STANDARD,
    TASK_REGION_LAYERS,
    VALUE,
    Boolean,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .BeadTask import BeadTask
from .ShapeTask import ShapeTask
from .SizingTask import SizingTask
from .TopologyTask import TopologyTask


@abaqus_class_doc
class OptimizationTaskModel(ModelBase):
    """Abaqus creates a Model object named `Model-1` when a session is started.

    .. note::
        This object can be accessed by::

            mdb.models[name]
    """

    @abaqus_method_doc
    def BeadTask(
        self,
        name: str,
        abaqusSensitivities: Boolean = True,
        algorithm: Literal[C.CONDITION_BASED_OPTIMIZATION, C.GENERAL_OPTIMIZATION] = GENERAL_OPTIMIZATION,
        areBCRegionsFrozen: Boolean = OFF,
        beadIter: str = 1,
        beadMaxMembraneStress: str = 0,
        beadMinStress: str = 0,
        beadPerturbation: str = 0,
        beadWidth: Literal[C.DEFAULT] = DEFAULT,
        curveSmooth: str = 5,
        filterRadius: str = 4,
        filterRadiusBy: Literal[C.VALUE, C.REFERENCE] = VALUE,
        flipNormalDir: Boolean = OFF,
        frozenBoundaryConditionRegion: Literal[C.MODEL] = MODEL,
        isSensCalcOnlyOnDesignNodes: Boolean = OFF,
        modeTrackingRegion: Literal[C.MODEL] = MODEL,
        nodalMoveLimit: float = 0,
        nodeSmooth: Literal[C.DEFAULT] = DEFAULT,
        nodeUpdateStrategy: Literal[C.AGGRESSIVE, C.NORMAL, C.CONSERVATIVE] = CONSERVATIVE,
        numTrackedModes: int = 5,
        updateShapeBasisVectors: Literal[C.EVERY_CYCLE, C.FIRST_CYCLE] = EVERY_CYCLE,
    ) -> BeadTask:
        """This method creates a BeadTask object.

        .. note::
            This function can be accessed by::

                mdb.models[name].BeadTask

        Parameters
        ----------
        name
            A String specifying the optimization task repository key.
        abaqusSensitivities
            A Boolean specifying whether to use Abaqus to compute the design responses and their
            sensitivities. The default value is True.

            .. versionadded:: 2019
                The ``abaqusSensitivities`` argument was added.
        algorithm
            A SymbolicConstant specifying the optimization task algorithm. Possible values are
            GENERAL_OPTIMIZATION and CONDITION_BASED_OPTIMIZATION. The default value is
            GENERAL_OPTIMIZATION.
        areBCRegionsFrozen
            A Boolean specifying whether to exclude elements with boundary conditions from the
            optimization. The default value is OFF.
        beadIter
            An int specifying the step size of the optimization. The default value is 1.
        beadMaxMembraneStress
            A float specifying maximum membrane/bending stress. The default value is 0.1.
        beadMinStress
            A float specifying minimum stress. The default value is 0.001.
        beadPerturbation
            A Sets perturbation size for finite differences. The default value is 0.0001.
        beadWidth
            A SymbolicConstant specifying the Optimization product default or a float specifying the
            bead width. The default value is DEFAULT.
        curveSmooth
            A float specifying relative value to the middle element edge length such that normals in
            this area do not cross each other. The default value is 5.
        filterRadius
            A float specifying the filter radius. The default value is 4.
        filterRadiusBy
            A SymbolicConstant specifying the method used to define filter radius. Possible values
            are VALUE and REFERENCE. The default is VALUE.
        flipNormalDir
            A Boolean specifying whether the growth direction is along the normal direction of
            elements or opposite to the normal direction. The default value is OFF
        frozenBoundaryConditionRegion
            When nodes with boundary conditions are excluded from the optimization
            (*frozenBoundaryConditionRegions* = ON). you can specify that this exclusion apply to
            nodes throughout the model or only to those nodes from a specific region. Set this
            parameter to the SymbolicConstant MODEL to apply the freeze to the entire model, or set
            this parameter to a Region object to specify an individual region over which nodes with
            boundary conditions should be frozen. The default value is MODEL.
        isSensCalcOnlyOnDesignNodes
            A Boolean specifying whether to calculate the sensitivities only on design nodes or the
            whole model. The default value is ON
        modeTrackingRegion
            The SymbolicConstant MODEL or a Region object specifying the region to use for mode
            tracking. The default value is MODEL.
        nodalMoveLimit
            A Float specifying the maximum change in nodal displacement per design cycle. The
            default value is 0.1.
        nodeSmooth
            A SymbolicConstant specifying the Optimization product default or a float specifying the
            node smooth. The default value is DEFAULT.
        nodeUpdateStrategy
            A SymbolicConstant specifying the strategy for how the nodal displacements are updated
            in the method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and
            AGGRESSIVE. The default value is CONSERVATIVE.
        numTrackedModes
            An Int specifying the number of modes included in mode tracking. The default value is 5.
        updateShapeBasisVectors
            A SymbolicConstant specifying whether to update shape basis vectors in the first design
            cycle or every design cycle. Possible values are EVERY_CYCLE and FIRST_CYCLE. The
            default value is EVERY_CYCLE.

        Returns
        -------
        BeadTask
            A BeadTask object.
        """
        self.optimizationTasks[name] = optimizationTask = BeadTask(
            name,
            abaqusSensitivities,
            algorithm,
            areBCRegionsFrozen,
            beadIter,
            beadMaxMembraneStress,
            beadMinStress,
            beadPerturbation,
            beadWidth,
            curveSmooth,
            filterRadius,
            filterRadiusBy,
            flipNormalDir,
            frozenBoundaryConditionRegion,
            isSensCalcOnlyOnDesignNodes,
            modeTrackingRegion,
            nodalMoveLimit,
            nodeSmooth,
            nodeUpdateStrategy,
            numTrackedModes,
            updateShapeBasisVectors,
        )
        return optimizationTask

    @abaqus_method_doc
    def ShapeTask(
        self,
        name: str,
        abaqusSensitivities: Boolean = True,
        absoluteStepSizeControl: Literal[C.MINIMUM, C.AVERAGE] = MINIMUM,
        activateDurability: Boolean = ON,
        additionalDurabilityFiles: str = "",
        constrainedLaplacianConvergenceLevel: Literal[C.AGGRESSIVE, C.NORMAL, C.CONSERVATIVE] = NORMAL,
        curvatureSmoothingEdgeLength: float = 5,
        durabilityInputfile: str = "",
        durabilitySolver: str = FE_SAFE,
        equalityConstraintTolerance: Optional[float] = None,
        featureRecognitionAngle: float = 30,
        filterExponent: float = 1,
        filterMaxRadius: Optional[float] = None,
        filterRadiusReduction: Optional[float] = None,
        firstCycleDeletedVolumeTechnique: Union[Literal[C.PERCENTAGE, C.ABSOLUTE], Boolean] = OFF,
        freezeBoundaryConditionRegions: Boolean = OFF,
        frozenBoundaryConditionRegion: Literal[C.MODEL] = MODEL,
        geometricRestrictionEvaluationFrequency: Literal[C.LOW, C.MEDIUM, C.HIGH] = LOW,
        growthScaleFactor: float = 1,
        haltUponViolation: Boolean = OFF,
        layerReferenceRegion: Optional[str] = None,
        meshSmoothingRegionMethod: Literal[C.NUMBER_OF_LAYERS, C.REGION, C.TASK_REGION_LAYERS] = TASK_REGION_LAYERS,
        meshSmoothingStrategy: Literal[C.CONSTRAINED_LAPLACIAN, C.LOCAL_GRADIENT] = CONSTRAINED_LAPLACIAN,
        midsideInterpolation: Literal[C.POSITIONS, C.OPTIMIZATION_DISPLACEMENT] = POSITIONS,
        numFreeNodeLayers: Literal[C.FIX_NONE] = 0,
        numSmoothedElementLayers: Optional[int] = None,
        presumeFeasibleBCRegionAtStart: Boolean = ON,
        quadMaxAngle: float = 160,
        quadMinAngle: float = 20,
        quadSkew: float = 30,
        quadTaper: float = 0,
        region: Literal[C.MODEL] = MODEL,
        reportPoorQualityElements: Boolean = OFF,
        reportQualityViolation: Boolean = OFF,
        shrinkScaleFactor: float = 1,
        smoothingRegion: Optional[str] = None,
        targetMeshQuality: Literal[C.LOW, C.MEDIUM, C.NONE, C.HIGH] = LOW,
        tetAspectRatio: float = 100,
        tetMaxAspect: float = 8,
        tetMinAspect: float = 0,
        tetSkew: float = 100,
        triMaxAngle: float = 140,
        triMinAngle: float = 20,
        updateShapeBasisVectors: Literal[C.EVERY_CYCLE, C.FIRST_CYCLE] = EVERY_CYCLE,
    ) -> ShapeTask:
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
                The ``abaqusSensitivities`` argument was added.
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
            FE_SAFE, FEMFAT, FLANS, MSC_FATIGUE, FE_FATIGUE, DESIGN_LIFE, CUSTOM, FEMSITE. The
            default value is FE_SAFE. Only valid if the **activateDurability** argument is ON.
        equalityConstraintTolerance
            A Float specifying the equality constraint tolerance. The default value is 10⁻³.
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

        Returns
        -------
        ShapeTask
            A ShapeTask object.
        """
        self.optimizationTasks[name] = optimizationTask = ShapeTask(
            name,
            abaqusSensitivities,
            absoluteStepSizeControl,
            activateDurability,
            additionalDurabilityFiles,
            constrainedLaplacianConvergenceLevel,
            curvatureSmoothingEdgeLength,
            durabilityInputfile,
            durabilitySolver,
            equalityConstraintTolerance,
            featureRecognitionAngle,
            filterExponent,
            filterMaxRadius,
            filterRadiusReduction,
            firstCycleDeletedVolumeTechnique,
            freezeBoundaryConditionRegions,
            frozenBoundaryConditionRegion,
            geometricRestrictionEvaluationFrequency,
            growthScaleFactor,
            haltUponViolation,
            layerReferenceRegion,
            meshSmoothingRegionMethod,
            meshSmoothingStrategy,
            midsideInterpolation,
            numFreeNodeLayers,
            numSmoothedElementLayers,
            presumeFeasibleBCRegionAtStart,
            quadMaxAngle,
            quadMinAngle,
            quadSkew,
            quadTaper,
            region,
            reportPoorQualityElements,
            reportQualityViolation,
            shrinkScaleFactor,
            smoothingRegion,
            targetMeshQuality,
            tetAspectRatio,
            tetMaxAspect,
            tetMinAspect,
            tetSkew,
            triMaxAngle,
            triMinAngle,
            updateShapeBasisVectors,
        )
        return optimizationTask

    @abaqus_method_doc
    def SizingTask(
        self,
        name: str,
        abaqusSensitivities: Boolean = True,
        elementThicknessDeltaStopCriteria: float = 0,
        freezeBoundaryConditionRegions: Boolean = OFF,
        freezeLoadRegions: Boolean = ON,
        modeTrackingRegion: str = MODEL,
        numFulfilledStopCriteria: int = 2,
        numTrackedModes: int = 5,
        objectiveFunctionDeltaStopCriteria: float = 0,
        stopCriteriaDesignCycle: int = 4,
        thicknessMoveLimit: float = 0,
        thicknessUpdateStrategy: Literal[C.AGGRESSIVE, C.NORMAL, C.CONSERVATIVE] = NORMAL,
    ) -> SizingTask:
        """This method creates a SizingTask object.

        .. note::
            This function can be accessed by::

                mdb.models[name].SizingTask

        Parameters
        ----------
        name
            A String specifying the optimization task repository key.
        abaqusSensitivities
            A Boolean specifying whether to use Abaqus to compute the design responses and their
            sensitivities. The default value is True.

            .. versionadded:: 2019
                The ``abaqusSensitivities`` argument was added.
        elementThicknessDeltaStopCriteria
            A Float specifying the stop criteria based on the change in element thickness. The
            default value is 0.5 x 10⁻².
        freezeBoundaryConditionRegions
            A Boolean specifying whether to exclude elements with boundary conditions from the
            optimization. The default value is OFF.
        freezeLoadRegions
            A Boolean specifying whether to exclude elements with loads and elements with loaded
            nodes from the optimization. The default value is ON.
        modeTrackingRegion
            The SymbolicConstatnt MODEL or a Region object specifying the region to use for mode
            tracking. The default value is MODEL.
        numFulfilledStopCriteria
            An Int specifying the number of stop criteria. The default value is 2.
        numTrackedModes
            An Int specifying the number of modes included in mode tracking. The default value is 5.
        objectiveFunctionDeltaStopCriteria
            A Float specifying the stop criteria based on the change in objective function. The
            default value is 0.001.
        stopCriteriaDesignCycle
            An Int specifying the first design cycle used to evaluate convergence criteria. The
            default value is 4.
        thicknessMoveLimit
            A Float specifying the maximum change in thickness per design cycle. The default value
            is 0.25.
        thicknessUpdateStrategy
            A SymbolicConstant specifying the strategy for how the thickness is updated in the
            method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and AGGRESSIVE.
            The default value is NORMAL.

        Returns
        -------
        SizingTask
            A SizingTask object.
        """
        self.optimizationTasks[name] = optimizationTask = SizingTask(
            name,
            abaqusSensitivities,
            elementThicknessDeltaStopCriteria,
            freezeBoundaryConditionRegions,
            freezeLoadRegions,
            modeTrackingRegion,
            numFulfilledStopCriteria,
            numTrackedModes,
            objectiveFunctionDeltaStopCriteria,
            stopCriteriaDesignCycle,
            thicknessMoveLimit,
            thicknessUpdateStrategy,
        )
        return optimizationTask

    @abaqus_method_doc
    def TopologyTask(
        self,
        name: str,
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
        softDeletionMethod: Literal[
            C.STANDARD,
            C.VOLUME_COMPRESSION,
            C.MAX_SHEAR_STRAIN,
            C.AGGRESSIVE,
            C.MIN_PRINCIPAL_STRAIN,
            C.MAX_ELASTOPLASTIC_STRAIN,
        ] = STANDARD,
        softDeletionRadius: float = 0,
        softDeletionRegion: Optional[str] = None,
        softDeletionThreshold: Optional[float] = None,
        stepSize: Literal[C.SMALL, C.LARGE, C.MODERATE, C.VERY_SMALL, C.DYNAMIC, C.MEDIUM] = MEDIUM,
        stiffnessMassDamping: Union[Literal[C.AVERAGE_EDGE_LENGTH], float] = AVERAGE_EDGE_LENGTH,
        stopCriteriaDesignCycle: int = 4,
        structuralMassDamping: Optional[float] = None,
        viscousMassDamping: Optional[float] = None,
        viscousStiffnessDamping: Optional[float] = None,
    ) -> TopologyTask:
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
            sensitivities. The default value is True.

            .. versionadded:: 2019
                The ``abaqusSensitivities`` argument was added.
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
            default value is 0.5x10⁻².
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
            A Float specifying the minimum density in the density update. The default value is 10⁻³.
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
            default value is 10⁻³.
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
            A TopologyTask object.
        """
        self.optimizationTasks[name] = optimizationTask = TopologyTask(
            name,
            abaqusSensitivities,
            algorithm,
            densityMoveLimit,
            densityUpdateStrategy,
            elementDensityDeltaStopCriteria,
            filterRadius,
            firstCycleDeletedVolume,
            firstCycleDeletedVolumeTechnique,
            freezeBoundaryConditionRegions,
            freezeLoadRegions,
            frequencySpectrumWeight,
            initialDensity,
            materialInterpolationPenalty,
            materialInterpolationTechnique,
            maxDensity,
            minDensity,
            modeTrackingRegion,
            numDesignCycles,
            numFulfilledStopCriteria,
            numTrackedModes,
            objectiveFunctionDeltaStopCriteria,
            region,
            softDeletionMethod,
            softDeletionRadius,
            softDeletionRegion,
            softDeletionThreshold,
            stepSize,
            stiffnessMassDamping,
            stopCriteriaDesignCycle,
            structuralMassDamping,
            viscousMassDamping,
            viscousStiffnessDamping,
        )
        return optimizationTask
