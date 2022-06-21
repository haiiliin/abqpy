from abaqusConstants import *
from .Section import Section
from .SectionLayerArray import SectionLayerArray


class CompositeSolidSection(Section):
    """The CompositeSolidSection object defines the properties of a composite solid section.
    The CompositeSolidSection object is derived from the Section object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import section
        mdb.models[name].sections[name]
        import odbSection
        session.odbs[name].sections[name]

    The corresponding analysis keywords are:

    - SOLID SECTION
    """

    def __init__(
        self,
        name: str,
        layup: SectionLayerArray,
        symmetric: Boolean = OFF,
        layupName: str = "",
    ):
        """This method creates a CompositeSolidSection object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].CompositeSolidSection
            session.odbs[name].CompositeSolidSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        layup
            A :py:class:`~abaqus.Section.SectionLayerArray.SectionLayerArray` object specifying the solid cross-section.
        symmetric
            A Boolean specifying whether or not the layup should be made symmetric by the analysis.
            The default value is OFF.
        layupName
            A String specifying the layup name for this section. The default value is an empty
            string.

        Returns
        -------
        A :py:class:`~abaqus.Section.CompositeSolidSection.CompositeSolidSection` object.
        """
        super().__init__()
        pass

    def setValues(self, symmetric: Boolean = OFF, layupName: str = ""):
        """This method modifies the CompositeSolidSection object.

        Parameters
        ----------
        symmetric
            A Boolean specifying whether or not the layup should be made symmetric by the analysis.
            The default value is OFF.
        layupName
            A String specifying the layup name for this section. The default value is an empty
            string.
        """
        pass
