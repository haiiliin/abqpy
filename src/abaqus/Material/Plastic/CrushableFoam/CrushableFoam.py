from abaqusConstants import *
from .CrushableFoamHardening import CrushableFoamHardening
from ..Metal.RateDependent.RateDependent import RateDependent


class CrushableFoam:
    """The CrushableFoam object specifies the crushable foam plasticity model.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].crushableFoam
        import odbMaterial
        session.odbs[name].materials[name].crushableFoam

    The table data for this object are:

    - If **hardening**=VOLUMETRIC, the table data specify the following:
        - Ratio, k, of initial yield stress in uniaxial compression, σc0, to initial yield stress in hydrostatic compression, p0cpc0; 0.0 <k< 3.0.
        - Ratio, kt, of yield stress in hydrostatic tension, pt, to initial yield stress in hydrostatic compression, pc0. The default value is 1.0.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    - If **hardening**=ISOTROPIC, the table data specify the following:
        - Ratio, k, of initial yield stress in uniaxial compression, σ0cσc0, to initial yield stress in hydrostatic compression, p00; 0.0 ≤k≤ 3.0.
        - Plastic Poisson's ratio.νpνp; -1≤νp≤0.5.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    The corresponding analysis keywords are:

    - CRUSHABLE FOAM

    """

    # A CrushableFoamHardening object.
    crushableFoamHardening: CrushableFoamHardening = CrushableFoamHardening(((),))

    # A RateDependent object.
    rateDependent: RateDependent = RateDependent(((),))

    def __init__(
        self,
        table: tuple,
        hardening: SymbolicConstant = VOLUMETRIC,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a CrushableFoam object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].materials[name].CrushableFoam
            session.odbs[name].materials[name].CrushableFoam

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        hardening
            A SymbolicConstant specifying the type of hardening/softening definition. Possible
            values are VOLUMETRIC and ISOTROPIC. The default value is VOLUMETRIC.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
            A CrushableFoam object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self):
        """This method modifies the CrushableFoam object.

        Raises
        ------
        RangeError
        """
        pass
