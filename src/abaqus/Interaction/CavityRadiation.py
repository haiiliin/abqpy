from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Interaction import Interaction
from ..BasicGeometry.ModelDot import ModelDot
from ..Region.RegionArray import RegionArray
from ..UtilityAndView.abaqusConstants import BLOCKING_ALL, Boolean, OFF, ON, SymbolicConstant


@abaqus_class_doc
class CavityRadiation(Interaction):
    """The CavityRadiation object defines cavities for thermal radiation heat transfer and
    controls the calculation of viewfactors.
    The CavityRadiation object is derived from the Interaction object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name]

        The corresponding analysis keywords are:

        - CAVITY DEFINITION
        - CYCLIC
        - EMISSIVITY
        - PERIODIC
        - RADIATION SYMMETRY
        - RADIATION VIEWFACTOR
        - REFLECTION
    """

    #: A String specifying the repository key.
    name: str = ""

    #: None or a Float specifying the reference ambient temperature value, θ0θ0. Specifying a
    #: value indicates an open cavity. The default value is None.
    ambientTemp: Optional[float] = None

    #: A Float specifying the facet area ratio above which the infinitesimal-to-finite area
    #: approximation is used for viewfactor calculations. The default value is 64.0.
    minInfinitesimalRatio: float = 64

    #: An Int specifying the number of Gauss integration points to be used along each edge when
    #: the numerical integration of contour integrals is used for viewfactor calculations. One
    #: to five integration points are allowed. The default value is 3.
    numPointsPerEdge: int = 3

    #: A Float specifying the nondimensional distance-square value above which the lumped area
    #: approximation is used for viewfactor calculations. The default value is 5.0.
    minLumpedAreaDS: float = 5

    #: A Boolean specifying whether cyclic symmetry will be applied. This argument cannot be
    #: specified for axisymmetric models. The default value is OFF.
    cyclicSymmetry: Boolean = OFF

    #: An Int specifying the number of cyclically similar images that compose the cavity formed
    #: as a result of this symmetry. This argument applies only when **cyclicSymmetry** = ON. The
    #: default value is 2.
    cyclicImages: int = 2

    #: An Int specifying the number of periodic symmetries that will be applied. The default
    #: value is 0.
    periodicSymmetries: int = 0

    #: An Int specifying the number of repetitions used in the numerical calculation of the
    #: cavity viewfactors resulting from the first periodic symmetry. The result of this
    #: symmetry is a cavity composed of the cavity surface defined in the model plus twice the
    #: value of **periodicImages_1**. This argument applies only when **periodicSymmetries** is
    #: greater than zero. The default value is 2.
    periodicImages_1: int = 2

    #: An Int specifying the number of repetitions used in the numerical calculation of the
    #: cavity viewfactors resulting from the second periodic symmetry. The result of this
    #: symmetry is a cavity composed of the cavity surface defined in the model plus twice the
    #: value of **periodicImages_2**. This argument applies only when **periodicSymmetries** is
    #: greater than one. The default value is 2.
    periodicImages_2: int = 2

    #: An Int specifying the number of repetitions used in the numerical calculation of the
    #: cavity viewfactors resulting from the third periodic symmetry. The result of this
    #: symmetry is a cavity composed of the cavity surface defined in the model plus twice the
    #: value of **periodicImages_3**. This argument applies only when **periodicSymmetries** = 3.
    #: The default value is 2.
    periodicImages_3: int = 2

    #: None or a Float specifying the Z value indicating the symmetry reference line in
    #: axisymmetric models. This argument applies only for axisymmetric models, and when
    #: **periodicSymmetries** = 1. The default value is None.
    periodicSymZ: Optional[float] = None

    #: None or a Float specifying the Z value indicating the periodic distance in axisymmetric
    #: models. This argument applies only for axisymmetric models, and when
    #: **periodicSymmetries** = 1. The default value is None.
    periodicDistZ: Optional[float] = None

    #: An Int specifying the number of reflection symmetries will be applied. The default value
    #: is 0.
    reflectionSymmetries: int = 0

    #: None or a Float specifying the Z value indicating the symmetry reference line in
    #: axisymmetric models. This argument applies only for axisymmetric models, and when
    #: **reflectionSymmetries** = 1. The default value is None.
    reflectionSymZ: Optional[float] = None

    #: A String specifying the name of the step in which the cavity radiation interaction
    #: should be created.
    createStepName: str = ""

    #: A :py:class:`~abaqus.Region.RegionArray.RegionArray` object specifying the surfaces for which radiation viewfactor control is
    #: being specified.
    surfaces: RegionArray = []

    #: A tuple of Strings specifying the names of the Cavity Radiation properties containing
    #: the surface emissivity data. One name per specified surface. The emissivity data is
    #: ignored when **surfaceReflection** = OFF.
    surfaceEmissivities: tuple = ()

    #: A :py:class:`~abaqus.BasicGeometry.ModelDot.ModelDot` object specifying the rotation axis point. This argument applies only when
    #: **cyclicSymmetry** = ON.
    cyclicRotPt: ModelDot = ModelDot()

    #: A :py:class:`~abaqus.BasicGeometry.ModelDot.ModelDot` object specifying the rotation axis end point. This argument applies only for
    #: three-dimensional models, and only when **cyclicSymmetry** = ON.
    cyclicRotEndPt: ModelDot = ModelDot()

    #: A :py:class:`~abaqus.BasicGeometry.ModelDot.ModelDot` object specifying the symmetry axis end point. This argument applies only
    #: when **cyclicSymmetry** = ON.
    cyclicSymPt: ModelDot = ModelDot()

    #: A tuple of tuples of Floats specifying the two points of the vector that describes the
    #: periodic distance for the first periodic symmetry. Each point is defined by a tuple of
    #: three coordinates indicating its position. This argument applies only when
    #: **periodicSymmetries** is greater than zero. The default value is an empty sequence.
    periodicDistance_1: tuple = ()

    #: A tuple of tuples of Floats specifying the two points of the vector that describes the
    #: periodic distance for the second periodic symmetry. Each point is defined by a tuple of
    #: three coordinates indicating its position. This argument applies only when
    #: **periodicSymmetries** is greater than one. The default value is an empty sequence.
    periodicDistance_2: tuple = ()

    #: A tuple of tuples of Floats specifying the two points of the vector that describes the
    #: periodic distance for the third periodic symmetry. Each point is defined by a tuple of
    #: three coordinates indicating its position. This argument applies only when
    #: **periodicSymmetries** = 3. The default value is an empty sequence.
    periodicDistance_3: tuple = ()

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        surfaces: RegionArray,
        surfaceEmissivities: tuple,
        ambientTemp: Optional[float] = None,
        blocking: SymbolicConstant = BLOCKING_ALL,
        blockingSurfaces: Optional[RegionArray] = None,
        rangeOfView: Optional[float] = None,
        surfaceReflection: Boolean = ON,
        viewfactorAccurTol: float = 0,
        minInfinitesimalRatio: float = 64,
        numPointsPerEdge: int = 3,
        minLumpedAreaDS: float = 5,
        cyclicSymmetry: Boolean = OFF,
        cyclicImages: int = 2,
        cyclicRotPt: Optional[ModelDot] = None, 
        cyclicRotEndPt: Optional[ModelDot] = None, 
        cyclicSymPt: Optional[ModelDot] = None, 
        periodicSymmetries: int = 0,
        periodicImages_1: int = 2,
        periodicImages_2: int = 2,
        periodicImages_3: int = 2,
        periodicSymAxis_1: str = "",
        periodicSymAxis_2: str = "",
        periodicSymPlane_1: str = "",
        periodicSymPlane_2: str = "",
        periodicSymPlane_3: str = "",
        periodicDistance_1: tuple = (),
        periodicDistance_2: tuple = (),
        periodicDistance_3: tuple = (),
        periodicSymZ: Optional[float] = None,
        periodicDistZ: Optional[float] = None,
        reflectionSymmetries: int = 0,
        reflectionSymAxis_1: str = "",
        reflectionSymAxis_2: str = "",
        reflectionSymPlane_1: str = "",
        reflectionSymPlane_2: str = "",
        reflectionSymPlane_3: str = "",
        reflectionSymZ: Optional[float] = None,
    ):
        """This method creates a CavityRadiation object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].CavityRadiation

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the cavity radiation interaction
            should be created.
        surfaces
            A :py:class:`~abaqus.Region.RegionArray.RegionArray` object specifying the surfaces for which radiation viewfactor control is
            being specified.
        surfaceEmissivities
            A sequence of Strings specifying the names of the Cavity Radiation properties containing
            the surface emissivity data. One name per specified surface. The emissivity data is
            ignored when **surfaceReflection** = OFF.
        ambientTemp
            None or a Float specifying the reference ambient temperature value, θ0θ0. Specifying a
            value indicates an open cavity. The default value is None.
        blocking
            A SymbolicConstant specifying the blocking checks to be performed in the viewfactor
            calculations. Possible values are BLOCKING_ALL, NO_BLOCKING, and PARTIAL_BLOCKING. The
            default value is BLOCKING_ALL.
        blockingSurfaces
            A :py:class:`~abaqus.Region.RegionArray.RegionArray` object specifying the surfaces that provide blocking inside the cavity.
            This argument applies only when **blocking** = PARTIAL_BLOCKING.
        rangeOfView
            None or a Float specifying the maximum distance between surface facets at which
            viewfactors are calculated. More distant facets are deemed too far apart to exchange
            significant amounts of heat through radiation effects, and the viewfactors between these
            facets are assumed to be zero. If **rangeOfView** = None, there is no upper limit. The
            default value is None.
        surfaceReflection
            A Boolean specifying whether heat reflections are to be included in the cavity radiation
            calculations. The default value is ON.
        viewfactorAccurTol
            A Float specifying the acceptable tolerance for the viewfactor calculations. The default
            value is 0.05.
        minInfinitesimalRatio
            A Float specifying the facet area ratio above which the infinitesimal-to-finite area
            approximation is used for viewfactor calculations. The default value is 64.0.
        numPointsPerEdge
            An Int specifying the number of Gauss integration points to be used along each edge when
            the numerical integration of contour integrals is used for viewfactor calculations. One
            to five integration points are allowed. The default value is 3.
        minLumpedAreaDS
            A Float specifying the nondimensional distance-square value above which the lumped area
            approximation is used for viewfactor calculations. The default value is 5.0.
        cyclicSymmetry
            A Boolean specifying whether cyclic symmetry will be applied. This argument cannot be
            specified for axisymmetric models. The default value is OFF.
        cyclicImages
            An Int specifying the number of cyclically similar images that compose the cavity formed
            as a result of this symmetry. This argument applies only when **cyclicSymmetry** = ON. The
            default value is 2.
        cyclicRotPt
            A :py:class:`~abaqus.BasicGeometry.ModelDot.ModelDot` object specifying the rotation axis point. This argument applies only when
            **cyclicSymmetry** = ON.
        cyclicRotEndPt
            A :py:class:`~abaqus.BasicGeometry.ModelDot.ModelDot` object specifying the rotation axis end point. This argument applies only for
            three-dimensional models, and only when **cyclicSymmetry** = ON.
        cyclicSymPt
            A :py:class:`~abaqus.BasicGeometry.ModelDot.ModelDot` object specifying the symmetry axis end point. This argument applies only
            when **cyclicSymmetry** = ON.
        periodicSymmetries
            An Int specifying the number of periodic symmetries that will be applied. The default
            value is 0.
        periodicImages_1
            An Int specifying the number of repetitions used in the numerical calculation of the
            cavity viewfactors resulting from the first periodic symmetry. The result of this
            symmetry is a cavity composed of the cavity surface defined in the model plus twice the
            value of **periodicImages_1**. This argument applies only when **periodicSymmetries** is
            greater than zero. The default value is 2.
        periodicImages_2
            An Int specifying the number of repetitions used in the numerical calculation of the
            cavity viewfactors resulting from the second periodic symmetry. The result of this
            symmetry is a cavity composed of the cavity surface defined in the model plus twice the
            value of **periodicImages_2**. This argument applies only when **periodicSymmetries** is
            greater than one. The default value is 2.
        periodicImages_3
            An Int specifying the number of repetitions used in the numerical calculation of the
            cavity viewfactors resulting from the third periodic symmetry. The result of this
            symmetry is a cavity composed of the cavity surface defined in the model plus twice the
            value of **periodicImages_3**. This argument applies only when **periodicSymmetries** = 3.
            The default value is 2.
        periodicSymAxis_1
            A straight Edge, a Datum object representing a datum axis, or an ElementEdge object
            indicating the first line of symmetry in two-dimensional models. This argument applies
            only for 2D models, and when **periodicSymmetries** is greater than zero.
        periodicSymAxis_2
            A straight Edge, a Datum object representing a datum axis, or an ElementEdge object
            indicating the second line of symmetry in two-dimensional models. This argument applies
            only for two-dimensional models, and when **periodicSymmetries** = 2.
        periodicSymPlane_1
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating
            the first plane of symmetry in three-dimensional models. This argument applies only for
            three-dimensional models, and when **periodicSymmetries** is greater than zero.
        periodicSymPlane_2
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating
            the second plane of symmetry in three-dimensional models. This argument applies only for
            three-dimensional models, and when **periodicSymmetries** is greater than one.
        periodicSymPlane_3
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating
            the third plane of symmetry in three-dimensional models. This argument applies only for
            three-dimensional models, and when **periodicSymmetries** = 3.
        periodicDistance_1
            A sequence of sequences of Floats specifying the two points of the vector that describes
            the periodic distance for the first periodic symmetry. Each point is defined by a tuple
            of three coordinates indicating its position. This argument applies only when
            **periodicSymmetries** is greater than zero. The default value is an empty sequence.
        periodicDistance_2
            A sequence of sequences of Floats specifying the two points of the vector that describes
            the periodic distance for the second periodic symmetry. Each point is defined by a tuple
            of three coordinates indicating its position. This argument applies only when
            **periodicSymmetries** is greater than one. The default value is an empty sequence.
        periodicDistance_3
            A sequence of sequences of Floats specifying the two points of the vector that describes
            the periodic distance for the third periodic symmetry. Each point is defined by a tuple
            of three coordinates indicating its position. This argument applies only when
            **periodicSymmetries** = 3. The default value is an empty sequence.
        periodicSymZ
            None or a Float specifying the Z value indicating the symmetry reference line in
            axisymmetric models. This argument applies only for axisymmetric models, and when
            **periodicSymmetries** = 1. The default value is None.
        periodicDistZ
            None or a Float specifying the Z value indicating the periodic distance in axisymmetric
            models. This argument applies only for axisymmetric models, and when
            **periodicSymmetries** = 1. The default value is None.
        reflectionSymmetries
            An Int specifying the number of reflection symmetries will be applied. The default value
            is 0.
        reflectionSymAxis_1
            A straight Edge, a Datum object representing a datum axis, or an ElementEdge object
            indicating the first line of symmetry in two-dimensional models. This argument applies
            only for two-dimensional models, and when **reflectionSymmetries** is greater than zero.
        reflectionSymAxis_2
            A straight Edge, a Datum object representing a datum axis, or an ElementEdge object
            indicating the second line of symmetry in two-dimensional models. This argument applies
            only for two-dimensional models, and when **reflectionSymmetries** = 2.
        reflectionSymPlane_1
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating
            the first plane of symmetry in three-dimensional models. This argument applies only for
            three-dimensional models, and when **reflectionSymmetries** is greater than zero.
        reflectionSymPlane_2
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating
            the second plane of symmetry in three-dimensional models. This argument applies only for
            three-dimensional models, and when **reflectionSymmetries** is greater than one.
        reflectionSymPlane_3
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating
            the third plane of symmetry in three-dimensional models. This argument applies only for
            three-dimensional models, and when **reflectionSymmetries** = 3.
        reflectionSymZ
            None or a Float specifying the Z value indicating the symmetry reference line in
            axisymmetric models. This argument applies only for axisymmetric models, and when
            **reflectionSymmetries** = 1. The default value is None.

        Returns
        -------
        CavityRadiation
            A :py:class:`~abaqus.Interaction.CavityRadiation.CavityRadiation` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        surfaceEmissivities: tuple = (),
        ambientTemp: Optional[float] = None,
        blocking: SymbolicConstant = BLOCKING_ALL,
        blockingSurfaces: Optional[RegionArray] = None,
        rangeOfView: Optional[float] = None,
        surfaceReflection: Boolean = ON,
        viewfactorAccurTol: float = 0,
        minInfinitesimalRatio: float = 64,
        numPointsPerEdge: int = 3,
        minLumpedAreaDS: float = 5,
        cyclicSymmetry: Boolean = OFF,
        cyclicImages: int = 2,
        cyclicRotPt: Optional[ModelDot] = None, 
        cyclicRotEndPt: Optional[ModelDot] = None, 
        cyclicSymPt: Optional[ModelDot] = None, 
        periodicSymmetries: int = 0,
        periodicImages_1: int = 2,
        periodicImages_2: int = 2,
        periodicImages_3: int = 2,
        periodicSymAxis_1: str = "",
        periodicSymAxis_2: str = "",
        periodicSymPlane_1: str = "",
        periodicSymPlane_2: str = "",
        periodicSymPlane_3: str = "",
        periodicDistance_1: tuple = (),
        periodicDistance_2: tuple = (),
        periodicDistance_3: tuple = (),
        periodicSymZ: Optional[float] = None,
        periodicDistZ: Optional[float] = None,
        reflectionSymmetries: int = 0,
        reflectionSymAxis_1: str = "",
        reflectionSymAxis_2: str = "",
        reflectionSymPlane_1: str = "",
        reflectionSymPlane_2: str = "",
        reflectionSymPlane_3: str = "",
        reflectionSymZ: Optional[float] = None,
    ):
        """This method modifies the data for an existing CavityRadiation object in the step where
        it is created.

        Parameters
        ----------
        surfaceEmissivities
            A sequence of Strings specifying the names of the Cavity Radiation properties containing
            the surface emissivity data. One name per specified surface. The emissivity data is
            ignored when **surfaceReflection** = OFF.
        ambientTemp
            None or a Float specifying the reference ambient temperature value, θ0θ0. Specifying a
            value indicates an open cavity. The default value is None.
        blocking
            A SymbolicConstant specifying the blocking checks to be performed in the viewfactor
            calculations. Possible values are BLOCKING_ALL, NO_BLOCKING, and PARTIAL_BLOCKING. The
            default value is BLOCKING_ALL.
        blockingSurfaces
            A :py:class:`~abaqus.Region.RegionArray.RegionArray` object specifying the surfaces that provide blocking inside the cavity.
            This argument applies only when **blocking** = PARTIAL_BLOCKING.
        rangeOfView
            None or a Float specifying the maximum distance between surface facets at which
            viewfactors are calculated. More distant facets are deemed too far apart to exchange
            significant amounts of heat through radiation effects, and the viewfactors between these
            facets are assumed to be zero. If **rangeOfView** = None, there is no upper limit. The
            default value is None.
        surfaceReflection
            A Boolean specifying whether heat reflections are to be included in the cavity radiation
            calculations. The default value is ON.
        viewfactorAccurTol
            A Float specifying the acceptable tolerance for the viewfactor calculations. The default
            value is 0.05.
        minInfinitesimalRatio
            A Float specifying the facet area ratio above which the infinitesimal-to-finite area
            approximation is used for viewfactor calculations. The default value is 64.0.
        numPointsPerEdge
            An Int specifying the number of Gauss integration points to be used along each edge when
            the numerical integration of contour integrals is used for viewfactor calculations. One
            to five integration points are allowed. The default value is 3.
        minLumpedAreaDS
            A Float specifying the nondimensional distance-square value above which the lumped area
            approximation is used for viewfactor calculations. The default value is 5.0.
        cyclicSymmetry
            A Boolean specifying whether cyclic symmetry will be applied. This argument cannot be
            specified for axisymmetric models. The default value is OFF.
        cyclicImages
            An Int specifying the number of cyclically similar images that compose the cavity formed
            as a result of this symmetry. This argument applies only when **cyclicSymmetry** = ON. The
            default value is 2.
        cyclicRotPt
            A :py:class:`~abaqus.BasicGeometry.ModelDot.ModelDot` object specifying the rotation axis point. This argument applies only when
            **cyclicSymmetry** = ON.
        cyclicRotEndPt
            A :py:class:`~abaqus.BasicGeometry.ModelDot.ModelDot` object specifying the rotation axis end point. This argument applies only for
            three-dimensional models, and only when **cyclicSymmetry** = ON.
        cyclicSymPt
            A :py:class:`~abaqus.BasicGeometry.ModelDot.ModelDot` object specifying the symmetry axis end point. This argument applies only
            when **cyclicSymmetry** = ON.
        periodicSymmetries
            An Int specifying the number of periodic symmetries that will be applied. The default
            value is 0.
        periodicImages_1
            An Int specifying the number of repetitions used in the numerical calculation of the
            cavity viewfactors resulting from the first periodic symmetry. The result of this
            symmetry is a cavity composed of the cavity surface defined in the model plus twice the
            value of **periodicImages_1**. This argument applies only when **periodicSymmetries** is
            greater than zero. The default value is 2.
        periodicImages_2
            An Int specifying the number of repetitions used in the numerical calculation of the
            cavity viewfactors resulting from the second periodic symmetry. The result of this
            symmetry is a cavity composed of the cavity surface defined in the model plus twice the
            value of **periodicImages_2**. This argument applies only when **periodicSymmetries** is
            greater than one. The default value is 2.
        periodicImages_3
            An Int specifying the number of repetitions used in the numerical calculation of the
            cavity viewfactors resulting from the third periodic symmetry. The result of this
            symmetry is a cavity composed of the cavity surface defined in the model plus twice the
            value of **periodicImages_3**. This argument applies only when **periodicSymmetries** = 3.
            The default value is 2.
        periodicSymAxis_1
            A straight Edge, a Datum object representing a datum axis, or an ElementEdge object
            indicating the first line of symmetry in two-dimensional models. This argument applies
            only for 2D models, and when **periodicSymmetries** is greater than zero.
        periodicSymAxis_2
            A straight Edge, a Datum object representing a datum axis, or an ElementEdge object
            indicating the second line of symmetry in two-dimensional models. This argument applies
            only for two-dimensional models, and when **periodicSymmetries** = 2.
        periodicSymPlane_1
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating
            the first plane of symmetry in three-dimensional models. This argument applies only for
            three-dimensional models, and when **periodicSymmetries** is greater than zero.
        periodicSymPlane_2
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating
            the second plane of symmetry in three-dimensional models. This argument applies only for
            three-dimensional models, and when **periodicSymmetries** is greater than one.
        periodicSymPlane_3
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating
            the third plane of symmetry in three-dimensional models. This argument applies only for
            three-dimensional models, and when **periodicSymmetries** = 3.
        periodicDistance_1
            A sequence of sequences of Floats specifying the two points of the vector that describes
            the periodic distance for the first periodic symmetry. Each point is defined by a tuple
            of three coordinates indicating its position. This argument applies only when
            **periodicSymmetries** is greater than zero. The default value is an empty sequence.
        periodicDistance_2
            A sequence of sequences of Floats specifying the two points of the vector that describes
            the periodic distance for the second periodic symmetry. Each point is defined by a tuple
            of three coordinates indicating its position. This argument applies only when
            **periodicSymmetries** is greater than one. The default value is an empty sequence.
        periodicDistance_3
            A sequence of sequences of Floats specifying the two points of the vector that describes
            the periodic distance for the third periodic symmetry. Each point is defined by a tuple
            of three coordinates indicating its position. This argument applies only when
            **periodicSymmetries** = 3. The default value is an empty sequence.
        periodicSymZ
            None or a Float specifying the Z value indicating the symmetry reference line in
            axisymmetric models. This argument applies only for axisymmetric models, and when
            **periodicSymmetries** = 1. The default value is None.
        periodicDistZ
            None or a Float specifying the Z value indicating the periodic distance in axisymmetric
            models. This argument applies only for axisymmetric models, and when
            **periodicSymmetries** = 1. The default value is None.
        reflectionSymmetries
            An Int specifying the number of reflection symmetries will be applied. The default value
            is 0.
        reflectionSymAxis_1
            A straight Edge, a Datum object representing a datum axis, or an ElementEdge object
            indicating the first line of symmetry in two-dimensional models. This argument applies
            only for two-dimensional models, and when **reflectionSymmetries** is greater than zero.
        reflectionSymAxis_2
            A straight Edge, a Datum object representing a datum axis, or an ElementEdge object
            indicating the second line of symmetry in two-dimensional models. This argument applies
            only for two-dimensional models, and when **reflectionSymmetries** = 2.
        reflectionSymPlane_1
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating
            the first plane of symmetry in three-dimensional models. This argument applies only for
            three-dimensional models, and when **reflectionSymmetries** is greater than zero.
        reflectionSymPlane_2
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating
            the second plane of symmetry in three-dimensional models. This argument applies only for
            three-dimensional models, and when **reflectionSymmetries** is greater than one.
        reflectionSymPlane_3
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating
            the third plane of symmetry in three-dimensional models. This argument applies only for
            three-dimensional models, and when **reflectionSymmetries** = 3.
        reflectionSymZ
            None or a Float specifying the Z value indicating the symmetry reference line in
            axisymmetric models. This argument applies only for axisymmetric models, and when
            **reflectionSymmetries** = 1. The default value is None.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        blocking: SymbolicConstant = BLOCKING_ALL,
        blockingSurfaces: Optional[RegionArray] = None,
        rangeOfView: Optional[float] = None,
        surfaceReflection: Boolean = ON,
        viewfactorAccurTol: float = 0,
    ):
        """This method modifies the propagating data of an existing CavityRadiation object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified.
        blocking
            A SymbolicConstant specifying the blocking checks to be performed in the viewfactor
            calculations. Possible values are BLOCKING_ALL, NO_BLOCKING, and PARTIAL_BLOCKING. The
            default value is BLOCKING_ALL.
        blockingSurfaces
            A :py:class:`~abaqus.Region.RegionArray.RegionArray` object specifying the surfaces that provide blocking inside the cavity.
            This argument applies only when **blocking** = PARTIAL_BLOCKING.
        rangeOfView
            None or a Float specifying the maximum distance between surface facets at which
            viewfactors are calculated. More distant facets are deemed too far apart to exchange
            significant amounts of heat through radiation effects, and the viewfactors between these
            facets are assumed to be zero. If **rangeOfView** = None, there is no upper limit. The
            default value is None.
        surfaceReflection
            A Boolean specifying whether heat reflections are to be included in the cavity radiation
            calculations. The default value is ON.
        viewfactorAccurTol
            A Float specifying the acceptable tolerance for the viewfactor calculations. The default
            value is 0.05.
        """
        ...
