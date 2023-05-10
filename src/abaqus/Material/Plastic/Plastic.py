from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ...UtilityAndView.abaqusConstants import (
    CONSTANT,
    HALF_CYCLE,
    ISOTROPIC,
    OFF,
    Boolean,
)
from ...UtilityAndView.abaqusConstants import abaqusConstants as C
from .Metal.Annealing.AnnealTemperature import AnnealTemperature
from .Metal.Cyclic.CycledPlastic import CycledPlastic
from .Metal.Cyclic.CyclicHardening import CyclicHardening
from .Metal.ORNL.Ornl import Ornl
from .Metal.RateDependent.RateDependent import RateDependent
from .Potential import Potential
from .TensileFailure import TensileFailure


@abaqus_class_doc
class Plastic:
    r"""The Plastic object specifies a metal plasticity model.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].Plastic
            import odbMaterial
            session.odbs[name].materials[name].Plastic

        The table data for this object are:

        - If **hardening** = ISOTROPIC, or if **hardening** = COMBINED and **dataType** = HALF_CYCLE, the table data specify the following:

            - Yield stress.
            - Plastic strain.
            - Equivalent plastic strain rate, :math:`\dot{\bar{\varepsilon}} p l`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **hardening** = COMBINED and **dataType** = STABILIZED, the table data specify the following:

            - Yield stress.
            - Plastic strain.
            - Strain range, if the data depend on strain range.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **hardening** = COMBINED and **dataType** = PARAMETERS, the table data specify the following:

            - Yield stress at zero Plastic strain.
            - The first kinematic hardening parameter, :math:`C_{1}`.
            - The first kinematic hardening parameter, :math:`\gamma_{1}`.
            - If applicable, the second kinematic hardening parameter, :math:`C_{2}`.
            - If applicable, the second kinematic hardening parameter, :math:`\gamma_{2}`.
            - Etc.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **hardening** = KINEMATIC, the table data specify the following:

            - Yield stress.
            - Plastic strain.
            - Temperature, if the data depend on temperature.
        - If **hardening** = JOHNSON_COOK, the table data specify the following:

            - :math:`A`.
            - :math:`B`.
            - :math:`\mathrm{n}`.
            - :math:`\mathrm{m}`.
            - Melting temperature.
            - Transition temperature.
        - If **hardening** = USER, the table data specify the following:

            - Hardening properties.

        The corresponding analysis keywords are:

        - PLASTIC
    """

    #: A RateDependent object.
    rateDependent: RateDependent = RateDependent(((),))

    #: A Potential object.
    potential: Potential = Potential(((),))

    #: A CyclicHardening object.
    cyclicHardening: CyclicHardening = CyclicHardening(((),))

    #: An Ornl object.
    ornl: Ornl = Ornl()

    #: A CycledPlastic object.
    cycledPlastic: CycledPlastic = CycledPlastic(((),))

    #: An AnnealTemperature object.
    annealTemperature: AnnealTemperature = AnnealTemperature(((),))

    #: A TensileFailure object.
    tensileFailure: TensileFailure = TensileFailure()

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        hardening: Literal[C.COMBINED, C.JOHNSON_COOK, C.USER, C.ISOTROPIC, C.KINEMATIC] = ISOTROPIC,
        rate: Boolean = OFF,
        dataType: Literal[C.PARAMETERS, C.HALF_CYCLE, C.COMBINED, C.STABILIZED] = HALF_CYCLE,
        strainRangeDependency: Boolean = OFF,
        numBackstresses: int = 1,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        extrapolation: Literal[C.CONSTANT, C.LINEAR] = CONSTANT,
    ):
        """This method creates a Plastic object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].Plastic
                session.odbs[name].materials[name].Plastic

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        hardening
            A SymbolicConstant specifying the type of hardening. Possible values are ISOTROPIC,
            KINEMATIC, COMBINED, JOHNSON_COOK, and USER. The default value is ISOTROPIC.
        rate
            A Boolean specifying whether the data depend on rate. The default value is OFF.
        dataType
            A SymbolicConstant specifying the type of combined hardening. This argument is only
            valid if **hardening** = COMBINED. Possible values are HALF_CYCLE, PARAMETERS, and
            STABILIZED. The default value is HALF_CYCLE.
        strainRangeDependency
            A Boolean specifying whether the data depend on strain range. This argument is only
            valid if **hardening** = COMBINED and **dataType** = STABILIZED. The default value is OFF.
        numBackstresses
            An Int specifying the number of backstresses. This argument is only valid if
            **hardening** = COMBINED. The default value is 1.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        extrapolation
            A SymbolicConstant specifying the extrapolation method for the yield stress with respect
            to the equivalent plastic strain. This argument is valid only if hardening=ISOTROPIC.
            Possible values are CONSTANT and LINEAR . The default value is CONSTANT.

            .. versionadded:: 2022
                The ``extrapolation`` argument was added.

        Returns
        -------
        Plastic
            A Plastic object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the Plastic object.

        Raises
        ------
        RangeError
        """
        ...
