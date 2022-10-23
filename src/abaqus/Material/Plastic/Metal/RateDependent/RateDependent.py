from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .....UtilityAndView.abaqusConstants import Boolean, OFF, POWER_LAW
from .....UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class RateDependent:
    r"""The RateDependent object defines a rate-dependent viscoplastic model.

    .. note::
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].crushableFoam.rateDependent
            mdb.models[name].materials[name].druckerPrager.rateDependent
            mdb.models[name].materials[name].Plastic.rateDependent
            import odbMaterial
            session.odbs[name].materials[name].crushableFoam.rateDependent
            session.odbs[name].materials[name].druckerPrager.rateDependent
            session.odbs[name].materials[name].Plastic.rateDependent

        The table data for this object are:

        - If **type** = POWER_LAW, the table data specify the following:

            - :math:`D`.
            - :math:`n`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = YIELD_RATIO, the table data specify the following:

            - Yield stress ratio, :math:`R=\bar{\sigma} / \sigma^{0}`.
            - Equivalent plastic strain rate, :math:`\dot{\bar{\varepsilon}}^{p l}`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = JOHNSON_COOK, the table data specify the following:

            - :math:`C`.
            - :math:`\dot{\varepsilon}_{0}`.

        The corresponding analysis keywords are:

        - RATE DEPENDENT
    """

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        type: Literal[C.JOHNSON_COOK, C.POWER_LAW, C.YIELD_RATIO] = POWER_LAW,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a RateDependent object.

        .. note::
            This function can be accessed by::

                mdb.models[name].materials[name].crushableFoam.RateDependent
                mdb.models[name].materials[name].druckerPrager.RateDependent
                mdb.models[name].materials[name].Plastic.RateDependent
                session.odbs[name].materials[name].crushableFoam.RateDependent
                session.odbs[name].materials[name].druckerPrager.RateDependent
                session.odbs[name].materials[name].Plastic.RateDependent

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        type
            A SymbolicConstant specifying the type of rate-dependent data. Possible values are
            POWER_LAW, YIELD_RATIO, and JOHNSON_COOK. The default value is POWER_LAW.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        RateDependent
            A :py:class:`~abaqus.Material.Plastic.Metal.RateDependent.RateDependent.RateDependent` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the RateDependent object.

        Raises
        ------
        RangeError
        """
        ...
