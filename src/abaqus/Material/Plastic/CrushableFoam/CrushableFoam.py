from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .CrushableFoamHardening import CrushableFoamHardening
from ..Metal.RateDependent.RateDependent import RateDependent
from ....UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class CrushableFoam:
    r"""The CrushableFoam object specifies the crushable foam plasticity model.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].crushableFoam
            import odbMaterial
            session.odbs[name].materials[name].crushableFoam

        The table data for this object are:

        - If **hardening** = VOLUMETRIC, the table data specify the following:
        
            - Ratio, :math:`k`, of initial yield stress in uniaxial compression, :math:`\sigma_{c}^{0}`, 
              to initial yield stress in hydrostatic compression, :math:`p_{c}^{0} ; 0.0<k<3.0`.
            - Ratio, :math:`k_{t}`, of yield stress in hydrostatic tension, :math:`p_{t}`, to initial 
              yield stress in hydrostatic compression, :math:`p_{c}^{0}`. The default value is :math:`1.0`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **hardening** = ISOTROPIC, the table data specify the following:
        
            - Ratio, :math:`k`, of initial yield stress in uniaxial compression, :math:`\sigma_{c}^{0}`, 
              to initial yield stress in hydrostatic compression, :math:`p_{c}^{0}`; :math:`0.0 \leq k \leq 3.0`
            - Plastic Poisson's ratio. :math:`\nu_{p} ;-1 \leq \nu_{p} \leq 0.5`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - CRUSHABLE FOAM
    """

    #: A :py:class:`~abaqus.Material.Plastic.CrushableFoam.CrushableFoamHardening.CrushableFoamHardening` object.
    crushableFoamHardening: CrushableFoamHardening = CrushableFoamHardening(((),))

    #: A :py:class:`~abaqus.Material.Plastic.Metal.RateDependent.RateDependent.RateDependent` object.
    rateDependent: RateDependent = RateDependent(((),))

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        hardening: SymbolicConstant = VOLUMETRIC,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a CrushableFoam object.

        .. note:: 
            This function can be accessed by::

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
        CrushableFoam
            A :py:class:`~abaqus.Material.Plastic.CrushableFoam.CrushableFoam.CrushableFoam` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the CrushableFoam object.

        Raises
        ------
        RangeError
        """
        ...
