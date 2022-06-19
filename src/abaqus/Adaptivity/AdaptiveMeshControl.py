from abaqusConstants import *


class AdaptiveMeshControl:
    """The AdaptiveMeshControl object is used to control various aspects of Arbitrary
    Lagrangian Eularian (ALE) style adaptive smoothing and advection algorithms applied to
    an ALE adaptive mesh domain.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import step
        mdb.models[name].adaptiveMeshControls[name]

    """

    def __init__(
        self,
        name: str,
        remapping: SymbolicConstant = SECOND_ORDER_ADVECTION,
        smoothingAlgorithm: SymbolicConstant = GEOMETRY_ENHANCED,
        smoothingPriority: SymbolicConstant = UNIFORM,
        initialFeatureAngle: float = 30,
        transitionFeatureAngle: float = 30,
        momentumAdvection: SymbolicConstant = ELEMENT_CENTER_PROJECTION,
        meshingPredictor: SymbolicConstant = CURRENT,
        curvatureRefinement: float = 1,
        volumetricSmoothingWeight: float = 1,
        laplacianSmoothingWeight: float = 0,
        equipotentialSmoothingWeight: float = 0,
        meshConstraintAngle: float = 60,
        originalConfigurationProjectionWeight: float = 1,
        standardVolumetricSmoothingWeight: float = 0,
    ):
        """This method creates an AdaptiveMeshControl object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].AdaptiveMeshControl

        Parameters
        ----------
        name
            A String specifying the name of the object.
        remapping
            A SymbolicConstant specifying the remapping algorithm. Possible values are
            FIRST_ORDER_ADVECTION and SECOND_ORDER_ADVECTION. The default value is
            SECOND_ORDER_ADVECTION.
        smoothingAlgorithm
            A SymbolicConstant specifying the type of smoothing algorithm to use. Possible values
            are STANDARD and GEOMETRY_ENHANCED. The default value is GEOMETRY_ENHANCED.
        smoothingPriority
            A SymbolicConstant specifying the type of smoothing to perform. Possible values are
            UNIFORM and GRADED. The default value is UNIFORM.
        initialFeatureAngle
            A Float specifying the initial geometric feature angle, θI, in degrees. Possible values
            are 0° ≤θI≤ 180°. The default value is 30.0.
        transitionFeatureAngle
            A Float specifying the transitional feature angle, θT, in degrees. Possible values are
            0° ≤θT≤ 180°. The default value is 30.0.
        momentumAdvection
            A SymbolicConstant specifying the type of momentum advection algorithm. Possible values
            are ELEMENT_CENTER_PROJECTION and HALF_INDEX_SHIFT. The default value is
            ELEMENT_CENTER_PROJECTION.
        meshingPredictor
            A SymbolicConstant specifying the nodal starting location to use for remeshing. Possible
            values are CURRENT and PREVIOUS. The default value is CURRENT.
        curvatureRefinement
            A Float specifying the solution dependence weight, αC. Possible values are 0.0 ≤αC≤ 1.0.
            The default value is 1.0.
        volumetricSmoothingWeight
            A Float specifying the weight used by Abaqus/Explicit for the volumetric smoothing
            method. The default value is 1.0.
        laplacianSmoothingWeight
            A Float specifying the weight for the Laplacian smoothing method. The default value is
            0.0.
        equipotentialSmoothingWeight
            A Float specifying the weight for the equipotential smoothing method. The default value
            is 0.0.
        meshConstraintAngle
            A Float specifying the initial geometric feature angle, θC. Possible values are 0° ≤θC≤
            180°. The default value is 60.0.
        originalConfigurationProjectionWeight
            A Float specifying the weight for the original configuration projection method. The
            default value is 1.0.
        standardVolumetricSmoothingWeight
            A Float specifying the weight used by Abaqus/Standard for the volumetric smoothing
            method. The default value is 0.0.

        Returns
        -------
            An AdaptiveMeshControl object.

        Raises
        ------
            RangeError.
        """
        pass

    def setValues(
        self,
        remapping: SymbolicConstant = SECOND_ORDER_ADVECTION,
        smoothingAlgorithm: SymbolicConstant = GEOMETRY_ENHANCED,
        smoothingPriority: SymbolicConstant = UNIFORM,
        initialFeatureAngle: float = 30,
        transitionFeatureAngle: float = 30,
        momentumAdvection: SymbolicConstant = ELEMENT_CENTER_PROJECTION,
        meshingPredictor: SymbolicConstant = CURRENT,
        curvatureRefinement: float = 1,
        volumetricSmoothingWeight: float = 1,
        laplacianSmoothingWeight: float = 0,
        equipotentialSmoothingWeight: float = 0,
        meshConstraintAngle: float = 60,
        originalConfigurationProjectionWeight: float = 1,
        standardVolumetricSmoothingWeight: float = 0,
    ):
        """This method modifies the AdaptiveMeshControl object.

        Parameters
        ----------
        remapping
            A SymbolicConstant specifying the remapping algorithm. Possible values are
            FIRST_ORDER_ADVECTION and SECOND_ORDER_ADVECTION. The default value is
            SECOND_ORDER_ADVECTION.
        smoothingAlgorithm
            A SymbolicConstant specifying the type of smoothing algorithm to use. Possible values
            are STANDARD and GEOMETRY_ENHANCED. The default value is GEOMETRY_ENHANCED.
        smoothingPriority
            A SymbolicConstant specifying the type of smoothing to perform. Possible values are
            UNIFORM and GRADED. The default value is UNIFORM.
        initialFeatureAngle
            A Float specifying the initial geometric feature angle, θI, in degrees. Possible values
            are 0° ≤θI≤ 180°. The default value is 30.0.
        transitionFeatureAngle
            A Float specifying the transitional feature angle, θT, in degrees. Possible values are
            0° ≤θT≤ 180°. The default value is 30.0.
        momentumAdvection
            A SymbolicConstant specifying the type of momentum advection algorithm. Possible values
            are ELEMENT_CENTER_PROJECTION and HALF_INDEX_SHIFT. The default value is
            ELEMENT_CENTER_PROJECTION.
        meshingPredictor
            A SymbolicConstant specifying the nodal starting location to use for remeshing. Possible
            values are CURRENT and PREVIOUS. The default value is CURRENT.
        curvatureRefinement
            A Float specifying the solution dependence weight, αC. Possible values are 0.0 ≤αC≤ 1.0.
            The default value is 1.0.
        volumetricSmoothingWeight
            A Float specifying the weight used by Abaqus/Explicit for the volumetric smoothing
            method. The default value is 1.0.
        laplacianSmoothingWeight
            A Float specifying the weight for the Laplacian smoothing method. The default value is
            0.0.
        equipotentialSmoothingWeight
            A Float specifying the weight for the equipotential smoothing method. The default value
            is 0.0.
        meshConstraintAngle
            A Float specifying the initial geometric feature angle, θC. Possible values are 0° ≤θC≤
            180°. The default value is 60.0.
        originalConfigurationProjectionWeight
            A Float specifying the weight for the original configuration projection method. The
            default value is 1.0.
        standardVolumetricSmoothingWeight
            A Float specifying the weight used by Abaqus/Standard for the volumetric smoothing
            method. The default value is 0.0.

        Raises
        ------
        RangeError
        """
        pass
