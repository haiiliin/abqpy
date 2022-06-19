from abaqusConstants import *
from .CapCreepCohesion import CapCreepCohesion
from .CapCreepConsolidation import CapCreepConsolidation
from .CapHardening import CapHardening


class CapPlasticity:
    """The CapPlasticity object specifies the modified Drucker-Prager/Cap plasticity model.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].capPlasticity
        import odbMaterial
        session.odbs[name].materials[name].capPlasticity

    The table data for this object are:

    - Material cohesion, d, in the p–t plane (Abaqus/Standard) or in the p–q plane (Abaqus/Explicit).
    - Material angle of friction, β, in the p–t plane (Abaqus/Standard) or in the p–q plane (Abaqus/Explicit). Give the value in degrees.
    - Cap eccentricity parameter, RR. Its value must be greater than zero (typically 0.0 <R< 1.0).
    - Initial cap yield surface position, ε_vol^pl|0.
    - Transition surface radius parameter, αα. The default value is 0.0 (i.e., no transition surface).
    - (Not used in Abaqus/Explicit) K, the ratio of the flow stress in triaxial tension to the flow stress in triaxial compression. Possible values are 0.778 ≤K≤ 1.0. If the default value of 0.0 is accepted, Abaqus/Standard assumes K= 1.0.
    - Temperature, if the data depend on temperature.
    - Value of the first field variable, if the data depend on field variables.
    - Value of the second field variable.
    - Etc.

    The corresponding analysis keywords are:

    - CAP PLASTICITY

    """

    # A CapCreepCohesion object.
    capCreepCohesion: CapCreepCohesion = CapCreepCohesion(((),))

    # A CapCreepConsolidation object.
    capCreepConsolidation: CapCreepConsolidation = CapCreepConsolidation(((),))

    # A CapHardening object.
    capHardening: CapHardening = CapHardening(((),))

    def __init__(
        self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0
    ):
        """This method creates a CapPlasticity object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].materials[name].CapPlasticity
            session.odbs[name].materials[name].CapPlasticity

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
            A CapPlasticity object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self):
        """This method modifies the CapPlasticity object.

        Raises
        ------
        RangeError
        """
        pass
