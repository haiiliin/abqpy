from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Section import Section


@abaqus_class_doc
class EulerianSection(Section):
    """The EulerianSection object defines the properties of a Eulerian section.
    The EulerianSection object is derived from the Section object.

    .. note::
        This object can be accessed by::

            import section
            mdb.models[name].sections[name]
            import odbSection
            session.odbs[name].sections[name]

        The corresponding analysis keywords are:

        - EULERIAN SECTION
    """

    #: A String specifying the repository key.
    name: str

    #: A String-to-String Dictionary specifying a dictionary mapping Material instance names to
    #: Material names. Internally the specified mapping gets sorted on Material instance name.
    data: str

    @abaqus_method_doc
    def __init__(self, name: str, data: str):
        """This method creates a EulerianSection object.

        .. note::
            This function can be accessed by::

                mdb.models[name].EulerianSection
                session.odbs[name].EulerianSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        data
            A String-to-String Dictionary specifying a dictionary mapping Material instance names to
            Material names. Internally the specified mapping gets sorted on Material instance name.

        Returns
        -------
        EulerianSection
            An :py:class:`~abaqus.Section.EulerianSection.EulerianSection` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the EulerianSection object."""
        ...
