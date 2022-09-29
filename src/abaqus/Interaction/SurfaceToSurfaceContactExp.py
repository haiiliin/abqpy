from typing import Union, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Interaction import Interaction
from ..Datum.DatumAxis import DatumAxis
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class SurfaceToSurfaceContactExp(Interaction):
    """The SurfaceToSurfaceContactExp object defines surface-to-surface contact during an
    Abaqus/Explicit analysis.
    The SurfaceToSurfaceContactExp object is derived from the Interaction object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactions[name]
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the step in which the SurfaceToSurfaceContactExp object
    #: is created.
    createStepName: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the main surface.
    #:
    #: .. versionchanged:: 2022
    #:     The attribute `master` was renamed to `main`.
    main: Region

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the secondary surface.
    #:
    #: .. versionchanged:: 2022
    #:     The attribute `slave` was renamed to `secondary`.
    secondary: Region

    #: A SymbolicConstant specifying the contact formulation. Possible values are FINITE and
    #: SMALL.
    sliding: SymbolicConstant

    #: A String specifying the name of the ContactProperty object associated with this
    #: interaction.
    interactionProperty: str

    #: A SymbolicConstant specifying the mechanical constraint formulation. Possible values are
    #: KINEMATIC and PENALTY. The default value is KINEMATIC.
    mechanicalConstraint: SymbolicConstant = KINEMATIC

    #: A SymbolicConstant specifying the weighting for node-to-face contact. Possible values
    #: are DEFAULT and SPECIFIED. The default value is DEFAULT.
    weightingFactorType: SymbolicConstant = DEFAULT

    #: A Float specifying the weighting factor for the contact surfaces when
    #: **weightingFactorType** = SPECIFIED. The default value is 0.0.
    weightingFactor: float = 0

    #: A String specifying the name of the ContactControl object associated with this
    #: interaction. An empty string indicates that the default contact controls will be used.
    #: The default value is an empty string.
    contactControls: str = ""

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

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        main: Region,
        secondary: Region,
        sliding: SymbolicConstant,
        interactionProperty: str,
        mechanicalConstraint: SymbolicConstant = KINEMATIC,
        weightingFactorType: SymbolicConstant = DEFAULT,
        weightingFactor: float = 0,
        contactControls: str = "",
        initialClearance: Union[SymbolicConstant, float] = OMIT,
        halfThreadAngle: Optional[str] = None,
        pitch: Optional[str] = None,
        majorBoltDiameter: Union[SymbolicConstant, float] = COMPUTED,
        meanBoltDiameter: Union[SymbolicConstant, float] = COMPUTED,
        datumAxis: Optional[DatumAxis] = None, 
        useReverseDatumAxis: Boolean = OFF,
        clearanceRegion: Optional[Region] = None,
    ):
        """This method creates a SurfaceToSurfaceContactExp object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].SurfaceToSurfaceContactExp

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the SurfaceToSurfaceContactExp object
            is created.
        main
            A :py:class:`~abaqus.Region.Region.Region` object specifying the main surface.

            .. versionchanged:: 2022
                The argument `master` was renamed to `main`.
        secondary
            A :py:class:`~abaqus.Region.Region.Region` object specifying the secondary surface.

            .. versionchanged:: 2022
                The argument `slave` was renamed to `secondary`.
        sliding
            A SymbolicConstant specifying the contact formulation. Possible values are FINITE and
            SMALL.
        interactionProperty
            A String specifying the name of the ContactProperty object associated with this
            interaction.
        mechanicalConstraint
            A SymbolicConstant specifying the mechanical constraint formulation. Possible values are
            KINEMATIC and PENALTY. The default value is KINEMATIC.
        weightingFactorType
            A SymbolicConstant specifying the weighting for node-to-face contact. Possible values
            are DEFAULT and SPECIFIED. The default value is DEFAULT.
        weightingFactor
            A Float specifying the weighting factor for the contact surfaces when
            **weightingFactorType** = SPECIFIED. The default value is 0.0.
        contactControls
            A String specifying the name of the ContactControl object associated with this
            interaction. An empty string indicates that the default contact controls will be used.
            The default value is an empty string.
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

        Returns
        -------
        SurfaceToSurfaceContactExp
            A :py:class:`~abaqus.Interaction.SurfaceToSurfaceContactExp.SurfaceToSurfaceContactExp` object.
        """
        super().__init__()

    @abaqus_method_doc
    def swapSurfaces(self):
        """This method switches the main and secondary surfaces of a surface-to-surface contact
        pair. This command is valid only during the step in which the interaction is created.

        .. versionchanged:: 2022
            Master and slave were changed to main and secondary.
        """
        ...

    @abaqus_method_doc
    def setValues(
        self,
        mechanicalConstraint: SymbolicConstant = KINEMATIC,
        weightingFactorType: SymbolicConstant = DEFAULT,
        weightingFactor: float = 0,
        contactControls: str = "",
        initialClearance: Union[SymbolicConstant, float] = OMIT,
        halfThreadAngle: Optional[str] = None,
        pitch: Optional[str] = None,
        majorBoltDiameter: Union[SymbolicConstant, float] = COMPUTED,
        meanBoltDiameter: Union[SymbolicConstant, float] = COMPUTED,
        datumAxis: Optional[DatumAxis] = None, 
        useReverseDatumAxis: Boolean = OFF,
        clearanceRegion: Optional[Region] = None,
    ):
        """This method modifies the data for an existing SurfaceToSurfaceContactExp object in the
        step where it is created.

        Parameters
        ----------
        mechanicalConstraint
            A SymbolicConstant specifying the mechanical constraint formulation. Possible values are
            KINEMATIC and PENALTY. The default value is KINEMATIC.
        weightingFactorType
            A SymbolicConstant specifying the weighting for node-to-face contact. Possible values
            are DEFAULT and SPECIFIED. The default value is DEFAULT.
        weightingFactor
            A Float specifying the weighting factor for the contact surfaces when
            **weightingFactorType** = SPECIFIED. The default value is 0.0.
        contactControls
            A String specifying the name of the ContactControl object associated with this
            interaction. An empty string indicates that the default contact controls will be used.
            The default value is an empty string.
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
        """
        ...

    @abaqus_method_doc
    def setValuesInStep(
        self, stepName: str, interactionProperty: str = "", contactControls: str = ""
    ):
        """This method modifies the propagating data for an existing SurfaceToSurfaceContactExp
        object in the specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified.
        interactionProperty
            A String specifying the name of the ContactProperty object associated with this
            interaction.
        contactControls
            A String specifying the name of the ContactControl object associated with this
            interaction. An empty string indicates that the default contact controls will be used.
            The default value is an empty string.
        """
        ...
