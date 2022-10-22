from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Section import Section
from .SectionLayerArray import SectionLayerArray
from ..UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class CompositeSolidSection(Section):
    """The CompositeSolidSection object defines the properties of a composite solid section.
    The CompositeSolidSection object is derived from the Section object.

    .. note:: 
        This object can be accessed by::

            import section
            mdb.models[name].sections[name]
            import odbSection
            session.odbs[name].sections[name]

        The corresponding analysis keywords are:

        - SOLID SECTION
    """

    #: A String specifying the repository key.
    name: str

    #: A :py:class:`~abaqus.Section.SectionLayerArray.SectionLayerArray` object specifying the solid cross-section.
    layup: SectionLayerArray

    #: A Boolean specifying whether or not the layup should be made symmetric by the analysis.
    #: The default value is OFF.
    symmetric: Boolean = OFF

    #: A String specifying the layup name for this section. The default value is an empty
    #: string.
    layupName: str = ""

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        layup: SectionLayerArray,
        symmetric: Boolean = OFF,
        layupName: str = "",
    ):
        """This method creates a CompositeSolidSection object.

        .. note:: 
            This function can be accessed by::

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
        CompositeSolidSection
            A :py:class:`~abaqus.Section.CompositeSolidSection.CompositeSolidSection` object.
        """
        super().__init__()

    @abaqus_method_doc
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
        ...
