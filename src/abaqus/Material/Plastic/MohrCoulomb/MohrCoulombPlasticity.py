import typing
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .MohrCoulombHardening import MohrCoulombHardening
from .TensionCutOff import TensionCutOff
from ....UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class MohrCoulombPlasticity:
    r"""The MohrCoulombPlasticity object specifies the extended Mohr-Coulomb plasticity model.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].mohrCoulombPlasticity
            import odbMaterial
            session.odbs[name].materials[name].mohrCoulombPlasticity

        The table data for this object are:

        - Friction angle (given in degrees), :math:`\phi`, at high confining pressure
          in the :math:`p-R_{m c} q` plane.
        - Dilation angle, :math:`\psi`, at high confining pressure in the :math:`p-R_{m w} q` plane.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - MOHR COULOMB
    """

    #: A :py:class:`~abaqus.Material.Plastic.MohrCoulomb.MohrCoulombHardening.MohrCoulombHardening` object.
    mohrCoulombHardening: MohrCoulombHardening = MohrCoulombHardening(((),))

    #: A :py:class:`~abaqus.Material.Plastic.MohrCoulomb.TensionCutOff.TensionCutOff` object.
    tensionCutOff: TensionCutOff = TensionCutOff(((),))

    @abaqus_method_doc
    def __init__(
        self,
        table: tuple,
        deviatoricEccentricity: typing.Optional[float] = None,
        meridionalEccentricity: float = 0,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        useTensionCutoff: Boolean = OFF,
    ):
        r"""This method creates a MohrCoulombPlasticity object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].MohrCoulombPlasticity
                session.odbs[name].materials[name].MohrCoulombPlasticity

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        deviatoricEccentricity
            None or a Float specifying the flow potential eccentricity in the deviatoric plane, 
            :math:`e`; :math:`1 / 2 \leq e \leq 1.0`. If **deviatoricEccentricity** = None, Abaqus calculates the value using the
            specified Mohr-Coulomb angle of friction. The default value is None.
        meridionalEccentricity
            A Float specifying the flow potential eccentricity in the meridional plane, :math:`\epsilon`. The
            default value is 0.1.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        useTensionCutoff
            A Boolean specifying whether tension cutoff specification is needed. The default value
            is OFF.

        Returns
        -------
        MohrCoulombPlasticity
            A :py:class:`~abaqus.Material.Plastic.MohrCoulomb.MohrCoulombPlasticity.MohrCoulombPlasticity` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the MohrCoulombPlasticity object.

        Raises
        ------
        RangeError
        """
        ...
