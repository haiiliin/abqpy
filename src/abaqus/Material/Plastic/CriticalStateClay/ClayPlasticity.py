from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ClayHardening import ClayHardening
from ....UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class ClayPlasticity:
    r"""The ClayPlasticity object specifies the extended Cam-clay plasticity model.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].clayPlasticity
            import odbMaterial
            session.odbs[name].materials[name].clayPlasticity

        The table data for this object are:

        - If **hardening** = EXPONENTIAL, the table data specify the following:
        
            - Logarithmic plastic bulk modulus, :math:`\lambda` (dimensionless).
            - Stress ratio at critical state, :math:`M`.
            - The initial yield surface size, :math:`a_{0}`.
            - :math:`\beta`, the parameter defining the size of the yield surface on the "wet" side of critical state.
            - :math:`K`, the ratio of the flow stress in triaxial tension to the flow stress in triaxial
              compression. :math:`0.778 \leq K \leq 1.0`. If the default value of :math:`0.0` is accepted, a 
              value of :math:`1.0` is assumed.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **hardening** = TABULAR, the table data specify the following:
        
            - Stress ratio at critical state, :math:`M`
            - The initial volumetric plastic strain, :math:`\left.\varepsilon_{\mathrm{vol}}^{p l}\right|_{0}`, 
              corresponding to :math:`\left.p_{c}\right|_{0}` according to the ClayHardening definition.
            - :math:`\beta`, the parameter defining the size of the yield surface on the "wet" side of critical state.
            - :math:`K`, the ratio of the flow stress in triaxial tension to the flow stress in triaxial compression. 
              :math:`0.778 \leq K \leq 1.0`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - CLAY PLASTICITY
    """

    #: A :py:class:`~abaqus.Material.Plastic.CriticalStateClay.ClayHardening.ClayHardening` object.
    clayHardening: ClayHardening = ClayHardening(((),))

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        intercept: Optional[float] = None,
        hardening: SymbolicConstant = EXPONENTIAL,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a ClayPlasticity object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].ClayPlasticity
                session.odbs[name].materials[name].ClayPlasticity

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        intercept
            None or a Float specifying :math:`e_1`, the intercept of the virgin consolidation line with the
            void ratio axis in a plot of void ratio versus the logarithm of pressure stress. The
            default value is None.This argument is valid only if **hardening** = EXPONENTIAL.
        hardening
            A SymbolicConstant specifying the type of hardening/softening definition. Possible
            values are EXPONENTIAL and TABULAR. The default value is EXPONENTIAL.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        ClayPlasticity
            A :py:class:`~abaqus.Material.Plastic.CriticalStateClay.ClayPlasticity.ClayPlasticity` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the ClayPlasticity object.

        Raises
        ------
        RangeError
        """
        ...
