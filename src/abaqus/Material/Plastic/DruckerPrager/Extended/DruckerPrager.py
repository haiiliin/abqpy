from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .....UtilityAndView.abaqusConstants import LINEAR, OFF, Boolean
from .....UtilityAndView.abaqusConstants import abaqusConstants as C
from ...Metal.RateDependent.RateDependent import RateDependent
from .DruckerPragerCreep import DruckerPragerCreep
from .DruckerPragerHardening import DruckerPragerHardening
from .TriaxialTestData import TriaxialTestData


@abaqus_class_doc
class DruckerPrager:
    r"""The DruckerPrager object specifies the extended Drucker-Prager plasticity model.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].druckerPrager
            import odbMaterial
            session.odbs[name].materials[name].druckerPrager

        The table data for this object are:

        - If **shearCriterion** = LINEAR (the only option allowed in an Abaqus/Explicit analysis), the table data specify the following:

            - Material angle of friction, :math:`\beta`, in the :math:`p-t` plane. Give the value in degrees.
            - :math:`K`, the ratio of the flow stress in triaxial tension to the flow stress in triaxial
              compression. :math:`0.778 \leq K \leq 1.0`. If the default value of :math:`0.0` is accepted, a
              value of :math:`1.0` is assumed.
            - Dilation angle, :math:`\psi`, in the :math:`p-t` plane. Give the value in degrees.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **shearCriterion** = HYPERBOLIC, the table data specify the following:

            - Material angle of friction, :math:`\beta`, at high confining pressure in the :math:`p-q` plane.
              Give the value in degrees.
            - Initial hydrostatic tension strength, :math:`\left.p_{t}\right|_{0}`.
            - Dilation angle, :math:`\psi`, at high confining pressure in the :math:`p-q` plane. Give the value
              in degrees.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **shearCriterion** = EXPONENTIAL, the table data specify the following:

            - Dilation angle, :math:`\psi`, at high confining pressure in the :math:`p-q` plane. Give
              the value in degrees.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - DRUCKER PRAGER
    """

    #: A DruckerPragerCreep object.
    druckerPragerCreep: DruckerPragerCreep = DruckerPragerCreep(((),))

    #: A DruckerPragerHardening object.
    druckerPragerHardening: DruckerPragerHardening = DruckerPragerHardening(((),))

    #: A RateDependent object.
    rateDependent: RateDependent = RateDependent(((),))

    #: A TriaxialTestData object.
    triaxialTestData: TriaxialTestData = TriaxialTestData(((),))

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        shearCriterion: Literal[C.EXPONENTIAL, C.HYPERBOLIC, C.LINEAR] = LINEAR,
        eccentricity: float = 0,
        testData: Boolean = OFF,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        r"""This method creates a DruckerPrager object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].DruckerPrager
                session.odbs[name].materials[name].DruckerPrager

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        shearCriterion
            A SymbolicConstant specifying the yield criterion. Possible values are LINEAR,
            HYPERBOLIC, and EXPONENTIAL. The default value is LINEAR.This argument applies only to
            Abaqus/Standard analyses. Only the linear Drucker-Prager model is available in
            Abaqus/Explicit analyses.
        eccentricity
            A Float specifying the flow potential eccentricity, :math:`\epsilon`, a small positive number that
            defines the rate at which the hyperbolic flow potential approaches its asymptote. The
            default value is 0.1.This argument applies only to Abaqus/Standard analyses.
        testData
            A Boolean specifying whether the material constants for the exponent model are to be
            computed by Abaqus/Standard from triaxial test data at different levels of confining
            pressure. The default value is OFF.This argument is valid only if
            **shearCriterion** = EXPONENTIAL.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        DruckerPrager
            A DruckerPrager object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the DruckerPrager object.

        Raises
        ------
        RangeError
        """
        ...
