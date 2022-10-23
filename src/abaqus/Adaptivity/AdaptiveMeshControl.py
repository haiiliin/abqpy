from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ..UtilityAndView.abaqusConstants import (
    CURRENT,
    ELEMENT_CENTER_PROJECTION,
    GEOMETRY_ENHANCED,
    SECOND_ORDER_ADVECTION,
    SymbolicConstant,
    UNIFORM,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class AdaptiveMeshControl:
    r"""The AdaptiveMeshControl object is used to control various aspects of Arbitrary
    Lagrangian Eularian (ALE) style adaptive smoothing and advection algorithms applied to
    an ALE adaptive mesh domain.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].adaptiveMeshControls[name]
    """

    #: A String specifying the name of the object.
    name: str

    #: A SymbolicConstant specifying the remapping algorithm. Possible values are
    #: FIRST_ORDER_ADVECTION and SECOND_ORDER_ADVECTION. The default value is
    #: SECOND_ORDER_ADVECTION.
    remapping: SymbolicConstant = SECOND_ORDER_ADVECTION

    #: A SymbolicConstant specifying the type of smoothing algorithm to use. Possible values
    #: are STANDARD and GEOMETRY_ENHANCED. The default value is GEOMETRY_ENHANCED.
    smoothingAlgorithm: SymbolicConstant = GEOMETRY_ENHANCED

    #: A SymbolicConstant specifying the type of smoothing to perform. Possible values are
    #: UNIFORM and GRADED. The default value is UNIFORM.
    smoothingPriority: SymbolicConstant = UNIFORM

    #: A Float specifying the initial geometric feature angle, :math:`\theta_I`, in degrees. Possible values
    #: are :math:`0^\circ\le\theta_I\le 180^\circ`. The default value is 30.0.
    initialFeatureAngle: float = 30

    #: A Float specifying the transitional feature angle, :math:`\theta_T`, in degrees. Possible values are
    #: :math:`0^\circ\le\theta_T\le 180^\circ`. The default value is 30.0.
    transitionFeatureAngle: float = 30

    #: A SymbolicConstant specifying the type of momentum advection algorithm. Possible values
    #: are ELEMENT_CENTER_PROJECTION and HALF_INDEX_SHIFT. The default value is
    #: ELEMENT_CENTER_PROJECTION.
    momentumAdvection: SymbolicConstant = ELEMENT_CENTER_PROJECTION

    #: A SymbolicConstant specifying the nodal starting location to use for remeshing. Possible
    #: values are CURRENT and PREVIOUS. The default value is CURRENT.
    meshingPredictor: SymbolicConstant = CURRENT

    #: A Float specifying the solution dependence weight, :math:`\alpha_C`. Possible values are
    #: :math:`0.0\le\alpha_C\le 1.0`. The default value is 1.0.
    curvatureRefinement: float = 1

    #: A Float specifying the weight used by Abaqus/Explicit for the volumetric smoothing
    #: method. The default value is 1.0.
    volumetricSmoothingWeight: float = 1

    #: A Float specifying the weight for the Laplacian smoothing method. The default value is
    #: 0.0.
    laplacianSmoothingWeight: float = 0

    #: A Float specifying the weight for the equipotential smoothing method. The default value
    #: is 0.0.
    equipotentialSmoothingWeight: float = 0

    #: A Float specifying the initial geometric feature angle, :math:`\theta_C`. Possible values
    #: are :math:`0^\circ\le\theta_C\le 180^\circ`. The default value is 60.0.
    meshConstraintAngle: float = 60

    #: A Float specifying the weight for the original configuration projection method. The
    #: default value is 1.0.
    originalConfigurationProjectionWeight: float = 1

    #: A Float specifying the weight used by Abaqus/Standard for the volumetric smoothing
    #: method. The default value is 0.0.
    standardVolumetricSmoothingWeight: float = 0

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        remapping: Literal[C.SECOND_ORDER_ADVECTION, C.FIRST_ORDER_ADVECTION] = SECOND_ORDER_ADVECTION,
        smoothingAlgorithm: Literal[C.GEOMETRY_ENHANCED, C.STANDARD] = GEOMETRY_ENHANCED,
        smoothingPriority: Literal[C.GRADED, C.UNIFORM] = UNIFORM,
        initialFeatureAngle: float = 30,
        transitionFeatureAngle: float = 30,
        momentumAdvection: Literal[C.HALF_INDEX_SHIFT, C.ELEMENT_CENTER_PROJECTION] = ELEMENT_CENTER_PROJECTION,
        meshingPredictor: Literal[C.PREVIOUS, C.CURRENT] = CURRENT,
        curvatureRefinement: float = 1,
        volumetricSmoothingWeight: float = 1,
        laplacianSmoothingWeight: float = 0,
        equipotentialSmoothingWeight: float = 0,
        meshConstraintAngle: float = 60,
        originalConfigurationProjectionWeight: float = 1,
        standardVolumetricSmoothingWeight: float = 0,
    ):
        r"""This method creates an AdaptiveMeshControl object.

        .. note::
            This function can be accessed by::

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
            A Float specifying the initial geometric feature angle, :math:`\theta_I`, in degrees. Possible values
            are :math:`0^\circ\le\theta_I\le 180^\circ`. The default value is 30.0.
        transitionFeatureAngle
            A Float specifying the transitional feature angle, :math:`\theta_T`, in degrees. Possible values are
            :math:`0^\circ\le\theta_T\le 180^\circ`. The default value is 30.0.
        momentumAdvection
            A SymbolicConstant specifying the type of momentum advection algorithm. Possible values
            are ELEMENT_CENTER_PROJECTION and HALF_INDEX_SHIFT. The default value is
            ELEMENT_CENTER_PROJECTION.
        meshingPredictor
            A SymbolicConstant specifying the nodal starting location to use for remeshing. Possible
            values are CURRENT and PREVIOUS. The default value is CURRENT.
        curvatureRefinement
            A Float specifying the solution dependence weight, :math:`\alpha_C`. Possible values are
            :math:`0.0\le\alpha_C\le 1.0`. The default value is 1.0.
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
            A Float specifying the initial geometric feature angle, :math:`\theta_C`. Possible values
            are :math:`0^\circ\le\theta_C\le 180^\circ`. The default value is 60.0.
        originalConfigurationProjectionWeight
            A Float specifying the weight for the original configuration projection method. The
            default value is 1.0.
        standardVolumetricSmoothingWeight
            A Float specifying the weight used by Abaqus/Standard for the volumetric smoothing
            method. The default value is 0.0.

        Returns
        -------
        AdaptiveMeshControl
            An :py:class:`~abaqus.Adaptivity.AdaptiveMeshControl.AdaptiveMeshControl` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(
        self,
        remapping: Literal[C.SECOND_ORDER_ADVECTION, C.FIRST_ORDER_ADVECTION] = SECOND_ORDER_ADVECTION,
        smoothingAlgorithm: Literal[C.GEOMETRY_ENHANCED, C.STANDARD] = GEOMETRY_ENHANCED,
        smoothingPriority: Literal[C.GRADED, C.UNIFORM] = UNIFORM,
        initialFeatureAngle: float = 30,
        transitionFeatureAngle: float = 30,
        momentumAdvection: Literal[C.HALF_INDEX_SHIFT, C.ELEMENT_CENTER_PROJECTION] = ELEMENT_CENTER_PROJECTION,
        meshingPredictor: Literal[C.PREVIOUS, C.CURRENT] = CURRENT,
        curvatureRefinement: float = 1,
        volumetricSmoothingWeight: float = 1,
        laplacianSmoothingWeight: float = 0,
        equipotentialSmoothingWeight: float = 0,
        meshConstraintAngle: float = 60,
        originalConfigurationProjectionWeight: float = 1,
        standardVolumetricSmoothingWeight: float = 0,
    ):
        r"""This method modifies the AdaptiveMeshControl object.

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
            A Float specifying the initial geometric feature angle, :math:`\theta_I`, in degrees. Possible values
            are :math:`0^\circ\le\theta_I\le 180^\circ`. The default value is 30.0.
        transitionFeatureAngle
            A Float specifying the transitional feature angle, :math:`\theta_T`, in degrees. Possible values are
            :math:`0^\circ\le\theta_T\le 180^\circ`. The default value is 30.0.
        momentumAdvection
            A SymbolicConstant specifying the type of momentum advection algorithm. Possible values
            are ELEMENT_CENTER_PROJECTION and HALF_INDEX_SHIFT. The default value is
            ELEMENT_CENTER_PROJECTION.
        meshingPredictor
            A SymbolicConstant specifying the nodal starting location to use for remeshing. Possible
            values are CURRENT and PREVIOUS. The default value is CURRENT.
        curvatureRefinement
            A Float specifying the solution dependence weight, :math:`\alpha_C`. Possible values are
            :math:`0.0\le\alpha_C\le 1.0`. The default value is 1.0.
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
            A Float specifying the initial geometric feature angle, :math:`\theta_c`. Possible values are
            :math:`0^\circ\le\theta_C\le 180^\circ`. The default value is 60.0.
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
        ...
