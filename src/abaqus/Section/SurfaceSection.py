import typing
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .RebarLayers import RebarLayers
from .Section import Section
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class SurfaceSection(Section):
    """The SurfaceSection object defines the properties of a surface section.
    The SurfaceSection object is derived from the Section object.

    .. note:: 
        This object can be accessed by::

            import section
            mdb.models[name].sections[name]
            import odbSection
            session.odbs[name].sections[name]

        The corresponding analysis keywords are:

        - SURFACE SECTION
    """

    #: A :py:class:`~abaqus.Section.RebarLayers.RebarLayers` object specifying reinforcement properties.
    rebarLayers: typing.Optional[RebarLayers] = None

    #: A String specifying the repository key.
    name: str

    #: A Boolean specifying whether or not to use the value of **density**. The default value is
    #: OFF.
    useDensity: Boolean = OFF

    #: A Float specifying the value of density to apply to this section. The default value is
    #: 0.0.
    density: float = 0

    @abaqus_method_doc
    def __init__(self, name: str, useDensity: Boolean = OFF, density: float = 0):
        """This method creates a SurfaceSection object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].SurfaceSection
                session.odbs[name].SurfaceSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        useDensity
            A Boolean specifying whether or not to use the value of **density**. The default value is
            OFF.
        density
            A Float specifying the value of density to apply to this section. The default value is
            0.0.

        Returns
        -------
        SurfaceSection
            A :py:class:`~abaqus.Section.SurfaceSection.SurfaceSection` object.

        Raises
        ------
        RangeError and InvalidNameError
        """
        super().__init__()
