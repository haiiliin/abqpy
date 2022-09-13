from .Inertia import Inertia
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import *
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class NonstructuralMass(Inertia):
    """The NonstructuralMass object defines the mass contribution from nonstructural features
    into the model.
    The NonstructuralMass object is derived from the Inertia object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import part
            mdb.models[name].parts[name].engineeringFeatures.inertias[name]
            import assembly
            mdb.models[name].rootAssembly.engineeringFeatures.inertias[name]

        The corresponding analysis keywords are:

        - NONSTRUCTURAL MASS
    """

    #: A Boolean specifying whether the inertia is suppressed or not. The default value is OFF.
    suppressed: Boolean = OFF

    #: A String specifying the repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the mass is applied.
    region: Region

    #: A SymbolicConstant specifying the units used to specify the nonstructural mass. Possible
    #: values are TOTAL_MASS, MASS_PER_VOLUME, MASS_PER_AREA, and MASS_PER_LENGTH.
    units: SymbolicConstant

    #: A Float specifying the mass magnitude.
    magnitude: float

    #: A SymbolicConstant specifying the distribution of the nonstructural mass. Possible
    #: values are MASS_PROPORTIONAL and VOLUME_PROPORTIONAL. The default value is
    #: MASS_PROPORTIONAL.The **distribution** argument applies only when **units** = TOTAL_MASS.
    distribution: SymbolicConstant = MASS_PROPORTIONAL

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        units: SymbolicConstant,
        magnitude: float,
        distribution: SymbolicConstant = MASS_PROPORTIONAL,
    ):
        """This method creates a NonstructuralMass object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].parts[name].engineeringFeatures.NonstructuralMass
                mdb.models[name].rootAssembly.engineeringFeatures.NonstructuralMass

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the mass is applied.
        units
            A SymbolicConstant specifying the units used to specify the nonstructural mass. Possible
            values are TOTAL_MASS, MASS_PER_VOLUME, MASS_PER_AREA, and MASS_PER_LENGTH.
        magnitude
            A Float specifying the mass magnitude.
        distribution
            A SymbolicConstant specifying the distribution of the nonstructural mass. Possible
            values are MASS_PROPORTIONAL and VOLUME_PROPORTIONAL. The default value is
            MASS_PROPORTIONAL.The **distribution** argument applies only when **units** = TOTAL_MASS.

        Returns
        -------
        NonstructuralMass
            A :py:class:`~abaqus.EngineeringFeature.NonstructuralMass.NonstructuralMass` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, distribution: SymbolicConstant = MASS_PROPORTIONAL):
        """This method modifies the NonstructuralMass object.

        Parameters
        ----------
        distribution
            A SymbolicConstant specifying the distribution of the nonstructural mass. Possible
            values are MASS_PROPORTIONAL and VOLUME_PROPORTIONAL. The default value is
            MASS_PROPORTIONAL.The **distribution** argument applies only when **units** = TOTAL_MASS.
        """
        ...
