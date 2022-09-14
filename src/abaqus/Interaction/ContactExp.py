import typing

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ContactPropertyAssignment import ContactPropertyAssignment
from .Interaction import Interaction
from .MainSecondaryAssignment import MainSecondaryAssignment
from .PolarityAssignments import PolarityAssignments
from .RegionPairs import RegionPairs
from .SmoothingAssignment import SmoothingAssignment
from .SurfaceCrushTriggerAssignment import SurfaceCrushTriggerAssignment
from .SurfaceFeatureAssignment import SurfaceFeatureAssignment
from .SurfaceFrictionAssignment import SurfaceFrictionAssignment
from .SurfaceOffsetAssignment import SurfaceOffsetAssignment
from .SurfaceThicknessAssignment import SurfaceThicknessAssignment
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class ContactExp(Interaction):
    """The ContactExp object defines the contact domain and associated properties during
    contact in an Abaqus/Explicit analysis.
    The ContactExp object is derived from the Interaction object.

    .. note:: 
        This object can be accessed by::

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

    #: A :py:class:`~abaqus.Interaction.SurfaceFeatureAssignment.SurfaceFeatureAssignment` object specifying the surface feature angle assignments in
    #: the contact domain.
    surfaceFeatureAssignments: SurfaceFeatureAssignment = SurfaceFeatureAssignment()

    #: A :py:class:`~abaqus.Interaction.SmoothingAssignment.SmoothingAssignment` object specifying the surface smoothing assignments in the contact
    #: domain.
    smoothingAssignments: SmoothingAssignment = SmoothingAssignment()

    #: A :py:class:`~abaqus.Interaction.MainSecondaryAssignment.MainSecondaryAssignment` object specifying the main-secondary assignments in the
    #: contact domain.
    #:
    #: .. versionchanged:: 2022
    #:     The attribute `masterSlaveAssignments` was renamed to `mainSecondaryAssignments`.
    mainSecondaryAssignments: MainSecondaryAssignment = MainSecondaryAssignment()

    #: A PolarityAssignments object specifying the polarity assignments in the contact domain.
    #:
    #: .. versionadded:: 2020
    #:     The `polarityAssignments` attribute was added.
    polarityAssignments: PolarityAssignments = PolarityAssignments()

    @typing.overload
    @abaqus_method_doc
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
        smoothingAssignments: SmoothingAssignment = None,
        surfaceCrushTriggerAssignments: SurfaceCrushTriggerAssignment = SurfaceCrushTriggerAssignment(),
        surfaceFrictionAssignments: SurfaceFrictionAssignment = SurfaceFrictionAssignment(),
        mainSecondaryAssignments: MainSecondaryAssignment = None,
        polarityAssignments: PolarityAssignments = PolarityAssignments(),
    ):
        """This method creates a ContactExp object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ContactExp

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which this contact interaction is created.
        useAllstar
            A Boolean specifying whether the contacting surface pair consists of all exterior faces,
            shell edges, beam segments, analytical rigid surfaces, and, when applicable, Eulerian
            material surfaces.
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
        smoothingAssignments
            A :py:class:`~abaqus.Interaction.SmoothingAssignment.SmoothingAssignment` object specifying the surface smoothing assignments in the contact
            domain.
        surfaceCrushTriggerAssignments
            A :py:class:`~abaqus.Interaction.SurfaceCrushTriggerAssignment.SurfaceCrushTriggerAssignment` object specifying the surface crush trigger assignments
            in the contact domain.

            .. versionadded:: 2021
                The `surfaceCrushTriggerAssignments` argument was added.
        surfaceFrictionAssignments
            A :py:class:`~abaqus.Interaction.SurfaceFrictionAssignment.SurfaceFrictionAssignment` object specifying the surface friction assignments in the
            contact domain.

            .. versionadded:: 2021
                The `surfaceFrictionAssignments` argument was added.
        mainSecondaryAssignments
            A :py:class:`~abaqus.Interaction.MainSecondaryAssignment.MainSecondaryAssignment` object specifying the main-secondary assignments in the
            contact domain.

            .. versionchanged:: 2022
                The argument `masterSlaveAssignments` was renamed to `mainSecondaryAssignments`.
        polarityAssignments
            A PolarityAssignments object specifying the polarity assignments in the contact domain.

            .. versionadded:: 2020
                The `polarityAssignments` argument was added.

        Returns
        -------
        ContactExp
            A :py:class:`~abaqus.Interaction.ContactExp.ContactExp` object.
        """
        super().__init__()

    @typing.overload
    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        globalSmoothing: Boolean = ON,
        surfaceCrushTriggerAssignments: SurfaceCrushTriggerAssignment = SurfaceCrushTriggerAssignment(),
        surfaceFrictionAssignments: SurfaceFrictionAssignment = SurfaceFrictionAssignment(),
        useAllstar: Boolean = OFF,
        includedPairs: SymbolicConstant = None,
        excludedPairs: SymbolicConstant = None,
        contactPropertyAssignments: SymbolicConstant = None,
        surfaceThicknessAssignments: typing.Union[SymbolicConstant, float] = ORIGINAL,
        surfaceOffsetAssignments: typing.Union[SymbolicConstant, float] = GLOBAL,
        surfaceFeatureAssignments: typing.Union[SymbolicConstant, float] = PERIMETER,
        smoothingAssignments: SymbolicConstant = None,
        mainSecondaryAssignments: SymbolicConstant = None,
        polarityAssignments: SymbolicConstant = None,
    ):
        """This method creates a ContactExp object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ContactExp

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which this contact interaction is created.
        globalSmoothing
            A Boolean specifying whether surface smoothing (geometric correction) is automatically
            applied to all eligible surfaces. The default value is ON.
        surfaceCrushTriggerAssignments
            A :py:class:`~abaqus.Interaction.SurfaceCrushTriggerAssignment.SurfaceCrushTriggerAssignment` object specifying the surface crush trigger assignments
            in the contact domain.

            .. versionadded:: 2021
                The `surfaceCrushTriggerAssignments` argument was added.
        surfaceFrictionAssignments
            A :py:class:`~abaqus.Interaction.SurfaceFrictionAssignment.SurfaceFrictionAssignment` object specifying the surface friction assignments in the
            contact domain.

            .. versionadded:: 2021
                The `surfaceFrictionAssignments` argument was added.
        useAllstar
            A Boolean specifying whether the contacting surface pair consists of all exterior faces,
            shell edges, beam segments, analytical rigid surfaces, and, when applicable, Eulerian
            material surfaces.
        includedPairs
            A sequence of pairs of Region objects or SymbolicConstants that specifies the surface
            pairs in contact. Possible values of the SymbolicConstants are ALLSTAR and SELF. This
            argument is valid only when **useAllstar** = OFF.
        excludedPairs
            A sequence of pairs of Region objects or SymbolicConstants that specify the surface
            pairs excluded from contact. Possible values of the SymbolicConstants are ALLSTAR and
            SELF.
        contactPropertyAssignments
            A sequence of tuples specifying the properties assigned to each surface pair. Each tuple
            contains three entries:
            - A :py:class:`~abaqus.Region.Region.Region` object or the SymbolicConstant GLOBAL.
            - A :py:class:`~abaqus.Region.Region.Region` object or the SymbolicConstant SELF.
            - A String specifying an InteractionProperty object associated with this pair of
              regions.
        surfaceThicknessAssignments
            A sequence of tuples specifying the surface thickness assignments in the contact domain.
            Each tuple contains three entries:
            - A region object or the SymbolicConstant GLOBAL specifying the surface to which the
              surface thickness is assigned.
            - A Float or a SymbolicConstant specifying the overriding thickness value to be used in
              the contact definition. Possible values of the SymbolicConstant are ORIGINAL or
            THINNING.
            - A Float specifying a scale factor that multiplies the thickness value specified in the
              second entry.
        surfaceOffsetAssignments
            A sequence of tuples specifying the surface offset fraction assignments in the contact
            domain. Each tuple contains two entries:
            - A region object or the SymbolicConstant GLOBAL specifying the surface to which the
              surface offset fraction is assigned.
            - A Float or a SymbolicConstant specifying the offset fraction value to be used in the
              contact definition. Possible values of the SymbolicConstant are ORIGINAL, SPOS, or SNEG.
        surfaceFeatureAssignments
            A sequence of tuples specifying the surface feature angle assignments in the contact
            domain. Each tuple contains two entries:
            - A region object or the SymbolicConstant GLOBAL specifying the surface to which the
              surface feature angle is assigned.
            - A Float or a SymbolicConstant specifying the overriding feature angle value to be used
              in the contact definition. Possible values of the SymbolicConstant are PERIMETER, ALL,
            PICKED, or NONE.
        smoothingAssignments
            A sequence of tuples specifying the surface smoothing assignments in the contact domain.
            Each tuple contains two entries:
            - A region object specifying the surface to which the smoothing option is assigned.
            - A SymbolicConstant specifying the smoothing option to be used in the contact
              definition. Possible values of the SymbolicConstant are NONE, REVOLUTION, SPHERICAL, or
            TOROIDAL.
        mainSecondaryAssignments
            A sequence of tuples specifying pure main-secondary assignments in the contact domain.
            Each tuple contains three entries:
            - A region object or the SymbolicConstant GLOBAL specifying the first surface that
              defines the main-secondary assignment.
            - A region object specifying the second surface in the main-secondary assignment
              definition.
            - A SymbolicConstant specifying the status of the first surface. Possible values are
              MAIN and SECONDARY.

            .. versionchanged:: 2022
                The argument `masterSlaveAssignments` was renamed to `mainSecondaryAssignments`.
        polarityAssignments
            A sequence of tuples specifying polarity assignments in the contact domain. Each tuple
            contains three entries:

            - A region object or the SymbolicConstant GLOBAL specifying the first surface that
              defines the polarity assignment.
            - A region object specifying the second surface in the polarity assignment definition.
            - A SymbolicConstant specifying the polarity of the second surface. Possible values are
              SPOS, SNEG, and TWO_SIDED.

              .. versionadded:: 2020
                    The `polarityAssignments` argument was added.

        Returns
        -------
        ContactExp
            A :py:class:`~abaqus.Interaction.ContactExp.ContactExp` object.
        """
        super().__init__()

    def __init__(self, *args, **kwargs):
        ...
