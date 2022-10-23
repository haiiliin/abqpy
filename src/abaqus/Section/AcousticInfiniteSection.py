from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Section import Section


@abaqus_class_doc
class AcousticInfiniteSection(Section):
    """The AcousticInfiniteSection object defines the properties of an acoustic section.
    The AcousticInfiniteSection object is derived from the Section object.

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

    #: An Int specifying the number of ninth-order polynomials that will be used to resolve the
    #: variation of the acoustic field in the infinite direction. Possible values are 0 <<
    #: **order** ≤ 10. The default value is 10.
    order: int = 10

    @abaqus_method_doc
    def __init__(self, name: str, material: str, thickness: float = 1, order: int = 10):
        """This method creates an AcousticInfiniteSection object.

        .. note::
            This function can be accessed by::

                mdb.models[name].AcousticInfiniteSection
                session.odbs[name].AcousticInfiniteSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        material
            A String specifying the name of the material.
        thickness
            A Float specifying the thickness of the section. Possible values are **thickness** >> 0.0.
            The default value is 1.0.
        order
            An Int specifying the number of ninth-order polynomials that will be used to resolve the
            variation of the acoustic field in the infinite direction. Possible values are 0 <<
            **order** ≤ 10. The default value is 10.

        Returns
        -------
        AcousticInfiniteSection
            An :py:class:`~abaqus.Section.AcousticInfiniteSection.AcousticInfiniteSection` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, thickness: float = 1, order: int = 10):
        """This method modifies the AcousticInfiniteSection object.

        Parameters
        ----------
        thickness
            A Float specifying the thickness of the section. Possible values are **thickness** >> 0.0.
            The default value is 1.0.
        order
            An Int specifying the number of ninth-order polynomials that will be used to resolve the
            variation of the acoustic field in the infinite direction. Possible values are 0 <<
            **order** ≤ 10. The default value is 10.

        Raises
        ------
        RangeError
        """
        ...
