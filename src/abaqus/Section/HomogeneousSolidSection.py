from .SolidSection import SolidSection


class HomogeneousSolidSection(SolidSection):
    """The HomogeneousSolidSection object defines the properties of a solid section.
    The HomogeneousSolidSection object is derived from the SolidSection object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import section
            mdb.models[name].sections[name]
            import odbSection
            session.odbs[name].sections[name]

        The corresponding analysis keywords are:

        - SOLID SECTION
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the material.
    material: str

    #: None or a Float specifying the thickness of the section. Possible values
    #: are None or a floating point value such that thickness >  0.0. The default value is None.
    thickness: float = None

    def __init__(self, name: str, material: str, thickness: float = None):
        """This method creates a HomogeneousSolidSection object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].HomogeneousSolidSection
                session.odbs[name].HomogeneousSolidSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        material
            A String specifying the name of the material.
        thickness
            None or a Float specifying the thickness of the section. Possible values
            are None or a floating point value such that thickness >  0.0. The default value is None.

        Returns
        -------
        HomogeneousSolidSection
            A :py:class:`~abaqus.Section.HomogeneousSolidSection.HomogeneousSolidSection` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        super().__init__()
        pass

    def setValues(self, thickness: float = 1):
        """This method modifies the HomogeneousSolidSection object.

        Parameters
        ----------
        thickness
            A Float specifying the thickness of the section. Possible values are None or greater
            than zero. The default value is 1.0.

        Raises
        ------
        RangeError
        """
        pass
