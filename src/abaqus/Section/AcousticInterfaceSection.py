from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Section import Section


@abaqus_class_doc
class AcousticInterfaceSection(Section):
    """The AcousticInterfaceSection object defines the properties of an acoustic section.
    The AcousticInterfaceSection object is derived from the Section object.

    .. note::
        This object can be accessed by::

            import section
            mdb.models[name].sections[name]
            import odbSection
            session.odbs[name].sections[name]

        The corresponding analysis keywords are:

        - INTERFACE
    """

    #: A String specifying the repository key.
    name: str

    #: A Float specifying the thickness of the section. Possible values are **thickness** > 0.0.
    #: The default value is 1.0.
    thickness: float = 1

    @abaqus_method_doc
    def __init__(self, name: str, thickness: float = 1):
        """This method creates an AcousticInterfaceSection object.

        .. note::
            This function can be accessed by::

                mdb.models[name].AcousticInterfaceSection
                session.odbs[name].AcousticInterfaceSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        thickness
            A Float specifying the thickness of the section. Possible values are **thickness** > 0.0.
            The default value is 1.0.

        Returns
        -------
        AcousticInterfaceSection
            An :py:class:`~abaqus.Section.AcousticInterfaceSection.AcousticInterfaceSection` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, thickness: float = 1):
        """This method modifies the AcousticInterfaceSection object.

        Parameters
        ----------
        thickness
            A Float specifying the thickness of the section. Possible values are **thickness** > 0.0.
            The default value is 1.0.

        Raises
        ------
        RangeError
        """
        ...
