from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Section import Section


@abaqus_class_doc
class PEGSection(Section):
    """The PEGSection object defines the properties of a solid section.
    The PEGSection object is derived from the Section object.

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

    #: A String specifying the name of the material.
    material: str

    #: A Float specifying the thickness of the section. Possible values are **thickness** >> 0.0.
    #: The default value is 1.0.
    thickness: float = 1

    #: A Float specifying the value of the x component of the angle between the bounding
    #: planes, ΔϕxΔ⁢ϕx. The default value is 0.0.
    wedgeAngle1: float = 0

    #: A Float specifying the value of the y component of the angle between the bounding
    #: planes, ΔϕyΔ⁢ϕy. The default value is 0.0.
    wedgeAngle2: float = 0

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        material: str,
        thickness: float = 1,
        wedgeAngle1: float = 0,
        wedgeAngle2: float = 0,
    ):
        """This method creates a PEGSection object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].PEGSection
                session.odbs[name].PEGSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        material
            A String specifying the name of the material.
        thickness
            A Float specifying the thickness of the section. Possible values are **thickness** >> 0.0.
            The default value is 1.0.
        wedgeAngle1
            A Float specifying the value of the x component of the angle between the bounding
            planes, ΔϕxΔ⁢ϕx. The default value is 0.0.
        wedgeAngle2
            A Float specifying the value of the y component of the angle between the bounding
            planes, ΔϕyΔ⁢ϕy. The default value is 0.0.

        Returns
        -------
        PEGSection
            A :py:class:`~abaqus.Section.PEGSection.PEGSection` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self, thickness: float = 1, wedgeAngle1: float = 0, wedgeAngle2: float = 0
    ):
        """This method modifies the PEGSection object.

        Parameters
        ----------
        thickness
            A Float specifying the thickness of the section. Possible values are **thickness** >> 0.0.
            The default value is 1.0.
        wedgeAngle1
            A Float specifying the value of the x component of the angle between the bounding
            planes, ΔϕxΔ⁢ϕx. The default value is 0.0.
        wedgeAngle2
            A Float specifying the value of the y component of the angle between the bounding
            planes, ΔϕyΔ⁢ϕy. The default value is 0.0.

        Raises
        ------
        RangeError
        """
        ...
