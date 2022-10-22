from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Section import Section
from ..UtilityAndView.SymbolicConstant import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import SOLVER_DEFAULT


@abaqus_class_doc
class CohesiveSection(Section):
    """The CohesiveSection object defines the properties of a cohesive section.
    The CohesiveSection object is derived from the Section object.

    .. note:: 
        This object can be accessed by::

            import section
            mdb.models[name].sections[name]
            import odbSection
            session.odbs[name].sections[name]

        The corresponding analysis keywords are:

        - COHESIVE SECTION
    """

    #: A String specifying the repository key.
    name: str

    #: A SymbolicConstant specifying the geometric assumption that defines the constitutive
    #: behavior of the cohesive elements. Possible values are TRACTION_SEPARATION, CONTINUUM,
    #: and GASKET.
    response: Literal[C.TRACTION_SEPARATION, C.CONTINUUM, C.GASKET]

    #: A String specifying the name of the material.
    material: str

    #: A SymbolicConstant specifying the method used to compute the initial thickness. Possible
    #: values are: SOLVER_DEFAULT, specifying that Abaqus will use the analysis product
    #: default; GEOMETRY, specifying that Abaqus will compute the thickness from the nodal
    #: coordinates of the elements. SPECIFY, specifying that Abaqus will use the value given for
    #: **initialThickness** The default value is SOLVER_DEFAULT.
    initialThicknessType: Literal[C.SOLVER_DEFAULT, C.GEOMETRY, C.SPECIFY] = SOLVER_DEFAULT

    #: A Float specifying the initial thickness for the section. The **initialThickness**
    #: argument applies only when **initialThicknessType** = SPECIFY. The default value is 1.0.
    initialThickness: float = 1

    #: None or a Float specifying the out-of-plane thickness for the section. The default value
    #: is None.
    outOfPlaneThickness: Optional[float] = None

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        response: Literal[C.TRACTION_SEPARATION, C.CONTINUUM, C.GASKET],
        material: str,
        initialThicknessType: Literal[
            C.SOLVER_DEFAULT, C.GEOMETRY, C.SPECIFY
        ] = SOLVER_DEFAULT,
        initialThickness: float = 1,
        outOfPlaneThickness: Optional[float] = None,
    ) -> None:
        """This method creates a CohesiveSection object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].CohesiveSection
                session.odbs[name].CohesiveSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        response
            A SymbolicConstant specifying the geometric assumption that defines the constitutive
            behavior of the cohesive elements. Possible values are TRACTION_SEPARATION, CONTINUUM,
            and GASKET.
        material
            A String specifying the name of the material.
        initialThicknessType
            A SymbolicConstant specifying the method used to compute the initial thickness. Possible
            values are:SOLVER_DEFAULT, specifying that Abaqus will use the analysis product
            defaultGEOMETRY, specifying that Abaqus will compute the thickness from the nodal
            coordinates of the elements.SPECIFY, specifying that Abaqus will use the value given for
            **initialThickness** The default value is SOLVER_DEFAULT.
        initialThickness
            A Float specifying the initial thickness for the section. The **initialThickness**
            argument applies only when **initialThicknessType** = SPECIFY. The default value is 1.0.
        outOfPlaneThickness
            None or a Float specifying the out-of-plane thickness for the section. The default value
            is None.

        Returns
        -------
        CohesiveSection
            A :py:class:`~abaqus.Section.CohesiveSection.CohesiveSection` object.

        Raises
        ------
        RangeError and InvalidNameError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        initialThicknessType: Literal[
            C.SOLVER_DEFAULT, C.GEOMETRY, C.SPECIFY
        ] = SOLVER_DEFAULT,
        initialThickness: float = 1,
        outOfPlaneThickness: Optional[float] = None,
    ) -> None:
        """This method modifies the CohesiveSection object.

        Parameters
        ----------
        initialThicknessType
            A SymbolicConstant specifying the method used to compute the initial thickness. Possible
            values are:SOLVER_DEFAULT, specifying that Abaqus will use the analysis product
            defaultGEOMETRY, specifying that Abaqus will compute the thickness from the nodal
            coordinates of the elements.SPECIFY, specifying that Abaqus will use the value given for
            **initialThickness** The default value is SOLVER_DEFAULT.
        initialThickness
            A Float specifying the initial thickness for the section. The **initialThickness**
            argument applies only when **initialThicknessType** = SPECIFY. The default value is 1.0.
        outOfPlaneThickness
            None or a Float specifying the out-of-plane thickness for the section. The default value
            is None.

        Raises
        ------
        RangeError
        """
        ...
