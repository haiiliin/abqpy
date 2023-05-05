from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .SolidSection import SolidSection


@abaqus_class_doc
class HomogeneousSolidSection(SolidSection):
    """The HomogeneousSolidSection object defines the properties of a solid section. The HomogeneousSolidSection
    object is derived from the SolidSection object.

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

    #: A Float specifying the thickness of the section. Possible values are None or greater
    #: than zero. The default value is 1.0.
    #:
    #: .. versionchanged:: 2018
    #:    The default value is now 1.0 instead of None.
    thickness: Optional[float] = None

    @abaqus_method_doc
    def __init__(self, name: str, material: str, thickness: Optional[float] = None) -> None:
        """This method creates a HomogeneousSolidSection object.

        .. note::
            This function can be accessed by::

                mdb.models[name].HomogeneousSolidSection
                session.odbs[name].HomogeneousSolidSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        material
            A String specifying the name of the material.
        thickness
            A Float specifying the thickness of the section. Possible values are None or greater
            than zero. The default value is 1.0.

            .. versionchanged:: 2018
                The default value is now 1.0 instead of None.

        Returns
        -------
        HomogeneousSolidSection
            A HomogeneousSolidSection object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, thickness: float = 1) -> None:
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
        ...
