from abaqusConstants import *
from .RebarLayers import RebarLayers
from .Section import Section


class SurfaceSection(Section):
    """The SurfaceSection object defines the properties of a surface section.
    The SurfaceSection object is derived from the Section object.

    Attributes
    ----------
    rebarLayers: RebarLayers
        A :py:class:`~abaqus.Section.RebarLayers.RebarLayers` object specifying reinforcement properties.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import section
        mdb.models[name].sections[name]
        import odbSection
        session.odbs[name].sections[name]

    The corresponding analysis keywords are:

    - SURFACE SECTION
    """

    # A RebarLayers object specifying reinforcement properties.
    rebarLayers: RebarLayers = None

    def __init__(self, name: str, useDensity: Boolean = OFF, density: float = 0):
        """This method creates a SurfaceSection object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

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
        A SurfaceSection object.

        Raises
        ------
        RangeError and InvalidNameError
        """
        super().__init__()
        pass
