from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Inertia import Inertia
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class HeatCapacitance(Inertia):
    """The HeatCapacitance object defines point heat capacitance on a part or an assembly
    region.
    The HeatCapacitance object is derived from the Inertia object.

    .. note:: 
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].engineeringFeatures.inertias[name]
            import assembly
            mdb.models[name].rootAssembly.engineeringFeatures.inertias[name]

        The table data specify the following:
        
        - Heat capacitance magnitude, ρcVρ⁢c⁢V (density × specific heat × volume).
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - HEATCAP
    """

    #: A Boolean specifying whether the inertia is suppressed or not. The default value is OFF.
    suppressed: Boolean = OFF

    #: A String specifying the repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the heat capacitance is applied.
    region: Region

    #: A sequence of sequences of Floats specifying heat capacitance properties. The items in
    #: the table data are described below.
    table: tuple

    #: A Boolean specifying whether the data depend on temperature. The default value is OFF.
    temperatureDependency: Boolean = OFF

    #: An Int specifying the number of field variable dependencies. The default value is 0.
    dependencies: int = 0

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        table: tuple,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a HeatCapacitance object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].engineeringFeatures.HeatCapacitance
                mdb.models[name].rootAssembly.engineeringFeatures.HeatCapacitance

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the heat capacitance is applied.
        table
            A sequence of sequences of Floats specifying heat capacitance properties. The items in
            the table data are described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        HeatCapacitance
            A :py:class:`~abaqus.EngineeringFeature.HeatCapacitance.HeatCapacitance` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method modifies the HeatCapacitance object.

        Parameters
        ----------
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        """
        ...
