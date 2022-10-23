from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ..UtilityAndView.abaqusConstants import (
    AVERAGE_STRAIN,
    Boolean,
    CUBIC,
    DEFAULT,
    ENHANCED,
    OFF,
    ON,
    STANDARD,
    SymbolicConstant,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class ElemType:
    """The ElemType object is an argument object used as an argument in the setElementType
    command.

    .. note::
        This object can be accessed by::

            import mesh
    """

    #: A SymbolicConstant specifying the Abaqus element code or just the element shape.
    #: Possible values are:
    #:
    #: - C3D8R, specifying a 8-node linear brick, reduced integration with hourglass control.
    #: - CODE, specifying add more codes.
    #: - UNKNOWN_TRI, specifying an unknown element type associated with a triangular shape.
    #: - UNKNOWN_QUAD, specifying an unknown element type associated with a quadrilateral
    #:   shape.
    #: - UNKNOWN_HEX, specifying an unknown element type associated with a hexahedral shape.
    #: - UNKNOWN_WEDGE, specifying an unknown element type associated with a wedge shape.
    #: - UNKNOWN_TET, specifying an unknown element type associated with a tetrahedral shape.
    elemCode: SymbolicConstant

    #: A SymbolicConstant specifying the Abaqus element library to use. Possible values are
    #: STANDARD and EXPLICIT. The default value is STANDARD.
    elemLibrary: SymbolicConstant = STANDARD

    #: A Float specifying the hourglass stiffness. (For shell elements this is the membrane
    #: hourglass stiffness.) A value of zero indicates the default value should be used. The
    #: default value will be used where appropriate. The default value is 0.0.This argument is
    #: applicable only to some Abaqus/Standard elements.
    hourglassStiffness: float = 0

    #: A Float specifying the bending hourglass stiffness. A value of zero indicates the
    #: default value should be used. The default value will be used where appropriate. The
    #: default value is 0.0.This argument is applicable only to some Abaqus/Standard elements.
    bendingHourglass: float = 0

    #: A Float specifying the drilling hourglass scaling factor. A value of zero indicates the
    #: default value should be used. The default value will be used where appropriate. The
    #: default value is 0.0.This argument is applicable only to some Abaqus/Standard elements.
    drillingHourglass: float = 0

    #: A SymbolicConstant specifying the kinematic split control. Possible values are
    #: AVERAGE_STRAIN, ORTHOGONAL, and CENTROID. The default value is AVERAGE_STRAIN.This
    #: argument is applicable only to some Abaqus/Explicit elements.
    kinematicSplit: SymbolicConstant = AVERAGE_STRAIN

    #: A Boolean specifying whether to prevent negative element volumes or other excessive
    #: distortions in crushable materials. The default value is OFF.This argument is applicable
    #: only to some Abaqus/Explicit elements.
    distortionControl: Boolean = OFF

    #: A Float specifying the length ratio for distortion control in crushable materials.
    #: Possible values are 0.0 ≤ **lengthRatio** ≤ 1.0. The default value is
    #: **lengthRatio** = 0.10.1This argument is applicable only when **distortionControl** is ON.
    lengthRatio: float = ON

    #: A Boolean specifying the second-order accuracy option. The default value is OFF.This
    #: argument is applicable only to some Abaqus/Explicit elements.
    secondOrderAccuracy: Boolean = OFF

    #: A SymbolicConstant specifying the hourglass control. Possible values are
    #: RELAX_STIFFNESS, STIFFNESS, VISCOUS, ENHANCED, and COMBINED. The default value is
    #: ENHANCED.This argument is applicable only to some Abaqus/Explicit elements.
    hourglassControl: SymbolicConstant = ENHANCED

    #: A Float specifying a weight factor when **hourglassControl** = COMBINED. The default value
    #: is 0.5.This argument is applicable only to some Abaqus/Explicit elements.
    weightFactor: float = 0

    #: A Float specifying the displacement hourglass scaling factor. The default value will be
    #: used where appropriate. The default value is 1.0.This argument is applicable only to
    #: some Abaqus/Explicit elements.
    displacementHourglass: float = 1

    #: A Float specifying the rotational hourglass scaling factor. The default value will be
    #: used where appropriate. The default value is 1.0.This argument is applicable only to
    #: some Abaqus/Explicit elements.
    rotationalHourglass: float = 1

    #: A Float specifying the out-of-plane displacement hourglass scaling factor. The default
    #: value will be used where appropriate. The default value is 1.0.This argument is
    #: applicable only to some Abaqus/Explicit elements.
    outOfPlaneDisplacementHourglass: float = 1

    #: A SymbolicConstant specifying the element deletion option. Possible values are DEFAULT,
    #: ON, and OFF. The default value is DEFAULT.
    elemDeletion: SymbolicConstant = DEFAULT

    #: A SymbolicConstant specifying the particle conversion option for smoothed particle
    #: hydrodynamics. When not OFF or DEFAULT this argument refers to the criterion used for
    #: conversion of elements to particles. Possible values are DEFAULT, OFF, TIME, STRAIN, and
    #: STRESS. The default value is DEFAULT.This argument is applicable only to some
    #: Abaqus/Explicit elements.
    particleConversion: SymbolicConstant = DEFAULT

    #: A Float specifying the threshold value for the particle conversion criterion specified
    #: by **particleConversion**. The default value is 0.0.This argument is applicable only to
    #: some Abaqus/Explicit elements.
    particleConversionThreshold: float = 0

    #: An Int specifying the number of particles per direction for element conversion when
    #: **particleConversion** is specified. The default value is 1.This argument is applicable
    #: only to some Abaqus/Explicit elements.
    particleConversionPPD: int = 1

    #: A SymbolicConstant specifying the interpolation function for particle conversion when
    #: **particleConversion** is specified. Possible values are CUBIC, QUADRATIC, and QUINTIC.
    #: The default value is CUBIC.This argument is applicable only to some Abaqus/Explicit
    #: elements.
    particleConversionKernel: SymbolicConstant = CUBIC

    #: A Float specifying the maximum degradation option for damage control. The default value
    #: is −1.0.
    maxDegradation: Optional[float] = None

    #: A Float specifying the viscosity option. The default value is 0.0.This argument is
    #: applicable only to some Abaqus/Standard elements.
    viscosity: float = 0

    #: A Float specifying the linear bulk viscosity scaling factor option for Abaqus/Explicit.
    #: The default value is 1.0.
    linearBulkViscosity: float = 1

    #: A Float specifying the quadratic bulk viscosity scaling factor option for
    #: Abaqus/Explicit. The default value is 1.0.
    quadraticBulkViscosity: float = 1

    #: A Float specifying the linear kinematic conversion value.This argument is applicable
    #: only to some Abaqus/Explicit elements.
    linearKinematicCtrl: Optional[float] = None

    #: A Float specifying the initial gap opening.This parameter is applicable only to some
    #: Abaqus/Standard elements.
    initialGapOpening: Optional[float] = None

    @abaqus_method_doc
    def __init__(
        self,
        elemCode: Literal[
            C.C3D8R, C.UNKNOWN_HEX, C.CODE, C.UNKNOWN_TET, C.UNKNOWN_TRI, C.UNKNOWN_WEDGE, C.UNKNOWN_QUAD
        ],
        elemLibrary: Literal[C.EXPLICIT, C.STANDARD] = STANDARD,
        hourglassStiffness: float = 0,
        bendingHourglass: float = 0,
        drillingHourglass: float = 0,
        kinematicSplit: Literal[C.ORTHOGONAL, C.AVERAGE_STRAIN, C.CENTROID] = AVERAGE_STRAIN,
        distortionControl: Boolean = OFF,
        lengthRatio: float = ON,
        secondOrderAccuracy: Boolean = OFF,
        hourglassControl: Literal[C.RELAX_STIFFNESS, C.COMBINED, C.VISCOUS, C.STIFFNESS, C.ENHANCED] = ENHANCED,
        weightFactor: float = 0,
        displacementHourglass: float = 1,
        rotationalHourglass: float = 1,
        outOfPlaneDisplacementHourglass: float = 1,
        elemDeletion: Literal[C.DEFAULT] = DEFAULT,
        particleConversion: Literal[C.TIME, C.STRESS, C.DEFAULT, C.STRAIN] = DEFAULT,
        particleConversionThreshold: float = 0,
        particleConversionPPD: int = 1,
        particleConversionKernel: Literal[C.QUADRATIC, C.CUBIC, C.QUINTIC] = CUBIC,
        maxDegradation: Optional[float] = None,
        viscosity: float = 0,
        linearBulkViscosity: float = 1,
        quadraticBulkViscosity: float = 1,
    ):
        """This method creates an ElemType object.

        .. note::
            This function can be accessed by::

                mesh.ElemType

        Parameters
        ----------
        elemCode
            A SymbolicConstant specifying the Abaqus element code or just the element shape.
            Possible values are:

            - C3D8R, specifying a 8-node linear brick, reduced integration with hourglass control.
            - CODE, specifying add more codes.
            - UNKNOWN_TRI, specifying an unknown element type associated with a triangular shape.
            - UNKNOWN_QUAD, specifying an unknown element type associated with a quadrilateral
              shape.
            - UNKNOWN_HEX, specifying an unknown element type associated with a hexahedral shape.
            - UNKNOWN_WEDGE, specifying an unknown element type associated with a wedge shape.
            - UNKNOWN_TET, specifying an unknown element type associated with a tetrahedral shape.
        elemLibrary
            A SymbolicConstant specifying the Abaqus element library to use. Possible values are
            STANDARD and EXPLICIT. The default value is STANDARD.
        hourglassStiffness
            A Float specifying the hourglass stiffness. (For shell elements this is the membrane
            hourglass stiffness.) A value of zero indicates the default value should be used. The
            default value will be used where appropriate. The default value is 0.0.This argument is
            applicable only to some Abaqus/Standard elements.
        bendingHourglass
            A Float specifying the bending hourglass stiffness. A value of zero indicates the
            default value should be used. The default value will be used where appropriate. The
            default value is 0.0.This argument is applicable only to some Abaqus/Standard elements.
        drillingHourglass
            A Float specifying the drilling hourglass scaling factor. A value of zero indicates the
            default value should be used. The default value will be used where appropriate. The
            default value is 0.0.This argument is applicable only to some Abaqus/Standard elements.
        kinematicSplit
            A SymbolicConstant specifying the kinematic split control. Possible values are
            AVERAGE_STRAIN, ORTHOGONAL, and CENTROID. The default value is AVERAGE_STRAIN.This
            argument is applicable only to some Abaqus/Explicit elements.
        distortionControl
            A Boolean specifying whether to prevent negative element volumes or other excessive
            distortions in crushable materials. The default value is OFF.This argument is applicable
            only to some Abaqus/Explicit elements.
        lengthRatio
            A Float specifying the length ratio for distortion control in crushable materials.
            Possible values are 0.0 ≤ **lengthRatio** ≤ 1.0. The default value is
            **lengthRatio** = 0.10.1This argument is applicable only when **distortionControl** is ON.
        secondOrderAccuracy
            A Boolean specifying the second-order accuracy option. The default value is OFF.This
            argument is applicable only to some Abaqus/Explicit elements.
        hourglassControl
            A SymbolicConstant specifying the hourglass control. Possible values are
            RELAX_STIFFNESS, STIFFNESS, VISCOUS, ENHANCED, and COMBINED. The default value is
            ENHANCED.This argument is applicable only to some Abaqus/Explicit elements.
        weightFactor
            A Float specifying a weight factor when **hourglassControl** = COMBINED. The default value
            is 0.5.This argument is applicable only to some Abaqus/Explicit elements.
        displacementHourglass
            A Float specifying the displacement hourglass scaling factor. The default value will be
            used where appropriate. The default value is 1.0.This argument is applicable only to
            some Abaqus/Explicit elements.
        rotationalHourglass
            A Float specifying the rotational hourglass scaling factor. The default value will be
            used where appropriate. The default value is 1.0.This argument is applicable only to
            some Abaqus/Explicit elements.
        outOfPlaneDisplacementHourglass
            A Float specifying the out-of-plane displacement hourglass scaling factor. The default
            value will be used where appropriate. The default value is 1.0.This argument is
            applicable only to some Abaqus/Explicit elements.
        elemDeletion
            A SymbolicConstant specifying the element deletion option. Possible values are DEFAULT,
            ON, and OFF. The default value is DEFAULT.
        particleConversion
            A SymbolicConstant specifying the particle conversion option for smoothed particle
            hydrodynamics. When not OFF or DEFAULT this argument refers to the criterion used for
            conversion of elements to particles. Possible values are DEFAULT, OFF, TIME, STRAIN, and
            STRESS. The default value is DEFAULT.This argument is applicable only to some
            Abaqus/Explicit elements.
        particleConversionThreshold
            A Float specifying the threshold value for the particle conversion criterion specified
            by **particleConversion**. The default value is 0.0.This argument is applicable only to
            some Abaqus/Explicit elements.
        particleConversionPPD
            An Int specifying the number of particles per direction for element conversion when
            **particleConversion** is specified. The default value is 1.This argument is applicable
            only to some Abaqus/Explicit elements.
        particleConversionKernel
            A SymbolicConstant specifying the interpolation function for particle conversion when
            **particleConversion** is specified. Possible values are CUBIC, QUADRATIC, and QUINTIC.
            The default value is CUBIC.This argument is applicable only to some Abaqus/Explicit
            elements.
        maxDegradation
            A Float specifying the maximum degradation option for damage control. The default value
            is −1.0.
        viscosity
            A Float specifying the viscosity option. The default value is 0.0.This argument is
            applicable only to some Abaqus/Standard elements.
        linearBulkViscosity
            A Float specifying the linear bulk viscosity scaling factor option for Abaqus/Explicit.
            The default value is 1.0.
        quadraticBulkViscosity
            A Float specifying the quadratic bulk viscosity scaling factor option for
            Abaqus/Explicit. The default value is 1.0.

        Returns
        -------
        elemType: ElemType
            An :py:class:`~abaqus.Mesh.ElemType.ElemType` object
        """
        ...
