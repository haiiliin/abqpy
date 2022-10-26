from typing import Union, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .AdaptiveMeshConstraint import AdaptiveMeshConstraint
from .AdaptiveMeshControl import AdaptiveMeshControl
from .DisplacementAdaptiveMeshConstraint import DisplacementAdaptiveMeshConstraint
from .RemeshingRule import RemeshingRule
from .VelocityAdaptiveMeshConstraint import VelocityAdaptiveMeshConstraint
from ..Datum.DatumCsys import DatumCsys
from ..Model.ModelBase import ModelBase
from ..Odb.Odb import Odb
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import (
    Boolean,
    CURRENT,
    DEFAULT,
    DEFAULT_LIMIT,
    ELEMENT_CENTER_PROJECTION,
    GEOMETRY_ENHANCED,
    INDEPENDENT,
    LAST_INCREMENT,
    MODEL,
    OFF,
    ON,
    SECOND_ORDER_ADVECTION,
    UNIFORM,
    UNSET,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class AdaptivityModel(ModelBase):
    """Abaqus creates a Model object named `Model-1` when a session is started.

    .. note::
        This object can be accessed by::

            mdb.models[name]
    """

    @abaqus_method_doc
    def adaptiveRemesh(self, odb: Odb):
        """This method remeshes the model using the active remesh rules in the model and the error
        indicator results from a previous analysis.

        Parameters
        ----------
        odb
            An :py:class:`~abaqus.Odb.Odb.Odb` object containing error output field results.

        Returns
        -------
        AdaptivityIteration
            An :py:class:`~abaqus.Adaptivity.AdaptivityIteration.AdaptivityIteration` object.
        """
        ...

    @abaqus_method_doc
    def AdaptiveMeshConstraint(
        self,
        name: str,
        category: Literal[C.THERMAL, C.MECHANICAL],
        region: Region,
        localCsys: Optional[DatumCsys] = None,
    ) -> AdaptiveMeshConstraint:
        """The AdaptiveMeshConstraint object is the abstract base type for other Arbitrary
        Lagrangian Eularian (ALE) style AdaptiveMeshConstraint objects. The
        AdaptiveMeshConstraint object has no explicit constructor. The methods and members of
        the AdaptiveMeshConstraint object are common to all objects derived from the
        AdaptiveMeshConstraint object.

        .. note::
            This function can be accessed by::

                mdb.models[name].AdaptiveMeshConstraint

        Parameters
        ----------
        name
            A String specifying the adaptive mesh constraint repository key.
        category
            A SymbolicConstant specifying the category of the adaptive mesh constraint. Possible values are
            MECHANICAL and THERMAL.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the adaptive mesh constraint is applied.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the adaptive mesh  constraint's
            degrees of freedom. If **localCsys** = None, the degrees of freedom are defined  in the global coordinate
            system. The default value is None.

        Returns
        -------
        AdaptiveMeshConstraint
            An :py:class:`~abaqus.Adaptivity.AdaptiveMeshConstraint.AdaptiveMeshConstraint` object
        """
        self.adaptiveMeshConstraints[name] = adaptiveMeshConstraint = AdaptiveMeshConstraint(
            name, category, region, localCsys
        )
        return adaptiveMeshConstraint

    @abaqus_method_doc
    def AdaptiveMeshControl(
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
    ) -> AdaptiveMeshControl:
        """This method creates an AdaptiveMeshControl object.

        .. note::
            This function can be accessed by::

                mdb.models[name].AdaptiveMeshConstraint

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
        AdaptiveMeshControl
            An :py:class:`~abaqus.Adaptivity.AdaptiveMeshControl.AdaptiveMeshControl` object
        """
        self.adaptiveMeshControls[name] = adaptiveMeshControl = AdaptiveMeshControl(
            name,
            remapping,
            smoothingAlgorithm,
            smoothingPriority,
            initialFeatureAngle,
            transitionFeatureAngle,
            momentumAdvection,
            meshingPredictor,
            curvatureRefinement,
            volumetricSmoothingWeight,
            laplacianSmoothingWeight,
            equipotentialSmoothingWeight,
            meshConstraintAngle,
            originalConfigurationProjectionWeight,
            standardVolumetricSmoothingWeight,
        )
        return adaptiveMeshControl

    @abaqus_method_doc
    def DisplacementAdaptiveMeshConstraint(
        self,
        name: str,
        createStepName: str,
        region: Region,
        u1: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        u2: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        u3: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        ur1: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        ur2: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        ur3: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        amplitude: str = UNSET,
        motionType: Literal[C.USER_DEFINED, C.INDEPENDENT, C.FOLLOW] = INDEPENDENT,
        localCsys: Optional[DatumCsys] = None,
    ) -> DisplacementAdaptiveMeshConstraint:
        """This method creates a DisplacementAdaptiveMeshConstraint object.

        .. note::
            This function can be accessed by::

                mdb.models[name].AdaptiveMeshConstraint

        Parameters
        ----------
        name
            A String specifying the adaptive mesh constraint repository key.
        createStepName
            A String specifying the name of the step in which the adaptive mesh constraint is
            created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the adaptive mesh constraint is applied.
        u1
            A Float or a SymbolicConstant specifying the displacement component in the 1-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is
            UNSET. Note: Although **u1**, **u2**, **u3**, **ur1**, **ur2**, and **ur3** are optional arguments, at
            least one of them must be specified.
        u2
            A Float or a SymbolicConstant specifying the displacement component in the 2-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.
        u3
            A Float or a SymbolicConstant specifying the displacement component in the 3-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.
        ur1
            A Float or a SymbolicConstant specifying the rotational displacement component about the
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        ur2
            A Float or a SymbolicConstant specifying the rotational displacement component about the
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        ur3
            A Float or a SymbolicConstant specifying the rotational displacement component about the
            3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the adaptive mesh constraint has no amplitude reference. The
            default value is UNSET. You should provide the **amplitude** argument only if it is valid
            for the specified step.
        motionType
            A SymbolicConstant specifying the mesh motion in relation to the underlying material.
            Possible values are INDEPENDENT, FOLLOW and USER_DEFINED. The default value is
            INDEPENDENT.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the adaptive mesh
            constraint's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.

        Returns
        -------
        DisplacementAdaptiveMeshConstraint
            A :py:class:`~abaqus.Adaptivity.DisplacementAdaptiveMeshConstraint.DisplacementAdaptiveMeshConstraint` object
        """
        self.adaptiveMeshConstraints[name] = adaptiveMeshConstraint = DisplacementAdaptiveMeshConstraint(
            name,
            createStepName,
            region,
            u1,
            u2,
            u3,
            ur1,
            ur2,
            ur3,
            amplitude,
            motionType,
            localCsys,
        )
        return adaptiveMeshConstraint

    @abaqus_method_doc
    def RemeshingRule(
        self,
        name: str,
        stepName: str,
        variables: tuple,
        description: str = "",
        region: Literal[C.MODEL] = MODEL,
        sizingMethod: Literal[C.MINIMUM_MAXIMUM, C.DEFAULT, C.UNIFORM_ERROR] = DEFAULT,
        errorTarget: float = 0,
        maxSolutionErrorTarget: float = 0,
        minSolutionErrorTarget: float = 0,
        meshBias: int = 0,
        minElementSize: float = 0,
        maxElementSize: float = 0,
        outputFrequency: Literal[C.LAST_INCREMENT, C.ALL_INCREMENTS] = LAST_INCREMENT,
        specifyMinSize: Boolean = OFF,
        specifyMaxSize: Boolean = ON,
        coarseningFactor: Literal[C.NOT_ALLOWED, C.DEFAULT_LIMIT] = DEFAULT_LIMIT,
        refinementFactor: Literal[C.NOT_ALLOWED, C.DEFAULT_LIMIT] = DEFAULT_LIMIT,
        elementCountLimit: Optional[int] = None,
    ) -> RemeshingRule:
        """This method creates a RemeshingRule object.

        .. note::
            This function can be accessed by::

                mdb.models[name].AdaptiveMeshConstraint

        Parameters
        ----------
        name
            A String specifying the name of the object.
        stepName
            A String specifying the name of the step in which resizing should occur for this rule.
        variables
            A sequence of Strings specifying the output request variables that Abaqus will use as
            error indicators.
        description
            A String specifying a descriptive string for this rule. The default value is an empty
            string.
        region
            The SymbolicConstant MODEL or a Region object specifying the region in which Abaqus will
            remesh and generate output. The SymbolicConstant MODEL represents the entire applicable
            model. The default value is MODEL.
        sizingMethod
            A SymbolicConstant specifying the method for calculating the new mesh sizes. The
            SymbolicConstant DEFAULT indicates that Abaqus will use the default calculation method
            for each individual variable. Possible values are DEFAULT, UNIFORM_ERROR, and
            MINIMUM_MAXIMUM. The default value is DEFAULT.
        errorTarget
            A Float specifying the target error percentage for each variable in the region. A value
            of 0.0 indicates that Abaqus will use automated error target reduction for the region.
            You use the **errorTarget** argument when **sizingMethod** = UNIFORM_ERROR. The default value
            is 0.0.
        maxSolutionErrorTarget
            A Float specifying the target error percentage at the location of the maximum solution
            value in the region. A value of 0.0 indicates that Abaqus will use automated error
            target reduction for the region. You use the **maxSolutionErrorTarget** argument when
            **sizingMethod** = MINIMUM_MAXIMUM. The default value is 0.0.
        minSolutionErrorTarget
            A Float specifying the target error percentage at the location of the minimum solution
            value in the region. A value of 0.0 indicates that Abaqus will use automated error
            target reduction for the region. You use the **minSolutionErrorTarget** argument when
            **sizingMethod** = MINIMUM_MAXIMUM. The default value is 0.0.
        meshBias
            An Int specifying an indication of how much Abaqus will bias the mesh toward the
            location of the maximum solution value in the region. The higher the value, the more the
            mesh will bias towards the location of the maximum solution value. You use the
            **meshBias** argument when **sizingMethod** = MINIMUM_MAXIMUM. The default value is 0.0.
        minElementSize
            A Float specifying the minimum size of any single element. The default value is 0.0.
        maxElementSize
            A Float specifying the maximum size of any single element. The default value is 0.0.
        outputFrequency
            A SymbolicConstant specifying the frequency with which the error indicators are saved to
            the output database file (.odb). Possible values are LAST_INCREMENT and ALL_INCREMENTS.
            The default value is LAST_INCREMENT.
        specifyMinSize
            A Boolean specifying an indication of whether to use a user-supplied minimum element
            size or to calculate a characteristic minimum element size. The default value is OFF.
        specifyMaxSize
            A Boolean specifying an indication of whether to use a user-supplied maximum element
            size or to calculate a characteristic maximum element size. The default value is ON.
        coarseningFactor
            A SymbolicConstant or an Int specifying an indication of the upper limit on the element
            growth from one remeshing iteration to the next. Possible values are DEFAULT_LIMIT and
            NOT_ALLOWED. The default value is DEFAULT_LIMIT.
        refinementFactor
            A SymbolicConstant or an Int specifying an indication of the upper limit on element
            shrinkage from one remeshing iteration to the next. Possible values are DEFAULT_LIMIT
            and NOT_ALLOWED. The default value is DEFAULT_LIMIT.
        elementCountLimit
            None or an Int specifying an approximate limit on the number of elements that will be
            created during remeshing. Use None to indicate there is not upper limit. The default
            value is None.

        Returns
        -------
        RemeshingRule
            A :py:class:`~abaqus.Adaptivity.RemeshingRule.RemeshingRule` object
        """
        self.remeshingRules[name] = remeshingRule = RemeshingRule(
            name,
            stepName,
            variables,
            description,
            region,
            sizingMethod,
            errorTarget,
            maxSolutionErrorTarget,
            minSolutionErrorTarget,
            meshBias,
            minElementSize,
            maxElementSize,
            outputFrequency,
            specifyMinSize,
            specifyMaxSize,
            coarseningFactor,
            refinementFactor,
            elementCountLimit,
        )
        return remeshingRule

    @abaqus_method_doc
    def VelocityAdaptiveMeshConstraint(
        self,
        name: str,
        createStepName: str,
        region: Region,
        v1: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        v2: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        v3: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        vr1: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        vr2: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        vr3: Union[Literal[C.SET, C.UNSET], float] = UNSET,
        amplitude: str = UNSET,
        localCsys: Optional[DatumCsys] = None,
        motionType: Literal[C.USER_DEFINED, C.INDEPENDENT, C.FOLLOW] = INDEPENDENT,
    ) -> VelocityAdaptiveMeshConstraint:
        """This method creates a VelocityAdaptiveMeshConstraint object.

        .. note::
            This function can be accessed by::

                mdb.models[name].AdaptiveMeshConstraint

        Parameters
        ----------
        name
            A String specifying the adaptive mesh constraint repository key.
        createStepName
            A String specifying the name of the step in which the adaptive mesh constraint is
            created.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the adaptive mesh constraint is applied.
        v1
            A Float or a SymbolicConstant specifying the velocity component in the 1-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is
            UNSET. Note: Although **v1**, **v2**, **v3**, **vr1**, **vr2**, and **vr3** are optional arguments, at
            least one of them must be specified.
        v2
            A Float or a SymbolicConstant specifying the velocity component in the 2-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.
        v3
            A Float or a SymbolicConstant specifying the velocity component in the 3-direction.
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.
        vr1
            A Float or a SymbolicConstant specifying the rotational velocity component about the
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        vr2
            A Float or a SymbolicConstant specifying the rotational velocity component about the
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        vr3
            A Float or a SymbolicConstant specifying the rotational velocity component about the
            3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
            value is UNSET.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the adaptive mesh constraint has no amplitude reference. The
            default value is UNSET. You should provide the **amplitude** argument only if it is valid
            for the specified step.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the adaptive mesh
            constraint's degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
            in the global coordinate system. The default value is None.
        motionType
            A SymbolicConstant specifying the mesh motion in relation to the underlying material.
            Possible values are INDEPENDENT, FOLLOW and USER_DEFINED. The default value is
            INDEPENDENT.

        Returns
        -------
        VelocityAdaptiveMeshConstraint
            A :py:class:`~abaqus.Adaptivity.VelocityAdaptiveMeshConstraint.VelocityAdaptiveMeshConstraint` object
        """
        self.adaptiveMeshConstraints[name] = adaptiveMeshConstraint = VelocityAdaptiveMeshConstraint(
            name,
            createStepName,
            region,
            v1,
            v2,
            v3,
            vr1,
            vr2,
            vr3,
            amplitude,
            localCsys,
            motionType,
        )
        return adaptiveMeshConstraint
