from typing_extensions import Literal
from typing import Union, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Interaction import Interaction
from ..Datum.DatumAxis import DatumAxis
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import (Boolean, COMPUTED, NONE, OFF, OMIT, ON, RIGHT,
                                              SELECTIVE, SURFACE_TO_SURFACE, SymbolicConstant,
                                              TWO_CONFIG)


@abaqus_class_doc
class SurfaceToSurfaceContactStd(Interaction):
    """The SurfaceToSurfaceContactStd object defines surface-to-surface contact during an
    Abaqus/Standard analysis.
    The SurfaceToSurfaceContactStd object is derived from the Interaction object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name]
    """

    #: A SymbolicConstant specifying the choice of contact tracking algorithm. The STATE
    #: tracking algorithm uses only normal projections and is specified by using ONE_CONFIG.
    #: The PATH tracking algorithm uses crossing and normal projections and is specified by
    #: using TWO_CONFIG. Possible values are ONE_CONFIG and TWO_CONFIG. The default value is
    #: TWO_CONFIG.This argument is valid only when **sliding** = FINITE and
    #: **enforcement** = SURFACE_TO_SURFACE.
    contactTracking: SymbolicConstant = TWO_CONFIG

    #: A SymbolicConstant specifying the manner in which midface constraints are employed.
    #: Possible values are SELECTIVE, NEVER, and ALWAYS. The default value is SELECTIVE.This
    #: argument is not valid when **sliding** = FINITE and **enforcement** = SURFACE_TO_SURFACE.
    supplementaryContact: SymbolicConstant = SELECTIVE

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the step in which the SurfaceToSurfaceContactStd object
    #: is created.
    createStepName: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the main surface.
    master: Region

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the secondary surface.
    slave: Region

    #: A SymbolicConstant specifying the contact formulation. Possible values are FINITE and
    #: SMALL.
    sliding: SymbolicConstant

    #: A String specifying the name of the ContactProperty object associated with this
    #: interaction.
    interactionProperty: str

    #: A SymbolicConstant specifying the type of time-dependent allowable interference for
    #: contact pairs and contact elements. Possible values are:
    

    #: - NONE, specifying no allowable contact interference.
    #: - SHRINK_FIT.
    #: - UNIFORM.
    #: 
    #: The default value is NONE.
    interferenceType: SymbolicConstant = NONE

    #: A Float specifying the maximum overclosure distance allowed. This argument applies only
    #: when **interferenceType** = UNIFORM. The default value is 0.0.
    overclosure: float = 0

    #: A SymbolicConstant specifying the method used to determine the interference direction.
    #: Possible values are COMPUTED and DIRECTION_COSINE. The default value is COMPUTED.
    interferenceDirectionType: SymbolicConstant = COMPUTED

    #: A sequence of three Floats specifying the following:
    #: 
    #: - XX-direction cosine of the interference direction vector.
    #: - YY-direction cosine of the interference direction vector.
    #: - ZZ-direction cosine of the interference direction vector.
    #: 
    #: This argument is required only when **interferenceDirectionType** = DIRECTION_COSINE.
    direction: tuple = ()

    #: A String specifying the name of the amplitude curve that defines the magnitude of the
    #: prescribed interference during the step. Use None to specify that the prescribed
    #: interference is applied immediately at the beginning of the step and ramped down to zero
    #: linearly over the step.
    amplitude: str = ""

    #: A Float specifying the degree of smoothing used for deformable or rigid main surfaces
    #: involved when **enforcement** = NODE_TO_SURFACE. The value given must lie between 0.0 and
    #: 0.5. The default value is 0.2.
    smooth: float = 0

    #: A Float specifying the distance by which a secondary node must penetrate the main
    #: surface before Abaqus/Standard abandons the current increment and tries again with a
    #: smaller increment. The default value is 0.0.
    hcrit: float = 0

    #: A Float specifying a fraction of the end segment or facet edge length by which the main
    #: surface is to be extended to avoid numerical round-off errors associated with contact
    #: modeling. The value given must lie between 0.0 and 0.2. The default value is 0.1.
    extensionZone: float = 0

    #: A SymbolicConstant specifying the adjust method. Possible values are NONE, OVERCLOSED,
    #: TOLERANCE, and SET. The default value is NONE.
    adjustMethod: SymbolicConstant = NONE

    #: A Float specifying the adjust tolerance. The default value is 0.0.
    adjustTolerance: float = 0

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the Set object to which the adjustment is to be applied.
    adjustSet: Optional[Region] = None

    #: A SymbolicConstant specifying the discretization method. Possible values are
    #: NODE_TO_SURFACE and SURFACE_TO_SURFACE. The default value is SURFACE_TO_SURFACE.
    enforcement: SymbolicConstant = SURFACE_TO_SURFACE

    #: A Boolean specifying whether shell/membrane element thickness is considered. The default
    #: value is ON.This argument is not valid when **sliding** = FINITE and
    #: **enforcement** = NODE_TO_SURFACE.
    thickness: Boolean = ON

    #: A String specifying the name of the ContactControl object associated with this
    #: interaction. The empty string indicates that the default contact controls will be used.
    #: The default value is an empty string.
    contactControls: str = ""

    #: A Boolean specifying whether the surfaces are to be "tied" together for the duration of
    #: the simulation. The default value is OFF.
    tied: Boolean = OFF

    #: A SymbolicConstant or a Float specifying the initial clearance at regions of contact.
    #: Possible values are OMIT and COMPUTED. The default value is OMIT.
    initialClearance: Union[SymbolicConstant, float] = OMIT

    #: None or a sequence of Floats specifying the half thread angle used for bolt clearance.
    #: The default value is None.
    halfThreadAngle: Optional[str] = None

    #: None or a sequence of Floats specifying the pitch used for bolt clearance. The default
    #: value is None.
    pitch: Optional[str] = None

    #: The SymbolicConstant COMPUTED or a Float specifying the major diameter of the bolt used
    #: for bolt clearance. The default value is COMPUTED.
    majorBoltDiameter: Union[SymbolicConstant, float] = COMPUTED

    #: The SymbolicConstant COMPUTED or a Float specifying the mean diameter of the bolt used
    #: for bolt clearance. The default value is COMPUTED.
    meanBoltDiameter: Union[SymbolicConstant, float] = COMPUTED

    #: A :py:class:`~abaqus.Datum.DatumAxis.DatumAxis` object specifying the orientation of the bolt hole when specifying bolt
    #: clearance.
    datumAxis: Optional[DatumAxis] = None

    #: A Boolean specifying whether to reverse the bolt clearance direction given by the datum
    #: axis. The default value is OFF.
    useReverseDatumAxis: Boolean = OFF

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the contact region for which clearance is specified.
    clearanceRegion: Optional[Region] = None

    #: A SymbolicConstant specifying whether to use surface smoothing for geometric surfaces in
    #: SurfaceToSurfaceContactStd interactions. Possible values are AUTOMATIC and NONE. The
    #: default value is NONE.
    surfaceSmoothing: SymbolicConstant = NONE

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the secondary node sub-set for bonding, used only when the
    #: contact property CohesiveBehavior option specifies use.
    bondingSet: Optional[Region] = None

    #: A SymbolicConstant specifying the bolt handedness formulation. Possible values are RIGHT
    #: and LEFT. The default value is RIGHT.
    #:
    #: .. versionadded:: 2019
    #:     The `handedness` attribute was added.
    handedness: SymbolicConstant = RIGHT

    #: A SymbolicConstant specifying the bolt normal adjustment formulation for all secondary
    #: nodes. Possible values are UNIFORM AXIAL COMPONENT and LOCATION DEPENDENT. The default
    #: value is UNIFORM AXIAL COMPONENT.
    #:
    #: .. versionadded:: 2019
    #:     The `normalAdjustment` attribute was added.
    normalAdjustment: SymbolicConstant = NONE

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        master: Region,
        slave: Region,
        sliding: Literal[C.SMALL, C.FINITE],
        interactionProperty: str,
        interferenceType: Literal[C.UNIFORM, C.NONE, C.SHRINK_FIT] = NONE,
        overclosure: float = 0,
        interferenceDirectionType: Literal[C.COMPUTED, C.DIRECTION_COSINE] = COMPUTED,
        direction: tuple = (),
        amplitude: str = "",
        smooth: float = 0,
        hcrit: float = 0,
        extensionZone: float = 0,
        adjustMethod: Literal[C.SET, C.TOLERANCE, C.OVERCLOSED, C.NONE] = NONE,
        adjustTolerance: float = 0,
        adjustSet: Optional[Region] = None,
        enforcement: Literal[C.NODE_TO_SURFACE, C.SURFACE_TO_SURFACE] = SURFACE_TO_SURFACE,
        thickness: Boolean = ON,
        contactControls: str = "",
        tied: Boolean = OFF,
        initialClearance: Union[Literal[C.OMIT, C.COMPUTED], float] = OMIT,
        halfThreadAngle: Optional[str] = None,
        pitch: Optional[str] = None,
        majorBoltDiameter: Union[Literal[C.COMPUTED], float] = COMPUTED,
        meanBoltDiameter: Union[Literal[C.COMPUTED], float] = COMPUTED,
        datumAxis: Optional[DatumAxis] = None, 
        useReverseDatumAxis: Boolean = OFF,
        clearanceRegion: Optional[Region] = None,
        surfaceSmoothing: Literal[C.AUTOMATIC, C.NONE] = NONE,
        bondingSet: Optional[Region] = None,
        handedness: Literal[C.RIGHT, C.LEFT] = RIGHT,
        normalAdjustment: Optional[Literal[C.AXIAL, C.LOCATION, C.COMPONENT, C.UNIFORM, C.DEPENDENT]] = None,
    ):
        """This method creates a SurfaceToSurfaceContactStd object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].SurfaceToSurfaceContactStd

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the SurfaceToSurfaceContactStd object
            is created.
        master
            A :py:class:`~abaqus.Region.Region.Region` object specifying the main surface.
        slave
            A :py:class:`~abaqus.Region.Region.Region` object specifying the secondary surface.
        sliding
            A SymbolicConstant specifying the contact formulation. Possible values are FINITE and
            SMALL.
        interactionProperty
            A String specifying the name of the ContactProperty object associated with this
            interaction.
        interferenceType
            A SymbolicConstant specifying the type of time-dependent allowable interference for
            contact pairs and contact elements. Possible values are:

            - NONE, specifying no allowable contact interference.
            - SHRINK_FIT.
            - UNIFORM.
            
            The default value is NONE.
        overclosure
            A Float specifying the maximum overclosure distance allowed. This argument applies only
            when **interferenceType** = UNIFORM. The default value is 0.0.
        interferenceDirectionType
            A SymbolicConstant specifying the method used to determine the interference direction.
            Possible values are COMPUTED and DIRECTION_COSINE. The default value is COMPUTED.
        direction
            A sequence of three Floats specifying the following:
            
            - XX-direction cosine of the interference direction vector.
            - YY-direction cosine of the interference direction vector.
            - ZZ-direction cosine of the interference direction vector.
            
            This argument is required only when **interferenceDirectionType** = DIRECTION_COSINE.
        amplitude
            A String specifying the name of the amplitude curve that defines the magnitude of the
            prescribed interference during the step. Use None to specify that the prescribed
            interference is applied immediately at the beginning of the step and ramped down to zero
            linearly over the step.
        smooth
            A Float specifying the degree of smoothing used for deformable or rigid main surfaces
            involved when **enforcement** = NODE_TO_SURFACE. The value given must lie between 0.0 and
            0.5. The default value is 0.2.
        hcrit
            A Float specifying the distance by which a secondary node must penetrate the main
            surface before Abaqus/Standard abandons the current increment and tries again with a
            smaller increment. The default value is 0.0.
        extensionZone
            A Float specifying a fraction of the end segment or facet edge length by which the main
            surface is to be extended to avoid numerical round-off errors associated with contact
            modeling. The value given must lie between 0.0 and 0.2. The default value is 0.1.
        adjustMethod
            A SymbolicConstant specifying the adjust method. Possible values are NONE, OVERCLOSED,
            TOLERANCE, and SET. The default value is NONE.
        adjustTolerance
            A Float specifying the adjust tolerance. The default value is 0.0.
        adjustSet
            A :py:class:`~abaqus.Region.Region.Region` object specifying the Set object to which the adjustment is to be applied.
        enforcement
            A SymbolicConstant specifying the discretization method. Possible values are
            NODE_TO_SURFACE and SURFACE_TO_SURFACE. The default value is SURFACE_TO_SURFACE.
        thickness
            A Boolean specifying whether shell/membrane element thickness is considered. The default
            value is ON.This argument is not valid when **sliding** = FINITE and
            **enforcement** = NODE_TO_SURFACE.
        contactControls
            A String specifying the name of the ContactControl object associated with this
            interaction. The empty string indicates that the default contact controls will be used.
            The default value is an empty string.
        tied
            A Boolean specifying whether the surfaces are to be "tied" together for the duration of
            the simulation. The default value is OFF.
        initialClearance
            A SymbolicConstant or a Float specifying the initial clearance at regions of contact.
            Possible values are OMIT and COMPUTED. The default value is OMIT.
        halfThreadAngle
            None or a sequence of Floats specifying the half thread angle used for bolt clearance.
            The default value is None.
        pitch
            None or a sequence of Floats specifying the pitch used for bolt clearance. The default
            value is None.
        majorBoltDiameter
            The SymbolicConstant COMPUTED or a Float specifying the major diameter of the bolt used
            for bolt clearance. The default value is COMPUTED.
        meanBoltDiameter
            The SymbolicConstant COMPUTED or a Float specifying the mean diameter of the bolt used
            for bolt clearance. The default value is COMPUTED.
        datumAxis
            A :py:class:`~abaqus.Datum.DatumAxis.DatumAxis` object specifying the orientation of the bolt hole when specifying bolt
            clearance.
        useReverseDatumAxis
            A Boolean specifying whether to reverse the bolt clearance direction given by the datum
            axis. The default value is OFF.
        clearanceRegion
            A :py:class:`~abaqus.Region.Region.Region` object specifying the contact region for which clearance is specified.
        surfaceSmoothing
            A SymbolicConstant specifying whether to use surface smoothing for geometric surfaces in
            SurfaceToSurfaceContactStd interactions. Possible values are AUTOMATIC and NONE. The
            default value is NONE.
        bondingSet
            A :py:class:`~abaqus.Region.Region.Region` object specifying the secondary node sub-set for bonding, used only when the
            contact property CohesiveBehavior option specifies use.
        handedness
            A SymbolicConstant specifying the bolt handedness formulation. Possible values are RIGHT
            and LEFT. The default value is RIGHT.

            .. versionadded:: 2019
                The `normalAdjustment` argument was added.
        normalAdjustment
            A SymbolicConstant specifying the bolt normal adjustment formulation for all secondary
            nodes. Possible values are UNIFORM AXIAL COMPONENT and LOCATION DEPENDENT. The default
            value is UNIFORM AXIAL COMPONENT.

            .. versionadded:: 2019
                The `normalAdjustment` argument was added.

        Returns
        -------
        SurfaceToSurfaceContactStd
            A :py:class:`~abaqus.Interaction.SurfaceToSurfaceContactStd.SurfaceToSurfaceContactStd` object.
        """
        super().__init__()

    @abaqus_method_doc
    def swapSurfaces(self):
        """This method switches the main and secondary surfaces of a surface-to-surface contact
        pair. This command is valid only for the step in which the interaction is created.

        .. versionchanged:: 2022
            Master and slave were changed to main and secondary.
        """
        ...

    @abaqus_method_doc
    def setValues(
        self,
        interferenceType: Literal[C.UNIFORM, C.NONE, C.SHRINK_FIT] = NONE,
        overclosure: float = 0,
        interferenceDirectionType: Literal[C.COMPUTED, C.DIRECTION_COSINE] = COMPUTED,
        direction: tuple = (),
        amplitude: str = "",
        smooth: float = 0,
        hcrit: float = 0,
        extensionZone: float = 0,
        adjustMethod: Literal[C.SET, C.TOLERANCE, C.OVERCLOSED, C.NONE] = NONE,
        adjustTolerance: float = 0,
        adjustSet: Optional[Region] = None,
        enforcement: Literal[C.NODE_TO_SURFACE, C.SURFACE_TO_SURFACE] = SURFACE_TO_SURFACE,
        thickness: Boolean = ON,
        contactControls: str = "",
        tied: Boolean = OFF,
        initialClearance: Union[Literal[C.OMIT, C.COMPUTED], float] = OMIT,
        halfThreadAngle: Optional[str] = None,
        pitch: Optional[str] = None,
        majorBoltDiameter: Union[Literal[C.COMPUTED], float] = COMPUTED,
        meanBoltDiameter: Union[Literal[C.COMPUTED], float] = COMPUTED,
        datumAxis: Optional[DatumAxis] = None, 
        useReverseDatumAxis: Boolean = OFF,
        clearanceRegion: Optional[Region] = None,
        surfaceSmoothing: Literal[C.AUTOMATIC, C.NONE] = NONE,
        bondingSet: Optional[Region] = None,
        handedness: Literal[C.RIGHT, C.LEFT] = RIGHT,
        normalAdjustment: Optional[Literal[C.AXIAL, C.LOCATION, C.COMPONENT, C.UNIFORM, C.DEPENDENT]] = None,
    ):
        """This method modifies the data for an existing SurfaceToSurfaceContactStd object in the
        step where it is created.

        Parameters
        ----------
        interferenceType
            A SymbolicConstant specifying the type of time-dependent allowable interference for
            contact pairs and contact elements. Possible values are:

            - NONE, specifying no allowable contact interference.
            - SHRINK_FIT.
            - UNIFORM.
            
            The default value is NONE.
        overclosure
            A Float specifying the maximum overclosure distance allowed. This argument applies only
            when **interferenceType** = UNIFORM. The default value is 0.0.
        interferenceDirectionType
            A SymbolicConstant specifying the method used to determine the interference direction.
            Possible values are COMPUTED and DIRECTION_COSINE. The default value is COMPUTED.
        direction
            A sequence of three Floats specifying the following:
            
            - XX-direction cosine of the interference direction vector.
            - YY-direction cosine of the interference direction vector.
            - ZZ-direction cosine of the interference direction vector.
            
            This argument is required only when **interferenceDirectionType** = DIRECTION_COSINE.
        amplitude
            A String specifying the name of the amplitude curve that defines the magnitude of the
            prescribed interference during the step. Use None to specify that the prescribed
            interference is applied immediately at the beginning of the step and ramped down to zero
            linearly over the step.
        smooth
            A Float specifying the degree of smoothing used for deformable or rigid main surfaces
            involved when **enforcement** = NODE_TO_SURFACE. The value given must lie between 0.0 and
            0.5. The default value is 0.2.
        hcrit
            A Float specifying the distance by which a secondary node must penetrate the main
            surface before Abaqus/Standard abandons the current increment and tries again with a
            smaller increment. The default value is 0.0.
        extensionZone
            A Float specifying a fraction of the end segment or facet edge length by which the main
            surface is to be extended to avoid numerical round-off errors associated with contact
            modeling. The value given must lie between 0.0 and 0.2. The default value is 0.1.
        adjustMethod
            A SymbolicConstant specifying the adjust method. Possible values are NONE, OVERCLOSED,
            TOLERANCE, and SET. The default value is NONE.
        adjustTolerance
            A Float specifying the adjust tolerance. The default value is 0.0.
        adjustSet
            A :py:class:`~abaqus.Region.Region.Region` object specifying the Set object to which the adjustment is to be applied.
        enforcement
            A SymbolicConstant specifying the discretization method. Possible values are
            NODE_TO_SURFACE and SURFACE_TO_SURFACE. The default value is SURFACE_TO_SURFACE.
        thickness
            A Boolean specifying whether shell/membrane element thickness is considered. The default
            value is ON.This argument is not valid when **sliding** = FINITE and
            **enforcement** = NODE_TO_SURFACE.
        contactControls
            A String specifying the name of the ContactControl object associated with this
            interaction. The empty string indicates that the default contact controls will be used.
            The default value is an empty string.
        tied
            A Boolean specifying whether the surfaces are to be "tied" together for the duration of
            the simulation. The default value is OFF.
        initialClearance
            A SymbolicConstant or a Float specifying the initial clearance at regions of contact.
            Possible values are OMIT and COMPUTED. The default value is OMIT.
        halfThreadAngle
            None or a sequence of Floats specifying the half thread angle used for bolt clearance.
            The default value is None.
        pitch
            None or a sequence of Floats specifying the pitch used for bolt clearance. The default
            value is None.
        majorBoltDiameter
            The SymbolicConstant COMPUTED or a Float specifying the major diameter of the bolt used
            for bolt clearance. The default value is COMPUTED.
        meanBoltDiameter
            The SymbolicConstant COMPUTED or a Float specifying the mean diameter of the bolt used
            for bolt clearance. The default value is COMPUTED.
        datumAxis
            A :py:class:`~abaqus.Datum.DatumAxis.DatumAxis` object specifying the orientation of the bolt hole when specifying bolt
            clearance.
        useReverseDatumAxis
            A Boolean specifying whether to reverse the bolt clearance direction given by the datum
            axis. The default value is OFF.
        clearanceRegion
            A :py:class:`~abaqus.Region.Region.Region` object specifying the contact region for which clearance is specified.
        surfaceSmoothing
            A SymbolicConstant specifying whether to use surface smoothing for geometric surfaces in
            SurfaceToSurfaceContactStd interactions. Possible values are AUTOMATIC and NONE. The
            default value is NONE.
        bondingSet
            A :py:class:`~abaqus.Region.Region.Region` object specifying the secondary node sub-set for bonding, used only when the
            contact property CohesiveBehavior option specifies use.
        handedness
            A SymbolicConstant specifying the bolt handedness formulation. Possible values are RIGHT
            and LEFT. The default value is RIGHT.

            .. versionadded:: 2019
                The `normalAdjustment` argument was added.
        normalAdjustment
            A SymbolicConstant specifying the bolt normal adjustment formulation for all secondary
            nodes. Possible values are UNIFORM AXIAL COMPONENT and LOCATION DEPENDENT. The default
            value is UNIFORM AXIAL COMPONENT.

            .. versionadded:: 2019
                The `normalAdjustment` argument was added.
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self,
        stepName: str,
        interactionProperty: str = "",
        interferenceType: Literal[C.UNIFORM, C.NONE, C.SHRINK_FIT] = NONE,
        overclosure: float = 0,
        interferenceDirectionType: Literal[C.COMPUTED, C.DIRECTION_COSINE] = COMPUTED,
        direction: tuple = (),
        amplitude: str = "",
        contactControls: str = "",
    ):
        """This method modifies the propagating data for an existing SurfaceToSurfaceContactStd
        object in the specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified.
        interactionProperty
            A String specifying the name of the ContactProperty object associated with this
            interaction.
        interferenceType
            A SymbolicConstant specifying the type of time-dependent allowable interference for
            contact pairs and contact elements. Possible values are:

            - NONE, specifying no allowable contact interference.
            - SHRINK_FIT.
            - UNIFORM.
            
            The default value is NONE.
        overclosure
            A Float specifying the maximum overclosure distance allowed. This argument applies only
            when **interferenceType** = UNIFORM. The default value is 0.0.
        interferenceDirectionType
            A SymbolicConstant specifying the method used to determine the interference direction.
            Possible values are COMPUTED and DIRECTION_COSINE. The default value is COMPUTED.
        direction
            A sequence of three Floats specifying the following:
            
            - XX-direction cosine of the interference direction vector.
            - YY-direction cosine of the interference direction vector.
            - ZZ-direction cosine of the interference direction vector.
            
            This argument is required only when **interferenceDirectionType** = DIRECTION_COSINE.
        amplitude
            A String specifying the name of the amplitude curve that defines the magnitude of the
            prescribed interference during the step. Use None to specify that the prescribed
            interference is applied immediately at the beginning of the step and ramped down to zero
            linearly over the step.
        contactControls
            A String specifying the name of the ContactControl object associated with this
            interaction. The empty string indicates that the default contact controls will be used.
            The default value is an empty string.
        """
        ...
