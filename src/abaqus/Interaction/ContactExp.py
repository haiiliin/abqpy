from typing import Union, overload, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ContactPropertyAssignment import ContactPropertyAssignment
from .Interaction import Interaction
from .MasterSlaveAssignment import MasterSlaveAssignment
from .RegionPairs import RegionPairs
from .SmoothingAssignment import SmoothingAssignment
from .SurfaceFeatureAssignment import SurfaceFeatureAssignment
from .SurfaceOffsetAssignment import SurfaceOffsetAssignment
from .SurfaceThicknessAssignment import SurfaceThicknessAssignment
from ..UtilityAndView.abaqusConstants import (Boolean, GLOBAL, OFF, ON, ORIGINAL, PERIMETER,
                                              SymbolicConstant)


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

    #: A :py:class:`~abaqus.Interaction.MasterSlaveAssignment.MasterSlaveAssignment` object specifying the master-slave assignments in the
    #: contact domain.
    masterSlaveAssignments: MasterSlaveAssignment = MasterSlaveAssignment()

    @overload
    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        useAllstar: Boolean = OFF,
        globalSmoothing: Boolean = ON,
        includedPairs: Optional[RegionPairs] = None, 
        excludedPairs: Optional[RegionPairs] = None, 
        contactPropertyAssignments: Optional[ContactPropertyAssignment] = None, 
        surfaceThicknessAssignments: Optional[SurfaceThicknessAssignment] = None, 
        surfaceOffsetAssignments: Optional[SurfaceOffsetAssignment] = None, 
        surfaceFeatureAssignments: Optional[SurfaceFeatureAssignment] = None,
        smoothingAssignments: Optional[SmoothingAssignment] = None, 
        masterSlaveAssignments: Optional[MasterSlaveAssignment] = None,
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
        masterSlaveAssignments
            A :py:class:`~abaqus.Interaction.MasterSlaveAssignment.MasterSlaveAssignment` object specifying the main-secondary assignments in the
            contact domain.

        Returns
        -------
        ContactExp
            A :py:class:`~abaqus.Interaction.ContactExp.ContactExp` object.
        """
        super().__init__()

    @overload
    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        createStepName: str,
        globalSmoothing: Boolean = ON,
        useAllstar: Boolean = OFF,
        includedPairs: Optional[SymbolicConstant] = None,
        excludedPairs: Optional[SymbolicConstant] = None,
        contactPropertyAssignments: Optional[SymbolicConstant] = None,
        surfaceThicknessAssignments: Union[SymbolicConstant, float] = ORIGINAL,
        surfaceOffsetAssignments: Union[SymbolicConstant, float] = GLOBAL,
        surfaceFeatureAssignments: Union[SymbolicConstant, float] = PERIMETER,
        smoothingAssignments: Optional[SymbolicConstant] = None,
        masterSlaveAssignments: Optional[SymbolicConstant] = None,
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
        masterSlaveAssignments
            A sequence of tuples specifying pure master-slave assignments in the contact domain.
            Each tuple contains three entries:
            - A region object or the SymbolicConstant GLOBAL specifying the first surface that
              defines the master-slave assignment.
            - A region object specifying the second surface in the master-slave assignment
              definition.
            - A SymbolicConstant specifying the status of the first surface. Possible values are
              MAIN and SECONDARY.

        Returns
        -------
        ContactExp
            A :py:class:`~abaqus.Interaction.ContactExp.ContactExp` object.
        """
        super().__init__()

    def __init__(self, *args, **kwargs):
        ...
