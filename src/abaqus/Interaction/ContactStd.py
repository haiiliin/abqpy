import typing

from abaqusConstants import *
from .ContactPropertyAssignment import ContactPropertyAssignment
from .InitializationAssignment import InitializationAssignment
from .Interaction import Interaction
from .MasterSlaveAssignment import MasterSlaveAssignment
from .RegionPairs import RegionPairs
from .SlidingTransitionAssignment import SlidingTransitionAssignment
from .SmoothingAssignment import SmoothingAssignment
from .StabilizationAssignment import StabilizationAssignment
from .SurfaceFeatureAssignment import SurfaceFeatureAssignment
from .SurfaceOffsetAssignment import SurfaceOffsetAssignment
from .SurfaceThicknessAssignment import SurfaceThicknessAssignment


class ContactStd(Interaction):
    """The ContactStd object defines the contact domain and associated properties during
    contact in an Abaqus/Standard analysis.
    The ContactStd object is derived from the Interaction object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import interaction
            mdb.models[name].interactions[name]

        The corresponding analysis keywords are:

        - CONTACT
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A Boolean specifying whether surface smoothing (geometric correction) is automatically
    #: applied to all eligible surfaces. The default value is ON.
    globalSmoothing: Boolean = ON

    #: A :py:class:`~abaqus.Interaction.RegionPairs.RegionPairs` object specifying the domain pairs included in contact.
    includedPairs: RegionPairs = RegionPairs()

    #: A :py:class:`~abaqus.Interaction.RegionPairs.RegionPairs` object specifying the domain pairs excluded from contact.
    excludedPairs: RegionPairs = RegionPairs()

    #: A :py:class:`~abaqus.Interaction.ContactPropertyAssignment.ContactPropertyAssignment` object specifying the contact property assignments in the
    #: contact domain.
    contactPropertyAssignments: ContactPropertyAssignment = ContactPropertyAssignment()

    #: A :py:class:`~abaqus.Interaction.SurfaceThicknessAssignment.SurfaceThicknessAssignment` object specifying the surface thickness assignments in the
    #: contact domain.
    surfaceThicknessAssignments: SurfaceThicknessAssignment = (
        SurfaceThicknessAssignment()
    )

    #: A :py:class:`~abaqus.Interaction.SurfaceOffsetAssignment.SurfaceOffsetAssignment` object specifying the surface offset fraction assignments in
    #: the contact domain.
    surfaceOffsetAssignments: SurfaceOffsetAssignment = SurfaceOffsetAssignment()

    #: A :py:class:`~abaqus.Interaction.MasterSlaveAssignment.MasterSlaveAssignment` object specifying the master-slave assignments in the
    #: contact domain.
    masterSlaveAssignments: MasterSlaveAssignment = MasterSlaveAssignment()

    #: An :py:class:`~abaqus.Interaction.InitializationAssignment.InitializationAssignment` object specifying the contact initialization assignments in
    #: the contact domain.
    initializationAssignments: InitializationAssignment = InitializationAssignment()

    #: A :py:class:`~abaqus.Interaction.StabilizationAssignment.StabilizationAssignment` object specifying the contact stabilization assignments in the
    #: contact domain.
    stabilizationAssignments: StabilizationAssignment = StabilizationAssignment()

    #: A :py:class:`~abaqus.Interaction.SmoothingAssignment.SmoothingAssignment` object specifying the surface smoothing assignments in the contact
    #: domain.
    smoothingAssignments: SmoothingAssignment = SmoothingAssignment()

    #: A :py:class:`~abaqus.Interaction.SurfaceFeatureAssignment.SurfaceFeatureAssignment` object specifying the surface feature angle assignments in
    #: the contact domain.
    surfaceFeatureAssignments: SurfaceFeatureAssignment = SurfaceFeatureAssignment()

    #: A SlidingTransitionAssignments object specifying the sliding transition assignments in
    #: the contact domain.
    slidingTransitionAssignments: SlidingTransitionAssignment = (
        SlidingTransitionAssignment()
    )

    #: A Boolean specifying whether to assign the edge-to-edge formulation. The default value
    #: is False.
    assignEdgeToEdgeformulation: Boolean = False

    #: A symbolic constant specifying edge-to-edge formulation. The default value is NO.
    edgeToEdgeFormulation: str = NO

    @typing.overload
    def __init__(
        self,
        name: str,
        createStepName: str,
        useAllstar: Boolean = OFF,
        globalSmoothing: Boolean = ON,
        includedPairs: RegionPairs = None, 
        excludedPairs: RegionPairs = None, 
        contactPropertyAssignments: ContactPropertyAssignment = None, 
        surfaceThicknessAssignments: SurfaceThicknessAssignment = None, 
        surfaceOffsetAssignments: SurfaceOffsetAssignment = None,
        surfaceFeatureAssignments: SurfaceFeatureAssignment = None,
        masterSlaveAssignments: MasterSlaveAssignment = None,
        initializationAssignments: InitializationAssignment = None, 
        stabilizationAssignments: StabilizationAssignment = None, 
        smoothingAssignments: SmoothingAssignment = None, 
        slidingTransitionAssignments: SlidingTransitionAssignment = None, 
    ):
        """This method creates a ContactStd object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].ContactStd

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which this contact interaction is created.
        useAllstar
            A Boolean specifying whether the contacting surface pairs consist of all exterior faces
            in the model.
        globalSmoothing
            A Boolean specifying whether surface smoothing (geometric correction) is automatically
            applied to all eligible surfaces. The default value is ON.
        includedPairs
            A :py:class:`~abaqus.Interaction.RegionPairs.RegionPairs` object specifying the domain pairs included in contact.
        excludedPairs
            A :py:class:`~abaqus.Interaction.RegionPairs.RegionPairs` object specifying the domain pairs excluded from contact.
        contactPropertyAssignments
            A :py:class:`~abaqus.Interaction.ContactPropertyAssignment.ContactPropertyAssignment` object specifying the contact property assignments in the
            contact domain.
        surfaceThicknessAssignments
            A :py:class:`~abaqus.Interaction.SurfaceThicknessAssignment.SurfaceThicknessAssignment` object specifying the surface thickness assignments in the
            contact domain.
        surfaceOffsetAssignments
            A :py:class:`~abaqus.Interaction.SurfaceOffsetAssignment.SurfaceOffsetAssignment` object specifying the surface offset fraction assignments in
            the contact domain.
        surfaceFeatureAssignments
            A :py:class:`~abaqus.Interaction.SurfaceFeatureAssignment.SurfaceFeatureAssignment` object specifying the surface feature angle assignments in
            the contact domain.
        masterSlaveAssignments
            A :py:class:`~abaqus.Interaction.MasterSlaveAssignment.MasterSlaveAssignment` object specifying the master-slave assignments in the
            contact domain.
        initializationAssignments
            An :py:class:`~abaqus.Interaction.InitializationAssignment.InitializationAssignment` object specifying the contact initialization assignments in
            the contact domain.
        stabilizationAssignments
            A :py:class:`~abaqus.Interaction.StabilizationAssignment.StabilizationAssignment` object specifying the contact stabilization assignments in the
            contact domain.
        smoothingAssignments
            A :py:class:`~abaqus.Interaction.SmoothingAssignment.SmoothingAssignment` object specifying the surface smoothing assignments in the contact
            domain.
        slidingTransitionAssignments
            A SlidingTransitionAssignments object specifying the sliding transition assignments in
            the contact domain.

        Returns
        -------
        ContactStd
            A :py:class:`~abaqus.Interaction.ContactStd.ContactStd` object.
        """
        super().__init__()
        ...

    @typing.overload
    def __init__(
        self,
        name: str,
        createStepName: str,
        globalSmoothing: Boolean = ON,
        useAllstar: Boolean = OFF,
        includedPairs: SymbolicConstant = None,
        excludedPairs: SymbolicConstant = None,
        contactPropertyAssignments: SymbolicConstant = None,
        surfaceFeatureAssignments: typing.Union[SymbolicConstant, float] = GLOBAL,
        surfaceThicknessAssignments: typing.Union[SymbolicConstant, float] = GLOBAL,
        surfaceOffsetAssignments: typing.Union[SymbolicConstant, float] = GLOBAL,
        masterSlaveAssignments: SymbolicConstant = None,
        initializationAssignments: SymbolicConstant = None,
        stabilizationAssignments: SymbolicConstant = None,
        smoothingAssignments: SymbolicConstant = None,
        slidingTransitionAssignments: SymbolicConstant = None,
    ):
        """This method creates a ContactStd object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].ContactStd

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which this contact interaction is created.
        globalSmoothing
            A Boolean specifying whether surface smoothing (geometric correction) is automatically
            applied to all eligible surfaces. The default value is ON.
        useAllstar
            A Boolean specifying whether the contacting surface pairs consist of all exterior faces
            in the model.
        includedPairs
            A sequence of pairs of Region objects or SymbolicConstants that specifies the surface
            pairs in contact. Possible values of the SymbolicConstants are ALLSTAR and SELF. This
            argument is valid only when **useAllstar** = OFF.
        excludedPairs
            A sequence of pairs of Region objects or SymbolicConstants that specifies the surface
            pairs excluded from contact. Possible values of the SymbolicConstants are ALLSTAR and
            SELF.
        contactPropertyAssignments
            A sequence of tuples specifying the properties assigned to each surface pair. Each tuple
            contains three entries:
            - A :py:class:`~abaqus.Region.Region.Region` object or the SymbolicConstant GLOBAL.
            - A :py:class:`~abaqus.Region.Region.Region` object or the SymbolicConstant SELF.
            - A String specifying an InteractionProperty object associated with this pair of
              regions.
        surfaceFeatureAssignments
            A sequence of tuples specifying the surface feature angle assignments in the contact
            domain. Each tuple contains two entries:
            - A region object or the SymbolicConstant GLOBAL specifying the surface to which the
              surface feature angle is assigned.
            - A Float or a SymbolicConstant specifying the overriding feature angle value to be used
              in the contact definition. Possible values of the SymbolicConstant are PERIMETER or
              NONE.
        surfaceThicknessAssignments
            A sequence of tuples specifying the surface thickness assignments in the contact domain.
            Each tuple contains three entries:
            - A region object or the SymbolicConstant GLOBAL specifying the surface to which the
              surface thickness is assigned.
            - A Float or a SymbolicConstant specifying the overriding thickness value to be used in
              the contact definition. The SymbolicConstant ORIGINAL may be specified instead of a
              floating point value.
            - A Float specifying a scale factor that multiplies the thickness value specified in the
              second entry.
        surfaceOffsetAssignments
            A sequence of tuples specifying the surface offset fraction assignments in the contact
            domain. Each tuple contains two entries:
            - A region object or the SymbolicConstant GLOBAL specifying the surface to which the
              surface offset fraction is assigned.
            - A Float or a SymbolicConstant specifying the offset fraction value to be used in the
              contact definition. Possible values of the SymbolicConstant are ORIGINAL, SPOS, or SNEG.
        masterSlaveAssignments
            A sequence of tuples specifying master-slave assignments in the contact domain. Each
            tuple contains three entries:
            - A region object or the SymbolicConstant GLOBAL specifying the first surface that
              defines the master-slave assignment.
            - A region object specifying the second surface in the master-slave assignment
              definition.
            - A SymbolicConstant specifying the status of the first surface. Possible values are
              MAIN, SECONDARY, and BALANCED.
        initializationAssignments
            A sequence of tuples specifying the contact initialization data assigned to each surface
            pair. Each tuple contains three entries:
            - A :py:class:`~abaqus.Region.Region.Region` object or the SymbolicConstant GLOBAL.
            - A :py:class:`~abaqus.Region.Region.Region` object or the SymbolicConstant SELF.
            - A String specifying a StdStabilization object associated with this pair of regions.
        stabilizationAssignments
            A sequence of tuples specifying the contact stabilization assigned to each surface pair.
            Each tuple contains three entries:
            - A :py:class:`~abaqus.Region.Region.Region` object or the SymbolicConstant GLOBAL.
            - A :py:class:`~abaqus.Region.Region.Region` object or the SymbolicConstant SELF.
            - A String specifying a StdStabilization object associated with this pair of regions.
        smoothingAssignments
            A sequence of tuples specifying the surface smoothing assignments in the contact domain.
            Each tuple contains two entries:
            - A region object specifying the surface to which the smoothing option is assigned.
            - A SymbolicConstant specifying the smoothing option to be used in the contact
              definition. Possible values of the SymbolicConstant are NONE, REVOLUTION, SPHERICAL, or
            TOROIDAL.
        slidingTransitionAssignments
            A sequence of tuples specifying sliding transition assignments in the contact domain.
            Each tuple contains three entries:
            - A region object or the SymbolicConstant GLOBAL specifying the first surface that
              defines the sliding transition assignment.
            - A region object specifying the second surface in the sliding transition assignment
              definition.
            - A SymbolicConstant specifying the smoothness value. Possible values are
              ELEMENT_ORDER_SMOOTHING, LINEAR_SMOOTHING, and QUADRATIC_SMOOTHING.

        Returns
        -------
        ContactStd
            A :py:class:`~abaqus.Interaction.ContactStd.ContactStd` object.
        """
        super().__init__()
        ...

    def __init__(self, *args, **kwargs):
        ...
