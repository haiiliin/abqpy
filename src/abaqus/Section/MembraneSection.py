from typing import Optional
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .RebarLayers import RebarLayers
from .Section import Section
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class MembraneSection(Section):
    """The MembraneSection object defines the properties of a membrane section.
    The MembraneSection object is derived from the Section object.

    .. note:: 
        This object can be accessed by::

            import section
            mdb.models[name].sections[name]
            import odbSection
            session.odbs[name].sections[name]

        The corresponding analysis keywords are:

        - MEMBRANE SECTION
    """

    #: A :py:class:`~abaqus.Section.RebarLayers.RebarLayers` object specifying reinforcement properties.
    rebarLayers: Optional[RebarLayers] = None

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the material.
    material: str

    #: A Float specifying the thickness for the section. Possible values are **thickness** >>
    #: 0.0. The default value is 1.0.
    thickness: float = 1

    #: A SymbolicConstant specifying the distribution used for defining the thickness of the
    #: elements. Possible values are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default
    #: value is UNIFORM.
    thicknessType: SymbolicConstant = UNIFORM

    #: A SymbolicConstant specifying whether to use the default value for the Poisson's ratio.
    #: Possible values are:DEFAULT, specifying that the default value for the Poisson's ratio
    #: is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an
    #: Abaqus/Explicit analysis.VALUE, specifying that the Poisson's ratio used in the analysis
    #: is the value provided in **poisson**.The default value is DEFAULT.
    poissonDefinition: SymbolicConstant = DEFAULT

    #: A Float specifying the section Poisson's ratio. Possible values are −1.0 ≤ **poisson** ≤
    #: 0.5. This argument is valid only when **poissonDefinition** = VALUE. The default value is
    #: 0.5.
    poisson: float = 0

    #: A String specifying the name of the AnalyticalField or DiscreteField object used to
    #: define the thickness of the shell elements. The **thicknessField** argument applies only
    #: when **thicknessType** = ANALYTICAL_FIELD or **thicknessType** = DISCRETE_FIELD. The default
    #: value is an empty string.
    thicknessField: str = ""

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        material: str,
        thickness: float = 1,
        thicknessType: SymbolicConstant = UNIFORM,
        poissonDefinition: SymbolicConstant = DEFAULT,
        poisson: float = 0,
        thicknessField: str = "",
    ):
        """This method creates a MembraneSection object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].MembraneSection
                session.odbs[name].MembraneSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        material
            A String specifying the name of the material.
        thickness
            A Float specifying the thickness for the section. Possible values are **thickness** >>
            0.0. The default value is 1.0.
        thicknessType
            A SymbolicConstant specifying the distribution used for defining the thickness of the
            elements. Possible values are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default
            value is UNIFORM.
        poissonDefinition
            A SymbolicConstant specifying whether to use the default value for the Poisson's ratio.
            Possible values are:DEFAULT, specifying that the default value for the Poisson's ratio
            is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an
            Abaqus/Explicit analysis.VALUE, specifying that the Poisson's ratio used in the analysis
            is the value provided in **poisson**.The default value is DEFAULT.
        poisson
            A Float specifying the section Poisson's ratio. Possible values are −1.0 ≤ **poisson** ≤
            0.5. This argument is valid only when **poissonDefinition** = VALUE. The default value is
            0.5.
        thicknessField
            A String specifying the name of the AnalyticalField or DiscreteField object used to
            define the thickness of the shell elements. The **thicknessField** argument applies only
            when **thicknessType** = ANALYTICAL_FIELD or **thicknessType** = DISCRETE_FIELD. The default
            value is an empty string.

        Returns
        -------
        MembraneSection
            A :py:class:`~abaqus.Section.MembraneSection.MembraneSection` object.

        Raises
        ------
        RangeError and InvalidNameError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        thickness: float = 1,
        thicknessType: SymbolicConstant = UNIFORM,
        poissonDefinition: SymbolicConstant = DEFAULT,
        poisson: float = 0,
        thicknessField: str = "",
    ):
        """This method modifies the MembraneSection object.

        Parameters
        ----------
        thickness
            A Float specifying the thickness for the section. Possible values are **thickness** >>
            0.0. The default value is 1.0.
        thicknessType
            A SymbolicConstant specifying the distribution used for defining the thickness of the
            elements. Possible values are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default
            value is UNIFORM.
        poissonDefinition
            A SymbolicConstant specifying whether to use the default value for the Poisson's ratio.
            Possible values are:DEFAULT, specifying that the default value for the Poisson's ratio
            is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an
            Abaqus/Explicit analysis.VALUE, specifying that the Poisson's ratio used in the analysis
            is the value provided in **poisson**.The default value is DEFAULT.
        poisson
            A Float specifying the section Poisson's ratio. Possible values are −1.0 ≤ **poisson** ≤
            0.5. This argument is valid only when **poissonDefinition** = VALUE. The default value is
            0.5.
        thicknessField
            A String specifying the name of the AnalyticalField or DiscreteField object used to
            define the thickness of the shell elements. The **thicknessField** argument applies only
            when **thicknessType** = ANALYTICAL_FIELD or **thicknessType** = DISCRETE_FIELD. The default
            value is an empty string.

        Raises
        ------
        RangeError
        """
        ...
