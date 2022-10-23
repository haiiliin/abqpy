from typing import Dict

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .DesignResponse import DesignResponse
from .GeometricRestriction import GeometricRestriction
from .ObjectiveFunction import ObjectiveFunction
from .OptimizationConstraint import OptimizationConstraint
from .OptimizationTask import OptimizationTask
from ..UtilityAndView.abaqusConstants import (Boolean, CONSERVATIVE, DEFAULT, EVERY_CYCLE,
                                              GENERAL_OPTIMIZATION, MODEL, OFF, SymbolicConstant,
                                              VALUE)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class BeadTask(OptimizationTask):
    """The BeadTask object defines a bead task.
    The BeadTask object is derived from the OptimizationTask object.

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

    #: A Boolean specifying whether to exclude elements with boundary conditions from the
    #: optimization. The default value is OFF.
    areBCRegionsFrozen: Boolean = OFF

    #: An int specifying the step size of the optimization. The default value is 1.
    beadIter: str = 1

    #: A float specifying maximum membrane/bending stress. The default value is 0.1.
    beadMaxMembraneStress: str = 0

    #: A float specifying minimum stress. The default value is 0.001.
    beadMinStress: str = 0

    #: A Sets perturbation size for finite differences. The default value is 0.0001.
    beadPerturbation: str = 0

    #: A SymbolicConstant specifying the Optimization product default or a float specifying the
    #: bead width. The default value is DEFAULT.
    beadWidth: SymbolicConstant = DEFAULT

    #: A float specifying relative value to the middle element edge length such that normals in
    #: this area do not cross each other. The default value is 5.
    curveSmooth: str = 5

    #: A float specifying the filter radius. The default value is 4.
    filterRadius: str = 4

    #: A SymbolicConstant specifying the method used to define filter radius. Possible values
    #: are VALUE and REFERENCE. The default is VALUE.
    filterRadiusBy: SymbolicConstant = VALUE

    #: A Boolean specifying whether the growth direction is along the normal direction of
    #: elements or opposite to the normal direction. The default value is OFF
    flipNormalDir: Boolean = OFF

    #: When nodes with boundary conditions are excluded from the optimization
    #: (*frozenBoundaryConditionRegions* = ON). you can specify that this exclusion apply to
    #: nodes throughout the model or only to those nodes from a specific region. Set this
    #: parameter to the SymbolicConstant MODEL to apply the freeze to the entire model, or set
    #: this parameter to a Region object to specify an individual region over which nodes with
    #: boundary conditions should be frozen. The default value is MODEL.
    frozenBoundaryConditionRegion: SymbolicConstant = MODEL

    #: A Boolean specifying whether to calculate the sensitivities only on design nodes or the
    #: whole model. The default value is ON
    isSensCalcOnlyOnDesignNodes: Boolean = OFF

    #: The SymbolicConstant MODEL or a Region object specifying the region to use for mode
    #: tracking. The default value is MODEL.
    modeTrackingRegion: SymbolicConstant = MODEL

    #: A Float specifying the maximum change in nodal displacement per design cycle. The
    #: default value is 0.1.
    nodalMoveLimit: float = 0

    #: A SymbolicConstant specifying the Optimization product default or a float specifying the
    #: node smooth. The default value is DEFAULT.
    nodeSmooth: SymbolicConstant = DEFAULT

    #: A SymbolicConstant specifying the strategy for how the nodal displacements are updated
    #: in the method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and
    #: AGGRESSIVE. The default value is CONSERVATIVE.
    nodeUpdateStrategy: SymbolicConstant = CONSERVATIVE

    #: An Int specifying the number of modes included in mode tracking. The default value is 5.
    numTrackedModes: int = 5

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
        groupOperator: Boolean = OFF,
    ):
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
                The `abaqusSensitivities` argument was added.
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
        groupOperator
            A Boolean specifying whether the group in the design response will be evaluated using
            the existing algorithm or a new algorithm based on Abaqus sensitivities. The default
            value of False means that the existing algorithm will be used.

            .. versionadded:: 2022
                The `groupOperator` argument was added.

        Returns
        -------
        BeadTask
            A :py:class:`~abaqus.Optimization.BeadTask.BeadTask` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
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
        groupOperator: Boolean = OFF,
    ):
        """This method modifies the BeadTask object.

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
        groupOperator
            A Boolean specifying whether the group in the design response will be evaluated using
            the existing algorithm or a new algorithm based on Abaqus sensitivities. The default
            value of False means that the existing algorithm will be used.

            .. versionadded:: 2022
                The `groupOperator` argument was added.
        """
        ...
