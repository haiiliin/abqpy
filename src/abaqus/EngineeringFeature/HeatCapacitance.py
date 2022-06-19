from abaqusConstants import *
from .Inertia import Inertia
from ..Region.Region import Region


class HeatCapacitance(Inertia):
    """The HeatCapacitance object defines point heat capacitance on a part or an assembly
    region.
    The HeatCapacitance object is derived from the Inertia object.

    Attributes
    ----------
    suppressed: Boolean
        A Boolean specifying whether the inertia is suppressed or not. The default value is OFF.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import part
        mdb.models[name].parts[name].engineeringFeatures.inertias[name]
        import assembly
        mdb.models[name].rootAssembly.engineeringFeatures.inertias[name]

        The table data for this object are:
        The table data specify the following:
            - Heat capacitance magnitude, ρcVρ⁢c⁢V (density × specific heat × volume).
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

    The corresponding analysis keywords are:

    - HEATCAP
    """

    # A Boolean specifying whether the inertia is suppressed or not. The default value is OFF.
    suppressed: Boolean = OFF

    def __init__(
        self,
        name: str,
        region: Region,
        table: tuple,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a HeatCapacitance object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].parts[name].engineeringFeatures.HeatCapacitance
            mdb.models[name].rootAssembly.engineeringFeatures.HeatCapacitance

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A Region object specifying the region to which the heat capacitance is applied.
        table
            A sequence of sequences of Floats specifying heat capacitance properties. The items in
            the table data are described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
            A HeatCapacitance object.
        """
        super().__init__()
        pass

    def setValues(self, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method modifies the HeatCapacitance object.

        Parameters
        ----------
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        """
        pass
